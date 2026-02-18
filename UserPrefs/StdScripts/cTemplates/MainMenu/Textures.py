import coat
from cTemplates.Structs import *

TexturesMenu = MainMenu("Textures")

@d_submenu("TexApproach", TexturesMenu)
def TexApproach():
       """
       Submenu to select the Texture Export/Import Workflow (PBR workflow).
       
       Items:
       - Gloss/Color Specular
       - Gloss/Metalness
       - Roughness/Metalness
       """
       coat.menu_item("GlossSpecular") # Gloss/Color Specular
       coat.menu_item("GlossMetallness") # Gloss/Metalness
       coat.menu_item("RoughnessMetallness") # Roughness/Metalness
 
@d_submenu("Import", TexturesMenu)
def ImportMenu():
       """
       Submenu for importing various texture maps and layers into the current project.
       
       Items:
       - Color/albedo Map
       - Layers Color
       - External AO
       - External Curvature
       - Glossiness Map (conditional)
       - Import Glossiness Layer (conditional)
       - Roughness (conditional)
       - Metalness Map
       - Specular Color (conditional)
       - Emissive
       - Emissive Intensity
       - Normal Map
       - World Space Normal Map
       - Displacement Map
       - Vector Displacement Map (conditional)
       - Import Depth Layer
       - Import Layer w/ Depth, Color & Glossiness
       - Flip PTEX Quads (conditional)
       - Color From PTEX (conditional)
       - Glossiness From PTEX (conditional)
       - Displacement From PTEX (conditional)
       - Vector Displacement From PTEX (conditional)
       - Absolute Positions From PTEX (conditional)
       - Textures.Import extensions
       """
       coat.menu_item("LOADTEX") # Color/albedo Map
       coat.menu_item("IMPORT_LAYERS_FROM_FILE") # Layers Color
       coat.menu_separator()
       coat.menu_item("ExternalAO") # External AO
       coat.menu_item("ExternalCavity") # External Curvature

       coat.menu_separator()
       if coat.tex_approach() != 2:
           coat.menu_item("LOADSPEC") # Glossiness Map
           coat.menu_item("IMPORT_SPEC_LAYERS_FROM_FILE") # Import Glossiness Layer
     
       else:
           coat.menu_item("LOADROUGHNESS") # Roughness
     
       coat.menu_separator()
       coat.menu_item("LOADMETAL") # Metalness Map
       if coat.tex_approach() == 0:
           coat.menu_item("LOADSPECCOL") # Specular Color
     
       coat.menu_separator()
       coat.menu_item("LOADEMISSIVE") # Emissive
       coat.menu_item("LOADEMISSIVE_BW") # Emissive Intensity
       coat.menu_separator()
       coat.menu_item("LOADLOPOLYTANG") # Normal Map
       coat.menu_item("ImportOSNormal") # World Space Normal Map
       coat.menu_separator()
       coat.menu_item("LOAD_LAYER_DISP") # Displacement Map
       if coat.is_mv():
           coat.menu_item("LOAD_LAYER_VDISP") # Vector Displacement Map
     
       coat.menu_item("IMPORT_DEPTH_LAYERS_FROM_FILE") # Import Depth Layer
       coat.menu_separator()
       coat.menu_item("IMPORT_ALL_LAYERS_FROM_FILES") # Import Layer w/ Depth, Color & Glossiness
       if coat.is_ptex():
           coat.menu_separator()
           coat.menu_item("FlipPtexQuads") # Flip PTEX Quads
           coat.menu_item("IMPORT_PTEX_COLOR") # Color From PTEX
           coat.menu_item("IMPORT_PTEX_SPECULAR") # Glossiness From PTEX
           coat.menu_item("IMPORT_PTEX_DISP") # Displacement From PTEX
           coat.menu_item("IMPORT_PTEX_VDISP") # Vector Displacement From PTEX
           coat.menu_item("IMPORT_PTEX_ABSPOS") # Absolute Positions From PTEX
     
       coat.menu_insert_extensions("Textures.Import")
 

@d_submenu("Export", TexturesMenu)
def ExportMenu():
       """
       Submenu for exporting various texture maps, layers, and Ptex data.
       
       Items:
       - Color/albedo Map
       - All Layers Color
       - Glossiness Map (conditional)
       - Roughness (conditional)
       - Metalness Map
       - Store gloss/roughness in metal alpha
       - Specular Color (conditional)
       - Normal Map (World-Space)
       - Normal Map (TS, Low-Poly Mesh)
       - Normal Map (TS, Layer0 Based) (conditional)
       - Normal Map (TS, Mid-poly Mesh) (conditional)
       - Displacement Map Current Layer
       - Displacement Map of Visible Layers
       - Export Depth Layer
       - Vector Displacement Map (conditional)
       - Export Layers w/ Depth, Color & Glossiness (conditional)
       - Flip PTEX Quads (conditional)
       - Color to PTEX (conditional)
       - Glossiness to PTEX (conditional)
       - Specular Color for PTEX (conditional)
       - Emissive Degree to PTEX (conditional)
       - Displacement to PTEX (conditional)
       - Vector Displacement to PTEX (conditional)
       - Absolute Positions to PTEX (conditional)
       - Export Layers w/ Depth, Color & Glossiness
       - Textures.Export extensions
       """
       coat.menu_item("SAVETEX") # Color/albedo Map
       coat.menu_item("EXPORT_LAYERS_TO_FILE") # All Layers Color
       coat.menu_separator()
       if coat.tex_approach() != 2:
           coat.menu_item("SAVESPECL") # Glossiness Map
     
       else:
           coat.menu_item("SAVEROUGH") # Roughness
     
       coat.menu_separator()
       coat.menu_item("SAVEMETAL") # Metalness Map
       coat.menu_item("UseMetAlpha") # Store gloss/roughness in metal alpha
       if coat.tex_approach() == 0:
           coat.menu_item("SAVECOLSPECL") # Specular Color
     
       # menu_separator();
       # menu_item("SAVEEMISS");/Emissive
       # menu_item("SAVEEMISSPOWR");/Emissive Intensity
       coat.menu_separator()
       coat.menu_item("SAVENM") # Normal Map (World-Space)
       coat.menu_item("SAVELOPOLYTANG") # Normal Map (TS, Low-Poly Mesh)
       if not coat.is_ppp():
           coat.menu_item("SAVELOPOLYTANGLAYER0") # Normal Map (TS, Layer0 Based)
           coat.menu_item("SAVEMIDPOLYTANG") # Normal Map (TS, Mid-poly Mesh)
     
       coat.menu_separator()
       coat.menu_item("SAVE_LAYER_DISP") # Displacement Map Current Layer
       coat.menu_item("SAVE_LAYERS_DISP") # Displacement Map of Visible Layers
       coat.menu_item("EXPORT_DEPTH_LAYERS_TO_FILE") # Export Depth Layer
       if coat.is_mv():
           coat.menu_item("SAVE_LAYERS_VDISP") # Vector Displacement Map
           coat.menu_item("EXPORT_ALL_LAYERS_TO_FILES") # Export Layers w/ Depth, Color & Glossiness
     
       if coat.is_ptex():
           coat.menu_separator()
           coat.menu_item("FlipPtexQuads") # Flip PTEX Quads
           coat.menu_item("EXPORT_PTEX_COLOR_TO_FILE") # Color to PTEX
           coat.menu_item("EXPORT_PTEX_SPECULAR_TO_FILE") # Glossiness to PTEX
           coat.menu_item("Export_ptex_specular_color") # Specular Color for PTEX
           coat.menu_item("Export_ptex_emissive_degree") # Emissive Degree to PTEX
           coat.menu_item("EXPORT_PTEX_DISP_TO_FILE") # Displacement to PTEX
           coat.menu_item("EXPORT_PTEX_VDISP_TO_FILE") # Vector Displacement to PTEX
           coat.menu_item("EXPORT_PTEX_ABSPOS_TO_FILE") # Absolute Positions to PTEX
     
       coat.menu_separator()
       coat.menu_item("EXPORT_ALL_LAYERS_TO_FILES") # Export Layers w/ Depth, Color & Glossiness
       coat.menu_insert_extensions("Textures.Export")

@d_menu_section(TexturesMenu)
def UV_SOURCE():
   """
   Option to use original UVs (available when not in Per-Pixel Painting mode).
   
   Items:
   - Use Original UV (conditional)
   """
   if not coat.is_ppp():
       coat.menu_item("UV_SOURCE") # Use Original UV
 
@d_menu_section(TexturesMenu)
def S_Alpha_CNL():
   """
   Settings for handling alpha channels in Normal and Color maps.
   
   Items:
   - Save Glossiness as Normal Map Alpha Channel
   - Save Displacement Map to Alpha
   - Don't Use Alpha in Normal Map
   - Don't Use Alpha in Color Map
   """
   coat.menu_item("SAVESPECINNM") # Save Glossiness as Normal Map Alpha Channel
   coat.menu_item("SAVEDISPINNM") # Save Displacement Map to Alpha
   coat.menu_item("DontUseAlphaInNM") # Don't Use Alpha in Normal Map
   coat.menu_item("DontUseAnphaAtAll") # Don't Use Alpha in Color Map
   coat.menu_separator()

@d_submenu("Adjust", TexturesMenu)
def Adjust():
       """
       Submenu for adjusting layer properties like color, glossiness, height, and applying filters.
       
       Items:
       - Color to Glossiness
       - Invert Color
       - Invert Glossiness
       - Set Height to Zero
       - Make Transparent
       - Remove Glossiness
       - Smooth Current Layer
       - Sharpen Current Layer
       - Hue/Saturation/Lightness
       - CMYK
       - Transform Color Space
       - Brightness/Contrast
       - RGB
       - Gamma Correction
       - Textures.Adjust extensions
       - To Uniform Color
       - Align colors
       - Color To Bump
       """
       coat.menu_item("COLOR2SPECULAR") # Color to Glossiness
       coat.menu_item("INVERTCOLOR") # Invert Color
       coat.menu_item("INVERTSPECULAR") # Invert Glossiness
       coat.menu_separator()
       coat.menu_item("SETZEROHEIGHT") # Set Height to Zero
       coat.menu_item("SETZEROCOLOR") # Make Transparent
       coat.menu_item("SETZEROSPECULAR") # Remove Glossiness
       coat.menu_separator()
       coat.menu_item("SMOOTH_LAYER") # Smooth Current Layer
       coat.menu_item("SHARPEN_LAYER") # Sharpen Current Layer
       coat.menu_item("HSV_LAYER") # Hue/Saturation/Lightness
       coat.menu_item("CMYK_LAYER") # CMYK
       coat.menu_item("TRANSCOLOR_LAYER") # Transform Color Space
       coat.menu_item("BC_LAYER") # Brightness/Contrast
       coat.menu_item("RGB_LAYER") # RGB
       coat.menu_item("GAMMA_LAYER") # Gamma Correction
       coat.menu_insert_extensions("Textures.Adjust")
       coat.menu_item("TO_UNIFORM_TOOL") # To Uniform Color
       coat.menu_item("ALIGN_COLORS_TOOL") # Align colors
       coat.menu_item("COLOR_TO_BUMP_TOOL") # Color To Bump
 

@d_menu_section(TexturesMenu)
def S_UV():
   """
   Section for importing and exporting UV sets and maps.
   
   Items:
   - Import UV
   - Export UV
   - Export SL Sculpt Map
   """
   coat.menu_item("IMPORTUV") # Import UV
   coat.menu_item("EXPORTUV") # Export UV
   coat.menu_item("SAVE_SL_PAINTMAP") # Export SL Sculpt Map

@d_menu_section(TexturesMenu)
def S_UV_Editor():
   """
   Section for UV editing tools and texture resolution settings.
   
   Items:
   - Texture UV Editor
   - UV Manager (conditional)
   - Mesh & Texture Resolution
   """
   coat.menu_item("VIEWEDIT_TEXTURES") # Texture UV Editor
   if coat.is_mv():
       coat.menu_item("UVSET_MANAGER") # UV Manager
 
   coat.menu_item("RESIZE_TOOL") # Mesh & Texture Resolution

@d_menu_section(TexturesMenu)
def S_Bake_Tool():
   """
   Section for texture baking and wrapping tools.
   
   Items:
   - Texture Baking Tool
   - Offset Tool
   """
   coat.menu_item("BAKE_TOOL") # Texture Baking Tool
   coat.menu_item("WRAP_TOOL") # Offset Tool

@d_menu_section(TexturesMenu)
def S_Extensions():
   """
   Inserts texture-related options provided by installed extensions.
   
   Items:
   - Textures extensions
   """
   coat.menu_insert_extensions("Textures")