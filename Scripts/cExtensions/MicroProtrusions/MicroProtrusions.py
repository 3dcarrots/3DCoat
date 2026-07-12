import os
import sys
import numpy as np
import math
from pathlib import Path

# PySide6 imports
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                               QLabel, QFileDialog, QCheckBox, QListWidget, QDoubleSpinBox, 
                               QMessageBox, QApplication, QMainWindow, QGroupBox, QRadioButton, QSpinBox, QComboBox)
from PySide6.QtCore import Qt
from cModules.QT import QT

# 3DCoat internal imports
try:
    import coat
    import cPy.cCore
    import cPy.cIO
    import cPy.cImage
    import cPy.CoreAPI
    from cTemplates.Structs import d_slot, d_menu_section
    import cTemplates.MainMenu.Scripts
except ImportError:
    # Allow logic testing outside of 3DCoat
    pass

class MicroProtrusionsUI(QMainWindow):
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
    QCheckBox, QRadioButton {
        background: transparent;
        spacing: 8px;
    }
    QRadioButton::indicator {
        width: 12px;
        height: 12px;
        border-radius: 7px;
        border: 1px solid #808080;
        background: #1e1e1e;
    }
    QRadioButton::indicator:checked {
        background: #5c7a90;
        border: 3px solid #1e1e1e;
    }
    QCheckBox::indicator {
        width: 12px;
        height: 12px;
        border-radius: 2px;
        border: 1px solid #808080;
        background: #1e1e1e;
    }
    QCheckBox::indicator:checked {
        background: #5c7a90;
        border: 3px solid #1e1e1e;
    }
    QPushButton {
        background-color: #383838;
        border: 1px solid #1e1e1e;
        color: #d0d0d0;
        padding: 6px 15px;
        border-radius: 3px;
    }
    QPushButton:hover {
        background-color: #444444;
    }
    QPushButton:pressed {
        background-color: #5c7a90;
        color: #ffffff;
    }
    QListWidget {
        background-color: #1e1e1e;
        border: 1px solid #383838;
        color: #ffffff;
    }
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

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Micro-Protrusions Filter")
        self.resize(500, 500)
        self.setStyleSheet(self.DARK_THEME_QSS)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Mode Selection
        mode_group = QGroupBox("Relief Map Type")
        mode_layout = QHBoxLayout(mode_group)
        self.radio_height = QRadioButton("Height Map")
        self.radio_normal = QRadioButton("Normal Map")
        self.radio_height.setChecked(True)
        mode_layout.addWidget(self.radio_height)
        mode_layout.addWidget(self.radio_normal)
        layout.addWidget(mode_group)
        
        # Relief Map Input
        relief_layout = QHBoxLayout()
        self.lbl_relief = QLabel("Relief Map: None")
        btn_relief = QPushButton("Load Relief Map...")
        btn_relief.clicked.connect(self.load_relief_map)
        relief_layout.addWidget(self.lbl_relief)
        relief_layout.addWidget(btn_relief)
        layout.addLayout(relief_layout)
        
        # Target Maps Input
        layout.addWidget(QLabel("Target Maps (Albedo, Gloss, etc.):"))
        self.list_targets = QListWidget()
        layout.addWidget(self.list_targets)
        
        btn_target = QPushButton("Add Target Maps...")
        btn_target.clicked.connect(self.add_target_maps)
        layout.addWidget(btn_target)
        
        btn_remove = QPushButton("Remove Selected Target")
        btn_remove.clicked.connect(self.remove_target_map)
        layout.addWidget(btn_remove)
        
        # Options
        options_group = QGroupBox("Processing Options")
        options_layout = QVBoxLayout(options_group)
        
        # General Processing Options
        ds_layout = QHBoxLayout()
        ds_layout.addWidget(QLabel("Target Downsampling Ratio:"))
        self.combo_ds = QComboBox()
        self.combo_ds.addItems(["1x (No downsample)", "2x", "4x", "8x", "16x", "32x"])
        self.combo_ds.setCurrentText("8x")
        ds_layout.addWidget(self.combo_ds)
        options_layout.addLayout(ds_layout)

        # Normal map specific options
        self.chk_invert_y = QCheckBox("Invert Y (Green) - For Normal Maps")
        
        shift_layout = QHBoxLayout()
        shift_layout.addWidget(QLabel("Displacement Distance:"))
        self.spin_shift = QDoubleSpinBox()
        self.spin_shift.setRange(0.0, 1000.0)
        self.spin_shift.setValue(10.0)
        shift_layout.addWidget(self.spin_shift)
        
        options_layout.addWidget(self.chk_invert_y)
        options_layout.addLayout(shift_layout)
        
        # Height map specific options
        power_layout = QHBoxLayout()
        power_layout.addWidget(QLabel("Height Map Weight Power (higher = preserves only highest peaks):"))
        self.spin_power = QDoubleSpinBox()
        self.spin_power.setRange(1.0, 10.0)
        self.spin_power.setValue(2.0)
        self.spin_power.setSingleStep(0.5)
        power_layout.addWidget(self.spin_power)
        options_layout.addLayout(power_layout)
        
        layout.addWidget(options_group)
        
        # Process Button
        self.btn_process = QPushButton("Process & Save Maps")
        self.btn_process.setMinimumHeight(50)
        self.btn_process.clicked.connect(self.process_maps)
        layout.addWidget(self.btn_process)
        
        self.relief_path = ""
        self.target_paths = []

    def load_relief_map(self):
        f, _ = QFileDialog.getOpenFileName(self, "Select Relief Map", "", "Images (*.png *.jpg *.jpeg *.tif *.tiff *.avif)")
        if f:
            self.relief_path = f
            self.lbl_relief.setText(f"Relief Map: {Path(f).name}")

    def add_target_maps(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Target Maps", "", "Images (*.png *.jpg *.jpeg *.tif *.tiff *.avif)")
        for f in files:
            if f not in self.target_paths:
                self.target_paths.append(f)
                self.list_targets.addItem(f)

    def remove_target_map(self):
        selected = self.list_targets.selectedItems()
        if not selected: return
        for item in selected:
            row = self.list_targets.row(item)
            self.list_targets.takeItem(row)
            self.target_paths.pop(row)

    def process_maps(self):
        if not self.relief_path:
            QMessageBox.warning(self, "Error", "Please select a Relief Map first.")
            return
        if not self.target_paths:
            QMessageBox.warning(self, "Error", "Please select at least one Target Map.")
            return
        
        try:
            self.btn_process.setText("Processing...")
            self.btn_process.setEnabled(False)
            QApplication.processEvents()
            
            # Load Relief Map
            r_cimg = cPy.cImage.cImage()
            if not cPy.cIO.cIO.LoadImage(self.relief_path, r_cimg):
                raise Exception("Failed to load Relief Map")
            relief_arr = np.asarray(r_cimg).copy()
            # If 3DCoat returns rgba, convert appropriately
            
            height, width = relief_arr.shape[:2]
            
            mode_height = self.radio_height.isChecked()
            
            ds_text = self.combo_ds.currentText()
            ds_factor = 1 # fallback
            if ds_text.startswith("32x"): ds_factor = 32
            elif ds_text.startswith("16x"): ds_factor = 16
            elif ds_text.startswith("8x"): ds_factor = 8
            elif ds_text.startswith("4x"): ds_factor = 4
            elif ds_text.startswith("2x"): ds_factor = 2

            if mode_height:
                # Downsampling preparation
                new_w = width // ds_factor
                new_h = height // ds_factor
                r_cimg = None # clear memory
                
                # Assume grayscale height map (use r channel if multi)
                if len(relief_arr.shape) == 3:
                    h_arr = relief_arr[:, :, 0].astype(np.float32)
                else:
                    h_arr = relief_arr.astype(np.float32)
                
                # Crop to multiple of ds_factor
                h_arr = h_arr[:new_h*ds_factor, :new_w*ds_factor]
                
                # Reshape to blocks
                if ds_factor > 1:
                    h_blocks = h_arr.reshape(new_h, ds_factor, new_w, ds_factor)
                    
                    block_min = h_blocks.min(axis=(1, 3), keepdims=True)
                    block_max = h_blocks.max(axis=(1, 3), keepdims=True)
                    denom = block_max - block_min
                    denom[denom == 0] = 1.0 # avoid div/0
                    
                    norm_h = (h_blocks - block_min) / denom
                    
                    # Mathematical logic: max(0, (x - 0.5) * 2) ** power
                    # Thus lowest and medium get 0 weight, only highest get >0.
                    power = self.spin_power.value()
                    w_h = np.maximum(0.0, (norm_h - 0.5) * 2.0)
                    weights = w_h ** power
                    
                    sum_w = weights.sum(axis=(1, 3), keepdims=True)
                    sum_w[sum_w == 0] = 1.0
                    weights /= sum_w
                else:
                    weights = None
                
            else:
                # Normal Mode Preparation
                if len(relief_arr.shape) < 3 or relief_arr.shape[2] < 3:
                    raise Exception("Normal map must have at least 3 channels (RGB)")
                
                N = relief_arr[:, :, :3].astype(np.float32) / 255.0
                N_x = N[:, :, 0] * 2.0 - 1.0
                N_y = N[:, :, 1] * 2.0 - 1.0
                N_z = N[:, :, 2] * 2.0 - 1.0
                
                if self.chk_invert_y.isChecked():
                    N_y = -N_y
                    
                dist = self.spin_shift.value()
                
                y_idx, x_idx = np.mgrid[0:height, 0:width]
                
                dst_x = np.round(x_idx + N_x * dist).astype(np.int32)
                dst_y = np.round(y_idx + N_y * dist).astype(np.int32)
                
                valid = (dst_x >= 0) & (dst_x < width) & (dst_y >= 0) & (dst_y < height)
                
                src_flat = (y_idx[valid] * width + x_idx[valid])
                dst_flat = (dst_y[valid] * width + dst_x[valid])
                z_flat = N_z[valid]
                
                # Sort by Z so higher Z overwrites
                order = np.argsort(z_flat)
                src_idx_sorted = src_flat[order]
                dst_idx_sorted = dst_flat[order]
            
            output_folder = QFileDialog.getExistingDirectory(self, "Select Output Folder for Processed Maps")
            if not output_folder:
                return # cancelled
                
            # Process Target Maps
            for idx, path in enumerate(self.target_paths):
                # Inform via UI
                self.btn_process.setText(f"Processing {idx+1}/{len(self.target_paths)}...")
                QApplication.processEvents()
                
                t_cimg = cPy.cImage.cImage()
                if not cPy.cIO.cIO.LoadImage(path, t_cimg):
                    print(f"Skipping {path}, could not load.")
                    continue
                    
                t_arr = np.asarray(t_cimg).copy()
                
                # Check for resolution mismatch and resize if needed
                if t_arr.shape[:2] != (height, width):
                    try:
                        import cv2
                        t_arr_contig = np.ascontiguousarray(t_arr)
                        t_arr = cv2.resize(t_arr_contig, (width, height), interpolation=cv2.INTER_LINEAR)
                    except ImportError:
                        from PIL import Image as PILImage
                        is_multi = len(t_arr.shape) > 2
                        if t_arr.dtype == np.uint8:
                            img = PILImage.fromarray(t_arr)
                            img = img.resize((width, height), PILImage.Resampling.BILINEAR if hasattr(PILImage, 'Resampling') else PILImage.BILINEAR)
                            t_arr = np.array(img)
                        elif t_arr.dtype == np.uint16:
                            if is_multi:
                                res_channels = [np.array(PILImage.fromarray(t_arr[:, :, i]).resize((width, height), PILImage.Resampling.BILINEAR if hasattr(PILImage, 'Resampling') else PILImage.BILINEAR)) for i in range(t_arr.shape[2])]
                                t_arr = np.stack(res_channels, axis=-1)
                            else:
                                img = PILImage.fromarray(t_arr)
                                img = img.resize((width, height), PILImage.Resampling.BILINEAR if hasattr(PILImage, 'Resampling') else PILImage.BILINEAR)
                                t_arr = np.array(img)
                        else:
                            raise Exception("cv2 is required to resize float32/complex target maps to match Relief map dimensions.")
                            
                channels = t_arr.shape[2] if len(t_arr.shape) == 3 else 1
                
                if mode_height:
                    # Height mode logic
                    # Ensure matching multiple of ds_factor
                    if ds_factor > 1:
                        t_arr = t_arr[:new_h*ds_factor, :new_w*ds_factor]
                        if channels == 1:
                            target_blocks = t_arr.reshape(new_h, ds_factor, new_w, ds_factor)
                            weights_exp = weights
                            res = np.sum(target_blocks * weights_exp, axis=(1, 3))
                        else:
                            target_blocks = t_arr.reshape(new_h, ds_factor, new_w, ds_factor, channels)
                            weights_exp = np.expand_dims(weights, axis=4)
                            res = np.sum(target_blocks * weights_exp, axis=(1, 3))
                            
                        res_arr = res.astype(t_arr.dtype)
                    else:
                        res_arr = t_arr
                     
                else:
                    # Normal mode logic
                    Result = np.zeros_like(t_arr)
                    if channels == 1:
                        t_flat = t_arr.flatten()
                        res_flat = Result.flatten()
                        res_flat[dst_idx_sorted] = t_flat[src_idx_sorted]
                    else:
                        t_flat = t_arr.reshape(-1, channels)
                        res_flat = Result.reshape(-1, channels)
                        res_flat[dst_idx_sorted] = t_flat[src_idx_sorted]
                    
                    Result = res_flat.reshape(height, width, channels if channels > 1 else 1)
                    
                    # Fill holes (simple nearest neighbor or left 0s as explicit scatter)
                    # For performance, we leave scattered 0s unless specified otherwise
                    
                    if ds_factor > 1:
                        nw = width // ds_factor
                        nh = height // ds_factor
                        if channels == 1:
                            blk = Result[:nh*ds_factor, :nw*ds_factor].reshape(nh, ds_factor, nw, ds_factor)
                            res_arr = np.mean(blk, axis=(1, 3)).astype(t_arr.dtype)
                        else:
                            blk = Result[:nh*ds_factor, :nw*ds_factor, :].reshape(nh, ds_factor, nw, ds_factor, channels)
                            res_arr = np.mean(blk, axis=(1, 3)).astype(t_arr.dtype)
                    else:
                        res_arr = Result.astype(t_arr.dtype)
                
                # Save out
                out_name = Path(path).stem + "_micro" + Path(path).suffix
                out_path = os.path.join(output_folder, out_name)
                
                # Try writing with cPy.CoreAPI
                res_cimg = cPy.cImage.cImage()
                res_contig = np.ascontiguousarray(res_arr)
                cPy.CoreAPI.Image.cImageFromArray(res_contig, res_cimg)
                cPy.cIO.cIO.SaveImage(out_path, res_cimg)
                
            QMessageBox.information(self, "Success", "Processing complete!")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            import traceback
            traceback.print_exc()
        finally:
            self.btn_process.setEnabled(True)
            self.btn_process.setText("Process & Save Maps")

# Define the Extension Hook for 3DCoat
class MicroProtrusionsExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)
        self.ui_window = None

    def onStart(self):
        print("MicroProtrusions Plugin starting...")

# Expose Command to UI
@d_slot
def OpenMicroProtrusionsUI():
    global global_micro_ui
    try:
        if 'global_micro_ui' not in globals() or global_micro_ui is None:
            global_micro_ui = MicroProtrusionsUI()
        global_micro_ui.show()
    except Exception as e:
        print(f"Error opening UI: {e}")

# Register into the Scripts Menu
@d_menu_section(cTemplates.MainMenu.Scripts.Scripts_S_Useful)
def MicroProtrusionsSection():
    try:
        coat.menu_item(OpenMicroProtrusionsUI.UICmd()) 
    except Exception as e:
        print(f"Error registering menu: {e}")

# IMPORTANT: instantiate the extension
microProtrusionsExtension = MicroProtrusionsExtension()
