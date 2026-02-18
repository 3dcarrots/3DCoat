import coat
from cTemplates.Structs import *

RetopoMenu = MainMenu("Mesh")

@d_menu_section(RetopoMenu)
def S_File():
   """
   Section for importing, exporting, and acquiring retopology meshes.
   
   Items:
   - Import
   - Export
   - Export Selected
   - Export Separate Poly Objects
   - Save contour for laser cutting
   - Copy Mesh from the Painting room
   """
   coat.menu_item("ImportRawMesh") # Import
   coat.menu_item("ExportRawMesh") # Export
   coat.menu_item("ExportSelected") # Export Selected
   coat.menu_item("ExportGroups") # Export Separate Poly Objects
   coat.menu_item("ExportEPS") # Save contour for laser cutting
   coat.menu_item("UseCurrMesh") # Copy Mesh from the Painting room

@d_submenu("SelectFaces", RetopoMenu)
def SelectFaces():
       """
       Submenu for selecting specific types of polygon topology.
       
       Items:
       - Select Triangles
       - Select Quads
       - Select N-Gons
       - Select Stars
       - Improve Quad Topology
       """
       coat.menu_item("SelectTriangles") # Select Triangles
       coat.menu_item("SelectQuads") # Select Quads
       coat.menu_item("SelectNGons") # Select N-Gons
       coat.menu_item("SelectStars") # Select Stars
       coat.menu_item("ImproveQuadTopology") # Improve Quad Topology
 
@d_menu_section(RetopoMenu)
def S_Symm():
   """
   Section for symmetry operations on the retopology mesh.
   
   Items:
   - Apply Symmetry to All Layers
   - Apply Symmetry to Current Layer
   - Virtual Mirror Mode
   """
   coat.menu_item("ApplyTopoSymm") # Apply Symmetry to All Layers
   coat.menu_item("ApplyTopoSymmCurr") # Apply Symmetry to Current Layer
   coat.menu_item("Show_Mirrored_Side") # Virtual Mirror Mode

@d_menu_section(RetopoMenu)
def S_Subdivide():
   """
   Section for live subdivision and smoothing of the retopo mesh.
   
   Items:
   - Live Smooth
   - Subdivide 1
   - Subdivide 2
   - Subdivide 3
   - Unlink Sculpt Mesh
   """
   coat.menu_item("SculptMesh") # Live Smooth
   coat.menu_item("Subdivide1") # Subdivide 1
   coat.menu_item("Subdivide2") # Subdivide 2
   coat.menu_item("Subdivide3") # Subdivide 3
   coat.menu_item("UnlinkSculptMesh") # Unlink Sculpt Mesh

@d_menu_section(RetopoMenu)
def S_Edit():
   """
   Section for mesh editing, cleanup, and unwrapping operations.
   
   Items:
   - Set Islands Min Distance
   - Auto Unwrap Attached Faces
   - Unwrap
   - Remove Self Intersections
   - Close Holes
   - Remove N-Gons
   - Clear Mesh
   - Subdivide
   - Relax
   - Apply Triangulation
   - Apply Quadrangulation
   """
   coat.menu_item("SetupIslandsMinDistance") # Set Islands Min Distance
   coat.menu_item("AutoUnwrapAttachedFaces") # Auto Unwrap Attached Faces
   coat.menu_item("Unwrap") # Unwrap
   coat.menu_item("RemoveSelfIntersections") # Remove Self Intersections
   coat.menu_item("Close_Holes") # Close Holes
   coat.menu_item("RemoveNGons") # Remove N-Gons
   coat.menu_item("ClearTopoMesh") # Clear Mesh
   coat.menu_item("ApplyTopoSubdiv") # Subdivide
   coat.menu_item("ApplyTopoSmooth") # Relax
   coat.menu_item("ApplyTriangulation") # Apply Triangulation
   coat.menu_item("ApplyQuadrangulation") # Apply Quadrangulation

@d_menu_section(RetopoMenu)
def S_Restore():
   """
   Section for saving and loading the temporary state of the retopology mesh.
   
   Items:
   - Save Retopology State
   - Load Retopology State
   """
   coat.menu_item("STORE_RETOPO_MESH") # Save Retopology State
   coat.menu_item("RESTORE_RETOPO_MESH") # Load Retopology State

@d_menu_section(RetopoMenu)
def S_Extensions():
   """
   Inserts retopo-related options provided by installed extensions.
   
   Items:
   - Retopo extensions
   """
   coat.menu_insert_extensions("Retopo")