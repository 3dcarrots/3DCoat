# 
# The Sculpt (Voxels) room toolset definition.
# 
# Insert commands and conditions within the main(){...} function
# use 
#   tools_item("IdentifierOfTheTool");
# to add new item into the toolset.
# use 
#   tools_section("Section name");
# to add tools section.
# The command
#   default_tool("IdentifierOfTheTool");
# defines the tool used by default in the room.
# 
# 
import coat
from cTemplates.Structs import *

proxy = False
vox = False

def SetType(Proxy, Vox):
    """
    Sets the global state for Proxy and Voxel modes to determine available tools.
    """
    global proxy
    global vox
    proxy = Proxy
    vox = Vox

@d_template
def InstallCurvesExtensions():
   """
   Adds curve-based surface generation tools.

   Tools in this section:
   - Vox Layer
   - Coat
   - Tube/Array
   - Array/Bend Volume
   - Sweep along Guide
   - Surface of Revolution
   - Polyhedron
   - Swept 2 Guide
   - Swept 2 Gener
   - Swept N Gener
   """
   coat.tools_item("[extension]VoxLayer") # Vox Layer
   coat.tools_item("[extension]CurvesLayer") # Coat
   coat.tools_item("[extension]TubeOnCurve") # Tube/Array
   coat.tools_item("[extension]BendVolume") # Array/Bend Volume
   coat.tools_item("[extension]SweptSurface") # Sweep along Guide
   coat.tools_item("[extension]RotateSurface") # Surface of Revolution
   coat.tools_item("[extension]SurfacePrism") # Polyhedron
   coat.tools_item("[extension]SurfaceSwept2") # Swept 2 Guide
   coat.tools_item("[extension]SurfaceSwept2Gener") # Swept 2 Gener
   coat.tools_item("[extension]SurfaceSweptNGener") # Swept N Gener


@d_tools_section("Layers")
def Layers():
      """
      Tools for manipulating Sculpt Layers (magnifying or erasing depth).

      Tools in this section:
      - Magnify SL
      - Erase SL
      """
      coat.tools_item("[extension]MagnifyLayers") # Magnify SL
      coat.tools_item("[extension]EraseLayers") # Erase SL

@d_tools_section("Clay/Draw")
def BaseSurfaceTools():
   """
   The core sculpting brushes available in Surface mode (and partially in Voxel mode).

   Tools in this section:
   - Clay
   - Draw
   - Flatten
   - Chisel
   - Flat Polish
   - Trim Adaptive
   - Fill
   - Lute
   - Buildup
   - Extrude
   - Pick & Paste
   - Expand
   - Absolute
   - Rapid
   - Rapid Smooth
   - Scratches
   - Mud
   - Pinch
   - Roof Pinch
   - Smart Pinch
   - Shift
   - Smooth
   - Super Relax
   - Smooth Convex
   - Smooth Concave
   - Tangent
   - Sharpen
   - Freeze
   - Surface Hide
   - Snake Clay
   - Copy Clay
   """
   coat.tools_item("[extension]SCULP_SCLAY") # Clay
   coat.tools_item("[extension]SCULPT_DRAW") # Draw
   coat.tools_item("{FLT}[extension]SCULP_PLANE") # Flatten
   coat.tools_item("{FLT}[extension]SCULP_PLANE2") # Chisel
   coat.tools_item("{FLT}[extension]FlatPolish") # Flat Polish
   coat.tools_item("{FLT}[extension]trim_adaptive") # Trim Adaptive
   coat.tools_item("{FILL}[extension]SCULP_SFILL") # Fill
   coat.tools_item("{FILL}[extension]SCULP_SFILL2") # Lute
   coat.tools_item("[extension]BUILDUP") # Buildup
   coat.tools_item("[extension]SCULP_SFEXTRUDE0") # Extrude
   coat.tools_item("[extension]PickVDM") # Pick & Paste
   coat.tools_item("[extension]SCULP_INFLATE") # Expand
   # tools_item("[VOX_SCULPT_TOOL]SCULP_SFEXTRUDE");Gum
   coat.tools_item("[extension]SCULP_SFEXTRUDEA") # Absolute
   coat.tools_item("{RAPID}[extension]SCULPT_RAPID") # Rapid
   coat.tools_item("{RAPID}[extension]RAPID2") # Rapid Smooth
   coat.tools_item("{RAPID}[extension]SCULPT_CLAWS") # Scratches
   # tools_item("{RAPID}[VOX_SCULPT_TOOL]CLAWS2");Scratches2
   coat.tools_item("{RAPID}[extension]SCULPT_MUD") # Mud
   # tools_item("{RAPID}[VOX_SCULPT_TOOL]MUD2");Mud 2
   coat.tools_item("{PINCH}[extension]SCULPT_PINCH") # Pinch
   coat.tools_item("{PINCH}[extension]RoofPinch") # Roof Pinch
   coat.tools_item("{PINCH}[extension]SmartPinch") # Smart Pinch
   coat.tools_item("[extension]SCULP_FOLLOW") # Shift
   if vox:
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_SMOOTH1") # Smooth
   else: 
      coat.tools_item("{RELAX}[VOX_SCULPT_TOOL]SCULPT_SMOOTH") # Smooth
   coat.tools_item("{RELAX}[extension]SuperRelax") # Super Relax
   coat.tools_item("{RELAX}[extension]smooth_convex") # Smooth Convex
   coat.tools_item("{RELAX}[extension]smooth_concave") # Smooth Concave
   coat.tools_item("{RELAX}[extension]TangentRelax") # Tangent
   coat.tools_item("[extension]Sharpen") # Sharpen
   coat.tools_item("{MASK}[VOX_SCULPT_TOOL]SCULP_SFREEZE") # Freeze
   coat.tools_item("{MASK}[VOX_SCULPT_TOOL]SurfHide") # Surface Hide
   if not proxy:
      coat.tools_item("[extension]SnakeClay") # Snake Clay
      coat.tools_item("[extension]CopyClay") # Copy Clay


@d_tools_section("Paint")
def PaintTools():
   """
   Painting tools for vertex/ptex/microvertex painting within the Sculpt room.

   Tools in this section:
   - Brush
   - Airbrush
   - Coloring
   - Smudge
   - Power Smooth
   - Clone
   - Curves
   - Text
   - Eraser
   - Fill
   """
   coat.tools_item("[StdPen]StdPen") # Brush
   coat.tools_item("[Airbrush]Airbrush") # Airbrush
   coat.tools_item("[ChangeColor]ChangeColor") # Coloring
   coat.tools_item("[SmudgeTool]SmudgeTool") # Smudge
   coat.tools_item("[POWRELAX]POWRELAX") # Power Smooth
   coat.tools_item("[CloneTool]CloneTool") # Clone
   coat.tools_item("[CurveTool]CurveTool") # Curves
   coat.tools_item("[TextTool]TextTool") # Text
   coat.tools_item("[EraserTool]EraserTool") # Eraser
   coat.tools_item("[FillTool]FillTool") # Fill


@d_tools_section("Adjust")
def AdjustProxy():
      """
      Adjustment tools specifically for Proxy mode (Multiresolution low level).

      Tools in this section:
      - Noise
      - Quick Pick
      - Pose
      - Fit
      - Reproject
      - Move
      - Measure
      - Transform
      - Instancer
      """
      coat.tools_item("[extension]Noise") # Noise
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_PICK") # Quick Pick
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
      coat.tools_item("[extension]FitTool") # Fit
      coat.tools_item("[extension]Reproject") # Reproject
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
      coat.tools_item("[extension]Measure") # Measure
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
      # tools_item("[extension]SCULPT_AXIAL");Axial


@d_tools_section("Adjust")
def AdjustVoxel():
      """
      Adjustment tools specific to Voxel mode.

      Tools in this section:
      - Cut Off
      - Measure
      - 3D-Print Supports
      - Vox Slice
      - Quick Pick
      - Fit
      - Reproject
      - Vox Hide
      - Cell
      - Copy
      - Bas-Relief
      - Undercuts
      - Moulding
      """
      coat.tools_item("[extension]CutOff") # Cut Off
      coat.tools_item("[extension]Measure") # Measure
      coat.tools_item("[extension]Supports") # 3D-Print Supports
      coat.tools_item("[extension]VoXRay") # Vox Slice
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_PICK") # Quick Pick
      coat.tools_item("[extension]FitTool") # Fit
      coat.tools_item("[extension]Reproject") # Reproject
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_HIDE") # Vox Hide
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_CLHIDE") # Cell
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_COPY") # Copy
      coat.tools_item("[extension]SCULPT_BARELIEF") # Bas-Relief
      coat.tools_item("[extension]Undercuts") # Undercuts
      coat.tools_item("[extension]Molding") # Moulding


@d_tools_section("Adjust")
def AdjustSurface():
      """
      Adjustment tools specific to Surface mode.

      Tools in this section:
      - Sculpt Bevel
      - Cut Off
      - Noise
      - Close Hole
      - Reconstruct
      - MeshDoctor
      - Clean Clay
      - Fill Holes
      - Poly Remove
      - Angulator
      - Dissolve
      - Subdivide
      - Measure
      - 3D-Print Supports
      - Vox Slice
      - Extrude Faces
      - Bridge
      - Quick Pick
      - Bas-Relief
      - Undercuts
      - Moulding
      """
      coat.tools_item("[extension]SculptBevel") # Sculpt Bevel
      coat.tools_item("[extension]CutOff") # Cut Off
      coat.tools_item("[extension]Noise") # Noise
      coat.tools_item("{HEAL}[extension]CloseHole") # Close Hole
      coat.tools_item("{HEAL}[extension]Reconstruct") # Reconstruct
      coat.tools_item("{HEAL}[extension]MeshDoctor") # MeshDoctor
      coat.tools_item("{HEAL}[extension]CleanClay") # Clean Clay
      coat.tools_item("[extension]FillHoles") # Fill Holes
      coat.tools_item("[extension]PaintHole") # Poly Remove
      if not coat.is_proxy():
         coat.tools_item("[extension]SuperPinch") # Angulator
         coat.tools_item("[extension]InfSmooth") # Dissolve
         coat.tools_item("[extension]Subdivide") # Subdivide
   
      coat.tools_item("[extension]Measure") # Measure
      coat.tools_item("[extension]Supports") # 3D-Print Supports
      coat.tools_item("[extension]VoXRay") # Vox Slice
      coat.tools_item("[extension]ExtrudeFaces") # Extrude Faces
      # tools_item("[extension]QuickPose");Quick Pose		
      coat.tools_item("[extension]Bridge") # Bridge
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_PICK") # Quick Pick
      coat.tools_item("[extension]SCULPT_BARELIEF") # Bas-Relief
      coat.tools_item("[extension]Undercuts") # Undercuts
      coat.tools_item("[extension]Molding") # Moulding


@d_tools_section("Objects")
def SurfaceObjects():
      """
      Generators, Primitives, and object creation tools for Surface mode.

      Tools in this section:
      - Primitives
      - Import
      - Tree generator
      - Logo
      - Sketch
      - Split & Joints
      - Split
      - Clone
      - Cut & Clone
      - Vox Extrude
      - Vox Layer
      - Points to Polygons
      - Snake
      - Spikes
      - Toothpaste
      - Tubes/Muscle
      - Cloth
      - Joints
      """
      coat.tools_item("[extension]SCULP_PRIM") # Primitives
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MERGE") # Import
      coat.tools_item("[extension]TreesGenerator") # Tree generator
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_LOGO") # Logo
      coat.tools_item("{CREATESIMP}[extension]SCULP_SKETCH") # Sketch
      coat.tools_item("[extension]SplitNJoint") # Split & Joints
      coat.tools_item("[extension]SCULPT_RECTSPLIT") # Split
      coat.tools_item("{clone}[extension]SCULPT_CLONE") # Clone
      coat.tools_item("{clone}[extension]SCULPT_CUTNCLONE") # Cut & Clone
      coat.tools_item("[extension]VoxExtrude") # Vox Extrude
      coat.tools_item("[extension]VoxLayer") # Vox Layer
      coat.tools_item("[RetopoTool]TopToolAddPoints") # Points to Polygons
      coat.tools_item("{snake}[extension]SCULP_SPSTROKE") # Snake
      coat.tools_item("{snake}[extension]SCULP_FREESP") # Spikes
      coat.tools_item("{snake}[extension]SCULP_TUBE") # Toothpaste
      coat.tools_item("{snake}[extension]SCULP_MUSCLE") # Tubes/Muscle
      coat.tools_item("{snake}[extension]SCULP_CLOTH") # Cloth
      coat.tools_item("[extension]JointsTool") # Joints


@d_tools_section("Custom")
def Custom():
      """
      Section for user-created or duplicated brushes.

      Tools in this section:
      - Base Brush
      - Add Brush
      """
      coat.tools_item("[extension]BaseBrush") # Base Brush
      coat.tools_item("AddNewBrush") # Add Brush      

@d_tools_section("ClayEngine")
def ClayEngine():
      """
      Voxel-specific clay engine brushes.

      Tools in this section:
      - Base Clay
      - Wet Clay
      - Vox Extrude
      - Vox Buildup
      - Thick layer
      """
      coat.tools_item("[extension]BaseVoxBrush") # Base Clay
      coat.tools_item("[extension]WetClay") # Wet Clay
      coat.tools_item("[extension]Extruder") # Vox Extrude
      coat.tools_item("[extension]VoxBuildup") # Vox Buildup
      coat.tools_item("[extension]LayerClay") # Thick layer


@d_tools_section("VoxelTools")
def Voxel():
      """
      General Voxel sculpting tools (Grow, Fill, Carve, etc.).

      Tools in this section:
      - Vox Clay
      - Grow
      - Build
      - Airbrush
      - Smooth
      - Fill
      - Carve
      - Blob
      - Sphere
      - 2D-Paint
      - Plane
      - Scrape
      - Pinch
      - Smudge
      """
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_CLAY") # Vox Clay
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_GROW") # Grow
      coat.tools_item("{LEGACYVOX}[extension]SCULPT_BUILD") # Build
      coat.tools_item("{LEGACYVOX}[VOX_SCULPT_TOOL]SCULPT_ALPGROW") # Airbrush
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_SMOOTH") # Smooth
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_FILL") # Fill
      coat.tools_item("[extension]SCULPT_CARVE") # Carve
      coat.tools_item("[extension]Blob") # Blob
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_SPHERE") # Sphere
      coat.tools_item("[extension]SCULPT_BRANCH") # 2D-Paint
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_RASPFILE") # Plane
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_VXPLANE") # Scrape
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_VXPINCH") # Pinch
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_VXFOLLOW") # Smudge


@d_tools_section("Pose")
def Pose():
      """
      Tools for posing, transforming, and arraying objects.

      Tools in this section:
      - Transform
      - Instancer
      - Move
      - Pose
      - Fit
      - Reproject
      - Bend
      - Twist
      - Warp
      - Array
      - Surface Array
      """
      coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
      coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move                
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
      coat.tools_item("[extension]FitTool") # Fit
      coat.tools_item("[extension]Reproject") # Reproject

      coat.tools_item("[extension]SCULP_BEND") # Bend
      coat.tools_item("[extension]SCULP_TWIST") # Twist
      coat.tools_item("[extension]SCULP_WRAP") # Warp
      # 		tools_item("[extension]SCULPT_AXIAL");Axial
      coat.tools_item("[extension]Sculpt_Array") # Array	
      coat.tools_item("[extension]MultiObject") # Surface Array


@d_tools_section("Objects")
def Objects():
      """
      Object creation and import tools for Voxel/General modes.

      Tools in this section:
      - Primitives
      - Import
      - Tree generator
      - LAS Point Cloud
      - Logo
      - Constructor
      - Sketch
      - Split
      - Clone
      - Cut & Clone
      - Vox Extrude
      - Vox Layer
      - Coat
      - Points to Polygons
      - Snake
      - Spikes
      - Toothpaste
      - Tubes/Muscle
      - Cloth
      - Surface Array
      """
      coat.tools_item("[extension]SCULP_PRIM") # Primitives
      coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MERGE") # Import
      coat.tools_item("[extension]TreesGenerator") # Tree generator
      coat.tools_item("[extension]lasPointCloud") # LAS Point Cloud
      coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_LOGO") # Logo
      coat.tools_item("[extension]PixelArt") # Constructor
      coat.tools_item("[extension]SCULP_SKETCH") # Sketch
      coat.tools_item("[extension]SCULPT_RECTSPLIT") # Split
      coat.tools_item("[extension]SCULPT_CLONE") # Clone
      coat.tools_item("[extension]SCULPT_CUTNCLONE") # Cut & Clone
      coat.tools_item("[extension]VoxExtrude") # Vox Extrude
      coat.tools_item("[extension]VoxLayer") # Vox Layer
      coat.tools_item("[extension]CurvesLayer") # Coat
      coat.tools_item("[RetopoTool]TopToolAddPoints") # Points to Polygons
      coat.tools_item("[extension]SCULP_SPSTROKE") # Snake
      coat.tools_item("[extension]SCULP_FREESP") # Spikes
      coat.tools_item("[extension]SCULP_TUBE") # Toothpaste
      coat.tools_item("[extension]SCULP_MUSCLE") # Tubes/Muscle
      coat.tools_item("[extension]SCULP_CLOTH") # Cloth
      coat.tools_item("[extension]MultiObject") # Surface Array


@d_tools_section("Curves")
def Curves():
      """
      Curve creation tools.

      Tools in this section:
      - Curves
      - Text
      """
      coat.tools_item("[extension]SCULP_CURVES") # Curves
      coat.tools_item("[extension]SCULP_TEXT") # Text		
      InstallCurvesExtensions()

@d_tools_section("Commands")
def Commands():
      """
      Global commands for resolution, clearing, and smoothing.

      Tools in this section:
      - Res+
      - Resample
      - Clear
      - Smooth All
      - Edges relax
      - Up
      - Down
      """
      coat.tools_item("[VOX_SCULPT_TOOL]IncRes") # Res+
      coat.tools_item("[VOX_SCULPT_TOOL]Resample") # Resample
      coat.tools_item("[VOX_SCULPT_TOOL]Clear") # Clear
      coat.tools_item("[VOX_SCULPT_TOOL]SmAll") # Smooth All
      # tools_item("[extension]StemTool");Stem Cell Checker
      if coat.is_surface(): 
         coat.tools_item("[VOX_SCULPT_TOOL]SmEdges") # Edges relax
         coat.tools_item("[VOX_SCULPT_TOOL]LevelUP") # Up
         coat.tools_item("[VOX_SCULPT_TOOL]LevelDN") # Down


@d_tools_section("Commands")
def ProxyCommands():
      """
      Commands available specifically in Proxy mode.

      Tools in this section:
      - Smooth All
      - Up
      - Down
      """
      coat.tools_item("[VOX_SCULPT_TOOL]SmAll") # Smooth All
      if coat.is_multires():
         coat.tools_item("[VOX_SCULPT_TOOL]LevelUP") # Up
         coat.tools_item("[VOX_SCULPT_TOOL]LevelDN") # Down


############################
#### ProxyTools
@d_template
def ProxyTools():
      """
      Template for the Proxy (Multiresolution) mode toolset.

      Includes:
      - BaseSurfaceTools
      - AdjustProxy
      - ProxyCommands
      - ProxyToolsPaint (if enabled)
      """
      coat.page_suffix("[P]")
      coat.default_tool("[extension]SCULP_SCLAY")
      SetType(True, False)
      ProxyTools.IncludeContent()

ProxyTools.Content.append(BaseSurfaceTools)
ProxyTools.Content.append(AdjustProxy)
ProxyTools.Content.append(ProxyCommands) 

@d_child(ProxyTools)
def ProxyToolsPaint():
      """
      Adds paint tools to Proxy mode if multiresolution is active.

      Includes:
      - PaintTools
      """
      if coat.is_multires():
            PaintTools()


############################
#### SurfaceTools
@d_template
def SurfaceTools():
      """
      Template for the Surface mode toolset.

      Includes:
      - BaseSurfaceTools
      - Custom
      - Layers
      - PaintTools
      - AdjustSurface
      - Pose
      - SurfaceObjects
      - Curves
      - Commands
      """
      coat.page_suffix("[S]")
      coat.default_tool("[extension]SCULP_SCLAY")
      SetType(False, False)
      SurfaceTools.IncludeContent()

SurfaceTools.Content.append(BaseSurfaceTools)
SurfaceTools.Content.append(Custom)
SurfaceTools.Content.append(Layers)   
SurfaceTools.Content.append(PaintTools)
SurfaceTools.Content.append(AdjustSurface)
SurfaceTools.Content.append(Pose)
SurfaceTools.Content.append(SurfaceObjects)
SurfaceTools.Content.append(Curves)
SurfaceTools.Content.append(Commands)

############################
#### VoxelTools
@d_template
def VoxelTools():
      """
      Template for the Voxel mode toolset.

      Includes:
      - ClayEngine
      - Voxel
      - BaseSurfaceTools
      - AdjustVoxel
      - PaintTools
      - Pose
      - Objects
      - Curves
      - Commands
      """
      coat.page_suffix("[V]")
      coat.default_tool("[extension]BaseVoxBrush")
      SetType(False, True)
      VoxelTools.IncludeContent()
      
VoxelTools.Content.append(ClayEngine)
VoxelTools.Content.append(Voxel)
VoxelTools.Content.append(BaseSurfaceTools)
VoxelTools.Content.append(AdjustVoxel)
VoxelTools.Content.append(PaintTools)
VoxelTools.Content.append(Pose)
VoxelTools.Content.append(Objects)
VoxelTools.Content.append(Curves)
VoxelTools.Content.append(Commands)

###############################

@d_template
def SculptTools():
   """
   Main entry point for the Sculpt Room toolset. 
   Determines which toolset (Proxy, Surface, or Voxel) to load based on the current object state.
   """
   if(coat.is_proxy()):
      ProxyTools()   
   elif coat.is_surface():
      SurfaceTools()
   else:
      VoxelTools()
      
   coat.insert_extensions()