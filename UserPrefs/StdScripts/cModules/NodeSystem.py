import __future__
import coat
import cPy.cCore


class ExtensionManager(cPy.cCore.ExtensionManager):
    """
    this is extension manager
    """
    def __init__(self):
        self.NeedReloadSomeModules = False
        cPy.cCore.ExtensionManager.__init__(self)





extensionManager = ExtensionManager()

cPy.cCore.ExtensionManager.SetExtensionManager(extensionManager)