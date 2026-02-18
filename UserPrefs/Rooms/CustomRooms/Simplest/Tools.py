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
#  def RegisterVoxels():

import coat
from cTemplates.Structs import *
from cTemplates.Rooms import reg_toolset

proxy = cTemplate()
surface = cTemplate()
voxels = cTemplate()

@reg_toolset
def SimplestToolset():
       if coat.is_proxy():
              coat.page_suffix("[P]")
              coat.default_tool("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE")
              proxy()
       elif coat.is_surface():
              coat.page_suffix("[S]")
              coat.default_tool("[extension]SCULP_PRIM")
              surface()
       else:
              coat.page_suffix("[V]")
              coat.default_tool("[extension]SCULP_PRIM")
              voxels()




@d_tools_section("Adjust", proxy)
def P_Adjust():
              coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
              coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move

@d_tools_section("Measure", proxy)
def P_Measure():
              coat.tools_item("[extension]Measure") # Measure
              coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
              coat.tools_item("[extension]SCULPT_AXIAL") # Axial

@d_tools_section("Commands", proxy)
def P_Commands():
              coat.tools_item("[VOX_SCULPT_TOOL]SmAll") # Smooth All
       
@d_tools_section("3DPrintBase", surface)
def S_3DPrintBase():
              coat.tools_item("[extension]SCULP_PRIM") # Primitives
              coat.tools_item("{CURV}[extension]SCULP_CURVES") # Curves
              coat.tools_item("{CURV}[extension]SCULP_TEXT") # Text
              coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
              coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
              coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
              coat.tools_item("[extension]CutOff") # Cut Off
              coat.tools_item("[extension]Measure") # Measure
              coat.tools_item("[extension]Supports") # Supports
              coat.tools_item("{BEND}[extension]SCULP_BEND") # Bend
              coat.tools_item("{BEND}[extension]SCULP_TWIST") # Twist
              coat.tools_item("{BEND}[extension]SCULP_WRAP") # Warp
              coat.tools_item("{BEND}[extension]SCULPT_AXIAL") # Axial
              coat.tools_item("{BASRELIEF}[extension]SCULPT_BARELIEF") # Bas-Relief
              coat.tools_item("{BASRELIEF}[extension]Undercuts") # Undercuts
              coat.tools_item("[extension]Molding")
              coat.tools_item("[extension]VoXRay") # VoXRay
              coat.tools_item("[extension]Noise") # Noise

@d_tools_section("Objects", surface)
def S_Objects():
              coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MERGE") # Import
              coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_LOGO") # Logo
              coat.tools_item("{Snake}[extension]SCULP_SPSTROKE") # Snake
              coat.tools_item("{Snake}[extension]SCULP_FREESP") # Spikes
              coat.tools_item("{Snake}[extension]SCULP_MUSCLE") # Muscle

@d_tools_section("Commands", surface)
def S_Commands():
              coat.tools_item("[VOX_SCULPT_TOOL]IncRes") # Res+
              coat.tools_item("[VOX_SCULPT_TOOL]Resample") # Resample
              coat.tools_item("[VOX_SCULPT_TOOL]Clear") # Clear
              coat.tools_item("[VOX_SCULPT_TOOL]SmAll") # Smooth All

@d_tools_section("Curves", surface)
def S_Curves():
              coat.tools_item("[extension]CurvesLayer") # Coat
              coat.tools_item("[extension]TubeOnCurve") # Tube/Array
              coat.tools_item("[extension]BendVolume") # Bend Volume
              coat.tools_item("[extension]SweptSurface") # Swep along Guide
              coat.tools_item("[extension]RotateSurface") # Rotate Surface
              coat.tools_item("[extension]SurfacePrism") # Polyhedron
              coat.tools_item("[extension]SurfaceSwept2") # Swept 2 Guide
              coat.tools_item("[extension]SurfaceSwept2Gener") # Swept 2 Gener
              coat.tools_item("[extension]SurfaceSweptNGener") # Swept N Gener
       
@d_tools_section("3DPrintBase", voxels)
def V_3DPrintBase():
              coat.tools_item("[extension]SCULP_PRIM") # Primitives
              coat.tools_item("[extension]Blob") # Blob
              coat.tools_item("{CURV}[extension]SCULP_CURVES") # Curves
              coat.tools_item("{CURV}[extension]SCULP_TEXT") # Text
              coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
              coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
              coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
              coat.tools_item("[extension]CutOff") # Cut Off
              coat.tools_item("[extension]Measure") # Measure
              coat.tools_item("[extension]Supports") # Supports
              coat.tools_item("{BEND}[extension]SCULP_BEND") # Bend
              coat.tools_item("{BEND}[extension]SCULP_TWIST") # Twist
              coat.tools_item("{BEND}[extension]SCULP_WRAP") # Warp
              coat.tools_item("{BEND}[extension]SCULPT_AXIAL") # Axial
              coat.tools_item("{BASRELIEF}[extension]SCULPT_BARELIEF") # Bas-Relief
              coat.tools_item("{BASRELIEF}[extension]Undercuts") # Undercuts
              coat.tools_item("[extension]Molding")
              coat.tools_item("[extension]VoXRay") # VoXRay

@d_tools_section("Objects", voxels)
def V_Objects():
              coat.tools_section("Objects")
              coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MERGE") # Import
              coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_LOGO") # Logo
              coat.tools_item("[extension]PixelArt") # Constructor
              coat.tools_item("[extension]SCULP_SKETCH") # Sketch
              coat.tools_item("[extension]SCULP_SPSTROKE") # Snake
              coat.tools_item("[extension]SCULP_FREESP") # Spikes
              coat.tools_item("[extension]SCULP_MUSCLE") # Muscle
              coat.tools_item("[extension]SCULP_CLOTH") # Cloth		

@d_tools_section("Commands", voxels)
def V_Commands():
              coat.tools_section("Commands")
              coat.tools_item("[VOX_SCULPT_TOOL]IncRes") # Res+
              coat.tools_item("[VOX_SCULPT_TOOL]Resample") # Resample
              coat.tools_item("[VOX_SCULPT_TOOL]Clear") # Clear
              coat.tools_item("[VOX_SCULPT_TOOL]SmAll") # Smooth All
       



