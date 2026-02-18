# 
# The Paint room toolset definition.
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
from cTemplates.paintTools import PaintTools
from cTemplates.Rooms import reg_toolset

@reg_toolset
def RegisterPaint():
    PaintTools()
