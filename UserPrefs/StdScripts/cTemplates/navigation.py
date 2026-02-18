import coat
from cTemplates.Structs import *


@d_template
def NavigationBar():
    """
    Defines the main navigation bar structure and includes the viewport menu.
    """
    NavigationBar.IncludeContent()
    ViewPortMenu()

@d_child(NavigationBar)
def Light():
    """
    Controls for lighting adjustment (contrast, brightness, position) and environment blurring.
    
    Items:
    - Adjust the contrast of lighting
    - Adjust the primary light intensity
    - Adjust the light angle
    - Drag to blur/sharp the environment texture
    """
    coat.menu_item("@LIGHT_CONTRAST") # Adjust the contrast of lighting
    coat.menu_item("@LIGHT_BRIGHTNESS") # Adjust the primary light intensity
    coat.menu_item("@MOVE_LIGHT") # Adjust the light angle
    coat.menu_item("@BLUR_PANO") # Drag to blur/sharp the environment texture
@d_child(NavigationBar)
def Roll():
    """
    Controls for rolling the camera view.
    
    Items:
    - Roll counterclockwise on the fixed angle
    - Roll clockwise on the fixed angle
    """
    coat.menu_item("$NAVY_ROLL_LEFT") # Roll counterclockwise on the fixed angle
    coat.menu_item("$NAVY_ROLL_RIGHT") # Roll clockwise on the fixed angle

@d_child(NavigationBar)
def Camera():
    """
    Standard camera controls: Rotate, Move, Scale, FOV, and rotation mode toggle.
    
    Items:
    - Toggle between two rotation modes
    - Rotate the camera
    - Move the camera
    - Zoom the camera
    - Vary field of view (FOV)
    """
    coat.menu_item("@TOGGLE_Y_ROTATION") # Toggle between two rotation modes
    coat.menu_item("$NAVY_RORATE") # Rotate the camera
    coat.menu_item("$NAVY_MOVE") # Move the camera
    coat.menu_item("$NAVY_SCALE") # Zoom the camera
    coat.menu_item("@NAVY_FOV") # Vary field of view (FOV)

@d_child(NavigationBar)
def ViewPort():
    """
    Viewport framing and projection controls.
    
    Items:
    - Frame. Put scene or current object in the center
    - Focus on the brush
    - Reset the camera to the default position
    - Toggle between perspective and orthographic projection
    """
    coat.menu_item("$NAVIFRAME") # Frame. Put scene or current object in the center
    coat.menu_item("$NAVY_FRAME2") # Focus on the brush
    coat.menu_item("@NAVY_CENTER") # Reset the camera to the default position
    coat.menu_item("$VIEW_ORTHO") # Toggle between perspective and orthographic projection

@d_child(NavigationBar)
def Grid():
    """
    3D Grid toggles.
    
    Items:
    - Show 3D Grid
    - Snap to 3D Grid
    """
    coat.menu_item("$SHOW_GRID_3D") # Show 3D Grid
    coat.menu_item("$SNAP_GRID_3D") # Snap to 3D Grid

@d_child(NavigationBar)
def View():
    """
    General view settings: Axis, Fullscreen, Panoramas, Reference images.
    
    Items:
    - Switch to the orthographic view and snap
    - Show/Hide Axis
    - Toggle Full Screen
    - Environment Map
    - Show/Hide Reference Images
    - Projector
    """
    coat.menu_item("$SNAP_NEAREST_VIEW") # Switch to the orthographic view and snap
    coat.menu_item("$SHOW_AXIS") # Show/Hide Axis
    coat.menu_item("@ToggleFullscreen") # Toggle Full Screen
    coat.menu_item("@NAVI_PanoramasList") # Environment Map
    coat.menu_item("@NAVI_Reference") # Show/Hide Reference Images
    coat.menu_item("@NAVI_Projector") # Projector


@d_child(NavigationBar)
def Addons():
    """
    Dropdown menu for custom addons.
    """
    if coat.iconic_submenu("arrow_drop_down_circle", 32):
        Addons.IncludeContent()
        coat.menu_exit()

@d_child(Addons)
def AddonList():
        """
        Dynamic list of addons.
        """
        coat.menu_item("ListAddons::ROOM::Custom")
        coat.menu_item("NewAddonsSection::Custom1")

################################
##### ViewPortMenu #############

@d_template
def ViewPortMenu():
    """
    The 'Camera' dropdown menu containing advanced view, background, and snapping options.
    """
    if coat.iconic_submenu("Camera4", 32):
        ViewPortMenu.IncludeContent()
        coat.menu_exit()

@d_submenu("Custom_sceme", ViewPortMenu)
def Custom_sceme():
            """
            Submenu for Custom Navigation presets.
            
            Items:
            - Navigation Presets
            """
            coat.menu_item("NavigationPresets") # Navigation Presets
    
@d_menu_section(ViewPortMenu)
def S_edit_navi():
        """
        Section for customizing navigation.
        
        Items:
        - Customize Navigation
        """
        coat.menu_item("edit_navi") # Customize Navigation
@d_menu_section(ViewPortMenu)
def S_CameraUndo():
        """
        Section for Camera Undo/Redo operations.
        
        Items:
        - Navigation undo
        - Navigation redo
        """
        coat.menu_item("CameraUndo") # Navigation undo
        coat.menu_hotkey("Z", 0, 0, 1) # ALT-Z
        coat.menu_item("CameraRedo") # Navigation redo
        coat.menu_hotkey("Y", 0, 0, 1) # ALT-Y

Background = Submenu("Background", ViewPortMenu)
            
@d_menu_section(Background)
def S_BackgroundType():
            """
            Select the type of background (Gradient, Image, Panorama).
            
            Items:
            - Vertical Gradient
            - Use Background Image
            - Use Environment Map
            """
            coat.menu_item("GradientBackground") # Vertical Gradient
            coat.menu_item("ImageBackground") # Use Background Image
            coat.menu_item("PanoramaBackground") # Use Environment Map
@d_menu_section(Background)
def S_ChooseBackground():
            """
            Pick colors or images for the background.
            
            Items:
            - Choose Top Color
            - Choose Bottom Color
            - Choose Background Image
            """
            coat.menu_item("ChooseTopColor") # Choose Top Color
            coat.menu_item("ChooseBottomColor") # Choose Bottom Color
            coat.menu_item("ChooseBackgrImage") # Choose Background Image
@d_menu_section(Background)
def S_Panorama():
            """
            Options for managing the Environment Map panorama.
            
            Items:
            - Lock Environment
            - Choose Environment Map
            - Rotate Environment Map CCW
            - Rotate Environment Map CW
            - Blur Environment Map
            - Sharpen Environment Map
            """
            coat.menu_item("LockPanorama") # Lock Environment
            coat.menu_item("ChoosePanoramaImage") # Choose Environment Map
            coat.menu_item("RotatePanoramaCCW") # Rotate Environment Map CCW
            coat.menu_item("RotatePanoramaCW") # Rotate Environment Map CW
            coat.menu_item("BlurPanorama") # Blur Environment Map
            coat.menu_hotkey("[", 1, 0, 0) # SHIFT+[
            coat.menu_item("SharpenPanorama") # Sharpen Environment Map
            coat.menu_hotkey("]", 1, 0, 0) # SHIFT+]
@d_menu_section(Background)
def S_RefImage():
            """
            Options for managing reference images on axis planes.
            
            Items:
            - Ref image for X-axis
            - Ref image for Y-axis
            - Ref image for Z-axis
            - Edit Image Placement
            - Paint over the references
            - Show in exact views
            """
            coat.menu_item("ChooseXRefImage") # Ref image for X-axis
            coat.menu_item("ChooseYRefImage") # Ref image for Y-axis
            coat.menu_item("ChooseZRefImage") # Ref image for Z-axis
            coat.menu_item("EditRefImagesPlacement") # Edit Image Placement
            coat.menu_item("PaintOverRefImages") # Paint over the references
            coat.menu_item("ShowInExactPositions") # Show in exact views


CameraSnapping = Submenu("CameraSnapping", ViewPortMenu)

@d_menu_section(CameraSnapping)
def S_CameraSnapping():
            """
            Presets for snapping the camera to specific isometric angles or centers.
            
            Items:
            - Snap camera by 45 degree
            - Equilateral hexagon isometry
            - Rhombus 2x1 isometry
            - Camera In World Center
            - Camera For 2D Painting
            """
            coat.menu_item("CameraIsometricSnap45dg") # Snap camera by 45 degree
            coat.menu_item("CameraIsometricSnapHexagon") # Equilateral hexagon isometry
            coat.menu_item("CameraIsometricSnapRhombus2x1") # Rhombus 2x1 isometry
            coat.menu_item("CameraInWorldCenter") # Camera In World Center
            coat.menu_item("CameraFor2DPaint") # Camera For 2D Painting
            # menu_item("CameraLock2DCanvas");/CameraLock2DCanvas
    
@d_menu_section(ViewPortMenu)
def S_ViewSide():
        """
        Standard orthographic view switching (Front, Back, Left, Right, Top, Bottom).
        
        Items:
        - Front
        - Back
        - Left
        - Right
        - Top
        - Bottom
        - Look Along Normal Vector
        """
        coat.menu_item("VIEW_FRONT") # Front
        coat.menu_hotkey("NUM2", 0, 0, 0) # NUM2
        coat.menu_item("VIEW_BACK") # Back
        coat.menu_hotkey("NUM8", 0, 0, 0) # NUM8
        coat.menu_item("VIEW_LEFT") # Left
        coat.menu_hotkey("NUM4", 0, 0, 0) # NUM4
        coat.menu_item("VIEW_RIGHT") # Right
        coat.menu_hotkey("NUM6", 0, 0, 0) # NUM6
        coat.menu_item("VIEW_TOP") # Top
        coat.menu_hotkey("NUM7", 0, 0, 0) # NUM7
        coat.menu_item("VIEW_BOTTOM") # Bottom
        coat.menu_hotkey("NUM1", 0, 0, 0) # NUM1
        coat.menu_item("ViewAlongNormal") # Look Along Normal Vector
        coat.menu_hotkey("NUM*", 0, 0, 0) # NUM*
@d_menu_section(ViewPortMenu)
def S_Presets():
        """
        Managing camera shortcuts (adding, deleting, switching).
        
        Items:
        - Add Camera Shortcut
        - Delete Camera Shortcut
        - Switch to Previous Shortcut
        - Switch to Next Shortcut
        - Save Camera
        - Load Camera
        """
        coat.menu_item("ADD_CAM_PRESET") # Add Camera Shortcut
        coat.menu_hotkey("UP", 0, 1, 0) # CTRL+UP
        coat.menu_item("DEL_CAM_PRESET") # Delete Camera Shortcut
        coat.menu_hotkey("DOWN", 0, 1, 0) # CTRL+DOWN
        coat.menu_item("PREV_CAM_PRESET") # Switch to Previous Shortcut
        coat.menu_hotkey("LEFT", 0, 1, 0) # CTRL+LEFT
        coat.menu_item("NEXT_CAM_PRESET") # Switch to Next Shortcut
        coat.menu_hotkey("RIGHT", 0, 1, 0) # CTRL+RIGHT
        coat.menu_item("SaveCamera") # Save Camera
        coat.menu_item("LoadCamera") # Load Camera
@d_menu_section(ViewPortMenu)
def S_Pivot():
        """
        Configuration for the rotation pivot point.
        
        Items:
        - 3DConnexion Pivot Algorithm
        - Rotate Around Current Pick Point
        - Rotate Around World Center
        - Rotate Around Last Draw Point
        - Rotate Around Object Bounding Box
        - Rotate Around Custom Point
        - Rotate around the Camera origin
        """
        coat.menu_item("Use3DConnexionPivot") # 3DConnexion Pivot Algorithm
        coat.menu_item("rotate_around_curr_pick_point") # Rotate Around Current Pick Point
        coat.menu_item("rotate_around_world_center") # Rotate Around World Center
        coat.menu_item("rotate_around_last_draw_point") # Rotate Around Last Draw Point
        coat.menu_item("rotate_around_bound_box_center") # Rotate Around Object Bounding Box
        coat.menu_item("rotate_around_custom_point") # Rotate Around Custom Point
        coat.menu_hotkey("F", 0, 0, 0) # F
        coat.menu_item("rotate_around_camera_origin") # Rotate around the Camera origin