
import cPy
import coat

import importlib

from cTemplates.Structs import *
import cTemplates.MainMenu.Scripts

@d_slot
def RebuildDocumentation():
    sphinx_builder = importlib.import_module("cModules.DocBuilder.sphinx_builder")
    sphinx_builder.main()

# Create a separate section for our extension in the View menu.
@d_menu_section(cTemplates.MainMenu.Scripts.Scripts_S_Useful)
def MouseInfoSection():
    # Add a menu item to this section that will enable and disable information about the mouse and cursor.
    coat.menu_item(RebuildDocumentation.UICmd()) 

class DocBuilderExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)

docBuilderExtension = DocBuilderExtension()

