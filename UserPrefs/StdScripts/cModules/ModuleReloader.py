import coat
import cPy.cCore
import os
import sys
import time
import threading
from importlib import reload 
import inspect


ReloadModuleList = list()
LoadedModulesList = list()

class ModuleFilesUpdaterInfo:
    filePath: str = ""
    modulePath: str = ""
    fileSize: int = 0
    ModifiedTime: float = 0
    Changed: bool = False

    def Reload(self):
        # print("RELOAD MODULE: " + self.modulePath)
        ReloadModuleList.clear()
        self.Changed = False
        exec("import "+self.modulePath+"\nfrom cModules.ModuleReloader import ReloadModule\nReloadModule("+self.modulePath+")",globals())
        self.UpdateModTimeAndSize()
        self.Changed = False
        # inspect.ismodule(os)
        # pt.PythonTerminalExt.__spec__.name
        # for i in dir(my_Module): 
        #     print (i,":  ", getattr(my_Module,i))


    def UpdateModTimeAndSize(self):
        changed = False
        
        fSize = os.path.getsize(self.filePath)
        if fSize != self.fileSize: 
            self.fileSize = fSize
            changed = True
        # print(self.fileSize)
        # print(fSize)
        
        mTime = os.path.getmtime(self.filePath)
        if mTime != self.ModifiedTime: 
            changed = True
            self.ModifiedTime = mTime
        # print(self.ModifiedTime)
        # print(mTime)
        if changed:
            self.Changed = True
        return changed


def findModuleByPath(module, module_path, module_path_str, pidx):

    joined_path = ""
    for i in range(pidx):
        joined_path = joined_path + module_path[i] + "."
    
    joined_path = joined_path + module_path[pidx]
    # print(joined_path)
    for i in dir(module):
        if inspect.ismodule(getattr(module, i)):
            refmod = getattr(module, i)
            # print("TEST: " + module_path[pidx] + " == " +refmod.__spec__.name)
            if refmod.__spec__.name == module_path_str:
                return True

            

            if refmod.__spec__.name == module_path[pidx] or refmod.__spec__.name == joined_path:
                if pidx < len(module_path)-1:
                    if findModuleByPath(refmod, module_path, module_path_str, pidx+1):
                        return True
                else:
                    return True
                    
    return False

def ReloadModule(p_module):
    if inspect.ismodule(p_module):
        print("RELOAD MODULE: " + p_module.__spec__.name)
        reload(p_module)
        
        mPathItems = p_module.__spec__.name.split(".")

        for rmdl in LoadedModulesList:
            # print(rmdl.modulePath)
            if "CustomRooms" in rmdl.modulePath:
                if not (rmdl.modulePath in ReloadModuleList):
                
                    # print("CustomRooms")
                    rmod = sys.modules[rmdl.modulePath]

                    if findModuleByPath(rmod, mPathItems, p_module.__spec__.name, 0):
                        ReloadModuleList.append(rmdl.modulePath)
                        ReloadModule(rmod)
                        cPy.cCore.CustomRoom.RefreshInterface()
                    # iNeedReload = False

                    # pidx = 0
                    # nextModItem = rmod
                    # while pidx < len(mPathItems):
                    #     nx = False
                    #     for i in dir(rmod):
                    #         if inspect.ismodule(getattr(rmod, i)):
                    #             refmod = getattr(rmod, i)
                    #             print("TEST: " + mPathItems[pidx] + " == " +refmod.__spec__.name)
                    #             if refmod.__spec__.name == mPathItems[pidx]:
                    #                 nx = True
                    #     if nx:
                    #         pidx += 1
                    #     else:
                    #         pidx = len(mPathItems)+2

                    # if pidx == len(mPathItems):
                    #     print("NeedReload")
                    #     ReloadModuleList.append(rmod)
                    #     ReloadModule(rmod)
                    ##################################################
                    ##################################################
                    # for i in dir(p_module):
                    #     if inspect.ismodule(getattr(p_module,i)):
                    #         mdl = getattr(p_module,i)
                    #         print("NEED RELOAD MODULE: " + mdl.__spec__.name)
                    #         if not (mdl in ReloadModuleList):
                    #             if "CustomRooms" in mdl.__spec__.name:
                    #                 ReloadModule(p_module)

