import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Addons")
def AddonsMenu():
   """
   Creates the Addons menu for managing scripts, and additional packages.
   
   Items:
   - Install Extension
   - Look for addons
   - Browse addons folder
   - ListAddons
   - NewAddonsSection
   """
   coat.menu_item("InstallExtension") # Install Extension
   coat.menu_item("ForumScriptsRef") # Look for addons
   coat.menu_item("BrowseAddonsFolder") # Browse addons folder
   coat.menu_item("ListAddons") # ListAddons
   coat.menu_item("NewAddonsSection") # NewAddonsSection