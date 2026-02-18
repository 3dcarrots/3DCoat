# 
# The Free Surface room toolset definition.
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

Tools = cTemplate()

@d_child(Tools)
def Mesh_to_NURBS_Comment():
   """
   Sets the toolset comment/header for the Mesh to NURBS workflow.
   """
   coat.tools_comment("Mesh to NURBS")

@d_tools_section("Basic", Tools)
def Basic():
   """
   Basic tools for selecting elements, creating primitives, and generating various surface types (NURBS, Loft, Patch, etc.).

   Tools in this section:
   - Select
   - 3D Primitives
   - 2D Primitives
   - Select (TopTool)
   - Surface Patch
   - Mesh to NURBS
   - Surface
   - Lofted Surface
   - Filling Surface
   - ReSurfaces
   - Ruled Surface
   - Surface To Mesh
   """
   coat.default_tool("[extension]MdlSelectTool")
   coat.tools_item("[extension]MdlSelectTool") # Select
   coat.tools_item("{RTPPRIM}[extension]RTP_PRIM") # 3D Primitives
   coat.tools_item("{RTPPRIM}[extension]RTP_PRIM2") # 2D Primitives
   coat.tools_item("[RetopoTool]TopToolSelectAndOperate") # Select
   coat.tools_item("[extension]MdlSurfacePatch") # Surface Patch
   coat.tools_item("[extension]SurfaceUnitTool") # Mesh to NURBS
   coat.tools_item("[extension]MdlRootSurface") # Surface
   coat.tools_item("[extension]LoftedSurface") # Lofted Surface
   coat.tools_item("[extension]FillingSurface") # Filling Surface
   coat.tools_item("[extension]MdlCoveringSurfaces") # ReSurfaces
   coat.tools_item("[extension]MdlRuledSurface") # Ruled Surface
   coat.tools_item("[extension]SurfaceToMesh") # Surface To Mesh


@d_tools_section("EditGeometry", Tools)
def EditGeometry():
   """
   Tools for modifying existing surfaces, including merging, extracting edges, snapping, and symmetry.

   Tools in this section:
   - Merge Surfaces
   - Extract Edge
   - Snap Surfaces
   - Smoothing Two Surfaces
   - Symmetry of Surface
   """
   coat.tools_item("[extension]UnitSurfaces") # Merge Surfaces
   coat.tools_item("[extension]MdlExtractEdge") # Extract Edge
   coat.tools_item("[extension]SnapSurfaces") # Snap Surfaces
   coat.tools_item("[extension]SmoothingTwoSurfaces") # Smoothing Two Surfaces
   coat.tools_item("[extension]SymmetrySurface") # Symmetry of Surface

@d_tools_section("WholeSurfaces", Tools)
def WholeSurfaces():
   """
   Global operations for importing, exporting, and analyzing surfaces.

   Tools in this section:
   - Export Surfaces
   - Import
   - Analyze Surfaces
   """
   coat.tools_item("[extension]ExportIgesSurfaces") # Export Surfaces
   coat.tools_item("[extension]ImportIgesSurfaces") # Import
   coat.tools_item("[extension]AnalyzeSurfaces") # Analyze Surfaces