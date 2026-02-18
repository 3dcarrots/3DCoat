import sys

import os
import time
import cPy.cCore
import cPy.CoreAPI
import coat

import av
import numpy as np

import cPy.cImage
import cPy.cIO

import cModules.ExtensionManager
from cModules.QT.__onstartup import *
from pathlib import Path
import math

from cTemplates.Structs import *

import sys
import math
from PySide6.QtCore import (Qt, Signal, QPointF, QRectF, QSize, QObject, 
                            QEvent, QPoint)
from PySide6.QtGui import (QColor, QPainter, QPainterPath, QPen, QBrush, 
                           QConicalGradient, QLinearGradient, QRadialGradient, 
                           QMouseEvent, QPolygonF, QPixmap, QImage, QAction, 
                           QIcon, QWheelEvent)
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QStackedWidget, QPushButton, QLabel, QLineEdit, 
                               QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, 
                               QFileDialog, QFrame, QSizePolicy, QSlider, QSpinBox,
                               QGridLayout)

# --- CONFIGURATION & STYLES ---
ENABLE_ALPHA = True  # Альфа-канал увімкнено

DARK_THEME_QSS = """
QMainWindow, QWidget {
    background-color: #2b2b2b;
    color: #d0d0d0;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}
QFrame#Separator {
    background-color: #3e3e3e;
    border: none;
    max-height: 1px;
}

/* TAB BUTTONS */
QPushButton.TabBtn {
    background-color: #383838;
    border: 1px solid #1e1e1e;
    color: #a0a0a0;
    padding: 6px 15px;
    border-radius: 0px;
    margin-right: -1px;
}
QPushButton.TabBtn:checked {
    background-color: #4a4a4a;
    color: #ffffff;
    border-bottom: 2px solid #5c7a90;
}
QPushButton.TabBtn:hover {
    background-color: #444444;
}

/* SLIDERS */
QSlider::groove:horizontal {
    border: 1px solid #1e1e1e;
    height: 4px;
    background: #181818;
    margin: 2px 0;
}
QSlider::handle:horizontal {
    background: #808080;
    border: 1px solid #5c7a90;
    width: 10px;
    height: 10px;
    margin: -4px 0;
    border-radius: 5px;
}

/* INPUTS & SPINBOX */
QLineEdit {
    background-color: #1e1e1e;
    border: 1px solid #383838;
    color: #ffffff;
    padding: 2px;
    border-radius: 2px;
}
QLabel { color: #b0b0b0; }

/* SPINBOX STYLING (VERTICAL BUTTONS) */
QSpinBox {
    background-color: #1e1e1e;
    border: 1px solid #383838;
    color: #ffffff;
    padding: 2px;
    padding-right: 5px; /* Місце для кнопок праворуч */
    border-radius: 2px;
}

/* Верхня кнопка */
QSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right; /* Притиснути вгору праворуч */
    width: 16px; 
    border-left: 1px solid #383838;
    border-bottom: 1px solid #383838;
    background: #2b2b2b;
    margin: 1px;
}
QSpinBox::up-button:hover { background: #383838; }
QSpinBox::up-button:pressed { background: #5c7a90; }

/* Нижня кнопка */
QSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right; /* Притиснути вниз праворуч */
    width: 16px;
    border-left: 1px solid #383838;
    border-top: 0px solid #383838; 
    background: #2b2b2b;
    margin: 1px;
}
QSpinBox::down-button:hover { background: #383838; }
QSpinBox::down-button:pressed { background: #5c7a90; }

/* Малюємо стрілочки через прозорі рамки (CSS трикутники) */
QSpinBox::up-arrow {
    width: 0px; 
    height: 0px;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-bottom: 3px solid #a0a0a0; /* Колір стрілки вгору */
}
QSpinBox::down-arrow {
    width: 0px; 
    height: 0px;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-top: 3px solid #a0a0a0; /* Колір стрілки вниз */
}
"""

# --- LOGIC CORE ---

class ColorModel(QObject):
    """Зберігає стан кольору і сповіщає всіх підписників про зміни."""
    colorChanged = Signal(QColor)

    def __init__(self):
        super().__init__()
        self._color = QColor("#587670")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, c):
        if c.isValid() and self._color != c:
            self._color = c
            self.colorChanged.emit(c)

    def set_hsv(self, h, s, v, a=1.0):
        c = QColor.fromHsvF(h if h <= 1.0 else h/360.0, s, v, a)
        self.color = c
        
# --- CUSTOM WIDGETS ---

class HueRingTriangle(QWidget):
    """HSL3: Трикутник всередині кільця."""
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.colorChanged.connect(self.update)
        self.setMinimumSize(220, 220)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ring_width = 25
        self._drag_mode = None 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        rect = self.rect()
        cx, cy = rect.center().x(), rect.center().y()
        radius = min(rect.width(), rect.height()) / 2 - 5
        inner_radius = radius - self.ring_width

        h, s, v, _ = self.model.color.getHsvF()
        h_deg = h * 360.0

        # 1. Кільце Hue
        gradient = QConicalGradient(cx, cy, 90) 
        stops = [
            (0.000, QColor(255, 0, 0)), (0.166, QColor(255, 255, 0)),
            (0.333, QColor(0, 255, 0)), (0.500, QColor(0, 255, 255)),
            (0.666, QColor(0, 0, 255)), (0.833, QColor(255, 0, 255)),
            (1.000, QColor(255, 0, 0))
        ]
        for pos, col in stops:
            gradient.setColorAt(pos, col)
            
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(QPointF(cx, cy), radius, radius)
        
        painter.setBrush(QBrush(QColor("#2b2b2b")))
        painter.drawEllipse(QPointF(cx, cy), inner_radius, inner_radius)

        # 2. Трикутник
        angle_rad = math.radians(h_deg + 90) 
        tri_r = inner_radius - 4
        
        p1 = QPointF(cx + tri_r * math.cos(angle_rad), cy - tri_r * math.sin(angle_rad))
        p2 = QPointF(cx + tri_r * math.cos(angle_rad + 2*math.pi/3), 
                     cy - tri_r * math.sin(angle_rad + 2*math.pi/3))
        p3 = QPointF(cx + tri_r * math.cos(angle_rad - 2*math.pi/3), 
                     cy - tri_r * math.sin(angle_rad - 2*math.pi/3))
        
        self.triangle_poly = QPolygonF([p1, p2, p3])

        painter.save()
        path = QPainterPath()
        path.addPolygon(self.triangle_poly)
        painter.setClipPath(path)
        
        painter.fillPath(path, Qt.black)
        
        mid_p1_p3 = (p1 + p3) / 2
        g_white = QLinearGradient(p2, mid_p1_p3)
        g_white.setColorAt(0, QColor(255, 255, 255, 255))
        g_white.setColorAt(1, QColor(255, 255, 255, 0))
        painter.fillRect(rect, g_white)
        
        hue_col = QColor.fromHsvF(h, 1.0, 1.0)
        hue_col.setAlpha(255)
        mid_p2_p3 = (p2 + p3) / 2
        g_hue = QLinearGradient(p1, mid_p2_p3)
        g_hue.setColorAt(0, hue_col)
        hue_transparent = QColor(hue_col)
        hue_transparent.setAlpha(0)
        g_hue.setColorAt(1, hue_transparent)
        
        painter.setCompositionMode(QPainter.CompositionMode_Screen)
        painter.fillRect(rect, g_hue)
        painter.restore()

        # 3. Маркери
        ring_marker_pos = QPointF(cx + (radius - self.ring_width/2) * math.cos(angle_rad),
                                  cy - (radius - self.ring_width/2) * math.sin(angle_rad))
        
        painter.setPen(QPen(Qt.white, 2))
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(ring_marker_pos, 5, 5)

        cursor_pos = (1-v)*p3 + v*((1-s)*p2 + s*p1)
        
        painter.setPen(QPen(Qt.black, 1))
        painter.drawRect(QRectF(cursor_pos.x()-3, cursor_pos.y()-3, 6, 6))
        painter.setPen(QPen(Qt.white, 1))
        painter.drawRect(QRectF(cursor_pos.x()-2, cursor_pos.y()-2, 4, 4))

    def mousePressEvent(self, event):
        self._update_from_mouse(event.position(), check_zone=True)

    def mouseMoveEvent(self, event):
        if self._drag_mode:
            self._update_from_mouse(event.position(), check_zone=False)

    def mouseReleaseEvent(self, event):
        self._drag_mode = None

    def _update_from_mouse(self, pos, check_zone=False):
        rect = self.rect()
        cx, cy = rect.center().x(), rect.center().y()
        dx = pos.x() - cx
        dy = cy - pos.y() 
        
        dist = math.hypot(dx, dy)
        radius = min(rect.width(), rect.height()) / 2 - 5
        inner_radius = radius - self.ring_width

        angle = math.degrees(math.atan2(dy, dx))
        if angle < 0: angle += 360
        hue_angle = (angle - 90) % 360
        
        if check_zone:
            if inner_radius < dist < radius:
                self._drag_mode = 'ring'
            elif dist < inner_radius:
                self._drag_mode = 'triangle'
            else:
                return

        if self._drag_mode == 'ring':
            s, v = self.model.color.saturationF(), self.model.color.valueF()
            self.model.set_hsv(hue_angle / 360.0, s, v, self.model.color.alphaF())
            
        elif self._drag_mode == 'triangle':
            h = self.model.color.hueF()
            h_rad = math.radians(h * 360.0 + 90)
            tri_r = inner_radius - 4
            p1 = QPointF(cx + tri_r * math.cos(h_rad), cy - tri_r * math.sin(h_rad))
            p2 = QPointF(cx + tri_r * math.cos(h_rad + 2*math.pi/3), cy - tri_r * math.sin(h_rad + 2*math.pi/3))
            p3 = QPointF(cx + tri_r * math.cos(h_rad - 2*math.pi/3), cy - tri_r * math.sin(h_rad - 2*math.pi/3))

            def sign(p1, p2, p3):
                return (p1.x() - p3.x()) * (p2.y() - p3.y()) - (p2.x() - p3.x()) * (p1.y() - p3.y())

            d = sign(p1, p2, p3)
            if d == 0: return
            
            w1 = (sign(pos, p2, p3)) / d
            w2 = (sign(pos, p3, p1)) / d
            w3 = 1.0 - w1 - w2

            if w1 < 0: w1 = 0
            if w2 < 0: w2 = 0
            if w3 < 0: w3 = 0
            
            total = w1 + w2 + w3
            if total == 0: return
            w1 /= total; w2 /= total; w3 /= total
            
            new_v = w1 + w2
            new_s = w1 / new_v if new_v > 0 else 0
            
            self.model.set_hsv(h, new_s, new_v, self.model.color.alphaF())


class ColorSquareWidget(QWidget):
    """HSL1: Квадрат Saturation/Value + Hue Bar"""
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.colorChanged.connect(self.update)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        hue_width = 30
        sv_rect = QRectF(hue_width + 5, 0, rect.width() - hue_width - 5, rect.height())
        hue_rect = QRectF(0, 0, hue_width, rect.height())
        h, s, v, _ = self.model.color.getHsvF()
        
        # Hue Bar
        g_hue = QLinearGradient(hue_rect.topLeft(), hue_rect.bottomLeft())
        for i in range(7):
            g_hue.setColorAt(i/6.0, QColor.fromHsvF(i/6.0 if i<6 else 0, 1, 1))
        painter.fillRect(hue_rect, g_hue)
        
        hue_y = h * rect.height()
        painter.setPen(Qt.black)
        painter.drawRect(0, int(hue_y)-2, hue_width, 4)
        
        # SV Square
        base_c = QColor.fromHsvF(h, 1, 1)
        painter.fillRect(sv_rect, base_c)
        
        g_sat = QLinearGradient(sv_rect.topLeft(), sv_rect.topRight())
        g_sat.setColorAt(0, Qt.white)
        g_sat.setColorAt(1, Qt.transparent)
        painter.fillRect(sv_rect, g_sat)
        
        g_val = QLinearGradient(sv_rect.topLeft(), sv_rect.bottomLeft())
        g_val.setColorAt(0, Qt.transparent)
        g_val.setColorAt(1, Qt.black)
        painter.fillRect(sv_rect, g_val)
        
        mx = sv_rect.x() + (s * sv_rect.width())
        my = sv_rect.y() + ((1-v) * sv_rect.height())
        painter.setPen(QPen(Qt.black if v > 0.5 else Qt.white, 2))
        painter.drawEllipse(QPointF(mx, my), 5, 5)

    def mousePressEvent(self, event):
        self._handle_mouse(event.position())
        
    def mouseMoveEvent(self, event):
        self._handle_mouse(event.position())
        
    def _handle_mouse(self, pos):
        rect = self.rect()
        hue_width = 30
        h, s, v, a = self.model.color.getHsvF()
        
        if pos.x() <= hue_width:
            new_h = pos.y() / rect.height()
            self.model.set_hsv(max(0, min(1, new_h)), s, v, a)
        elif pos.x() > hue_width + 5:
            sv_rect = QRectF(hue_width + 5, 0, rect.width() - hue_width - 5, rect.height())
            new_s = (pos.x() - sv_rect.x()) / sv_rect.width()
            new_v = 1.0 - (pos.y() / sv_rect.height())
            self.model.set_hsv(h, max(0, min(1, new_s)), max(0, min(1, new_v)), a)


class ImagePickerWidget(QWidget):
    """IMG: Завантаження зображення та піпетка"""
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        
        toolbar = QHBoxLayout()
        self.btn_load = QPushButton("Select Image")
        self.btn_load.clicked.connect(self.load_image)
        toolbar.addWidget(self.btn_load)
        self.layout.addLayout(toolbar)
        
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.view.setBackgroundBrush(QColor("#222"))
        self.layout.addWidget(self.view)
        
        self.image_item = None
        self.pixmap = None

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self.pixmap = QPixmap(path)
            self.scene.clear()
            self.image_item = QGraphicsPixmapItem(self.pixmap)
            self.scene.addItem(self.image_item)
            self.view.fitInView(self.image_item, Qt.KeepAspectRatio)
            self.image_item.setAcceptHoverEvents(True)
            self.view.mousePressEvent = self.pick_color

    def pick_color(self, event):
        if self.image_item and event.button() == Qt.LeftButton:
            scene_pos = self.view.mapToScene(event.pos())
            item_pos = self.image_item.mapFromScene(scene_pos)
            x = int(item_pos.x())
            y = int(item_pos.y())
            
            img = self.pixmap.toImage()
            if 0 <= x < img.width() and 0 <= y < img.height():
                col = img.pixelColor(x, y)
                self.model.color = col
        QGraphicsView.mousePressEvent(self.view, event)


class HSDiscWidget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.colorChanged.connect(self.update)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.margin = 10
        self.bar_height = 25

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        
        disk_area_h = rect.height() - self.bar_height - self.margin * 2
        radius = min(rect.width(), disk_area_h) / 2 - 5
        if radius <= 0: return
        
        center_x = rect.center().x()
        center_y = 5 + radius
        center = QPointF(center_x, center_y)
        bar_rect = QRectF(20, rect.height() - self.bar_height - 5, rect.width() - 40, self.bar_height)

        h, s, v, _ = self.model.color.getHsvF()

        painter.save()
        painter.translate(center)
        
        conical = QConicalGradient(0, 0, 0)
        for i in range(0, 361, 60):
            conical.setColorAt(i/360.0, QColor.fromHsvF(i/360.0, 1, 1))
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(conical))
        painter.drawEllipse(QPointF(0, 0), radius, radius)

        radial = QRadialGradient(0, 0, radius)
        radial.setColorAt(0, QColor(255, 255, 255, 255))
        radial.setColorAt(1, QColor(255, 255, 255, 0))
        painter.setBrush(QBrush(radial))
        painter.drawEllipse(QPointF(0, 0), radius, radius)
        
        angle_rad = -h * 2 * math.pi 
        dist = s * radius
        mx = dist * math.cos(angle_rad)
        my = dist * math.sin(angle_rad)
        
        painter.translate(mx, my)
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(Qt.white)
        painter.drawRect(-3, -3, 6, 6)
        painter.restore()

        base_color = QColor.fromHsvF(h, s, 1.0)
        l_grad = QLinearGradient(bar_rect.topLeft(), bar_rect.topRight())
        l_grad.setColorAt(0.0, Qt.black)
        l_grad.setColorAt(1.0, base_color)
        
        painter.setBrush(QBrush(l_grad))
        painter.setPen(QPen(Qt.black, 1))
        painter.drawRect(bar_rect)
        
        val_x = bar_rect.left() + v * bar_rect.width()
        painter.setPen(QPen(Qt.white, 2))
        painter.drawLine(val_x, bar_rect.top(), val_x, bar_rect.bottom())
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(val_x - 3, bar_rect.top(), 6, bar_rect.height())

    def mousePressEvent(self, event):
        self._handle_mouse(event.position())
        
    def mouseMoveEvent(self, event):
        self._handle_mouse(event.position())

    def _handle_mouse(self, pos):
        rect = self.rect()
        bar_top = rect.height() - self.bar_height - 10
        h, s, v, a = self.model.color.getHsvF()

        if pos.y() >= bar_top:
            bar_width = rect.width() - 40
            bar_start = 20
            ratio = (pos.x() - bar_start) / bar_width
            new_v = max(0.0, min(1.0, ratio))
            self.model.set_hsv(h, s, new_v, a)
        else:
            disk_area_h = rect.height() - self.bar_height - self.margin * 2
            radius = min(rect.width(), disk_area_h) / 2 - 5
            center_x = rect.center().x()
            center_y = 5 + radius
            
            dx = pos.x() - center_x
            dy = pos.y() - center_y
            
            dist = math.hypot(dx, dy)
            angle = math.degrees(math.atan2(dy, dx))
            if angle < 0: angle += 360
            new_h = (360 - angle) / 360.0
            new_h = new_h % 1.0
            new_s = min(1.0, dist / radius)
            
            self.model.set_hsv(new_h, new_s, v, a)

# --- MAIN GUI ASSEMBLY ---

class ColorPaletteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Palette")
        self.resize(360, 600)
        self.model = ColorModel()
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.initial_color = None  # Сюди збережемо колір для Cancel

        main_vbox = QVBoxLayout(self)
        main_vbox.setSpacing(0)
        main_vbox.setContentsMargins(2, 2, 2, 2)
        
        # Tabs
        self.tabs_layout = QHBoxLayout()
        self.tabs_layout.setSpacing(0)
        self.btn_hsl1 = self.create_tab_btn("HSL1")
        self.btn_hsl2 = self.create_tab_btn("HSL2")
        self.btn_hsl3 = self.create_tab_btn("HSL3")
        self.btn_img = self.create_tab_btn("IMG")
        self.tabs_layout.addStretch()
        main_vbox.addLayout(self.tabs_layout)
        
        # Stack
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: #262626;")
        
        self.widget_hsl1 = ColorSquareWidget(self.model)
        self.widget_hsl2 = HueRingTriangle(self.model) 
        self.widget_hsl3 = HSDiscWidget(self.model)
        self.widget_img = ImagePickerWidget(self.model)
        
        self.stack.addWidget(self.widget_hsl1)
        self.stack.addWidget(self.widget_hsl2)
        self.stack.addWidget(self.widget_hsl3)
        self.stack.addWidget(self.widget_img)
        main_vbox.addWidget(self.stack)
        
        self.btn_hsl1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_hsl2.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_hsl3.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.btn_img.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        
        self.btn_hsl3.setChecked(True)
        self.stack.setCurrentIndex(2)

        # --- FOOTER ---
        self.footer = QWidget()
        self.footer.setStyleSheet("background-color: #2b2b2b;")
        footer_layout = QVBoxLayout(self.footer)
        
        # Gradient Bar
        self.grad_bar = QFrame()
        self.grad_bar.setFixedHeight(8)
        footer_layout.addWidget(self.grad_bar)
        
        # Controls Row
        ctrl_row = QHBoxLayout()
        
        # Swatch
        self.swatch = QFrame()
        self.swatch.setFixedSize(60, 60)
        self.swatch.setStyleSheet("border: 1px solid #555;")
        ctrl_row.addWidget(self.swatch)
        
        # Sliders Form
        sliders_layout = QGridLayout()
        sliders_layout.setSpacing(4)
        
        self.sl_h, self.sb_h = self.create_slider(sliders_layout, "Hue", 0, 360, 0)
        self.sl_s, self.sb_s = self.create_slider(sliders_layout, "Sat", 0, 255, 1)
        self.sl_l, self.sb_l = self.create_slider(sliders_layout, "Light", 0, 255, 2)
        
        next_row = 3
        if ENABLE_ALPHA:
            self.sl_a, self.sb_a = self.create_slider(sliders_layout, "Alpha", 0, 255, 3)
            self.sl_a.valueChanged.connect(self.on_slider_change)
            next_row = 4
        else:
            self.sl_a, self.sb_a = None, None

        self.hex_input = QLineEdit()
        self.hex_input.setPlaceholderText("#AARRGGBB" if ENABLE_ALPHA else "#RRGGBB")
        self.hex_input.returnPressed.connect(self.on_hex_entered)
        sliders_layout.addWidget(QLabel("Hex"), next_row, 0)
        sliders_layout.addWidget(self.hex_input, next_row, 1, 1, 2)
        
        ctrl_row.addLayout(sliders_layout)
        footer_layout.addLayout(ctrl_row)


        # Buttons
        btns_layout = QHBoxLayout()
        btn_ok = QPushButton("OK")
        btn_cancel = QPushButton("Cancel")
        btn_ok.clicked.connect(self.accept)
        btn_cancel.clicked.connect(self.reject)        
        for b in [btn_ok, btn_cancel]:
            b.setStyleSheet("background-color: #3e3e3e; border: 1px solid #111; min-width: 60px; padding: 4px;")
        
        btns_layout.addStretch()
        btns_layout.addWidget(btn_ok)
        btns_layout.addWidget(btn_cancel)
        footer_layout.addLayout(btns_layout)
        
        # !!! ВАЖЛИВО: Додаємо футер до головного вікна !!!
        main_vbox.addWidget(self.footer)
        
        # Logic Connections
        self.model.colorChanged.connect(self.sync_ui_from_model)
        self.sl_h.valueChanged.connect(self.on_slider_change)
        self.sl_s.valueChanged.connect(self.on_slider_change)
        self.sl_l.valueChanged.connect(self.on_slider_change)
        
        # Init
        self.sync_ui_from_model(self.model.color)

    def set_initial_color(self, color):
        """Запам'ятовуємо колір перед початком редагування"""
        self.initial_color = QColor(color)
        self.model.color = color

    def accept(self):
        """Закриваємо вікно, зберігаючи зміни (просто закриваємо)"""
        self.close()

    def reject(self):
        """Повертаємо початковий колір і закриваємо"""
        if self.initial_color:
            self.model.color = self.initial_color
        self.close()

    def create_tab_btn(self, text):
        btn = QPushButton(text)
        btn.setCheckable(True)
        btn.setAutoExclusive(True)
        btn.setProperty("class", "TabBtn")
        self.tabs_layout.addWidget(btn)
        return btn

    def create_slider(self, layout, label, min_v, max_v, row):
        lbl = QLabel(label)
        sl = QSlider(Qt.Horizontal)
        sl.setRange(min_v, max_v)
        
        sb = QSpinBox()
        sb.setRange(min_v, max_v)
        sb.setFixedWidth(65) 
        #sb.setButtonSymbols(QSpinBox.NoButtons)
        
        # Sync
        sl.valueChanged.connect(sb.setValue)
        sb.valueChanged.connect(sl.setValue)
        
        layout.addWidget(lbl, row, 0)
        layout.addWidget(sl, row, 1)
        layout.addWidget(sb, row, 2)
        return sl, sb

    def sync_ui_from_model(self, col):
        self.block_sliders(True)
        
        h, s, v, a = col.getHsv()
        if h == -1: h = self.sl_h.value() 
        
        self.sl_h.setValue(int(h))
        self.sb_h.setValue(int(h))
        self.sl_s.setValue(int(s))
        self.sb_s.setValue(int(s))
        self.sl_l.setValue(int(v))
        self.sb_l.setValue(int(v))
        
        if ENABLE_ALPHA and self.sl_a:
            self.sl_a.setValue(a)
            self.sb_a.setValue(a)
            self.hex_input.setText(col.name(QColor.HexArgb).upper())
        else:
            self.hex_input.setText(col.name().upper())

        r, g, b, alpha = col.red(), col.green(), col.blue(), col.alpha()
        self.swatch.setStyleSheet(f"background-color: rgba({r}, {g}, {b}, {alpha/255.0}); border: 1px solid #555;")
        
        col_css = f"rgba({r},{g},{b},{alpha/255.0})"
        grad_css = f"background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #000, stop:1 {col_css});"
        self.grad_bar.setStyleSheet(grad_css)
        
        self.block_sliders(False)

    def on_slider_change(self):
        h = self.sl_h.value()
        s = self.sl_s.value()
        v = self.sl_l.value()
        
        a = 255
        if ENABLE_ALPHA and self.sl_a:
            a = self.sl_a.value()
            
        self.model.set_hsv(h, s/255.0, v/255.0, a/255.0)

    def on_hex_entered(self):
        txt = self.hex_input.text().strip()
        if not txt.startswith('#'): txt = '#' + txt
        
        c = QColor(txt)
        if c.isValid():
            if not ENABLE_ALPHA:
                c.setAlpha(255)
            self.model.color = c

    def block_sliders(self, blocked):
        self.sl_h.blockSignals(blocked)
        self.sb_h.blockSignals(blocked)
        self.sl_s.blockSignals(blocked)
        self.sb_s.blockSignals(blocked)
        self.sl_l.blockSignals(blocked)
        self.sb_l.blockSignals(blocked)
        
        if ENABLE_ALPHA and self.sl_a:
            self.sl_a.blockSignals(blocked)
            self.sb_a.blockSignals(blocked)

            

class QTColorSelector(cPy.cCore.cColorSelectorInterface):
    def __init__(self):
        cPy.cCore.cColorSelectorInterface.__init__(self)
        self.window = ColorPaletteApp()

    def ShowModal(self):
        global ENABLE_ALPHA
        ENABLE_ALPHA = self.ShowAlpha
        
        
        # Застосування стилю (якщо він не був застосований глобально)
        self.window.setStyleSheet(DARK_THEME_QSS)
        
        # 3. Передача початкового кольору з 3DCoat (cColorSelectorInterface) в UI
        # Дані приходять у float (0.0 - 1.0)
        initial_color = QColor.fromRgbF(
            self.Red, 
            self.Green, 
            self.Blue, 
            self.Alpha if self.ShowAlpha else 1.0
        )
        
        # Встановлюємо колір у модель, це автоматично оновить всі слайдери і віджети
        self.window.set_initial_color(initial_color)        
        
        self.window.show()
        return True
        

    def IsActive(self):        
        global app
        app.processEvents() # Оновлення подій Qt
        
        if self.window is None:
            return False

        is_visible = self.window.isVisible()
        
        current_color = self.window.model.color
        
        if current_color.isValid():
            # Записуємо назад у змінні батьківського класу
            self.Red = current_color.redF()
            self.Green = current_color.greenF()
            self.Blue = current_color.blueF()
            self.Alpha = current_color.alphaF()
        
        return is_visible        

class QTColorSelectorExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)

    def onStart(self):
        self.colorSelectorForm = QTColorSelector()
        cPy.cCore.ExtensionManager.MainColorSelector = self.colorSelectorForm

    def postrender(self):
        if self.colorSelectorForm.window.isVisible:
            self.colorSelectorForm.window.raise_()


colorSelectorExtension = QTColorSelectorExtension()
