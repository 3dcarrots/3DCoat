import coat
from cTemplates.Structs import *

CreateFileMenu = MainMenu("FILE")

@d_menu_section(CreateFileMenu)
def S_New():
   """
   Creates the standard file operations section: New, Open, Recent, and Autosave.
   
   Items:
   - New
   - Open
   - Open Recent
   - Auto Save
   - Applinks (conditional)
   """
   coat.menu_item("CLEARSCENE") # New
   coat.menu_hotkey("N", 0, 1, 0) # CTRL+N
   coat.menu_item("OPEN_FILE") # Open
   coat.menu_hotkey("O", 0, 1, 0) # CTRL+O
   coat.menu_item("RecentFiles") # Open Recent
   coat.menu_item("Autosave") # Auto Save
   if not coat.is_new_scene(): 
       coat.menu_item("Applinks") # Applinks

@d_submenu("Install", CreateFileMenu)
def Install():
       """
       Submenu for installing various extensions and assets.
       
       Items:
       - Install Extension
       - Install Quixel asset as Smart Material
       - Install Quixel asset as Shader
       - Install Quixel asset as VerTexture
       """
       coat.menu_item("InstallExtension") # Install Extension
       coat.menu_item("InstallQuixelAssetAsMaterial") # Install Quixel asset as Smart Material
       coat.menu_item("InstallQuixelAssetAsShader") # Install Quixel asset as Shader
       coat.menu_item("InstallQuixelAssetAsFacture") # Install Quixel asset as VerTexture
 
@d_menu_section(CreateFileMenu)
def S_CreateExtension():
   """
   Section for creating new 3DCoat extensions.
   
   Items:
   - Create Extension
   """
   coat.menu_item("CreateExtension") # Create Extension


@d_submenu("Browse", CreateFileMenu)
def Browse():
       """
       Submenu for browsing various system and user data folders.
       
       Items:
       - Documents folder
       - Installation Folder
       - Alphas
       - Strips
       - Stencils
       - Smart Materials
       - User Data
       - Sample Objects
       - Sample 3D Alphas
       - Stored States
       - Color Swatches
       - Shaders
       - Temporary Folder
       """
       coat.menu_item("DocsFolder") # Documents folder
       coat.menu_item("InstFolder") # Installation Folder
       coat.menu_item("PensFolder") # Alphas
       coat.menu_item("StripsFolder") # Strips
       coat.menu_item("MasksFolder") # Stencils
       coat.menu_item("MaterialsFolder") # Smart Materials
       coat.menu_item("UserDataFolder") # User Data
       coat.menu_item("ObjSamplesFolder") # Sample Objects
       coat.menu_item("ObjPensSamplesFolder") # Sample 3D Alphas
       coat.menu_item("StoredStatesFolder") # Stored States
       coat.menu_item("PaletteFolder") # Color Swatches
       coat.menu_item("ShadersFolder") # Shaders
       coat.menu_item("TempFolder") # Temporary Folder
 
@d_menu_section(CreateFileMenu)
def S_Save():
   """
   Section for saving scenes and files, including incremental and Steam cloud saves.
   
   Items:
   - Save
   - Save As
   - Save Incrementally
   - Save to Steam Cloud (conditional)
   - File extensions
   """
   coat.menu_item("SAVE_FILEFAST") # Save
   coat.menu_hotkey("S", 0, 1, 0) # CTRL+S
   coat.menu_item("SAVE_FILE") # Save As
   coat.menu_hotkey("S", 0, 1, 1) # CTRL+ALT+S
   coat.menu_item("SAVE_INC") # Save Incrementally
   coat.menu_hotkey("S", 1, 1, 0) # SHIFT+CTRL+S
   if coat.is_steam_app():
        coat.menu_item("Save_to_Steam_cloud") # Save to Steam Cloud
   coat.menu_insert_extensions("File")
 
@d_menu_section(CreateFileMenu)
def S_csgo():
   """
   Specific section for CS:GO related imports/exports if configured.
   
   Items:
   - cs_import
   - cs_export
   - cs_texture
   - rust_export
   """
   if coat.CheckIfExists("csgo.txt"):
        coat.menu_submenu("CS:GO")
        coat.menu_item("cs_import") # cs_import
        coat.menu_item("cs_export") # cs_export
        coat.menu_item("cs_texture") # cs_texture
        coat.menu_item("rust_export") # rust_export
 
@d_submenu("Import", CreateFileMenu)
def Import():
       """
       Submenu for importing various mesh formats, planes, and reference objects depending on the active room mode.
       
       Items:
       - Import TF2 Sample (conditional)
       - Import TF2 Mesh as Voxel Reference (conditional)
       - Model for Per Pixel Painting
       - Simplified Import (conditional)
       - Simplified Import of Unclosed Surfaces (conditional)
       - Import for Sculpt/Vertex Painting/Reference (conditional)
       - Import Image as Mesh
       - Import for AUTOPO
       - Import Multiple Objects (conditional)
       - Model for Microvertex Painting
       - Model for PTEX
       - Import Retopo Mesh
       - Reference Mesh
       - Image Plane
       - Import Curve as Mesh
       - Import DICOM Slices
       - SL Object
       - VDB Object
       - Import Mesh for Voxelization
       - ImportGuides (conditional)
       - File.Import extensions
       - Import Raw Voxel Data (conditional)
       - Import Vertex Positions (conditional)
       - Import to Replace Geometry Only (conditional)
       - Import and Lock Normals (conditional)
       """
       if coat.is_steam_app():
           coat.menu_item("ImportTF2Mesh") # Import TF2 Sample
           coat.menu_item("MergeTF2_VoxelReference") # Import TF2 Mesh as Voxel Reference
           coat.menu_separator()
     
       coat.menu_item("ImportDPMesh") # Model for Per Pixel Painting
       if coat.is_medical():
           coat.menu_item("SimpleImportForVoxelizing") # Simplified Import
           coat.menu_item("SimpleImportForSurfaceVoxelizing") # Simplified Import of Unclosed Surfaces
     
       else:
           coat.menu_item("ImportForVertexPainting") # Import for Sculpt/Vertex Painting/Reference
     
       coat.menu_item("ImportImageAsMesh") # Import Image as Mesh
       coat.menu_item("IMPORT_FOR_RETOPO") # Import for AUTOPO
       if coat.IsInRoom("Voxels") or coat.IsInRoom("Retopo"):
           coat.menu_item("ImportObjectsByLayers") # Import Multiple Objects
     
       coat.menu_separator()
       coat.menu_item("OPENOBJ") # Model for Microvertex Painting
       coat.menu_hotkey("O", 1, 1, 0) # SHIFT+CTRL+O
       coat.menu_item("OPENOBJ_PTEX") # Model for PTEX
       coat.menu_separator()
       coat.menu_item("ImportRetopoMesh") # Import Retopo Mesh
       coat.menu_item("ImportRefMesh") # Reference Mesh
       coat.menu_separator()
       coat.menu_item("IMPORT_PLANE") # Image Plane
       coat.menu_hotkey("M", 1, 1, 0) # SHIFT+CTRL+M
       coat.menu_item("LoadSplineAs3DObject") # Import Curve as Mesh
       # Added import dicom object
       coat.menu_item("IMPORT_DICOM_OBJ") # Import DICOM Slices
       # if(las_support()){
       # 	menu_item("IMPORT_LAS_OBJECT");  Import las object
       # }
       coat.menu_item("IMPORT_SL_OBJECT") # SL Object
       coat.menu_item("IMPORT_VDB_OBJECT") # VDB Object
       coat.menu_item("ImportForVoxelizing") # Import Mesh for Voxelization
       if coat.is_medical():
           coat.menu_item("ImportGuides") # ImportGuides
     
       coat.menu_insert_extensions("File.Import")
       if coat.IsInRoom("Voxels"):
           coat.menu_item("ImportRawVoxelObject") # Import Raw Voxel Data
     
       if coat.is_ppp():
           coat.menu_separator()
           coat.menu_item("ImportPositions") # Import Vertex Positions
           coat.menu_item("ReplaceGeometry") # Import to Replace Geometry Only
           coat.menu_item("ImportLockedNormals") # Import and Lock Normals
     


Export = Submenu("Export", CreateFileMenu)

@d_menu_section(Export)
def S_Export_Voxels():
    """
    Export section specifically for Voxel room operations, including scene, objects, and raw data.
    
    Items:
    - Export Scene
    - Export Selected Objects
    - Decimate > Auto-UV Map > Export
    - Export Dense Quads
    - Export Projected Quads
    - Save to Meshes Panel
    - Save to Splines Panel
    - Export Raw Voxel Object
    - Export Depth Along Y
    """
    coat.menu_item("ExportScene") # Export Scene
    coat.menu_item("ExportSelObject") # Export Selected Objects
    coat.menu_item("DecimateAutoMapExport") # Decimate > Auto-UV Map > Export
    coat.menu_separator()
    coat.menu_item("ExportDenseQuads") # Export Dense Quads
    coat.menu_item("ExportProjectedQuads") # Export Projected Quads
    coat.menu_item("ExportPatternForMerge") # Save to Meshes Panel
    coat.menu_item("ExportCurveProfile") # Save to Splines Panel
    coat.menu_item("ExportRawVoxelObject") # Export Raw Voxel Object
    coat.menu_item("ExportDepthMap") # Export Depth Along Y
   
@d_submenu("ExportGltf", S_Export_Voxels)
def ExportGltf():
    """
    Submenu for exporting to GLTF format.
    
    Items:
    - Gltf Separate (.gltf + .bin + textures)
    - Gltf Embedded (.gltf)
    """
    coat.menu_item("ExportGltfSeparate") # Gltf Separate (.gltf + .bin + textures)
    coat.menu_item("ExportGltfEmbedded") # Gltf Embedded (.gltf)

@d_submenu("3D-Printing", S_Export_Voxels)
def Printing3D():
    """
    Submenu for 3D Printing tools and exports.
    
    Items:
    - Export For 3D Printing
    - Export and open in Cura
    - Prepare to publish
    """
    coat.menu_item("ExportForPrinting") # Export For 3D Printing
    coat.menu_item("ExportCura") # Export and open in Cura
    coat.menu_item("PrepareToPublish") # Prepare to publish


@d_menu_section(Export)
def S_Export_Retopo():
    """
    Export section for Retopology objects.
    
    Items:
    - Export Poly Object
    """
    coat.menu_item("ExportRtpMesh") # Export Poly Object
   
@d_menu_section(Export)
def S_Export_PPP():
    """
    Export section for Per-Pixel Painting objects.
    
    Items:
    - Export Objects & Textures
    """
    coat.menu_item("EXPORTOBJECT") # Export Objects & Textures
    # menu_item("WorkshopExport");/Export for Steam Workshop
    # if (ue5_support()){
    # 	menu_submenu("Export");
    # 	{		
    # 		menu_item("ToUE5");
    # 		menu_item("ToUE5As");
    # 		menu_item("EditUE5");
    # 	}
    # }
   
@d_menu_section(Export)
def S_Export_MV():
    """
    Export section for Microvertex Painting objects.
    
    Items:
    - Export Objects & Textures
    - High-poly Mesh
    - High-poly Mesh
    - High-poly Mesh
    """
    coat.menu_item("EXPORTOBJECT") # Export Objects & Textures
    coat.menu_item("SAVEHIPOLYX4") # High-poly Mesh
    coat.menu_item("SAVEHIPOLYX16") # High-poly Mesh
    coat.menu_item("SAVEHIPOLYX64") # High-poly Mesh



@d_template
def CheckRoom():
   """
   Checks the current active room and enables/disables relevant export menus accordingly.
   Runs before the file menu is displayed.
   """
   ExportGltf.Enabled = coat.gltf_support()
   S_Export_Voxels.Enabled = False
   Printing3D.Enabled      = False
   S_Export_Retopo.Enabled = False
   S_Export_PPP.Enabled    = False
   S_Export_MV.Enabled     = False

   if not coat.is_new_scene():
       if coat.IsInRoom("Voxels"):
           Printing3D.Enabled = True
           S_Export_Voxels.Enabled = True     
       if coat.IsInRoom("Retopo"):
           S_Export_Retopo.Enabled = True
       if coat.is_ppp():
           S_Export_PPP.Enabled = True
       if coat.is_mv():
           S_Export_MV.Enabled = True
         
CreateFileMenu.Before.append(CheckRoom)

@d_menu_section(CreateFileMenu)
def S_Export_Extensions():
       """
       Inserts export options provided by installed extensions.
       
       Items:
       - File.Export extensions
       """
       coat.menu_insert_extensions("File.Export")

@d_menu_section(CreateFileMenu)
def S_Exit():
   """
   Standard exit command.
   
   Items:
   - Exit
   """
   coat.menu_item("EXIT") # Exit