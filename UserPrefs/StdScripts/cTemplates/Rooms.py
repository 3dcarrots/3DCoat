import os
import coat
import cPy.cUI
import cPy.cCore
import pathlib
import inspect
import cTemplates.Structs

from cTemplates.menu import DefaultMenu
from cTemplates.voxTreeRmb import VoxTreeRmb
from cTemplates.curves import CurvesRMB
from cTemplates.navigation import NavigationBar
from cTemplates.sculptTools import SculptTools

def pathToRoomName(file_path: str):
    """
    Extracts the room name from the given file path by looking at the parent directory name.
    """
    path = pathlib.PurePath(file_path)
    return path.parent.name

rooms_history = list()
rooms = dict()

rmb = dict()
toolset = dict()
start_page = dict()
curves_rmb = dict()
main_menu = dict()
navigation_bar = dict()

class RoomBehavior(cPy.cUI.RoomBehavior):
    """
    Base class for defining the behavior of a custom room in the application.
    It handles updates for tools, menus, navigation bars, and context menus based on the active room.
    """
    def __init__(self):
        cPy.cUI.RoomBehavior.__init__(self)
        room_folder_name = ""

    def UpdateToolsList(self):
            """
            Updates the list of available tools. 
            Loads the specific toolset for the room if defined; otherwise, loads default SculptTools.
            """
            if self.room_folder_name in toolset:# and self.UseScriptsForToolset():
                toolset[self.room_folder_name]()
            else:
                SculptTools()

    def OnStartPageToolsList(self):
        """
        Loads the toolset configuration specifically for the Start Page if defined for this room.
        """
        if self.room_folder_name in start_page:
            start_page[self.room_folder_name]()

    def UpdateNavigationControls(self):
        """
        Updates the navigation bar controls.
        Loads the specific navigation bar for the room if defined; otherwise, loads the default NavigationBar.
        """
        if self.room_folder_name in navigation_bar and self.UseScriptsForNavigation():
            navigation_bar[self.room_folder_name]()
        else:
            NavigationBar()

    def UpdateMainMenu(self):
        """
        Updates the main menu structure.
        Loads the specific main menu for the room if defined; otherwise, loads the DefaultMenu.
        """
        if self.room_folder_name in main_menu and self.UseScriptsForMenu():
            main_menu[self.room_folder_name]()
        else:
            DefaultMenu()

    def ShowPopupMenu(self, propertytype):
        """
        Displays a context-sensitive popup menu (Right-Click Menu).
        
        Args:
            propertytype (str): The type of property triggering the menu (e.g., "curves").
        """
        if propertytype == "curves":
            if self.room_folder_name in curves_rmb:# and self.UseScriptsForCurves():
                curves_rmb[self.room_folder_name]()
            else:
                CurvesRMB()
        else:
            if self.room_folder_name in rmb and self.UseScriptsForRmb():
                rmb[self.room_folder_name]()
            else:
                VoxTreeRmb()

def reg_toolset(ref):
    """
    Registers a function as the toolset definition for a specific room.
    The room name is derived from the file path of the reference function.
    """
    n_action = cTemplates.Structs.cTemplate()
    n_action_content = cTemplates.Structs.cTemplate()
    n_action.Content.append(n_action_content)
    n_action_content.Implementation = ref
    room_folder_name = pathToRoomName(inspect.getsourcefile(ref))
    toolset[room_folder_name] = n_action
    return n_action

def reg_main_menu(ref):
    """
    Registers a function as the main menu definition for a specific room.
    """
    n_action = cTemplates.Structs.cTemplate()
    n_action_content = cTemplates.Structs.cTemplate()
    n_action.Content.append(n_action_content)
    n_action_content.Implementation = ref
    room_folder_name = pathToRoomName(inspect.getsourcefile(ref))
    main_menu[room_folder_name] = n_action
    return n_action

def reg_rmb(ref):
    """
    Registers a function as the Right Mouse Button (RMB) menu definition for a specific room.
    """
    n_action = cTemplates.Structs.cTemplate()
    n_action_content = cTemplates.Structs.cTemplate()
    n_action.Content.append(n_action_content)
    n_action_content.Implementation = ref
    room_folder_name = pathToRoomName(inspect.getsourcefile(ref))
    rmb[room_folder_name] = n_action
    return n_action

def reg_curves_rmb(ref):
    """
    Registers a function as the Curves context menu definition for a specific room.
    """
    n_action = cTemplates.Structs.cTemplate()
    n_action_content = cTemplates.Structs.cTemplate()
    n_action.Content.append(n_action_content)
    n_action_content.Implementation = ref
    room_folder_name = pathToRoomName(inspect.getsourcefile(ref))
    curves_rmb[room_folder_name] = n_action
    return n_action

def reg_navigation_bar(ref):
    """
    Registers a function as the navigation bar definition for a specific room.
    """
    n_action = cTemplates.Structs.cTemplate()
    n_action_content = cTemplates.Structs.cTemplate()
    n_action.Content.append(n_action_content)
    n_action_content.Implementation = ref
    room_folder_name = pathToRoomName(inspect.getsourcefile(ref))
    navigation_bar[room_folder_name] = n_action
    return n_action


def reg_room(room_beh):
    """
    Registers a new room behavior and automatically imports associated components 
    (Tools, CurvesMenu, RMBMenu, MainMenu, NavigationBar) if they exist in the room's directory.
    
    Args:
        room_beh: The class defining the room's behavior.
        
    Returns:
        The registered room behavior class.
    """
    behavior = room_beh()
    source_path = inspect.getsourcefile(room_beh)
    behavior.room_folder_name = pathToRoomName(source_path)

    if pathlib.Path(pathlib.PurePath(source_path).parent.joinpath("Tools.py")).exists():
        exec("import CustomRooms." + behavior.room_folder_name + ".Tools")

    if pathlib.Path(pathlib.PurePath(source_path).parent.joinpath("CurvesMenu.py")).exists():
        exec("import CustomRooms." + behavior.room_folder_name + ".CurvesMenu")

    if pathlib.Path(pathlib.PurePath(source_path).parent.joinpath("RMBMenu.py")).exists():
        exec("import CustomRooms." + behavior.room_folder_name + ".RMBMenu")

    if pathlib.Path(pathlib.PurePath(source_path).parent.joinpath("MainMenu.py")).exists():
        exec("import CustomRooms." + behavior.room_folder_name + ".MainMenu")

    if pathlib.Path(pathlib.PurePath(source_path).parent.joinpath("NavigationBar.py")).exists():
        exec("import CustomRooms." + behavior.room_folder_name + ".NavigationBar")

    behavior.SetRoomName(behavior.room_folder_name)
    rooms_history.append(behavior)
    rooms[behavior.room_folder_name] = behavior
    behavior.Apply()
    return room_beh