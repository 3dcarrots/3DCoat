import os
import sys
import subprocess
import cPy.cCore
import coat
import cTemplates.Structs
from cPy.cCore import cExtension

# Define path for local dependencies within the extension folder
EXTENSION_DIR = os.path.dirname(os.path.abspath(__file__))
LIBS_DIR = os.path.join(EXTENSION_DIR, "libs")

def ensure_dependencies():
    """Ensure required packages are installed in the local libs directory."""
    if not os.path.exists(LIBS_DIR):
        os.makedirs(LIBS_DIR)
        
    if LIBS_DIR not in sys.path:
        sys.path.insert(0, LIBS_DIR)
        
    required_packages = ["google-genai", "mcp", "sounddevice", "numpy", "markdown", "pygments"]
    missing_packages = []
    
    for pkg in required_packages:
        try:
            if pkg == "google-genai":
                __import__("google.genai")
            else:
                __import__(pkg)
        except ImportError:
            missing_packages.append(pkg)
            
    if missing_packages:
        print(f"[VoiceAIAssistant] Installing missing dependencies: {', '.join(missing_packages)}...")
        python_exe = sys.executable
        
        # Determine actual package names for pip
        pip_packages = [pkg for pkg in missing_packages]
                
        try:
            # Since sys.executable is 3DCoat.exe, using subprocess will launch a new 3DCoat instance!
            # Use pip programmatically instead.
            import pip
            if hasattr(pip, 'main'):
                pip.main(['install', '--target', LIBS_DIR] + pip_packages)
            else:
                from pip._internal import main as pipmain
                pipmain(['install', '--target', LIBS_DIR] + pip_packages)
            print("[VoiceAIAssistant] Dependencies installed successfully.")
        except Exception as e:
            print(f"[VoiceAIAssistant] Failed to install dependencies: {e}")

# Inject libs into sys.path immediately upon import
if os.path.exists(LIBS_DIR) and LIBS_DIR not in sys.path:
    sys.path.insert(0, LIBS_DIR)

class VoiceAIAssistantExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)
        self.ui_instance = None
        self.is_active = False
        cExtension.begin_work_in_bg()

    def onStart(self):
        print("VoiceAIAssistant started. Ensuring dependencies...")
        ensure_dependencies()
        
        # Now we can safely import them
        self.init_ui()
        self.is_active = True
        
    def init_ui(self):
        # We handle UI creation safely to ensure PySide6 runs well with 3DCoat
        try:
            from .ui import VoiceAIAssistantUI
            self.ui_instance = VoiceAIAssistantUI()
            self.ui_instance.show()
        except ImportError as e:
            print(f"[VoiceAIAssistant] Failed to load UI module: {e}")

    def onExit(self):
        print("VoiceAIAssistant stopped.")
        if self.ui_instance:
            self.ui_instance.close()
            self.ui_instance = None
        self.is_active = False

# Required for 3DCoat to load the extension
voiceAIAssistantExtension = VoiceAIAssistantExtension()

# Register a menu item to explicitly toggle our window, under "Extensions"
@cTemplates.Structs.d_slot
def ShowVoiceAIAssistantUI():
    if voiceAIAssistantExtension.ui_instance:
        if voiceAIAssistantExtension.ui_instance.isHidden():
            voiceAIAssistantExtension.ui_instance.show()
        else:
            voiceAIAssistantExtension.ui_instance.raise_()
            voiceAIAssistantExtension.ui_instance.activateWindow()
    else:
        print("[VoiceAIAssistant] Extension is not active. Please start it from Extensions menu.")

import cTemplates.MainMenu.Edit
@cTemplates.Structs.d_menu_section(cTemplates.MainMenu.Edit.CreateEditMenu)
def AISection():
    coat.menu_item(ShowVoiceAIAssistantUI.UICmd())

