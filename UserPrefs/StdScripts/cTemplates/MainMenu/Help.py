import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Help")
def HelpMenu():
   """
   Creates the Help menu containing documentation links, licensing tools, migration assistants, and update managers.
   
   Items:
   - This page description
   - 3DCoat Manual
   - Suggest UI Text Changes
   - Translate new texts
   - YouTube Channel
   - Install plugin license (deprecated)
   - Hotkeys & Sticky Keys
   - Hotkeys Manager
   - Migration Master 2021 -> 2022 and later
   - Migration Master from 4.9 to 20XX
   - Uninstall License
   - Show My Key (conditional)
   - SelLanguage
   - Community
   - {CY}Updates Manager
   - About 3DCoat
   - Help extensions
   """
   coat.menu_item("SetSmartSeams")
   coat.menu_item("ThisPageDoc") # This page description
   coat.menu_item("READ_MANUAL") # 3DCoat Manual
   coat.menu_item("ModifyHint") # Suggest UI Text Changes
   coat.menu_hotkey("F9", 0, 0, 0) # F9
   coat.menu_item("EditNewTexts") # Translate new texts
   coat.menu_item("YotubeChannel") # YouTube Channel
   coat.menu_item("InstallPluginLicense") # Install plugin license (deprecated)
   coat.menu_separator()
   coat.menu_item("Hotkeys_and_sticky") # Hotkeys & Sticky Keys
   coat.menu_item("HotkeysManager") # Hotkeys Manager
   coat.menu_item("MigrationMaster20XX") # Migration Master 2021 -> 2022 and later
   coat.menu_item("MigrationMaster49") # Migration Master from 4.9 to 20XX
   coat.menu_separator()
   coat.menu_item("UNINST_LICENCE") # Uninstall License
   if not coat.is_medical(): 
       coat.menu_item("ShowMyKey") # Show My Key
   coat.menu_separator()
   coat.menu_item("SelLanguage") # SelLanguage
   coat.menu_item("COMMUNITY") # Community
#    if not coat.is_medical(): 
#        coat.menu_item("Send_file_to_support") # Send File to support@pilgway.com
   coat.menu_separator()
   coat.menu_item("AutoUpdater") # {CY}Updates Manager
   # if (!is_steam_app())menu_item("CHECK_UPDATES");/Check for Updates
   coat.menu_item("ABOUT") # About 3DCoat
   coat.menu_insert_extensions("Help")