
# Place this file in Documents\3DCoat\UserPrefs\Scripts\cExtensions\MouseTest\MouseTest.py so that it appears in 3DCoat's list of extensions in the "Extensions" window.
import coat
import CMD
import coat.cCore
import coat.cRender

from cTemplates.Structs import *
import cTemplates.MainMenu.View


# A variable that determines whether to show or hide information about the mouse and cursor.
ShowMouseInfo = True

# The function that will be called when a menu item is clicked. We use the d_slot dicatorator to get a command that calls it for the coat.menu_item function.
@d_slot
def ToggleMouseInfo():
    global ShowMouseInfo
    ShowMouseInfo = not ShowMouseInfo

# Create a separate section for our extension in the View menu.
@d_menu_section(cTemplates.MainMenu.View.CreateViewMenu)
def MouseInfoSection():
    # Add a menu item to this section that will enable and disable information about the mouse and cursor.
    coat.menu_item(ToggleMouseInfo.UICmd()) 


#############################################################################################################
# Create our extension class; in order for it to work correctly, it must be inherited from coat.cCore.cExtension #
class MouseTestExtension(coat.cCore.cExtension):

    def __init__(self):
        coat.cCore.cExtension.__init__(self)        

    # Rewrite the inherited "postrender" function, which will be called every time after rendering to display our information on the screen.
    def postrender(self):
        # Display information only if ShowMouseInfo is True
        if not ShowMouseInfo:
            return
        
        # display information about the mouse and cursor as text on the viewport.
        coat.cRender.RenderUtils.draw_text(300, 200, f"Cursor pos: {coat.io.cursorPos().x}, {coat.io.cursorPos().y}") #cursor pos (variant 1)
        coat.cRender.RenderUtils.draw_text(300, 230, f"Cursor pos: {CMD.GetMouseX()}, {CMD.GetMouseY()}")#cursor pos (variant 2)

        coat.cRender.RenderUtils.draw_text(300, 290, f"Left mouse button: {CMD.LMBPressed()}")
        coat.cRender.RenderUtils.draw_text(300, 320, f"Middle mouse button: {CMD.MMBPressed()}")
        coat.cRender.RenderUtils.draw_text(300, 350, f"Right mouse button: {CMD.RMBPressed()}")
        coat.cRender.RenderUtils.draw_text(300, 380, f"Wheel pressed: {CMD.WheelPressed()}")

        coat.cRender.RenderUtils.draw_text(300, 410, f"Screen space pen radius: {CMD.GetVisiblePenRadius()}")

        coat.cRender.RenderUtils.draw_text(300, 440, f"Picks Object: {CMD.ScreenRayPicksObject(CMD.GetMouseX(), CMD.GetMouseY())}")

        # If the cursor is hovering over an object, we draw a sphere on the object and display the 3D coordinates of the point the cursor is hovering over.
        if CMD.ScreenRayPicksObject(CMD.GetMouseX(), CMD.GetMouseY()):

            # Find out the 3D coordinates of the point the cursor is hovering over.
            pickPos: coat.vec3 = coat.cRender.RenderUtils.PickPointSpacePos()

            # draw a sphere
            coat.cRender.RenderUtils.drawCoolSphere(pickPos, 10.0, int("FF00FFFF", 16))

            # Displaying 3D coordinates as text in the viewport
            mx = CMD.GetMouseX()
            my = CMD.GetMouseY()
            coat.cRender.RenderUtils.draw_text(mx, my, " 3D Coord")
            coat.cRender.RenderUtils.draw_text(mx, my+30, f" X: {pickPos.x}")
            coat.cRender.RenderUtils.draw_text(mx, my+60, f" Y: {pickPos.y}")
            coat.cRender.RenderUtils.draw_text(mx, my+90, f" Z: {pickPos.z}")



# Create an extension (an instance of the class that will perform the work of our extension).
myMouseTestExtension = MouseTestExtension()

