import numpy as np
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage, QPixmap
import cPy.cRender

try:
    import moderngl
    HAS_MODERNGL = True
except ImportError:
    HAS_MODERNGL = False

from .TilerShaders import VERTEX_SHADER, FRAGMENT_SHADER
from .MathAlgorithms import calculate_homography

class PBRRenderer(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.setScaledContents(True)
        self.setStyleSheet("background-color: #222;")
        
        self.ctx = None
        self.prog = None
        self.vao = None
        self.vbo = None
        self.fbo = None
        self.render_size = (1024, 1024)
        
        # State variables
        self.tex_albedo = None
        self.tex_normal = None
        self.tex_height = None
        
        self.rotation_angle = 0.0
        self.crop_offset = (0.0, 0.0)
        self.crop_scale = (1.0, 1.0)
        self.tile_offset = (0.0, 0.0)
        self.pan_offset = (0.0, 0.0)
        
        self.view_mode = 0 # 0=Albedo, 1=Normal, 2=Height
        self.tiling_mode = 0 # 0=Decal Stamp, 1=Seamless
        self.preview_grid = 0 # 0=off, 1=2x2 grid
        
        self.corners = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0)]
        self.orig_corners = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0)]
        
        self.target_color = (0.0, 1.0, 0.0)
        
        self.hue_shift = 0.0
        self.sat_mult = 1.0
        self.exp_shift = 0.0
        
        self.bal_r = 1.0
        self.bal_g = 1.0
        self.bal_b = 1.0
        
        self.use_height_blend = 0
        self.height_blend_threshold = 0.5
        self.height_blend_contrast = 0.2

        if HAS_MODERNGL:
            self._init_gl()

    def _init_gl(self):
        try:
            # Tell 3DCoat C++ to make its primary GL context current on this thread
            cPy.cRender.RenderUtils.MakeGLContextCurrent()
            
            # ModernGL detects the bound context natively!
            self.ctx = moderngl.create_context()
        except Exception as e:
            print("PBRTiler: Could not acquire ModernGL context:", e)
            return

        self.fbo = self.ctx.framebuffer(
            color_attachments=[self.ctx.texture(self.render_size, 4, dtype='f1')]
        )
        self.fbo_pass1 = self.ctx.framebuffer(
            color_attachments=[self.ctx.texture(self.render_size, 4, dtype='f1')]
        )
        
        self.prog = self.ctx.program(
            vertex_shader=VERTEX_SHADER,
            fragment_shader=FRAGMENT_SHADER
        )
        
        # We use a procedural vertex shader (gl_VertexID) to bypass 3DCoat VBO/VAO memory corruption!
        self.vbo = None
        self.vao = self.ctx.vertex_array(self.prog, [])
        
        # Create dummy textures
        dummy_data = np.zeros((4, 4, 3), dtype='f4')
        self.tex_albedo = self.ctx.texture((4, 4), 3, dummy_data.tobytes(), dtype='f4')
        self.tex_normal = self.ctx.texture((4, 4), 3, dummy_data.tobytes(), dtype='f4')
        self.tex_height = self.ctx.texture((4, 4), 1, np.zeros((4,4,1), dtype='f4').tobytes(), dtype='f4')
        
        if 'tex_albedo' in self.prog: self.prog['tex_albedo'].value = 5
        if 'tex_normal' in self.prog: self.prog['tex_normal'].value = 6
        if 'tex_height' in self.prog: self.prog['tex_height'].value = 7

    def set_textures(self, albedo_np, normal_np, height_np, custom_nps=[]):
        if not self.ctx: return
        
        try:
            cPy.cRender.RenderUtils.MakeGLContextCurrent()
            h_a, w_a, _ = albedo_np.shape
            h_n, w_n, _ = normal_np.shape
            h_h, w_h, _ = height_np.shape
            
            linear_albedo = np.power(albedo_np.astype(np.float32), 2.2)
            avg_linear = np.mean(linear_albedo, axis=(0,1))
            avg_srgb = np.power(avg_linear, 1.0 / 2.2)
            self.global_albedo_avg = (float(avg_srgb[0]), float(avg_srgb[1]), float(avg_srgb[2]))
            
            if self.tex_albedo: self.tex_albedo.release()
            if self.tex_normal: self.tex_normal.release()
            if self.tex_height: self.tex_height.release()
            for t in getattr(self, 'custom_tex_objs', []):
                t.release()
            self.custom_tex_objs = []
            
            w_exp = 1024
            h_exp = 1024
            if hasattr(self, 'parent_window'):
                try:
                    w_exp = int(self.parent_window.combo_export_w.currentText())
                    h_exp = int(self.parent_window.combo_export_h.currentText())
                except: pass
                
            if self.render_size != (w_exp, h_exp):
                self.render_size = (w_exp, h_exp)
                if self.fbo: self.fbo.release()
                if self.fbo_pass1: self.fbo_pass1.release()
                self.fbo = self.ctx.framebuffer(color_attachments=[self.ctx.texture(self.render_size, 4, dtype='f1')])
                self.fbo_pass1 = self.ctx.framebuffer(color_attachments=[self.ctx.texture(self.render_size, 4, dtype='f1')])
                
            self.fbo_pass1.color_attachments[0].filter = (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
            
            self.tex_albedo = self.ctx.texture((w_a, h_a), 3, albedo_np.astype('f4').tobytes(), dtype='f4')
            self.tex_albedo.build_mipmaps() # Crucial for textureLod algorithm!
            
            self.tex_normal = self.ctx.texture((w_n, h_n), 3, normal_np.astype('f4').tobytes(), dtype='f4')
            self.tex_height = self.ctx.texture((w_h, h_h), 1, height_np.astype('f4').tobytes(), dtype='f4')
            
            self.tex_albedo.filter = (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
            self.tex_normal.filter = (moderngl.LINEAR, moderngl.LINEAR)
            self.tex_height.filter = (moderngl.LINEAR, moderngl.LINEAR)
            
            # Create custom textures
            for idx, c_np in enumerate(custom_nps):
                if idx >= 8: break # Shader only has size 8 array limit
                h_c, w_c, _ = c_np.shape
                c_tex = self.ctx.texture((w_c, h_c), 3, c_np.astype('f4').tobytes(), dtype='f4')
                c_tex.build_mipmaps()
                c_tex.filter = (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
                self.custom_tex_objs.append(c_tex)
            
            self.request_render()
        except Exception as e:
            import traceback
            with open(r'C:\Users\carro\(PBRTiler_Crash2.txt)', 'w') as f:
                f.write(traceback.format_exc())
            print("PBRTiler set_textures Error:", e)

    def request_render(self):
        self.render_pending = True
        
    def poll_render(self):
        if getattr(self, 'render_pending', False):
            self.render_frame()
            self.render_pending = False

    def render_frame(self):
        # Override QWidget.update to perform our own render pass and update the label
        if not self.ctx or not self.fbo: return
        
        try:
            cPy.cRender.RenderUtils.MakeGLContextCurrent()
            
            self.fbo.use()
            # Inherit main context states can break our fbo drawing, enforce defaults:
            w, h = self.fbo.size
            self.fbo.viewport = (0, 0, 1, 1) # Invalidate ModernGL viewport cache!
            self.fbo.viewport = (0, 0, w, h)
            
            # Mercilessly override any 3DCoat rendering states using raw ctypes
            import ctypes
            gl = ctypes.windll.opengl32
            gl.glDisable(0x0C11) # GL_SCISSOR_TEST
            gl.glDisable(0x0B44) # GL_CULL_FACE
            gl.glDisable(0x0B71) # GL_DEPTH_TEST
            gl.glDisable(0x0BE2) # GL_BLEND
            gl.glDisable(0x0B90) # GL_STENCIL_TEST
            gl.glDisable(0x8C89) # GL_RASTERIZER_DISCARD
            gl.glColorMask(1, 1, 1, 1) # Force color writing
            gl.glDepthMask(0) # Prevent depth writing
            
            self.ctx.scissor = None
            self.ctx.disable(moderngl.CULL_FACE)
            self.ctx.disable(moderngl.DEPTH_TEST)
            self.ctx.disable(moderngl.BLEND)
            self.fbo.color_mask = (True, True, True, True)
            self.ctx.clear(0.2, 0.2, 0.2, 1.0)
            
            H_inv = calculate_homography(self.orig_corners, self.corners)
            
            if 'inverseHomography' in self.prog: self.prog['inverseHomography'].write(H_inv.T.astype('f4').tobytes())
            if 'rotationAngle' in self.prog: self.prog['rotationAngle'].value = self.rotation_angle
            if 'cropOffset' in self.prog: self.prog['cropOffset'].value = self.crop_offset
            if 'cropScale' in self.prog: self.prog['cropScale'].value = self.crop_scale
            if 'tileOffset' in self.prog: self.prog['tileOffset'].value = self.tile_offset
            
            if 'tex_albedo' in self.prog:
                self.prog['texelSize'].value = (1.0 / float(max(1, self.tex_albedo.width)), 1.0 / float(max(1, self.tex_albedo.height)))
            
            if 'hueShift' in self.prog: self.prog['hueShift'].value = getattr(self, 'hue_shift', 0.0)
            if 'satMult' in self.prog: self.prog['satMult'].value = getattr(self, 'sat_mult', 1.0)
            if 'expShift' in self.prog: self.prog['expShift'].value = getattr(self, 'exp_shift', 0.0)
            if 'colorBalance' in self.prog: self.prog['colorBalance'].value = (getattr(self, 'bal_r', 1.0), getattr(self, 'bal_g', 1.0), getattr(self, 'bal_b', 1.0))
            
            if 'useHeightBlend' in self.prog: self.prog['useHeightBlend'].value = self.use_height_blend
            if 'blendMargin' in self.prog: self.prog['blendMargin'].value = max(0.001, float(getattr(self, 'blend_margin', 5.0)) / 100.0)
            if 'blendHeightInfluence' in self.prog: self.prog['blendHeightInfluence'].value = getattr(self, 'blend_height_influence', 1.0)
            if 'heightBlendThreshold' in self.prog: self.prog['heightBlendThreshold'].value = self.height_blend_threshold
            if 'heightBlendContrast' in self.prog: self.prog['heightBlendContrast'].value = self.height_blend_contrast
            if 'panOffset' in self.prog: self.prog['panOffset'].value = getattr(self, 'pan_offset', (0.0, 0.0))
            
            is_export = getattr(self, 'preview_grid', 1) == 0
            if 'viewMode' in self.prog: self.prog['viewMode'].value = self.view_mode
            if 'tilingMode' in self.prog: self.prog['tilingMode'].value = getattr(self, 'preview_grid', 1)
            if 'previewGrid' in self.prog: self.prog['previewGrid'].value = getattr(self, 'preview_grid', 0)
            if 'zoomLevel' in self.prog: self.prog['zoomLevel'].value = 1.0 if is_export else getattr(self, 'zoom', 1.0)
            if 'panOffset' in self.prog: self.prog['panOffset'].value = (0.0, 0.0) if is_export else getattr(self, 'pan_offset', (0.0, 0.0))
            
            if 'eqAlbedoEnabled' in self.prog: self.prog['eqAlbedoEnabled'].value = getattr(self, 'eq_albedo_enabled', 0)
            if 'eqAlbedoLodCenter' in self.prog: self.prog['eqAlbedoLodCenter'].value = getattr(self, 'eq_albedo_lod_center', 5.0)
            if 'eqAlbedoLodEdge' in self.prog: self.prog['eqAlbedoLodEdge'].value = getattr(self, 'eq_albedo_lod_edge', 9.0)
            if 'globalAvgColor' in self.prog: self.prog['globalAvgColor'].value = getattr(self, 'global_albedo_avg', (0.5, 0.5, 0.5))
            if 'invertNormalY' in self.prog: self.prog['invertNormalY'].value = getattr(self, 'invert_normal_y', 0)
            
            if 'tex_albedo' in self.prog: self.prog['tex_albedo'].value = 5
            if 'tex_normal' in self.prog: self.prog['tex_normal'].value = 6
            if 'tex_height' in self.prog: self.prog['tex_height'].value = 7
            
            # ModernGL assigns array uniforms via list assignments natively
            if 'tex_custom' in self.prog:
                tex_binds = []
                for i in range(8):
                    tex_binds.append(8 + i)
                self.prog['tex_custom'].value = tex_binds
                
            self.tex_albedo.use(5)
            self.tex_normal.use(6)
            self.tex_height.use(7)
            
            # Bind all loaded custom textures into the exact memory slots 8..15
            for idx, c_tex in enumerate(getattr(self, 'custom_tex_objs', [])):
                if idx >= 8: break
                c_tex.use(8 + idx)
            
            # Pass 1: Render seamless tile
            self.fbo_pass1.use()
            self.fbo_pass1.viewport = (0, 0, w, h)
            self.ctx.clear(0.0, 0.0, 0.0, 0.0)
            
            if 'isPass2' in self.prog: self.prog['isPass2'].value = 0
            
            self.vao.render(moderngl.TRIANGLE_STRIP, vertices=4)
            
            # Pass 2: Apply effects and tiling
            self.fbo.use()
            self.fbo.viewport = (0, 0, w, h)
            self.ctx.clear(0.2, 0.2, 0.2, 1.0)
            
            self.fbo_pass1.color_attachments[0].build_mipmaps()
            self.fbo_pass1.color_attachments[0].use(4) # tex_pass1
            if 'tex_pass1' in self.prog: self.prog['tex_pass1'].value = 4
            if 'isPass2' in self.prog: self.prog['isPass2'].value = 1
            
            self.vao.render(moderngl.TRIANGLE_STRIP, vertices=4)
            
            self.fbo.use()
            data = self.fbo.read(components=4, dtype='f1')
            self._current_frame_data = data # Keep memory reference alive for QImage!
            
            qimg = QImage(data, self.render_size[0], self.render_size[1], QImage.Format_RGBA8888).copy()
            qimg = qimg.mirrored(False, True) 
            
            self.setPixmap(QPixmap.fromImage(qimg))
            self.update() # Force repaint
            
        except Exception as e:
            import traceback
            with open(r'C:\Users\carro\(PBRTiler_Crash.txt)', 'w') as f:
                f.write(traceback.format_exc())
            print("PBRTiler Render Error:", e)

    def export_to_qimage(self, width, height):
        if not self.ctx: return None
        try:
            cPy.cRender.RenderUtils.MakeGLContextCurrent()
            
            old_fbo = self.fbo
            old_fbo_pass1 = self.fbo_pass1
            
            export_fbo = self.ctx.framebuffer(
                color_attachments=[self.ctx.texture((width, height), 4, dtype='f1')]
            )
            
            export_fbo_pass1 = self.ctx.framebuffer(
                color_attachments=[self.ctx.texture((width, height), 4, dtype='f1')]
            )
            export_fbo_pass1.color_attachments[0].filter = (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
            
            self.fbo = export_fbo
            self.fbo_pass1 = export_fbo_pass1
            
            # Use viewport override to skip ModernGL internal checks
            self.fbo.viewport = (0, 0, 1, 1)
            self.fbo.viewport = (0, 0, width, height)
            
            self.render_frame() 
            
            self.fbo.use()
            data = self.fbo.read(components=4, dtype='f1')
            qimg = QImage(data, width, height, QImage.Format_RGBA8888).copy()
            qimg = qimg.mirrored(False, True)
            
            export_fbo.release()
            export_fbo_pass1.release()
            self.fbo = old_fbo
            self.fbo_pass1 = old_fbo_pass1
            
            return qimg
        except Exception as e:
            print("PBRTiler Export Error:", e)
            return None

    def mousePressEvent(self, event):
        self.last_mouse_pos = event.pos()
        if hasattr(self, 'parent_window') and getattr(self.parent_window, 'picking_color', False):
            pixmap = self.pixmap()
            if not pixmap or pixmap.isNull(): return
            
            w, h = self.width(), self.height()
            px, py = event.pos().x(), event.pos().y()
            
            img_x = int((px / w) * self.render_size[0])
            img_y = int((py / h) * self.render_size[1])
            
            img = pixmap.toImage()
            if 0 <= img_x < img.width() and 0 <= img_y < img.height():
                color = img.pixelColor(img_x, img_y)
                self.parent_window.target_color_picked(color)

    def mouseMoveEvent(self, event):
        import PySide6.QtCore as QtCore
        if hasattr(self, 'last_mouse_pos') and (event.buttons() & QtCore.Qt.LeftButton) and (event.modifiers() & QtCore.Qt.AltModifier):
            dx = event.pos().x() - self.last_mouse_pos.x()
            dy = event.pos().y() - self.last_mouse_pos.y()
            
            nx = dx / self.width()
            ny = dy / self.height()
            
            zoom = getattr(self, 'zoom', 1.0)
            self.pan_offset = (self.pan_offset[0] + nx / zoom, self.pan_offset[1] - ny / zoom)
            self.last_mouse_pos = event.pos()
            self.request_render()
