import coat
from cTemplates.Structs import *

CreateViewMenu = MainMenu("VIEW")

@d_menu_section(CreateViewMenu)
def View_S_ShadingOptions():
   """
   Menu section for configuring general shader display options.
   
   Items:
   - ShadingOptions
   """
   coat.menu_item("ShadingOptions") # ShadingOptions
@d_menu_section(CreateViewMenu)
def View_S_Pass():
   """
   Menu section for selecting different viewport render passes and lighting modes.
   
   Items:
   - Greyscale Panorama
   - Smooth Shade
   - Relief Only
   - Flat Shade
   - Gloss/Roughness Only
   - Specular Color
   - Metalness
   """
   coat.menu_item("GreyscaleLight") # Greyscale Panorama
   coat.menu_item("VIEW_SHADED") # Smooth Shade
   coat.menu_hotkey("5", 0, 0, 0) # 5
   coat.menu_item("VIEW_RELIEF_ONLY") # Relief Only
   coat.menu_hotkey("1", 0, 0, 0) # 1
   coat.menu_item("VIEW_NON_SHADED") # Flat Shade
   coat.menu_hotkey("2", 0, 0, 0) # 2
   coat.menu_item("VIEW_GLOSS_ONLY") # Gloss/Roughness Only
   coat.menu_hotkey("3", 0, 0, 0) # 3
   coat.menu_item("VIEW_SPECULAR_COLOR_ONLY") # Specular Color
   coat.menu_hotkey("7", 0, 0, 0) # 7
   coat.menu_item("VIEW_METALNESS_ONLY") # Metalness
   coat.menu_hotkey("8", 0, 0, 0) # 8
@d_menu_section(CreateViewMenu)
def View_S_Mesh():
   """
   Settings for mesh visualization, including wireframe and backface culling.
   
   Items:
   - Backface Culling
   - Wireframe
   - Correct Alpha Ordering
   """
   coat.menu_item("BackfaceCulling") # Backface Culling
   coat.menu_item("VIEW_WIREFRAME") # Wireframe
   coat.menu_hotkey("W", 0, 0, 0) # W
   coat.menu_item("CorrectAlphaOrdering") # Correct Alpha Ordering
@d_menu_section(CreateViewMenu)
def View_S_Texture():
   """
   Texture visualization settings, such as filtering, seams, and low-poly view.
   
   Items:
   - Linear Texture Filtering
   - Seams
   - Low-Poly
   """
   coat.menu_item("VIEW_TEXTURE_FILTERING") # Linear Texture Filtering
   coat.menu_item("VIEW_SEAMS") # Seams
   coat.menu_hotkey("W", 1, 0, 0) # SHIFT+W
   coat.menu_item("VIEW_LOWPOLY") # Low-Poly
   coat.menu_hotkey("6", 0, 0, 0) # 6
@d_menu_section(CreateViewMenu)
def View_S_Grid():
   """
   Controls for the 3D grid visibility and snapping.
   
   Items:
   - Show 3D Grid
   - Snap to 3D Grid
   """
   coat.menu_item("SHOW_GRID_3D") # Show 3D Grid
   coat.menu_item("SNAP_TO_3DGRID") # Snap to 3D Grid

@d_submenu("GridPlacement", View_S_Grid)
def GridPlacement():
       """
       Submenu to select the orientation plane of the grid.
       
       Items:
       - ZX Plane
       - XY Plane
       - YZ Plane
       - Auto Placement
       """
       coat.menu_item("Grid_ZX") # ZX Plane
       coat.menu_item("Grid_XY") # XY Plane
       coat.menu_item("Grid_YZ") # YZ Plane
       coat.menu_item("AutoGrid") # Auto Placement
 
@d_submenu("GRID_DENSITY", View_S_Grid)
def GRID_DENSITY():
       """
       Submenu to adjust the density/size of the grid cells.
       
       Items:
       - Small
       - Medium
       - Large
       - Custom
       - Customize Grid
       """
       coat.menu_item("RARE_GRID") # Small
       coat.menu_item("NORMAL_GRID") # Medium
       coat.menu_item("DENSE_GRID") # Large
       coat.menu_item("CUSTOM_GRID") # Custom
       coat.menu_item("CUSTOMIZE_GRID") # Customize Grid
 
@d_menu_section(CreateViewMenu)
def View_S_Print():
   """
   Settings specific to 3D printing views, such as build volume.
   
   Items:
   - Setup Printing Area
   """
   coat.menu_item("CustomizeBuildvolume") # Setup Printing Area

@d_menu_section(CreateViewMenu)
def View_S_Axis():
   """
   Controls for displaying the coordinate axes.
   
   Items:
   - Axis
   """
   coat.menu_item("SHOW_AXIS") # Axis

@d_submenu("Separate_axis", View_S_Axis)
def Separate_axis():
       """
       Submenu to toggle individual axes visibility.
       
       Items:
       - X
       - Y
       - Z
       """
       coat.menu_item("showaxX") # X
       coat.menu_item("showaxY") # Y
       coat.menu_item("showaxZ") # Z
 
@d_menu_section(CreateViewMenu)
def View_S_Snap():
   """
   Snapping options for measurement guides and curves.
   
   Items:
   - Show Measurement Guides
   - Snap to Measurement Guides
   - Snap to Curve
   - Snap to Curve Points
   - Snap to Center
   """
   coat.menu_item("showMeasureGuides") # Show Measurement Guides
   coat.menu_item("snapToMeasureGuides") # Snap to Measurement Guides
   coat.menu_item("cuSnapToCurve") # Snap to Curve
   coat.menu_item("cuSnapToPoints") # Snap to Curve Points
   coat.menu_item("cuSnapToCurveCenter") # Snap to Center

@d_menu_section(CreateViewMenu)
def View_S_Snap_Grid():
   """
   Controls for the 2D grid visibility and snapping options.
   
   Items:
   - Show 2D Grid
   - Snap to 2D Grid
   - Snap to Low-Poly Vertices
   """
   coat.menu_item("SHOW_GRID") # Show 2D Grid
   coat.menu_hotkey("'", 0, 1, 0) # CTRL+'
   coat.menu_item("SNAP_TO_GRID") # Snap to 2D Grid
   coat.menu_item("SNAP_TO_ORIG_VERTS") # Snap to Low-Poly Vertices

@d_menu_section(CreateViewMenu)
def View_S_Show():
   """
   Room-specific visibility toggles (e.g., UV overlaps, cross-room object visibility).
   
   Items:
   - Show UV Overlapping (conditional)
   - Show Voxels in Painting Room (conditional)
   - Show Poly Objects in Sculpt room (conditional)
   - Show Retopo Objects in Sculpt room (conditional)
   """
   if coat.IsInRoom("UV") or coat.IsInRoom("Modeling"):
       coat.menu_item("ShowUVOverlapping") # Show UV Overlapping
       coat.menu_hotkey("+", 0, 1, 0) # CTRL++
 
   if coat.IsInRoom("Paint"):
       coat.menu_item("ShowVoxelsInPaintRoom") # Show Voxels in Painting Room
 
   if coat.IsInRoom("Voxels"):
       coat.menu_item("ShowPolyObjectsInVoxelRoom") # Show Poly Objects in Sculpt room
       coat.menu_item("ShowRetopoObjectsInVoxelRoom") # Show Retopo Objects in Sculpt room

@d_menu_section(None)
def View_S_Show_Print():
   """
   Specific visibility options for printing context.
   
   Items:
   - Show Retopo Objects in Sculpt room
   """
   coat.menu_item("ShowRetopoObjectsInVoxelRoom") # Show Retopo Objects in Sculpt room

@d_menu_section(CreateViewMenu)
def View_S_Viewport():
   """
   General viewport projection and display settings.
   
   Items:
   - Orthographic Projection
   - Projector
   - Toggle Full Screen
   """
   coat.menu_item("VIEW_ORTHO") # Orthographic Projection
   coat.menu_hotkey("NUM5", 0, 0, 0) # NUM5
   coat.menu_item("PROJECTOR") # Projector
   coat.menu_item("ToggleFullscreen") # Toggle Full Screen
   coat.menu_hotkey("ENTER", 0, 0, 1) # ALT+ENTER

@d_menu_section(CreateViewMenu)
def View_S_Displacement():
   """
   Settings related to mesh displacement and tessellation visualization.
   
   Items:
   - Show Displaced Mesh (conditional)
   - Adjust Tessellation
   """
   if coat.is_ppp():
            coat.menu_item("VIEW_DISP") # Show Displaced Mesh
   coat.menu_item("AdjustSubpatching") # Adjust Tessellation

@d_menu_section(CreateViewMenu)
def View_S_Extensions():
   """
   Inserts view-related options provided by installed extensions.
   
   Items:
   - View extensions
   """
   coat.menu_insert_extensions("View")