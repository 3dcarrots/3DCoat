import coat
from cTemplates.Structs import *

WindowsMenu = MainMenu("Windows")

Popups = Submenu("Popups", WindowsMenu)

@d_menu_section(Popups)
def Popups_S1():
    """
    Section for general popup panels and room-specific previews.
    
    Items:
    - UV Preview (conditional)
    - Start Menu
    - Tool Presets
    - Tools Palette
    """
    if coat.IsInRoom("Retopo"):
        coat.menu_item("UV_PREV") # UV Preview
    
    if coat.IsInRoom("UV"):
        coat.menu_item("UV_PREV") # UV Preview

    coat.menu_item("GLOBALSEARCH")       
    coat.menu_hotkey("F", 0, 1, 0) # SPACE
    coat.menu_item("StartMenu") # Start Menu
    coat.menu_item("SHOW_PRESETS") # Tool Presets
    coat.menu_item("SHOW_TOOLS_PALETTE") # Tools Palette
    coat.menu_hotkey("SPACE", 0, 0, 0) # SPACE
    # menu_item("SHOW_SUBOBJ");/Paint Objects
    # menu_item("SHOW_MATERIALS");/Surface Materials

@d_menu_section(Popups)
def Popups_S_ProxySlider():
    """
    Section for the Proxy Slider popup.
    
    Items:
    - Proxy Slider
    """
    coat.menu_item("ProxySlider") # Proxy Slider

@d_menu_section(Popups)
def Popups_paint():
    """
    Section for painting-related popups and hotkeys (Channels, Stroke Mode, Quick Panel).
    
    Items:
    - Depth Channel
    - Color Channel
    - Glossiness Channel
    - Stroke Mode
    - Quick Panel
    """
    coat.menu_item("ID_BUMP_HDR") # Depth Channel
    coat.menu_hotkey("D", 0, 0, 0) # D
    coat.menu_item("ID_COLOR_HDR") # Color Channel
    coat.menu_hotkey("C", 0, 0, 0) # C
    coat.menu_item("ID_SPECULAR_HDR") # Glossiness Channel
    coat.menu_hotkey("R", 0, 0, 0) # R
    coat.menu_item("ID_PENOPS") # Stroke Mode
    coat.menu_hotkey("E", 0, 0, 0) # E
    coat.menu_item("QuickPanel") # Quick Panel
    coat.menu_hotkey("T", 0, 0, 0) # T



@d_menu_section(Popups)
def Popups_Extensions():
    """
    Inserts popup menu items provided by installed extensions.
    
    Items:
    - Windows.Popups extensions
    """
    coat.menu_insert_extensions("Windows.Popups")
    coat.menu_sort()
    # menu_item("VoxTreeRMB");/Trigger Volume Properties Window


Sliders = Submenu("Sliders", WindowsMenu)
@d_menu_section(Sliders)
def Sliders_S1():
    """
    Section for incremental adjustments of Opacity, Angle, Radius, and Degree.
    
    Items:
    - Decrease Opacity
    - Increase Opacity
    - Decrease Angle
    - Increase Angle
    - Decrease Radius
    - Increase Radius
    - Decrease Degree
    - Increase Degree
    """
    coat.menu_item("DEC_OPACITY") # Decrease Opacity
    coat.menu_item("INC_OPACITY") # Increase Opacity
    coat.menu_item("DEC_ANGLE") # Decrease Angle
    coat.menu_item("INC_ANGLE") # Increase Angle
    coat.menu_item("DEC_RADIUS") # Decrease Radius
    coat.menu_item("INC_RADIUS") # Increase Radius
    coat.menu_item("DEC_DEGREE") # Decrease Degree
    coat.menu_item("INC_DEGREE") # Increase Degree
@d_menu_section(Sliders)
def Sliders_S2():
    """
    Section for incremental adjustments of Smoothing, Glossiness, and Color Swapping.
    
    Items:
    - Decrease Smooth Degree
    - Increase Smooth Degree
    - Decrease Glossiness Opacity
    - Increase Glossiness Opacity
    - Decrease Glossiness Degree
    - Increase Glossiness Degree
    - Swap Colors
    - Windows.Sliders extensions
    """
    coat.menu_item("DEC_SM_DEGREE") # Decrease Smooth Degree
    coat.menu_item("INC_SM_DEGREE") # Increase Smooth Degree
    coat.menu_item("DEC_SPEC_OPACITY") # Decrease Glossiness Opacity
    coat.menu_item("INC_SPEC_OPACITY") # Increase Glossiness Opacity
    coat.menu_item("DEC_SPEC_DEGREE") # Decrease Glossiness Degree
    coat.menu_item("INC_SPEC_DEGREE") # Increase Glossiness Degree
    coat.menu_item("SWAP_COLORS") # Swap Colors
    coat.menu_insert_extensions("Windows.Sliders")

@d_menu_section(Sliders)
def Sliders_S3():
    """
    Section for shortcuts to main brush parameters: Depth, Radius, Rotation, Smoothing.
    
    Items:
    - Depth
    - Radius
    - Rotation
    - Smoothing
    """
    coat.menu_item("PEN_DEPTH") # Depth
    coat.menu_item("PEN_RADIUS") # Radius
    coat.menu_item("PEN_ROTSN") # Rotation
    coat.menu_item("SMOOTH_DEG") # Smoothing
@d_menu_section(Sliders)
def Sliders_S4():
    """
    Section for shortcuts to Opacity, Glossiness Intensity, and Debug Layers.
    
    Items:
    - Opacity
    - Glossiness Intensity
    - Debug Layers
    """
    coat.menu_item("PEN_MASK") # Opacity
    coat.menu_item("PEN_SPEC") # Glossiness Intensity
    coat.menu_item("DebugLayers") # Debug Layers

@d_menu_section(Sliders)
def Sliders_S_ToggleUI():
    """
    Shortcut for toggling the User Interface visibility.
    
    Items:
    - Toggle Popup/Docked Windows
    """
    coat.menu_item("ToggleUI") # Toggle Popup/Docked Windows
    coat.menu_hotkey("Tab", 0, 0, 0)

@d_menu_section(Sliders)
def Sliders_S_Pick():
    """
    Section for picking colors and layers/volumes.
    
    Items:
    - Pick Color/Depth/Glossiness
    - Pick Current Layer/Volume
    - Pick layer add
    - Pick layer sub
    """
    coat.menu_item("Pick_color") # Pick Color/Depth/Glossiness
    coat.menu_hotkey("V", 0, 0, 0) # V
    coat.menu_item("Pick_layer") # Pick Current Layer/Volume
    coat.menu_hotkey("H", 0, 0, 0) # H
    coat.menu_item("Pick_layer_add") # Pick layer add
    coat.menu_hotkey("H", 1, 0, 0) # SHIFT+H
    coat.menu_item("Pick_layer_sub") # Pick layer sub
    coat.menu_hotkey("H", 0, 1, 0) # CTRL+H


@d_menu_section(WindowsMenu) 
def Windows_S_UIColorThemesList():
   """
   Menu item for selecting UI Color Themes.
   
   Items:
   - UI Color Scheme
   """
   coat.menu_item("UIColorThemesList") # UI Color Scheme

@d_menu_section(WindowsMenu) 
def Windows_S_Default():
   """
   Section for resetting page layouts to defaults.
   
   Items:
   - Reset This Page to Default
   - Reset All Pages to Default
   """
   coat.menu_item("ResetThisPageToDefault") # Reset This Page to Default
   coat.menu_item("ResetAllPagesToDefault") # Reset All Pages to Default

@d_menu_section(WindowsMenu) 
def Windows_S_Restore():
   """
   Section for storing and restoring the layout of the current page.
   
   Items:
   - Store This Page Layout
   - Restore This Page Layout
   """
   coat.menu_item("StoreThisPageLayout") # Store This Page Layout
   coat.menu_item("RestoreThisPageLayout") # Restore This Page Layout

@d_menu_section(WindowsMenu) 
def Windows_S_RestoreAll():
   """
   Section for storing and restoring the entire workspace layout.
   
   Items:
   - Store Workspace
   - Restore Workspace
   """
   coat.menu_item("StoreAllPagesLayout") # Store Workspace
   coat.menu_item("RestoreAllPagesLayout") # Restore Workspace

@d_menu_section(WindowsMenu) 
def Windows_S_Reset():
   """
   Section for managing room visibility and adding new rooms.
   
   Items:
   - Make All Default Rooms Visible
   - Make All Rooms Visible
   - Hide Current Room
   - Add New Room
   """
   coat.menu_item("ResetDefaultPagesVisibility") # Make All Default Rooms Visible
   coat.menu_item("ResetAllPagesVisibility") # Make All Rooms Visible
   coat.menu_item("HideCurrentRoom") # Hide Current Room
   coat.menu_item("AddNewRoom") # Add New Room

@d_menu_section(WindowsMenu) 
def Windows_S_ToggleUI():
   """
   Section for general UI visibility and customization toggles.
   
   Items:
   - Toggle Popup/Docked Windows
   - Customize UI (conditional)
   - Windows extensions
   """
   coat.menu_item("ToggleUI") # Toggle Popup/Docked Windows
   if coat.menu_hotkey("TAB", 0, 0, 0):
        if not coat.lock_ui_changes():
            coat.menu_separator()
            coat.menu_item("CustomizeUI") # Customize UI
 
   coat.menu_insert_extensions("Windows")