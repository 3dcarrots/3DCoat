import coat
import cPy.cCore
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PySide6.QtGui import QImage, QPixmap, QColorSpace, QPainter
from PySide6.QtCore import QTimer, Qt
import sys

# Ensure QApplication exists for PySide6
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

class FlippedImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self._qimage = None

    def paintEvent(self, event):
        if self._qimage is not None:
            painter = QPainter(self)
            painter.scale(1, -1)
            # Translate up by the ACTUAL height of the FBO image, not the current widget's height. 
            # This correctly anchors the upside-down OpenGL FBO to the Top-Left of the window!
            painter.translate(0, -self._qimage.height())
            
            # Draw the image in its native resolution without stretching
            painter.drawImage(0, 0, self._qimage)
            painter.end()
        else:
            super().paintEvent(event)


class PyWindowsManager(cPy.cCore.WindowsManager):
    def __init__(self, target_widget, ext):
        super().__init__()
        
        try:
            cPy.cCore.cExtension.begin_work_in_bg()
        except Exception:
            pass
            
        self.target_widget = target_widget
        self.ext = ext
        self.window = QMainWindow()
        self.window.setWindowTitle(f"3DCoat Popup: {target_widget}")
        
        from PySide6.QtWidgets import QWidget, QVBoxLayout
        central = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(0)
                
        self.label = FlippedImageLabel()
        self.label.setMinimumSize(1, 1)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.label)
        
        central.setLayout(layout)
        self.window.setCentralWidget(central)
        
        try:
            rect = self.GetWidgetScreenRect(target_widget)
            if rect and len(rect) == 4 and rect[2] > 0 and rect[3] > 0:
                x, y, w, h = rect
                # Add a little extra width/height for margins
                self.window.setGeometry(x, y, w + 8, h + 8)
            else:
                self.window.resize(300, 300)
        except Exception:
            self.window.resize(300, 300)

        self.window.setStyleSheet("background-color: #353535;")
        self.label.setMouseTracking(True)
        
        # Focus tracking for blocking native input
        self.window.setFocusPolicy(Qt.StrongFocus)
        self.label.setFocusPolicy(Qt.StrongFocus)
        
        def window_focus_in(event):
            try:
                self.SetBlockNativeInput(True)
            except Exception:
                pass
            
        def window_focus_out(event):
            try:
                self.SetBlockNativeInput(False)
            except Exception:
                pass
                
        def window_close(event):
            try:
                self.SetBlockNativeInput(False)
            except Exception:
                pass
            
            try:
                cPy.cCore.cExtension.end_work_in_bg()
            except Exception:
                pass
            
            try:
                pw = cPy.cCore.PopupWindow.Find(self.target_widget)
                if pw:
                    pw.Visible = True
            except Exception:
                pass
                
            self.current_widget = ""

        self.window.focusInEvent = window_focus_in
        self.window.focusOutEvent = window_focus_out
        self.window.closeEvent = window_close
        
        # Override mouse events
        self.label.mousePressEvent = self.on_mouse_press
        self.label.mouseMoveEvent = self.on_mouse_move
        self.label.mouseReleaseEvent = self.on_mouse_release
        self.label.leaveEvent = self.on_mouse_leave
        self.label.wheelEvent = self.wheelEvent
        self.window.keyPressEvent = self.keyPressEvent
        
        # Hook resize event to redraw FBO dynamically during resize drag
        self._original_resize = self.window.resizeEvent
        def custom_resize(event):
            self._original_resize(event)
            if hasattr(self, 'current_widget') and self.current_widget:
                self.process_frame()
        self.window.resizeEvent = custom_resize
        
        # Select target widget inside 3DCoat
        self.current_widget = ""
        self.fboID = -1
        
        # Ensure rendering pipeline ticks even when Qt events stop (e.g. holding window border)
        self.render_timer = QTimer()
        self.render_timer.timeout.connect(self.process_frame)
        self.render_timer.start(16) # ~60fps
        
        # Pre-allocate Reusable Image Buffers to enable True Zero-Allocation
        # Double buffering prevents Qt from accessing a dangling pointer if the window is resized
        import Coat_CPP
        self.img_buffers = [Coat_CPP.cImage(), Coat_CPP.cImage()]
        self.current_buffer_idx = 0

    def OnUndockToQt(self, widgetName):
        if widgetName != self.target_widget:
            return
            
        self.current_widget = widgetName
        
        # Hide the native widget so 3DCoat native loop doesn't render it 
        # and overwrite its cached CanvasRect with global coordinates!
        try:
            pw = cPy.cCore.PopupWindow.Find(widgetName)
            if pw:
                pw.Visible = False
        except Exception as e:
            pass
            
        self.window.show()
        self.window.raise_()
        self.window.activateWindow()

    def get_scaled_coordinates(self, x, y):
        # We need to map (x, y) from the visual QLabel size back to the native FBO resolution
        if not hasattr(self, "_last_pixels") or self._last_pixels is None:
            return int(x), int(y)
        
        # Native FBO size
        fbo_h, fbo_w, _ = self._last_pixels.shape
        
        # Label size
        lbl_w = self.label.width()
        lbl_h = self.label.height()
        
        if lbl_w == 0 or lbl_h == 0:
            return int(x), int(y)
            
        scaled_x = int(x * (fbo_w / lbl_w))
        scaled_y = int(y * (fbo_h / lbl_h))
        return scaled_x, scaled_y

    def _show_qt_input(self, wid, cls_name, x, y, bx, by, bw, bh, val_str=""):
        if not hasattr(self, 'qt_input'):
            from PySide6.QtWidgets import QLineEdit
            self.qt_input = QLineEdit(self.label)
            self.qt_input.editingFinished.connect(self._on_qt_input_finished)
            # Add a bit of style to make it match 3DCoat roughly
            self.qt_input.setStyleSheet("QLineEdit { background: #333; color: white; border: 1px solid #555; }")
        
        self.active_input_wid = wid
        self.active_input_cls = cls_name
        
        import coat
        
        if cls_name in ("SimpleSlider", "SimpleSliderH"):
            try:
                # Format to drop trailing zeros from C++ std::to_string
                val_str = f"{float(val_str):g}"
            except ValueError:
                pass

        try:
            self.qt_input.setText(val_str)
        except Exception as e:
            with open("E:/3dcoat_qt_debug.txt", "a") as f:
                f.write(f"_show_qt_input exception 1: {e}\n")
            self.qt_input.setText("")

        fbo_h, fbo_w, _ = self._last_pixels.shape if hasattr(self, "_last_pixels") and self._last_pixels is not None else (1, 1, 3)
        lbl_w = self.label.width()
        lbl_h = self.label.height()
        
        if fbo_w > 0 and fbo_h > 0:
            scale_x = lbl_w / fbo_w
            scale_y = lbl_h / fbo_h
        else:
            scale_x = 1.0
            scale_y = 1.0
            
        final_x = int(bx * scale_x)
        final_y = int(by * scale_y)
        final_w = int(bw * scale_x)
        final_h = int(bh * scale_y)
        
        try:
            self.qt_input.setGeometry(final_x, final_y, final_w, final_h)
            self.qt_input.raise_()
            self.qt_input.show()
            self.qt_input.setFocus()
            self.qt_input.selectAll()
        except Exception as e:
            print(f"_show_qt_input exception: {e}")
        self.qt_input.selectAll()

    def _on_qt_input_finished(self):
        if not hasattr(self, 'qt_input') or not self.qt_input.isVisible():
            return
            
        wid = self.active_input_wid
        cls_name = self.active_input_cls
        text = self.qt_input.text()
        self.qt_input.hide()
        
        try:
            import coat
            success = False
            if wid and len(wid) > 0:
                if cls_name in ("SimpleSlider", "SimpleSliderH"):
                    try:
                        success = coat.ui.setSliderValue(wid, float(text))
                    except ValueError:
                        success = coat.ui.setEditBoxValue(wid, text)
                else:
                    success = coat.ui.setEditBoxValue(wid, text)
                    
            if not success:
                # Fallback to direct coordinate injection if Coat API fails or ID is missing
                self.InjectWidgetValue(self.current_widget, self.active_input_x, self.active_input_y, text)
        except Exception as e:
            print(f"Failed to inject value into widget {wid}: {e}")

    def on_mouse_press(self, event):
        try:
            self.SetBlockNativeInput(True)
        except Exception:
            pass
            
        x, y = self.get_scaled_coordinates(event.position().x(), event.position().y())
        btn = event.button()
        flags = 1 if (event.buttons() & Qt.LeftButton) else 0
        
        self.input_intercepted = False
        if btn == Qt.LeftButton:
            try:
                wid, is_editable, cls_name, bx, by, bw, bh, val_str = self.GetEditableWidgetAt(self.current_widget, x, y)
            except Exception as e:
                print(f"GetEditableWidgetAt EXCEPTION: {e}")
                is_editable = False
                
            if is_editable:
                self.input_intercepted = True
                try:
                    self.active_input_x = x
                    self.active_input_y = y
                    self._show_qt_input(wid, cls_name, x, y, bx, by, bw, bh, val_str)
                except Exception as e:
                    print(f"on_mouse_press CRASH when showing input: {e}")
                return
                
            if hasattr(self, 'qt_input') and self.qt_input.isVisible():
                self.qt_input.clearFocus()
                
            self.InjectMouseEvent(self.current_widget, 513, x, y, flags)
            self.mouse_pressed = True
        elif btn == Qt.RightButton:
            self.InjectMouseEvent(self.current_widget, 516, x, y, flags)

    def on_mouse_move(self, event):
        x, y = self.get_scaled_coordinates(event.position().x(), event.position().y())
        flags = 1 if (event.buttons() & Qt.LeftButton) else 0
        self.InjectMouseEvent(self.current_widget, 512, x, y, flags)

    def on_mouse_release(self, event):
        x, y = self.get_scaled_coordinates(event.position().x(), event.position().y())
        btn = event.button()
        flags = 1 if (event.buttons() & Qt.LeftButton) else 0
        if btn == Qt.LeftButton:
            self.InjectMouseEvent(self.current_widget, 514, x, y, flags)
            self.mouse_pressed = False
        elif btn == Qt.RightButton:
            self.InjectMouseEvent(self.current_widget, 517, x, y, flags)

    def on_mouse_leave(self, event):
        # When mouse leaves PySide QLabel, send a far-off coordinate to 3D-Coat to clear any hovering elements
        self.InjectMouseEvent(self.current_widget, 512, -10000, -10000, 0)
        
    def wheelEvent(self, event):
        x, y = self.get_scaled_coordinates(event.position().x(), event.position().y())
        delta = event.angleDelta().y() # Typically 120 or -120
        flags = event.buttons().value if hasattr(event.buttons(), 'value') else 0
        self.InjectWheelEvent(self.current_widget, delta, x, y, flags)
        self.process_frame()
        
    def keyPressEvent(self, event):
        flags = event.modifiers().value if hasattr(event.modifiers(), 'value') else 0
        self.InjectKeyEvent(self.current_widget, 256, event.nativeVirtualKey(), flags)

    def process_frame(self):
        if getattr(self, "_is_processing", False):
            return
            
        self._is_processing = True
        try:
            if hasattr(self.window, "isVisible") and self.window.isVisible():
                if self.window.isActiveWindow():
                    self.SetBlockNativeInput(True)
                else:
                    self.SetBlockNativeInput(False)
        except Exception:
            pass
        try:
            if hasattr(self.window, "isVisible") and not self.window.isVisible():
                return
                
            if not self.current_widget:
                app.processEvents()
                return

            if not hasattr(self, "_pending_fbo"):
                self._pending_fbo = -1

            if self._pending_fbo != -1:
                if not self.IsTexturePixelsReady(self._pending_fbo):
                    return
                    
            if not self.window:
                return
            
            w = self.label.width()
            h = self.label.height()
            if w <= 0 or h <= 0:
                return
                
            # --- FIX: Read the pending FBO BEFORE calling RenderWidgetToTexture.
            # If the size changed, RenderWidgetToTexture will destroy the old FBO in C++.
            # Reading it after destruction causes garbage memory reads and crashes!
            if self._pending_fbo != -1:
                self.current_buffer_idx = (self.current_buffer_idx + 1) % 2
                active_buffer = self.img_buffers[self.current_buffer_idx]
                
                if self.GetTexturePixels(self._pending_fbo, active_buffer):
                    import numpy as np
                    pixels = np.array(active_buffer, copy=False)
                    
                    if len(pixels.shape) == 3:
                        h_arr, w_arr, c_arr = pixels.shape
                        self._last_pixels = pixels
                        self.label._qimage = QImage(pixels.data, w_arr, h_arr, w_arr * 4, QImage.Format_RGBX8888)
                        self.label.update()
                
                self.FreeTexturePixelsBuffer(self._pending_fbo)
                self._pending_fbo = -1
                
            self.fboID = self.RenderWidgetToTexture(self.current_widget, int(w), int(h))
            
            if self.fboID != -1:
                self.RequestTexturePixels(self.fboID)
                self._pending_fbo = self.fboID
                
        except Exception as e:
            print("PyWindowsManager Render Error:", e)
        finally:
            self._is_processing = False


class ListenerWindowsManager(cPy.cCore.WindowsManager):
    def __init__(self, ext):
        super().__init__()
        self.ext = ext

    def OnUndockToQt(self, widgetName):
        if widgetName not in self.ext.active_managers:
            mgr = PyWindowsManager(widgetName, self.ext)
            self.ext.active_managers[widgetName] = mgr
            
        self.ext.active_managers[widgetName].OnUndockToQt(widgetName)


class QTWindowsExtension(cPy.cCore.cExtension):
    def __init__(self):
        super().__init__()
        self.active_managers = {}
        self.listener = None

    def onStart(self):
        self.listener = ListenerWindowsManager(self)

    def afterUI(self):
        for mgr in list(self.active_managers.values()):
            mgr.process_frame()

ext = QTWindowsExtension()
print("QTWindowsExtension loaded")