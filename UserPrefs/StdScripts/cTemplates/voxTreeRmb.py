import coat
from cTemplates.Structs import *

NoCache = True
Surface = True


def SetType(noCache, surface):
   """
   Sets the global state for cache and surface mode to determine menu availability.
   """
   global NoCache
   global Surface
   NoCache = noCache
   Surface = surface
     
@d_rmb_menu
def VoxTreeRmb():
   """
   The main Right-Click Menu (RMB) for the VoxTree (Sculpt Tree).
   Dynamic content based on whether the object is cached (Proxy) or is a Surface.
   
   Items:
   - Auto Pick
   - Edit procedural object
   - Reference Color
   """
   global NoCache
   global Surface
   NoCache = not coat.menu_property("RMBObjectInCache")
   Surface = coat.menu_property("RMBObjectIsSurface")

   coat.menu_item("$AutoPick") # Auto Pick
   coat.menu_item("EditProcedural") # Edit procedural object
   coat.menu_item("ChooseRefColor") # Reference Color

@d_submenu("Settings", VoxTreeRmb)
def Settings():
   """
   Submenu for visual settings related to the volume in the tree.
   
   Items:
   - Show Density near the Volume's Name
   - Show Polycount near the Volume's Name
   """
   coat.menu_item("ShowDensityNearVolumes") # Show Density near the Volume's Name
   coat.menu_item("ShowPolycountNearVolumes") # Show Polycount near the Volume's Name

S_tree = MenuSection(VoxTreeRmb)

@d_submenu("LiveBooleans", S_tree)
def LiveBooleans():
       """
       Submenu for non-destructive (Live) Boolean operations and tree management.
       
       Items:
       - Boolean Rules
       - Collapse Boolean tree
       - Clone & Collapse
       - Live Subtraction
       - Live Intersection
       - Live union
       - No Live Booleans
       """
       coat.menu_item("BooleanRules") # Boolean Rules
       coat.menu_item("CollapseBoolTree") # Collapse Boolean tree
       coat.menu_item("CloneCollapsedBTree") # Clone & Collapse
       coat.menu_item("LiveSubtraction") # Live Subtraction
       coat.menu_item("LiveIntersection") # Live Intersection
       coat.menu_item("LiveUnion") # Live union
       coat.menu_item("NormalSculptLayer") # No Live Booleans
 
@d_menu_section(VoxTreeRmb)
def S_Show():
   """
   Section for showing hidden volumes or subtrees.
   
   Items:
   - Show All Hidden Volumes
   - Show Hidden Volumes in Sub-Tree
   """
   coat.menu_item("ShowAll") # Show All Hidden Volumes
   coat.menu_item("ShowSubtree") # Show Hidden Volumes in Sub-Tree
@d_menu_section(VoxTreeRmb)
def S_Voxtree():
   """
   Section for basic tree management: Add, Delete, Rename.
   
   Items:
   - Delete
   - Add Child
   - Rename
   """
   coat.menu_item("DelVoxTree") # Delete
   coat.menu_item("AddVoxTree") # Add Child
   coat.menu_item("RenameVoxTree") # Rename
@d_menu_section(VoxTreeRmb)
def S_Dencity():
   """
   Section for resolution/density management, space transformation, and topological changes (Hull/Close Holes).
   
   Items:
   - Decrease Object 2X (Increase Density)
   - Increase Object 2X (Decrease Density)
   - To Global Space (conditional)
   - To Uniform Space (conditional)
   - Resample (conditional)
   - Radial Array (conditional)
   - Extrude (conditional)
   - Thicken (conditional)
   - Close Holes in Surface (conditional)
   - Separate Disconnected Parts (conditional)
   - Separate Selected/Frozen (conditional)
   - MakeHull (conditional)
   - Fill Voids (conditional)
   - Close Invisible Hulls (conditional)
   """
   coat.menu_item("IncDencity2X") # Decrease Object 2X (Increase Density)
   coat.menu_item("DecDencity2X") # Increase Object 2X (Decrease Density)
   if(NoCache):
       coat.menu_item("ToGlobalSpace") # To Global Space
       coat.menu_item("ToUniformSpace") # To Uniform Space
       coat.menu_item("Resample") # Resample
       coat.menu_item("AxialSymmetry") # Radial Array
       coat.menu_separator()
       coat.menu_item("ExtrudeVO") # Extrude
       if(Surface):
           coat.menu_item("CreateSurfaceShell") # Thicken
           coat.menu_item("CloseSurfaceHoles") # Close Holes in Surface
           coat.menu_item("Decompose") # Separate Disconnected Parts
           coat.menu_item("DecomposeFrozen") # Separate Selected/Frozen
     
       else:
           MakeHull()
         
           coat.menu_item("CloseHoles") # Fill Voids
           coat.menu_item("CloseInnerTunnels") # Close Invisible Hulls
     
@d_submenu("MakeHull", S_Dencity)
def MakeHull():
                    """
                    Submenu for creating a hull/shell from the volume.
                    
                    Items:
                    - Make Shell Mesh Using Voxels
                    - Thicken Using Surface
                    """        
                    coat.menu_item("MakeVoxHull") # Make Shell Mesh Using Voxels
                    coat.menu_item("MakeSurfHull") # Thicken Using Surface
 
@d_menu_section(VoxTreeRmb)
def S_Vox():
   """
   Section for I/O operations, shaders, and baking nodes.
   
   Items:
   - Save Volume as 3B
   - Save Volume w/ Sub-Tree as 3B
   - Import 3B File
   - Voxels extensions
   - Edit Shader Settings
   - Bake the Node Graph (conditional)
   - Import (submenu, conditional)
   - Import Point Cloud (conditional)
   - Import Object (conditional)
   """
   coat.menu_item("SaveVox3B") # Save Volume as 3B
   coat.menu_item("SaveVoxSubtree3B") # Save Volume w/ Sub-Tree as 3B
   coat.menu_item("MergeVox3B") # Import 3B File
   coat.menu_insert_extensions("Voxels")
   coat.menu_item("EditShaderSettings") # Edit Shader Settings
   if coat.menu_property("ObjectHasNodes"):
       coat.menu_item("BakeNodesToGeometry") # Bake the Node Graph
 
   if NoCache:
       if coat.menu_submenu("rmbImport"): # Import
           coat.menu_item("MergeCloud") # Import Point Cloud
           coat.menu_item("MergeObject") # Import Object
           coat.menu_exit()
     
 
@d_submenu("Export", S_tree)
def Export():
       """
       Submenu for exporting the selected volume or scene.
       
       Items:
       - Export Scene
       - Export Selected Objects
       - Save to Meshes Panel
       - Save to Splines Panel
       - Decimate > Auto-UV Map > Export (conditional)
       """
       coat.menu_item("ExportScene") # Export Scene
       coat.menu_item("ExportSelObject") # Export Selected Objects
       coat.menu_item("ExportPatternForMerge") # Save to Meshes Panel
       coat.menu_item("ExportCurveProfile") # Save to Splines Panel
       if coat.ue5_support():
           coat.menu_separator()
           coat.menu_item("DecimateAutoMapExport") # Decimate > Auto-UV Map > Export
     
S_Autopo = MenuSection(VoxTreeRmb)

@d_submenu("AUTOPO", S_Autopo)
def AUTOPO():
       """
       Submenu for Retopology operations (Auto-retopo, decimation).
       
       Items:
       - AUTOPO
       - AUTOPO w/ PTEX
       - AUTOPO w/ MV Painting
       - AUTOPO for Per Pixel
       - Old-style quadrangulation
       - Custom Retopology Tools
       - Retopo via decimation (conditional)
       - Retopo via decimation, visible objects (conditional)
       """
       coat.menu_item("Quadrangulate") # AUTOPO
       coat.menu_item("QuadrangulateAndMergePtex") # AUTOPO w/ PTEX
       coat.menu_item("QuadrangulateAndMerge") # AUTOPO w/ MV Painting
       coat.menu_item("QuadrangulateAndMergeDP") # AUTOPO for Per Pixel
       coat.menu_separator()
       coat.menu_item("OldStyleQuads") # Old-style quadrangulation
       coat.menu_separator()
       coat.menu_item("CustomRetopers") # Custom Retopology Tools
 
       if coat.RoomExists("Retopo"):
            coat.menu_item("DecimateToRetopo") # Retopo via decimation
            coat.menu_item("DecimateAllToRetopo") # Retopo via decimation, visible objects

@d_menu_section(VoxTreeRmb)
def S_transform():
   """
   Section for transforming the volume (Gizmo, snapping to ground).
   
   Items:
   - Transform
   - Snap to Ground
   - Lay on Ground
   """
   coat.menu_item("TransformVoxTree") # Transform
   coat.menu_item("PutOnGround") # Snap to Ground
   coat.menu_item("LayOnGround") # Lay on Ground

@d_submenu("Clone", VoxTreeRmb)
def Clone():
       """
       Submenu for cloning and instancing volumes.
       
       Items:
       - Clone Instance
       - Instance To Parent Instances
       - Clone
       - Instance w/ Symmetry
       - Clone w/ Symmetry
       - Clone & Degrade
       - Clone Space Density
       """
       coat.menu_item("CloneInstance") # Clone Instance
       coat.menu_item("InstanceToParentInstances") # Instance To Parent Instances
       coat.menu_item("CloneVoxTree") # Clone
       coat.menu_item("CloneInstanceSymm") # Instance w/ Symmetry
       coat.menu_item("CloneSymm") # Clone w/ Symmetry
       coat.menu_item("CloneDegrade") # Clone & Degrade
       coat.menu_item("CloneSpace") # Clone Space Density
 
@d_submenu("Flip", VoxTreeRmb)
def Flip():
       """
       Submenu for flipping the volume along axes.
       
       Items:
       - Flip X
       - Flip Y
       - Flip Z
       - Flip Normals (conditional)
       """
       global Surface
       coat.menu_item("VoxFlipX") # Flip X
       coat.menu_item("VoxFlipY") # Flip Y
       coat.menu_item("VoxFlipZ") # Flip Z
       if Surface:
           coat.menu_item("FlipNormals") # Flip Normals
     
 
@d_menu_section(VoxTreeRmb)
def S_BakeColorsFromAllVolumes():
   """
   Tool to bake vertex colors from other volumes onto the current one.
   
   Items:
   - Bake Color From Visible Volumes
   """
   coat.menu_item("BakeColorsFromAllVolumes") # Bake Color From Visible Volumes
@d_menu_section(VoxTreeRmb)
def S_SoftBooleansForVolumes():
   """
   Settings for Soft Boolean operations.
   
   Items:
   - Soft Booleans Settings
   """
   coat.menu_item("SoftBooleansForVolumes") # Soft Booleans Settings

@d_submenu("MergeMove", VoxTreeRmb)
def MergeMove():
       """
       Submenu for merging volumes or moving them into other volumes (Union).
       
       Items:
       - Merge Visible (no booleans) (conditional)
       - Merge Sub-Tree (no booleans) (conditional)
       - Merge Selected (no booleans) (conditional)
       - Copy & Merge (no booleans)... (conditional)
       - Merge (move, no booleans)... (conditional)
       - Merge Visible
       - Merge Sub-Tree
       - Merge Selected
       - Copy & Merge With...
       - Merge With (move to)...
       """
       if(Surface):
           coat.menu_item("PlainMergeVisible") # Merge Visible (no booleans)
           coat.menu_item("PlainMergeSubtree") # Merge Sub-Tree (no booleans)
           coat.menu_item("PlainMergeSelected") # Merge Selected (no booleans)
           coat.menu_item("PlainMergeTo") # Copy & Merge (no booleans)...
           coat.menu_item("PlainMoveTo") # Merge (move, no booleans)...
           coat.menu_separator()
     
       coat.menu_item("MergeVisible") # Merge Visible
       coat.menu_item("MergeSubtree") # Merge Sub-Tree
       coat.menu_item("MergeSelected") # Merge Selected
       coat.menu_item("MergeTo") # Copy & Merge With...
       coat.menu_item("MoveTo") # Merge With (move to)...
 
@d_menu_section(VoxTreeRmb)
def S_ops():
   """
   Section for Boolean operations (Subtract, Intersect, Split) and hierarchy changes.
   
   Items:
   - Copy & Subtract From...
   - Subtract From...
   - Intersect With...
   - Remove Intersection With...
   - Split With...
   - Change Parent...
   - Create Intersection Curve
   """
   coat.menu_item("CopySubtractFrom") # Copy & Subtract From...
   coat.menu_item("SubtractFrom") # Subtract From...
   coat.menu_item("IntersectWith") # Intersect With...
   coat.menu_item("RemoveIntersectionWith") # Remove Intersection With...
   coat.menu_item("SplitWith") # Split With...
   coat.menu_item("ChangeParent") # Change Parent...
   coat.menu_item("IntersectionCurveWith") # Create Intersection Curve