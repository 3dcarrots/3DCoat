from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication

import coat

import ctypes
from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QApplication, QWidget

class Global3DCoatCursorFixer(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.h_arrow = ctypes.windll.user32.LoadCursorW(0, 32512)

    def eventFilter(self, obj, event):
        if not isinstance(obj, QWidget) or not obj.isWindow():
            return False

        if event.type() == QEvent.Enter:
            self.force_show_cursor(obj)
            
        elif event.type() == QEvent.Leave or event.type() == QEvent.Close:
            self.restore_cursor(obj)

        return False

    def force_show_cursor(self, window_obj):
        if getattr(window_obj, "_cursor_is_fixed", False):
            return

        ctypes.windll.user32.SetCursor(self.h_arrow)

        depth = 0
        loop_guard = 0
        
        while loop_guard < 50:
            count = ctypes.windll.user32.ShowCursor(True)
            depth += 1
            if count >= 0:
                break
            loop_guard += 1

        window_obj._cursor_fix_depth = depth
        window_obj._cursor_is_fixed = True

    def restore_cursor(self, window_obj):
        if not getattr(window_obj, "_cursor_is_fixed", False):
            return

        depth = getattr(window_obj, "_cursor_fix_depth", 0)
        
        while depth > 0:
            ctypes.windll.user32.ShowCursor(False)
            depth -= 1

        window_obj._cursor_fix_depth = 0
        window_obj._cursor_is_fixed = False

#app = QApplication()
app = QApplication(["-no-opengl"])


if not hasattr(QApplication, "_cursor_fixer_instance"):
    fixer = Global3DCoatCursorFixer()
    QApplication.instance().installEventFilter(fixer)
    QApplication._cursor_fixer_instance = fixer


QApplication.setAttribute(QtCore.Qt.AA_UseDesktopOpenGL, True)
# app.setAttribute(QtCore.AA_UseOpenGLES); 
app.processEvents()