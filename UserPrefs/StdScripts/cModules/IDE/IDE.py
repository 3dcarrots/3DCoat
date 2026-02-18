import sys

import os
import time
import cPy.cCore
import cPy.cIDE
import coat

DEBUG = True

if(DEBUG):
    DEBUG_PORT = '5588'
    DEBUG_URL = 'http://127.0.0.1:%s' % DEBUG_PORT
    os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = DEBUG_PORT


from PySide6 import QtCore, QtGui
from PySide6.QtCore import QUrl, Slot, Qt, QByteArray, QThread, QMetaObject
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton, QToolBar, QDockWidget, QTabWidget, QTabBar)
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from cModules.QT import QT

import threading
import time

ide_file_path = __file__

# def thread_function(browser: QWebEnginePage, aWindow:QMainWindow):
#     global lastPingTime
#     global gShow
#     for line in sys.stdin:
#         logger.info("IN: "+line)
#         lastPingTime = round(time.time() * 1000)
#         if "<{close}>" in line:
#             gShow = False
#         else:
#             if "<{CML_PING}>" in line:
#                 lastPingTime = round(time.time() * 1000)
#             else:
#                 if "<{SHOW}>" in line:
#                     logger.info("SHOW")
#                     availableGeometry = aWindow.screen().availableGeometry()
#                     logger.info("SHOW: Window size:")
#                     showArgs = line.split(" ")
#                     if len(showArgs) > 1:
#                         logger.info(showArgs[1])
#                         iSize = showArgs[1].split("x")
#                         aWindow.resize(int(iSize[0]), int(iSize[1]))
#                     else:
#                         logger.info("SHOW: not defined")
#                         aWindow.resize(availableGeometry.width() * 2 / 3+1, availableGeometry.height() * 2 / 3+1)
#                     if (len(showArgs) > 2) and (showArgs[2] == "StayOnTop"):
#                         logger.info("SHOW: StayOnTop")
#                         aWindow.setWindowFlags(aWindow.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
#                     if len(showArgs) > 3:
#                         aWindow.setWindowTitle(showArgs[3])
#                     gShow = True
#                 else:
#                     logger.info("SET SOURCE")
#                     runJavaScriptQueue.append(line)
#                     #webEngineView.page().runJavaScript("MessageFrom3DCoat('"+line.replace("'", "&apos;").replace("\n", " ")+"');")
#                     logger.info("SET SOURCE FINISH")



class MainWindow(QMainWindow):
    textChanged = QtCore.Signal(str)
    iStayOnTop = False
    scriptSource: cPy.cIDE.cHostScriptSource = None

    def AddMenuItem(self, aMenu, aName, aIcon, aShorcut, aStatusTip, aAction):
        nAction = QtGui.QAction(QtGui.QIcon("icons/"+aIcon), aName, self)
        nAction.setShortcut(aShorcut)
        nAction.setStatusTip(aStatusTip)
        nAction.triggered.connect(aAction)        
        aMenu.addAction(nAction)
        return nAction

    def AddMenuItemCM(self, aMenu, aName, aIcon, aShorcut, aStatusTip, aCommand):
        self.AddMenuItem(aMenu, aName, aIcon, aShorcut, aStatusTip, lambda: self.CMLEditor.runJavaScript('editor.execCommand("'+aCommand+'")'))

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
            self.scriptSource.IsOpennedInEditor = False
        else:
            event.ignore()
    

    def __init__(self):
        global DEBUG
        global gShow
        global gClose
        global lastPingTime
        super().__init__()

        self.m_text = ""

        # Globals
        # self.logger = _logging.getLogger("CMLEditor.py")

        self.lastPingTime = round(time.time() * 1000)
        self.iLoop: int = 0


        self.gShow: bool = False
        self.gClose: bool = False
        self.webEngineView: QWebEngineView

        self.runJavaScriptQueue = []
        self.runJavaScriptFinished: int = 0
        ##########################################################################
        ##########################################################################

        sshFile=os.fspath(os.path.dirname(os.path.realpath(ide_file_path)) + "\CMLEditorUI.css")
        with open(sshFile,"r") as fh:
            QT.app.setStyleSheet(fh.read())

        if len(sys.argv) > 2:
            self.setWindowTitle(sys.argv[2])
        else:
            self.setWindowTitle('NGL Editor')

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


        global webEngineView
        webEngineView = QWebEngineView()
        #webEngineView.loadFinished.connect(self.myLoadFin)
        webEngineView.setStyleSheet("background-color: #111;")
        #webEngineView.setVisible(False)
        
        self.setCentralWidget(webEngineView)

        #htmlFileName = os.fspath(os.path.dirname(os.path.realpath(ide_file_path)) + "/temp.html")
        htmlFileName = os.fspath(os.path.dirname(os.path.realpath(ide_file_path)) + "/CMLEditor.html")
        self.channel.registerObject("cml_editor", self)
        webEngineView.page().setWebChannel(self.channel)
        webEngineView.load( QUrl.fromLocalFile(htmlFileName))
        #webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.CMLEditor = webEngineView.page()
        #self.channel.registerObject("code_editor", webEngineView)
        #self.channel.registerObject("code_editor_page", webEngineView.page())

        ## DevTools Inspector
        if(DEBUG):
            self.inspector_dock = QDockWidget("DevTools", self)
            self.inspector_dock.setVisible(False)
            self.inspector_dock.setMinimumWidth(400)
            self.inspector = QWebEngineView(self.inspector_dock)
            self.inspector.page().setWebChannel(self.channel)
            self.inspector.load(QtCore.QUrl(DEBUG_URL))
            self.inspector_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
            self.inspector_dock.setWidget(self.inspector)
            self.addDockWidget(Qt.RightDockWidgetArea, self.inspector_dock)
            self.inspector_dock.toggleViewAction().setStatusTip("Show devTools")
            #self.channel.registerObject("inspector_dock", self.inspector_dock)
            #self.channel.registerObject("inspector", self.inspector)
            #self.channel.registerObject("inspector_page", self.inspector.page())
            helpMenu.addAction(self.inspector_dock.toggleViewAction())

        ## HotKeys
        hotkeysFileName = os.fspath(os.path.dirname(os.path.realpath(ide_file_path)) + "/hotkeys.html")
        self.hotkeys_page_dock = QDockWidget("HotKeys", self)
        self.hotkeys_page_dock.setVisible(False)
        self.hotkeys_page_dock.setMinimumWidth(400)
        self.hotkeys_page = QWebEngineView(self.hotkeys_page_dock)
        self.hotkeys_page.page().setWebChannel(self.channel)
        self.hotkeys_page.load( QUrl.fromLocalFile(hotkeysFileName))
        self.hotkeys_page_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.hotkeys_page_dock.setWidget(self.hotkeys_page)
        self.addDockWidget(Qt.RightDockWidgetArea, self.hotkeys_page_dock)
        self.hotkeys_page_dock.toggleViewAction().setStatusTip("Display a list of editor commands and hotkeys")
        #self.channel.registerObject("hotkeys_dock", self.hotkeys_page_dock)
        #self.channel.registerObject("hotkeys", self.hotkeys_page)
        #self.channel.registerObject("hotkeys_page", self.hotkeys_page.page())
        helpMenu.addAction(self.hotkeys_page_dock.toggleViewAction())

        ## Documentation
        #docFileName = os.fspath(os.path.dirname(os.path.realpath(ide_file_path)) + "/glslDoc/index.html")
        docFileName = os.fspath(os.path.dirname(os.path.realpath(ide_file_path)) + "/docs.html")
        self.documentation_page_dock = QDockWidget("Documentation", self)
        self.documentation_page_dock.setVisible(False)
        self.documentation_page_dock.setMinimumWidth(400)
        self.documentation_page = QWebEngineView(self.documentation_page_dock)
        self.documentation_page.page().setWebChannel(self.channel)
        self.documentation_page.load( QUrl.fromLocalFile(docFileName))
        self.documentation_page_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.documentation_page_dock.setWidget(self.documentation_page)
        self.addDockWidget(Qt.RightDockWidgetArea, self.documentation_page_dock)
        self.documentation_page_dock.toggleViewAction().setStatusTip("Display a list of editor commands and hotkeys")
        #self.channel.registerObject("documentation_dock", self.documentation_page_dock)
        #self.channel.registerObject("documentation", self.documentation_page)
        #self.channel.registerObject("documentation_page", self.documentation_page.page())
        helpMenu.addAction(self.documentation_page_dock.toggleViewAction())

        ####
        if(DEBUG):
            #self.hotkeys_page.page().setDevToolsPage(self.inspector.page())
            #self.documentation_page.page().setDevToolsPage(self.inspector.page())
            webEngineView.page().setDevToolsPage(self.inspector.page())
            self.tabifyDockWidget(self.documentation_page_dock, self.inspector_dock)

        self.tabifyDockWidget(self.documentation_page_dock, self.hotkeys_page_dock)

        ####
        self.AddMenuItem(fileMenu, '&Exit', 'exit.png', 'Ctrl+Q', 'Exit application', self.close)
        self.cbStayOnTop = self.AddMenuItem(fileMenu, '&StayOnTop', 'up.png', 'Alt+Q', 'Stay on top', self.changeStayOnTop)
        self.cbStayOnTop.setCheckable(True)
        ####
        self.AddMenuItemCM(editMenu, '&Undo', 'undo.png', 'Ctrl+Z', 'Undo last action', "undo")
        self.AddMenuItemCM(editMenu, '&Redo', 'redo.png', 'Ctrl+Y', 'Redo last action', "redo")
        editMenu.addSeparator()
        self.AddMenuItemCM(editMenu, '&Find', 'find.png', 'Ctrl+F', 'Find text in the source code', "find")
        self.AddMenuItemCM(editMenu, '&FindNext', 'down.png', 'Shift+Ctrl+G', 'Find next', "findNext")
        self.AddMenuItemCM(editMenu, '&FindPrev', 'up.png', 'Shift+Ctrl+F', 'Search up text', "findPrev")
        self.AddMenuItemCM(editMenu, '&Replace', 'replace.png', 'Shift+Ctrl+H', 'Replace text in the source code', "replace")
        self.AddMenuItemCM(editMenu, '&ReplaceAll', 'replace_all.png', 'Shift+Ctrl+R', 'Replace all in the source code', "replaceAll")

        ####

        # self.thread = QThread()

        # inOutThread = threading.Thread(target=thread_function, args=(webEngineView.page(),self))
        # inOutThread.daemon = True
        # inOutThread.start()

        # lastPingTime = round(time.time() * 1000)

        # timer = QtCore.QTimer(self)
        # timer.timeout.connect(self.on_timeout)
        # timer.start(50)

        # logger.info("NEED SHOW COMMAND")
        # while (not gShow) and (not gClose):
        #     app.processEvents()
        #     if gClose: print("gclose")

        # if not gClose:
        #     self.show()
        #     #self.setFocus(Qt.ActiveWindowFocusReason)
        #     self.activateWindow()
        #     self.raise_()

        #if gClose: 
        #    raise SystemExit()


    #@Slot()
    #def myLoadFin(self):
 
    # def on_timeout(self):
    #     self.text  = QtCore.QDateTime.currentDateTime().toString()
    #     global iLoop
    #     global gClose
    #     #global gShow
    #     global webEngineView
        
    #     global runJavaScriptQueue
    #     global runJavaScriptFinished
    #     if runJavaScriptFinished < len(runJavaScriptQueue):
    #         line = runJavaScriptQueue[runJavaScriptFinished]
    #         webEngineView.page().runJavaScript("MessageFrom3DCoat('"+line.replace("'", "&apos;").replace("\n", " ")+"');")
    #         runJavaScriptFinished += 1

        
    #     #webEngineView.page().runJavaScript("MessageFrom3DCoat('<{SET_SOURCE}><{br}>in color AlbedoColor;<{br}>Material myMTL;<{br}>myMTL.ioAlbedoColor = AlbedoColor;<{br}>myMTL.ioAlbedoColor *= 1.0;<{br}>ioMTL.ioAlbedoColor = myMTL.ioAlbedoColor;');")        
    #     if len(sys.argv) <= 1 or sys.argv[1] != "stay":
    #         iLoop = iLoop+1
    #         #if iLoop > 2 and round(time.time() * 1000) - lastPingTime > 60000: # and gShow:
    #             #print("Close2")
    #             #raise SystemExit()

    @Slot(str)
    def SaveCML(self, html):
        #f = open(os.path.dirname(os.path.realpath(ide_file_path))+"/tmp.cml", "w")
        #f.write(html)
        #f.close()
        #logger.info(" CML_RESULT_UPDATE "+html+" UPDATE_RESULT_CML ")        
        # logger.info(" CML_RESULT_UPDATE "+html+" UPDATE_RESULT_CML ")        
        # time.sleep(0)
        if(self.scriptSource.getSource() != html):
            self.scriptSource.setSource(html)
            self.scriptSource.OnChange()


    @Slot(str)
    def ShowCMLHelp(self, aWord):
        if os.path.exists(os.path.dirname(os.path.realpath(ide_file_path))+"/glslDoc/"+aWord+".html"):
            self.documentation_page.page().runJavaScript("document.getElementById('docs').src='glslDoc/"+aWord+".html';")
            self.documentation_page_dock.setVisible(True)
            self.documentation_page_dock.focusWidget()
            self.documentation_page_dock.activateWindow()
            for bar in self.findChildren(QTabBar):
                count = bar.count()
                for i in range(count):
                    tName = bar.tabText(i)
                    if tName == self.documentation_page_dock.windowTitle():
                        bar.setCurrentIndex(i)


    def getText(self):
        return self.m_text

    def setText(self, text):
        if self.m_text == text:
            return
        self.m_text = text
        self.textChanged.emit(self.m_text)

    text = QtCore.Property(str, getText, setText, notify=textChanged)




class CoatIDE(cPy.cIDE.cIDE):
    def __init__(self):
        cPy.cIDE.cIDE.__init__(self)
        self.mainWin = MainWindow()
        # for k in range(1000000):
        #     app.processEvents()

        # self.QTAppThread = threading.Thread(target=startQTAppThread)
        # self.QTAppThread.start()
        #mainWin.setStyleSheet("background-color: #111;")
        #sys.exit(app.exec())

    def EditSource(self, scriptSource):
        # coat.dialog().text(scriptSource.FilePath.ToCharPtr()).ok().show()
        cPy.cCore.cExtension.begin_work_in_bg()
        self.mainWin.scriptSource = scriptSource
        self.mainWin.show()
        self.mainWin.raise_()
        for k in range(10000):
            QT.app.processEvents()
        src = self.mainWin.scriptSource.getSource().replace("'", "&apos;").replace("\n", "<{br}>").replace("\r", " ")
        webEngineView.page().runJavaScript("SetSource('"+src+"');")
        self.mainWin.scriptSource.IsOpennedInEditor = True

    def sendMessage(self, scriptSource, message): 
        # webEngineView.page().runJavaScript("SetSource('"+src+"');")    
        webEngineView.page().runJavaScript("MessageFrom3DCoat('"+message.replace("'", "&apos;").replace("\n", " ").replace("\r", " ")+"');")



class IdeExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)
        self.coat_IDE = CoatIDE()
        cPy.cIDE.cIDE.SetDefaultIDE(self.coat_IDE)

    def onExit(self):
        self.coat_IDE.mainWin.deleteLater()



ideExtension = IdeExtension()
# class ideExtension: 


# if __name__ == '__main__':
    # coat_IDE = CoatIDE()
    # coat.cPy.cIDE.SetDefaultIDE(coat_IDE)
    # global app
    # app = QApplication.instance()
    # global app
    # app = QApplication.instance()
    # if app is None:
    # app = QApplication([])
    # app.exec()
    #app.exit()
    #raise SystemExit()

# quit()

# class qt_proc(coat.cThread):
#     def __init__(self):
#         coat.cThread.__init__(self)

#     def process(self):
#         app = QApplication.instance()
#         if app is None:
#             app = QApplication([])
#         self.mainWin = MainWindow()
#         self.mainWin.show()
#         while True:
#             app.processEvents()



# if __name__ == '__main__':
#     print("BEGIN")
#     logger.setLevel(_logging.DEBUG)
#     stream_handler = _logging.StreamHandler()
#     formatter = _logging.Formatter("[%(filename)s] %(message)s")
#     stream_handler.setFormatter(formatter)
#     logger.addHandler(stream_handler)
#     logger.info("INITCMLEDITOR")


