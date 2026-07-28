# 3DCoat Extension (cExtensions) Creation Guide

This document is an extremely detailed and comprehensive guide for creating extensions (cExtensions) purely in 3DCoat. Use this information ALWAYS when the user asks to write a new application, tool, interface, script, or integration with other software. This guide is based on 3DCoat's architecture and the best practices of existing modules (MouseTest, AVIF, DocBuilder, RealityCapture).

---

## 1. Basic Rules for Creating Extensions (cExtensions)

If the user wants to write an extension (cExtensions), extensions are written exactly like modules. You can look at how modules are written in the `cModules` folder, and write extensions following their example. However, extensions are stored in the current project's folder, in the `cExtensions` subfolder. Then, there should be a folder with the extension's name, and a `.py` file containing an instance of a class inherited from `cExtension` (this is the file that will be imported when the extension is activated).

---

## 2. What are cExtensions and where to create them?

Extensions (cExtensions) are 3DCoat's mechanism for adding new functionality that loads along with the application or can be toggled by the user in the "Extensions" window.

**Location:**
As per rule 6, extensions are stored in the current project's folder `UserPrefs/Scripts/cExtensions/`.
The structure must be as follows:
`UserPrefs/Scripts/cExtensions/MyNewTool/MyNewTool.py`

This file MUST instantiate a class that inherits from `cPy.cCore.cExtension`. 3DCoat will automatically scan this folder, find the file, and register the extension.

---

## 3. Basic Extension Structure and Lifecycle

Inheriting from `cPy.cCore.cExtension` grants access to several critical render and framerate events.

```python
import cPy.cCore
import coat

class MyFirstExtension(cPy.cCore.cExtension):
    def __init__(self):
        # We must initialize the parent class
        cPy.cCore.cExtension.__init__(self)

    def onStart(self):
        # Called when the user activates the extension (Clicks Start)
        # Perfect place for initializing servers, registering codecs, adding hooks
        print("MyFirstExtension started!")

    def preprocess(self):
        # Called on every frame BEFORE 3DCoat's core logic processing
        # Use for intercepting inputs or modifying global states
        pass

    def postprocess(self):
        # Called on every frame AFTER 3DCoat's core logic
        pass

    def prerender(self):
        # Called BEFORE rendering the 3D scene
        pass

    def postrender(self):
        # Called AFTER rendering the scene
        # Crucial: This is the BEST place for drawing 2D elements (text, UI) in the viewport!
        pass

    def onExit(self):
        # Called when the extension is disabled or 3DCoat closes
        print("MyFirstExtension exited!")

# INSTANCE: You must create an instance of the class in the file's global scope!
myFirstExtension = MyFirstExtension()
```

---

## 4. Adding UI Commands (Menus and Interfaces)

To allow the user to interact with the extension, you need to add menu items.

### Using `@d_slot` and `@d_menu_section` Decorators

3DCoat uses a decorator system to register menus:

1.  **`@d_slot`**: Registers a standard function as a UI command.
2.  **`@d_menu_section`**: Attaches an array of items to an existing menu section.

**Example (From the MouseTest extension):**
```python
import coat
from cTemplates.Structs import *
import cTemplates.MainMenu.View

ShowMouseInfo = True

# Function to be called when the menu item is clicked. 
# We use the @d_slot decorator to expose its UICmd() for the coat.menu_item function.
@d_slot
def ToggleMouseInfo():
    global ShowMouseInfo
    ShowMouseInfo = not ShowMouseInfo

# We create a dedicated section for our extension under the View menu.
@d_menu_section(cTemplates.MainMenu.View.CreateViewMenu)
def MouseInfoSection():
    # We add a menu item to this section, mapping it to the toggle function.
    coat.menu_item(ToggleMouseInfo.UICmd())
```
*Note: Other menu examples are found in `cTemplates.MainMenu.Scripts.Scripts_S_Useful`.*

---

## 5. Mouse Interaction and Viewport (RenderUtils & CMD)

3DCoat provides powerful means for rendering graphics and handling the cursor via the `CMD` and `cPy.cRender` modules. This is demonstrated in the **MouseTest** extension.

### Getting Mouse / Cursor State:
-   `CMD.GetMouseX()`, `CMD.GetMouseY()`: Screen coordinates of the cursor.
-   `coat.io.cursorPos()`: Another way to get coordinates (returns a structure).
-   `CMD.LMBPressed()`, `CMD.MMBPressed()`, `CMD.RMBPressed()`: Boolean states for mouse buttons.
-   `CMD.WheelPressed()`: Mouse wheel state.
-   `CMD.GetVisiblePenRadius()`: Screen-space radius of the active brush.

### Drawing in the Viewport (in `postrender`):
-   **Drawing text**: `cPy.cRender.RenderUtils.draw_text(x, y, "My Text")`
    *Example: `cPy.cRender.RenderUtils.draw_text(300, 200, f"Pos: {CMD.GetMouseX()}")`*
-   **Raycasting to object**:
    Check if the cursor is hovering over a model:
    `if CMD.ScreenRayPicksObject(CMD.GetMouseX(), CMD.GetMouseY()):`
-   **Getting 3D coordinates at hover/click location**:
    `pickPos: coat.vec3 = cPy.cRender.RenderUtils.PickPointSpacePos()`
-   **Drawing 3D Primitives (spheres)**:
    `cPy.cRender.RenderUtils.drawCoolSphere(pickPos, 10.0, int("FF00FFFF", 16))` — draws a Magenta sphere of radius 10.0.

**Pro-tip:** Perform ALL drawing operations STRICTLY within the `postrender()` function of your `cExtension` class!

---

## 6. Working with Codecs and Images (AVIF cImageCodec)

You can add support for new image formats by creating a custom Image Codec. The **AVIF** extension is a prime example.

To do this:

1.  Create a class inheriting from `cPy.cIO.cImageCodec`.
2.  Override the `Decode(self, Src: cPy.cIO.cFile, To: cPy.cImage.cImage)` and `Encode(self, Image: cPy.cImage.cImage, To: cPy.cIO.cFile)` methods.
3.  Register it via `cPy.cIO.cIO.AddCodec(...)`.

**Registration Example:**
```python
class AVIFCodec(cPy.cIO.cImageCodec):
    def __init__(self):
        cPy.cIO.cImageCodec.__init__(self)

    def Decode(self, Src: cPy.cIO.cFile, To: cPy.cImage.cImage):
        # Format decoding...
        pass

class AVIFExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)

    def onStart(self):
        self.avifCodec = AVIFCodec()
        cPy.cIO.cIO.AddCodec("AVIF", self.avifCodec)

avifExtension = AVIFExtension()
```

### Working with Numpy and Images:
Often, extensions use `numpy` for processing (like `np.ndarray` in the AVIF example). To pass a `numpy` array to a 3DCoat `cImage` object or vice-versa:
- To load: `img_array = np.asarray(Image)`
- To save back: `cPy.CoreAPI.Image.cImageFromArray(img_array, To)` where `To` is a `cPy.cImage.cImage`.
*Warning: You may sometimes need to flip the image vertically for 3DCoat: `img_array = np.flip(img_array, axis=0)`*

---

## 7. Settings and Dialogs

### Serializing settings via `BaseClass`
To create a settings menu whose values persist in 3DCoat's preferences:
1. Create a class inheriting from `cPy.cCore.BaseClass` decorated with `@d_class`.
2. Use variables of types `cPy.cCore.cSInt`, `cPy.cCore.cSBool`, `cPy.cCore.cSFloat`.
3. In the `pySerialize(self)` method, register them for the UI.

```python
@d_class
class AVIFSettings(cPy.cCore.BaseClass):
    def __init__(self):
        cPy.cCore.BaseClass.__init__(self)        
        # Title, default value, minimum, maximum
        self.quality = cPy.cCore.cSInt("Quality", 80, 0, 100)
        self.speed = cPy.cCore.cSInt("speed", 3, 0, 10)
        self.greyscale = cPy.cCore.cSBool("greyscale")

    def pySerialize(self):
        # UI registration for rendering
        cPy.cCore.cREG.slider_int(self.quality)
        cPy.cCore.cREG.slider_int(self.speed)
        # cPy.cCore.cREG.checkbox(self.greyscale)

avifSettings = AVIFSettings()
```

### Modal MessageBox Windows
To present the above settings to the user in a pop-up window and await their selection:
```python
# Returns 1 (OK) or 2 (Cancel)
flag = cPy.cCore.cREG.modalMessageBox("MyDialog", "Export Settings", "Ok,Cancel", 1, avifSettings)
if flag == 1:
    print(f"Chosen quality: {avifSettings.quality.Value}")
```

### Interactive dialogs via `coat.dialog()`
There is an alternative approach (used in RealityCapture) when you don't need persistent settings, but require tighter control over input types:
```python
class VideoTo3DDialog:
    def __init__(self):
        self.shotCount = 300
        self.inputVideo = ''
        self.rcprojFile = ''

    def ui(self):
        return [
            "shotCount", 
            "inputVideo,load:*.*", # File load dialog
            "rcprojFile,save:*.rcproj", # File save dialog
        ]

videoTo3DDialog = VideoTo3DDialog()
# Display the window
if coat.dialog().ok().cancel().params(videoTo3DDialog).caption("Video Settings").show() == 1:
    print(videoTo3DDialog.inputVideo)
```

## 8. GPU Computing and Compute Shaders (NGL)

Python scripts in 3DCoat can offload heavy image processing or other workloads to the GPU using NGL nodes (NodeGraph Language - a GLSL-like shader language) and FBOs (Frame Buffer Objects).

### Initializing and Loading Shaders
To load a shader from a `.glsl` file, use the `cPy.cNodeSystem` module:
```python
import cPy.cNodeSystem

# Initialize the node graph
nodes = cPy.cNodeSystem.NodeGraph()
# Load the file and assign a unique node name
nodes.LoadNGLFile("D:/my_shader.glsl", "MyComputeNode")
```

### Creating and Managing FBOs (Render Targets)
To store GPU computation results or intermediate data, you need FBOs, created via `cPy.cRender`:
```python
import cPy.cRender

width, height = 8192, 4320
# Create an FBO with the required format (Rgb32f, Rgba32f, Rgb8, etc.)
my_fbo = cPy.cRender.RenderUtils.CreateFBO(width, height, cPy.cRender.image_format.Rgb32f)

# Clear the FBO
cPy.cRender.RenderUtils.clear(my_fbo, [0, 0, 0, 0])

# IMPORTANT: Always delete textures/FBOs from the GPU when they are no longer needed to prevent memory leaks
# cPy.cRender.RenderUtils.DeleteGPUTexture(my_fbo)
```

### Passing Data and Computing
Before executing the shader, you must supply it with parameters (Uniforms) and textures:
```python
# Pass numeric values (SetProperty)
nodes.SetProperty("MyComputeNode", "radius", 5.0)
nodes.SetProperty("MyComputeNode", "direction", 0.0, 1.0, 0.0, 1.0) # For vectors

# Bind textures (DefineTexture)
nodes.DefineTexture(":SourceTXT", source_texture_id)
nodes.DefineTexture(":ResultTXT", my_fbo)

# Execute the GPU computation
nodes.ComputeRender()
```

### Interacting with `coat.Image` and Numpy
To convert between FBOs, `coat.Image`, and memory arrays (e.g., `numpy` with OpenCV `cv2`):
```python
import numpy as np
import coat

# Create an empty image via coat
imgBuf = coat.Image()

# Read pixels from the FBO into RAM
imgBuf.FromTexture(my_fbo)

# Upload a numpy array to a GPU texture
# bufDst_numpy_array = np.empty((height, width, 3), np.dtype('uint8'))
# imgBuf.FromArray(bufDst_numpy_array) # Or imgBuf.Paste(bufDst_numpy_array, x, y)
# srcTextureId = imgBuf.ToTexture()
```

These tools allow for creating extensions that demand complex pixel processing.

---

## 9. System Command Execution (Subprocess)

Modules like **DocBuilder** or **RealityCapture** rely on external executables (e.g., Sphinx or RealityCapture.exe). It is completely safe to use the standard Python `subprocess` library to launch them. 3DCoat manages Python subprocesses without issue.

```python
import subprocess

# Calling an external application (Always use quotes around paths when necessary)
cmdLine = f'"{RealityCapturePath}" -addFolder "{imageFolder}" -save "{rcprojFile}" -quit'
subprocess.run(cmdLine, shell=True)
```

For internal Python modules, like in **DocBuilder**, you can dynamically load modules via `importlib` (a useful practice to avoid cramming all code into a single cExtension file):
```python
import importlib
@d_slot
def RebuildDocumentation():
    sphinx_builder = importlib.import_module("cModules.DocBuilder.sphinx_builder")
    sphinx_builder.main()
```

---

## 10. Object Integration with the Scene Tree (Linked Objects)

In the `RealityCapture` example, there is functionality to link an external project file (`.rcproj`) directly to a branch in 3DCoat's VoxTree.

```python
# Import the object into the scene
coat.Scene.importMesh("path/to/model.obj")

# Link the external file to the imported mesh (the current VoxTree layer)
coat.Scene.current().addLinkedPath("path/to/project.rcproj")
coat.Scene.current().rename("ProjectNode")
coat.Scene.current().setReferenceColor(coat.vec4(1,0,0,1))
```

Adding specialized Context Menu commands to the Right-Mouse Button (RMB) menu for these linked objects:
```python
self.linkedType = cPy.cCore.LinkedObjectBaseType()
self.linkedType.setObjectType("rcproj") # Trigger extension
# Adds an action to the VoxTree layer context menu for this file type
self.linkedType.addAction("RealityCapture Group", "BakeUVTextures")
self.linkedType.addAction("RealityCapture Group", "ReloadModel")
cPy.cCore.LinkedObjectBaseType.registerObjectType(self.linkedType)
```

When the user clicks the menu item on the layer, your `cExtension` receives a message in its `onMessage` method:
```python
def onMessage(self, message):
    if message == "BakeUVTextures": 
        self.realityCaptureEngine.BakeUVTextures()
    if message == "ReloadModel": 
        self.realityCaptureEngine.ReloadModel()
```

---

## 11. Debugging and Development

- **Editing in Visual Studio Code**: It's most convenient to edit files by opening `Documents\3DCoat\UserPrefs\Scripts` in VS Code. You'll see documentation in hover hints and can jump to definitions via Ctrl+Click.
- **Debugger**: To activate the debugger, simply press F5 in Visual Studio Code after starting 3DCoat.
- 3DCoat ships with and runs on embedded Python environments (3.9/3.10), so importing third-party or native libraries (`os`, `sys`, `time`, `pathlib`) works seamlessly.
- **Hot Reloading**: Changes in cExtensions (as they register on startup) often require a full 3DCoat restart or at least deactivating and reactivating the extension within the Extensions window (via "Stop" -> "Start").
- **Logs**: To debug the MCP agent itself, look at the `mcp_server_panic.log` or `mcp_server.log` files in the Scripts folder. Standard `print()` outputs are also mirrored in 3DCoat's internal Scripting console.

---

## 12. Additional UI / Interaction Utilities

-   **System Dialogs for Files/Folders**:
    -   Open file: `coat.io.openFileDialog("*.*")` (Format masks like `*.png;*.jpg` can be used).
    -   Save file: `coat.io.saveFileDialog("*.rcproj")`
-   **Progress Bars**: 
    If your extension performs a lengthy operation, inform the user:
    `coat.io.progressBar(current_step, total_steps, "Message...")`
-   **3DCoat Internal Commands (`cmd` execution)**:
    3DCoat cmd execution is done using the `CMD.cmd` function. The function takes a single argument, the command name:
    ```python
    import CMD
    CMD.cmd("$SHOW_GRID_3D")
    
    # Or via coat
    import coat
    coat.ui.cmd("$SHOW_GRID_3D")
    ```
    You can find examples of commands in all `tools_item` and `menu_item` function calls located in the `cTemplates/MainMenu` folders and its subfolders, as well as in `cTemplates/sculptTools.py`, `cTemplates/paintTools.py`, `cTemplates/retopoTools.py`, `cTemplates/CADTools.py`, and `cTemplates/curves.py`. Passing the identical argument to the `cmd` function will trigger the exact same macro. Each command typically has a descriptive comment next to it.

## 13. API Architecture Overview (`cPy/`)

When writing extensions, you must know where to find functions within the 3DCoat API. Always use the `mcp_3dcoat-live_get_python_api_sources(read_file="...")` command to inspect signatures and available methods BEFORE calling them.

Here is a basic breakdown of the API modules relevant for extensions:

- **`cPy.cTypes`**: Fundamental types (`cVec2`, `cVec3`, `cVec4`, `cMat4`, `cQuat`, `cRect`, `cStr`). **Critical:** You must use these specific classes, not standard Python Tuples or arrays.
- **`cPy.cScene`**: Scene object management (VoxTree). `VoxTreeBranch` allows for boolean operations (`SubObj`, `MergeObj`), setting visibility, and applying transformation matrices (`SetTransform`).
- **`cPy.cModel`**: The core of the Sculpt Room space. The `VolumeObject` class provides access to `ABOcTree` and `SpOcTree` for spatial queries and fetching volume densities `GetVolumetricValue(cVec3)`.
- **`cPy.PrimAPI`**: Geometry generation (spheres, boxes, spirals) via `prim` classes. Useful for setting radii, offsets, or colors of procedural primitives prior to merging.
- **`cPy.CoreAPI`**: Access to the `Mesh` class, and mechanisms for checking room or file existence.
- **`cPy.cPaint` and `cPy.cImage`**: Tools for painting, importing/exporting PPP objects, and the raw pixel buffer `cImage` (allowing format conversions and mipmap generation).
- **`cPy.cOptions`**: The `AppOptions` class provides global access to software preferences (dimensions, colors, grids).
- **Building Custom Workspace Rooms**: To create an entirely new proprietary tab (Room), set up subdirectories inside `CustomRooms/` and inherit from `cTemplates.Rooms.RoomBehavior`. You can override `OnStartPage()` to initialize specific tools whenever the user toggles to your room.

