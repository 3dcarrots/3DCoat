import asyncio
import json
import os
import sys

# Inject local libs directory into sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LIBS_DIR = os.path.join(SCRIPT_DIR, "libs")
if os.path.exists(LIBS_DIR):
    sys.path.insert(0, LIBS_DIR)

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from google.genai import types
from contextlib import AsyncExitStack

async def run():
    async with AsyncExitStack() as stack:
        port = 53186 # Default fallback, normally read from config
        mcp_url = f"http://127.0.0.1:{port}/mcp"
        
        # Read port from config if possible
        try:
            with open(os.path.expanduser(r'~/.gemini/antigravity/mcp_config.json'), 'r') as f:
                config = json.load(f)
                mcp_url = config.get("mcpServers", {}).get("3dcoat-live", {}).get("serverUrl", mcp_url)
        except Exception:
            pass
            
        print(f"Connecting to {mcp_url}...")
        
        try:
            transport = await stack.enter_async_context(streamablehttp_client(mcp_url))
            session = await stack.enter_async_context(ClientSession(transport[0], transport[1]))
            await session.initialize()
            
            tools_response = await session.list_tools()
            tools = tools_response.tools
            print(f"Got {len(tools)} tools:")
            
            def convert_schema(schema):
                if not schema:
                    return None
                    
                tType = types.Type.OBJECT
                if schema.get("type") == "string": tType = types.Type.STRING
                elif schema.get("type") == "integer": tType = types.Type.INTEGER
                elif schema.get("type") == "number": tType = types.Type.NUMBER
                elif schema.get("type") == "boolean": tType = types.Type.BOOLEAN
                elif schema.get("type") == "array": tType = types.Type.ARRAY
                
                props = {}
                if "properties" in schema:
                    for k, v in schema["properties"].items():
                        props[k] = convert_schema(v)
                        
                return types.Schema(
                    type=tType,
                    description=schema.get("description", ""),
                    properties=props if props else None,
                    required=schema.get("required") if schema.get("required") else None
                )
            
            for t in tools:
                gemini_tool = types.FunctionDeclaration(
                    name=t.name.replace("-", "_"),
                    description=t.description,
                    parameters=convert_schema(t.inputSchema)
                )
                print(gemini_tool)
        except Exception as e:
            print("Error", e)

if __name__ == "__main__":
    asyncio.run(run())
