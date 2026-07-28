# 3DCoat Python API: The Master Guide for AI Agents

This is the definitive, exhaustive guide for AI agents (like Antigravity and Cursor) operating within the 3DCoat environment. It provides a complete breakdown of all internal modules, their specific responsibilities, and how to effectively navigate the API using MCP tools.

---

## 1. Core Principles & Navigating via MCP

You do not have a traditional web documentation link. You **MUST** use the provided MCP tools to explore the API dynamically. The C++ bindings dictate strict type requirements (e.g., using `cVec3` instead of Python tuples), so guessing method signatures will result in errors.

**Tool:** `mcp_3dcoat-live_get_python_api_sources(read_file="...")`
- **Without arguments:** Returns the complete directory tree of all available Python API files.
- **With `read_file="path/to/file.py"`:** Returns the raw source code of that specific API file.

**Your Standard Operating Procedure (SOP):**
1. **Identify the Domain:** Determine what the user wants to do (e.g., UI drawing, scene modification, primitive generation).
2. **Find the Module:** Consult Section 2 of this guide to locate the correct file (e.g., `cPy/PrimAPI.py` for primitives).
3. **Read the Source:** Execute `get_python_api_sources(read_file="cPy/PrimAPI.py")` to check the exact class names, Enums, and method signatures.
4. **Import and Execute:** Write your script using the correct types from `cPy.cTypes` and execute it via `mcp_3dcoat-live_run_script_from_source`.

> [!IMPORTANT]
> **Importing Modules:** All of the files listed by `get_python_api_sources` can be imported directly into your scripts as modules. To do this, simply replace all slashes (`/`) with dots (`.`) and remove the `.py` extension. For example, to import the file `cTemplates/MainMenu/Scripts.py`, you would write:
> `import cTemplates.MainMenu.Scripts`

---

## 2. The `Bridge` Module (C++ Bindings)

The `Bridge` directory (specifically the `cPy/` subfolder) contains the core C++ bindings. This is where 95% of your programming will take place. `coat.py` serves as a global entry point that imports many of these core functions.

### Math, Arrays & Types
*   **`cPy/cTypes.py`**: The fundamental building blocks. Contains `cVec2`, `cVec3`, `cVec4`, `cMat4`, `cQuat`, `cRect`, and `cStr`. **Crucial:** You must instantiate and pass these specific classes to API methods, primitive Python types will fail.
*   **`cPy/cArray.py`**: Contains `cArray_int`, `cArray_float`, `cArray_double`. Used when methods require or return raw C++ style arrays of fundamental types.

### Scene Hierarchy & State
*   **`cPy/cScene.py`**: **The VoxTree Controller.** Contains `VoxTreeBranch` for manipulating the layer hierarchy. Use this for boolean operations between layers (`SubObj`, `MergeObj`), applying matrix transformations to whole branches (`SetTransform`), and visibility toggles.
*   **`cPy/CoreAPI.py`**: Global state and broad commands. Contains functions like `coat.menu_item()`, room/file existence checks, and the `Mesh` class definition. Contains the `BoolOpType` enum necessary for scene boolean operations.

### Primitives, Sculpting & Volumes
*   **`cPy/PrimAPI.py`**: **Primitive Generation.** Contains the abstract `prim` class and structural shapes (e.g., `box`, `sphere`, `SpiralProfile`, `ThreadProfile`). Use this for procedural generation (e.g., setting radius, scale, translation, color, and merging primitives into the volume).
*   **`cPy/cModel.py`**: **The Sculpt Room Core.** Defines `VolumeObject`, representing the raw voxel/surface data. Contains methods for spatial lookups (`ABOcTree`, `SpOcTree`), smoothing, carving, generating cavity details, and querying exact volumetric values at specific `cVec3` locations.

### Painting & Texturing
*   **`cPy/cPaint.py`**: **The Paint Room Core.** Defines `PPPObject` (Paint Object) and `PaintRoom`. Used for loading/exporting meshes specifically for painting, and loading color textures directly into layers.
*   **`cPy/cImage.py`**: **Image Buffers.** Defines the `cImage` class for handling raster data, mipmaps, extracting pixels (`GetPixelR8`), flipping/resizing, and converting pixel formats to prepare for OpenGL textures.

### Rendering & UI Output
*   **`cPy/cRender.py`**: **Viewport UI & Rendering.** Extremely important for custom overlays. Contains `RenderUtils` which provides methods like `draw_text()`, `draw_on_screen()`, `drawThickLine()`, `drawThickCircle()`. It also manages Frame Buffer Objects (FBOs) and texture creation (`CreateGPUTexture`), using the `image_format` enum.

### I/O, Configuration, Base Classes & IDE
*   **`cPy/cIO.py`**: **File System & Archives.** Contains `cFileDisk` and `cFile` for raw binary reading/writing. Contains `cIO` for mounting ZIP archives, throwing Open/Save dialogs (`SelectFolderDialog`, `LoadImageDialog`), and finding system paths.
*   **`cPy/cOptions.py`**: **Application Settings.** Contains the massive `AppOptions` class. This handles everything from grid color (`AppOptions.GridColor`) to performance settings, auto-save timers, and UI theme colors.
*   **`cPy/cCore.py`**: **Serialization & Fundamentals.** Contains `BaseClass`, the root class for UI registration and XML serialization. Use this when you need deeply integrated custom data structures that save with the 3DCoat project.
*   **`cPy/cIDE.py`**: **IDE & Terminal Output.** Contains `PythonTerminal` and `cIDE`. Useful for manipulating the internal script editor or intercepting Python console prints.
*   **`cPy/Legacy.py` (and `CMD.py`)**: **Legacy UI Commands.** A massive collection of older global functions like `ShowFloatingText`, `ModalDialogYesNo`, `GetSliderValue`, and specific tool triggers (e.g., `voxelize()`, `autopo()`). It also contains basic `PrimTranslate` and `PrimScaleAt` state methods.
*   **`cPy/cList.py` & `cPy/ClassArray.py`**: **Advanced Collections.** Dynamic arrays and list wrappers for specific types (e.g., `cList_int`, `ClassArray_NGComponent`).
*   **`cPy/cUI.py`**: Contains `RoomBehavior` and `CustomRoom` for scaffolding entire new workspaces.
*   **`cPy/cNodeSystem.py`**: Contains `NodeGraph`, `BaseNode`, used for interacting with the material and shader node editors.

---

## 3. The `StdScripts` Module (Built-in Extensions)

This directory houses the Python code that implements 3DCoat's standard toolsets, menus, and developer utilities.

*   **`cModules/DevTools/DevTools.py`**: The MCP Server. Look here if you need to understand how the agent communicates with the host application.
*   **`cModules/QT/QT.py`**: **PySide6 / PyQt Integration.** Shows how 3DCoat injects `app.processEvents()` into the `prerender` and `postprocess` loops to run Qt windows inside the host application without blocking the main thread.
*   **`cModules/RealityCapture/RealityCapture.py` & `cModules/VideoTo3D.py`**: **External Integrations.** Shows how 3DCoat talks to external apps (Epic Games RealityCapture) via `subprocess.run`, and how it uses `cv2` (OpenCV) to extract sharp frames from video for photogrammetry.
*   **`cModules/PythonTerminal/` & `cModules/IDE/`**: The actual implementations of the in-app script editor and console.
*   **`cTemplates/menu.py`**: **The Main Menu.** Constructs the top application menu bar (File, Edit, View) utilizing standard decorators.
*   **`cTemplates/navigation.py`**: **Viewport Controls.** Defines the camera navigation bar, grid snapping, and environment map toggles.
*   **`cTemplates/MainMenu/*`**: Sub-files for every single dropdown menu (e.g., `Scripts.py`, `Bake.py`, `Geometry.py`). They show how to attach functions using `@d_menu_section` decorators.
*   **`cTemplates/sculptTools.py`, `paintTools.py`, `retopoTools.py`, `CADTools.py`, `curves.py`**: UI layouts for the left-hand toolbars and dedicated right-click menus. These files show how 3DCoat populates toolboxes using commands like `coat.tools_item("[StdPen]StdPen")` for specific rooms (Voxel, Paint, Retopo, Free Surface). Look here if the user wants to add a custom tool button to the UI.
*   **`cTemplates/voxTreeRmb.py`**: **Context Menus.** Shows how the Right-Click menu is built in the VoxTree using `@d_rmb_menu`. Useful for adding custom right-click actions to layers.
*   **`cModules/DataTree.py` & `NodeSystem.py`**: Examples of how extensions and property generation work under the hood.

---

## 4. The `Rooms` Module (Workspace Contexts)

Rooms represent the main UI tabs at the top of 3DCoat (Voxel Sculpting, Retopo, UV, Paint, Render).

*   **`CustomRooms/<RoomName>/room.py`**: Each room has a file that inherits from `cTemplates.Rooms.RoomBehavior`.
*   **`CustomRooms/<RoomName>/Tools.py` & `RMBMenu.py`**: Specifies the exact tools and right-click menus available *only* when that room is active.
*   **Usage**: You can override methods (e.g., `OnStartPage()`) to automatically trigger scripts, change `AppOptions`, or modify the layout whenever the user switches into that specific workspace.

---

## 5. Practical Agent Workflows & Snippets


### Scenario B: Custom Viewport UI (`cRender.py`)
If the user asks to "Draw some text on the screen":
```python
from cPy.cRender import RenderUtils

# draws white text at x=100, y=100
RenderUtils.draw_text(100.0, 100.0, "Hello 3DCoat!", 1.0, 1.0, 1.0, 1.0)
```


### Scenario D: Raw Volumetric Editing (`cModel.py`)
If the user asks to "Query the scene density at a coordinate":
```python
import coat
from cPy.cTypes import cVec3

# Assuming VoxTree item 0 is active VolumeObject
branch = coat.GetVoxTree().GetItem(0)
if branch and branch.GetVolume():
    volume = branch.GetVolume()
    # Get density value at specific world coordinate
    val = volume.GetVolumetricValue(cVec3(0.0, 10.0, 0.0))
    print(f"Density: {val}")
```

### Final Reminder
Never assume you know the methods of `VolumeObject`, `VoxTreeBranch`, `RenderUtils`, or `AppOptions`. Use `mcp_3dcoat-live_get_python_api_sources` to **read the specific file** to check exactly what methods are available and what `cPy.cTypes` they expect before executing your code.


### 3DCoat cmd execution

3DCoat cmd execution is done using the `CMD.cmd` function. The function has only one argument is the name of the command:

```python
import CMD

CMD.cmd("$SHOW_GRID_3D")
```

or 

```python
import coat

coat.ui.cmd("$SHOW_GRID_3D")
```

You can find examples of commands in all `tools_item` and `menu_item` function calls located in the `cTemplates/MainMenu` folders and its subfolders, as well as in the files `cTemplates/sculptTools.py`, `cTemplates/paintTools.py`, `cTemplates/retopoTools.py`, `cTemplates/CADTools.py`, and `cTemplates/curves.py`. Passing the same argument to the `CMD.cmd` function will execute the exact same command as in those `tools_item` or `menu_item` calls. Each command is accompanied by a comment describing its functionality.