import coat
from cTemplates.Structs import *

BakeMenu = MainMenu("Bake")
@d_menu_section(BakeMenu)
def S1():
   """
   Section for baking settings, selection handling, and name correspondence.
   
   Items:
   - Bake Selected Only
   - Import Coarsed Mesh
   - Name Correspondence for Baking
   - Correspond Retopo Object w/ Sculpt Object
   - Bake Normals with Dithering
   """
   coat.menu_item("MergeSelectedOnly") # Bake Selected Only
   coat.menu_item("MergeCoarsedMesh") # Import Coarsed Mesh
   coat.menu_item("UseNamesCorrespondence") # Name Correspondence for Baking
   coat.menu_item("CheckGroupsCorrespondence") # Correspond Retopo Object w/ Sculpt Object
   coat.menu_item("BakeNormalmapsWithDithering") # Bake Normals with Dithering
@d_menu_section(BakeMenu)
def S2():
   """
   Section for updating existing paint geometry and configuring bake parameters.
   
   Items:
   - Baking Scan Settings
   - Re-Bake Sculpt Mesh changes onto Paint Mesh
   - Update Painting Mesh with Retopo Mesh
   """
   coat.menu_item("Baking_parameters") # Baking Scan Settings
   coat.menu_item("MergeIntoExisting") # Re-Bake Sculpt Mesh changes onto Paint Mesh
   coat.menu_item("ReplacePaintGeometry") # Update Painting Mesh with Retopo Mesh
@d_menu_section(BakeMenu)
def S_Disp():
   """
   Section for baking Normal Maps and Displacement for Per-Pixel Painting.
   
   Items:
   - {CY}Bake w/ Normal Map (Per-Pixel)
   - Retopo/Model to Per Pixel Painting without Baking
   - Bake w/ Normal Map (Per-Pixel) + flat displacement
   - Bake w/ Per Pixel Painting w/ Displacement
   """
   coat.menu_item("MergeForDPNM") # {CY}Bake w/ Normal Map (Per-Pixel)
   coat.menu_item("MergePatchIntoSceneDP") # Retopo/Model to Per Pixel Painting without Baking
   coat.menu_item("MergeForDPNM_flatdisp") # Bake w/ Normal Map (Per-Pixel) + flat displacement
   coat.menu_item("MergeForDP_disp") # Bake w/ Per Pixel Painting w/ Displacement
@d_menu_section(BakeMenu)
def S_PTex():
   """
   Section for baking operations specific to the PTex workflow.
   
   Items:
   - Bake w/ PTEX
   - Retopo->PTEX (no baking)
   """
   coat.menu_item("MergeIntoScenePtex") # Bake w/ PTEX
   coat.menu_item("MergePatchIntoScenePtex") # Retopo->PTEX (no baking)
@d_menu_section(BakeMenu)
def S_Microvertex():
   """
   Section for baking operations specific to the Microvertex workflow.
   
   Items:
   - Bake Into Scene (Microvertex)
   - Retopo->microvertex (no baking)
   """
   coat.menu_item("MergeIntoScene") # Bake Into Scene (Microvertex)
   coat.menu_item("MergePatchIntoScene") # Retopo->microvertex (no baking)
@d_menu_section(BakeMenu)
def S_Bake():
   """
   General texture baking commands and extensions insertion.
   
   Items:
   - Bake Texture
   - Bake extensions
   """
   coat.menu_item("BakeTexture") # Bake Texture
   coat.menu_insert_extensions("Bake")