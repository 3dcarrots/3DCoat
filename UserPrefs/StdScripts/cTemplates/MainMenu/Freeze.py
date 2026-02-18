import coat
from cTemplates.Structs import *

FreezeMenu = MainMenu("Freeze")

@d_menu_section(FreezeMenu)
def S1():
   """
   Section for activating freeze tools and toggling freeze visibility.
   
   Items:
   - Activate Freeze Tool (conditional)
   - Toggle Freeze View (conditional)
   - Show/Hide Freeze/Pose selection
   """
   if not coat.IsInRoom("Voxels"):
       coat.menu_item("SWITCH_FREEZE_TOOL") # Activate Freeze Tool
       coat.menu_item("TOGGLE_FREEZE_PATTERN") # Toggle Freeze View
       coat.menu_hotkey("F", 0, 0, 1) # ALT+F
 
   coat.menu_item("MENU_TOGGLE_FREEZE_VIEW") # Show/Hide Freeze/Pose selection
   coat.menu_no_hotkey("F", 0, 1, 0)
   coat.menu_hotkey("F", 0, 1, 1)

@d_menu_section(FreezeMenu)
def S2P():
   """
   Section for freezing pixels based on transparency, painting objects, or materials.
   
   Items:
   - Freeze Painted Pixels
   - Freeze Transparent Pixels
   - Freeze Painting Object
   - Freeze Surface Material
   """
   coat.menu_item("FREEZE_TRANSP") # Freeze Painted Pixels
   coat.menu_item("FREEZE_TRANSP_INV") # Freeze Transparent Pixels
   coat.menu_item("MENU_FREEZE_OBJECT") # Freeze Painting Object
   coat.menu_item("MENU_FREEZE_MTL") # Freeze Surface Material
@d_menu_section(FreezeMenu)
def S3():
   """
   Section for freezing based on current surface conditions or borders.
   
   Items:
   - Freeze Surface
   - Freeze Border
   """
   coat.menu_item("MENU_FREEZE_CURRENT_CONDITION") # Freeze Surface
   coat.menu_item("MENU_FREEZE_BORDER") # Freeze Border
   coat.menu_hotkey("NUM/", 0, 1, 0) # CTRL+NUM/
@d_menu_section(FreezeMenu)
def S4P():
   """
   Section for unfreezing objects, materials, or everything.
   
   Items:
   - Unfreeze Painting Object
   - Unfreeze Surface Material
   - Unfreeze All
   """
   coat.menu_item("MENU_UNFREEZE_OBJECT") # Unfreeze Painting Object
   coat.menu_item("MENU_UNFREEZE_MTL") # Unfreeze Surface Material
   coat.menu_item("MENU_UNFREEZE_ALL") # Unfreeze All
   coat.menu_hotkey("D", 0, 1, 0) # CTRL+D
@d_menu_section(FreezeMenu)
def S5():
   """
   Section for modifying the freeze mask (invert, blur, sharpen) and operations on frozen/unfrozen parts.
   
   Items:
   - Invert Freeze/Selection
   - Smooth Freezing
   - Sharpen Freezing
   - Fill Entire Layer
   - Erase Unfrozen
   - Hide Frozen Area
   """
   coat.menu_item("MENU_INVERT_FREEZE") # Invert Freeze/Selection
   coat.menu_hotkey("I", 1, 1, 0) # SHIFT+CTRL+I
   coat.menu_item("MENU_BLUR_FREEZE") # Smooth Freezing
   coat.menu_hotkey("NUM*", 0, 1, 0) # CTRL+NUM*
   coat.menu_item("MENU_SHARPEN_FREEZE") # Sharpen Freezing
   coat.menu_item("FILLLAYER1") # Fill Entire Layer
   coat.menu_item("DEL_UNFROZEN_PARTS") # Erase Unfrozen
   coat.menu_item("HideFrozenArea") # Hide Frozen Area
@d_menu_section(FreezeMenu)
def S6():
   """
   Section for expanding or contracting the frozen area.
   
   Items:
   - Expand Frozen Area
   - Contract Frozen Area
   """
   coat.menu_item("MENU_EXPAND_FREEZE") # Expand Frozen Area
   coat.menu_hotkey("NUM_MINUS", 0, 1, 0) # CTRL+NUM_MINUS
   coat.menu_item("MENU_CONTRACT_FREEZE") # Contract Frozen Area
@d_menu_section(FreezeMenu)
def S7():
   """
   Section for storing and restoring the freeze state, and loading extensions.
   
   Items:
   - Store Freezing State
   - Restore Freezing State
   - Freeze extensions
   """
   coat.menu_item("STORE_FREEZE_DATA") # Store Freezing State
   coat.menu_item("RESTORE_FREEZE_DATA") # Restore Freezing State
   coat.menu_insert_extensions("Freeze")