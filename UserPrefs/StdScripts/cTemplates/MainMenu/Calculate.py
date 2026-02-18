import coat
from cTemplates.Structs import d_template, d_main_menu

@d_main_menu("Calculate")
def CalcMenu():
   """
   Creates the Calculate menu for generating ambient occlusion, curvature, and light maps.
   
   Items:
   - Calculate Occlusion
   - Calculate Curvature
   - Light Baking Tool
   """
   coat.menu_item("OCCLUSION_TOOL") # Calculate Occlusion
   coat.menu_item("CAVITY_TOOL") # Calculate Curvature
   coat.menu_item("LIGHTBAKING_TOOL") # Light Baking Tool