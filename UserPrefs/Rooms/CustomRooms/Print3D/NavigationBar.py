import coat
from cTemplates.Structs import *
from cTemplates.navigation import *
import cTemplates.navigation
from cTemplates.Rooms import reg_navigation_bar

@reg_navigation_bar
def PrintNavigationBar():
    pass    


PrintNavigationBar.Content.append(Light)
PrintNavigationBar.Content.append(Camera)
PrintNavigationBar.Content.append(ViewPort)
PrintNavigationBar.Content.append(Grid)
PrintNavigationBar.Content.append(View)

@d_child(PrintNavigationBar)
def PrintViewPortMenu():
    if coat.iconic_submenu("Camera4", 32):
        PrintViewPortMenu.IncludeContent()
        coat.menu_exit()

PrintViewPortMenu.Content.append(S_edit_navi)
PrintViewPortMenu.Content.append(cTemplates.navigation.Background)
PrintViewPortMenu.Content.append(cTemplates.navigation.CameraSnapping)
PrintViewPortMenu.Content.append(S_ViewSide)
PrintViewPortMenu.Content.append(S_Presets)
PrintViewPortMenu.Content.append(S_Pivot)

