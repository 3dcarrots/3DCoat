from __future__ import annotations
import cPy.cTypes
#cRender
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class image_format(Enum):
	'''
			
		The coat namespace used for most 3DCoat API calls except low-level internal structures.
		
	'''
	fmtNone = Coat_CPP.image_format.fmtNone.value
	R8 = Coat_CPP.image_format.R8.value
	Rg8 = Coat_CPP.image_format.Rg8.value
	Rgb8 = Coat_CPP.image_format.Rgb8.value
	Rgba8 = Coat_CPP.image_format.Rgba8.value
	R16 = Coat_CPP.image_format.R16.value
	Rg16 = Coat_CPP.image_format.Rg16.value
	Rgb16 = Coat_CPP.image_format.Rgb16.value
	Rgba16 = Coat_CPP.image_format.Rgba16.value
	R16f = Coat_CPP.image_format.R16f.value
	Rg16f = Coat_CPP.image_format.Rg16f.value
	Rgb16f = Coat_CPP.image_format.Rgb16f.value
	Rgba16f = Coat_CPP.image_format.Rgba16f.value
	R32f = Coat_CPP.image_format.R32f.value
	Rg32f = Coat_CPP.image_format.Rg32f.value
	Rgb32f = Coat_CPP.image_format.Rgb32f.value
	Rgba32f = Coat_CPP.image_format.Rgba32f.value
	Depth16 = Coat_CPP.image_format.Depth16.value
	Depth24 = Coat_CPP.image_format.Depth24.value
	Depth24Stencil8 = Coat_CPP.image_format.Depth24Stencil8.value
	Dxt1 = Coat_CPP.image_format.Dxt1.value
	Dxt3 = Coat_CPP.image_format.Dxt3.value
	Dxt5 = Coat_CPP.image_format.Dxt5.value
	PVRTC4 = Coat_CPP.image_format.PVRTC4.value
	PVRTC4_Alpha = Coat_CPP.image_format.PVRTC4_Alpha.value
	Count = Coat_CPP.image_format.Count.value


class RenderUtils():
	'''
			
		Base class for rendering utilities
		
	'''

	@staticmethod
	def CreateFBO(width: int, height: int, format: image_format) -> int:
		'''
			
		Create frame buffer object. An FBO is a texture or data that can accept a rendered result

		Args:
			width (int): The size of the sampler in width
			height (int): The size of the sampler in height
			format (image_format): image_format - enum with the number of channels and the channel type. For example coat.image_format.Rgb8

		Returns:
			int: texture id - can be used as texture id and as FBO for rendering target
		
		'''
		pass # cpp source

	@staticmethod
	def clear(fbo_id: int, fill_color: any, clear_color: bool = True, clear_depth: bool = True, fill_depth: float = 1) -> int:
		'''
			
		Clear the framebuffer object - fill each pixel of the FBO sample with the same data

		Args:
			fbo_id (int): FBO ID to be filled for clearing
			fill_color : Color to fill each pixel
			clear_color (bool): Do you want to clear the FBO color? if "true" the color of each pixel will be changed to fill_color, if "false" the color will not be changed.
			clear_depth (bool): Do you want to clear the FBO depth? if "true" the depth of each pixel will be changed to fill_depth, if "false" the depth will not be changed.
			fill_depth (float): Depth value for fill each pixel

		Returns:
			int: true if successfully
		
		'''
		pass # cpp source

	@staticmethod
	def draw_on_screen(texture: int = 1, left: int = 0, top: int = 0, right: int = 0, bottom: int = 0, red: int = 255, green: int = 255, blue: int = 255, opacity: int = 255) -> int:
		'''
			
		Draw a texture rectangle in the main 3DCoat window

		Args:
			texture (int): The ID of the texture that will be rendered
			left (int): The position of the left side of the rendered texture on the screen
			top (int): The position of the top side of the rendered texture on the screen
			right (int): The position of the right side of the rendered texture on the screen
			bottom (int): The position of the bottom side of the rendered texture on the screen
			red (int): Multiplier for the red channel of the texture
			green (int): Multiplier for the green channel of the texture
			blue (int): Multiplier for the blue channel of the texture

		Returns:
			int: true if successfully
		
		'''
		pass # cpp source

	@staticmethod
	def draw_text(x: float, y: float, text: str, color_r: float = 1, color_g: float = 1, color_b: float = 1, color_a: float = 1) -> int:
		'''
			
		Draw the text in the main 3DCoat window

		Args:
			x (float): The position of the left side of the text block
			y (float): The position of the top side of the text block
			text (str): The content of the text block you want to display
			color_r (float): Value of the red channel of the text color
			color_g (float): Value of the gleen channel of the text color
			color_b (float): Value of the blue channel of the text color
			color_a (float): Opacity of the rendered text

		Returns:
			int: true if successfully
		
		'''
		pass # cpp source

	@staticmethod
	def CreateGPUTexture(src_data: any, format: image_format) -> int:
		'''
			
		Create a 2D sampler in GPU memory from a numpy array

		Args:
			src_data : numpy array from which the 2d sampler will be created. A numpy array must have the correct width and height, type and number of channels as in OpenCV
			format (image_format): The texture type must match the numpy structure and type. For example coat.image_format.Rgb8

		Returns:
			int: the texture id of the new sampler
		
		'''
		pass # cpp source

	@staticmethod
	def GPUTextureFromFile(file_path: str, Clamp: bool = False, Smooth: bool = True, swapRB: bool = False, Flip: bool = False) -> int:
		'''
			
		Create a 2D sampler in GPU memory from a numpy array

		Returns:
			int: the texture id of the new sampler
		
		'''
		pass # cpp source

	@staticmethod
	def DeleteGPUTexture(texture_id: int) -> bool:
		'''
			
		Remove sampler from GPU memory

		Args:
			texture_id (int): Texture ID

		Returns:
			bool: true if successfully
		
		'''
		pass # cpp source

	@staticmethod
	def work_area() -> any:
		'''
			
		3DCoat workspace rectangle (viewport)
		
		'''
		pass # cpp source

	@staticmethod
	def GetTextureID(Name: str, Clamp: bool = False, Smooth: bool = False, swapRB: bool = False, Flip: bool = False) -> int:
		pass # cpp source

	@staticmethod
	def GetTextureName(TextureID: int) -> str:
		pass # cpp source

	@staticmethod
	def GetTextureWidth(TextureID: int) -> int:
		pass # cpp source

	@staticmethod
	def GetTextureHeight(TextureID: int) -> int:
		pass # cpp source

	@staticmethod
	def GetShaderID(Name: str, VType: int, Extra: str = None) -> int:
		pass # cpp source

	@staticmethod
	def GetScreenShader(name: str) -> int:
		pass # cpp source

	@staticmethod
	def GetWorldShader(name: str) -> int:
		pass # cpp source

	@staticmethod
	def SetShader(ShaderID: int):
		pass # cpp source

	@staticmethod
	def GetShader() -> int:
		pass # cpp source

	@staticmethod
	def SetShaderVar(Shader: int, Var: int, v: cPy.cTypes.cVec3):
		pass # cpp source

	@staticmethod
	def SetShaderVar(Shader: int, Var: int, v: float):
		pass # cpp source

	@staticmethod
	def SetShaderVar(Shader: int, Var: int, v: cPy.cTypes.cVec4):
		pass # cpp source

	@staticmethod
	def SetShaderVar(Shader: int, Var: int, m: cPy.cTypes.cMat4):
		pass # cpp source

	@staticmethod
	def GetViewPort() -> any:
		pass # cpp source

	@staticmethod
	def SetViewPort(R: any):
		pass # cpp source

	@staticmethod
	def AddRenderTargetRGBA(width: int, Height: int, Linear: bool = True) -> int:
		pass # cpp source

	@staticmethod
	def PushRenderTarget(Target: int):
		pass # cpp source

	@staticmethod
	def PopRenderTarget():
		pass # cpp source

	@staticmethod
	def ClearDevice():
		pass # cpp source

	@staticmethod
	def GetTexMemorySize() -> int:
		pass # cpp source

	@staticmethod
	def GetWorldViewProjTM() -> cPy.cTypes.cMat4:
		pass # cpp source

	@staticmethod
	def GetWorldViewProjTMInv() -> cPy.cTypes.cMat4:
		pass # cpp source

	@staticmethod
	def SetWorldViewProjTM(M: cPy.cTypes.cMat4):
		pass # cpp source

	@staticmethod
	def GetHWND() -> any:
		pass # cpp source

	@staticmethod
	def GetHomeDirectory() -> str:
		pass # cpp source

	@staticmethod
	def PickPointPos() -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def PickPointSpacePos() -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def GetPickRay(V: cPy.cTypes.cVec2) -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def GetPickRayFrom(V: cPy.cTypes.cVec2) -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def GetPickRayWVPTM(V: cPy.cTypes.cVec2) -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def GetPickRayWVPTMFrom(V: cPy.cTypes.cVec2) -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def Flush():
		pass # cpp source

	@staticmethod
	def drawPicture(rect: any, Texture: int, Color: int, Shadow: bool):
		pass # cpp source

	@staticmethod
	def drawBottomAlignedText(xb: int, yb: int, Text: str, MaxLx: int, FontSize: int, Color: int, Align: int, Draw: bool) -> int:
		pass # cpp source

	@staticmethod
	def drawCenetrAlignedText(x: int, y: int, Text: str, MaxLx: int, FontSize: int, Color: int) -> int:
		pass # cpp source

	@staticmethod
	def drawMultilineText(x: int, y: int, s: str, DefaultFont: int, DefColor: int, MaxLx: int, MaxLy: int = 100000, CenterX: any = 0, Draw: bool = True) -> int:
		pass # cpp source

	@staticmethod
	def drawThickLine(x: float, y: float, x1: float, y1: float, Color1: int, Color2: int, Thickness: float):
		pass # cpp source

	@staticmethod
	def drawThickLine(V1: cPy.cTypes.cVec3, V2: cPy.cTypes.cVec3, Color1: int, Color2: int, Thickness: float):
		pass # cpp source

	@staticmethod
	def drawThickCurve(curve: list[cPy.cTypes.cVec3], Color: int, Thickness: float):
		pass # cpp source

	@staticmethod
	def drawThickCurve(curve: list[cPy.cTypes.cVec2], Color: int, Thickness: float):
		pass # cpp source

	@staticmethod
	def drawThickCircle(x: float, y: float, R: float, Color: int, Thickness: float):
		pass # cpp source

	@staticmethod
	def drawThickCircle(pos: cPy.cTypes.cVec3, n: cPy.cTypes.cVec3, R: float, Color: int, Thickness: float):
		pass # cpp source

	@staticmethod
	def drawCoolSphere(Center: cPy.cTypes.cVec3, R: float, Color: int, Dense: bool = False):
		pass # cpp source

	@staticmethod
	def drawCoolScreenSphere(Center: cPy.cTypes.cVec3, R: float, Color: int):
		pass # cpp source

	@staticmethod
	def drawThickArrow(x: float, y: float, x1: float, y1: float, Color1: int, Color2: int, Thickness: float):
		pass # cpp source

	@staticmethod
	def drawScreenArrow(Start: cPy.cTypes.cVec3, End: cPy.cTypes.cVec3, Size: float, Color: int):
		pass # cpp source

	@staticmethod
	def drawTransformedText(x: float, y: float, text: str, Color: int, shadow: bool = False, Angle: float = 0.0, Scale: float = 1.0, HorizontalShift: float = 0.0, VerticalShift: float = 1.0):
		pass # cpp source

	@staticmethod
	def screenToWorldSpace(v: cPy.cTypes.cVec3) -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def screenToWorldSpaceZ(v: cPy.cTypes.cVec3) -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def worldToScreenSpace(v: cPy.cTypes.cVec3) -> cPy.cTypes.cVec3:
		pass # cpp source

	@staticmethod
	def worldToScreenSpaceZ(v: cPy.cTypes.cVec3) -> cPy.cTypes.cVec3:
		pass # cpp source

