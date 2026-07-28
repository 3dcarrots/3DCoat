import asyncio
import threading
import queue
import numpy as np
import sounddevice as sd
import os
import sys
import json
import base64
import io
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client
from mcp.client.streamable_http import streamablehttp_client
from google import genai
from google.genai import types

class AudioServiceThread(threading.Thread):
    def __init__(self, ui_instance, model="gemini-2.0-flash"):
        super().__init__(daemon=True)
        self.ui = ui_instance
        self.model = model
        
        # Asyncio event loop running in this thread
        self.loop = None
        
        # We need an active API key. Assuming it's set in the environment for now, 
        # or it could be added in the UI later. 
        self.client = None
        self.session = None
        
        # Audio configuration required by Gemini Live
        self.audio_in_rate = 16000
        self.audio_out_rate = 24000
        self.audio_channels = 1
        self.audio_format = 'int16'
        
        # Queues for audio handling
        self.audio_in_queue = asyncio.Queue()
        self.audio_out_queue = queue.Queue()
        self.audio_out_buffer = bytearray()
        
        # MCP Variables
        self.mcp_session = None
        self.mcp_client = None
        self.mcp_tools = []
        self.gemini_tools = []
        
        self.is_running = True
        self.is_mic_active = False
        self.is_speaker_active = True
        self.is_tool_call_pending = False
        self.mic_stream = None
        self.speaker_stream = None
        
    def get_live_models(self, api_key: str):
        """Fetches and categorizes available models for Gemini Live"""
        try:
            client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta', 'timeout': 120000})
            
            categorized_models = {
                "Fast": [],
                "Thinking": [],
                "Pro": [],
                "Other": []
            }
            
            for m in client.models.list():
                methods = []
                if hasattr(m, "supported_generation_methods"):
                    methods = m.supported_generation_methods or []
                elif isinstance(m, dict):
                    methods = m.get("supported_generation_methods", [])
                    
                name = m.name if hasattr(m, 'name') else m.get('name', '')
                model_id = name.replace("models/", "")
                
                # Step 3.1: Check method or allowlist
                has_bidi = "bidiGenerateContent" in methods or model_id in [
                    "gemini-2.5-flash-native-audio-latest"
                ]
                
                if not has_bidi:
                    continue
                
                desc = m.description if hasattr(m, 'description') else m.get('description', 'ÐžÐ¿Ð¸Ñ Ð½ÐµÐ´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ð¸Ð¹')
                model_desc = f"{model_id} ({desc})"
                
                # Categorize based on lexical patterns
                if "thinking" in model_id.lower():
                    categorized_models["Thinking"].append((model_id, model_desc))
                elif "pro" in model_id.lower():
                    categorized_models["Pro"].append((model_id, model_desc))
                    if "2.5-pro" in model_id.lower() or "3-pro" in model_id.lower():
                         categorized_models["Thinking"].append((model_id, model_desc))
                elif "flash" in model_id.lower():
                    categorized_models["Fast"].append((model_id, model_desc))
                else:
                    categorized_models["Other"].append((model_id, model_desc))
                    
            for category in categorized_models:
                categorized_models[category].sort(key=lambda x: x[0])
                
            # Step 3.2: Fallback if no Live models found
            if not any(categorized_models.values()):
                raise ValueError("0 Live-compatible models found. Falling back to default list.")
                
            return categorized_models
            
        except Exception as e:
            msg = str(e) if "0 Live-compatible models" in str(e) else f"Failed to fetch models: {e}"
            self.ui.log_message.emit(f"> <b style='color:orange;'>Info:</b> {msg}")
            return {
                "Fast": [
                    ("gemini-live-2.5-flash-native-audio", "Gemini Live 2.5 Flash Native Audio (GA)"),
                    ("gemini-2.5-flash-native-audio-latest", "Gemini 2.5 Flash Native Audio (Latest Alias)"),
                    ("gemini-3.1-flash-live-preview", "Gemini 3.1 Flash Live Preview")
                ],
                "Thinking": [],
                "Pro": [("gemini-3.1-pro-preview", "Gemini 3.1 Pro Preview (Fallback)")],
                "Other": []
            }
            
    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        
        # Initialize audio streams
        try:
            self.speaker_stream = sd.OutputStream(
                samplerate=self.audio_out_rate,
                channels=self.audio_channels,
                dtype=self.audio_format,
                latency='high',
                blocksize=4096,
                callback=self._audio_out_callback
            )
            self.speaker_stream.start()
        except Exception as e:
            self.ui.log_message.emit(f"> Speaker init failed: {e}")
            
        self.ui.log_message.emit("> Background service started successfully.")
        
        # Run the loop forever until stopped
        try:
            self.loop.run_until_complete(self._main_loop())
        except Exception as e:
            self.ui.log_message.emit(f"Service crashed: {str(e)}")
            
    async def _main_loop(self):
        while self.is_running:
            await asyncio.sleep(0.1)

    def stop(self):
        self.is_running = False
        
        if self.mcp_session:
            # Note: We don't have an easy way to gently close the stdio context without async contextlib
            pass
            
        if self.mic_stream:
            self.mic_stream.stop()
            self.mic_stream.close()
            
        if self.speaker_stream:
            self.speaker_stream.stop()
            self.speaker_stream.close()
            
        if self.loop and self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)
            
    # ------ Audio Callbacks ------
    
    def _audio_in_callback(self, indata, frames, time_info, status):
        """Called by sounddevice when mic has data"""
        # CRITICAL FIX: The Input Gating Pattern
        if getattr(self, 'is_tool_call_pending', False):
            return # Drop audio chunk to prevent race condition and 1008 error
            
        if status:
            pass # Handle status if needed
            
        if self.is_mic_active and self.loop:
            try:
                if hasattr(self, 'ui') and hasattr(self.ui, 'user_audio_level_signal'):
                    import numpy as np
                    audio_np = np.frombuffer(indata, dtype=np.int16).astype(np.float32)
                    if len(audio_np) > 0:
                        rms = np.sqrt(np.mean(np.square(audio_np)))
                        normalized_amp = min(1.0, (rms / 32768.0) * 8.0)
                        self.ui.user_audio_level_signal.emit(normalized_amp)
            except Exception:
                pass
                
            self.loop.call_soon_threadsafe(
                self.audio_in_queue.put_nowait, indata.tobytes()
            )

    def _audio_out_callback(self, outdata, frames, time_info, status):
        """Called by sounddevice when speaker needs data"""
        bytes_needed = frames * 2 * self.audio_channels
        while len(self.audio_out_buffer) < bytes_needed:
            try:
                data = self.audio_out_queue.get_nowait()
                if self.is_speaker_active:
                    self.audio_out_buffer.extend(data)
            except queue.Empty:
                break
                
        if not self.is_speaker_active:
            self.audio_out_buffer.clear()
            outdata[:] = 0
            if hasattr(self, 'ui') and hasattr(self.ui, 'audio_level_signal'):
                try:
                    self.ui.audio_level_signal.emit(0.0)
                except Exception:
                    pass
            return
                
        if len(self.audio_out_buffer) >= bytes_needed:
            chunk = self.audio_out_buffer[:bytes_needed]
            del self.audio_out_buffer[:bytes_needed]
            outdata[:] = np.frombuffer(chunk, dtype=np.int16).reshape(-1, 1)
        else:
            if len(self.audio_out_buffer) >= 2:
                valid_bytes = (len(self.audio_out_buffer) // 2) * 2
                chunk = self.audio_out_buffer[:valid_bytes]
                del self.audio_out_buffer[:valid_bytes]
                samples = len(chunk) // 2
                outdata[:samples] = np.frombuffer(chunk, dtype=np.int16).reshape(-1, 1)
                outdata[samples:] = 0
            else:
                outdata[:] = 0
                
        # Emit audio amplitude based on actual playback buffer
        try:
            if hasattr(self, 'ui') and hasattr(self.ui, 'audio_level_signal'):
                audio_np = np.frombuffer(outdata, dtype=np.int16).astype(np.float32)
                if len(audio_np) > 0:
                    rms = np.sqrt(np.mean(np.square(audio_np)))
                    normalized_amp = min(1.0, (rms / 32768.0) * 8.0)
                    # We can use QTimer.singleShot or signal to safely emit across threads to UI
                    self.ui.audio_level_signal.emit(normalized_amp)
                else:
                    self.ui.audio_level_signal.emit(0.0)
        except Exception:
            pass
            
    # ------ Thread-Safe API for UI ------
            
    def start_session(self, api_key: str):
        """Called by UI to connect to Gemini."""
        if not self.loop:
            return
            
        try:
            self.client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta', 'timeout': 120000})
        except Exception as e:
            self.ui.log_message.emit(f"> <b style='color:red;'>Client init failed:</b> {e}")
            return
            
        self.is_mic_active = False
        if not self.mic_stream:
            try:
                self.mic_stream = sd.InputStream(
                    samplerate=self.audio_in_rate,
                    channels=self.audio_channels,
                    dtype=self.audio_format,
                    latency='high',
                    blocksize=4096,
                    callback=self._audio_in_callback
                )
                self.mic_stream.start()
            except Exception as e:
                self.ui.log_message.emit(f"> Mic init failed: {e}")
                
        asyncio.run_coroutine_threadsafe(self._connect_to_gemini(), self.loop)
        
    def end_session(self):
        """Called by UI to disconnect."""
        self.is_mic_active = False
        if self.mic_stream:
            self.mic_stream.stop()
            self.mic_stream.close()
            self.mic_stream = None
            
        if not self.loop:
            return
        asyncio.run_coroutine_threadsafe(self._disconnect_from_gemini(), self.loop)
        
    def send_text_message(self, text, image_bytes=None, mime_type=None):
        if not self.loop:
            return
        asyncio.run_coroutine_threadsafe(self._send_text(text, image_bytes, mime_type), self.loop)

    # ------ Coroutines running in Service Thread ------

    async def _setup_mcp(self):
        """Initializes the connection to the 3DCoat MCP server"""
        try:
            self.ui.log_message.emit("> Waiting for local 3DCoat MCP Server to initialize...")
            
            import json
            import os
            import asyncio
            from contextlib import AsyncExitStack
            
            mcp_url = None
            mcp_type = "sse" # default
            extension_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            config_paths = [
                os.path.expanduser(r'~/.gemini/antigravity/mcp_config.json'),
                os.path.join(extension_root, ".cursor", "mcp.json"),
                os.path.join(extension_root, ".windsurf", "mcp.json"),
            ]
            
            # Wait until the URL is available
            for _ in range(60): # wait up to 60 seconds
                for path in config_paths:
                    if os.path.exists(path):
                        try:
                            with open(path, "r", encoding="utf-8") as f:
                                config = json.load(f)
                                mcp_conf = config.get("mcpServers", {}).get("3dcoat-live", {})
                                # Prefer serverUrl if available (Antigravity's HTTP proxy), else url
                                mcp_url = mcp_conf.get("serverUrl") or mcp_conf.get("url")
                                mcp_type = mcp_conf.get("type", "sse")
                                if mcp_url: break
                        except Exception as e:
                            pass
                if mcp_url:
                    break
                await asyncio.sleep(1)
                
            if not mcp_url:
                raise Exception("Could not find 3DCoat MCP Server URL in config. Ensure AITools is running.")
            
            # Use retry loop in case the Server is still starting
            for attempt in range(5):
                try:
                    self.ui.log_message.emit(f"> Connecting to {mcp_type.upper()} MCP at {mcp_url} (Attempt {attempt+1}/5)...")
                    
                    if getattr(self, "exit_stack", None) is None:
                        self.exit_stack = AsyncExitStack()
                    
                    # Choose transport based on type
                    if mcp_type == "http":
                        transport = await self.exit_stack.enter_async_context(streamablehttp_client(mcp_url))
                        read, write = transport[0], transport[1]
                    else:
                        transport = await self.exit_stack.enter_async_context(sse_client(mcp_url))
                        read, write = transport
                    self.mcp_session = await self.exit_stack.enter_async_context(ClientSession(read, write))
                    
                    await self.mcp_session.initialize()
                    self.ui.log_message.emit("> MCP connection established.")
                    break
                except Exception as e:
                    if getattr(self, "exit_stack", None):
                        await self.exit_stack.aclose()
                        self.exit_stack = AsyncExitStack()
                    if attempt == 4:
                        raise e
                    await asyncio.sleep(2)
            
            # Fetch tools
            tools_response = await self.mcp_session.list_tools()
            self.mcp_tools = tools_response.tools
            
            # Create a reverse map to resolve real MCP Tool Names from Gemini
            self.mcp_tool_map = {}
            for t in self.mcp_tools:
                gemini_safe_name = t.name.replace("-", "_") if t.name else ""
                self.mcp_tool_map[gemini_safe_name] = t.name
            
            self.ui.log_message.emit(f"> Loaded {len(self.mcp_tools)} tools from 3DCoat MCP.")
            
            # Convert to Gemini FunctionDeclarations
            self.gemini_tools = [self._mcp_tool_to_gemini(t) for t in self.mcp_tools]
            
        except Exception as e:
            self.ui.log_message.emit(f"> <b style='color:red;'>Failed to connect to MCP:</b> {e}")
            self.mcp_session = None

    def _mcp_tool_to_gemini(self, mcp_tool):
        """Converts an MCP Tool definition to Gemini FunctionDeclaration"""
        
        # Simple schema conversion (handles basic type mapping and drops invalid keys)
        def convert_schema(schema):
            if not schema or not isinstance(schema, dict):
                return None
                
            tType = types.Type.OBJECT
            s_type = schema.get("type", "object")
            if s_type == "string": tType = types.Type.STRING
            elif s_type == "integer": tType = types.Type.INTEGER
            elif s_type == "number": tType = types.Type.NUMBER
            elif s_type == "boolean": tType = types.Type.BOOLEAN
            elif s_type == "array": tType = types.Type.ARRAY
            
            props = {}
            if "properties" in schema and isinstance(schema["properties"], dict):
                for k, v in schema["properties"].items():
                    converted = convert_schema(v)
                    if converted:
                        props[k] = converted
                        
            items = None
            if "items" in schema and isinstance(schema["items"], dict):
                items = convert_schema(schema["items"])
                
            req = schema.get("required", [])
            if not isinstance(req, list):
                req = []
                
            return types.Schema(
                type=tType,
                description=schema.get("description", ""),
                properties=props if props else None,
                required=req if req else None,
                items=items
            )
            
        # Coerce the top-level schema to always be a valid type: object
        input_schema = mcp_tool.inputSchema if mcp_tool.inputSchema else {}
        if not isinstance(input_schema, dict):
            input_schema = {}
            
        if "type" not in input_schema or input_schema["type"] != "object":
            input_schema["type"] = "object"
            
        converted_params = convert_schema(input_schema)
        
        # Ensure name exists and is formatted correctly
        tool_name = mcp_tool.name.replace("-", "_") if mcp_tool.name else "unnamed_tool"
            
        return types.FunctionDeclaration(
            name=tool_name,
            description=mcp_tool.description or "",
            parameters=converted_params if converted_params and converted_params.properties else None
        )

    async def _connect_to_gemini(self):
        from contextlib import AsyncExitStack
        try:
            if getattr(self, "exit_stack", None):
                await self.exit_stack.aclose()
            self.exit_stack = AsyncExitStack()
            
            await self._setup_mcp()
        
            self.ui.log_message.emit("> Establishing connection to Gemini Live...")
            
            # --- Model Fallback System ---
            if not self.model:
                self.model = "gemini-2.5-flash-native-audio-latest"
                
            try:
                model_info = self.client.models.get(model=self.model)
                methods = []
                if hasattr(model_info, "supported_generation_methods"):
                    methods = model_info.supported_generation_methods or []
                elif isinstance(model_info, dict):
                    methods = model_info.get("supported_generation_methods", [])
                
                has_bidi = "bidiGenerateContent" in methods or self.model in [
                    "gemini-2.5-flash-native-audio-latest"
                ]
                
                if not has_bidi:
                    self.ui.log_message.emit(f"> <b style='color:orange;'>Warning:</b> Model '{self.model}' does not support Live API. Falling back to native audio model.")
                    self.model = "gemini-2.5-flash-native-audio-latest"
            except Exception as e:
                self.ui.log_message.emit(f"> <b style='color:orange;'>Model Introspection failed:</b> {e}. Proceeding anyway...")
            # -----------------------------
            
            # Tool integration
            tools_obj = None
            if self.gemini_tools:
                tools_obj = [{"function_declarations": self.gemini_tools}]
                
            # Fix Modality Conflicts & Speech Config Management
            # Live API native audio models require response_modalities=[AUDIO].
            # We explicitly enable output_audio_transcription to receive the text script back alongside the audio stream.
            req_modalities = [types.Modality.AUDIO]
            
            import coat
            try:
                lang = coat.ui.getCurrentLanguage()
            except:
                lang = "English"

            thinking_profile = getattr(self, 'thinking_profile', 'balanced')
            thinking_rule = ""
            if thinking_profile == 'fast':
                thinking_rule = "THINKING PROFILE: FAST. Do NOT overthink. Provide immediate, brief, and intuitive answers without breaking down the steps unless explicitly asked."
            elif thinking_profile == 'deep':
                thinking_rule = "THINKING PROFILE: DEEP. You must think very carefully. Take your time, reason step-by-step out loud before giving your final answer. Analyze all possible aspects."
            else:
                thinking_rule = "THINKING PROFILE: BALANCED. Provide thoughtful but concise answers."

            config = types.LiveConnectConfig(
                response_modalities=req_modalities,
                output_audio_transcription=types.AudioTranscriptionConfig(),
                input_audio_transcription=types.AudioTranscriptionConfig(),
                tools=tools_obj,
                system_instruction=types.Content(parts=[types.Part.from_text(
                    text="You are a 3D modeling assistant integrated into 3DCoat. "
                         "You can execute actions using the provided tools. "
                         "CRITICAL: As soon as you connect, you MUST immediately call tools "
                         "or look at your available tools to familiarize yourself with the environment. "
                         f"Give a VERY SHORT greeting (max 1 sentence). Do NOT list your tools or explain what you can do unless asked. Keep it under 10 seconds. "
                         f"By default, you MUST speak and answer in the '{lang}' language (the user's UI language). However, if the user explicitly asks you to speak in a different language, you must switch to the requested language immediately. "
                         "You are a 3DCoat expert. Actively use the tools available to you. "
                         "IMPORTANT: When telling the user to click a button, DO NOT speak any weird prefix symbols (like $IconName or #IconName or raw internal IDs). Only speak the natural human-readable name of the button. "
                         "CRITICAL: DO NOT speak, say anything, or emit audio while you are thinking or calling tools. Call all necessary tools silently. Only speak AFTER you have finished all tool calls and are providing your final answer. "
                         "UI RULES: 1) When asked to point to a WINDOW or PANEL (like 'Layers panel'), use `find_open_window_id` to find the container ID, then `point_out_ui_element`. Do NOT point at the menu item that opens the window. 2) ALWAYS set dim_duration=8000 and highlight_duration=16000 in point_out_ui_element. "
                         "3) MODAL DIALOGS: Before trying to interact with the UI, use `get_active_modal_json`. If \"status\" is \"modal_open\", the UI is BLOCKED. Read the \"dialog_meta\" to understand the dialog. If it's a simple Warning/Error, use `run_script_from_source` to click 'Yes' or 'OK'. If it's a complex settings dialog, explain the \"main_message\" and \"hint\" to the user and ask what they want to click. "
                         "4) ROOMS: To switch rooms, use `run_script_from_source` with `coat.ui.toRoom(\"Paint\")` (or Sculpt, Retopo, Modeling, Factures, KitBash, 3DPrint, Nurbs, Nodes, UV, Render, Photogrammetry, Simplest). "
                         "5) GLOBAL MENU MAP: Use `get_full_menu_map_json` when asked to find, show, or point out a MENU ITEM, TOOL, or COMMAND (e.g., 'Where is auto retopology?'). Pass a `query` argument to filter the results if you are looking for something specific (e.g., query='Autopo') to avoid truncation! If `room_context` is empty `\"\"`, the tool is in the top menu bar. Top menus change based on the room. Tell the user: \"This tool is in the menu: [menu_path]\". If it's available in the current room, immediately call `point_out_ui_element(id)` to show it! If `point_out_ui_element` returns an error that it's hidden (because it's in a dropdown, i.e. `menu_path` contains `->`), use `run_script_from_source` to call `print(coat.ui.openMenuAndHighlight(\"[menu_path]\", \"[id]\", \"Look here!\"))` (e.g. `print(coat.ui.openMenuAndHighlight(\"Geometry->AUTOPO->AUTOPO\", \"$Quadrangulate\", \"Here it is\"))`). This will physically open the nested menus, point to the tool, and print the debug output! To activate the tool, execute its `python_api_command`."
                         f"{thinking_rule}"
                )])
            )
            
            self.session = await self.exit_stack.enter_async_context(
                self.client.aio.live.connect(model=self.model, config=config)
            )
            
            self.ui.log_message.emit(f"> <b style='color:green;'>Connected successfully to {self.model}!</b>")
            
            # Start listening to Gemini's responses and sending mic data
            asyncio.create_task(self._receive_from_gemini())
            asyncio.create_task(self._send_audio_loop())
            
            # Send initial prompt automatically
            initial_prompt = f"Please initialize, check your tools silently, and then YOU MUST give a VERY SHORT verbal greeting (max 1 sentence) in {lang}."
            self.ui.log_message.emit(f"<b>You:</b> <i>(Auto-Prompt)</i> {initial_prompt}")
            await self.session.send_client_content(
                turns=types.Content(role='user', parts=[types.Part.from_text(text=initial_prompt)]),
                turn_complete=True
            )
            self.ui.log_message.emit("> Sent auto-prompt to Gemini.")
            
        except Exception as e:
            error_msg = str(e)
            if "API key not valid" in error_msg:
                self.ui.log_message.emit("> <b style='color:red;'>Connection failed:</b> Invalid API Key. Please check the API Key and try again.")
            else:
                self.ui.log_message.emit(f"> <b style='color:red;'>Connection failed:</b> {e}")
            self.session = None
            if hasattr(self.ui, 'connection_failed_signal'):
                self.ui.connection_failed_signal.emit()

    async def _disconnect_from_gemini(self):
        self.ui.log_message.emit("> Disconnecting...")
        if getattr(self, 'exit_stack', None):
            try:
                await asyncio.wait_for(self.exit_stack.aclose(), timeout=3.0)
            except asyncio.TimeoutError:
                self.ui.log_message.emit("> Disconnect timeout. Forcing disconnect...")
            except Exception as e:
                self.ui.log_message.emit(f"> Disconnect warning: {e}")
            self.exit_stack = None
        self.session = None
        self.mcp_session = None
        self.ui.log_message.emit("> Disconnected.")

    async def _send_text(self, text, image_bytes=None, mime_type=None):
        try:
            if self.session:
                if image_bytes:
                    blob = types.Blob(data=image_bytes, mime_type=mime_type)
                    await self.session.send_realtime_input(text=text, media=blob)
                else:
                    await self.session.send_realtime_input(text=text)
                self.ui.log_message.emit("> Sent message to Gemini.")
                
            else:
                self.ui.log_message.emit("> Error: Not connected to Gemini.")
        except Exception as e:
            self.ui.log_message.emit(f"> <b style='color:red;'>Failed to send message:</b> {e}")

    async def _receive_from_gemini(self):
        try:
            while self.is_running and self.session:
                async for response in self.session.receive():
                    server_content = response.server_content
                    if server_content is not None:
                        # Output Transcription channel (asynchronous side-channel for chat UI text update)
                        try:
                            in_trans = getattr(server_content, "input_transcription", None)
                            if in_trans and hasattr(in_trans, 'text') and in_trans.text:
                                is_finished = getattr(in_trans, 'finished', False)
                                if hasattr(self.ui, 'user_speech_message'):
                                    self.ui.user_speech_message.emit(in_trans.text, is_finished)
                                    
                            # Safely extract transcription
                            out_trans = getattr(server_content, "output_transcription", None)
                            if out_trans and hasattr(out_trans, 'text') and out_trans.text:
                                if hasattr(self.ui, 'speech_message'):
                                    self.ui.speech_message.emit(out_trans.text)
                                else:
                                    self.ui.log_message.emit(f"<b>Gemini:</b> <span style='font-weight:bold; font-size:1.1em;'>{out_trans.text}</span>")
                                    
                            if hasattr(server_content, "interrupted") and server_content.interrupted:
                                self.ui.log_message.emit("<i>[Gemini interrupted]</i>")
                        except Exception as e:
                            pass
                            
                        model_turn = server_content.model_turn
                        if model_turn is not None:
                            for part in model_turn.parts:
                                # Check if it's explicitly marked as a thought in newer SDKs
                                if getattr(part, 'thought', False):
                                    if hasattr(self.ui, 'thought_message'):
                                        self.ui.thought_message.emit("Thinking...")
                                elif part.text:
                                    # part.text is the actual markdown response, including code blocks!
                                    if hasattr(self.ui, 'speech_message'):
                                        self.ui.speech_message.emit(part.text)
                                    else:
                                        self.ui.log_message.emit(f"<b>Gemini:</b> {part.text}<br>")
                                elif part.inline_data:
                                    # We have audio!
                                    if part.inline_data.data:
                                        raw_audio = part.inline_data.data
                                        self.audio_out_queue.put(raw_audio)
                                        
                        if getattr(server_content, "turn_complete", False):
                            if hasattr(self.ui, 'turn_complete_signal'):
                                self.ui.turn_complete_signal.emit()
                                    
                    # Tool Calls in Gemini Live API are delivered at the root message level
                    if getattr(response, "tool_call", None) is not None:
                        self.is_tool_call_pending = True
                        if hasattr(self.ui, 'thinking_signal'):
                            self.ui.thinking_signal.emit(True)
                        async def process_all_tools(tool_calls):
                            try:
                                responses = await asyncio.gather(*(self._handle_function_call(fc) for fc in tool_calls))
                                if self.session and responses:
                                    await self.session.send_tool_response(function_responses=list(responses))
                            finally:
                                self.is_tool_call_pending = False
                                if hasattr(self.ui, 'thinking_signal'):
                                    self.ui.thinking_signal.emit(False)
                                
                        asyncio.create_task(process_all_tools(response.tool_call.function_calls))
                            
        except asyncio.CancelledError:
            pass
        except Exception as e:
            msg = str(e)
            if "closed" not in msg.lower(): # ignore closed websocket errors
                self.ui.log_message.emit(f"> Error receiving from Gemini: {e}")
                
            if "1008" in msg and self.is_running:
                self.ui.log_message.emit("> <b style='color:orange;'>Attempting auto-reconnect due to 1008 error...</b>")
                asyncio.create_task(self._auto_reconnect())
            elif "1011" in msg and self.is_running:
                self.ui.log_message.emit("> <b style='color:orange;'>Attempting auto-reconnect due to 1011 timeout error...</b>")
                asyncio.create_task(self._auto_reconnect())

    async def _auto_reconnect(self):
        await self._disconnect_from_gemini()
        await asyncio.sleep(1)
        if self.is_running:
            await self._connect_to_gemini()

    async def _handle_function_call(self, function_call):
        self.ui.log_message.emit(f"> <b style='color:purple;'>Tool Call:</b> {function_call.name}")
        
        try:
            # Look up the actual MCP tool name from the mapping
            mcp_tool_map = getattr(self, "mcp_tool_map", {})
            tool_name = mcp_tool_map.get(function_call.name, function_call.name)
            
            call_id = function_call.id
            
            # We convert kwargs from protobuf dict
            args = dict(function_call.args) if function_call.args else {}
            
            if self.mcp_session:
                result = await self.mcp_session.call_tool(tool_name, arguments=args)
                
                # Format string result
                result_text = ""
                for content in result.content:
                    if content.type == "text":
                        result_text += content.text + "\n"
                        
                # Protect Gemini Live API websocket from 1008 policy violation (size limit is ~32KB)
                # Cyrillic characters take 2 bytes, so 8000 characters is a safe limit (16KB)
                if len(result_text) > 8000:
                    truncated_msg = "\n\n...[TRUNCATED: Response exceeded size limit. Consider reading files in chunks or searching.]..."
                    result_text = result_text[:8000 - len(truncated_msg)] + truncated_msg
                            
                self.ui.log_message.emit(f"> <b style='color:purple;'>Result:</b> {result_text[:100]}...")
                
                # Return feedback to be sent to Gemini using proper Response type
                return types.FunctionResponse(
                    id=call_id,
                    name=function_call.name,
                    response={"result": result_text}
                )
            else:
                raise Exception("MCP Session not available")
                
        except Exception as e:
            self.ui.log_message.emit(f"> <b style='color:red;'>Tool Call failed:</b> {e}")
            
            return types.FunctionResponse(
                id=call_id,
                name=function_call.name,
                response={"error": str(e)}
            )

    async def _send_audio_loop(self):
        """Continuously pulls from audio queue and sends to Gemini"""
        in_buffer = bytearray()
        while self.is_running and self.session:
            try:
                # Wait for mic data
                audio_bytes = await self.audio_in_queue.get()
                if self.session and self.is_mic_active:
                    in_buffer.extend(audio_bytes)
                    
                    # Drain the queue to catch up instantly if our network loop is lagging
                    while not self.audio_in_queue.empty():
                        in_buffer.extend(self.audio_in_queue.get_nowait())
                        
                    # Send in chunks to avoid 1008 WebSocket payload violation (max ~32KB per message)
                    valid_bytes = (len(in_buffer) // 2) * 2
                    if valid_bytes > 0:
                        if self.is_tool_call_pending:
                            # Drop audio while tool is running to prevent 1008 protocol violation
                            del in_buffer[:valid_bytes]
                        else:
                            chunk_size = 4096 # 4KB per chunk max
                            for i in range(0, valid_bytes, chunk_size):
                                chunk = bytes(in_buffer[i:i+chunk_size])
                                if self.is_mic_active and self.session and not self.is_tool_call_pending:
                                    try:
                                        await self.session.send_realtime_input(
                                            audio=types.Blob(data=chunk, mime_type=f"audio/pcm;rate={self.audio_in_rate}")
                                        )
                                    except Exception as e:
                                        pass
                                await asyncio.sleep(0.01) # Yield to event loop to prevent WebSocket 1008 flood violation
                            del in_buffer[:valid_bytes]
                else:
                    in_buffer.clear()
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"Error sending audio: {e}")

