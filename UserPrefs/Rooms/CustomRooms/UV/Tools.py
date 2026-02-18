# 
# The UV room toolset definition.
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
from cTemplates.Rooms import reg_toolset

@reg_toolset
def UV_Toolset(): pass

@d_tools_section("UV-Modes", UV_Toolset)
def UVModes():
   coat.tools_item("[uv_mapper_tool]MARK_CLUSTERS") # Add Clusters
   coat.tools_item("[uv_mapper_tool]MARK_EDGES") # Mark Seams
   coat.tools_item("[uv_mapper_tool]MARK_LOOPS") # Edge Loops
   coat.tools_item("[uv_mapper_tool]UV_Path") # UV Path
   coat.tools_item("[extension]JoinUVCL")

@d_tools_section("Selected", UV_Toolset)
def selected_uv():
       if coat.GetCurrentToolSubmode("uv") == 1: # verts
              coat.tools_item("[uv_mapper_tool]ClearSel") # Clear
              coat.tools_item("[uv_mapper_tool]uvInvSel") # Invert
              coat.tools_item("[uv_mapper_tool]RotateCW") # Rotate CW
              coat.tools_item("[uv_mapper_tool]RotateCCW") # Rotate CCW
              coat.tools_item("[uv_mapper_tool]FlipU") # Flip U
              coat.tools_item("[uv_mapper_tool]FlipV") # Flip V
              coat.tools_item("[uv_mapper_tool]uvRelax") # Relax
              coat.tools_item("[uv_mapper_tool]Relax2") # Cloth Relax
       elif coat.GetCurrentToolSubmode("uv") == 2: # edges
              coat.tools_item("[uv_mapper_tool]ClearSel") # Clear
              coat.tools_item("[uv_mapper_tool]uvInvSel") # Invert
              coat.tools_item("[uv_mapper_tool]RotateCW") # Rotate CW
              coat.tools_item("[uv_mapper_tool]RotateCCW") # Rotate CCW
              coat.tools_item("[uv_mapper_tool]FlipU") # Flip U
              coat.tools_item("[uv_mapper_tool]FlipV") # Flip V
              coat.tools_item("[uv_mapper_tool]uvToLine") # To Line
              coat.tools_item("[uv_mapper_tool]uvEquidist") # Equidistant
              coat.tools_item("[uv_mapper_tool]uvHorizontal") # Horizontal
              coat.tools_item("[uv_mapper_tool]uvVertical") # Vertical
              coat.tools_item("[uv_mapper_tool]uvLoop") # Edge Loop
              coat.tools_item("[uv_mapper_tool]uvRing") # Edge Ring
              coat.tools_item("[uv_mapper_tool]uvSeams") # Set Seams
              coat.tools_item("[uv_mapper_tool]uvClrSeams") # Del. Seams
       elif coat.GetCurrentToolSubmode("uv") == 3: # faces
              coat.tools_item("[uv_mapper_tool]ClearSel") # Clear
              coat.tools_item("[uv_mapper_tool]uvInvSel") # Invert
              coat.tools_item("[uv_mapper_tool]RotateCW") # Rotate CW
              coat.tools_item("[uv_mapper_tool]RotateCCW") # Rotate CCW
              coat.tools_item("[uv_mapper_tool]FlipU") # Flip U
              coat.tools_item("[uv_mapper_tool]FlipV") # Flip V
              coat.tools_item("[uv_mapper_tool]Strict") # Relax
              coat.tools_item("[uv_mapper_tool]Relax2") # Cloth Relax
              coat.tools_item("[uv_mapper_tool]uvHide") # Hide
              coat.tools_item("[uv_mapper_tool]uvInvHide") # Inv. Hidden
              coat.tools_item("[uv_mapper_tool]uvUnhide") # Unhide
              coat.tools_item("[uv_mapper_tool]uvUnhideAll") # Unhide All
              coat.tools_item("[uv_mapper_tool]hdExpand") # HD Expand
              coat.tools_item("[uv_mapper_tool]hdContract") # HD Contract
       elif coat.GetCurrentToolSubmode("uv") == 4: # islands
              coat.tools_item("[uv_mapper_tool]ClearSel") # Clear
              coat.tools_item("[uv_mapper_tool]uvInvSel") # Invert
              coat.tools_item("[uv_mapper_tool]RotateCW") # Rotate CW
              coat.tools_item("[uv_mapper_tool]RotateCCW") # Rotate CCW
              coat.tools_item("[uv_mapper_tool]FlipU") # Flip U
              coat.tools_item("[uv_mapper_tool]FlipV") # Flip V
              coat.tools_item("[uv_mapper_tool]Strict") # Relax
              coat.tools_item("[uv_mapper_tool]Relax2") # Cloth Relax
              coat.tools_item("[uv_mapper_tool]toABF") # To ABF
              coat.tools_item("[uv_mapper_tool]toGU") # To GU
              coat.tools_item("[uv_mapper_tool]toLSCM") # To LSCM
              coat.tools_item("[uv_mapper_tool]toPlanar") # To Planar
              coat.tools_item("[uv_mapper_tool]toStripe")
              coat.tools_item("[uv_mapper_tool]uvHide") # Hide
              coat.tools_item("[uv_mapper_tool]uvInvHide") # Inv. Hidden
              coat.tools_item("[uv_mapper_tool]uvUnhide") # Unhide
              coat.tools_item("[uv_mapper_tool]uvUnhideAll") # Unhide All
              coat.tools_item("[uv_mapper_tool]hdExpand") # HD Expand
              coat.tools_item("[uv_mapper_tool]hdContract") # HD Contract
              coat.tools_item("[uv_mapper_tool]CopyUV") # Copy UV
              coat.tools_item("[uv_mapper_tool]PasteUV") # Paste UV
       else:
              coat.tools_item("[uv_mapper_tool]ClearSel")
              coat.tools_item("[uv_mapper_tool]uvInvSel")


@d_tools_section("Commands", UV_Toolset)
def Commands():
   coat.tools_item("[uv_mapper_tool]UV_Settings") # UV Settings
   coat.tools_item("[uv_mapper_tool]ClearClusters") # Clear Clusters
   coat.tools_item("[uv_mapper_tool]ClearEdges") # Clear Seams
   coat.tools_item("[uv_mapper_tool]AutoEdges") # Auto Seams
   coat.tools_item("[uv_mapper_tool]SharpSeams") # Sharp Seams
   coat.tools_item("[uv_mapper_tool]UnifyUV") # Unify UV
   coat.tools_item("[uv_mapper_tool]Unwrap") # Unwrap
   coat.tools_item("[uv_mapper_tool]AutoMap") # AutoMap
   coat.tools_item("[uv_mapper_tool]PackUV") # Pack UV
   coat.tools_item("[uv_mapper_tool]ShuffleUV") # Shuffle/Pack
   coat.tools_item("[uv_mapper_tool]PackUnf") # PackUV2
   coat.tools_item("[uv_mapper_tool]AutoSc") # Auto Scale
   coat.tools_item("[uv_mapper_tool]RemoveUVIntr")
   coat.tools_item("[uv_mapper_tool]UpdateIsl") # Upd. Islands
   coat.tools_item("[uv_mapper_tool]RestoreUV") # Restore UV
   coat.tools_item("[uv_mapper_tool]ApplyUV") # Apply UV-set
   coat.tools_item("[uv_mapper_tool]STORE_UV") # Save
   coat.tools_item("[uv_mapper_tool]RESTORE_UV") # Load
   coat.tools_item("[uv_mapper_tool]rLazerCut") # Save contour
   coat.tools_item("[extension]StemTool") # Stem Cell Checker
   coat.default_tool("[uv_mapper_tool]MARK_EDGES")



