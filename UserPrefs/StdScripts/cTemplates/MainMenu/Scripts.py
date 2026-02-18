import coat
from cTemplates.Structs import *

ScriptsMenu = MainMenu("Scripts")

@d_menu_section(ScriptsMenu)
def Scripts_S_RunScript():
    """
    Section for executing existing scripts.
    
    Items:
    - Run Script
    """
    coat.menu_item("RunScript") # Run Script

@d_menu_section(ScriptsMenu)
def Scripts_S_Tools():
    """
    Section containing Python-specific tools, console, documentation, and package management.
    
    Items:
    - Create the {CY}Python{C} script
    - Show the {CY}Python{C} console
    - {CY}Python API{C} documentation
    - Install python packages
    - Uninstall Python Packages
    - Attach to the Python debugger
    - Show the commands log
    """
    coat.menu_item("CreatePythonScript") # Create the {CY}Python{C} script
    coat.menu_item("ShowPyConsole") # Show the {CY}Python{C} console
    coat.menu_item("PythonAPI_Docs") # {CY}Python API{C} documentation
    coat.menu_item("PipInstall") # Install python packages
    coat.menu_item("PipUnInstall") # Uninstall Python Packages
    coat.menu_item("AttachToPytonDebugger") # Attach to the Python debugger
    coat.menu_item("ShowPyCommandsLog") # Show the commands log
    
@d_menu_section(ScriptsMenu)
def Scripts_S_Useful():
    """
    Section for Core API (C++) scripting tools and documentation.
    
    Items:
    - Create New {CY}Core API{C} Script
    - {CY}Core API{C} Documentation
    """
    coat.menu_item("CreateNewCoreScript") # Create New {CY}Core API{C} Script
    coat.menu_item("CoreAPI_Docs") # {CY}Core API{C} Documentation

UseFulScriptsSubMenu = Submenu("UseFulScripts", ScriptsMenu)
Export = Submenu("Export", UseFulScriptsSubMenu)

@d_menu_section(ScriptsMenu)
def Scripts_S_Edit():
    """
    Section for script recording, legacy scripting tools, and extension insertion.
    
    Items:
    - Stop Record Script (conditional)
    - Start Record Script (conditional)
    - Scripts extensions
    - RecentScripts
    """
    #coat.menu_item("CreateScript") # Create Angelscript (simplified C++) 
    # coat.menu_item("HowToWriteScripts") # Scripting Manual
    #coat.menu_item("ViewExecutionLog") # View Execution Log
 
    if coat.UseRecordScript():
        if coat.IsRecordScript():
            coat.menu_item("StopRecordScript") # Stop Record Script
        else:
            coat.menu_item("RecordScript") # Start Record Script
  
    coat.menu_insert_extensions("Scripts")
    coat.menu_item("RecentScripts") # RecentScripts