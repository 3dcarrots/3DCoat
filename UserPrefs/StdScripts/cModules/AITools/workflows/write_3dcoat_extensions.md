---
description: how to write or edit 3DCoat cExtensions
---
Before creating or editing any 3DCoat extensions (cExtensions), you MUST follow these steps:

1. Read the core rules: Use the `view_file` tool to read `.agent/rules/core.md` (relative to the workspace root).
2. Read the API rules for extra context on 3DCoat API: `view_file` on `.agent/rules/api.md` (relative to the workspace root).
3. Follow Rule 6 in `core.md` EXACTLY. Store your extensions correctly in `cExtensions/ExtensionName/`.
4. Look at examples inside `cModules/` to understand how extensions are written.
