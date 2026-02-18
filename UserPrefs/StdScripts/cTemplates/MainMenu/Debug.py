import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Debug")
def DebugMenu():
   """
   Creates the Debug menu for reloading internal resources like shaders and localization strings.
   
   Items:
   - Reload Shaders
   - Reload Text
   """
   coat.menu_item("Reload Shaders") # Reload Shaders
   coat.menu_item("Reload Text") # Reload Text