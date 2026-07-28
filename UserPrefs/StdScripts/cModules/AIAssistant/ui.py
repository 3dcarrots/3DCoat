import os
import sys

# Import our service later in '__init__' of the UI or directly
from .service import AudioServiceThread

# PySide6 is included with 3DCoat
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QTextBrowser, QLineEdit, QLabel, QApplication, QFileDialog,
    QComboBox
)
from PySide6.QtCore import Qt, Signal, Slot, QTimer, QThread, QRectF
from PySide6.QtGui import QPainter, QColor, QRadialGradient, QPen
import math

class ModelFetchThread(QThread):
    models_fetched = Signal(dict)
    
    def __init__(self, service, api_key):
        super().__init__()
        self.service = service
        self.api_key = api_key
        
    def run(self):
        models_dict = self.service.get_live_models(self.api_key)
        self.models_fetched.emit(models_dict if models_dict else {})

class VoiceVisualizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(60)
        self.amplitude = 0.0
        self.target_amplitude = 0.0
        self.user_amplitude = 0.0
        self.target_user_amplitude = 0.0
        self.is_thinking = False
        self.think_time = 0.0
        
        self.user_was_speaking = False
        self.silence_timer = 0
        self.is_processing = False
        self.processing_timer = 0
        
        self.think_off_timer = QTimer(self)
        self.think_off_timer.setSingleShot(True)
        self.think_off_timer.timeout.connect(self._do_set_thinking_false)
        
        # Timer for smooth animation decay
        self.anim_timer = QTimer(self)
        self.anim_timer.timeout.connect(self.update_animation)
        self.anim_timer.start(30) # ~30 fps
        
    @Slot(float)
    def set_amplitude(self, amp):
        if amp > 0.05:
            self.is_processing = False
        self.target_amplitude = min(1.0, max(0.0, amp))
        
    @Slot(float)
    def set_user_amplitude(self, amp):
        self.target_user_amplitude = min(1.0, max(0.0, amp))
        
    @Slot(bool)
    def set_thinking(self, thinking):
        if thinking:
            self.think_off_timer.stop()
            self.is_thinking = True
            self.is_processing = False
        else:
            # Wait 1000ms before turning off to prevent blinking during rapid tool calls
            self.think_off_timer.start(1000)
            
    def _do_set_thinking_false(self):
        self.is_thinking = False
        
    def update_animation(self):
        self.amplitude += (self.target_amplitude - self.amplitude) * 0.2
        self.target_amplitude *= 0.8
        self.user_amplitude += (self.target_user_amplitude - self.user_amplitude) * 0.2
        self.target_user_amplitude *= 0.8
        
        if self.target_user_amplitude > 0.05:
            self.user_was_speaking = True
            self.silence_timer = 0
            self.is_processing = False
            self.processing_timer = 0
        elif self.user_was_speaking:
            self.silence_timer += 1
            if self.silence_timer > 30: # ~1 second of silence
                self.user_was_speaking = False
                self.is_processing = True
                self.processing_timer = 0
                
        if self.is_processing:
            self.processing_timer += 1
            if self.processing_timer > 150: # Max 5 seconds
                self.is_processing = False
                
        if self.is_thinking:
            self.think_time += 0.15
            
        self.update() # trigger paintEvent
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        rect = self.rect()
        center = rect.center()
        
        # Base size + amplitude modulation
        base_radius = 10
        max_bonus_radius = 20
        
        import math
        amp = 0.0
        colors = []
        if self.user_amplitude > 0.05:
            amp = self.user_amplitude
            colors = [QColor(100, 255, 100, 200), QColor(50, 200, 50, 100), QColor(0, 150, 0, 0)]
        elif self.amplitude > 0.05:
            amp = self.amplitude
            colors = [QColor(100, 150, 255, 200), QColor(150, 100, 255, 100), QColor(200, 100, 255, 0)]
        elif self.is_thinking:
            amp = 0.3 + 0.2 * math.sin(self.think_time)
            colors = [QColor(255, 150, 0, 200), QColor(255, 100, 0, 100), QColor(255, 50, 0, 0)]
        elif self.is_processing:
            amp = 0.2 + 0.1 * math.sin(self.processing_timer * 0.15)
            colors = [QColor(0, 200, 255, 200), QColor(0, 150, 255, 100), QColor(0, 100, 255, 0)] # Cyan
        else:
            amp = 0.0
            colors = [QColor(150, 150, 150, 100), QColor(150, 150, 150, 0)]
            
        current_radius = base_radius + (amp * max_bonus_radius)
        gradient = QRadialGradient(center, current_radius * 2)
        
        if len(colors) == 3:
            gradient.setColorAt(0.0, colors[0])
            gradient.setColorAt(0.5, colors[1])
            gradient.setColorAt(1.0, colors[2])
        else:
            gradient.setColorAt(0.0, colors[0])
            gradient.setColorAt(1.0, colors[1])
            
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(gradient)
        
        draw_rect = QRectF(
            center.x() - current_radius * 2,
            center.y() - current_radius * 2,
            current_radius * 4,
            current_radius * 4
        )
        painter.drawEllipse(draw_rect)

class VoiceAIAssistantUI(QWidget):
    # Signals for cross-thread communication will go here later
    log_message = Signal(str)
    thought_message = Signal(str)
    speech_message = Signal(str)
    user_speech_message = Signal(str, bool)
    turn_complete_signal = Signal()
    connection_failed_signal = Signal()
    audio_level_signal = Signal(float)
    user_audio_level_signal = Signal(float)
    thinking_signal = Signal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gemini Voice AI Assistant")
        self.resize(400, 600)
        
        # Ensure window stays on top of 3DCoat but isn't strictly modal
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        
        self.setup_ui()
        self.setup_connections()
        
        # State tracking
        self.is_listening = False
        self.chat_history = []
        self.current_thought = ""
        self.current_speech = ""
        self.current_user_speech = ""
        
        self.pygments_css = ""
        try:
            from pygments.formatters import HtmlFormatter
            self.pygments_css = HtmlFormatter(style='monokai').get_style_defs('.codehilite')
        except ImportError:
            pass
        
        # Start the background service
        self.service = AudioServiceThread(self)
        self.service.start()
        
        # Auto-refresh models if API key is already loaded
        if self.api_key_input.text().strip():
            QTimer.singleShot(500, self.refresh_models_list)
        
    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        
        # Status Label
        status_layout = QHBoxLayout()
        self.status_label = QLabel("Status: Idle")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-weight: bold; font-size: 14px; padding: 10px;")
        
        self.visualizer = VoiceVisualizer()
        
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.visualizer)
        status_layout.setStretch(0, 1)
        status_layout.setStretch(1, 1)
        
        main_layout.addLayout(status_layout)
        
        import coat
        self.api_key_path = coat.io.documents("UserPrefs/AIAssistant.apikey")
        
        # API Key Input
        api_layout = QHBoxLayout()
        self.api_label = QLabel("API Key:")
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Enter Gemini API Key...")
        self.api_key_input.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        
        # Try load from env or local file
        saved_key = self.load_api_key()
        env_key = os.environ.get("GEMINI_API_KEY", "")
        if saved_key:
            self.api_key_input.setText(saved_key)
        elif env_key:
            self.api_key_input.setText(env_key)
            
        api_layout.addWidget(self.api_label)
        api_layout.addWidget(self.api_key_input)
        
        self.get_key_btn = QPushButton("Get Key")
        self.get_key_btn.setToolTip("Opens Google AI Studio to get your free API Key")
        api_layout.addWidget(self.get_key_btn)
        
        self.save_key_btn = QPushButton("Save Key")
        api_layout.addWidget(self.save_key_btn)
        
        main_layout.addLayout(api_layout)
        
        # API Key Help Text
        self.help_text = QLabel(
            "<small><i>No Key? Click 'Get Key', sign in to Google, click <b>'Create API key'</b>,<br> "
            "then <b>'Create API key in new project'</b> and copy the generated key here.</i></small>"
        )
        self.help_text.setWordWrap(True)
        self.help_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.help_text)
        
        # Model Selection
        model_layout = QHBoxLayout()
        self.model_label = QLabel("Model:")
        self.model_combo = QComboBox()
        
        self.refresh_models_btn = QPushButton("Refresh Models")
        self.refresh_models_btn.setToolTip("Fetches Live-compatible models using your API key")
        
        model_layout.addWidget(self.model_label)
        model_layout.addWidget(self.model_combo)
        model_layout.addWidget(self.refresh_models_btn)
        main_layout.addLayout(model_layout)
        
        # Thinking Profile Selection
        profile_layout = QHBoxLayout()
        self.profile_label = QLabel("Thinking Speed:")
        self.profile_combo = QComboBox()
        self.profile_combo.addItem("Balanced (Default)", "balanced")
        self.profile_combo.addItem("Fast & Intuitive (Less thinking)", "fast")
        self.profile_combo.addItem("Slow & Deep (Step-by-step)", "deep")
        
        profile_layout.addWidget(self.profile_label)
        profile_layout.addWidget(self.profile_combo)
        main_layout.addLayout(profile_layout)
        
        # Connection & Mic Buttons
        btn_layout = QHBoxLayout()
        
        self.connect_btn = QPushButton("\U0001F50C Connect")
        self.connect_btn.setMinimumHeight(40)
        self.connect_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
        btn_layout.addWidget(self.connect_btn)
        
        self.mic_btn = QPushButton("\U0001F399\uFE0F Mute/Unmute Mic")
        self.mic_btn.setMinimumHeight(40)
        self.mic_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.mic_btn.setEnabled(False)  # Disabled until connected
        btn_layout.addWidget(self.mic_btn)
        
        self.speaker_btn = QPushButton("\U0001F50A Speaker On")
        self.speaker_btn.setMinimumHeight(40)
        self.speaker_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.speaker_btn.setEnabled(False)
        btn_layout.addWidget(self.speaker_btn)
        
        main_layout.addLayout(btn_layout)
        
        # History View
        self.history_view = QTextBrowser()
        self.history_view.setPlaceholderText("Dialogue history will appear here...")
        main_layout.addWidget(self.history_view)
        
        # Image Attachment Area
        attachment_layout = QHBoxLayout()
        self.attach_btn = QPushButton("\U0001F4CE Attach Image")
        self.attach_btn.setToolTip("Attach an image to the current context")
        self.attachment_label = QLabel("No attachment")
        
        attachment_layout.addWidget(self.attach_btn)
        attachment_layout.addWidget(self.attachment_label)
        attachment_layout.addStretch()
        main_layout.addLayout(attachment_layout)
        
        # Text Input Area
        input_layout = QHBoxLayout()
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type a command instead of speaking...")
        self.send_btn = QPushButton("Send")
        
        input_layout.addWidget(self.text_input)
        input_layout.addWidget(self.send_btn)
        main_layout.addLayout(input_layout)
        
        # Enable Drag & Drop
        self.setAcceptDrops(True)
        
    def setup_connections(self):
        self.connect_btn.clicked.connect(self.toggle_connection)
        self.mic_btn.clicked.connect(self.toggle_mute)
        self.speaker_btn.clicked.connect(self.toggle_speaker)
        self.attach_btn.clicked.connect(self.browse_attachment)
        self.send_btn.clicked.connect(self.send_text)
        self.text_input.returnPressed.connect(self.send_text)
        self.get_key_btn.clicked.connect(self.open_api_key_page)
        self.save_key_btn.clicked.connect(self.save_api_key)
        self.refresh_models_btn.clicked.connect(self.refresh_models_list)
        self.log_message.connect(self.append_log)
        self.thought_message.connect(self.append_thought)
        self.speech_message.connect(self.append_speech)
        self.user_speech_message.connect(self.append_user_speech)
        self.turn_complete_signal.connect(self.end_turn)
        self.connection_failed_signal.connect(self.on_connection_failed)
        self.audio_level_signal.connect(self.visualizer.set_amplitude)
        self.user_audio_level_signal.connect(self.visualizer.set_user_amplitude)
        self.thinking_signal.connect(self.visualizer.set_thinking)
        
    @Slot()
    def refresh_models_list(self):
        api_key = self.api_key_input.text().strip()
        if not api_key:
            self.append_log("> <b style='color:red;'>Enter API Key first to refresh models.</b>")
            return
            
        self.append_log("> Fetching available models...")
        self.refresh_models_btn.setEnabled(False)
        
        # Use QThread to prevent UI freezing and silent PySide threading crashes
        self.fetch_thread = ModelFetchThread(self.service, api_key)
        self.fetch_thread.models_fetched.connect(self._on_models_fetched)
        self.fetch_thread.finished.connect(self.fetch_thread.deleteLater)
        self.fetch_thread.start()
        
    @Slot(dict)
    def _on_models_fetched(self, models_dict):
        self.refresh_models_btn.setEnabled(True)
        if not models_dict:
            return
            
        self.model_combo.clear()
        
        count = 0
        last_item_idx = -1
        for category, m_list in models_dict.items():
            if m_list:
                # Add separator/category header
                self.model_combo.addItem(f"--- {category} ---", None)
                idx = self.model_combo.count() - 1
                # Disable the separator item
                self.model_combo.setItemData(idx, 0, Qt.ItemDataRole.UserRole - 1) 
                
                for model_id, model_desc in m_list:
                    # Clean display name for known tags
                    display = model_desc
                    self.model_combo.addItem(display, model_id)
                    last_item_idx = self.model_combo.count() - 1
                    count += 1
                    
        self.append_log(f"> <b style='color:green;'>Found {count} Live-compatible models.</b>")
        
        if count == 1 and last_item_idx != -1:
            self.model_combo.setCurrentIndex(last_item_idx)
            self.append_log("> Automatically selected the only available model.")
            api_key = self.api_key_input.text().strip()
            if api_key and not self.is_listening:
                self.append_log("> Auto-connecting to the selected model...")
                QTimer.singleShot(200, self.toggle_connection)
        elif count > 1:
            target_idx = -1
            for i in range(self.model_combo.count()):
                data = self.model_combo.itemData(i)
                if isinstance(data, str) and "gemini-2.5-flash-native-audio-latest" in data:
                    target_idx = i
                    break
            
            if target_idx != -1:
                self.model_combo.setCurrentIndex(target_idx)
                self.append_log("> Automatically selected native audio model.")
                api_key = self.api_key_input.text().strip()
                if api_key and not self.is_listening:
                    self.append_log("> Auto-connecting to the selected model...")
                    QTimer.singleShot(200, self.toggle_connection)

    @Slot()
    def on_connection_failed(self):
        self.is_listening = False
        self.connect_btn.setText("\U0001F50C Connect")
        self.connect_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.mic_btn.setEnabled(False)
        self.mic_btn.setText("\U0001F399\uFE0F Mute/Unmute Mic")
        self.mic_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.speaker_btn.setEnabled(False)
        self.speaker_btn.setText("\U0001F50A Speaker On")
        self.speaker_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.update_status("Idle", "black")
        self.set_connection_ui_visible(True)
        self.service.end_session()
        
    def set_connection_ui_visible(self, visible: bool):
        self.api_label.setVisible(visible)
        self.api_key_input.setVisible(visible)
        self.get_key_btn.setVisible(visible)
        self.save_key_btn.setVisible(visible)
        self.help_text.setVisible(visible)
        self.model_label.setVisible(visible)
        self.model_combo.setVisible(visible)
        self.refresh_models_btn.setVisible(visible)
        self.profile_label.setVisible(visible)
        self.profile_combo.setVisible(visible)
        
    def load_api_key(self):
        if os.path.exists(self.api_key_path):
            try:
                with open(self.api_key_path, "r", encoding="utf-8") as f:
                    return f.read().strip()
            except Exception as e:
                print(f"Failed to load API key: {e}")
        return ""
        
    @Slot()
    def save_api_key(self):
        api_key = self.api_key_input.text().strip()
        if not api_key:
            self.append_log("> <b style='color:red;'>Cannot save an empty API Key.</b>")
            return
        try:
            with open(self.api_key_path, "w", encoding="utf-8") as f:
                f.write(api_key)
            self.append_log("> <b style='color:green;'>API Key saved successfully.</b>")
        except Exception as e:
            self.append_log(f"> <b style='color:red;'>Failed to save API Key: {e}</b>")
        
    @Slot()
    def toggle_connection(self):
        if getattr(self, 'connection_cooldown', False):
            self.append_log("> <b style='color:orange;'>Please wait a moment before reconnecting (Rate limit protection)...</b>")
            return
            
        self.is_listening = not self.is_listening
        if self.is_listening:
            api_key = self.api_key_input.text().strip()
            if not api_key:
                self.append_log("> <b style='color:red;'>Please enter an API Key first.</b>")
                self.is_listening = False
                return
                
            # Prevent rapid reconnects (Step 3.4)
            self.connection_cooldown = True
            QTimer.singleShot(5000, lambda: setattr(self, 'connection_cooldown', False))
                
            self.connect_btn.setText("\U0001F6D1 Disconnect")
            self.connect_btn.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #aa2222; color: white;")
            self.mic_btn.setEnabled(True)
            self.update_status("Connected (Mic Muted)", "orange")
            self.append_log("> Waiting for Gemini Session... (Mic is muted)")
            
            selected_model = self.model_combo.currentData()
            self.service.model = selected_model
            self.service.thinking_profile = self.profile_combo.currentData()
            self.service.start_session(api_key)
            
            # Start with mic muted by default when connecting
            self.service.is_mic_active = False
            self.mic_btn.setText("\U0001F399\uFE0F Unmute Mic")
            self.mic_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
            
            # Start with speaker on
            self.service.is_speaker_active = True
            self.speaker_btn.setEnabled(True)
            self.speaker_btn.setText("\U0001F50A Speaker On")
            self.speaker_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
            
            self.set_connection_ui_visible(False)
        else:
            self.connect_btn.setText("\U0001F50C Connect")
            self.connect_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
            self.mic_btn.setEnabled(False)
            self.mic_btn.setText("\U0001F399\uFE0F Mute/Unmute Mic")
            self.mic_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
            self.speaker_btn.setEnabled(False)
            self.speaker_btn.setText("\U0001F50A Speaker On")
            self.speaker_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
            self.update_status("Idle", "black")
            self.set_connection_ui_visible(True)
            self.append_log("> Session stopped.")
            self.service.end_session()
            
    @Slot()
    def toggle_mute(self):
        if not self.is_listening:
            return
            
        self.service.is_mic_active = not self.service.is_mic_active
        if self.service.is_mic_active:
            self.update_status("Connected (Mic On)", "green")
            self.mic_btn.setText("\U0001F399\uFE0F Mute Mic")
            self.mic_btn.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #aa2222; color: white;")
            self.append_log("> Microphone unmuted.")
        else:
            self.update_status("Connected (Mic Muted)", "orange")
            self.mic_btn.setText("\U0001F399\uFE0F Unmute Mic")
            self.mic_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
            self.append_log("> Microphone muted.")
            
    @Slot()
    def toggle_speaker(self):
        if not self.is_listening:
            return
            
        self.service.is_speaker_active = not self.service.is_speaker_active
        if self.service.is_speaker_active:
            self.speaker_btn.setText("\U0001F50A Speaker On")
            self.speaker_btn.setStyleSheet("font-size: 14px; font-weight: bold;")
            self.append_log("> Speaker unmuted.")
        else:
            self.speaker_btn.setText("\U0001F507 Speaker Muted")
            self.speaker_btn.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #aa2222; color: white;")
            self.append_log("> Speaker muted.")
            
    @Slot()
    def browse_attachment(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.xpm *.jpg *.jpeg)"
        )
        if file_name:
            self.set_attachment(file_name)
            
    def set_attachment(self, file_path):
        filename = os.path.basename(file_path)
        self.attachment_label.setText(f"Attached: {filename}")
        self.current_attachment = file_path
        self.append_log(f"> Loaded image: {filename}")
        
    @Slot()
    def open_api_key_page(self):
        import webbrowser
        webbrowser.open("https://aistudio.google.com/app/apikey")
        
    @Slot()
    def send_text(self):
        text = self.text_input.text().strip()
        if not text:
            return
            
        self.append_log(f"<b>You:</b> {text}")
        self.text_input.clear()
        
        if self.is_listening:
            self.update_status("Processing Text...", "blue")
            
            # Read attachment bytes if present
            image_bytes = None
            mime_type = None
            if hasattr(self, 'current_attachment') and self.current_attachment:
                try:
                    with open(self.current_attachment, "rb") as f:
                        image_bytes = f.read()
                    
                    ext = self.current_attachment.lower().split('.')[-1]
                    mime_type = f"image/{ext}" if ext != "jpg" else "image/jpeg"
                    
                    # Clear attachment after sending
                    self.current_attachment = None
                    self.attachment_label.setText("No attachment")
                except Exception as e:
                    self.append_log(f"> <b style='color:red;'>Failed to read image:</b> {e}")
                    
            self.service.send_text_message(text, image_bytes, mime_type)
        else:
            self.append_log("<i>Please connect first by pressing the Mic button.</i>")
            
    @Slot(str)
    def append_log(self, text):
        self._commit_user_speech()
        self._commit_speech()
        self.chat_history.append(text)
        self._render_history()
        
        if "> Sent message to Gemini." in text or "Failed to send message" in text:
            if self.is_listening:
                status_text = "Connected (Mic On)" if self.service.is_mic_active else "Connected (Mic Muted)"
                status_color = "green" if self.service.is_mic_active else "orange"
                self.update_status(status_text, status_color)
                
    def _commit_user_speech(self):
        if self.current_user_speech:
            self.chat_history.append(f"<b>You:</b> <i>{self.current_user_speech}</i>")
            self.current_user_speech = ""

    @Slot(str)
    def append_speech(self, text):
        self._commit_user_speech()
        self.current_speech += text
        self.current_thought = ""
        self._render_history()
        
    @Slot(str, bool)
    def append_user_speech(self, text, is_finished):
        if text:
            self.current_user_speech += text
            
        if is_finished:
            self._commit_user_speech()
            
        self._render_history()
        
    @Slot(str)
    def append_thought(self, text):
        self._commit_user_speech()
        self.current_thought += text
        self._render_history()

    @Slot()
    def end_turn(self):
        self._commit_speech()
        self.current_thought = ""
        self._render_history()

    def _markdown(self, text):
        try:
            import markdown
            return markdown.markdown(text, extensions=['fenced_code', 'codehilite'])
        except ImportError:
            return text

    def _commit_speech(self):
        if self.current_speech:
            speech_md = self._markdown(self.current_speech)
            self.chat_history.append(f"<b>Gemini:</b> <div style='font-size: 1.15em; font-weight: 800;'>{speech_md}</div>")
            self.current_speech = ""

    def _render_history(self):
        full_html = f"<style>{self.pygments_css}</style>\n" if self.pygments_css else ""
        full_html += "<br>".join(self.chat_history)
        
        if self.current_user_speech:
            full_html += f"<br><b>You:</b> <i>{self.current_user_speech}</i>"
            
        if self.current_speech:
            speech_md = self._markdown(self.current_speech)
            full_html += f"<br><b>Gemini:</b> <div style='font-size: 1.15em; font-weight: 800;'>{speech_md}</div>"
            
        if self.current_thought:
            full_html += f"<br><small style='color:gray;'><i>{self.current_thought}</i></small>"
            
        self.history_view.setHtml(full_html)
        scrollbar = self.history_view.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def update_status(self, text, color="black"):
        self.status_label.setText(f"Status: <span style='color:{color};'>{text}</span>")

    # Drag & Drop Support
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            
    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                self.set_attachment(file_path)
                break # Only handle one image

    def closeEvent(self, event):
        if hasattr(self, 'service') and self.service:
            self.service.stop()
            self.service.join(timeout=1.0)
        super().closeEvent(event)



