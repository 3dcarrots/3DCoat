import cPy.cCore
import gc
import time
from PySide6.QtCore import QEvent
from PySide6.QtCore import QUrl
from cModules.QT.__onstartup import *
import shiboken6
import cPy.cIDE
from PySide6.QtCore import QTimer

class QTExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)


    def preprocess(self):
        global app
        app.processEvents()

    def postprocess(self):
        global app
        app.processEvents()

    def prerender(self):
        global app
        app.processEvents()

    def postrender(self):
        global app
        app.processEvents()

    def onExit(self):
        global app
        cPy.cIDE.PythonTerminal.Set(cPy.cIDE.DefaultTerminal.defaultTerminal)

        app.closeAllWindows() 

        app.processEvents()

        all_widgets = QApplication.allWidgets()
        
        for widget in all_widgets:
            if not shiboken6.isValid(widget):
                continue

            try:
                if widget.inherits("QWebEngineView") or widget.metaObject().className() == 'QWebEngineView':
                    widget.stop()
                    widget.load(QUrl("about:blank"))
                    
                    page = widget.page()
                    if shiboken6.isValid(page):
                        widget.setPage(None)
                        page.deleteLater()
                    
                    widget.close()
                    widget.deleteLater()
            except Exception:
                pass

        # for widget in QApplication.topLevelWidgets():
        #     if shiboken6.isValid(widget):
        #         widget.close()
        #         widget.deleteLater()

        for _ in range(10):
            app.sendPostedEvents(None, QEvent.Type.DeferredDelete)
            app.processEvents()
            time.sleep(0.01)

        QTimer.singleShot(0, app.quit)
        app.exec()


        app.quit()
        
        del app
        gc.collect()


qtExtension = QTExtension()

