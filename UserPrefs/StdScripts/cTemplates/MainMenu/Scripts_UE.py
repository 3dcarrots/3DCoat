import coat
from cTemplates.Structs import *
from cTemplates.MainMenu.Scripts import Export

@d_menu_section(Export)
def ExportToUE():
    """
    Section for exporting projects to Unreal Engine 5.
    
    Items:
    - Export to UE5
    - Export to UE5 as ...
    - Edit UE5 script
    """
    coat.menu_item("ToUE5") # Export to UE5
    coat.menu_item("ToUE5As") # Export to UE5 as ...
    coat.menu_item("EditUE5") # Edit UE5 script

@d_template
def CheckExportUE():
    """
    Enables the UE export menu only if UE5 support is active, the scene is not new,
    and the user is in the Voxels room or Paint room (Per-Pixel Painting).
    """
    ExportToUE.Enabled = False
    if coat.ue5_support():
        if not coat.is_new_scene():
            if coat.IsInRoom("Voxels"):
                ExportToUE.Enabled = True
            if coat.IsInRoom("Paint"):
                if coat.is_ppp():
                    ExportToUE.Enabled = True

ExportToUE.Before.append(CheckExportUE)