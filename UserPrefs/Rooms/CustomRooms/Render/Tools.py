
import coat
from cTemplates.Structs import *
from cTemplates.Rooms import reg_toolset

@reg_toolset
def RenderTools():
	coat.tools_item("[RenderTool]RenderTool")
	coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSFORM")
	coat.default_tool("[RenderTool]RenderTool")

