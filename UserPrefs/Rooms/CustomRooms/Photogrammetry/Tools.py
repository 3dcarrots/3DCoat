
import coat
from cTemplates.Structs import *
from cTemplates.sculptTools import *
from cTemplates.Rooms import reg_toolset

@reg_toolset
def pgTools():
    coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
    coat.tools_item("[extension]PhotogrammetryTool") # Photogrammetry
    coat.tools_item("[extension]PclTool") # Point cloud
    coat.tools_item("[extension]MidasTool") # midas tool

pgTools.Content.append(SculptTools)

@d_child
def insert_extensions():
    coat.insert_extensions()

