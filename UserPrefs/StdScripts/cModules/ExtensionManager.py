import __future__
import coat
import cPy.cCore
import os
import sys
import CMD
import cPy.Legacy
import cPy.cIDE
import cPy.cNodeSystem
import time
import threading

import cModules.ModuleReloader
import cTemplates.Structs
import runpy
import math
import re

try:
    import pkg_resources
except ImportError:
    pkg_resources = None

def dict_from_module(module):
    context = {}
    for setting in dir(module):
        context[setting] = getattr(module, setting)

    return context

cmd_mmembs = dict_from_module(CMD)
cmd_mmembs["sphere"] = cPy.Legacy.sphere1
cmd_mmembs["ellipse"] = cPy.Legacy.mk_ellipse
cmd_mmembs["cube"] =  cPy.Legacy.mk_cube
cmd_mmembs["cylinder"] = cPy.Legacy.mk_cylinder
cmd_mmembs["cone"] = cPy.Legacy.mk_cone
cmd_mmembs["ngon"] = cPy.Legacy.mk_ngon
cmd_mmembs["tube"] = cPy.Legacy.mk_tube
cmd_mmembs["ngontube"] = cPy.Legacy.mk_ngontube
cmd_mmembs["capsule"] = cPy.Legacy.mk_capsule
cmd_mmembs["prim"] = cPy.Legacy.mk_prim
cmd_mmembs["merge"] = cPy.Legacy.merge1
cmd_mmembs["vertexpaint"] = cPy.Legacy.vertexpaint1
cmd_mmembs["autopo"] = cPy.Legacy.autopo1
cmd_mmembs["uv"] = cPy.Legacy.activate_uv
cmd_mmembs["__open"] = cPy.Legacy.__open
cmd_mmembs["open"] = cPy.Legacy.__open


cmd_mmembs["coat"] = coat
cmd_mmembs["cCore"] = cPy.cCore
cmd_mmembs["cIDE"] = cPy.cIDE
cmd_mmembs["cNodeSystem"] = cPy.cNodeSystem
cmd_mmembs["os"] = os
cmd_mmembs["sys"] = sys
cmd_mmembs["CMD"] = CMD

cmd_mmembs["true"] = True
cmd_mmembs["false"] = False


for name in dir(math):
    if not name.startswith('__'):  
        attr = getattr(math, name)
        cmd_mmembs[name] = attr

def ExecActionByIdx(action_idx):
    cTemplates.Structs._action_list[action_idx]()


def ModuleWatcher():
    pass
    # while(True):
    #     time.sleep(0.1)
    #     extensionManager.GetLoadedModulesInfo()
    #     time.sleep(0.1)
    #     for i in range(10):
    #         time.sleep(0.75)
    #         if cPy.cCore.ExtensionManager.AutoReloadModules():
    #             for mds in cModules.ModuleReloader.LoadedModulesList:
    #                 if mds.UpdateModTimeAndSize():
    #                     extensionManager.NeedReloadSomeModules = True
    #                 time.sleep(0.001)

 
class ExtensionManager(cPy.cCore.ExtensionManager):
    """
    this is extension manager
    """
    def __init__(self):
        self.NeedReloadSomeModules = False
        cPy.cCore.ExtensionManager.__init__(self)

        ModuleWatcherThread = threading.Thread(target=ModuleWatcher)
        ModuleWatcherThread.start()        

    def CheckIfMuduleInList(self, mName: str):
        for m in cModules.ModuleReloader.LoadedModulesList:
            if m.modulePath == mName:
                return True
        return False
        

    def GetLoadedModulesInfo(self):
        for md in sys.modules:
            if not self.CheckIfMuduleInList(md):
                instFolder  = cPy.cCore.cExtension.getCoatInstallForder()
                if ("cModules" in md) or ("cTemplates" in md):
                    mdToFile = md.replace(".", "/")
                    filePath = instFolder + "/UserPrefs/StdScripts/"+mdToFile+".py"
                    filePath = filePath.replace("\\", "/")
                    filePath = filePath.replace("//", "/")
                    if os.path.isfile(filePath):
                            # print(filePath)
                            # print(md)
                            mfu = cModules.ModuleReloader.ModuleFilesUpdaterInfo()
                            mfu.filePath = filePath
                            mfu.modulePath = md
                            mfu.UpdateModTimeAndSize()
                            mfu.Changed = False
                            cModules.ModuleReloader.LoadedModulesList.append(mfu)

                if ("CustomRooms" in md):
                    mdToFile = "UserPrefs/Rooms/"+md.replace(".", "/")+".py"
                    if coat.CheckIfExists(mdToFile):
                        filePath = coat.io.documents(mdToFile)
                        filePath = filePath.replace("\\", "/")
                        filePath = filePath.replace("//", "/")
                        if os.path.isfile(filePath):
                            # print(filePath)
                            # print(md)
                            mfu = cModules.ModuleReloader.ModuleFilesUpdaterInfo()
                            mfu.filePath = filePath
                            mfu.modulePath = md
                            mfu.UpdateModTimeAndSize()
                            mfu.Changed = False
                            cModules.ModuleReloader.LoadedModulesList.append(mfu)

                if ("cExtensions" in md):
                    mdToFile = "UserPrefs/Scripts/"+md.replace(".", "/")+".py"
                    if coat.CheckIfExists(mdToFile):
                        filePath = coat.io.documents(mdToFile)
                        filePath = filePath.replace("\\", "/")
                        filePath = filePath.replace("//", "/")
                        if os.path.isfile(filePath):
                            # print(filePath)
                            # print(md)
                            mfu = cModules.ModuleReloader.ModuleFilesUpdaterInfo()
                            mfu.filePath = filePath
                            mfu.modulePath = md
                            mfu.UpdateModTimeAndSize()
                            mfu.Changed = False
                            cModules.ModuleReloader.LoadedModulesList.append(mfu)

            # for mp in sys.path:
            #     if "UserPrefs" in mp:
            #         if ("Scripts" in mp) or ("StdScripts" in mp) or ("Rooms" in mp):
            #             print(mp)

            #             for root, dirs, files in os.walk(mp):
            #                 for file in files:
            #                     if file.endswith(".py"):
            #                         pfile = os.path.join(root, file)
            #                         print(pfile)

            #                         fSize = os.path.getsize(pfile)
            #                         print(fSize)
            #                         mTime = os.path.getmtime(pfile)
            #                         print(mTime)


    def Expression(self, source):
        global cmd_mmembs
        if not isinstance(source, str):
            return source

        stripped_text = source.strip()

        if stripped_text.startswith("PY:"):
            code_body = stripped_text[3:].strip()
            
            if "return " in code_body:
                try:
                    lines = [line.strip() for line in code_body.split(';') if line.strip()]
                    
                    indented_body = "\n".join(f"    {line}" for line in lines)
                    
                    func_source = f"def _temp_isolated_func():\n{indented_body}"
                    
                    local_scope = {}
                    exec(func_source, cmd_mmembs, local_scope)
                    
                    return str(local_scope['_temp_isolated_func']())
                    
                except Exception as e:
                    print(f"Error in PY block: {e}") 
                    return source
            else:
                try:
                    return str(eval(code_body, cmd_mmembs))
                except Exception as e:
                    print(f"Error in PY block: {e}") 
                    return source

        math_pattern = r'^[\d\s\+\-\*\/\(\)\.]+$'
        if re.match(math_pattern, stripped_text):
            try:
                return str(eval(stripped_text))
            except Exception:
                return source

        return source

    def OnProcess(self):
        if self.NeedReloadSomeModules:
            for mds in cModules.ModuleReloader.LoadedModulesList:
                if mds.Changed:
                    mds.Reload()

    def ExecScript(self, script):
        """
        exec python script from string
        """
        exec(script, globals())
        return True

    def ExecByIdx(self, action_idx):
        """
        exec python function made usind d_slot
        """
        ExecActionByIdx(action_idx)

    def RunPy(self, file_path):
        start_time = time.time()

        abs_path = coat.io.toFullPathInInstallFolder(file_path)
        print("<b>RUN:</B> "+file_path)
        globals()["__file__"] = file_path


        file_dir = os.path.dirname(os.path.abspath(file_path))

        contains_path = True 
        if file_dir not in sys.path:
            sys.path.append(file_dir)
            contains_path = False


        with open(abs_path, 'r', encoding='utf-8') as f:
            code_string = f.read()
            annotations_flag = __future__.annotations.compiler_flag
            code_object = compile(code_string, abs_path, 'exec', flags=annotations_flag)
            exec(code_object, globals())


        globals()["__file__"] = ""
        if not contains_path:
            sys.path.remove(file_dir)
        print("exec time: %s seconds" % (time.time() - start_time))

        return True

    def OnImport(self, module):
        pass
        # print("import module "+module)

    def ReloadChangedModules(self):
        print("Reload Changed Modules")
        if not cPy.cCore.ExtensionManager.AutoReloadModules():
            self.GetLoadedModulesInfo()

        for mfu in cModules.ModuleReloader.LoadedModulesList:
            if mfu.UpdateModTimeAndSize():
                mfu.Reload()
                
    def Command(self, command):
        global cmd_mmembs
        start_time = time.time()
        print("<b>CMD:</b> "+command)
        as2py = ExtensionManager.CommandToPy(command)
        pyhtml = as2py.replace(" ", "&nbsp;")
        print("<b>PY:</b> \n"+pyhtml)
        print("convert time: %s seconds" % (time.time() - start_time))
        # as2py = command.replace("  ", " ").replace("; ", ";").replace(";", "\n").replace("\n ", "\n")
        start_time = time.time()
        exec(as2py, cmd_mmembs)
        print("exec time: %s seconds" % (time.time() - start_time))
        return True

    def Exec(self, cmd):
        exec(cmd)
        
    def RefreshInstalledList(self):
        if pkg_resources != None:
            self.ClearInstalledPyModuleList()
            installed_packages = pkg_resources.working_set
            for i in installed_packages:
                self.AddInstalledPyModule(i.key)
                #TODO: i.version




extensionManager = ExtensionManager()

cPy.cCore.ExtensionManager.SetExtensionManager(extensionManager)