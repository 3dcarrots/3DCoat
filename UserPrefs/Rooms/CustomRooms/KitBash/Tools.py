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
import cTemplates.sculptTools as O_SculptTools
from cTemplates.Rooms import reg_toolset

@reg_toolset
def KitBashTools():
    coat.default_tool("[extension]SCULP_PRIM")
    coat.insert_extensions()


def BaseSurfaceTools(proxy, vox):
   coat.tools_section("Clay/Draw")
   coat.tools_item("{FLT}[extension]SCULP_PLANE") # Flatten
   coat.tools_item("{FLT}[extension]SCULP_PLANE2") # Chisel
   coat.tools_item("[extension]SCULP_SFEXTRUDE0") # Extrude
   coat.tools_item("[extension]PickVDM")
   coat.tools_item("{PINCH}[extension]RoofPinch")
   coat.tools_item("{PINCH}[extension]SmartPinch")
   coat.tools_item("[extension]SCULP_FOLLOW")
   if(not proxy):
       coat.tools_item("[extension]SnakeClay") # Snake Clay
 


@d_child(KitBashTools)
def SculptTools():
   if(coat.is_proxy()):
       coat.page_suffix("[P]")
       BaseSurfaceTools(True, False)
       ProxyTools()
 
   elif(coat.is_surface()):
       coat.page_suffix("[S]")
       BaseSurfaceTools(False, False)
       SurfaceTools()
   else:
       coat.page_suffix("[V]")
       VoxelTools()

###########################################
#### Surface Tools

ProxyTools = cTemplate()

@d_tools_section("Adjust", ProxyTools)
def ProxyAdjust():
       coat.tools_item("[extension]Noise") # Noise
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_PICK") # Quick Pick
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
       coat.tools_item("[extension]Measure")
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
       coat.tools_item("[extension]SCULPT_AXIAL") # Axial

###########################################
#### Surface Tools

SurfaceTools = cTemplate()

@d_tools_section("Adjust", SurfaceTools)
def VoxelAdjust():
       coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
       coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move                
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
       coat.tools_item("[extension]CutOff") # Cut Off
       coat.tools_item("[extension]Noise") # Noise
       coat.tools_item("[extension]Measure") # Measure
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_PICK") # Quick Pick
       coat.tools_item("[extension]SCULPT_AXIAL") # Axial

@d_tools_section("Objects", SurfaceTools)
def VoxelObjects():
       coat.tools_item("[extension]SCULP_PRIM") # Primitives
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MERGE") # Import
       coat.tools_item("[extension]SCULPT_RECTSPLIT") # Split
       coat.tools_item("{clone}[extension]SCULPT_CLONE") # Clone
       coat.tools_item("{clone}[extension]SCULPT_CUTNCLONE") # Cut & Clone
       coat.tools_item("{snake}[extension]SCULP_SPSTROKE") # Snake
       coat.tools_item("{snake}[extension]SCULP_CLOTH") # Cloth
       coat.tools_item("[extension]JointsTool")

SurfaceTools.Content.append(O_SculptTools.Curves)

###########################################
#### Voxel Tools

VoxelTools = cTemplate()

@d_tools_section("VoxelTools", VoxelTools)
def VoxelTools():
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_CARVE") # Carve
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_SPHERE") # Sphere
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_BRANCH") # 2D-Paint
       BaseSurfaceTools(False, True)

@d_tools_section("Adjust", VoxelTools)
def VoxelAdjust():
       coat.tools_item("[extension]CutOff") # Cut Off
       coat.tools_item("[extension]Measure") # Measure
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_PICK") # Quick Pick
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
       coat.tools_item("[extension]SCULPT_AXIAL") # Axial
@d_tools_section("Objects", VoxelTools)
def VoxelObjects():
       coat.tools_item("[extension]SCULP_PRIM") # Primitives
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MERGE") # Import
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_LOGO") # Logo
       coat.tools_item("[extension]PixelArt") # Constructor
       coat.tools_item("[extension]SCULP_SKETCH") # Sketch
       coat.tools_item("[extension]SCULPT_RECTSPLIT") # Split
       coat.tools_item("[extension]SCULPT_CLONE") # Clone
       coat.tools_item("[extension]SCULPT_CUTNCLONE") # Cut & Clone
       coat.tools_item("[extension]SCULP_SPSTROKE") # Snake
       coat.tools_item("[extension]SCULP_CLOTH") # Cloth

VoxelTools.Content.append(O_SculptTools.Curves)
 




@d_tools_section("PolySupports", KitBashTools)
def PolySupports():
    coat.tools_section("PolySupports")
    coat.tools_item("[RetopoTool]TopToolAddPoints") # Points/Faces
    coat.tools_item("[RetopoTool]TopToolSelectAndOperate") # Select
    coat.tools_item("[RetopoTool]sfShell") # Shell
    coat.tools_item("[extension]RTP_PRIM") # Primitives
    coat.tools_item("[RetopoTool]TopToolDeletePolygones") # Del. Polygons
    coat.tools_item("[RetopoTool]rtClearPoints") # Clear points
    coat.tools_item("[RetopoTool]sfTransform") # Transform

