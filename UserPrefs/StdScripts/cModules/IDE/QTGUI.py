# The simplest program - just show the Hello world!
import sys
import time
#from decord import VideoReader
#from decord import cpu, gpu
import os

import coat

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QUrl, Slot, Qt, QByteArray, QThread
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import (QApplication, QLineEdit,
    QMainWindow, QPushButton, QToolBar, QDockWidget, QTabWidget, QTabBar)
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
import threading
import time


# def startQTAppThread():
#     global app
#     app = QApplication.instance()
#     if app is None:
#         app = QApplication([])
#     for k in range(1000):
#         app.processEvents()
#     app.quit()

class qt_gui_events(coat.GlobalEvent):
    def __init__(self):
        coat.GlobalEvent.__init__(self)
        coat.GlobalEvent.begin_work_in_bg()
        # self.QTAppThread = threading.Thread(target=startQTAppThread)
        # self.QTAppThread.start()
        global app
        app = QApplication.instance()
    
    def pre_process(self):
        global app
        # if app is None:
        #     app = QApplication([])

        if app is not None:
            app.instance().processEvents()



# startQTAppThread()

qt_gui = qt_gui_events()

qt_gui.Activate()
# time.sleep(1)
# sys.exit()
