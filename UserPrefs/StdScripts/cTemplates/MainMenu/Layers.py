import coat
from cTemplates.Structs import *

LayersMenu = MainMenu("LAYERS")

@d_menu_section(LayersMenu)
def S_Show():
   """
   Section for toggling the visibility of Layer and Blending panels.
   
   Items:
   - Layers
   - Layer Blending
   """
   coat.menu_item("SHOW_LAYERS_LIST") # Layers
   coat.menu_hotkey("L", 0, 0, 0) # L
   coat.menu_item("SHOW_LAYER_BLENDING_LIST") # Layer Blending

@d_menu_section(LayersMenu)
def S_Edit():
   """
   Section for creating, duplicating, and deleting layers.
   
   Items:
   - New
   - Add Layer w/ Normal Map
   - Duplicate
   - Delete
   """
   coat.menu_item("ADD_NEW_LAYER") # New
   coat.menu_hotkey("N", 1, 1, 0) # SHIFT+CTRL+N
   coat.menu_item("ADD_LAYER_WITH_NM") # Add Layer w/ Normal Map
   coat.menu_item("DUPLICATE_LAYER") # Duplicate
   coat.menu_hotkey("D", 1, 1, 0) # SHIFT+CTRL+D
   coat.menu_item("DELETE_LAYER") # Delete
   coat.menu_hotkey("DELETE", 1, 1, 0) # SHIFT+CTRL+DELETE

@d_menu_section(LayersMenu)
def S_Merge():
   """
   Section for merging layers (visible, down, up).
   
   Items:
   - Merge Visible
   - Merge Down
   - Merge Up
   """
   coat.menu_item("MERGE_VISIBLE") # Merge Visible
   coat.menu_item("MERGE_DOWN") # Merge Down
   coat.menu_item("MERGE_UP") # Merge Up

@d_menu_section(LayersMenu)
def S_Cnl():
   """
   Section for channel-specific operations like filling, masking, and depth clamping.
   
   Items:
   - Copy Channels
   - Apply Layer Blending
   - Discard Clip Masked Pixels
   - Erase Unfrozen
   - Fill Entire Layer
   - Refill Material
   - Clamp Min. Depth
   - Clamp Layer Depth
   """
   coat.menu_item("Copy_channels") # Copy Channels
   coat.menu_item("ApplyBlending") # Apply Layer Blending
   coat.menu_item("APPLY_LMASK") # Discard Clip Masked Pixels
   coat.menu_item("DEL_UNFROZEN_PARTS") # Erase Unfrozen
   coat.menu_hotkey("DELETE", 0, 0, 0) # DELETE
   coat.menu_item("FILLLAYER1") # Fill Entire Layer
   coat.menu_hotkey("INS", 0, 0, 0) # INS
   coat.menu_item("FILLLAYERTR1") # Refill Material
   coat.menu_hotkey("INS", 0, 1, 0) # CTRL+INS
   coat.menu_item("Remove_spikes") # Clamp Min. Depth
   coat.menu_item("Clamp_layer_depth") # Clamp Layer Depth

@d_menu_section(LayersMenu)
def S_Extensions():
   """
   Inserts layer-related options provided by installed extensions.
   
   Items:
   - Layers extensions
   """
   coat.menu_insert_extensions("Layers")

@d_submenu("SYMM_OP", LayersMenu)
def SYMM_OP():
       """
       Submenu for symmetrical layer operations (flip, copy across symmetry).
       
       Items:
       - Flip Layer and Duplicate
       - Flip Layer
       - Copy Blue to Red
       - Copy Red to Blue
       """
       coat.menu_item("DUPLICATE_WITH_FLIP") # Flip Layer and Duplicate
       coat.menu_item("FLIP_LAYER") # Flip Layer
       coat.menu_item("COPY_BLUE_TO_RED") # Copy Blue to Red
       coat.menu_item("COPY_RED_TO_BLUE") # Copy Red to Blue
 
@d_submenu("Import", LayersMenu)
def Import():
       """
       Submenu for importing specific texture maps into layers.
       
       Items:
       - Layers Color
       - Glossiness Map (conditional)
       - Import Glossiness Layer (conditional)
       - Roughness (conditional)
       - Metalness
       - Depth
       - Layers.Import extensions
       """
       coat.menu_item("IMPORT_LAYERS_FROM_FILE") # Layers Color
       if coat.tex_approach() != 2:
           coat.menu_item("LOADSPEC") # Glossiness Map
           coat.menu_item("IMPORT_SPEC_LAYERS_FROM_FILE") # Import Glossiness Layer
     
       else:
           coat.menu_item("LOADROUGHNESS") # Roughness
     
       coat.menu_item("IMPORT_METAL_FROM_FILE") # Metalness
       coat.menu_item("IMPORT_DEPTH_FROM_FILE") # Depth
       coat.menu_insert_extensions("Layers.Import")
 
@d_submenu("Export", LayersMenu)
def Export():
       """
       Submenu for exporting specific texture maps from layers.
       
       Items:
       - Color
       - All Layers Color
       - Glossiness Map (conditional)
       - Import Glossiness Layer (conditional)
       - Roughness (conditional)
       - Metalness
       - Depth
       - Layers.Export extensions
       """
       coat.menu_item("EXPORT_IMAGE_TO_FILE") # Color
       coat.menu_item("EXPORT_LAYERS_TO_FILE") # All Layers Color
       if coat.tex_approach() != 2:
           coat.menu_item("SAVESPECL") # Glossiness Map
           coat.menu_item("IMPORT_SPEC_LAYERS_FROM_FILE") # Import Glossiness Layer
     
       else:
           coat.menu_item("SAVEROUGH") # Roughness
     
       coat.menu_item("EXPORT_METAL_TO_FILE") # Metalness
       coat.menu_item("EXPORT_DEPTH_TO_FILE") # Depth
       coat.menu_insert_extensions("Layers.Export")