import coat
from cTemplates.Structs import *
from cTemplates.Rooms import reg_toolset

@reg_toolset
def FacturesTools():
    coat.page_suffix("[S]")
    coat.PureIconic()
    coat.tools_item("[extension]PaintFacture") # /Paint
    coat.tools_item("[extension]EraseFacture") # /Erase
    coat.tools_item("[extension]FillFacture") # /Fill
    coat.tools_item("[extension]RoadsTool")
    coat.tools_item("[extension]FactureSpot")

@d_tools_section("Adjust", FacturesTools)
def Adjust():
    coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSFORM") # Transform
    coat.tools_item("[VOX_SCULPT_TOOL]SCULPT_TRANSPOSE") # Pose
    coat.tools_item("[extension]SCULP_BEND") # Bend
    coat.tools_item("[VOX_SCULPT_TOOL]SCULP_MOVE") # Move
    coat.tools_item("[VOX_SCULPT_TOOL]SCULP_SFREEZE") # Freeze
    coat.tools_item("[VOX_SCULPT_TOOL]SurfHide") # Surface Hide                
    coat.tools_item("[VOX_SCULPT_TOOL]IncRes") # Res+
    coat.default_tool("[extension]PaintFacture")

