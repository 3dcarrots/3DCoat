import coat
from cTemplates.Structs import *

GeometryMenu = MainMenu("VoxelsMenu")

@d_menu_section(GeometryMenu)
def S_base():
   """
   Section for basic geometry operations like statistics, resolution, and symmetry.
   
   Items:
   - Show Statistics
   - Define Measurement Units
   - Res+
   - Resample
   - Screen Space Subdivide
   - Symm Copy
   """
   coat.menu_item("ShowStatistics") # Show Statistics
   coat.menu_item("DefineUnits") # Define Measurement Units
   coat.menu_item("IncreaseResolution") # Res+
   coat.menu_item("Resample") # Resample
   coat.menu_item("RESAMPLE4SCREEN_TOOL") # Screen Space Subdivide
   coat.menu_item("MakeSymm") # Symm Copy

@d_menu_section(GeometryMenu)
def S_rooms():
   """
   Section for transferring objects between different rooms (Retopo/Paint to Sculpt).
   
   Items:
   - Retopo Mesh to Sculpt Mesh
   - Paint Mesh to Sculpt Mesh (No Color or Subdivision)
   - Paint Mesh to Sculpt Mesh (Baked Texture & Subdivision)
   - Paint Mesh to Sculpt Mesh (Subdivided Only)
   """
   coat.menu_item("GetObjectFromRetopoRoom") # Retopo Mesh to Sculpt Mesh
   coat.menu_item("GetObjectFromPaintRoom") # Paint Mesh to Sculpt Mesh (No Color or Subdivision)
   coat.menu_item("GetTexturedObjectFromPaintRoom") # Paint Mesh to Sculpt Mesh (Baked Texture & Subdivision)
   coat.menu_item("GetSubdObjectFromPaintRoom") # Paint Mesh to Sculpt Mesh (Subdivided Only)

@d_submenu("AUTOPO", GeometryMenu)
def AUTOPO():
       """
       Submenu for automatic retopology tools (AUTOPO).
       
       Items:
       - AUTOPO
       - AUTOPO w/ PTEX
       - AUTOPO w/ MV Painting
       - AUTOPO for Per Pixel
       - Old-style quadrangulation
       - Custom Retopology Tools
       """
       coat.menu_item("Quadrangulate") # AUTOPO
       coat.menu_item("QuadrangulateAndMergePtex") # AUTOPO w/ PTEX
       coat.menu_item("QuadrangulateAndMerge") # AUTOPO w/ MV Painting
       coat.menu_item("QuadrangulateAndMergeDP") # AUTOPO for Per Pixel
       coat.menu_separator()
       coat.menu_item("OldStyleQuads") # Old-style quadrangulation
       coat.menu_separator()
       coat.menu_item("CustomRetopers") # Custom Retopology Tools
 
@d_menu_section(GeometryMenu)
def S_Extensions():
   """
   Inserts geometry-related options provided by installed extensions.
   
   Items:
   - Voxels extensions
   - Geometry extensions
   """
   coat.menu_insert_extensions("Voxels")
   coat.menu_insert_extensions("Geometry")

@d_menu_section(GeometryMenu)
def S_Surface_Tools():
   """
   Tools specific to Surface mode operations (cleaning, closing holes, decimation).
   
   Items:
   - Shell (conditional)
   - Clean Surface (conditional)
   - Close Holes (conditional)
   - Weld Vertices (conditional)
   - Decimate (conditional)
   - Cleanup Memory (conditional)
   - Separate Disconnected Parts (conditional)
   """
   if coat.is_surface():
       coat.menu_separator()
       coat.menu_item("Shell") # Shell
       coat.menu_item("CleanSurface") # Clean Surface
       coat.menu_item("CloseSurfHoles") # Close Holes
       coat.menu_item("LegacyFix") # Weld Vertices
       coat.menu_item("Decimate") # Decimate
       coat.menu_item("CleanupMemory") # Cleanup Memory
       coat.menu_item("Decompose") # Separate Disconnected Parts
 
@d_menu_section(GeometryMenu)
def S_edit():
   """
   General editing tools for scene management, smoothing, and hiding geometry.
   
   Items:
   - Clear
   - Smooth All
   - Unhide All
   - Make all uniform
   - Invert Hidden
   - Delete Hidden
   - Separate Hidden Volumes
   """
   coat.menu_item("ClearScene") # Clear
   coat.menu_item("SmoothObject") # Smooth All
   coat.menu_item("UnhideAll") # Unhide All
   coat.menu_item("ToUniformSpaceAll") # Make all uniform
   coat.menu_hotkey("X", 0, 1, 0) # CTRL+X
   coat.menu_item("InvertHide") # Invert Hidden
   coat.menu_hotkey("X", 1, 1, 0) # CTRL+SHIFT+X
   coat.menu_item("DeleteHidden") # Delete Hidden
   coat.menu_item("SeparateHidden") # Separate Hidden Volumes

@d_submenu("VisGhost", GeometryMenu)
def VisGhost():
       """
       Submenu for visibility and ghosting controls.
       
       Items:
       - Isolate
       - Toggle Visibility
       - Isolate Ghosting
       - Toggle Ghosting
       - Invert Volumes Visibility
       """
       coat.menu_item("HideButCurrent") # Isolate
       coat.menu_item("Toggle_vox_visibility") # Toggle Visibility
       coat.menu_hotkey("V", 1, 0, 0) # SHIFT+V
       coat.menu_item("Isolate_ghosting") # Isolate Ghosting
       coat.menu_hotkey("G", 1, 0, 0) # SHIFT+G
       coat.menu_item("Toggle_ghosting") # Toggle Ghosting
       coat.menu_hotkey("G", 0, 0, 0) # G
       coat.menu_item("Invert_vox_visibility") # Invert Volumes Visibility
       coat.menu_hotkey("I", 1, 0, 0) # SHIFT+I
       coat.menu_separator()
 
@d_submenu("Caching", GeometryMenu)
def Caching():
       """
       Submenu for managing object caching (Proxy Mode) to optimize performance.
       
       Items:
       - Toggle Proxy Mode
       - Uncache Visible Objects
       - Cache Visible Objects
       - Clear All Caches
       """
       coat.menu_item("ToggleCachingVolume") # Toggle Proxy Mode
       coat.menu_item("UnCacheVisible") # Uncache Visible Objects
       coat.menu_item("CacheVisible") # Cache Visible Objects
       coat.menu_item("ClearAllCache") # Clear All Caches
 
@d_submenu("CacheMethod", GeometryMenu)
def CacheMethod():
       """
       Submenu for selecting the reduction method (Reduction vs Decimation) for caching.
       
       Items:
       - Reduce 2X
       - Reduce 4X
       - Reduce 8X
       - Decimate 2X
       - Decimate 4X
       - Decimate 8X
       - Decimate 16X
       """
       coat.menu_item("Reduce2X") # Reduce 2X
       coat.menu_item("Reduce4X") # Reduce 4X
       coat.menu_item("Reduce8X") # Reduce 8X
       coat.menu_separator()
       coat.menu_item("Decimate2X") # Decimate 2X
       coat.menu_item("Decimate4X") # Decimate 4X
       coat.menu_item("Decimate8X") # Decimate 8X
       coat.menu_item("Decimate16X") # Decimate 16X
 
@d_submenu("Highlight", GeometryMenu)
def Highlight():
       """
       Submenu for configuring object highlighting behavior.
       
       Items:
       - Highlight
       - Highlight Settings
       - Highlight Selected
       """
       coat.menu_item("Highlight") # Highlight
       coat.menu_item("HighlightSettings") # Highlight Settings
       coat.menu_item("HighlightSelected") # Highlight Selected
       coat.menu_hotkey("F11", 0, 0, 0) # F11
 
@d_menu_section(GeometryMenu)
def S_Sculpt():
   """
   Section for contour selection parameters and rendering.
   
   Items:
   - Edit contour selection parameters
   - Render the selection contour
   """
   coat.menu_item("SculptSelParams") # Edit contour selection parameters
   coat.menu_item("RenderSculptSelection") # Render the selection contour
@d_menu_section(GeometryMenu)
def S_GPU():
   """
   Section for GPU acceleration settings.
   
   Items:
   - UseCUDA
   - Cuda Smooth Boost
   """
   coat.menu_item("UseCUDA") # Use CUDA
   coat.menu_item("CudaSmoothBoost") # Cuda Smooth Boost
@d_menu_section(GeometryMenu)
def S_Render():
   """
   Section for rendering options like shadows and incremental rendering.
   
   Items:
   - Cast Shadows
   - Incremental Render
   - Accurate Smoothing
   - Stroke Expansion
   """
   coat.menu_item("CastShadows") # Cast Shadows
   coat.menu_item("IncrementalRender") # Incremental Render
   coat.menu_item("AccurateSmoothing") # Accurate Smoothing
   coat.menu_item("MoveBasedGrowth") # Stroke Expansion