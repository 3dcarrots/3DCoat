import coat
from cTemplates.Structs import *

@d_rmb_menu
def CurvesRMB():
    """
    The Right-Click Menu (RMB) for Curves. 
    Initializes global variables based on the properties of the clicked curve (Primitive, Closed).
    """
    global prim, Closed
    prim = coat.menu_property("IsCurvePrimitive")
    Closed = coat.menu_property("IsCurveClosed")

@d_menu_section(CurvesRMB)
def S_Edit():
    """
    Section for general curve editing, conversion, and application.
    
    Items:
    - {CY}Convert to regular curve (conditional)
    - {CY}Edit primitive parameters (conditional)
    - Apply Curves
    - Save Curve...
    - Find Offset (conditional)
    - Duplicate
    """
    global prim, Closed
    if prim:
        coat.menu_item("ConvertToRegularCurve") # {CY}Convert to regular curve
        coat.menu_item("EditPrimParams") # {CY}Edit primitive parameters

    coat.menu_item("ApplyCurves") # Apply Curves
    coat.menu_item("SaveCurve") # Save Curve...
    if not prim:
        coat.menu_item("SM_PointsExtrude") # Find Offset

    coat.menu_item("DuplicateCurve") # Duplicate

@d_submenu("PutOnPlane", CurvesRMB)
def PutOnPlane():
        """
        Submenu for aligning the curve to specific spatial planes.
        
        Items:
        - Average Plane
        - Center Mass + YZ - Plane
        - Center Mass + ZX - Plane
        - Center Mass + XY - Plane
        - YZ - Plane
        - ZX - Plane
        - XY - Plane
        """
        coat.menu_item("AveragePlane") # Average Plane
        coat.menu_item("CmPlaneYZ") # Center Mass + YZ - Plane
        coat.menu_item("CmPlaneZX") # Center Mass + ZX - Plane
        coat.menu_item("CmPlaneXY") # Center Mass + XY - Plane
        coat.menu_item("PlaneYZ") # YZ - Plane
        coat.menu_item("PlaneZX") # ZX - Plane
        coat.menu_item("PlaneXY") # XY - Plane

@d_child(CurvesRMB)
def SM_CurvesOperations_check():
    """
    Conditionally shows curve operations if the curve is not a primitive.
    """
    global prim, Closed
    if not prim:
         SM_CurvesOperations()
         
@d_submenu("SM_CurvesOperations")
def SM_CurvesOperations():
            """
            Submenu for algorithmic operations on the curve structure.
            
            Items:
            - Separate Disconnected Curves
            - Split Self Intersections
            - Boolean Operations
            - Simplify Curve
            - Smoothing Curve
            - Remove Sharp Corners
            - Subdivide Curve
            - Reverse Curve Direction
            - Find Offset
            - Clear Symmetry Dependency
            """
            coat.menu_item("SeparateDisconnectedCurves") # Separate Disconnected Curves
            coat.menu_item("SM_SplitSelfIntersections") # Split Self Intersections
            coat.menu_item("SM_BooleanOperations") # Boolean Operations
            coat.menu_item("SM_SimplifyCurve") # Simplify Curve
            coat.menu_item("SM_SmoothingCurve") # Smoothing Curve
            coat.menu_item("SM_RemoveSharp") # Remove Sharp Corners
            coat.menu_item("SM_SubdivideCurve") # Subdivide Curve
            coat.menu_item("SM_ReverseCurveDirection") # Reverse Curve Direction
            coat.menu_item("SM_PointsExtrude") # Find Offset
            coat.menu_item("SM_ClearSymmetryDependency") # Clear Symmetry Dependency
    

@d_menu_section(CurvesRMB)
def S_OverSculptObject():
    """
    Operations interacting with the underlying Sculpt Object (splitting, beveling).
    
    Items:
    - Split Sculpt Object by Curve (conditional)
    - Make Bevel from Curve (conditional)
    """
    if coat.menu_property("OverSculptObject"):
        coat.menu_item("RichSplitObjectByCurve") # Split Sculpt Object by Curve
        coat.menu_item("BevelOverCurve") # Make Bevel from Curve

@d_menu_section(CurvesRMB)
def S_Brush():
    """
    Tools for running brushes along the curve path.
    
    Items:
    - Brush Along Curve
    - Run Brush Along Projection
    - Edit Pressure Profile
    """
    coat.menu_item("RunBrushAlongCurve") # Brush Along Curve
    coat.menu_item("RunBrushAlongProjection") # Run Brush Along Projection
    coat.menu_item("EditPressuerProfile") # Edit Pressure Profile

@d_menu_section(CurvesRMB)
def S_Projection():
    """
    Tools for selection and filling based on curve projection.
    
    Items:
    - Fill Inside the Closed Curve (conditional)
    - Select/Freeze Projection Area
    - Select/Freeze in 3D Space. (conditional)
    - Freeze/Selection to Curve (conditional)
    """
    global prim, Closed
    if Closed:
        coat.menu_item("FillInsideInProjection") # Fill Inside the Closed Curve

    coat.menu_item("SelectInProjection") # Select/Freeze Projection Area
    if Closed and coat.IsInRoom("Voxels"):
        coat.menu_item("SelectIn3D") # Select/Freeze in 3D Space.

    if coat.IsInRoom("Voxels"):
        coat.menu_item("CreateFromSelectionEdge") # Freeze/Selection to Curve

@d_menu_section(CurvesRMB)
def S_Surface():
    """
    Tools for generating surface geometry (meshes, tubes, sweeps) from curves.
    
    Items:
    - ActiveCurveModifiers
    - Fill with Mesh Layer
    - Attach Tube or Models Array
    - Array/Bend Volume
    - Sweep Profile along Guide Curve
    - Create Surface of Revolution
    - Create Polyhedron
    - Create Swept Surface 2 Guide
    - Create Swept Surface 2 Geners
    - Create Swept Surface N Geners
    - Create Profile Along Guide
    """
    coat.menu_item("ActiveCurveModifiers") # ActiveCurveModifiers
    coat.menu_item("CoverWithSurfaceObject") # Fill with Mesh Layer
    coat.menu_item("TubeOrModels") # Attach Tube or Models Array
    coat.menu_item("BendVolume") # Array/Bend Volume
    coat.menu_item("CreateSweptSurface") # Sweep Profile along Guide Curve
    coat.menu_item("CreateRotateSurface") # Create Surface of Revolution
    coat.menu_item("CreateSurfacePrism") # Create Polyhedron
    coat.menu_item("CreateSweptSurface2Guide") # Create Swept Surface 2 Guide
    coat.menu_item("CreateSweptSurface2Geners") # Create Swept Surface 2 Geners
    coat.menu_item("CreateSweptSurfaceNGeners") # Create Swept Surface N Geners
    coat.menu_item("CreateProfileAlongGuide") # Create Profile Along Guide

@d_menu_section(CurvesRMB)
def S_Settings():
    """
    General curve settings and creation from edges (Retopo room).
    
    Items:
    - Create from selected edges (conditional)
    - Create from open edges (conditional)
    - Snap to Surface
    - Delete Item
    """
    # CurveModifier::RegInMenu(this, Prop);
    if coat.IsInRoom("Retopo"):
        coat.menu_item("CreateFromSelectedEdges") # Create from selected edges
        coat.menu_item("CreateFromOpenEdges") # Create from open edges

    coat.menu_item("AttachToSurface") # Snap to Surface
    CurveSettings()
    coat.menu_item("DeleteItem") # Delete Item

@d_submenu("CurveSettings")
def CurveSettings():
    """
    Submenu for curve visualization and property locking.
    
    Items:
    - Closed Curve (conditional)
    - Show Radiuses
    - Lock Radius
    - Show Normals
    - Lock Normals
    - Show Points
    - Snap To Surfaces
    - Keep In Plane (conditional)
    - Show Length
    - Assign Radius
    - Change Curve Color
    """
    global prim, Closed
    if not prim:
        coat.menu_item("ClosedCurve") # Closed Curve

    coat.menu_item("ShowRadiuses") # Show Radiuses
    coat.menu_item("LockRadius") # Lock Radius
    coat.menu_item("ShowNormals") # Show Normals
    coat.menu_item("LockNormals") # Lock Normals
    coat.menu_item("ShowPoints") # Show Points
    coat.menu_item("SnapToSurfaces") # Snap To Surfaces
    if not prim:
        coat.menu_item("KeepInPlane") # Keep In Plane

    coat.menu_item("SM_ShowLength") # Show Length
    coat.menu_item("SameRadius") # Assign Radius
    coat.menu_item("ChangeCurveColor") # Change Curve Color