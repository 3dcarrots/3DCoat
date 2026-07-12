from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QSlider, QLabel, QFileDialog, QCheckBox,
                               QColorDialog, QFormLayout, QComboBox, QMessageBox,
                               QGroupBox, QGridLayout, QSpinBox, QDoubleSpinBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage
import numpy as np

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

from .GLRenderer import PBRRenderer
from .MathAlgorithms import calculate_seam_energy_offset, frankot_chellappa

DARK_THEME_QSS = """
QMainWindow, QWidget {
    background-color: #2b2b2b;
    color: #d0d0d0;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}
QGroupBox {
    border: 1px solid #383838;
    border-radius: 3px;
    margin-top: 25px;
    padding-top: 15px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
    left: 10px;
    top: 5px;
}
QPushButton {
    background-color: #383838;
    border: 1px solid #1e1e1e;
    color: #d0d0d0;
    padding: 6px 15px;
    border-radius: 3px;
}
QPushButton:hover { background-color: #444444; }
QPushButton:pressed { background-color: #5c7a90; color: #ffffff; }
QSpinBox, QDoubleSpinBox {
    background-color: #1e1e1e;
    border: 1px solid #383838;
    color: #ffffff;
    padding: 2px;
    padding-right: 15px; 
    border-radius: 2px;
}
QSpinBox::up-button, QDoubleSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 16px; 
    border-left: 1px solid #383838;
    border-bottom: 1px solid #383838;
    background: #2b2b2b;
    margin: 1px;
}
QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover { background: #383838; }
QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed { background: #5c7a90; }

QSpinBox::down-button, QDoubleSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 16px;
    border-left: 1px solid #383838;
    border-top: 0px solid #383838; 
    background: #2b2b2b;
    margin: 1px;
}
QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover { background: #383838; }
QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed { background: #5c7a90; }

QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {
    width: 0px; 
    height: 0px;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-bottom: 3px solid #a0a0a0;
}
QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {
    width: 0px; 
    height: 0px;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-top: 3px solid #a0a0a0;
}
"""

class TilerMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PBR Seamless Tiler & Editor")
        self.setStyleSheet(DARK_THEME_QSS)
        self.picking_color = False
        self.resize(1200, 800)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QHBoxLayout()
        main_widget.setLayout(layout)
        
        # Left Panel (Controls)
        control_panel = QWidget()
        control_layout = QVBoxLayout()
        control_panel.setLayout(control_layout)
        control_panel.setFixedWidth(350)
        
        # 1. Top Core Settings
        top_form = QFormLayout()
        
        self.combo_view = QComboBox()
        self.refresh_view_modes()
        self.combo_view.currentIndexChanged.connect(self.update_view_mode)
        top_form.addRow("Display:", self.combo_view)
        
        control_layout.addLayout(top_form)

        # 2. Load Textures
        self.btn_load_base = QPushButton("Load Albedo")
        self.btn_load_norm = QPushButton("Load Normal")
        self.btn_load_hght = QPushButton("Load Height")
        
        self.btn_load_base.clicked.connect(lambda: self.load_texture("albedo"))
        self.btn_load_norm.clicked.connect(lambda: self.load_texture("normal"))
        self.btn_load_hght.clicked.connect(lambda: self.load_texture("height"))
        
        control_layout.addWidget(self.btn_load_base)
        control_layout.addWidget(self.btn_load_norm)
        control_layout.addWidget(self.btn_load_hght)
        
        self.btn_load_custom = QPushButton("+ Add Custom Map...")
        self.btn_load_custom.clicked.connect(self.add_custom_map)
        control_layout.addWidget(self.btn_load_custom)
        
        # 2.5 Albedo Equalizer
        self.chk_albedo_eq = QCheckBox("Enable Albedo Equalization")
        self.chk_albedo_eq.setChecked(True)
        self.chk_albedo_eq.stateChanged.connect(self.update_renderer)
        control_layout.addWidget(self.chk_albedo_eq)
        
        self.spin_albedo_eq_rad_center = QSpinBox()
        self.spin_albedo_eq_rad_center.setRange(1, 2048) # Linear Pixel Radius
        self.spin_albedo_eq_rad_center.setValue(500)
        self.spin_albedo_eq_rad_center.valueChanged.connect(self.update_renderer)
        al_eq_layout = QHBoxLayout()
        al_eq_layout.addWidget(QLabel("Eq Center:"))
        al_eq_layout.addWidget(self.spin_albedo_eq_rad_center)
        
        self.spin_albedo_eq_rad_edge = QSpinBox()
        self.spin_albedo_eq_rad_edge.setRange(1, 2048)
        self.spin_albedo_eq_rad_edge.setValue(50)
        self.spin_albedo_eq_rad_edge.valueChanged.connect(self.update_renderer)
        al_eq_layout.addWidget(QLabel("Eq Edge:"))
        al_eq_layout.addWidget(self.spin_albedo_eq_rad_edge)
        control_layout.addLayout(al_eq_layout)
        
        # 3. Export Resolutions
        self.btn_export = QPushButton("Export Result")
        self.btn_export.clicked.connect(self.export_textures)
        
        self.combo_export_w = QComboBox()
        self.combo_export_w.addItems(["512", "1024", "2048", "4096", "8192"])
        self.combo_export_w.setCurrentIndex(3)
        self.combo_export_w.setEditable(True)
        self.combo_export_w.currentTextChanged.connect(self.update_renderer)
        
        self.combo_export_h = QComboBox()
        self.combo_export_h.addItems(["512", "1024", "2048", "4096", "8192"])
        self.combo_export_h.setCurrentIndex(3)
        self.combo_export_h.setEditable(True)
        self.combo_export_h.currentTextChanged.connect(self.update_renderer)
        
        res_layout = QHBoxLayout()
        res_layout.addWidget(QLabel("Exp W:"))
        res_layout.addWidget(self.combo_export_w)
        res_layout.addWidget(QLabel("H:"))
        res_layout.addWidget(self.combo_export_h)
        control_layout.addLayout(res_layout)
        
        # 4. Normal Processing Tools
        self.chk_invert_y = QCheckBox("Invert Normal Y (Green)")
        self.chk_invert_y.setChecked(True)
        self.chk_invert_y.stateChanged.connect(self.update_renderer)
        control_layout.addWidget(self.chk_invert_y)
        
        self.btn_norm2hght = QPushButton("Generate Height from Normal")
        self.btn_norm2hght.clicked.connect(self.run_normal_to_height)
        control_layout.addWidget(self.btn_norm2hght)
        
        self.spin_hp_radius_center = QSpinBox()
        self.spin_hp_radius_center.setRange(0, 500)
        self.spin_hp_radius_center.setValue(100)
        hp_layout = QHBoxLayout()
        hp_layout.addWidget(QLabel("HP Center:"))
        hp_layout.addWidget(self.spin_hp_radius_center)
        
        self.spin_hp_radius_edge = QSpinBox()
        self.spin_hp_radius_edge.setRange(0, 500)
        self.spin_hp_radius_edge.setValue(50)
        hp_layout.addWidget(QLabel("HP Edge:"))
        hp_layout.addWidget(self.spin_hp_radius_edge)
        control_layout.addLayout(hp_layout)
        
        # 4.5 Microprotrusions (Max Albedo)
        micro_group = QGroupBox("Microprotrusions")
        micro_layout = QVBoxLayout(micro_group)
        self.btn_gen_micro = QPushButton("Generate Microprotrusions")
        self.btn_gen_micro.clicked.connect(self.run_microprotrusions)
        
        self.spin_micro_radius = QSpinBox()
        self.spin_micro_radius.setRange(1, 100)
        self.spin_micro_radius.setValue(10)
        self.spin_micro_radius.setSuffix(" px")
        self.spin_micro_radius.valueChanged.connect(self.on_micro_radius_changed)
        
        m_rad_layout = QHBoxLayout()
        m_rad_layout.addWidget(QLabel("Radius:"))
        m_rad_layout.addWidget(self.spin_micro_radius)
        
        self.spin_micro_samples = QSpinBox()
        self.spin_micro_samples.setRange(0, 31)
        self.spin_micro_samples.setSingleStep(1)
        self.spin_micro_samples.setValue(3)
        self.spin_micro_samples.setSpecialValueText("0 (Dense / Full Radius)")
        self.spin_micro_samples.valueChanged.connect(self.on_micro_radius_changed)
        
        m_samp_layout = QHBoxLayout()
        m_samp_layout.addWidget(QLabel("Samples (NxN):"))
        m_samp_layout.addWidget(self.spin_micro_samples)
        
        micro_layout.addWidget(self.btn_gen_micro)
        micro_layout.addLayout(m_rad_layout)
        micro_layout.addLayout(m_samp_layout)
        control_layout.addWidget(micro_group)
        
        self._micro_timer = QTimer(self)
        self._micro_timer.setSingleShot(True)
        self._micro_timer.timeout.connect(self.run_microprotrusions)
        
        # 5. Crop Group
        crop_group = QGroupBox("Crop Source (px)")
        crop_layout = QGridLayout(crop_group)
        self.spin_crop_top = QSpinBox()
        self.spin_crop_bot = QSpinBox()
        self.spin_crop_lft = QSpinBox()
        self.spin_crop_rgt = QSpinBox()
        for spin in [self.spin_crop_top, self.spin_crop_bot, self.spin_crop_lft, self.spin_crop_rgt]:
            spin.setRange(0, 8192)
            spin.valueChanged.connect(self.update_renderer)
            
        crop_layout.addWidget(QLabel("Top:"), 0, 0)
        crop_layout.addWidget(self.spin_crop_top, 0, 1)
        crop_layout.addWidget(QLabel("Bottom:"), 1, 0)
        crop_layout.addWidget(self.spin_crop_bot, 1, 1)
        crop_layout.addWidget(QLabel("Left:"), 0, 2)
        crop_layout.addWidget(self.spin_crop_lft, 0, 3)
        crop_layout.addWidget(QLabel("Right:"), 1, 2)
        crop_layout.addWidget(self.spin_crop_rgt, 1, 3)
        control_layout.addWidget(crop_group)
        
        # 6. Tile Offset Group
        ofs_group = QGroupBox("Tile Offset (%)")
        ofs_layout = QHBoxLayout(ofs_group)
        self.spin_offset_x = QDoubleSpinBox()
        self.spin_offset_y = QDoubleSpinBox()
        for spin in [self.spin_offset_x, self.spin_offset_y]:
            spin.setRange(0.00, 100.00)
            spin.setSingleStep(1.0)
            spin.setDecimals(2)
            spin.valueChanged.connect(self.update_renderer)
        ofs_layout.addWidget(QLabel("X:"))
        ofs_layout.addWidget(self.spin_offset_x)
        ofs_layout.addWidget(QLabel("Y:"))
        ofs_layout.addWidget(self.spin_offset_y)
        control_layout.addWidget(ofs_group)

        # 7. Corners Group
        corn_group = QGroupBox("Corner Pixel Tweaks (px)")
        corn_layout = QGridLayout(corn_group)
        self.spin_corn_tl_x = QSpinBox()
        self.spin_corn_tl_y = QSpinBox()
        self.spin_corn_tr_x = QSpinBox()
        self.spin_corn_tr_y = QSpinBox()
        self.spin_corn_bl_x = QSpinBox()
        self.spin_corn_bl_y = QSpinBox()
        self.spin_corn_br_x = QSpinBox()
        self.spin_corn_br_y = QSpinBox()
        c_spins = [
            (self.spin_corn_tl_x, self.spin_corn_tl_y),
            (self.spin_corn_tr_x, self.spin_corn_tr_y),
            (self.spin_corn_bl_x, self.spin_corn_bl_y),
            (self.spin_corn_br_x, self.spin_corn_br_y)
        ]
        for i, (sx, sy) in enumerate(c_spins):
            sx.setRange(-4096, 4096)
            sy.setRange(-4096, 4096)
            sx.setSingleStep(1)
            sy.setSingleStep(1)
            sx.setValue(0)
            sy.setValue(0)
            sx.valueChanged.connect(self.update_renderer)
            sy.valueChanged.connect(self.update_renderer)
            
        corn_layout.addWidget(QLabel("TL:"), 0, 0)
        corn_layout.addWidget(self.spin_corn_tl_x, 0, 1)
        corn_layout.addWidget(self.spin_corn_tl_y, 0, 2)
        corn_layout.addWidget(QLabel("TR:"), 1, 0)
        corn_layout.addWidget(self.spin_corn_tr_x, 1, 1)
        corn_layout.addWidget(self.spin_corn_tr_y, 1, 2)
        corn_layout.addWidget(QLabel("BL:"), 2, 0)
        corn_layout.addWidget(self.spin_corn_bl_x, 2, 1)
        corn_layout.addWidget(self.spin_corn_bl_y, 2, 2)
        corn_layout.addWidget(QLabel("BR:"), 3, 0)
        corn_layout.addWidget(self.spin_corn_br_x, 3, 1)
        corn_layout.addWidget(self.spin_corn_br_y, 3, 2)
        control_layout.addWidget(corn_group)
        
        # 8. Sliders Form (Rotation, Blending, Chroma)
        form = QFormLayout()
        
        self.spin_rot = QDoubleSpinBox()
        self.spin_rot.setRange(0.0, 360.0)
        self.spin_rot.setSingleStep(0.1)
        self.spin_rot.setDecimals(2)
        self.spin_rot.valueChanged.connect(self.update_renderer)
        form.addRow("Rotation (°):", self.spin_rot)
        
        self.chk_height_blend = QCheckBox("Enable Edge Blending")
        self.chk_height_blend.setChecked(False)
        self.chk_height_blend.stateChanged.connect(self.update_renderer)
        form.addRow("Height Blend:", self.chk_height_blend)
        
        self.spin_blend_margin = QDoubleSpinBox()
        self.spin_blend_margin.setRange(0.00, 30.00)
        self.spin_blend_margin.setSingleStep(0.01)
        self.spin_blend_margin.setValue(0.05)
        self.spin_blend_margin.valueChanged.connect(self.update_renderer)
        form.addRow("Overlap (1-30):", self.spin_blend_margin)
        
        self.slider_h_thresh = QSlider(Qt.Horizontal)
        self.slider_h_thresh.setRange(0, 100)
        self.slider_h_thresh.setValue(20)
        self.slider_h_thresh.valueChanged.connect(self.update_renderer)
        form.addRow("Threshold:", self.slider_h_thresh)
        
        self.slider_h_contrast = QSlider(Qt.Horizontal)
        self.slider_h_contrast.setRange(0, 100)
        self.slider_h_contrast.setValue(50)
        self.slider_h_contrast.valueChanged.connect(self.update_renderer)
        form.addRow("Softness:", self.slider_h_contrast)
        
        self.slider_h_inf = QSlider(Qt.Horizontal)
        self.slider_h_inf.setRange(0, 100)
        self.slider_h_inf.setValue(20)
        self.slider_h_inf.valueChanged.connect(self.update_renderer)
        form.addRow("Height Inf (%):", self.slider_h_inf)
        
        control_layout.addLayout(form)
        
        # 9. Color Correction
        color_group = QGroupBox("Color Correction")
        color_form = QFormLayout(color_group)
        
        self.slider_hue = QSlider(Qt.Horizontal)
        self.slider_hue.setRange(-180, 180)
        self.slider_hue.setValue(0)
        self.slider_hue.valueChanged.connect(self.update_renderer)
        color_form.addRow("HUE:", self.slider_hue)
        
        btn_layout = QHBoxLayout()
        self.btn_red = QPushButton("Red")
        self.btn_red.clicked.connect(lambda: self.auto_hue(0))
        self.btn_green = QPushButton("Green")
        self.btn_green.clicked.connect(lambda: self.auto_hue(120))
        self.btn_blue = QPushButton("Blue")
        self.btn_blue.clicked.connect(lambda: self.auto_hue(240))
        btn_layout.addWidget(self.btn_red)
        btn_layout.addWidget(self.btn_green)
        btn_layout.addWidget(self.btn_blue)
        color_form.addRow("Auto Target:", btn_layout)
        
        self.slider_sat = QSlider(Qt.Horizontal)
        self.slider_sat.setRange(0, 200)
        self.slider_sat.setValue(100)
        self.slider_sat.valueChanged.connect(self.update_renderer)
        color_form.addRow("Saturation:", self.slider_sat)
        
        self.slider_exp = QSlider(Qt.Horizontal)
        self.slider_exp.setRange(-100, 100)
        self.slider_exp.setValue(0)
        self.slider_exp.valueChanged.connect(self.update_renderer)
        color_form.addRow("Exposure:", self.slider_exp)
        
        self.slider_bal_r = QSlider(Qt.Horizontal)
        self.slider_bal_r.setRange(-100, 100)
        self.slider_bal_r.setValue(0)
        self.slider_bal_r.valueChanged.connect(self.update_renderer)
        color_form.addRow("Balance R:", self.slider_bal_r)
        
        self.slider_bal_g = QSlider(Qt.Horizontal)
        self.slider_bal_g.setRange(-100, 100)
        self.slider_bal_g.setValue(0)
        self.slider_bal_g.valueChanged.connect(self.update_renderer)
        color_form.addRow("Balance G:", self.slider_bal_g)
        
        self.slider_bal_b = QSlider(Qt.Horizontal)
        self.slider_bal_b.setRange(-100, 100)
        self.slider_bal_b.setValue(0)
        self.slider_bal_b.valueChanged.connect(self.update_renderer)
        color_form.addRow("Balance B:", self.slider_bal_b)
        
        control_layout.addWidget(color_group)
        control_layout.addStretch()
        control_layout.addWidget(self.btn_export)
        
        # Right Panel (GL View)
        self.renderer = PBRRenderer()
        self.renderer.parent_window = self
        
        # Adding wheel zoom logic directly to widget
        self.renderer.zoom = 1.0
        def wheelEvent_override(event):
            delta = event.angleDelta().y()
            if delta > 0: self.renderer.zoom *= 1.1
            else: self.renderer.zoom /= 1.1
            self.renderer.zoom = max(0.2, min(self.renderer.zoom, 10.0))
            self.renderer.request_render()
        self.renderer.wheelEvent = wheelEvent_override
        
        layout.addWidget(control_panel)
        layout.addWidget(self.renderer, 1) # Give it stretch factor
        
        # Data
        self.albedo_np = np.zeros((1024, 1024, 3), dtype=np.float32)
        self.normal_np = np.zeros((1024, 1024, 3), dtype=np.float32)
        self.height_np = np.zeros((1024, 1024, 1), dtype=np.float32)
        self.custom_maps = [] # List of {"name": str, "np": data}
        
    def refresh_view_modes(self):
        self.combo_view.blockSignals(True)
        self.combo_view.clear()
        self.combo_view.addItems(["View Albedo", "View Normal", "View Height"])
        for m in getattr(self, "custom_maps", []):
            self.combo_view.addItem("View " + m["name"])
            
        if hasattr(self, 'renderer'):
            idx = self.renderer.view_mode
            if idx < self.combo_view.count():
                self.combo_view.setCurrentIndex(idx)
            else:
                self.combo_view.setCurrentIndex(0)
                self.renderer.view_mode = 0
            
        self.combo_view.blockSignals(False)
        
    def read_image_data(self, file_name):
        img = None
        try:
            import cPy.cIO
            import cPy.cImage
            
            c_img = cPy.cImage.cImage()
            if cPy.cIO.cIO.LoadImage(file_name, c_img):
                img_arr = np.asarray(c_img).copy()
                
                # Normalize to float32 0..1
                if img_arr.dtype == np.uint8:
                    img_arr = img_arr.astype(np.float32) / 255.0
                elif img_arr.dtype == np.uint16:
                    img_arr = img_arr.astype(np.float32) / 65535.0
                else:
                    img_arr = img_arr.astype(np.float32)
                    
                # Handle channels
                if len(img_arr.shape) == 2:
                    img_arr = np.expand_dims(img_arr, axis=2)
                if img_arr.shape[2] == 1:
                    img_arr = np.repeat(img_arr, 3, axis=2)
                    
                img = img_arr[:, :, :3]
        except:
            pass
            
        if img is None:
            # Fallback to QImage
            qimg = QImage(file_name)
            if qimg.isNull():
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.critical(self, "Error", f"Failed to load image from:\n{file_name}\n\nPlease check if the file format is supported.")
                return None

            qimg = qimg.convertToFormat(QImage.Format_RGBA8888)
            w, h = qimg.width(), qimg.height()
            
            ptr = qimg.constBits()
            img = np.array(ptr).reshape((h, w, 4))
            img = img[:, :, :3].astype(np.float32) / 255.0
            
        return img
        
    def add_custom_map(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Custom Map", "", "Images (*.png *.jpg *.jpeg *.tif *.exr *.tga *.avif)")
        if not file_name: return
        
        from PySide6.QtWidgets import QInputDialog
        name, ok = QInputDialog.getText(self, "Custom Map Name", "Enter a name for this custom map (e.g. Roughness):")
        if not ok or not name.strip(): return
        
        img = self.read_image_data(file_name)
        if img is not None:
            self.custom_maps.append({"name": name.strip(), "np": img})
            self.refresh_view_modes()
            self.push_textures_to_renderer()
            
    def load_texture(self, t_type):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.tif *.exr *.tga *.avif)")
        if not file_name: return
        
        img = self.read_image_data(file_name)
        if img is None: return
        
        if t_type == "albedo": self.albedo_np = img
        elif t_type == "normal": self.normal_np = img
        elif t_type == "height": 
            self.height_np = img[:, :, 0:1] # Just take red channel
            self.chk_height_blend.setChecked(True)
            
        self.push_textures_to_renderer()
        self.update_renderer()
        
    def push_textures_to_renderer(self):
        c_nps = [m["np"] for m in getattr(self, "custom_maps", [])]
        self.renderer.set_textures(self.albedo_np, self.normal_np, self.height_np, c_nps)
        
    def auto_hue(self, target_hue):
        if getattr(self, 'albedo_np', None) is None or self.albedo_np.size == 0:
            return
        avg_rgb = self.albedo_np.mean(axis=(0,1))
        import colorsys
        h, s, v = colorsys.rgb_to_hsv(avg_rgb[0], avg_rgb[1], avg_rgb[2])
        current_hue = h * 360.0
        shift = target_hue - current_hue
        if shift > 180: shift -= 360
        if shift < -180: shift += 360
        shift_int = int(max(-180, min(180, shift)))
        self.slider_hue.setValue(shift_int)
        
        # Calculate new average RGB after exact per-pixel hue shift
        import numpy as np
        if HAS_CV2:
            import cv2
            albedo_u8 = (self.albedo_np * 255).astype(np.uint8)
            hsv_np = cv2.cvtColor(albedo_u8, cv2.COLOR_RGB2HSV) # OpenCV uses H:0-179
            
            # Add hue shift (OpenCV hue is 0-179, so shift_int / 2)
            cv2_shift = int(shift_int / 2.0)
            h_chan = hsv_np[:, :, 0].astype(np.int16)
            h_chan = (h_chan + cv2_shift) % 180
            hsv_np[:, :, 0] = h_chan.astype(np.uint8)
            
            shifted_rgb = cv2.cvtColor(hsv_np, cv2.COLOR_HSV2RGB)
            new_r, new_g, new_b = shifted_rgb.mean(axis=(0,1)) / 255.0
        else:
            new_h = (h + shift_int / 360.0) % 1.0
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)
        
        bal_r, bal_g, bal_b = 0.0, 0.0, 0.0
        if target_hue == 0: # Red
            avg_gb = (new_g + new_b) / 2.0
            if new_g > 0: bal_g = (avg_gb / new_g - 1.0) * 100
            if new_b > 0: bal_b = (avg_gb / new_b - 1.0) * 100
        elif target_hue == 120: # Green
            avg_rb = (new_r + new_b) / 2.0
            if new_r > 0: bal_r = (avg_rb / new_r - 1.0) * 100
            if new_b > 0: bal_b = (avg_rb / new_b - 1.0) * 100
        elif target_hue == 240: # Blue
            avg_rg = (new_r + new_g) / 2.0
            if new_r > 0: bal_r = (avg_rg / new_r - 1.0) * 100
            if new_g > 0: bal_g = (avg_rg / new_g - 1.0) * 100
            
        self.slider_bal_r.setValue(int(max(-100, min(100, bal_r))))
        self.slider_bal_g.setValue(int(max(-100, min(100, bal_g))))
        self.slider_bal_b.setValue(int(max(-100, min(100, bal_b))))
            
    def update_view_mode(self, index):
        self.renderer.view_mode = index
        self.renderer.request_render()
        
    def update_renderer(self):
        h, w = self.albedo_np.shape[:2]
        if w > 0 and h > 0:
            c_l = self.spin_crop_lft.value() / w
            c_r = self.spin_crop_rgt.value() / w
            c_t = self.spin_crop_top.value() / h
            c_b = self.spin_crop_bot.value() / h
            
            self.renderer.crop_offset = (c_l, c_b)
            self.renderer.crop_scale = (max(0.01, 1.0 - c_l - c_r), max(0.01, 1.0 - c_t - c_b))
            
        self.renderer.tiling_mode = 1
        self.renderer.preview_grid = 1
        
        self.renderer.invert_normal_y = 1 if self.chk_invert_y.isChecked() else 0
        self.renderer.rotation_angle = np.radians(self.spin_rot.value())
        
        self.renderer.use_height_blend = 1 if self.chk_height_blend.isChecked() else 0
        self.renderer.height_blend_threshold = self.slider_h_thresh.value() / 100.0
        self.renderer.height_blend_contrast = self.slider_h_contrast.value() / 100.0
        self.renderer.blend_margin = self.spin_blend_margin.value()
        self.renderer.blend_height_influence = self.slider_h_inf.value() / 100.0
        
        self.renderer.tile_offset = (self.spin_offset_x.value() / 100.0, self.spin_offset_y.value() / 100.0)
        
        nw = max(1.0, float(w))
        nh = max(1.0, float(h))
        self.renderer.corners = np.array([
            [(0.0 * nw + self.spin_corn_bl_x.value()) / nw, (0.0 * nh + self.spin_corn_bl_y.value()) / nh], # BL (0, 0)
            [(1.0 * nw + self.spin_corn_br_x.value()) / nw, (0.0 * nh + self.spin_corn_br_y.value()) / nh], # BR (1, 0)
            [(0.0 * nw + self.spin_corn_tl_x.value()) / nw, (1.0 * nh + self.spin_corn_tl_y.value()) / nh], # TL (0, 1)
            [(1.0 * nw + self.spin_corn_tr_x.value()) / nw, (1.0 * nh + self.spin_corn_tr_y.value()) / nh]  # TR (1, 1)
        ], dtype='f4')
        
        self.renderer.eq_albedo_enabled = 1 if self.chk_albedo_eq.isChecked() else 0
        
        self.renderer.eq_albedo_lod_center = float(self.spin_albedo_eq_rad_center.value())
        self.renderer.eq_albedo_lod_edge = float(self.spin_albedo_eq_rad_edge.value())
        
        self.renderer.hue_shift = float(self.slider_hue.value())
        self.renderer.sat_mult = float(self.slider_sat.value()) / 100.0
        self.renderer.exp_shift = float(self.slider_exp.value()) / 100.0 * 2.0
        
        self.renderer.bal_r = 1.0 + float(self.slider_bal_r.value()) / 100.0
        self.renderer.bal_g = 1.0 + float(self.slider_bal_g.value()) / 100.0
        self.renderer.bal_b = 1.0 + float(self.slider_bal_b.value()) / 100.0
        
        self.renderer.request_render()

    def on_micro_radius_changed(self, val):
        found = False
        for m in getattr(self, "custom_maps", []):
            if m["name"] == "MicroprotrusionsColor":
                found = True
                break
        if found:
            self._micro_timer.start(150) # Debounce processing

    def run_microprotrusions(self):
        if not HAS_CV2:
            QMessageBox.warning(self, "Missing Dependency", "OpenCV is required for this operation.")
            return
            
        if getattr(self, 'albedo_np', None) is None or self.albedo_np.size == 0:
            return
            
        import cv2
        radius = self.spin_micro_radius.value()
        samples = self.spin_micro_samples.value()
        
        # Pad with wrap around to ensure seamless generation
        padded = cv2.copyMakeBorder(self.albedo_np, radius, radius, radius, radius, cv2.BORDER_WRAP)
        h, w = self.albedo_np.shape[:2]
        
        if samples == 0:
            k_size = radius * 2 + 1
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k_size, k_size))
            dilated = cv2.dilate(padded, kernel)
            micro = dilated[radius:radius+h, radius:radius+w]
        elif samples == 1:
            micro = self.albedo_np.copy()
        else:
            micro = np.zeros_like(self.albedo_np)
            step = (2 * radius) / (samples - 1)
            for i in range(samples):
                for j in range(samples):
                    dy = int(round(-radius + i * step))
                    dx = int(round(-radius + j * step))
                    
                    y_start = radius + dy
                    x_start = radius + dx
                    shifted = padded[y_start:y_start+h, x_start:x_start+w]
                    micro = np.maximum(micro, shifted)
        
        # Update or add to custom maps
        found = False
        for m in self.custom_maps:
            if m["name"] == "MicroprotrusionsColor":
                m["np"] = micro
                found = True
                break
                
        if not found:
            self.custom_maps.append({"name": "MicroprotrusionsColor", "np": micro})
            self.refresh_view_modes()
            
        self.push_textures_to_renderer()
        
        # Switch view to MicroprotrusionsColor
        for i in range(self.combo_view.count()):
            if self.combo_view.itemText(i) == "View MicroprotrusionsColor":
                self.combo_view.setCurrentIndex(i)
                break
                
        self.renderer.request_render()

    def run_normal_to_height(self):
        norm_to_process = self.normal_np.copy()
        
        # Address defective source boundary clamping
        norm_to_process[0:2, :] = norm_to_process[2:3, :]
        norm_to_process[-2:, :] = norm_to_process[-3:-2, :]
        norm_to_process[:, 0:2] = norm_to_process[:, 2:3]
        norm_to_process[:, -2:] = norm_to_process[:, -3:-2]
        
        if self.chk_invert_y.isChecked():
            norm_to_process[:,:,1] = 1.0 - norm_to_process[:,:,1]
            
        height = frankot_chellappa(norm_to_process)
        
        radius_c = self.spin_hp_radius_center.value()
        radius_e = self.spin_hp_radius_edge.value()
        margin = 4 # Base margin for FFT ring tolerance
        
        if (radius_c > 0 or radius_e > 0) and HAS_CV2:
            import cv2
            h_h, h_w = height.shape
            
            if radius_c == radius_e:
                k_size = radius_c * 2 + 1
                blurred = cv2.GaussianBlur(height, (k_size, k_size), 0, borderType=cv2.BORDER_REPLICATE)
            else:
                if radius_c > 0:
                    k_c = radius_c * 2 + 1
                    blur_c = cv2.GaussianBlur(height, (k_c, k_c), 0, borderType=cv2.BORDER_REPLICATE)
                else:
                    blur_c = height.copy()
                    
                if radius_e > 0:
                    k_e = radius_e * 2 + 1
                    blur_e = cv2.GaussianBlur(height, (k_e, k_e), 0, borderType=cv2.BORDER_REPLICATE)
                else:
                    blur_e = height.copy()
                    
                y_indices, x_indices = np.indices((h_h, h_w))
                y_norm = (y_indices / (h_h - 1)) * 2.0 - 1.0
                x_norm = (x_indices / (h_w - 1)) * 2.0 - 1.0
                dist_to_edge = np.maximum(np.abs(x_norm), np.abs(y_norm))
                mask = 3.0 * (dist_to_edge ** 2) - 2.0 * (dist_to_edge ** 3) # smoothstep
                
                blurred = blur_c * (1.0 - mask) + blur_e * mask
                
            height = (height - blurred) + 0.5
            margin = max(radius_c, radius_e)
            
        # Auto Levels taking care to ignore margin halos
        h_h, h_w = height.shape
        my = min(margin, h_h // 3)
        mx = min(margin, h_w // 3)
        
        valid_area = height[my:h_h-my, mx:h_w-mx]
        if valid_area.size > 0:
            h_min, h_max = valid_area.min(), valid_area.max()
            if h_max > h_min:
                height = (height - h_min) / (h_max - h_min)
                
        height = np.clip(height, 0.0, 1.0)
            
        self.height_np = np.expand_dims(height, axis=2)
        
        self.chk_height_blend.setChecked(True)
        
        self.renderer.set_textures(self.albedo_np, self.normal_np, self.height_np)
        self.combo_view.setCurrentIndex(2) # View Height
        self.renderer.request_render() 
    def export_textures(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Export Folder")
        if not folder: return
        import os
        
        old_mode = self.renderer.view_mode
        self.renderer.preview_grid = 0
        try:
            res_w = int(self.combo_export_w.currentText())
            res_h = int(self.combo_export_h.currentText())
        except ValueError:
            res_w = 4096
            res_h = 4096
            
        exports = [
            ("Albedo", 0),
            ("Normal", 1),
            ("Height", 2)
        ]
        
        for idx, m in enumerate(getattr(self, "custom_maps", [])):
            exports.append((m["name"], 3 + idx))
            
        for name, v_mode in exports:
            self.renderer.view_mode = v_mode
            img = self.renderer.export_to_qimage(res_w, res_h)
            if img: img.save(os.path.join(folder, f"Tiled_{name}.png"))
        
        self.renderer.view_mode = old_mode
        self.renderer.preview_grid = 1
        self.renderer.request_render()
        
        QMessageBox.information(self, "Export Complete", f"Textures successfully exported to:\n{folder}\nat {res_w}x{res_h} resolution!")
