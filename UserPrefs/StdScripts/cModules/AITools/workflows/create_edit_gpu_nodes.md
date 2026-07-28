---
description: how to create or edit 3DCoat GPU Nodes (GLSL)
---
Before creating or editing any 3DCoat GPU Nodes (.glsl files, NodeGraph Language), you MUST follow these steps:

1. Read the core rules: Use the `view_file` tool to read `.agent/rules/core.md` (relative to the workspace root).
2. If the user asks about NGL, try to find and read `.agent/rules/ngl.md` if it exists.
3. Follow the exact directory structure rules specified in `core.md` (Rule 4 and 5) for saving and modifying nodes in the `GPUNodes` folder.
4. Use `mcp_3dcoat-live_get_std_GPU_Nodes` to check existing node structures and get their source code before making changes.
