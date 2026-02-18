# 
# The Modeling room toolset definition.
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
import coat
from cTemplates.Structs import *
from cTemplates.retopoTools import *
from cTemplates.Rooms import reg_toolset

@reg_toolset
def ModelingTools():
   coat.tools_comment("TheModelingRoom")

ModelingTools.Content.append(Basic)


@d_child(ModelingTools)
def Modeling():
   coat.tools_item("{SWEPTSURF}[extension]MdlSurfaceSwept") # Surface Swept
   coat.tools_item("{SWEPTSURF}[extension]MdlProfileSurface") # Profile Surface
   coat.tools_item("{SWEPTSURF}[extension]MdlSurfaceSweptStrip") # Surface Swept Strip
   coat.tools_item("{SWEPTSURF}[extension]MdlSurfaceSwept2") # Surface Swept2
   coat.tools_item("{SWEPTSURF}[extension]MdlSurfaceNGenerTwoGuide") # Surface NGener TwoGuide
   coat.tools_item("{ROTATESRF}[extension]MdlSurfaceRotate") # Surface Rotate
   coat.tools_item("{ROTATESRF}[extension]MdlSurfacePrism") # Surface Prism
   coat.tools_item("{CONICSRF}[extension]MdlShapeSurface") # ShapeSurface
   coat.tools_item("{CONICSRF}[extension]MdlCinematicSurface") # Cinematic Surface
   coat.tools_item("[extension]MdlSurfaceLofte") # Surface Lofte
   coat.tools_item("[extension]MdlSurfacePatch") # Surface Patch
   # 	tools_item("[extension]Bevel"); Bevel
   coat.tools_item("[extension]ArrayCopyTool") # Array Copy
   coat.tools_item("[extension]GridTool") # Array Copy


ModelingTools.Content.append(Tweak)
ModelingTools.Content.append(SmartHybrid)
ModelingTools.Content.append(UV)
 
