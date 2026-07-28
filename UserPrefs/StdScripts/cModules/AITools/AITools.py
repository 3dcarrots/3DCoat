import cPy.cCore
import coat
import gc
import time
import os
import json


import threading
import random
import cModules.ExtensionManager
from cPy.cCore import cExtension
from mcp.server.fastmcp import FastMCP
from cPy.cIDE import PTRecord
import cPy.cNodeSystem
import cPy.cTypes

# 3DCoat internal libraries are imported here
# import 3dcoat_api 

# Server initialization
mcp = FastMCP("3DCoat Live API", sse_path="/mcp")
mcp_port = random.randint(49152, 65535)

ScriptsFolder = "UserPrefs/Scripts"

import sys
import io
import os
import json

task_queue_lock = threading.Lock()
task_queue = []

import functools

def run_in_main_thread(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        task = {
            "func": func,
            "args": args,
            "kwargs": kwargs,
            "event": threading.Event(),
            "result": None,
            "error": None
        }
        with task_queue_lock:
            task_queue.append(task)
            
        task["event"].wait(timeout=60.0)
        
        if task["error"]:
            raise task["error"]
            
        if not task["event"].is_set():
            return f"Error: Tool execution timeout (Timeout 60s) for {func.__name__}."
            
        return task["result"]
    return wrapper

nodeGraph = None

@mcp.tool()
@run_in_main_thread
def check_gpu_node_source(node_source: str) -> str:
    """Checks if the GPU node source code is valid and returns its output and errors."""
    print("check_gpu_node_source")
    print(node_source)
    global nodeGraph
    if nodeGraph == None:
        nodeGraph = cPy.cNodeSystem.NodeGraph()
    nodeGraph.Clear()
    test_node = nodeGraph.AddNode()
    test_node.setNGLSource(node_source)

    nodeGraph.MakeScript()
    print(nodeGraph.CompileLog)
    return nodeGraph.CompileLog

@mcp.tool()
@run_in_main_thread
def run_script_from_source(script_source: str) -> str:
    """Runs a Python script and returns its output and errors."""
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = io.StringIO()
    sys.stdout = redirected_output
    sys.stderr = redirected_output
    
    error_msg = ""
    try:
        PTRecord.add("AGENT:", "", script_source)
        exec(script_source, globals())
    except Exception as e:
        import traceback
        error_msg = f"\nExecution error:\n{traceback.format_exc()}"
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        
    output = redirected_output.getvalue()
    
    if output:
        print(output, end="")
    if error_msg:
        print(error_msg, end="", file=sys.stderr)
        
    final_result = ""
    if output:
        final_result += f"Output:\n{output}\n"
    if error_msg:
        final_result += error_msg
        
    if not final_result.strip():
        final_result = "Script successfully executed (no output)."
    return final_result
    

def _get_python_files_info(folders: dict, read_file: str = "") -> str:
    if read_file:
        for name, folder in folders.items():
            if folder and os.path.exists(folder):
                full_path = os.path.normpath(os.path.join(folder, read_file))
                # Security check to prevent path traversal
                if os.path.commonpath([full_path, os.path.normpath(folder)]) == os.path.normpath(folder):
                    if os.path.exists(full_path):
                        try:
                            with open(full_path, "r", encoding="utf-8") as f:
                                return f"--- File: {read_file} (from {name}) ---\n\n" + f.read()
                        except Exception as e:
                            return f"Error reading {read_file}: {e}"
        return f"Error: File '{read_file}' not found in any of the allowed directories."
    else:
        results = {}
        for name, folder in folders.items():
            results[name] = []
            if folder and os.path.exists(folder):
                for dirpath, _, filenames in os.walk(folder):
                    for f in filenames:
                        if f.endswith(".py"):
                            rel_dir = os.path.relpath(dirpath, folder)
                            if rel_dir == ".":
                                results[name].append(f)
                            else:
                                results[name].append(os.path.join(rel_dir, f).replace("\\", "/"))
        
        instructions = (
            "Here is a list of available Python files.\n"
            "To read the source code of a specific file, call this same tool again and pass the relative "
            "filename (e.g. 'coat.py' or 'subfolder/script.py') to the `read_file` parameter."
        )
        return instructions + "\n\n" + json.dumps(results, indent=2)

@mcp.tool()
@run_in_main_thread
def get_python_api_sources(read_file: str = "") -> str:
    """Returns a list of all available Python API modules. If read_file (filename) is provided, returns the code of that file."""
    folders = {}
    
    # Try using cExtension paths first since it's most robust within 3DCoat
    try:
        base_install = cExtension.getCoatInstallForder()
        folders["Bridge"] = os.path.join(base_install, "UserPrefs", "PythonAPI", "Bridge")
        folders["StdScripts"] = os.path.join(base_install, "UserPrefs", "StdScripts")
    except:
        pass
        
    try:
        import coat
        folders["Rooms"] = coat.io.documents("UserPrefs/Rooms")
    except:
        pass

    return _get_python_files_info(folders, read_file)

@mcp.tool()
@run_in_main_thread
def get_python_examples(read_file: str = "") -> str:
    """Returns a list of code examples for the Python API. If read_file (filename) is provided, returns the code of that file."""
    folders = {}
    try:
        base_install = cExtension.getCoatInstallForder()
        folders["Templates"] = os.path.join(base_install, "UserPrefs", "PythonAPI", "Templates")
    except:
        pass

    return _get_python_files_info(folders, read_file)

@mcp.tool()
@run_in_main_thread
def get_std_GPU_Nodes(read_file: str = "") -> str:
    """Returns a list of all standard GPU Nodes installed with 3DCoat. This directory does not contain nodes created, modified, or installed by the user. If read_file (filename) is provided, returns the code of that file."""
    folders = {}
    try:
        base_install = cExtension.getCoatInstallForder()
        folders["GPU Nodes"] = os.path.join(base_install, "UserPrefs", "Scripts", "GPUNodes")
    except:
        pass

    return _get_python_files_info(folders, read_file)

@mcp.tool()
@run_in_main_thread
def get_full_ui_description_as_json() -> str:
    """Returns a full JSON representation of the entire 3DCoat UI hierarchy.
    The 'rect' property is formatted as an array [x, y, width, height] representing screen coordinates.
    
    INSTRUCTIONS FOR AI AGENTS (How to interact with UI):
    When you need to change a parameter in 3DCoat, find it in this JSON tree by its name (Text or Hint fields). Look at its "class", "current_value", and "id":
    - If it's a SimpleSlider, use: coat.ui.setSliderValue("id", float)
      Note: Sliders expose "min_value" and "max_value". If a UI element displays a percentage (e.g. 100%) but max_value is 1, you must pass 1.0 (internal fractional value), not 100.
    - If it's a TextWidget and its value is true/false (checkbox), use: coat.ui.setBoolField("id", bool)
    - If it's a regular text input field, use: coat.ui.setEditBoxValue("id", "text")
    - If it's a clickable button or menu item, use: coat.ui.cmd("id")
    
    After changing values via UI, you may need to update the interface by calling coat.ui.apply().
    Important: Some UI elements are generated dynamically (e.g., via BaseClass system). If a Python script cannot find an element by ID, ensure that the window containing this tool is currently open, as 3DCoat destroys inactive widgets.
    """
    try:
        import coat
        if hasattr(coat.ui, "getFullUIDescriptionAsJSON"):
            return coat.ui.getFullUIDescriptionAsJSON()
        else:
            return "Error: coat.ui.getFullUIDescriptionAsJSON is not available in the current 3DCoat version."
    except Exception as e:
        import traceback
        return f"Error executing getFullUIDescriptionAsJSON:\n{traceback.format_exc()}"

@mcp.tool()
@run_in_main_thread
def get_hovered_ui_element_as_json() -> str:
    """Returns the JSON representation of the 3DCoat UI element currently under the user's mouse cursor. 
    Use this when the user asks "what is this?", "fill this field", or points at something. 
    Returns the same detailed JSON format as get_full_ui_description_as_json (with class, current_value, python_api_command, etc.), but only for the specific hovered element."""
    try:
        import coat
        if hasattr(coat.ui, "getHoveredWidgetAsJSON"):
            return coat.ui.getHoveredWidgetAsJSON()
        else:
            return "Error: coat.ui.getHoveredWidgetAsJSON is not available in the current 3DCoat version."
    except Exception as e:
        import traceback
        return f"Error executing get_hovered_ui_element_as_json:\n{traceback.format_exc()}"

@mcp.tool()
@run_in_main_thread
def get_ui_element_info(widget_id: str) -> str:
    """Returns the full detailed JSON info (including rect, Hint, python_api_command) for a specific widget ID.
    Use this tool when you found an element in get_full_ui_description_as_json or search_ui_commands, but you need its full details (like Hint or rect)."""
    try:
        import coat
        if hasattr(coat.ui, "getWidgetInfoAsJSON"):
            return coat.ui.getWidgetInfoAsJSON(widget_id)
        else:
            return "Error: coat.ui.getWidgetInfoAsJSON is not available. Please recompile 3DCoat."
    except Exception as e:
        import traceback
        return f"Error executing get_ui_element_info:\n{traceback.format_exc()}"

@mcp.tool()
@run_in_main_thread
def get_active_modal_json() -> str:
    """Returns the JSON representation of the currently active modal dialog in 3DCoat.
    Use this tool BEFORE taking any UI actions or when the user mentions a dialog or popup message.
    It returns the dialog's title, description, and available buttons to interact with.
    If no modal is open, it returns {"status": "no_modal_open"}."""
    try:
        import coat
        if hasattr(coat.ui, "getActiveModalJSON"):
            return coat.ui.getActiveModalJSON()
        else:
            return "Error: coat.ui.getActiveModalJSON is not available. Please recompile 3DCoat."
    except Exception as e:
        import traceback
        return f"Error executing get_active_modal_json:\n{traceback.format_exc()}"

@mcp.tool()
@run_in_main_thread
def point_out_ui_element(widget_id: str, message: str, dim_duration: int = 4000, highlight_duration: int = 8000) -> str:
    """Points out a specific UI element to the user by highlighting it with a red box, dimming the screen, and showing a message.
    Use this tool when you need to guide the user's attention to a specific tool or button in the interface.
    The screen will dim for 'dim_duration' ms (default 4000) and the red highlight will remain for 'highlight_duration' ms (default 8000). The interface will automatically scroll to the element if needed.
    IMPORTANT: You MUST ONLY point out widget_ids that you have found in the output of get_full_ui_description_as_json or get_hovered_ui_element_as_json. Do not guess widget IDs.
    """
    try:
        import coat
        if hasattr(coat.ui, "pointOutUIElement"):
            success = coat.ui.pointOutUIElement(widget_id, message, dim_duration, highlight_duration)
            if success:
                return f"Successfully pointed out UI element '{widget_id}' to the user."
            else:
                return f"Error: The UI element with ID '{widget_id}' was not found. It might be hidden or not present in the current layout."
        else:
            return "Error: coat.ui.pointOutUIElement is not available in the current 3DCoat version."
    except Exception as e:
        import traceback
        return f"Error executing pointOutUIElement:\n{traceback.format_exc()}"

@mcp.tool()
@run_in_main_thread
def find_open_window_id(window_name: str) -> str:
    """Finds the internal ID of an open window, panel, or popup by its visible name.
    Use this tool when the user asks you to show or point out a window/panel.
    If this returns an ID, use point_out_ui_element on it.
    If it returns not found, use run_script_from_source(coat.ui.cmd(...)) to open the tool first, then call this again."""
    try:
        import coat
        import json
        
        ui_json_str = ""
        if hasattr(coat.ui, "getFullUIDescriptionAsJSON"):
            ui_json_str = coat.ui.getFullUIDescriptionAsJSON()
        else:
            return "Error: getFullUIDescriptionAsJSON not available."
            
        ui_data = json.loads(ui_json_str)
        name_lower = window_name.lower().strip()
        
        def search_node(node):
            node_class = node.get("class", "")
            node_id = node.get("id", "")
            node_text = node.get("Text", "")
            
            # Exclude leaf widgets from being considered as window containers
            is_leaf = "Text" in node_class or "Button" in node_class or "Slider" in node_class or "Rect" in node_class or "Scroll" in node_class or "Menu" in node_class
            is_container = not is_leaf and ("Widget" in node_class or "Panel" in node_class or "Frame" in node_class or "Window" in node_class)
            
            if is_container:
                # Prioritize explicit Text matching the window name
                if node_text and name_lower in node_text.lower() and len(node_text) < 50:
                    return node_id
                # Check if ID itself is the text fallback (without $ prefix meaning command)
                if node_id and name_lower in node_id.lower() and len(node_id) < 50 and not node_id.startswith("$"):
                    return node_id
                    
            for child in node.get("sub_elements", []):
                res = search_node(child)
                if res: return res
            return None
                
        for root_node in ui_data.get("3DCoat_UI_Root", []):
            found_id = search_node(root_node)
            if found_id:
                return f"Found open window ID: {found_id}"
                
        return f"Could not find an open window matching '{window_name}'. It might be closed. Open it first via run_script_from_source(coat.ui.cmd(...))."
    except Exception as e:
        return f"Error executing find_open_window_id: {e}"

@mcp.tool()
@run_in_main_thread
def search_ui_commands(query: str, limit: int = 20) -> str:
    """Searches the 3DCoat language/localization files for a specific command name or UI text.
    Use this tool when you need to find the internal ID (e.g. '$IncRes') of a tool or menu item that is currently hidden in a dropdown menu and not visible in get_full_ui_description_as_json.
    'query' is the text you are looking for (e.g., 'Increase resolution' or 'Збільшити дозвіл').
    Returns a list of matching IDs and their associated text.
    """
    try:
        import os
        import coat
        import cPy.cCore
        install_dir = cPy.cCore.cExtension.getCoatInstallForder()
        # Find the language folder
        lang_dir = os.path.join(install_dir, "data", "Languages")
        if not os.path.exists(lang_dir):
            return "Error: Languages directory not found."
            
        import glob
        import re
        
        # Determine current language or use English/Ukrainian as fallback
        # This is a simple grep implementation through the XML files
        xml_files = glob.glob(os.path.join(lang_dir, "*.xml"))
        
        current_lang_file = "English.xml"
        if hasattr(coat.ui, "getCurrentLanguage"):
            lang_name = coat.ui.getCurrentLanguage()
            if lang_name:
                current_lang_file = f"{lang_name}.xml"
        
        results = []
        # Split query into words
        query_words = set(re.findall(r'\w+', query.lower()))
        if not query_words:
            return "Error: Invalid query."
            
        def match_score(text):
            text_lower = text.lower()
            if query.lower() in text_lower:
                return len(query_words) # Exact substring match is best
            text_words = set(re.findall(r'\w+', text_lower))
            match_count = len(query_words.intersection(text_words))
            return match_count

        for xml_file in xml_files:
            file_name = os.path.basename(xml_file)
            if file_name != "English.xml" and file_name != current_lang_file:
                continue # To keep it fast, check only main languages
                
            try:
                with open(xml_file, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    
                for i in range(len(lines)):
                    is_match = False
                    match_text = ""
                    
                    if "<Text>" in lines[i] or "<Hint>" in lines[i]:
                        text_val = re.search(r'<(Text|Hint)>(.*?)</\1>', lines[i])
                        if text_val:
                            content = text_val.group(2)
                            score = match_score(content)
                            
                            # Match if strict substring OR at least half the words match (or exactly 1 word if query is 1 word)
                            required_matches = max(1, len(query_words) - 1) if len(query_words) > 1 else 1
                            if score >= required_matches:
                                is_match = True
                                match_text = content
                                
                    if is_match:
                        id_val = None
                        # Look back up to 10 lines to find the ID (since Hint might be further down)
                        for j in range(i-1, max(-1, i-10), -1):
                            match = re.search(r'<ID>(.*?)</ID>', lines[j])
                            if match:
                                id_val = "$" + match.group(1)
                                break
                                
                        if id_val:
                            # Verify if the command is actually available/valid in the current UI context
                            is_valid = True
                            if hasattr(coat.ui, "isValidCommand"):
                                is_valid = coat.ui.isValidCommand(id_val)
                                
                            if is_valid:
                                # Avoid adding exact duplicates
                                entry = f"ID: {id_val} | Text/Hint: {match_text}"
                                if entry not in results:
                                    results.append(entry)
                                if len(results) >= limit:
                                    break
            except:
                pass
                
            if len(results) >= limit:
                break
                
        if not results:
            return f"No UI commands found matching '{query}'."
            
        return "Found matching commands:\n" + "\n".join(results)
    except Exception as e:
        import traceback
        return f"Error executing search_ui_commands:\n{traceback.format_exc()}"

def _read_rule_file(filename: str) -> str:
    try:
        devtools_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        import inspect
        try:
            devtools_dir = os.path.dirname(os.path.abspath(inspect.getfile(_read_rule_file)))
        except:
            # Fallback
            devtools_dir = os.path.join(os.path.expanduser("~"), "Documents", "3DCoat", "UserPrefs", "Scripts", "cModules", "DevTools")
    
    filepath = os.path.join(devtools_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return f"Error: Cannot find {filename}"

@mcp.tool()
@run_in_main_thread
def read_global_ai_rules() -> str:
    """MANDATORY READING BEFORE FIRST ACTION. Returns the core global rules and constraints for all AI agents working in 3DCoat. You MUST read this before writing any code or answering user questions."""
    return _read_rule_file("AI_RULES_TEMPLATE.md")

@mcp.tool()
@run_in_main_thread
def read_node_graph_language_rules() -> str:
    """MANDATORY READING FOR GPU NODES (NGL). Returns the syntax and structure rules for 3DCoat's NodeGraph Language. You MUST read this before writing, editing, or analyzing any .glsl files or GPU nodes."""
    return _read_rule_file("NGL_RULES_TEMPLATE.md")

@mcp.tool()
@run_in_main_thread
def read_3dcoat_python_api_guide() -> str:
    """MANDATORY READING FOR PYTHON SCRIPTS. Returns the comprehensive guide to the 3DCoat Python API. You MUST read this before writing, editing, or exploring any python scripts to understand imports, types, and module locations."""
    return _read_rule_file("3DCoat_API_Guide.md")

@mcp.tool()
@run_in_main_thread
def read_3dcoat_extension_guide() -> str:
    """MANDATORY READING BEFORE CREATING NEW EXTENSIONS OR APPS (cExtensions). Returns the comprehensive guide on how to build, debug and architecture 3DCoat extensions/apps using python. You MUST read this before you start writing any new extensions or UI additions."""
    return _read_rule_file("cExtensions_Guide.md")

@mcp.tool()
@run_in_main_thread
def read_3dcoat_log(lines: int = 150) -> str:
    """Returns the latest records from 3DCoat's internal Log.txt and python_error.txt. Extremely useful for debugging crashes, Python syntax errors before the terminal starts, or general application errors. 'lines' limits the output from the end of Log.txt."""
    try:
        import coat
        import os
        
        log_path = coat.io.documents("Log.txt")
        err_path = coat.io.documents("python_error.txt")
        
        output = ""
        log_mtime = 0
        err_mtime = 0
        
        if os.path.exists(log_path):
            log_mtime = os.path.getmtime(log_path)
            
        if os.path.exists(err_path):
            err_mtime = os.path.getmtime(err_path)
            
        # If there are python errors, and the error file was created AFTER the start of the session (or is newer than the log)
        # Usually python_error.txt is updated on startup if there are critical syntax errors.
        if os.path.exists(err_path) and (err_mtime >= log_mtime - 10):
            with open(err_path, "r", encoding="utf-8", errors="replace") as f:
                err_content = f.read().strip()
                if err_content:
                    output += f"--- PYTHON_ERROR.TXT (Warning: CRITICAL INITIALIZATION ERRORS) ---\n{err_content}\n\n"
                    
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8", errors="replace") as f:
                # Read the last N lines to optimize context
                log_lines = f.readlines()
                if len(log_lines) > lines:
                    log_lines = log_lines[-lines:]
                output += f"--- LOG.TXT (Last {lines} lines) ---\n" + "".join(log_lines)
        else:
            output += "Log.txt not found."
            
        return output
    except Exception as e:
        return f"Error reading logs: {e}"

@mcp.tool()
@run_in_main_thread
def read_3dcoat_modeling_guide() -> str:
    """MANDATORY READING BEFORE WRITING SCRIPT FOR MODELING. Returns the comprehensive guide on how to perform modeling, generate primitives, and use booleans in 3DCoat via Python. You MUST read this before writing any python scripts that generate, modify, or interact with 3D geometry/meshes."""
    return _read_rule_file("3DCoat_Modeling_Guide.md")

@mcp.tool()
@run_in_main_thread
def read_3dcoat_node_graph_guide() -> str:
    """MANDATORY READING BEFORE CREATING NODE GRAPHS. Returns rules and examples for creating and saving NodeGraphs or node schemes via Python. You MUST read this before writing any python scripts that create node schemes."""
    return _read_rule_file("3DCoat_NodeGraph_Guide.md")

@mcp.tool()
@run_in_main_thread
def search_3dcoat_faq(query: str, limit: int = 5) -> str:
    """Searches the official 3DCoat FAQ and Knowledge Base (chat.pilgway.com) for answers. Use this tool when answering general usage, licensing, or troubleshooting questions.
    'query' is the search phrase. Try to use simple keywords rather than full sentences for better matching."""
    import sqlite3
    import os
    import re
    
    try:
        devtools_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        import inspect
        try:
            devtools_dir = os.path.dirname(os.path.abspath(inspect.getfile(search_3dcoat_faq)))
        except:
            devtools_dir = os.path.join(os.path.expanduser("~"), "Documents", "3DCoat", "UserPrefs", "Scripts", "cModules", "AITools")
            
    db_path = os.path.join(devtools_dir, "knowledge_base.db")
    if not os.path.exists(db_path):
        return f"Error: knowledge_base.db not found at {db_path}."
        
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        words = re.findall(r'\w+', query)
        if not words:
            return "Error: Invalid query."
            
        fts_query = " OR ".join([f'"{w}"*' for w in words])
        
        c.execute("SELECT question, answer FROM faq WHERE faq MATCH ? ORDER BY rank LIMIT ?", (fts_query, limit))
        results = c.fetchall()
        
        if not results:
            return f"No results found for query: {query}. Try using different or fewer keywords."
            
        output = f"--- FAQ Search Results for '{query}' ---\n\n"
        for idx, (q, a) in enumerate(results):
            output += f"Q{idx+1}: {q}\nA{idx+1}: {a}\n\n"
            
        return output.strip()
    except Exception as e:
        return f"Error querying FAQ: {e}"

def create_primitive_in_scene(radius: float) -> str:
    """Creates a new sphere directly in the open 3DCoat scene."""
    # Direct 3DCoat API call for geometry generation
    # 3dcoat_api.create_sphere(radius)
    return f"Sphere with radius {radius} successfully added to the scene."

def update_antigravity_config(mcp_port: int):
    import os
    import json
    
    # Define the paths to the global Antigravity ecosystem folders
    home = os.path.expanduser('~')
    config_paths = [
        os.path.join(home, '.gemini', 'antigravity', 'mcp_config.json'), # IDE
        os.path.join(home, '.gemini', 'config', 'mcp_config.json'),      # Standalone
        os.path.join(home, '.gemini', 'antigravity-cli', 'mcp_config.json') # CLI
    ]

    for config_path in config_paths:
        config_dir = os.path.dirname(config_path)
        os.makedirs(config_dir, exist_ok=True)
    
        # Basic configuration structure
        config_data = {}
    
        # If the file already exists, read it so as not to overwrite other settings
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config_data = json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: File {config_path} contains invalid JSON. Content will be overwritten.")
    
        # Ensure the root key exists
        if "mcpServers" not in config_data:
            config_data["mcpServers"] = {}
    
        # Add the 3dcoat-live configuration with the correct type
        config_data["mcpServers"]["3dcoat-live"] = {
            "type": "sse",
            "url": "http://127.0.0.1:" + str(mcp_port) + "/mcp",
            "serverURL": "http://127.0.0.1:" + str(mcp_port) + "/mcp",
            "serverUrl": "http://127.0.0.1:" + str(mcp_port) + "/mcp"
        }
    
        # Write updated configuration back to file
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Configuration successfully updated in file: {config_path}")


def start_mcp_server():
    """Function to start the server via HTTP/SSE."""
    global mcp_port, ScriptsFolder
    import sys
    import os
    import json
    import traceback
    import asyncio
    import contextlib
    import uvicorn
    import logging
    import subprocess

    class ThreadSafeUvicornServer(uvicorn.Server):
        def install_signal_handlers(self):
            pass

        @contextlib.contextmanager
        def run_in_thread(self):
            def thread_target():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    loop.run_until_complete(self.serve())
                except Exception as e:
                    log_path = os.path.join(ScriptsFolder, "mcp_fatal_crash.log")
                    try:
                        with open(log_path, "w") as f:
                            f.write(f"Fatal exception: {e}\n")
                            traceback.print_exc(file=f)
                    except: pass
                finally:
                    loop.close()

            thread = threading.Thread(target=thread_target, daemon=True)
            thread.start()
            
            try:
                while not self.started:
                    time.sleep(0.01)
                yield
            finally:
                self.should_exit = True
                thread.join(timeout=2.0)
    
    try:
        ScriptsFolder = coat.io.documents("UserPrefs/Scripts")
        print(f"Scripts Folder: {ScriptsFolder}")

        mcp_config = {
            "mcpServers": {
                "3dcoat-live": {
                    "type": "sse",
                    "url": "http://127.0.0.1:" + str(mcp_port) + "/mcp"
                }
            }
        }

        # Directory search for rule templates
        try:
            devtools_dir = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            import inspect
            try:
                devtools_dir = os.path.dirname(os.path.abspath(inspect.getfile(start_mcp_server)))
            except:
                devtools_dir = os.path.join(ScriptsFolder, "cModules", "DevTools")
                
        # Template content reading
        def read_template(template_name):
            template_path = os.path.join(devtools_dir, template_name)
            if os.path.exists(template_path):
                with open(template_path, 'r', encoding='utf-8') as f:
                    return f.read().strip()
            return ""

        ai_rules_content = read_template("AI_RULES_TEMPLATE.md")
        ngl_rules_content = read_template("NGL_RULES_TEMPLATE.md")
        api_guide_content = read_template("3DCoat_API_Guide.md")

        for target_folder in [coat.io.documents("UserPrefs/Scripts"), coat.io.documents("UserPrefs/StdScripts")]:
            if not os.path.exists(target_folder):
                continue

            # --- 1. Settings for Cursor (.mdc) ---
            cursor_rules_dir = os.path.join(target_folder, ".cursor", "rules")
            if not os.path.exists(cursor_rules_dir):
                os.makedirs(cursor_rules_dir)

            if ai_rules_content:
                with open(os.path.join(cursor_rules_dir, "core.mdc"), 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    f.write("description: \"Global project rules and basic AI agent instructions for 3DCoat\"\n")
                    f.write("alwaysApply: true\n")
                    f.write("---\n\n")
                    f.write(ai_rules_content + "\n")

            if ngl_rules_content:
                with open(os.path.join(cursor_rules_dir, "ngl.mdc"), 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    f.write("description: \"NGL (NodeGraph Language) rules for creating and modifying GPU nodes in 3DCoat\"\n")
                    f.write("globs: \"*.glsl\"\n")
                    f.write("alwaysApply: false\n")
                    f.write("---\n\n")
                    f.write(ngl_rules_content + "\n")

            if api_guide_content:
                with open(os.path.join(cursor_rules_dir, "api.mdc"), 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    f.write("description: \"3DCoat Python API Guide - Use when writing or modifying python scripts or tools\"\n")
                    f.write("globs: \"*.py\"\n")
                    f.write("alwaysApply: false\n")
                    f.write("---\n\n")
                    f.write(api_guide_content + "\n")

            # --- 2. Settings for Google Antigravity (.md) ---
            antigravity_rules_dir = os.path.join(target_folder, ".agent", "rules")
            if not os.path.exists(antigravity_rules_dir):
                os.makedirs(antigravity_rules_dir)

            # For Antigravity we save ai_rules_content in core.md, supplementing it with links to other files.
            if ai_rules_content:
                with open(os.path.join(antigravity_rules_dir, "core.md"), 'w', encoding='utf-8') as f:
                    f.write(ai_rules_content + "\n\n")
                    f.write("### Additional specialized rules (Routing)\n")
                    f.write("If the task concerns NGL (writing or editing GPU nodes .glsl), mandatory refer to rules from @ngl.md\n")
                    f.write("If the task concerns using the 3DCoat Python API (writing or editing .py scripts), mandatory refer to rules from @api.md\n")

            if ngl_rules_content:
                with open(os.path.join(antigravity_rules_dir, "ngl.md"), 'w', encoding='utf-8') as f:
                    f.write(ngl_rules_content + "\n")

            if api_guide_content:
                with open(os.path.join(antigravity_rules_dir, "api.md"), 'w', encoding='utf-8') as f:
                    f.write(api_guide_content + "\n")

            # --- 3. Copying workflows for Google Antigravity ---
            import shutil
            workflows_src = os.path.join(devtools_dir, "workflows")
            if os.path.exists(workflows_src) and os.path.isdir(workflows_src):
                workflows_dest = os.path.join(target_folder, ".agent", "workflows")
                
                # Delete old directory if it exists to avoid conflicts or outdated files
                if os.path.exists(workflows_dest):
                    try:
                        shutil.rmtree(workflows_dest)
                    except Exception as e:
                        print(f"Failed to delete old workflows directory: {e}")
                        
                try:
                    shutil.copytree(workflows_src, workflows_dest)
                except Exception as e:
                    pass

            # --- 4. Cleaning up old migration files and AGENTS.md ---
            agents_path = os.path.join(target_folder, "AGENTS.md")
            with open(agents_path, 'w', encoding='utf-8') as f:
                f.write("# Warning: This file is deprecated\n")
                f.write("Refer to `.cursor/rules/` or `.agent/rules/` folders for the latest rules.\n")
                
        print(f"Generated modular AI routing proxies in .agent/rules/ and .cursor/rules/")


        print(f"MCP Port: {mcp_port}")

        log_file = os.path.join(ScriptsFolder, "mcp_server.log")
        
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
            
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            force=True
        )
        
        logging.getLogger("uvicorn").handlers = []
        logging.getLogger("uvicorn").propagate = True
        logging.getLogger("mcp").handlers = []
        logging.getLogger("mcp").propagate = True
        
        print(f"Starting robust uvicorn server on port {mcp_port}...")
        
        try:
            app = mcp.http_app(path="/mcp")
        except AttributeError:
            app = mcp.streamable_http_app()


        config = uvicorn.Config(
            app=app, 
            host="127.0.0.1", 
            port=mcp_port, 
            log_level="debug", 
            log_config=None, 
            access_log=True
        )
        server = ThreadSafeUvicornServer(config=config)
        
        with server.run_in_thread():
            print(f"Uvicorn successfully bound to http://127.0.0.1:{mcp_port}/mcp")
            # Write configs ONLY when Uvicorn is successfully listening
            update_antigravity_config(mcp_port)

            for target_folder in [coat.io.documents("UserPrefs/Scripts"), coat.io.documents("UserPrefs/StdScripts")]:
                if not os.path.exists(target_folder):
                    continue
                # For Cursor
                cursor_dir = os.path.join(target_folder, ".cursor")
                if not os.path.exists(cursor_dir): os.makedirs(cursor_dir)
                with open(os.path.join(cursor_dir, "mcp.json"), "w") as f:
                    json.dump(mcp_config, f, indent=4)
                    
                # For Windsurf
                windsurf_dir = os.path.join(target_folder, ".windsurf")
                if not os.path.exists(windsurf_dir): os.makedirs(windsurf_dir)
                with open(os.path.join(windsurf_dir, "mcp.json"), "w") as f:
                    json.dump(mcp_config, f, indent=4)
                    
                # For Roo Code / Cline
                for ext_dir in [".roo", ".cline"]:
                    ide_dir = os.path.join(target_folder, ext_dir)
                    if not os.path.exists(ide_dir): os.makedirs(ide_dir)
                    with open(os.path.join(ide_dir, "mcp_settings.json"), "w") as f:
                        json.dump(mcp_config, f, indent=4)

            print("Created MCP configs for IDEs after server was ready")
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
                
        print("Uvicorn server exited.")
        
    except Exception as e:
        print(f"CRITICAL ERROR in start_mcp_server: {e}")
        try:
            with open(os.path.join(ScriptsFolder, "mcp_server_panic.log"), "w") as f:
                f.write(f"Panic: {e}\n")
                traceback.print_exc(file=f)
        except: pass
        traceback.print_exc()




@mcp.tool()
@run_in_main_thread
def get_full_menu_map_json(query: str = "") -> str:
    """Returns a complete JSON map of all 3DCoat menus, submenus, and commands globally available.
    Use this tool when the user asks "Where is tool X?", "How do I do Y?", or to find the location and English_Hint of tools.
    If the output is too long and gets truncated, provide a 'query' parameter to filter by name or description.
    The map provides the tool's 'id', 'menu_path', 'room_context', 'English_Text', 'English_Hint', and 'python_api_command'.
    You can directly execute the python_api_command (e.g., coat.ui.cmd("SAVE_FILE")) to activate the tool.
    """
    try:
        import coat
        if hasattr(coat.ui, "getFullMenuMapAsJSON"):
            json_str = coat.ui.getFullMenuMapAsJSON()
            if not query:
                return json_str
            import json
            data = json.loads(json_str)
            filtered = []
            q = query.lower()
            for item in data.get("3DCoat_Menu_Map", []):
                if q in item.get("id", "").lower() or \
                   q in item.get("menu_path", "").lower() or \
                   q in item.get("English_Text", "").lower() or \
                   q in item.get("English_Hint", "").lower():
                    filtered.append(item)
            return json.dumps({"3DCoat_Menu_Map": filtered}, indent=2)
        else:
            return "Error: getFullMenuMapAsJSON is not available in this build of 3DCoat. Please recompile the application."
    except Exception as e:
        import traceback
        return f"Error executing getFullMenuMapAsJSON:\n{traceback.format_exc()}"

lockPreprocess = False
class DevToolsExtension(cExtension):
    def __init__(self):
        cExtension.__init__(self)

    def onStart(self):
        cExtension.begin_work_in_bg()
        # When running the script in 3DCoat, the server starts in the background
        server_thread = threading.Thread(target=start_mcp_server, daemon=True)
        server_thread.start()


    def preprocess(self):
        global lockPreprocess
        if lockPreprocess:
            return
        lockPreprocess = True   
        try:
            tasks_to_run = []
            with task_queue_lock:
                if task_queue:
                    tasks_to_run = list(task_queue)
                    task_queue.clear()
            
            for task in tasks_to_run:
                try:
                    task["result"] = task["func"](*task["args"], **task["kwargs"])
                except Exception as e:
                    import traceback
                    task["error"] = e
                    print(f"Error in main thread task {task['func'].__name__}:\n{traceback.format_exc()}", file=sys.stderr)
                finally:
                    task["event"].set()

        except Exception as e:
            import traceback
            print(f"Preprocess error:\n{traceback.format_exc()}", file=sys.stderr)
        finally:
            lockPreprocess = False

    def postprocess(self):
        pass

    def prerender(self):
        pass

    def postrender(self):
        pass

    def onExit(self):
        pass


devToolsExtension = DevToolsExtension()


# --- Antigravity UI Integration ---
import cTemplates.MainMenu.Scripts
from cTemplates.Structs import d_slot, d_menu_section
import os
import subprocess
import shutil
import platform
import webbrowser

def open_antigravity_download():
    """Направляє користувача на сайт для завантаження GUI."""
    print("\n🌐 Відкриваємо офіційну сторінку для завантаження графічного Antigravity...")
    download_url = "https://antigravity.google/download"
    webbrowser.open(download_url)

@d_slot
def OpenInAntigravity():
    import coat
    project_dir = coat.io.documents("UserPrefs/Scripts")
    
    if platform.system() == "Windows":
        gui_path = os.path.expandvars("%LOCALAPPDATA%/Programs/Antigravity/Antigravity.exe")
        if os.path.exists(gui_path):
            subprocess.Popen([gui_path, project_dir])
            return
            
    elif platform.system() == "Darwin":
        mac_path = "/Applications/Antigravity.app"
        if os.path.exists(mac_path):
            subprocess.Popen(["open", "-a", mac_path, project_dir])
            return
            
    print("⚠️ Графічна версія Antigravity (чат) не знайдена.")
    open_antigravity_download()

@d_slot
def OpenInAntigravityIDE():
    import coat
    project_dir = coat.io.documents("UserPrefs/Scripts")
    
    if platform.system() == "Windows":
        ide_path = os.path.expandvars("%LOCALAPPDATA%/Programs/Antigravity IDE/Antigravity IDE.exe")
        if os.path.exists(ide_path):
            subprocess.Popen([ide_path, project_dir])
            return
            
    elif platform.system() == "Darwin":
        mac_path = "/Applications/Antigravity IDE.app"
        if os.path.exists(mac_path):
            subprocess.Popen(["open", "-a", mac_path, project_dir])
            return
            
    print("⚠️ Antigravity IDE не знайдено.")
    open_antigravity_download()

@d_menu_section(cTemplates.MainMenu.Scripts.Scripts_S_Useful)
def _ag_menu():
    coat.menu_item(OpenInAntigravity.UICmd())
    coat.menu_item(OpenInAntigravityIDE.UICmd())


