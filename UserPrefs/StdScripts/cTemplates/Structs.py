import coat
import cPy.cCore
import cPy.cNodeSystem
import os
import sys
import time
import ctypes

# Access Python C API to handle reference counting manually
pythonapi = ctypes.pythonapi

# Define argument types for Py_IncRef and Py_DecRef to ensure correct pointer handling
pythonapi.Py_IncRef.argtypes = [ctypes.py_object]
pythonapi.Py_DecRef.argtypes = [ctypes.py_object]

call_id: int = 0

# Global list to keep track of all created actions/templates to prevent GC
_action_list = list()


def _force_register_member(func, n_action):
    """
    Helper function to manually register a dynamically created action instance 
    as a member of the module where the decorated function resides.
    
    This ensures that 3DCoat's C++ engine can find and execute the Python action 
    by name/module path.
    """
    try:
        # Copy metadata from the original function to the action instance
        n_action.__module__ = func.__module__
        n_action.__name__ = func.__name__
        n_action.__qualname__ = func.__qualname__
        n_action.__doc__ = func.__doc__

        if func.__module__ in sys.modules:
            mod = sys.modules[func.__module__]
            
            # Attach the action instance to the module
            setattr(mod, func.__name__, n_action)
            
            # Ensure it's listed in __all__ for export visibility
            if not hasattr(mod, '__all__'):
                mod.__all__ = []
            if isinstance(mod.__all__, tuple):
                mod.__all__ = list(mod.__all__)
                
            if func.__name__ not in mod.__all__:
                mod.__all__.append(func.__name__)
    except Exception as e:
        print(f"Registration error for {func.__name__}: {e}")


class cTemplate(cPy.cCore.cAction):
    """
    The base class for all UI elements (Menus, Tools, Sections).
    It acts as a recursive container that manages the execution order of UI commands.
    Inherits from cPy.cCore.cAction to interface with the C++ engine.
    """
    def __init__(self):
        cPy.cCore.cAction.__init__(self)
        self.if_has_Enabled_content = False
        self.is_first = False
        self.Enabled = True
        self.child: cTemplate = None
        
        # Actions to run before the main content
        self.Before: list[cTemplate] = list()
        # Actions to run after the main content
        self.After:  list[cTemplate] = list()
        # Children elements (submenus, items)
        self.Content: list[cTemplate] = list()
        
        # Default implementation executes child content
        self.Implementation =  lambda: self.IncludeContent()
        
        self.last_call_id: int = -1
        self.call_count: int = 0

        # Register global instance to prevent garbage collection
        global _action_list
        _action_list.append(self)
        self._action_idx = len(_action_list)-1

    def UICmd(self):
        """
        Generates the command string used by the UI system to trigger this action.
        Format: "python:ExecActionByIdx(index)#FunctionName"
        """
        return "python:ExecActionByIdx("+str(self._action_idx)+")#"+self.Implementation.__name__

    def __str__(self):
        return self.UICmd()

    def RunBeforeList(self):
        """
        Executes the 'Before' hooks and recursively triggers setup for content.
        """
        for act in self.Before:
            if act.Enabled:
                act()

        for act in self.Content:
            act.RunBeforeList()

    def Run(self, run_before_list = True):
        """
        Main execution logic.
        1. Checks if Enabled.
        2. Runs pre-requisites (Before list).
        3. Validates content availability.
        4. Executes the actual Implementation (creating the menu/tool item).
        5. Runs post-requisites (After list).
        """
        global call_id
        if not self.Enabled: 
            return

        if run_before_list:
            call_id += 1
            self.RunBeforeList()

        if self.if_has_Enabled_content and not self.HasEnabledContent():
            return False

        self.Implementation()

        for act in self.After:
            act()

        return True
    
    def IncludeContent(self):
        """
        Iterates through the `Content` list and executes children.
        Manages recursion depth/call count to prevent infinite loops or stack overflows.
        """
        global call_id
        result: bool = False
        first: bool = True        
        if call_id != self.last_call_id:
            self.call_count = 0
            self.last_call_id = call_id
        self.call_count += 1
        
        # Limit recursion depth/re-entry
        if self.call_count < 10:
            for act in self.Content:
                if act != None: 
                    act.is_first = first
                    if act.Run(False):
                        result = True
                        first = False
        return result

    def __call__(self):
        """
        Allows the instance to be called like a function to trigger Run().
        """
        global call_id
        call_id += 1
        self.Run()

    def HasEnabledContent(self):
        """
        Recursively checks if this element or any of its children are enabled.
        """
        for act in self.Content:
            if act.Enabled and act.HasEnabledContent():
                return True
            if not act.if_has_Enabled_content and act.Enabled:
                return True

        return False

###########################################

def d_node(cls_to_decorate):
    """
    Decorator to register a class as a Node in the Node System.
    Increments the reference count to keep the class definition alive.
    
    Example:
        @d_node
        class MyCustomNode(cPy.cNodeSystem.BaseNode):
            def __init__(self):
                ...
    """
    def get_class_name(self):
        return cls_to_decorate.__name__

    def new_element(self):
        X = self.__class__()
        pythonapi.Py_IncRef(X)
        X.SetParents()
        return X

    setattr(cls_to_decorate, 'get_class_name', get_class_name)
    setattr(cls_to_decorate, 'new_element', new_element)
    try:
        instance_for_reg = cls_to_decorate()
        pythonapi.Py_IncRef(instance_for_reg) # Prevent GC
        cPy.cNodeSystem.BaseNode.RegNodeType(cls_to_decorate.__module__, instance_for_reg)
        cPy.cCore.cREG.reg_class(instance_for_reg)
        print("REG NODE: " + cls_to_decorate.__module__)
        print("ClassName: " + cls_to_decorate.__name__)
    except Exception as e:
        print(f"[@d_node]: !!! NODE REG ERROR {cls_to_decorate.__name__}: {e}")

    return cls_to_decorate

def d_slot(func):
    """
    Decorator to register a function as a generic slot action.
    """
    n_action = cTemplate()
    n_action.Implementation = func
    _force_register_member(func, n_action)
    return n_action

def d_template(func):
    """
    Decorator to wrap a function into a cTemplate. 
    Used for logic that doesn't necessarily create a visual menu item itself but structures execution.

    Example:
        @d_template
        def PaintTools():
            coat.tools_section("Paint")
            coat.tools_item("[StdPen]StdPen") # Brush
            PaintTools.IncludeContent()
    """
    n_action = cTemplate()
    n_action.Implementation = func
    _force_register_member(func, n_action)
    return n_action

def d_child(parent: cTemplate = None):
    """
    Decorator to register a function as a child action of a parent cTemplate.
    Useful for building hierarchies (e.g., adding items to a specific menu).

    Example (from navigation.py):
        @d_child(NavigationBar)
        def Light():
            coat.menu_item("@LIGHT_CONTRAST")
            coat.menu_item("@LIGHT_BRIGHTNESS")
    """
    def cChildActionD(func):
        n_action = cTemplate()
        n_action.Implementation = func
        _force_register_member(func, n_action)
        if parent != None:
            parent.Content.append(n_action)
        return n_action
    return cChildActionD

##########################################

def d_class(cls_to_decorate):
    """
    Decorator to register base class types in the core registry.
    Similar to d_node but for general classes.
    """
    def get_class_name(self):
        return cls_to_decorate.__name__

    def new_element(self):
        X = self.__class__()
        pythonapi.Py_IncRef(X)
        X.SetParents()
        return X

    setattr(cls_to_decorate, 'get_class_name', get_class_name)
    setattr(cls_to_decorate, 'new_element', new_element)
    try:
        instance_for_reg = cls_to_decorate()
        pythonapi.Py_IncRef(instance_for_reg)
        cPy.cCore.cREG.reg_class(instance_for_reg)
    except Exception as e:
        print(f"[@d_class]: !!! CALSS REG ERROR {cls_to_decorate.__name__}: {e}")

    return cls_to_decorate

# Re-definition of d_slot, d_template, d_child likely for scoping reasons or redundant imports
# in the original codebase structure. 

def d_slot(func):
    """
    Decorator to register a function as a slot.
    """
    n_action = cTemplate()
    n_action.Implementation = func
    _force_register_member(func, n_action)
    return n_action

def d_template(func):
    """
    Decorator to create a template action.
    """
    n_action = cTemplate()
    n_action.Implementation = func
    _force_register_member(func, n_action)
    return n_action

def d_child(parent: cTemplate = None):
    """
    Decorator to add a child action to a parent template.
    """
    def cChildActionD(func):
        n_action = cTemplate()
        n_action.Implementation = func
        _force_register_member(func, n_action)
        if parent != None:
            parent.Content.append(n_action)
        return n_action
    return cChildActionD

#### Tools Section


def new_tools_section(section_name, n_action: cTemplate):
    """
    Executes the C++ binding to create a new tool section in the UI (Left Panel).
    """
    coat.tools_section(section_name)
    n_action.IncludeContent()

class ToolsSection(cTemplate):
    """
    Class representing a Tool Section (group of tools in the left panel).
    """
    def __init__(self, section_name = None, parent: cTemplate = None):
        if section_name != None:
            cTemplate.__init__(self)
            self.Implementation =  lambda: new_tools_section(section_name, self)
            self.if_has_Enabled_content = True
        if parent != None:
            parent.Content.append(self)

def d_tools_section(section_name: str, parent: cTemplate = None):
    """
    Decorator to define a Tool Section.
    
    Example (from sculptTools.py):
        Tools = cTemplate()
        
        @d_tools_section("Layers", Tools)
        def Layers():
            coat.tools_item("[extension]MagnifyLayers") # Magnify SL
            coat.tools_item("[extension]EraseLayers") # Erase SL
    """
    def cToolsSectionD(func):
        n_action = cTemplate()
        n_action.Implementation =  lambda: new_tools_section(section_name, n_action)
        n_action.if_has_Enabled_content = True
        n_action.child = cTemplate()
        n_action.child.Implementation = func
        _force_register_member(func, n_action)
        n_action.Content.append(n_action.child)
        if parent != None:
            parent.Content.append(n_action)
        return n_action
    return cToolsSectionD


#### Main menu

def new_main_menu(submenu_name, n_action: cTemplate):
    """
    Executes the C++ binding to start a main top-level menu (File, Edit, View...).
    """
    coat.start_main_menu(submenu_name)
    n_action.IncludeContent()

class MainMenu(cTemplate):
    """
    Class representing a top-level Main Menu.
    """
    def __init__(self, menu_name = None, parent: cTemplate = None):
        cTemplate.__init__(self)
        if menu_name != None:
            self.Implementation =  lambda: new_main_menu(menu_name, self)
            self.if_has_Enabled_content = True
        if parent != None:
            parent.Content.append(self)

def d_main_menu(menu_name: str, parent: cTemplate = None):
    """
    Decorator to define a Main Menu item.

    Example (from Addons.py):
        @d_main_menu("Addons")
        def AddonsMenu():
            coat.menu_item("InstallExtension")
            coat.menu_item("ListAddons")
    """
    def cToolsSectionD(func):
        n_action = MainMenu(menu_name)
        n_action.child = cTemplate()
        n_action.child.Implementation = func
        _force_register_member(func, n_action)
        n_action.Content.append(n_action.child)
        if parent != None:
            parent.Content.append(n_action)
        return n_action
    return cToolsSectionD


#### Submenu

def new_submenu(menu_name, n_action: cTemplate):
    """
    Executes C++ bindings to create a nested submenu.
    """
    coat.menu_submenu(menu_name)
    n_action.IncludeContent()
    coat.menu_exit() # Close the submenu scope

class Submenu(cTemplate):
    """
    Class representing a nested Submenu.
    """
    def __init__(self, submenu_name = None, parent: cTemplate = None):
        cTemplate.__init__(self)
        if submenu_name != None:
            self.Implementation =  lambda: new_submenu(submenu_name, self)
            self.if_has_Enabled_content = True
        if parent != None:
            parent.Content.append(self)


def d_submenu(submenu_name: str, parent: cTemplate = None):
    """
    Decorator to define a Submenu.

    Example (from File.py):
        CreateFileMenu = MainMenu("FILE")

        @d_submenu("Export", CreateFileMenu)
        def Export():
            coat.menu_item("ExportScene")
            coat.menu_item("ExportSelObject")
    """
    def cToolsSectionD(func):
        n_action = Submenu(submenu_name)
        n_action.child = cTemplate()
        n_action.child.Implementation = func
        _force_register_member(func, n_action)
        n_action.Content.append(n_action.child)
        if parent != None:
            parent.Content.append(n_action)
        return n_action
    return cToolsSectionD

#### Submenu (RMB)

def new_rmb_menu(n_action: cTemplate):
    """
    Executes C++ bindings to create a Right-Click Context Menu.
    """
    coat.start_rmb_panel()
    n_action.IncludeContent()
    coat.show_rmb_panel()

class RMBMenu(cTemplate):
    """
    Class representing a Right-Click Context Menu.
    """
    def __init__(self, parent: cTemplate = None):
        cTemplate.__init__(self)
        self.Implementation = lambda: new_rmb_menu(self)
        self.if_has_Enabled_content = True
        if parent != None:
            parent.Content.append(self)


def d_rmb_menu(func):
        """
        Decorator to define a Right-Click Menu logic.
        
        Example (from voxTreeRmb.py):
            @d_rmb_menu
            def VoxTreeRmb():
                coat.menu_item("$AutoPick")
                coat.menu_item("EditProcedural")
        """
        n_action = RMBMenu()
        n_action.child = cTemplate()
        n_action.child.Implementation = func
        _force_register_member(func, n_action)
        n_action.Content.append(n_action.child)
        return n_action

#### Menu Section

def new_menu_section(n_action: cTemplate):
    """
    Executes C++ bindings to create a menu separator (section).
    """
    # if n_action.is_first:
    coat.menu_separator()
    n_action.IncludeContent()

class MenuSection(cTemplate):
    """
    Class representing a section within a menu (usually separated by a line).
    """
    def __init__(self, parent: cTemplate = None):
        cTemplate.__init__(self)
        self.Implementation =  lambda: new_menu_section(self)
        self.if_has_Enabled_content = True
        if parent != None:
            parent.Content.append(self)

def d_menu_section(Menu: cTemplate = None):
    """
    Decorator to define a Menu Section.
    Adds a separator before the content defined in the decorated function.

    Example (from File.py):
        @d_menu_section(CreateFileMenu)
        def S_New():
            coat.menu_item("CLEARSCENE") # New
            coat.menu_hotkey("N", 0, 1, 0) # CTRL+N
            coat.menu_item("OPEN_FILE") # Open
    """
    def cToolsSectionD(func):
        n_action = MenuSection()
        n_action.child = cTemplate()
        n_action.child.Implementation = func
        _force_register_member(func, n_action)
        n_action.Content.append(n_action.child)
        if Menu != None:
            Menu.Content.append(n_action)
        return n_action
    return cToolsSectionD