import coat
from cTemplates.Structs import d_template
from cTemplates.MainMenu.File import CreateFileMenu
from cTemplates.MainMenu.Edit import CreateEditMenu
from cTemplates.MainMenu.View import CreateViewMenu
from cTemplates.MainMenu.Textures import TexturesMenu
from cTemplates.MainMenu.Layers import LayersMenu
from cTemplates.MainMenu.Freeze import FreezeMenu
from cTemplates.MainMenu.Hide import HideMenu
from cTemplates.MainMenu.Windows import WindowsMenu
from cTemplates.MainMenu.Scripts import ScriptsMenu
import cTemplates.MainMenu.Scripts_UE
from cTemplates.MainMenu.Capture import CaptureMenu
from cTemplates.MainMenu.Help import HelpMenu
from cTemplates.MainMenu.Debug import DebugMenu
from cTemplates.MainMenu.Geometry import GeometryMenu
from cTemplates.MainMenu.Retopo import RetopoMenu
from cTemplates.MainMenu.Bake import BakeMenu
from cTemplates.MainMenu.PaintBake import PaintBakeMenu
from cTemplates.MainMenu.Curves import CurvesMenu
from cTemplates.MainMenu.Addons import AddonsMenu
from cTemplates.MainMenu.Symmetry import SymmetryMenu
from cTemplates.MainMenu.Calculate import CalcMenu



@d_template
def DefaultMenu():
    """
    Constructs the default main menu bar for the application.
    It conditionally includes sub-menus (File, Edit, View, Room-specific menus) based on the active room (Paint, Voxels, Retopo, etc.) and debug state.
    
    Items:
    - Edit the current room settings.
    - RoomsSelector
    - Splitter
    - BlankSpace
    - File Menu
    - Edit Menu
    - View Menu
    - Symmetry Menu (conditional)
    - Textures Menu (conditional)
    - Calculate Menu (conditional)
    - Layers Menu (conditional)
    - Freeze Menu (conditional)
    - Hide Menu (conditional)
    - Paint Bake Menu (conditional)
    - Geometry Menu (conditional)
    - Retopo Menu (conditional)
    - Bake Menu (conditional)
    - Curves Menu
    - Windows Menu
    - Scripts Menu
    - Addons Menu
    - Capture Menu
    - Help Menu
    - Debug Menu (conditional)
    - PaintDependency (conditional)
    - PickMethod (conditional)
    - ShiftActions (conditional)
    - Auto Pick (conditional)
    - GhostActions (conditional)
    """
    coat.menu_item("ThisRoomSettings") # Edit the current room settings.
    coat.menu_item("RoomsSelector")
    coat.menu_item("Splitter")
    coat.menu_item("BlankSpace")
    CreateFileMenu()
    CreateEditMenu()
    CreateViewMenu()
    if not coat.is_new_scene():
        SymmetryMenu()
        if coat.IsInRoom("Paint"):
            TexturesMenu()
    
        if coat.IsInRoom("Factures"):
            CalcMenu()
    
        if coat.IsInRoom("Paint"):
            LayersMenu()
    
        if coat.IsInRoom("Paint"):
            FreezeMenu()
            HideMenu()
            PaintBakeMenu()
    

    if coat.IsInRoom("Voxels"):
        FreezeMenu()
        GeometryMenu()

    if coat.IsInRoom("Retopo"):
        RetopoMenu()
        BakeMenu()

    CurvesMenu()
    WindowsMenu()
    ScriptsMenu()
    AddonsMenu()
    CaptureMenu()
    HelpMenu()
    if coat.IsDebug():
        DebugMenu()

    if coat.IsInRoom("Paint"):
        coat.menu_item("PaintDependency")
        coat.menu_item("PickMethod")
    elif coat.IsInRoom("Factures"):
        coat.menu_item("PaintDependency")
    elif coat.IsInRoom("Voxels"):
        coat.menu_item("ShiftActions")
        coat.menu_item("AutoPick") # Auto Pick
        coat.menu_item("GhostActions")