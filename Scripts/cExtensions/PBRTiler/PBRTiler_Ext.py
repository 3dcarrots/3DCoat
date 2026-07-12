import cPy.cCore
import coat
from cTemplates.Structs import *
import cTemplates.MainMenu.Scripts

from PySide6.QtWidgets import QApplication
import sys

# We keep a global reference to the window so it doesn't get garbage collected
active_window = None

@d_slot
def OpenPBRTiler():
    global active_window
    
    # Needs to ensure QApplication exists
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
        
    try:
        from .TilerMainWindow import TilerMainWindow
        
        if active_window is None:
            active_window = TilerMainWindow()
            
        active_window.show()
        active_window.raise_()
        active_window.activateWindow()
        
    except Exception as e:
        print(f"Error launching PBRTiler: {e}")

@d_menu_section(cTemplates.MainMenu.Scripts.ScriptsMenu)
def PBRTilerSection():
    coat.menu_item(OpenPBRTiler.UICmd())

class PBRTilerExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)

    def onStart(self):
        print("PBRTiler extension initialized.")
        
    def preprocess(self):
        global active_window
        if active_window and hasattr(active_window, 'renderer'):
            active_window.renderer.poll_render()

    def onExit(self):
        global active_window
        if active_window:
            active_window.close()
            active_window = None
        print("PBRTiler extension exited.")

pbrTilerExtension = PBRTilerExtension()
