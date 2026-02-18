import coat
from cTemplates.Structs import *
import cTemplates.MainMenu.View as O_View
import cTemplates.MainMenu.File as O_File
import cTemplates.MainMenu.Symmetry as O_Symmetry
import cTemplates.MainMenu.Windows as O_Windows
import cTemplates.MainMenu.Scripts as O_Scripts
import cTemplates.MainMenu.Help as O_Help
import cTemplates.MainMenu.Geometry as O_Geometry
import cTemplates.MainMenu.Curves as O_Curves

CreateFileMenu = MainMenu("FILE")

CreateFileMenu.Content.append(O_File.S_New)
CreateFileMenu.Content.append(O_File.S_Save)

@d_menu_section(CreateFileMenu)
def S_save():
   """
   Section for file saving operations.
   
   Items:
   - Save
   - Save As
   - Save Incrementally
   """
   if not coat.is_new_scene():
       coat.menu_item("SAVE_FILEFAST") # Save
       coat.menu_hotkey("S", 0, 1, 0) # CTRL+S
       coat.menu_item("SAVE_FILE") # Save As
       coat.menu_hotkey("S", 0, 1, 1) # CTRL+ALT+S
       coat.menu_item("SAVE_INC") # Save Incrementally
       coat.menu_hotkey("S", 1, 1, 0) # SHIFT+CTRL+S
 
@d_menu_section(CreateFileMenu)
def S_Import_Export():
   """
   Section for importing and exporting mesh data.
   
   Items:
   - Import for Sculpt/Vertex Painting/Reference
   - Import Image as Mesh
   - Export Scene
   """
   coat.menu_item("ImportForVertexPainting") # Import for Sculpt/Vertex Painting/Reference
   coat.menu_item("ImportImageAsMesh") # Import Image as Mesh
   coat.menu_item("ExportScene") # Export Scene

CreateFileMenu.Content.append(O_File.Printing3D)


#######################################
#### Edit Menu


@d_main_menu("COMMANDS")
def CreateEditMenu():
   """
   Creates the Edit (Commands) menu with general application settings and history operations.
   
   Items:
   - Undo
   - Redo
   - Load Hotkeys
   - Save Hotkeys
   - Customize UI
   - Preferences
   - Reset to Default Settings
   - Relocate 3DCoat's Data
   """
   coat.menu_item("UNDO") # Undo
   coat.menu_hotkey("Z", 0, 1, 0) # CTRL+Z
   coat.menu_item("REDO") # Redo
   coat.menu_hotkey("Y", 0, 1, 0) # CTRL+Y
   coat.menu_separator()
   coat.menu_item("LoadHotkeys") # Load Hotkeys
   coat.menu_item("SaveHotkeys") # Save Hotkeys
   coat.menu_item("CustomizeUI") # Customize UI
   coat.menu_item("OPTIONS") # Preferences
   coat.menu_item("ResetSettings") # Reset to Default Settings
   coat.menu_item("EditDataPlacement") # Relocate 3DCoat's Data

CreateViewMenu = MainMenu("VIEW")

CreateViewMenu.Content.append(O_View.View_S_ShadingOptions)
CreateViewMenu.Content.append(O_View.View_S_Pass)

@d_menu_section(CreateViewMenu)
def S_Mesh():
   """
   Section for mesh display modes.
   
   Items:
   - BackfaceCulling
   - Wireframe
   - Low-Poly
   """
   coat.menu_item("BackfaceCulling") # Backface Culling
   coat.menu_item("VIEW_WIREFRAME") # Wireframe
   coat.menu_hotkey("W", 0, 0, 0) # W
   coat.menu_hotkey("W", 1, 0, 0) # SHIFT+W
   coat.menu_item("VIEW_LOWPOLY") # Low-Poly
   coat.menu_hotkey("6", 0, 0, 0) # 6

CreateViewMenu.Content.append(O_View.View_S_Grid)
CreateViewMenu.Content.append(O_View.View_S_Print)
CreateViewMenu.Content.append(O_View.View_S_Axis)
CreateViewMenu.Content.append(O_View.View_S_Snap_Grid)
CreateViewMenu.Content.append(O_View.View_S_Viewport)

#######################################
#### Symmetry Menu

SymmetryMenu = O_Symmetry.SymmetryMenu

#######################################
#### Windows Menu

WindowsMenu = O_Windows.WindowsMenu

#######################################
#### Scripts Menu

ScriptsMenu = O_Scripts.ScriptsMenu

#######################################
#### Help Menu

HelpMenu = O_Help.HelpMenu

#######################################
#### Geometry Menu

GeometryMenu = MainMenu("VoxelsMenu")

GeometryMenu.Content.append(O_Geometry.S_base)
GeometryMenu.Content.append(O_Geometry.S_Surface_Tools)
 
@d_menu_section(GeometryMenu)
def S_Simple():
   """
   Simple geometry operations like clearing or smoothing the scene.
   
   Items:
   - Clear
   - Smooth All
   """
   coat.menu_item("ClearScene") # Clear
   coat.menu_item("SmoothObject") # Smooth All

GeometryMenu.Content.append(O_Geometry.VisGhost)
GeometryMenu.Content.append(O_Geometry.Caching)
GeometryMenu.Content.append(O_Geometry.CacheMethod)
GeometryMenu.Content.append(O_Geometry.Highlight)
 
@d_menu_section(GeometryMenu)
def S_Render():
   """
   Rendering options within the Geometry menu.
   
   Items:
   - Cast Shadows
   """
   coat.menu_item("CastShadows") # Cast Shadows

#######################################
#### Curves Menu
CurvesMenu = O_Curves.CurvesMenu



@d_template
def SimplestMainMenu():
    """
    Defines the layout of the simplified main menu including file, edit, view, and room-specific menus.
    
    Items:
    - Edit the current room settings.
    - RoomsSelector
    - Splitter
    - BlankSpace
    """
    coat.menu_item("ThisRoomSettings") # Edit the current room settings.
    coat.menu_item("RoomsSelector")
    coat.menu_item("Splitter")
    coat.menu_item("BlankSpace")
    SimplestMainMenu.IncludeContent()

SimplestMainMenu.Content.append(CreateFileMenu)
SimplestMainMenu.Content.append(CreateEditMenu)
SimplestMainMenu.Content.append(CreateViewMenu)

@d_child(SimplestMainMenu)
def M_SymmetryMenu():
    """
    Conditionally adds the Symmetry menu if not in a new scene.
    
    Items:
    - SymmetryMenu (conditional)
    """
    if(not coat.is_new_scene()):
        SymmetryMenu()

@d_child(SimplestMainMenu)
def M_GeometryMenu():
    """
    Conditionally adds the Geometry menu if in the Voxels room.
    
    Items:
    - GeometryMenu (conditional)
    """
    if(coat.IsInRoom("Voxels")):
        GeometryMenu()

SimplestMainMenu.Content.append(CurvesMenu)
SimplestMainMenu.Content.append(WindowsMenu)
SimplestMainMenu.Content.append(ScriptsMenu)
SimplestMainMenu.Content.append(HelpMenu)