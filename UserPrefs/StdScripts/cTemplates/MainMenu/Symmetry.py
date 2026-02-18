import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Symmetry")
def SymmetryMenu():
   """
   Creates the Symmetry menu for managing symmetry planes and toggles.
   
   Items:
   - No Symmetry
   - Toggle Symmetry
   - Symmetry
   - Reset Symmetry Planes
   - Show Symmetry Plane
   - Symmetry extensions
   """
   coat.menu_item("SYMMETRY_NONE") # No Symmetry
   coat.menu_item("ToggleSymmetry") # Toggle Symmetry
   coat.menu_item("SYMMETRY") # Symmetry
   coat.menu_hotkey("S", 0, 0, 0) # S
   coat.menu_separator()
   coat.menu_item("SYMMETRY_RESET") # Reset Symmetry Planes
   coat.menu_item("SHOW_SYMM_PLANE") # Show Symmetry Plane
   coat.menu_insert_extensions("Symmetry")


@d_template
def checkNewScene():
   SymmetryMenu.Enabled = not coat.is_new_scene()

SymmetryMenu.Before.append(checkNewScene)