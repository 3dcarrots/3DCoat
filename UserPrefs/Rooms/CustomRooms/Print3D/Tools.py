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
from cTemplates.sculptTools import *
from cTemplates.sculptTools import SetType
from cTemplates.Rooms import reg_toolset

@reg_toolset
def RegisterVoxels():
   if(coat.is_proxy()):
       PrintProxyTools()
   elif(coat.is_surface()):
       PrintSurfaceTools()
   else:
       PrintVoxelTools()
 
   coat.insert_extensions()



@d_tools_section("3DPrintBase")
def PrintBase3D():
       coat.tools_section("3DPrintBase")
       coat.tools_item("[extension]SCULP_PRIM") # Primitives
       coat.tools_item("{CURV}[extension]SCULP_CURVES") # Curves
       coat.tools_item("{CURV}[extension]SCULP_TEXT") # Text
       coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
       coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
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

@d_tools_section("3DPrintBase")
def V_PrintBase3D():
       coat.tools_item("[extension]SCULP_PRIM") # Primitives
       coat.tools_item("[extension]Blob") # Blob
       coat.tools_item("{CURV}[extension]SCULP_CURVES") # Curves
       coat.tools_item("{CURV}[extension]SCULP_TEXT") # Text
       coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
       coat.tools_item("{transform}[VOX_SCULPT_TOOL]SCULP_INST") # Instancer
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
       coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
       coat.tools_item("[extension]CutOff") # Cut Off
       coat.tools_item("[extension]Measure") # Measure
       coat.tools_item("[extension]Supports") # Supports
       coat.tools_item("{BEND}[extension]SCULP_BEND") # Bend
       coat.tools_item("{BEND}[extension]SCULP_TWIST") # Twist
       coat.tools_item("{BEND}[extension]SCULP_WRAP") # Warp
       coat.tools_item("{BEND}[extension]SCULPT_AXIAL") # Axial
       coat.tools_item("{BASRELIEF}[extension]SCULPT_BARELIEF") # Bas-Relief
       coat.tools_item("{BASRELIEF}[extension]Undercuts") # Undercuts
       coat.tools_item("[extension]VoXRay") # VoXRay

@d_tools_section("Objects")
def V_PrintObjects():
       coat.tools_section("Objects")
       coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MERGE") # Import
       coat.tools_item("{CREATESIMP}[VOX_SCULPT_TOOL]SCULPT_LOGO") # Logo
       coat.tools_item("{CREATESIMP}[extension]PixelArt") # Constructor
       coat.tools_item("{CREATESIMP}[extension]SCULP_SKETCH") # Sketch
       coat.tools_item("[extension]SCULPT_RECTSPLIT") # Split
       coat.tools_item("[extension]SCULPT_CLONE") # Clone
       coat.tools_item("[extension]SCULPT_CUTNCLONE") # Cut & Clone
       coat.tools_item("[extension]VoxExtrude") # Vox Extrude
       coat.tools_item("[extension]VoxLayer") # Vox Layer
       coat.tools_item("[extension]CurvesLayer") # Coat
       coat.tools_item("{SNAKES}[extension]SCULP_SPSTROKE") # Snake
       coat.tools_item("{SNAKES}[extension]SCULP_FREESP") # Spikes
       coat.tools_item("{SNAKES}[extension]SCULP_TUBE") # ToothPaste
       coat.tools_item("{SNAKES}[extension]SCULP_MUSCLE") # Muscle
       coat.tools_item("[extension]SCULP_CLOTH") # Cloth




############################
#### ProxyTools
@d_template
def PrintProxyTools():
      coat.page_suffix("[P]")
      coat.default_tool("[extension]SCULP_SCLAY")
      SetType(True, False)
      PrintProxyTools.IncludeContent()

PrintProxyTools.Content.append(BaseSurfaceTools)
PrintProxyTools.Content.append(AdjustProxy)
PrintProxyTools.Content.append(ProxyCommands) 

############################
#### SurfaceTools
@d_template
def PrintSurfaceTools():
       coat.page_suffix("[S]")
       coat.default_tool("[VOX_SCULPT_TOOL]SCULP_PRIM")
       SetType(False, False)
       PrintSurfaceTools.IncludeContent()

PrintSurfaceTools.Content.append(PrintBase3D)
PrintSurfaceTools.Content.append(SurfaceObjects)
PrintSurfaceTools.Content.append(BaseSurfaceTools)
PrintSurfaceTools.Content.append(Layers)
PrintSurfaceTools.Content.append(Custom)
PrintSurfaceTools.Content.append(AdjustSurface)
PrintSurfaceTools.Content.append(Curves)
PrintSurfaceTools.Content.append(Commands) 

############################
#### VoxelTools
@d_template
def PrintVoxelTools():
      coat.page_suffix("[V]")
      coat.default_tool("[extension]SCULP_PRIM")
      SetType(False, True)
      PrintVoxelTools.IncludeContent()
      
PrintVoxelTools.Content.append(V_PrintBase3D)
PrintVoxelTools.Content.append(V_PrintObjects)
PrintVoxelTools.Content.append(ClayEngine)
PrintVoxelTools.Content.append(VoxelTools)
PrintVoxelTools.Content.append(BaseSurfaceTools)
PrintVoxelTools.Content.append(AdjustVoxel)
PrintVoxelTools.Content.append(Curves)       
PrintVoxelTools.Content.append(Commands)

###############################