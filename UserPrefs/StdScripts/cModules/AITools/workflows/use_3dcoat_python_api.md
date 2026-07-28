---
description: how to write or edit Python scripts for 3DCoat API
---
Before writing any Python script or using the 3DCoat Python API, you MUST follow these steps:

1. Read the core rules: Use the `view_file` tool to read `.agent/rules/core.md` (relative to the workspace root).
2. Read the API guide: Use the `view_file` tool to read `.agent/rules/api.md` (relative to the workspace root).
3. Follow the instructions in `api.md` EXACTLY. 
4. Always use `mcp_3dcoat-live_get_python_api_sources` to read the specific C++ bindings source files before writing your code to avoid guessing the API.
5. Use `mcp_3dcoat-live_run_script_from_source` to test your generated scripts dynamically without saving them to a file.
