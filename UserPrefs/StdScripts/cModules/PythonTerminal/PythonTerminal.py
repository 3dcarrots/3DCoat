import sys
import os

import cPy.cCore
import cPy.cIDE

from cModules.PythonTerminal import PythonTerminalExt

class PythonTerminalExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)
        self.pythonTerminal = PythonTerminalExt.PythonTerminal()
        self.pythonTerminal.cExtension = self
        cPy.cIDE.PythonTerminal.Set(self.pythonTerminal)

    def onStartup(self):
        self.pythonTerminal.OnActivate()
    
    def postprocess(self):
        return self.pythonTerminal.postprocess()
    
    

pythonTerminalExtension = PythonTerminalExtension()


