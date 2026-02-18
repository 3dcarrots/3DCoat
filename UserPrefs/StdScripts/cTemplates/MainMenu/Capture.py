import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Capture")
def CaptureMenu():
   """
   Creates the Capture menu for recording timelapses, taking screenshots, and uploading models.
   
   Items:
   - Record Timelapse
   - Edit timelapse settings
   - Upload Screenshot
   - Upload Mesh to sketchfab.com
   - Create Turnable (MP4)
   - Render Turntables w/ Post Process
   """
   coat.menu_item("RecordTimelapse") # Record Timelapse
   coat.menu_item("EditTimelapseSettings") # Edit timelapse settings
   coat.menu_separator()
   coat.menu_item("UPLOAD_SCREENSHOT") # Upload Screenshot
   coat.menu_hotkey("S", 1, 0, 1) # SHIFT+ALT+S
   coat.menu_item("UploadToSketchFab") # Upload Mesh to sketchfab.com
   coat.menu_hotkey("K", 1, 0, 1) # SHIFT+ALT+K
   coat.menu_item("UPLOAD_TURNABLE") # Create Turnable (MP4)
   coat.menu_hotkey("T", 1, 0, 1) # SHIFT+ALT+T
   coat.menu_item("Reender_turnable_screenshots") # Render Turntables w/ Post Process