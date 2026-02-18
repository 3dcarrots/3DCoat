# 
# The Retopo room toolset definition.
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
def RetopoTools():
   """
   Initializes the Retopo room toolset, setting the tool comment and including content.
   """
   coat.tools_comment("TheRetopoRoom") # The Retopo room is intended to perform the retopology over the existing mesh. It is very similar to the Modeling room but the snapping to the surface is turned on by default.
   RetopoTools.IncludeContent()

@d_tools_section("Basic", RetopoTools)
def Basic():
   """
   Basic set of retopology tools for creating and modifying geometry.

   Tools in this section:
   - Add/Split
   - Select
   - Select/Transform
   - Select Path
   - Quads
   - Points to Polygons
   - Cap
   - Strokes
   - Curves/Strokes
   - 3D Primitives
   - 2D Primitives
   - R-Fill
   - Knife
   - Smart Retopo
   - Smart Extrude
   - Inset
   - Spine Tool
   - Free Moving
   - Free Rotating
   - Free Scaling
   - Make Joints
   """
   coat.default_tool("[RetopoTool]TopToolAddPolygones")
   coat.tools_item("[RetopoTool]TopToolAddPolygones") # Add/Split
   coat.tools_item("[RetopoTool]TopToolSelectAndOperate") # Select
   coat.tools_item("[RetopoTool]TopToolSelTransform") # Select/Transform
   coat.tools_item("[RetopoTool]SelPath") # Select Path
   coat.tools_item("[RetopoTool]TopToolAddQuads") # Quads
   coat.tools_item("[RetopoTool]TopToolAddPoints") # Points to Polygons
   coat.tools_item("[extension]CapRetopo") # Cap
   coat.tools_item("[RetopoTool]TopToolDrawStrokes") # Strokes
   coat.tools_item("[extension]CurveAsStroke") # Curves/Strokes
   coat.tools_item("[extension]RTP_PRIM") # 3D Primitives
   coat.tools_item("[extension]RTP_PRIM2") # 2D Primitives
   coat.tools_item("[extension]RFill") # R-Fill
   coat.tools_item("[extension]RtKnife") # Knife
   coat.tools_item("[extension]SmartRetopo") # Smart Retopo
   coat.tools_item("{EXTRD}[extension]RtExtrudeFreeSl") # Smart Extrude
   coat.tools_item("{EXTRD}[extension]InSet") # Inset
   coat.tools_item("{EXTRD}[extension]SpineTool") # Spine Tool
   coat.tools_item("{TRFM}[extension]RtFreeMoving") # Free Moving
   coat.tools_item("{TRFM}[extension]RtFreeRotating") # Free Rotating
   coat.tools_item("{TRFM}[extension]RtFreeScaling") # Free Scaling
   coat.tools_item("[extension]MakeJoints") # Make Joints

@d_tools_section("Tweak", RetopoTools)
def Tweak():
   """
   Tools for tweaking and refining the retopology mesh.

   Tools in this section:
   - Sharp Edges
   - Brush
   - Delete Face/Edge
   - Collapse
   - Split Rings
   - Move
   - Slide Edges/Vertex
   - Measure
   - Show Open Edge
   """
   coat.tools_item("[RetopoTool]TopToolSharp") # Sharp Edges
   coat.tools_item("[RetopoTool]TopToolTweakWithBrush") # Brush
   # 	tools_item("[RetopoTool]TopToolDeletePolygones");Del. Polygons
   # 	tools_item("[RetopoTool]TopToolDeleteEdges");Del. Edges
   coat.tools_item("[extension]DeleteFaceOrEdge") # Delete Face/Edge
   coat.tools_item("[RetopoTool]TopToolCollapseEdges") # Collapse
   coat.tools_item("[extension]SplitRings") # Split Rings
   coat.tools_item("[RetopoTool]TopToolTweakVerts") # Move
   coat.tools_item("[extension]SlideEdgesOrVertex") # Slide Edges/Vertex
   coat.tools_item("[extension]Measure") # Measure
   coat.tools_item("[extension]MdlShowOpenEdge") # Show Open Edge

@d_tools_section("UV", RetopoTools)
def UV():
   """
   Tools for UV mapping, marking seams, and managing clusters within the Retopo room.

   Tools in this section:
   - Add Clusters
   - Mark Seams
   - Edge Loops
   - UV Path
   - Join Clusters
   """
   coat.tools_item("[RetopoTool]MARK_CLUSTERS") # Add Clusters
   coat.tools_item("[RetopoTool]TopToolMarkSeams") # Mark Seams
   coat.tools_item("[RetopoTool]TopToolMarkEdgeLoops") # Edge Loops
   coat.tools_item("[RetopoTool]UV_Path") # UV Path
   coat.tools_item("[extension]JoinUVCL") # Join Clusters
   if coat.IsInTool("[RetopoTool]TopToolAddPoints"):
       TopToolAddPoints_Special()
 
   if coat.IsInTool("[RetopoTool]TopToolDrawStrokes"):
       TopToolDrawStrokes_Special()

 
   if coat.IsInTool("[RetopoTool]TopToolMarkSeams") or coat.IsInTool("[RetopoTool]TopToolMarkEdgeLoops") or coat.IsInTool("[extension]JoinUVCL") or coat.IsInTool("[RetopoTool]MARK_CLUSTERS") or coat.IsInTool("[RetopoTool]UV_Path") or coat.doc_mode():
       selected_uv()
       UV_Commands()
 
   selm: int = coat.GetCurrentToolSubmode("selected")
   if coat.IsInTool("[RetopoTool]TopToolSelectAndOperate") or coat.IsInTool("[RetopoTool]TopToolSelTransform") or coat.IsInTool("[RetopoTool]SelPath") or selm != 0:
       if coat.GetCurrentToolSubmode("retopo") == 2 or coat.IsInTool("[RetopoTool]SelPath") or coat.doc_mode() or selm == 2: # edges
           Selected_Edges()
     
       if coat.GetCurrentToolSubmode("retopo") == 1 or coat.doc_mode() or selm == 1: # verts
           Selected_Verts()
     
       if coat.GetCurrentToolSubmode("retopo") == 3 or coat.doc_mode() or selm == 3: # faces
           Selected_Faces()
     
       WholeMesh()
   else:
       Commands()

@d_tools_section("Special")
def TopToolDrawStrokes_Special():
       """
       Special context-sensitive tools visible when using the Strokes tool.

       Tools in this section:
       - Clear
       - Smooth
       - Delete
       """
       coat.tools_item("[RetopoTool]ClearLines") # Clear
       coat.tools_item("[RetopoTool]SmoothLines") # Smooth
       coat.tools_item("[RetopoTool]DelStroke") # Delete

@d_tools_section("Special")
def TopToolAddPoints_Special():
       """
       Special context-sensitive tools visible when using the Add Points tool.

       Tools in this section:
       - Clear Points
       """
       coat.tools_item("[RetopoTool]rtClearPoints") # Clear Points

@d_tools_section("Commands")
def UV_Commands():
       """
       Commands for UV manipulation, unwrapping, packing, and managing UV sets.

       Tools in this section:
       - UV Settings
       - Clear Clusters
       - Clear Seams
       - Auto Seams
       - Sharp Seams
       - Unify UV
       - Unwrap
       - Auto-Map
       - Pack UV
       - Shuffle/Pack
       - PackUV2
       - Auto Scale
       - Intersections
       - Upd. Islands
       - Restore UV
       - Apply UV-set
       - Save
       - Load
       - Save Contour
       - StemCell
       """
       coat.tools_item("[RetopoTool]UV_Settings") # UV Settings
       coat.tools_item("[RetopoTool]ClearClusters") # Clear Clusters
       coat.tools_item("[RetopoTool]ClearEdges") # Clear Seams
       coat.tools_item("[RetopoTool]AutoEdges") # Auto Seams
       coat.tools_item("[RetopoTool]SharpSeams") # Sharp Seams
       coat.tools_item("[RetopoTool]UnifyUV") # Unify UV
       coat.tools_item("[RetopoTool]Unwrap") # Unwrap
       coat.tools_item("[RetopoTool]AutoMap") # Auto-Map
       coat.tools_item("[RetopoTool]PackUV") # Pack UV
       coat.tools_item("[RetopoTool]ShuffleUV") # Shuffle/Pack
       coat.tools_item("[RetopoTool]PackUnf") # PackUV2
       coat.tools_item("[RetopoTool]AutoSc") # Auto Scale
       coat.tools_item("[RetopoTool]RemoveUVIntr") # Intersections
       coat.tools_item("[RetopoTool]UpdateIsl") # Upd. Islands
       coat.tools_item("[RetopoTool]RestoreUV") # Restore UV
       coat.tools_item("[RetopoTool]ApplyUV") # Apply UV-set
       coat.tools_item("[RetopoTool]STORE_UV") # Save
       coat.tools_item("[RetopoTool]RESTORE_UV") # Load
       coat.tools_item("[RetopoTool]rLazerCut") # Save Contour
       coat.tools_item("[extension]StemTool") # StemCell

@d_tools_section("Selected")
def Selected_Edges():
           """
           Operations available when Edges are selected in Retopo tools.

           Tools in this section:
           - Expand
           - Contract
           - Transform
           - Smart Extrude
           - Cut Edges
           - Snap
           - Scale
           - Relax
           - Rotate CW
           - Rotate CCW
           - Split
           - Collapse
           - Delete
           - Edge Loop
           - Edge Ring
           - Select Sharp
           - Bevel
           - Set Seams
           - Delete UV Seams
           - Mark as Sharp
           - Clear Sharp
           - Store Selection
           - Load Selection
           - Clear Selection
           - Split Edge
           - Bridge
           - Align Verts/Faces
           - Edge Flow
           - Equalize Edges
           """
           coat.tools_comment("EdgesModeComment") # The next commands are available only if the select/edges tool activated.
           coat.tools_item("[RetopoTool]sfExpand") # Expand
           coat.tools_item("[RetopoTool]sfContract") # Contract
           coat.tools_item("[RetopoTool]sfTransform") # Transform
           coat.tools_item("[extension]RtExtrudeFreeSl") # Smart Extrude
           coat.tools_item("[RetopoTool]sfCutEdges") # Cut Edges
           coat.tools_item("[RetopoTool]SnapRT") # Snap
           coat.tools_item("[RetopoTool]ScaleCL") # Scale
           coat.tools_item("[RetopoTool]ApplyTSm") # Relax
           coat.tools_item("[RetopoTool]seSpin") # Rotate CW
           coat.tools_item("[RetopoTool]seSpinBack") # Rotate CCW
           coat.tools_item("[RetopoTool]seSplit") # Split
           coat.tools_item("[RetopoTool]seCollapse") # Collapse
           coat.tools_item("[RetopoTool]seDelete") # Delete
           coat.tools_item("[RetopoTool]seEdgeLoop") # Edge Loop
           coat.tools_item("[RetopoTool]seEdgeRing") # Edge Ring
           coat.tools_item("[RetopoTool]seSelSharp") # Select Sharp
           coat.tools_item("[extension]Bevel") # Bevel
           coat.tools_item("[RetopoTool]uvSeams") # Set Seams
           coat.tools_item("[RetopoTool]uvClrSeams") # Delete UV Seams
           coat.tools_item("[RetopoTool]uvSharp") # Mark as Sharp
           coat.tools_item("[RetopoTool]uvClrSharp") # Clear Sharp
           coat.tools_item("[RetopoTool]rtStoreSel") # Store Selection
           coat.tools_item("[RetopoTool]rtRecallSel") # Load Selection
           coat.tools_item("[RetopoTool]rtClearSel") # Clear Selection
           coat.tools_item("[RetopoTool]rtSpliteEdge") # Split Edge
           coat.tools_item("[extension]MdlBridgeTool") # Bridge
           coat.tools_item("[extension]RtAlignmentVertexs") # Align Verts/Faces
           coat.tools_item("[extension]MdlEdgeFlow") # Edge Flow
           coat.tools_item("[extension]UnifArrangementVertex") # Equalize Edges


@d_tools_section("Selected")
def Selected_Verts():
           """
           Operations available when Vertices are selected in Retopo tools.

           Tools in this section:
           - Expand
           - Contract
           - Transform
           - Connect
           - Snap
           - Scale
           - Store Selection
           - Load Selection
           - Clear Selection
           - Bevel
           - Weld Vertices
           - Align Verts/Faces
           - Relax
           """
           coat.tools_comment("VertsModeComment") # The next commands are available only if the select/vertex tool activated.
           coat.tools_item("[RetopoTool]sfExpand") # Expand
           coat.tools_item("[RetopoTool]sfContract") # Contract
           coat.tools_item("[RetopoTool]sfTransform") # Transform
           coat.tools_item("[RetopoTool]sfConnect") # Connect
           coat.tools_item("[RetopoTool]SnapRT") # Snap
           coat.tools_item("[RetopoTool]ScaleCL") # Scale
           coat.tools_item("[RetopoTool]rtStoreSel") # Store Selection
           coat.tools_item("[RetopoTool]rtRecallSel") # Load Selection
           coat.tools_item("[RetopoTool]rtClearSel") # Clear Selection
           coat.tools_item("[extension]Bevel") # Bevel
           coat.tools_item("[extension]RtWeldingVertexs") # Weld Vertices
           coat.tools_item("[extension]RtAlignmentVertexs") # Align Verts/Faces
           coat.tools_item("[RetopoTool]ApplyTSm") # Relax

@d_tools_section("Selected")
def Selected_Faces():
           """
           Operations available when Faces are selected in Retopo tools.

           Tools in this section:
           - Expand
           - Contract
           - Transform
           - Smart Extrude
           - Intrude
           - Inset
           - Shell
           - Snap
           - Scale
           - Relax
           - Smooth Selection CC
           - Delete
           - Clone
           - Separate
           - Subdivide
           - Hide
           - Flip faces
           - Invert Hidden
           - Unhide
           - Poke Face
           - Bevel
           - Bridge
           - Align Verts/Faces
           - Clear Selection
           """
           coat.tools_comment("FacesModeComment") # The next commands are available only if the select/faces tool activated.
           coat.tools_item("[RetopoTool]sfExpand") # Expand
           coat.tools_item("[RetopoTool]sfContract") # Contract
           coat.tools_item("[RetopoTool]sfTransform") # Transform
           coat.tools_item("[extension]RtExtrudeFreeSl") # Smart Extrude
           coat.tools_item("[RetopoTool]sfIntrude") # Intrude
           coat.tools_item("[extension]InSet") # Inset
           coat.tools_item("[RetopoTool]sfShell") # Shell
           coat.tools_item("[RetopoTool]SnapRT") # Snap
           coat.tools_item("[RetopoTool]ScaleCL") # Scale
           coat.tools_item("[RetopoTool]ApplyTSm") # Relax
           coat.tools_item("[RetopoTool]sfSmooth") # Smooth Selection CC
           coat.tools_item("[RetopoTool]sfDelete") # Delete
           coat.tools_item("[RetopoTool]sfClone") # Clone
           coat.tools_item("[RetopoTool]sfCutnClone") # Separate
           coat.tools_item("[RetopoTool]sfSubdiv") # Subdivide
           coat.tools_item("[RetopoTool]sfHide") # Hide
           coat.tools_item("[RetopoTool]rtFlipFaces") # Flip faces
           coat.tools_item("[RetopoTool]sfInvHidden") # Invert Hidden
           coat.tools_item("[RetopoTool]sfUnhide") # Unhide
           coat.tools_item("[RetopoTool]rtPoke") # Poke Face
           coat.tools_item("[extension]Bevel") # Bevel
           coat.tools_item("[extension]MdlBridgeTool") # Bridge
           coat.tools_item("[extension]RtAlignmentVertexs") # Align Verts/Faces
           coat.tools_item("[RetopoTool]rtClearSel") # Clear Selection

@d_tools_section("WholeMesh")
def WholeMesh():
       """
       Global operations applicable to the entire retopology mesh.

       Tools in this section:
       - Transform
       - Snap
       - Scale
       - Relax
       - Import
       - Export
       - Subdivide
       - Smooth (CC)
       - Delete Mesh
       - Symmetry
       - Unwrap
       - Store Selection
       - Load Selection
       - Clear Selection
       - Save Contour
       - StemCell
       """
       coat.tools_item("[RetopoTool]sfTransform") # Transform
       coat.tools_item("[RetopoTool]SnapRT") # Snap
       coat.tools_item("[RetopoTool]ScaleCL") # Scale
       coat.tools_item("[RetopoTool]ApplyTSm") # Relax
       coat.tools_item("[RetopoTool]ImportRM") # Import
       coat.tools_item("[RetopoTool]ExportRM") # Export
       coat.tools_item("[RetopoTool]ApplyTS") # Subdivide
       coat.tools_item("[RetopoTool]ApplyTSmooth") # Smooth (CC)
       coat.tools_item("[RetopoTool]ClearTM") # Delete Mesh
       coat.tools_item("[RetopoTool]ApplyTSym") # Symmetry
       coat.tools_item("[RetopoTool]Unwrap") # Unwrap
       coat.tools_item("[RetopoTool]rtStoreSel") # Store Selection
       coat.tools_item("[RetopoTool]rtRecallSel") # Load Selection
       coat.tools_item("[RetopoTool]rtClearSel") # Clear Selection
       coat.tools_item("[RetopoTool]rLazerCut") # Save Contour
       coat.tools_item("[extension]StemTool") # StemCell	


@d_tools_section("Commands")
def Commands():
       """
       General retopology commands and mesh operations.

       Tools in this section:
       - Auto-retopo
       - Transform
       - Snap
       - Scale
       - Relax
       - Import
       - Export
       - Subdivide
       - Smooth (CC)
       - Delete Mesh
       - Symmetry
       - Unwrap
       - Auto-Map
       - Store Selection
       - Load Selection
       - Clear Selection
       - Save Contour
       - StemCell
       """
       coat.tools_item("[extension]AutoRetopo") # Auto-retopo
       coat.tools_item("[RetopoTool]sfTransform") # Transform
       coat.tools_item("[RetopoTool]SnapRT") # Snap
       coat.tools_item("[RetopoTool]ScaleCL") # Scale
       coat.tools_item("[RetopoTool]ApplyTSm") # Relax
       coat.tools_item("[RetopoTool]ImportRM") # Import
       coat.tools_item("[RetopoTool]ExportRM") # Export
       coat.tools_item("[RetopoTool]ApplyTS") # Subdivide
       coat.tools_item("[RetopoTool]ApplyTSmooth") # Smooth (CC)
       coat.tools_item("[RetopoTool]ClearTM") # Delete Mesh
       coat.tools_item("[RetopoTool]ApplyTSym") # Symmetry
       coat.tools_item("[RetopoTool]Unwrap") # Unwrap
       coat.tools_item("[RetopoTool]AutoMap") # Auto-Map
       coat.tools_item("[RetopoTool]rtStoreSel") # Store Selection
       coat.tools_item("[RetopoTool]rtRecallSel") # Load Selection
       coat.tools_item("[RetopoTool]rtClearSel") # Clear Selection
       coat.tools_item("[RetopoTool]rLazerCut") # Save Contour
       coat.tools_item("[extension]StemTool") # StemCell



@d_template
def selected_uv():
    """
    Defines context-sensitive UV operations based on the selected UV submode (vertices, edges, faces, islands).

    Tools in this section (Vertices):
    - Clear
    - Invert
    - Rotate CW/CCW
    - Flip U/V
    - Relax / Cloth Relax

    Tools in this section (Edges):
    - Clear
    - Invert
    - Rotate CW/CCW
    - Flip U/V
    - To Line
    - Equidistant
    - Horizontal/Vertical
    - Edge Loop/Ring
    - Set/Delete UV Seams

    Tools in this section (Faces):
    - Clear
    - Invert
    - Rotate CW/CCW
    - Flip U/V
    - Relax / Cloth Relax
    - Hide/Unhide
    - HD Expand/Contract

    Tools in this section (Islands):
    - Clear
    - Invert
    - Rotate CW/CCW
    - Flip U/V
    - Relax / Cloth Relax
    - To ABF/GU/LSCM/Planar/Stripe
    - Hide/Unhide
    - HD Expand/Contract
    - Copy/Paste UV
    """
    coat.tools_section("Selected")
    if coat.GetCurrentToolSubmode("uv") == 1: # verts
       coat.tools_comment("uv_VertsComment") # The next commands are available only if UV - vertex manupulation commands activated.
       coat.tools_item("[RetopoTool]ClearSel") # Clear
       coat.tools_item("[RetopoTool]uvInvSel") # Invert
       coat.tools_item("[RetopoTool]RotateCW") # Rotate CW
       coat.tools_item("[RetopoTool]RotateCCW") # Rotate CCW
       coat.tools_item("[RetopoTool]FlipU") # Flip U
       coat.tools_item("[RetopoTool]FlipV") # Flip V
       coat.tools_item("[RetopoTool]uvRelax") # Relax
       coat.tools_item("[RetopoTool]Relax2") # Cloth Relax
    elif coat.GetCurrentToolSubmode("uv") == 2: # edges
       coat.tools_comment("uv_EdgesComment") # The next commands are available only if UV - edges manupulation commands activated.
       coat.tools_item("[RetopoTool]ClearSel") # Clear
       coat.tools_item("[RetopoTool]uvInvSel") # Invert
       coat.tools_item("[RetopoTool]RotateCW") # Rotate CW
       coat.tools_item("[RetopoTool]RotateCCW") # Rotate CCW
       coat.tools_item("[RetopoTool]FlipU") # Flip U
       coat.tools_item("[RetopoTool]FlipV") # Flip V
       coat.tools_item("[RetopoTool]uvToLine") # To Line
       coat.tools_item("[RetopoTool]uvEquidist") # Equidistant
       coat.tools_item("[RetopoTool]uvHorizontal") # Horizontal
       coat.tools_item("[RetopoTool]uvVertical") # Vertical
       coat.tools_item("[RetopoTool]uvLoop") # Edge Loop
       coat.tools_item("[RetopoTool]uvRing") # Edge Ring
       coat.tools_item("[RetopoTool]uvSeams") # Set Seams
       coat.tools_item("[RetopoTool]uvClrSeams") # Delete UV Seams
    elif coat.GetCurrentToolSubmode("uv") == 3: # faces
       coat.tools_comment("uv_FacesComment") # The next commands are available only if UV - faces manupulation commands activated.
       coat.tools_item("[RetopoTool]ClearSel") # Clear
       coat.tools_item("[RetopoTool]uvInvSel") # Invert
       coat.tools_item("[RetopoTool]RotateCW") # Rotate CW
       coat.tools_item("[RetopoTool]RotateCCW") # Rotate CCW
       coat.tools_item("[RetopoTool]FlipU") # Flip U
       coat.tools_item("[RetopoTool]FlipV") # Flip V
       coat.tools_item("[RetopoTool]Strict") # Relax
       coat.tools_item("[RetopoTool]Relax2") # Cloth Relax
       coat.tools_item("[RetopoTool]uvHide") # Hide
       coat.tools_item("[RetopoTool]uvInvHide") # Inv. Hidden
       coat.tools_item("[RetopoTool]uvUnhide") # Unhide
       coat.tools_item("[RetopoTool]uvUnhideAll") # Unhide All
       coat.tools_item("[RetopoTool]hdExpand") # HD Expand
       coat.tools_item("[RetopoTool]hdContract") # HD Contract
    elif coat.GetCurrentToolSubmode("uv") == 4: # islands
       coat.tools_comment("uv_IslandsComment") # The next commands are available only if UV - islands manupulation commands activated.
       coat.tools_item("[RetopoTool]ClearSel") # Clear
       coat.tools_item("[RetopoTool]uvInvSel") # Invert
       coat.tools_item("[RetopoTool]RotateCW") # Rotate CW
       coat.tools_item("[RetopoTool]RotateCCW") # Rotate CCW
       coat.tools_item("[RetopoTool]FlipU") # Flip U
       coat.tools_item("[RetopoTool]FlipV") # Flip V
       coat.tools_item("[RetopoTool]Strict") # Relax
       coat.tools_item("[RetopoTool]Relax2") # Cloth Relax
       coat.tools_item("[RetopoTool]toABF") # To ABF
       coat.tools_item("[RetopoTool]toGU") # To GU
       coat.tools_item("[RetopoTool]toLSCM") # To LSCM
       coat.tools_item("[RetopoTool]toPlanar") # To Planar
       coat.tools_item("[RetopoTool]toStripe") # To Stripe
       coat.tools_item("[RetopoTool]uvHide") # Hide
       coat.tools_item("[RetopoTool]uvInvHide") # Inv. Hidden
       coat.tools_item("[RetopoTool]uvUnhide") # Unhide
       coat.tools_item("[RetopoTool]uvUnhideAll") # Unhide All
       coat.tools_item("[RetopoTool]hdExpand") # HD Expand
       coat.tools_item("[RetopoTool]hdContract") # HD Contract
       coat.tools_item("[RetopoTool]CopyUV") # Copy UV
       coat.tools_item("[RetopoTool]PasteUV") # Paste UV
    else:
       coat.tools_item("[RetopoTool]ClearSel") # Clear
       coat.tools_item("[RetopoTool]uvInvSel") # Invert
 

@d_tools_section("SmartHybrid")
def SmartHybrid():
	"""
	Experimental toolset for Smart Hybrid modeling operations.

	Tools in this section:
	- Select
	- Create Smart Hybrid
	- Smart Hybrid Tool
	- Smart Hybrid Extrude
	- Smart Hybrid Transform
	- Smart Hybrid Offset
	- Smart Hybrid Alignment
	- Smart Hybrid SubDivide
	"""
	coat.tools_item("[extension]MdlSelectTool") # Select
	coat.tools_item("[extension]SmartHybridCreate") # Create Smart Hybrid
	coat.tools_item("[extension]SmartHybridTool") # Smart Hybrid Tool
	coat.tools_item("[extension]SmartHybridExtrude") # Smart Hybrid Extrude
	coat.tools_item("[extension]SmartHybridTransform") # Smart Hybrid Transform
	coat.tools_item("[extension]SmartHybridOffset") # Smart Hybrid Offset
	coat.tools_item("[extension]SmartHybridAlignment") # Smart Hybrid Alignment
	coat.tools_item("[extension]SmartHybridSubDivide") # Smart Hybrid SubDivide
