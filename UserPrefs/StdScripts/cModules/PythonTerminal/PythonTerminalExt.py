import sys

import os
import time
import cPy.cCore
import cPy.cIDE
import coat


from PySide6 import QtCore, QtGui
from PySide6.QtCore import QUrl, Slot, Qt, QByteArray, QThread, QMetaObject
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton, QToolBar, QDockWidget, QTabWidget, QTabBar)
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineCore import QWebEngineSettings
from cModules.QT import QT

from time import gmtime, strftime
import timeit

import time
import pydoc

PCExt_file_path = __file__



def SendSafeStr(source):
    return source.replace("'", "<{&apos;}>").replace("\n", "<{<br />}>").replace("\r", "").replace("\\", "\\\\")

def SendSafeHtml(source):
    return source.replace("'", "&apos;").replace("\n", "<br />").replace("\\", "\\\\")

lastHelpDataObj = None
lastDataSearchTarget = ""
lastDataSearchVarPath = ""
lastDataSearchResult = ""

mainWindow = None

class MainWindow(QMainWindow):
    textChanged = QtCore.Signal(str)
    iStayOnTop = False
    scriptSource: cPy.cIDE.cHostScriptSource = None

    @Slot(str)
    def PyInputLine(self, lineIn):
        cPy.cIDE.PTRecord.add(">>", "", lineIn)
        for i in range(100):
            QT.app.processEvents()
            self.pythonTerminal.postprocess()
        self.pythonTerminal.ApplyBuf(False)
        exec(lineIn, globals())
        for i in range(100):
            QT.app.processEvents()
            self.pythonTerminal.postprocess()
        self.pythonTerminal.ApplyBuf(False)
        # self.pythonTerminal.cExtension.evalPy(lineIn)
        # PTEvalPy.PTEvalPy(lineIn)
        # eval(lineIn)


    @Slot(str)
    def AutoComplete(self, var_path):
        global lastDataSearchVarPath, lastDataSearchTarget, lastHelpDataObj
        pathItems = var_path.split('.')
        
        if lastDataSearchTarget == "PyEditor":
            self.scripting_page.page().runJavaScript("AutoComplete('"+pathItems[-1]+"')")

        if lastDataSearchTarget == "input":
            self.webEngineView.page().runJavaScript("AutoComplete('"+pathItems[-1]+"')")


    @Slot(str)
    def ShowDoc(self, var_path):
        global lastDataSearchVarPath, lastDataSearchTarget, lastHelpDataObj
        pathItems = var_path.split('.')

        curObjP = None
        curObj = globals()

        iError = False
        try:
            for keyObj in pathItems:
                if keyObj in curObj.keys():
                    curObjP = curObj[keyObj]
                    curObjDir = dir(curObj[keyObj])
                    curObj = vars(curObj[keyObj])
                else:
                    iError = True
        except:
            iError = True

        try:
            QT.app.processEvents()
            if lastHelpDataObj != curObjP:
                # strhelp = pydoc.render_doc(curObjP, renderer=pydoc.plaintext)
                strhelp = pydoc.render_doc(curObjP, renderer=pydoc.html)
                strhelp = strhelp.replace("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","&nbsp;&nbsp;")
                strhelp = strhelp.replace("#ffffff","#999")
                strhelp = strhelp.replace("#000000","#321")
                strhelp = strhelp.replace('href="','href="#')
                strhelp = strhelp.replace('href="##','href="#')
                strhelp = strhelp.replace('color="#321"','color="#987"')
                
                
                self.help_page.page().runJavaScript("ShowData('"+SendSafeStr(strhelp)+"')")
                lastHelpDataObj = curObjP
                QT.app.processEvents()
                # with open("d:/pyDoc.html", "w") as text_file:
                #     text_file.write(strhelp)      
        except:
            pass

    @Slot(str)
    def DataSearch(self, var_path, targ, showDoc = True):
        global lastDataSearchVarPath, lastDataSearchTarget, lastHelpDataObj, lastDataSearchResult
        if len(var_path) < 1: 
            return
        if len(targ) < 4: 
            return
        
        global mainWindow
        if lastDataSearchVarPath != var_path:
            mainWindow.data_browser_page.page().runJavaScript("window.scrollTo(0, 0)")

        lastDataSearchTarget = targ
        lastDataSearchVarPath = var_path

        memberIdx = 0
        pathItems = var_path.split('.')

        curObjP = None
        curObj = globals()
        curObjDir = globals().keys()

        iError = False
        nPath = ""
        try:
            for keyObj in pathItems:
                    if keyObj != pathItems[-1]:
                        if keyObj in curObj.keys():
                            curObjP = curObj[keyObj]
                            curObjDir = dir(curObj[keyObj])
                            curObj = vars(curObj[keyObj])
                            nPath += keyObj + "."
                        else:
                            iError = True
        except:
            iError = True

        resultList = "<table style=\"width: 100%\">"
        oddRow = False            
        for key in curObjDir:
            oddRow = not oddRow
            rowClass = "evenRow"
            if oddRow:
                rowClass = "oddRow"
            srcKey = pathItems[-1].lower()
            if srcKey in key.lower() or len(srcKey) == 0:
                try:
                    value = ""
                    valueType = ""

                    iSepVT = " : "

                    piObj = None

                    if key in curObj:
                        piObj = curObj[key]

                    if curObjP != None:
                        piObj = getattr(curObjP, key)

                    if piObj != None:
                        value = str(piObj)
                        valueType = str(type(piObj).__name__)
                        
                        if "method" in valueType or "function" in valueType:
                            valueType = pydoc.render_doc(piObj, renderer=pydoc.plaintext)
                            iLines = valueType.splitlines()
                            valueType = ""
                            for iL in range(len(iLines)):
                                iLine = iLines[iL]
                                if iL == 0:
                                    valueType += '<div class="intOf">'+iLine+'</div>'
                                else: 
                                    if "(" in iLine and ")" in iLine:
                                        valueType += '<div class="code">'+iLine+'</div>'
                                        iSepVT = ""
                                        value = ""
                                    else:
                                        valueType += '<div class="desc">'+iLine+'</div>'
                    iPath = nPath+key

                    resultList += "<tr id=\"member"+str(memberIdx)+"\" onclick=\"py_console.AutoComplete('"+iPath+"')\" onmouseenter=\"py_console.ShowDoc('"+iPath+"')\" class=\""+rowClass+"\"><td><b>" + str(key) + "</b></td><td><pre>" + str(value) + iSepVT+valueType+"</pre></td></tr>"
                    memberIdx += 1
                except:
                    pass

        resultList += "</table>"
        result = SendSafeStr(resultList)
        if lastDataSearchResult != result:
            lastDataSearchResult = result
            mainWindow.data_browser_page.page().runJavaScript("ShowData('"+result+"')")

        if showDoc:
            self.ShowDoc(var_path)
        # with open("d:/pyDoc.html", "w") as text_file:
        #     text_file.write(resultList)      

        # globals()
        # globals().keys()
        # pydoc.render_doc(help, renderer=pydoc.plaintext)
        # strhelp = pydoc.render_doc(str, "Help on %s")

    def DataSearchUpdate(self):
        global lastDataSearchVarPath, lastDataSearchTarget, lastHelpDataObj
        self.DataSearch(lastDataSearchVarPath, lastDataSearchTarget, False)

    @Slot(str)
    def DataSearchInput(self, var_path):
        self.DataSearch(var_path, "input")

    @Slot(str)
    def DataSearchEditor(self, var_path):
        self.DataSearch(var_path, "PyEditor")

    def AddMenuItem(self, aMenu, aName, aIcon, aShorcut, aStatusTip, aAction):
        nAction = QtGui.QAction(QtGui.QIcon("icons/"+aIcon), aName, self)
        nAction.setShortcut(aShorcut)
        nAction.setStatusTip(aStatusTip)
        nAction.triggered.connect(aAction)        
        aMenu.addAction(nAction)
        return nAction

    def AddMenuItemCM(self, aMenu, aName, aIcon, aShorcut, aStatusTip, aCommand):
        self.AddMenuItem(aMenu, aName, aIcon, aShorcut, aStatusTip, lambda: self.scripting_page.page().runJavaScript('editor.execCommand("'+aCommand+'")'))

    def changeStayOnTop(self):
        self.iStayOnTop = not self.iStayOnTop
        self.cbStayOnTop.setChecked(self.iStayOnTop)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, on=self.iStayOnTop)
        self.show()

    def closeEvent(self, event):
        can_exit = True
        if can_exit:
            event.accept() # let the window close
            cPy.cCore.cExtension.end_work_in_bg()
        else:
            event.ignore()
    

    def __init__(self):
        global gShow
        global gClose
        global lastPingTime
        super().__init__()

        global mainWindow
        mainWindow = self


        self.m_text = ""

        # Globals
        # self.logger = _logging.getLogger("ConsolOutContent.py")

        self.lastPingTime = round(time.time() * 1000)
        self.iLoop: int = 0


        self.gShow: bool = False
        self.gClose: bool = False

        self.runJavaScriptQueue = []
        self.runJavaScriptFinished: int = 0
        ##########################################################################
        ##########################################################################

        sshFile=os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/UI.css")
        with open(sshFile,"r") as fh:
            QT.app.setStyleSheet(fh.read())

        if len(sys.argv) > 2:
            self.setWindowTitle(sys.argv[2])
        else:
            self.setWindowTitle('Python Console')

        self.setTabPosition(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea, QTabWidget.TabPosition.North)
        self.setDocumentMode(True)
        #self.DockOption.ForceTabbedDocks = True
        #####################

        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        helpMenu = menubar.addMenu('&Help')

        self.channel = QWebChannel(self)

        #self.channel.registerObject("main_menu", menubar)
        #self.channel.registerObject("menu_file", fileMenu)
        #self.channel.registerObject("menu_edit", editMenu)
        #self.channel.registerObject("menu_help", helpMenu)
        #self.channel.registerObject("status_bar", self.statusBar())


        self.webEngineView = QWebEngineView()
        #self.webEngineView.loadFinished.connect(self.myLoadFin)
        self.webEngineView.setStyleSheet("background-color: #111;")
        #self.webEngineView.setVisible(False)
        
        self.setCentralWidget(self.webEngineView)

        #htmlFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/temp.html")
        htmlFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/TerminalOut.html")
        self.channel.registerObject("py_console", self)
        self.webEngineView.page().setWebChannel(self.channel)
        self.webEngineView.load( QUrl.fromLocalFile(htmlFileName))
        #self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.ConsolOutContent = self.webEngineView.page()
        #self.channel.registerObject("code_editor", self.webEngineView)
        #self.channel.registerObject("code_editor_page", self.webEngineView.page())


        ## HotKeys
        hotkeysFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/hotKeys.html")
        self.hotkeys_page_dock = QDockWidget("HotKeys", self)
        self.hotkeys_page_dock.setVisible(False)
        self.hotkeys_page_dock.setMinimumWidth(400)
        self.hotkeys_page = QWebEngineView(self.hotkeys_page_dock)
        self.hotkeys_page.page().setWebChannel(self.channel)
        self.hotkeys_page.load( QUrl.fromLocalFile(hotkeysFileName))
        self.hotkeys_page_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.hotkeys_page_dock.setWidget(self.hotkeys_page)
        self.addDockWidget(Qt.RightDockWidgetArea, self.hotkeys_page_dock)
        self.hotkeys_page_dock.toggleViewAction().setStatusTip("Display a list of editor commands and hotkeys")
        #self.channel.registerObject("hotkeys_dock", self.hotkeys_page_dock)
        #self.channel.registerObject("hotkeys", self.hotkeys_page)
        #self.channel.registerObject("hotkeys_page", self.hotkeys_page.page())
        helpMenu.addAction(self.hotkeys_page_dock.toggleViewAction())


        ## documentation
        documentationFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/docs.html")
        self.documentation_page_dock = QDockWidget("documentation", self)
        self.documentation_page_dock.setVisible(False)
        self.documentation_page_dock.setMinimumWidth(400)
        self.documentation_page = QWebEngineView(self.documentation_page_dock)
        self.documentation_page.settings().setAttribute( QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.documentation_page.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        self.documentation_page.page().setWebChannel(self.channel)
        self.documentation_page.load( QUrl.fromLocalFile(documentationFileName))
        self.documentation_page_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.documentation_page_dock.setWidget(self.documentation_page)
        self.addDockWidget(Qt.RightDockWidgetArea, self.documentation_page_dock)
        self.documentation_page_dock.toggleViewAction().setStatusTip("Display a list of editor commands and documentation")
        #self.channel.registerObject("documentation_dock", self.documentation_page_dock)
        #self.channel.registerObject("documentation", self.documentation_page)
        #self.channel.registerObject("documentation_page", self.documentation_page.page())
        helpMenu.addAction(self.documentation_page_dock.toggleViewAction())

        ## help
        helpFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/help.html")
        self.help_page_dock = QDockWidget("help", self)
        self.help_page_dock.setVisible(True)
        self.help_page_dock.setMinimumWidth(400)
        self.help_page = QWebEngineView(self.help_page_dock)
        self.help_page.settings().setAttribute( QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.help_page.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        self.help_page.page().setWebChannel(self.channel)
        self.help_page.load( QUrl.fromLocalFile(helpFileName))
        self.help_page_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.help_page_dock.setWidget(self.help_page)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.help_page_dock)
        self.help_page_dock.toggleViewAction().setStatusTip("Help for selected object")
        #self.channel.registerObject("help_dock", self.help_page_dock)
        #self.channel.registerObject("help", self.help_page)
        #self.channel.registerObject("help_page", self.help_page.page())
        helpMenu.addAction(self.help_page_dock.toggleViewAction())

        ## data_browser
        data_browserFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/data_browser.html")
        self.data_browser_page_dock = QDockWidget("data_browser", self)
        self.data_browser_page_dock.setVisible(True)
        self.data_browser_page_dock.setMinimumWidth(300)
        self.data_browser_page = QWebEngineView(self.data_browser_page_dock)
        self.data_browser_page.settings().setAttribute( QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.data_browser_page.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        self.data_browser_page.page().setWebChannel(self.channel)
        self.data_browser_page.load( QUrl.fromLocalFile(data_browserFileName))
        self.data_browser_page_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.data_browser_page_dock.setWidget(self.data_browser_page)
        self.addDockWidget(Qt.RightDockWidgetArea, self.data_browser_page_dock)
        self.data_browser_page_dock.toggleViewAction().setStatusTip("Display a list of editor commands and data_browser")
        #self.channel.registerObject("data_browser_dock", self.data_browser_page_dock)
        #self.channel.registerObject("data_browser", self.data_browser_page)
        #self.channel.registerObject("data_browser_page", self.data_browser_page.page())
        helpMenu.addAction(self.data_browser_page_dock.toggleViewAction())

        self.AddMenuItem(editMenu, "&NextMember", "arrow_right.png", "Alt+Down", "Next member", lambda: self.data_browser_page.page().runJavaScript('NextMember()'))
        self.AddMenuItem(editMenu, "&PreviousMember", "arrow_left.png", "Alt+Up", "Previous member", lambda: self.data_browser_page.page().runJavaScript('PreviousMember()'))
        self.AddMenuItem(editMenu, "&AutoComplete", "check_box.png", "Alt+Return", "Auto complete", lambda: self.data_browser_page.page().runJavaScript('AutoComplete()'))


        ## Documentation
        #docFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/glslDoc/index.html")
        docFileName = os.fspath(os.path.dirname(os.path.realpath(PCExt_file_path)) + "/PyEditor.html")
        self.scripting_page_dock = QDockWidget("Scripting", self)
        self.scripting_page_dock.setVisible(True)
        self.scripting_page_dock.setMinimumWidth(400)
        self.scripting_page = QWebEngineView(self.scripting_page_dock)
        self.scripting_page.page().setWebChannel(self.channel)
        self.scripting_page.load( QUrl.fromLocalFile(docFileName))
        self.scripting_page_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.scripting_page_dock.setWidget(self.scripting_page)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.scripting_page_dock)
        self.scripting_page_dock.toggleViewAction().setStatusTip("Display a list of editor commands and hotkeys")
        #self.channel.registerObject("documentation_dock", self.scripting_page_dock)
        #self.channel.registerObject("documentation", self.scripting_page)
        #self.channel.registerObject("scripting_page", self.scripting_page.page())
        helpMenu.addAction(self.scripting_page_dock.toggleViewAction())


        # self.tabifyDockWidget(self.scripting_page_dock, self.hotkeys_page_dock)

        ####
        self.AddMenuItem(fileMenu, '&Exit', 'exit.png', 'Ctrl+Q', 'Exit application', self.close)
        self.cbStayOnTop = self.AddMenuItem(fileMenu, '&StayOnTop', 'up.png', 'Alt+Q', 'Stay on top', self.changeStayOnTop)
        self.cbStayOnTop.setCheckable(True)
        ####
        self.AddMenuItemCM(editMenu, '&Undo', 'undo.png', 'Ctrl+Z', 'Undo last action', "undo")
        self.AddMenuItemCM(editMenu, '&Redo', 'redo.png', 'Ctrl+Y', 'Redo last action', "redo")
        # self.AddMenuItemCM(editMenu, '&Exec', 'script.png', 'Ctrl+Return', 'Run script', "Exec")
        self.AddMenuItem(editMenu, '&Exec', 'script.png', 'Ctrl+Return', 'Run script', lambda: self.scripting_page.page().runJavaScript('RunScript()'))

        editMenu.addSeparator()
        self.AddMenuItemCM(editMenu, '&Find', 'find.png', 'Ctrl+F', 'Find text in the source code', "find")
        self.AddMenuItemCM(editMenu, '&FindNext', 'down.png', 'Shift+Ctrl+G', 'Find next', "findNext")
        self.AddMenuItemCM(editMenu, '&FindPrev', 'up.png', 'Shift+Ctrl+F', 'Search up text', "findPrev")
        self.AddMenuItemCM(editMenu, '&Replace', 'replace.png', 'Shift+Ctrl+H', 'Replace text in the source code', "replace")
        self.AddMenuItemCM(editMenu, '&ReplaceAll', 'replace_all.png', 'Shift+Ctrl+R', 'Replace all in the source code', "replaceAll")


WorkingInBackGround: bool = False
class PythonTerminal(cPy.cIDE.PythonTerminal):
    def __init__(self):
        cPy.cIDE.PythonTerminal.__init__(self)
        self.mainWin: MainWindow = MainWindow()
        self.stdOut = cPy.cIDE.PythonTerminalOut()
        self.stdOut.TypeName = "stdOut"
        self.stdErr = cPy.cIDE.PythonTerminalOut()
        self.stdErr.TypeName = "stdErr"
        self.lastTime = 0
        self.lastMsgType = ""
        self.messageBuf: str = ""
        self.codeBuf: str = ""
        self.lastTime = 0
        self.mainWin.pythonTerminal = self
        self.LastMessagePyTime = timeit.default_timer()


    def OnRunScript(self):
        sys.stdout = self.stdOut
        sys.stderr = self.stdErr

    def OnActivate(self):
        sys.stdout = self.stdOut
        sys.stderr = self.stdErr
	
    def OnShow(self):
        # if not self.mainWin.isVisible:
        global WorkingInBackGround

        if not WorkingInBackGround:
            cPy.cCore.cExtension.begin_work_in_bg()
            WorkingInBackGround = True
        self.mainWin.show()
        self.mainWin.raise_()
        


    def ApplyBuf(self, replace_last):        
        if len(self.messageBuf) == 0 and len(self.codeBuf) == 0:
            return
        
        if self.lastMsgType == "stdErr" and "PythonTerminal.py" in self.messageBuf and "exec(source)" in self.messageBuf:
            if ', line 1, in' in self.messageBuf:
                self.messageBuf = self.messageBuf.split(', line 1, in')[-1]
            else:
                if ', line 1' in self.messageBuf:
                    self.messageBuf = self.messageBuf.split(', line 1')[-1]
                else:
                    if ', line 0, in' in self.messageBuf:
                        self.messageBuf = self.messageBuf.split(', line 0, in')[-1]
                    else:
                        if ', line 0' in self.messageBuf:
                            self.messageBuf = self.messageBuf.split(', line 0')[-1]

        msgStr = SendSafeStr(self.messageBuf)
        codeStr = SendSafeStr(self.codeBuf)

        rpLast = "false"
        if replace_last:
            rpLast = "true"

        if self.lastMsgType == "PinJS":
            self.mainWin.ConsolOutContent.runJavaScript("showPin('"+msgStr+"', "+ str(self.lastTime) +")")
            self.mainWin.ConsolOutContent.runJavaScript(self.codeBuf)
        else:
            self.mainWin.ConsolOutContent.runJavaScript("PushMessage('"+msgStr+"', '"+codeStr+"', '"+ self.lastMsgType +"', "+ str(self.lastTime) +", "+rpLast+")")
        self.messageBuf = ""
        self.codeBuf = ""

        if self.lastMsgType == "stdErr" or  self.lastMsgType == "ERROR":
            self.mainWin.show()
            self.mainWin.raise_()
        

    def OnMessage(self, type_name, message, aCode, message_time, replace_last):
        if len(message) == 0 and len(aCode) == 0:
            return

        self.LastMessagePyTime = timeit.default_timer()

        if self.lastTime != message_time or self.lastMsgType != type_name:
            self.ApplyBuf(False)

        self.lastMsgType = type_name
        self.messageBuf += message
        self.codeBuf += aCode
        self.lastTime = message_time
        if (type_name != "stdErr" and  type_name != "stdOut") or replace_last or (len(message) > 0 and len(aCode) > 0):
            self.ApplyBuf(replace_last)
        
    lastUpdateData = 0
    def postprocess(self):
        if timeit.default_timer() - self.LastMessagePyTime > 0.030:
            self.ApplyBuf(False)

        if timeit.default_timer() - self.lastUpdateData > 0.5:
            self.lastUpdateData = timeit.default_timer()
            if mainWindow.iStayOnTop and mainWindow.isVisible(): 
                mainWindow.DataSearchUpdate()
            self.ApplyBuf(False)
            global WorkingInBackGround
            if not self.mainWin.isVisible():
                if WorkingInBackGround:
                    cPy.cCore.cExtension.end_work_in_bg()
                    WorkingInBackGround = False

            if self.mainWin.isVisible():
                if not WorkingInBackGround:
                    cPy.cCore.cExtension.begin_work_in_bg()
                    WorkingInBackGround = True


