import os
import sys
import numpy as np
import traceback
from pathlib import Path

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                               QLabel, QFileDialog, QCheckBox, QListWidget, QSpinBox, 
                               QMessageBox, QApplication, QMainWindow, QGroupBox, 
                               QLineEdit, QListWidgetItem, QRadioButton, QColorDialog)
from PySide6.QtGui import QColor
from cModules.QT import QT

try:
    import coat
    import cPy.cCore
    import cPy.cIO
    import cPy.cImage
    import cPy.CoreAPI
    from cTemplates.Structs import d_slot, d_menu_section
    import cTemplates.MainMenu.Scripts
    import cModules.AVIF.AVIF as AVIF_Module
except ImportError:
    pass

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
QLineEdit {
    background-color: #1e1e1e;
    border: 1px solid #383838;
    color: #ffffff;
    padding: 2px;
    border-radius: 2px;
}
"""

class SuffixRuleWidget(QWidget):
    def __init__(self, parent_list, item_ref):
        super().__init__()
        self.parent_list = parent_list
        self.item_ref = item_ref
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        
        layout.addWidget(QLabel("Suffix:"))
        self.le_suffix = QLineEdit()
        self.le_suffix.setPlaceholderText("e.g. _H")
        self.le_suffix.setFixedWidth(80)
        layout.addWidget(self.le_suffix)
        
        layout.addWidget(QLabel("Quality:"))
        self.spin_quality = QSpinBox()
        self.spin_quality.setRange(0, 100)
        self.spin_quality.setValue(95)
        layout.addWidget(self.spin_quality)
        
        self.chk_force8bit = QCheckBox("Force 8-bit")
        self.chk_force8bit.setChecked(False)
        layout.addWidget(self.chk_force8bit)
        
        self.chk_normalize = QCheckBox("Norm")
        self.chk_normalize.setChecked(False)
        layout.addWidget(self.chk_normalize)
        
        self.btn_wb = QPushButton("WB")
        self.btn_wb.setFixedWidth(35)
        self.btn_wb.setStyleSheet("background-color: #ffffff; color: #000; border-radius: 2px;")
        self.btn_wb.clicked.connect(self.pick_wb_color)
        self.wb_color = (255, 255, 255)
        layout.addWidget(self.btn_wb)
        
        self.chk_srgb = QCheckBox("sRGB")
        self.chk_srgb.setChecked(True)
        layout.addWidget(self.chk_srgb)
        
        btn_remove = QPushButton("X")
        btn_remove.setFixedWidth(30)
        btn_remove.clicked.connect(self.remove_self)
        layout.addWidget(btn_remove)
        
    def remove_self(self):
        row = self.parent_list.row(self.item_ref)
        self.parent_list.takeItem(row)

    def pick_wb_color(self):
        color = QColorDialog.getColor(QColor(*self.wb_color), self, "Select White Balance Reference")
        if color.isValid():
            self.wb_color = (color.red(), color.green(), color.blue())
            text_col = "#000" if (color.red()*0.299 + color.green()*0.587 + color.blue()*0.114) > 128 else "#fff"
            self.btn_wb.setStyleSheet(f"background-color: {color.name()}; color: {text_col}; border-radius: 2px;")


class AvifConvertorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart AVIF Convertor")
        self.resize(600, 550)
        self.setStyleSheet(DARK_THEME_QSS)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Source Selection
        src_group = QGroupBox("Target Source")
        src_layout = QVBoxLayout(src_group)
        
        mode_layout = QHBoxLayout()
        self.radio_files = QRadioButton("Select Files")
        self.radio_folder = QRadioButton("Select Folder")
        self.radio_files.setChecked(True)
        mode_layout.addWidget(self.radio_files)
        mode_layout.addWidget(self.radio_folder)
        src_layout.addLayout(mode_layout)
        
        self.chk_recursive = QCheckBox("Recursive Search (For Folders)")
        self.chk_recursive.setChecked(False)
        src_layout.addWidget(self.chk_recursive)
        layout.addWidget(src_group)
        
        # Global Settings
        global_group = QGroupBox("Global Processing Settings")
        global_layout = QHBoxLayout(global_group)
        
        self.chk_global_pow2 = QCheckBox("Force Power-of-2 Resizing")
        self.chk_global_pow2.setChecked(True)
        global_layout.addWidget(self.chk_global_pow2)
        
        layout.addWidget(global_group)
        
        # Default Settings
        def_group = QGroupBox("Default Settings (applied if no suffix matches)")
        def_layout = QHBoxLayout(def_group)
        
        def_layout.addWidget(QLabel("Quality:"))
        self.spin_def_quality = QSpinBox()
        self.spin_def_quality.setRange(0, 100)
        self.spin_def_quality.setValue(80)
        def_layout.addWidget(self.spin_def_quality)
        
        def_layout.addWidget(QLabel("Speed (0-10):"))
        self.spin_def_speed = QSpinBox()
        self.spin_def_speed.setRange(0, 10)
        self.spin_def_speed.setValue(3)
        def_layout.addWidget(self.spin_def_speed)
        
        self.chk_def_force8bit = QCheckBox("Force 8-bit")
        self.chk_def_force8bit.setChecked(True)
        def_layout.addWidget(self.chk_def_force8bit)
        
        self.chk_def_normalize = QCheckBox("Norm")
        self.chk_def_normalize.setChecked(False)
        def_layout.addWidget(self.chk_def_normalize)
        
        self.btn_def_wb = QPushButton("WB")
        self.btn_def_wb.setFixedWidth(35)
        self.btn_def_wb.setStyleSheet("background-color: #ffffff; color: #000; border-radius: 2px;")
        self.btn_def_wb.clicked.connect(self.pick_def_wb_color)
        self.def_wb_color = (255, 255, 255)
        def_layout.addWidget(self.btn_def_wb)
        
        self.chk_def_srgb = QCheckBox("sRGB")
        self.chk_def_srgb.setChecked(True)
        def_layout.addWidget(self.chk_def_srgb)
        
        layout.addWidget(def_group)
        
        # Suffix Rules
        rules_group = QGroupBox("Custom Suffix Rules")
        rules_layout = QVBoxLayout(rules_group)
        
        self.list_rules = QListWidget()
        rules_layout.addWidget(self.list_rules)
        
        btn_add_rule = QPushButton("Add Suffix Rule")
        btn_add_rule.clicked.connect(lambda: self.add_rule())
        rules_layout.addWidget(btn_add_rule)
        
        layout.addWidget(rules_group)
        
        # Add default rules
        self.add_rule(suffix="_H", quality=95, force_8bit=False, normalize=True, srgb=False)
        self.add_rule(suffix="_N", quality=95, force_8bit=False, normalize=False, srgb=False)
        
        # Process Button
        self.btn_process = QPushButton("Process Conversions")
        self.btn_process.setMinimumHeight(45)
        self.btn_process.clicked.connect(self.start_conversion)
        layout.addWidget(self.btn_process)

    def pick_def_wb_color(self):
        color = QColorDialog.getColor(QColor(*self.def_wb_color), self, "Select White Balance Reference")
        if color.isValid():
            self.def_wb_color = (color.red(), color.green(), color.blue())
            text_col = "#000" if (color.red()*0.299 + color.green()*0.587 + color.blue()*0.114) > 128 else "#fff"
            self.btn_def_wb.setStyleSheet(f"background-color: {color.name()}; color: {text_col}; border-radius: 2px;")

    def add_rule(self, suffix="", quality=95, force_8bit=False, normalize=False, wb_color=(255,255,255), srgb=True):
        item = QListWidgetItem(self.list_rules)
        widget = SuffixRuleWidget(self.list_rules, item)
        widget.le_suffix.setText(suffix)
        widget.spin_quality.setValue(quality)
        widget.chk_force8bit.setChecked(force_8bit)
        widget.chk_normalize.setChecked(normalize)
        
        widget.wb_color = wb_color
        text_col = "#000" if (wb_color[0]*0.299 + wb_color[1]*0.587 + wb_color[2]*0.114) > 128 else "#fff"
        widget.btn_wb.setStyleSheet(f"background-color: {'#%02x%02x%02x' % wb_color}; color: {text_col}; border-radius: 2px;")
        widget.chk_srgb.setChecked(srgb)
        
        item.setSizeHint(widget.sizeHint())
        self.list_rules.setItemWidget(item, widget)

    def get_rules(self):
        rules = []
        for i in range(self.list_rules.count()):
            item = self.list_rules.item(i)
            widget = self.list_rules.itemWidget(item)
            if widget and widget.le_suffix.text().strip():
                rules.append({
                    "suffix": widget.le_suffix.text().strip(),
                    "quality": widget.spin_quality.value(),
                    "force_8bit": widget.chk_force8bit.isChecked(),
                    "normalize": widget.chk_normalize.isChecked(),
                    "wb_color": widget.wb_color,
                    "srgb": widget.chk_srgb.isChecked()
                })
        return rules

    def start_conversion(self):
        target_extensions = {'.jpg', '.jpeg', '.png', '.avif', '.tif', '.tiff', '.tga', '.exr'}
        files_to_convert = []

        if self.radio_files.isChecked():
            files, _ = QFileDialog.getOpenFileNames(self, "Select Images to Convert", "", "Images (*.png *.jpg *.jpeg *.tif *.tiff *.tga *.avif *.exr)")
            if not files: return
            files_to_convert = [Path(f) for f in files]
        else:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder to Convert")
            if not folder_path: return
            
            search_path = Path(folder_path)
            iterator = search_path.rglob('*') if self.chk_recursive.isChecked() else search_path.iterdir()
            
            for p in iterator:
                if p.is_file() and p.suffix.lower() in target_extensions:
                    files_to_convert.append(p)
                    
        if len(files_to_convert) == 0:
            QMessageBox.information(self, "Info", "No compatible files found.")
            return

        rules = self.get_rules()
        def_qual = self.spin_def_quality.value()
        def_spd = self.spin_def_speed.value()
        def_8bit = self.chk_def_force8bit.isChecked()
        
        self.btn_process.setEnabled(False)
        self.btn_process.setText("Converting...")
        QApplication.processEvents()
        
        errors = 0
        total = len(files_to_convert)
        
        try:
            for idx, file_path in enumerate(files_to_convert):
                coat.io.progressBar(idx, total, f"Converting {file_path.name}")
                self.btn_process.setText(f"Converting {idx+1}/{total}...")
                QApplication.processEvents()
                
                # Match Suffix Rules
                name_stem = file_path.stem
                applied_quality = def_qual
                applied_speed = def_spd
                applied_8bit = def_8bit
                applied_normalize = self.chk_def_normalize.isChecked()
                applied_wb = self.def_wb_color
                applied_srgb = self.chk_def_srgb.isChecked()
                
                for rule in rules:
                    if name_stem.endswith(rule['suffix']):
                        applied_quality = rule['quality']
                        applied_8bit = rule['force_8bit']
                        applied_normalize = rule['normalize']
                        applied_wb = rule['wb_color']
                        applied_srgb = rule['srgb']
                        # Speed is kept global
                        break
                        
                dst_path = file_path.with_suffix(".avif")
                
                # Load Image
                c_img = cPy.cImage.cImage()
                if not cPy.cIO.cIO.LoadImage(str(file_path), c_img):
                    print(f"Failed to load: {file_path}")
                    errors += 1
                    continue
                    
                # White Balance
                if applied_wb != (255, 255, 255):
                    arr = np.asarray(c_img).copy()
                    
                    if arr.dtype == np.uint8: scale = 255.0
                    elif arr.dtype == np.uint16: scale = 65535.0
                    else: scale = 1.0
                    
                    arr_f = arr.astype(np.float32) / scale
                    
                    wb_sample = np.array(applied_wb, dtype=np.float32) / 255.0 
                    wb_sample = np.clip(wb_sample, 0.001, 1.0)
                    
                    if applied_srgb:
                        arr_f[..., :3] = np.power(arr_f[..., :3].clip(0.0), 2.2)
                        wb_sample = np.power(wb_sample, 2.2)
                        
                    arr_f[..., :3] = arr_f[..., :3] / wb_sample
                    
                    if applied_srgb:
                        arr_f[..., :3] = np.power(arr_f[..., :3].clip(0.0), 1.0/2.2)
                        
                    arr_f = arr_f * scale
                    
                    if arr.dtype == np.uint8:
                        arr = arr_f.clip(0, 255).astype(np.uint8)
                    elif arr.dtype == np.uint16:
                        arr = arr_f.clip(0, 65535).astype(np.uint16)
                    else:
                        arr = arr_f.astype(np.float32)
                        
                    cPy.CoreAPI.Image.cImageFromArray(np.ascontiguousarray(arr), c_img)
                
                # Normalization
                if applied_normalize:
                    arr = np.asarray(c_img).copy()
                    amin, amax = arr.min(), arr.max()
                    if amax > amin:
                        if arr.dtype == np.uint16:
                            arr = ((arr.astype(np.float64) - amin) / (amax - amin) * 65535.0).astype(np.uint16)
                        elif arr.dtype == np.uint8:
                            arr = ((arr.astype(np.float64) - amin) / (amax - amin) * 255.0).astype(np.uint8)
                        elif arr.dtype == np.float32:
                            arr = ((arr - amin) / (amax - amin)).astype(np.float32)
                    cPy.CoreAPI.Image.cImageFromArray(np.ascontiguousarray(arr), c_img)
                    
                # Modify bits if force_8bit is True
                if applied_8bit:
                    arr = np.asarray(c_img).copy()
                    needs_update = False
                    if arr.dtype == np.uint16:
                        arr = (arr / 257.0).astype(np.uint8) # proper 16 -> 8 map
                        needs_update = True
                    elif arr.dtype == np.float32:
                        arr = (arr * 255.0).clip(0, 255).astype(np.uint8)
                        needs_update = True
                        
                    if needs_update:
                        cPy.CoreAPI.Image.cImageFromArray(np.ascontiguousarray(arr), c_img)
                        
                # Ensure global properties are set for the AVIF Encode call
                try: 
                    AVIF_Module.avifSettings.power_of_two.Value = self.chk_global_pow2.isChecked()
                except: 
                    pass
                AVIF_Module.avifSettings.quality.Value = applied_quality
                AVIF_Module.avifSettings.speed.Value = applied_speed
                
                # Save
                if not cPy.cIO.cIO.SaveImage(str(dst_path), c_img):
                    print(f"Failed to save AVIF: {dst_path}")
                    errors += 1
                    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error during conversion:\n{e}")
            traceback.print_exc()
        finally:
            coat.io.progressBar(total, total, "Done")
            self.btn_process.setEnabled(True)
            self.btn_process.setText("Process Conversions")
            msg = f"Completed conversion of {total} files."
            if errors > 0: msg += f"\n({errors} errors occurred, check console)"
            QMessageBox.information(self, "Done", msg)


class AvifConvertorExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)

    def onStart(self):
        print("AvifConvertor Plugin starting...")

# Expose Command to UI
@d_slot
def OpenAvifConvertorUI():
    global global_avif_ui
    try:
        if 'global_avif_ui' not in globals() or global_avif_ui is None:
            global_avif_ui = AvifConvertorUI()
        global_avif_ui.show()
    except Exception as e:
        print(f"Error opening UI: {e}")

# Register into Scripts Menu
@d_menu_section(cTemplates.MainMenu.Scripts.Scripts_S_Useful)
def AvifConvertorSection():
    try:
        coat.menu_item(OpenAvifConvertorUI.UICmd()) 
    except Exception as e:
        print(f"Error registering menu: {e}")

# IMPORTANT: instantiate the extension
avifConvertorExt = AvifConvertorExtension()
