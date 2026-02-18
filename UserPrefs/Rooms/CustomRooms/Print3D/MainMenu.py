
import coat
from cTemplates.Structs import *
import cTemplates.MainMenu.File as O_File
import cTemplates.MainMenu.Edit as O_Edit
import cTemplates.MainMenu.View as O_View
import cTemplates.MainMenu.Symmetry as O_Symmetry
import cTemplates.MainMenu.Freeze as O_Freeze
import cTemplates.MainMenu.Hide as O_Hide
import cTemplates.MainMenu.Windows as O_Windows
import cTemplates.MainMenu.Scripts as O_Scripts
import cTemplates.MainMenu.Help as O_Help
import cTemplates.MainMenu.Geometry as O_Geometry
import cTemplates.MainMenu.Curves as O_Curves
import cTemplates.MainMenu.Debug as O_Debug

from cTemplates.Rooms import reg_main_menu

@reg_main_menu
def PrintMainMenu():
    Print3DMenu()

#######################
##### File Menu

FileMenu = MainMenu("FILE")

FileMenu.Content.append(O_File.S_New)
FileMenu.Content.append(O_File.Install)
FileMenu.Content.append(O_File.S_CreateExtension)
FileMenu.Content.append(O_File.Browse)
FileMenu.Content.append(O_File.S_Save)
FileMenu.Content.append(O_File.S_New)
FileMenu.Content.append(O_File.S_csgo)

 
@d_submenu("Import", FileMenu)
def Import():
       coat.menu_item("ImportForVertexPainting") # /{CY}Import for Vertex Painting/Big reference
       coat.menu_item("ImportImageAsMesh") # /{CY}Import Image as Mesh
       coat.menu_item("ImportObjectsByLayers") # /Import multiple objects
       coat.menu_item("LoadSplineAs3DObject") # /Import Curve as Mesh
       coat.menu_item("ImportForVoxelizing") # /Import Mesh for Voxelization


@d_child(FileMenu)
def FileIfVoxels():
   if coat.IsInRoom("Voxels"):
       FileIfVoxels.IncludeContent()

@d_submenu("3D-Printing", FileIfVoxels)
def V_3DPrinting():
           coat.menu_item("ExportForPrinting") # /Export For 3D Printing
           coat.menu_item("ExportCura")
           coat.menu_item("PrepareToPublish")

@d_submenu("Export", FileIfVoxels)
def V_Export():
           coat.menu_item("ExportScene") # /Export Scene
           coat.menu_item("ExportSelObject") # /Export selected objects				
           coat.menu_exit()


FileMenu.Content.append(O_File.S_Export_Extensions)
FileMenu.Content.append(O_File.S_Exit)


#######################
##### Edit Menu
EditMenu = MainMenu("COMMANDS")
EditMenu.Content.append(O_Edit.S_Undo)
EditMenu.Content.append(O_Edit.GIZMOLESS)
# EditMenu.Content.append(O_Edit.S_Edit) #???
EditMenu.Content.append(O_Edit.S_Project)
EditMenu.Content.append(O_Edit.S_Options)

#######################
##### Windows Menu

WindowsMenu = MainMenu("Windows")

Popups = Submenu("Popups", WindowsMenu)

Popups.Content.append(O_Windows.Popups_S1)
Popups.Content.append(O_Windows.Popups_Extensions)

Sliders = Submenu("Sliders", WindowsMenu)

Sliders.Content.append(O_Windows.Sliders_S1)
Sliders.Content.append(O_Windows.Sliders_S3)

WindowsMenu.Content.append(O_Windows.Windows_S_UIColorThemesList)
WindowsMenu.Content.append(O_Windows.Windows_S_Default)
WindowsMenu.Content.append(O_Windows.Windows_S_Restore)
WindowsMenu.Content.append(O_Windows.Windows_S_Reset)
WindowsMenu.Content.append(O_Windows.Windows_S_ToggleUI)


#######################
##### Geometry Menu

GeometryMenu = MainMenu("VoxelsMenu")

GeometryMenu.Content.append(O_Geometry.S_base)
GeometryMenu.Content.append(O_Geometry.S_Extensions)
GeometryMenu.Content.append(O_Geometry.S_Surface_Tools)
GeometryMenu.Content.append(O_Geometry.S_edit)
GeometryMenu.Content.append(O_Geometry.VisGhost)
GeometryMenu.Content.append(O_Geometry.Caching)
GeometryMenu.Content.append(O_Geometry.CacheMethod)
GeometryMenu.Content.append(O_Geometry.Highlight)
GeometryMenu.Content.append(O_Geometry.S_GPU)
GeometryMenu.Content.append(O_Geometry.S_Render)

#######################
##### View Menu
ViewMenu = MainMenu("VIEW")

ViewMenu.Content.append(O_View.View_S_Grid)
ViewMenu.Content.append(O_View.View_S_Print)
ViewMenu.Content.append(O_View.View_S_Axis)
ViewMenu.Content.append(O_View.View_S_Snap)
ViewMenu.Content.append(O_View.View_S_Snap_Grid)
ViewMenu.Content.append(O_View.View_S_Show_Print)
ViewMenu.Content.append(O_View.View_S_Viewport)
ViewMenu.Content.append(O_View.View_S_Extensions)

#######################################
#######################################
@d_template
def Print3DMenu():

    coat.menu_item("ThisRoomSettings")
    coat.menu_item("RoomsSelector")
    coat.menu_item("Splitter")
    coat.menu_item("BlankSpace")
    
    Print3DMenu.IncludeContent()

    if coat.IsDebug():
        O_Debug.DebugMenu()


Print3DMenu.Content.append(FileMenu)
Print3DMenu.Content.append(EditMenu)
Print3DMenu.Content.append(ViewMenu)
Print3DMenu.Content.append(O_Symmetry.SymmetryMenu)
Print3DMenu.Content.append(O_Freeze.FreezeMenu)
Print3DMenu.Content.append(GeometryMenu)
Print3DMenu.Content.append(O_Curves.CurvesMenu)
Print3DMenu.Content.append(WindowsMenu)
Print3DMenu.Content.append(O_Scripts.ScriptsMenu)
Print3DMenu.Content.append(O_Help.HelpMenu)

    