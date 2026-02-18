import coat
from cTemplates.Structs import *

CreateEditMenu = MainMenu("COMMANDS")

@d_menu_section(CreateEditMenu)
def S_Undo():
   """
   Section for Undo and Redo operations.
   
   Items:
   - Undo
   - Redo
   """
   coat.menu_item("UNDO") # Undo
   coat.menu_hotkey("Z", 0, 1, 0) # CTRL+Z
   coat.menu_item("REDO") # Redo
   coat.menu_hotkey("Y", 0, 1, 0) # CTRL+Y
   coat.menu_separator()

@d_submenu("GIZMOLESS", CreateEditMenu)
def GIZMOLESS():
       """
       Submenu for 'Transform without Gizmo'. 
       Contains tools for moving, scaling, and rotating objects numerically or via hotkeys without using the visual gizmo.
       
       Items:
       - Move to pick point
       - Move in screen space
       - Move along the X-axis
       - Move along the Y-axis
       - Move along the Z-axis
       - Scale uniformly (as a whole)
       - Scale along the X-axis
       - Scale along the Y-axis
       - Scale along the Z-axis
       - Rotate in screen space
       - Rotate around the X-axis
       - Rotate around the Y-axis
       - Rotate around the Z-axis
       - Transform via navigation
       """
       coat.menu_item("TRANSFORM_TRANSLATE_SNAP") # Move to pick point
       coat.menu_item("TRANSFORM_TRANSLATE_FREE") # Move in screen space
       coat.menu_item("TRANSFORM_TRANSLATE_X") # Move along the X-axis
       coat.menu_item("TRANSFORM_TRANSLATE_Y") # Move along the Y-axis
       coat.menu_item("TRANSFORM_TRANSLATE_Z") # Move along the Z-axis
       coat.menu_separator()
       coat.menu_item("TRANSFORM_SCALE_FREE") # Scale uniformly (as a whole)
       coat.menu_item("TRANSFORM_SCALE_X") # Scale along the X-axis
       coat.menu_item("TRANSFORM_SCALE_Y") # Scale along the Y-axis
       coat.menu_item("TRANSFORM_SCALE_Z") # Scale along the Z-axis
       coat.menu_separator()
       coat.menu_item("TRANSFORM_ROTATE_FREE") # Rotate in screen space
       coat.menu_item("TRANSFORM_ROTATE_X") # Rotate around the X-axis
       coat.menu_item("TRANSFORM_ROTATE_Y") # Rotate around the Y-axis
       coat.menu_item("TRANSFORM_ROTATE_Z") # Rotate around the Z-axis
       coat.menu_separator()
       coat.menu_item("StartObjTransform3D") # Transform via navigation
       coat.menu_hotkey("N", 0, 0, 0)
 
@d_menu_section(CreateEditMenu)
def S_DefineScaleCorrespondence():
   """
   Tool for editing scene scale settings.
   
   Items:
   - Scene Scale Master
   """
   coat.menu_item("DefineScaleCorrespondence") # Scene Scale Master

@d_menu_section(CreateEditMenu)
def S_UVOverlapping():
   """
   Tools for checking and managing UV overlaps (available in UV or Modeling rooms).
   
   Items:
   - Check UV Overlapping
   - Uncheck UV Overlapping
   """
   if coat.IsInRoom("UV") or coat.IsInRoom("Modeling"):
            coat.menu_item("CheckUVOverlapping") # Check UV Overlapping
            coat.menu_hotkey(">", 0, 1, 0) # CTRL+>
            coat.menu_item("UncheckUVOverlapping") # Uncheck UV Overlapping
            coat.menu_hotkey("<", 0, 1, 0) # CTRL+<
            coat.menu_separator()
 
@d_menu_section(CreateEditMenu)
def S_CalculateMaps():
   """
   Tools for calculating Occlusion, Curvature, and Light Baking maps.
   
   Items:
   - Calculate Occlusion
   - Calculate Curvature
   - Light Baking Tool
   """
   coat.menu_item("OCCLUSION_TOOL") # Calculate Occlusion
   coat.menu_item("CAVITY_TOOL") # Calculate Curvature
   coat.menu_item("LIGHTBAKING_TOOL") # Light Baking Tool

@d_menu_section(CreateEditMenu)
def S_Edit():
   """
   Tools for syncing layers with an external editor (e.g., Photoshop).
   
   Items:
   - Sync Layer w/ Ext. Editor
   - Edit All Layers in Ext. Editor
   - Edit All Roughness Layers
   - Edit All Metal Layers
   - Edit Projections in Ext. Editor
   """
   if not coat.is_new_scene():
        # menu_item("PSProjectionCommands");/PSProjectionCommands
        coat.menu_item("EDIT_CURR_LAYER") # Sync Layer w/ Ext. Editor
        coat.menu_item("EDIT_ALL_LAYERS") # Edit All Layers in Ext. Editor
        coat.menu_item("EDIT_ALL_ROUGH_LAYERS") # Edit All Roughness Layers
        coat.menu_item("EDIT_ALL_METAL_LAYERS") # Edit All Metal Layers
        coat.menu_item("EDIT_PROJECTION") # Edit Projections in Ext. Editor
@d_menu_section(CreateEditMenu)
def S_Project():
   """
   Projection settings for external editing.
   
   Items:
   - Project Through
   - External Editor Projection Scale
   """
   if not coat.is_new_scene():
        coat.menu_item("ProjectThrough") # Project Through
        coat.menu_item("Project_scale") # External Editor Projection Scale
 
@d_menu_section(CreateEditMenu)
def S_Options():
   """
   General application options, UI customization, and hotkey management.
   
   Items:
   - Load Hotkeys
   - Save Hotkeys
   - Customize UI
   - Preferences
   - Reset to Default Settings
   - Relocate 3DCoat's Data
   - Convert Older Materials (pre 4.5)
   """
   coat.menu_item("LoadHotkeys") # Load Hotkeys
   coat.menu_item("SaveHotkeys") # Save Hotkeys
   coat.menu_item("CustomizeUI") # Customize UI
   coat.menu_item("OPTIONS") # Preferences
   coat.menu_item("ResetSettings") # Reset to Default Settings
   coat.menu_item("EditDataPlacement") # Relocate 3DCoat's Data
   coat.menu_item("ConvertMaterials") # Convert Older Materials (pre 4.5)

@d_menu_section(CreateEditMenu)
def S_NodeGraph():
   """
   Tools for baking shader nodes.
   
   Items:
   - Bake Shader Nodes
   """
   coat.menu_item("NODEBAKING_TOOL") # Bake Shader Nodes

@d_menu_section(CreateEditMenu)
def S_Extension():
   """
   Inserts edit-related options provided by installed extensions.
   
   Items:
   - Edit extensions
   """
   coat.menu_insert_extensions("Edit")