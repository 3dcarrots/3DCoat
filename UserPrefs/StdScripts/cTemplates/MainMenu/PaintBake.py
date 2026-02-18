import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Bake")
def PaintBakeMenu():
   """
   Creates the Bake menu for moving objects between Paint and Sculpt rooms and updating existing meshes.
   
   Items:
   - Paint Mesh to Sculpt Mesh ({CY}No Color or Subdivision{C})
   - Paint Mesh to Sculpt Mesh ({CY}Baked Texture & Subdivision{C})
   - Paint Mesh to Sculpt Mesh (Subdivided Only)
   - Name Correspondence for Baking
   - Re-Bake Sculpt Mesh changes onto Paint Mesh
   """
   coat.menu_item("GetObjectFromPaintRoom") # Paint Mesh to Sculpt Mesh ({CY}No Color or Subdivision{C})
   coat.menu_item("GetTexturedObjectFromPaintRoom") # Paint Mesh to Sculpt Mesh ({CY}Baked Texture & Subdivision{C})
   coat.menu_item("GetSubdObjectFromPaintRoom") # Paint Mesh to Sculpt Mesh (Subdivided Only)
   coat.menu_separator()
   coat.menu_item("UseNamesCorrespondence") # Name Correspondence for Baking
   coat.menu_item("MergeIntoExisting") # Re-Bake Sculpt Mesh changes onto Paint Mesh