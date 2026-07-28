import os
import json
import sys
from google import genai

config_path = r"C:\Users\carro\.gemini\antigravity\mcp_config.json"
try:
    with open(config_path, "r") as f:
        config = json.load(f)
        api_key = config.get("mcpServers", {}).get("3dcoat-live", {}).get("env", {}).get("GEMINI_API_KEY", "")
except:
    pass

if not api_key:
    # Try reading from the extension's local save file
    key_file = os.path.join(os.path.expanduser("~"), "Documents", "3DCoat", "UserPrefs", "AIAssistant.apikey")
    try:
        with open(key_file, "r") as f:
            api_key = f.read().strip()
    except:
        api_key = os.environ.get("GEMINI_API_KEY", "")

client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta'})
for m in client.models.list():
    if "gemini-2.5" in m.name or "gemini-3.1" in m.name or "flash" in m.name:
        methods = getattr(m, 'supported_generation_methods', [])
        if isinstance(m, dict):
            methods = m.get('supported_generation_methods', [])
        print(f"{m.name}: {methods}")
