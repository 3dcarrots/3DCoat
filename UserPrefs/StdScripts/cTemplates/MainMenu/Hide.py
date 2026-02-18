import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Hide")
def HideMenu():
   """
   Creates the Hide menu for managing visibility of objects, materials, and faces.
   
   Items:
   - Activate Hide Tool
   - Hide Painting Object
   - Hide Surface Material
   - Unhide Painting Object
   - Unhide Surface Material
   - Unhide All
   - Hide Frozen Area
   - Invert Hidden Faces
   - Delete Hidden Faces Permanently
   - Expand Hidden Area
   - Contract Hidden Area
   - Store Hidden State
   - Restore Hidden State
   - Hide extensions
   """
   coat.menu_item("SWITCH_HIDE_TOOL") # Activate Hide Tool
   coat.menu_item("MENU_HIDE_OBJECT") # Hide Painting Object
   coat.menu_item("MENU_HIDE_MTL") # Hide Surface Material
   coat.menu_separator()
   coat.menu_item("MENU_UNHIDE_OBJECT") # Unhide Painting Object
   coat.menu_item("MENU_UNHIDE_MTL") # Unhide Surface Material
   coat.menu_item("MENU_UNHIDE_ALL") # Unhide All
   coat.menu_hotkey("X", 0, 1, 0) # CTRL+X
   coat.menu_item("HideFrozenArea") # Hide Frozen Area
   coat.menu_separator()
   coat.menu_item("MENU_INVERT_HIDE") # Invert Hidden Faces
   coat.menu_hotkey("X", 1, 1, 0) # CTRL+X
   coat.menu_item("MENU_DEL_PERMANENTLY") # Delete Hidden Faces Permanently
   coat.menu_separator()
   coat.menu_item("MENU_EXPAND_HIDE") # Expand Hidden Area
   coat.menu_hotkey("NUM_MINUS", 0, 0, 0) # NUM_MINUS
   coat.menu_item("MENU_CONTRACT_HIDE") # Contract Hidden Area
   coat.menu_separator()
   coat.menu_item("STORE_HIDE_DATA") # Store Hidden State
   coat.menu_item("RESTORE_HIDE_DATA") # Restore Hidden State
   coat.menu_insert_extensions("Hide")