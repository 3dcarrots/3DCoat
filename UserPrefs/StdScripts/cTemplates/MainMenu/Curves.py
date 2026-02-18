import coat
from cTemplates.Structs import *

CurvesMenu = MainMenu("Curves")
@d_menu_section(CurvesMenu)
def S_Edit():
   """
   Section for activating the curve editor, visibility controls, and general curve management.
   
   Items:
   - Activate Curves Editor
   - Curves Quick Menu
   - Stop Editing Curves
   - Stop Editing and Hide Selected
   - Hide Selected Curves
   - Curves Usage Hint
   - Curves Tree
   - Record strokes
   """
   coat.menu_item("ActivateCurvesEditor") # Activate Curves Editor
   coat.menu_item("CurvParamsPopup") # Curves Quick Menu
   coat.menu_hotkey("Q", 0, 0, 0)
   coat.menu_item("StopEditCurves") # Stop Editing Curves
   coat.menu_item("StopEditCurvesAndHide") # Stop Editing and Hide Selected
   coat.menu_item("HideSelectedCurves") # Hide Selected Curves
   coat.menu_item("SplineUsageHint") # Curves Usage Hint
   coat.menu_item("CurvesTree") # Curves Tree
   coat.menu_item("RecordStrokes") # Record strokes

@d_menu_section(CurvesMenu)
def S_File():
   """
   Section for importing and exporting curve data.
   
   Items:
   - Save Curve...
   - Save Curves Separately...
   - Load Curve...
   - Load Curve from Image...
   """
   coat.menu_item("SaveCurve") # Save Curve...
   coat.menu_item("SaveSeparateCurves") # Save Curves Separately...
   coat.menu_item("LoadCurve") # Load Curve...
   coat.menu_item("LoadCurveAsImage") # Load Curve from Image...

@d_menu_section(CurvesMenu)
def S_Snap():
   """
   Section for configuring how curve points snap to surfaces, other points, or grids.
   
   Items:
   - Snap to Surface
   - Snap to Curve Points
   - Snap to Curve
   - Snap to Center
   - Quantize length
   - Snap to Horizontal/Vertical
   - Snapping Settings
   """
   coat.menu_item("cuSnapToSurface") # Snap to Surface
   coat.menu_item("cuSnapToPoints") # Snap to Curve Points
   coat.menu_item("cuSnapToCurve") # Snap to Curve
   coat.menu_item("cuSnapToCurveCenter") # Snap to Center
   coat.menu_item("cuSnapToDistance") # Quantize length
   coat.menu_item("cuSnapToHorizontalVertical") # Snap to Horizontal/Vertical
   coat.menu_item("cuSnapSettings") # Snapping Settings

@d_menu_section(CurvesMenu)
def S_Render():
   """
   Rendering options for curves visibility.
   
   Items:
   - Render Curves on Back Side
   """
   coat.menu_item("RenderCurvesOnBackFaces") # Render Curves on Back Side

@d_submenu("PutOnPlane", CurvesMenu)
def PutOnPlane():
       """
       Submenu for aligning curves to specific planes (Average, Center Mass, or Axis planes).
       
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
 
@d_submenu("SM_CurvesOperations", CurvesMenu)
def SM_CurvesOperations():
       """
       Submenu for algorithmic operations on curves such as booleans, simplification, and smoothing.
       
       Items:
       - Separate Disconnected Curves
       - Split Self Intersections
       - Boolean Operations
       - Simplify Curve
       - Smoothing Curve
       - Remove Sharp Corners
       - Subdivide Curve
       - Reverse Curve Direction
       - Toggle Length Displaying
       """
       coat.menu_item("SeparateDisconnectedCurves") # Separate Disconnected Curves
       coat.menu_item("SM_SplitSelfIntersections") # Split Self Intersections
       coat.menu_item("SM_BooleanOperations") # Boolean Operations
       coat.menu_item("SM_SimplifyCurve") # Simplify Curve
       coat.menu_item("SM_SmoothingCurve") # Smoothing Curve
       coat.menu_item("SM_RemoveSharp") # Remove Sharp Corners
       coat.menu_item("SM_SubdivideCurve") # Subdivide Curve
       coat.menu_item("SM_ReverseCurveDirection") # Reverse Curve Direction
       coat.menu_item("ToogleDisplayLength") # Toggle Length Displaying
 
@d_submenu("Modifiers", CurvesMenu)
def Modifiers():
       """
       Submenu for managing meshes (modifiers) attached to curves.
       
       Items:
       - Detach Curve Modifiers (selected)
       - Detach and Delete Meshes (selected)
       - Edit Curve Modifier (selected)
       - Hide Selected Modifiers
       - Hide All Meshes w/ Curve Modifiers
       - Show All Meshes w/ Curve Modifiers
       """
       coat.menu_item("DetachCurvModifierSel") # Detach Curve Modifiers (selected)
       coat.menu_item("DetachCurvAndRemoveSel") # Detach and Delete Meshes (selected)
       coat.menu_item("EditCurvModifierPropertiesSel") # Edit Curve Modifier (selected)
       coat.menu_item("HideCurvModifier") # Hide Selected Modifiers
       coat.menu_item("HideAllCurvModifiers") # Hide All Meshes w/ Curve Modifiers
       coat.menu_item("ShowAllCurvModifiers") # Show All Meshes w/ Curve Modifiers
 
@d_menu_section(CurvesMenu)
def S_Apply():
   """
   Section for applying curves to create strokes or geometry.
   
   Items:
   - Apply Curves
   - Start New Curve
   - Brush Along Curve
   - Run Brush Along Projection
   - Edit Pressure Profile
   """
   coat.menu_item("ApplyCurves") # Apply Curves
   coat.menu_item("StartNewCurve") # Start New Curve
   coat.menu_item("RunBrushAlongCurve") # Brush Along Curve
   coat.menu_item("RunBrushAlongProjection") # Run Brush Along Projection
   coat.menu_item("EditPressuerProfile") # Edit Pressure Profile

@d_menu_section(CurvesMenu)
def S_Select():
   """
   Section for operations involving selection masks and room-specific geometry creation (Voxel/Retopo).
   
   Items:
   - Select/Freeze Projection Area
   - Select/Freeze in 3D Space. (conditional)
   - Freeze/Selection to Curve (conditional)
   - Fill by Quads (conditional)
   - Fill by Triangles (conditional)
   - Create from selected edges (conditional)
   - Create from open edges (conditional)
   - Snap to Surface
   - Assign Radius
   - Set Coordinate
   - Delete All Curves
   """
   coat.menu_item("SelectInProjection") # Select/Freeze Projection Area
   if coat.IsInRoom("Voxels"):
        coat.menu_item("SelectIn3D") # Select/Freeze in 3D Space.
        # menu_item("FillByVoxels");/Fill by voxels
        coat.menu_item("CreateFromSelectionEdge") # Freeze/Selection to Curve
 
   if coat.IsInRoom("Retopo"):
       coat.menu_item("FillByQuads") # Fill by Quads
       coat.menu_item("FillByTriangles") # Fill by Triangles
       coat.menu_item("CreateFromSelectedEdges") # Create from selected edges
       coat.menu_item("CreateFromOpenEdges") # Create from open edges
 
   coat.menu_item("AttachToSurface") # Snap to Surface
   coat.menu_item("SameRadius") # Assign Radius
   coat.menu_item("SetCoordinate") # Set Coordinate
   coat.menu_item("DelSplines") # Delete All Curves