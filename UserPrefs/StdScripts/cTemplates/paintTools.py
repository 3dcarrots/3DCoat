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
from cTemplates.Structs import *

@d_template
def PaintTools():
   """
   Main toolset for the Paint room, containing standard brushes, editing tools, and topological operations.

   Tools in this section:
   - Brush
   - Pencil
   - Airbrush
   - Coloring
   - Height
   - Smudge
   - Power Smooth
   - Clone
   - Transform
   - Copy/Paste
   - Curves
   - Text
   - Picture
   - Eraser
   - Hide
   - Freeze
   - Fill
   - Selection
   - Pick
   - Flatten
   - Measure
   - Topo-Symmetry
   - Ptex res+
   """
   coat.PureIconic()
   coat.tools_section("Paint")
   coat.tools_item("[StdPen]StdPen") # Brush
   coat.tools_item("[Pencil]Pencil") # Pencil
   coat.tools_item("[Airbrush]Airbrush") # Airbrush
   coat.tools_item("[ChangeColor]ChangeColor") # Coloring
   coat.tools_item("[ChangeHeight]ChangeHeight") # Height
   coat.tools_item("[SmudgeTool]SmudgeTool") # Smudge
   coat.tools_item("[POWRELAX]POWRELAX") # Power Smooth
   coat.tools_item("[CloneTool]CloneTool") # Clone
   coat.tools_item("[RectTransformTool]RectTransformTool") # Transform
   coat.tools_item("[CopyPaste]CopyPaste") # Copy/Paste
   coat.tools_item("[CurveTool]CurveTool") # Curves
   coat.tools_item("[TextTool]TextTool") # Text
   coat.tools_item("[PictTool]PictTool") # Picture
   coat.tools_item("[EraserTool]EraserTool") # Eraser
   coat.tools_item("[CutFace]CutFace") # Hide
   coat.tools_item("[FreezeTool]FreezeTool") # Freeze
   coat.tools_item("[FillTool]FillTool") # Fill
   coat.tools_item("[MagicWand]MagicWand") # Selection
   coat.tools_item("[PickTool]PickTool") # Pick
   coat.tools_item("[PlaneTool]PlaneTool") # Flatten
   coat.tools_item("[MeasureTool]MeasureTool") # Measure
   coat.tools_item("[TopoSymmTool]TopoSymmTool") # Topo-Symmetry
   if(coat.is_ptex()): coat.tools_item("PTEX_RES") # Ptex res+
   coat.default_tool("[StdPen]StdPen")
   PaintTools.IncludeContent()

@d_tools_section("Tweak/Sculpt", PaintTools)
def TweakSculpt():
   """
   Sculpting and Tweak tools available within the Paint room context for mesh deformation.

   Tools in this section:
   - Move
   - Select/Transform
   - Draw
   - Collapse
   - Expand
   - Shift
   - Smudge
   - Flatten
   - Smooth
   """
   coat.tools_item("[SculptTool]{1}SCULPT_DRAG") # Move
   coat.tools_item("[SculptTool]{1}SCULPT_SELTRANSFORM") # Select/Transform
   coat.tools_item("[SculptTool]{1}SCULPT_DRAW") # Draw
   coat.tools_item("[SculptTool]{1}SCULP_COLLAPSE") # Collapse
   coat.tools_item("[SculptTool]{1}SCULP_EXPAND") # Expand
   coat.tools_item("[SculptTool]{1}SCULP_FOLLOW") # Shift
   coat.tools_item("[SculptTool]{1}SCULP_FOLLOW_TANGENT") # Smudge
   coat.tools_item("[SculptTool]{1}SCULP_PLANE") # Flatten
   coat.tools_item("[SculptTool]{1}SCULP_SMOOTH") # Smooth
   coat.default_tool("[SculptTool]{1}SCULPT_DRAW")