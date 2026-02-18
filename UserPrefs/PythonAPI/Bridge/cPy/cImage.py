from __future__ import annotations
#cImage
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class cImage():
	'''
			
		Main class for handling raster images.
		* Provides functionality for creating, loading, manipulating, and querying
		image data. Supports various pixel formats, mipmapping, and compression operations.
		Designed to be compatible with OpenGL texture uploads.
		
	'''

	@staticmethod
	def CalcImageSize(Format: any, Width: int, Height: int, Depth: int, MipMapCount: int) -> int:
		'''
			
		Calculates total size in bytes for an image with given parameters.
		
		'''
		pass # cpp source

	MipMapsAll: int = Coat_CPP.cImage.MipMapsAll #: static int (T)  Default max count of mipmaps 
	def __init__(self):
		pass # CPP source

	def __init__(self, Src: cImage):
		pass # CPP source

	def Copy(self, Src: cImage):
		pass # cpp source

	def __init__(self, Src: cImage, rc: any):
		pass # CPP source

	def Copy(self, Src: cImage, rc: any):
		pass # cpp source

	def Copy(self, Pixels: any, Format: any, Width: int, Height: int, Depth: int, MipMapCount: int):
		'''
			
		Copies data from a raw buffer.
		
		'''
		pass # cpp source

	def Set(self, Pixels: any, Format: any, Width: int, Height: int, Depth: int, MipMapCount: int):
		'''
			
		Sets the image to point to existing memory (or adopts it).
		
		'''
		pass # cpp source

	def SetHeight(self, Height: int):
		pass # cpp source

	def Create(self, Format: any, Width: int, Height: int, Depth: int, MipMapCount: int):
		'''
			
		Allocates memory for a new image.
		
		'''
		pass # cpp source

	def __init__(self, Format: any, Width: int, Height: int, Depth: int, MipMapCount: int):
		pass # CPP source

	def Free(self):
		'''
			
		Releases the pixel memory.
		
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def GetWidth(self) -> int:
		pass # cpp source

	def GetHeight(self) -> int:
		pass # cpp source

	def GetDepth(self) -> int:
		pass # cpp source

	def GetWidth(self, MipMapLevel: int) -> int:
		pass # cpp source

	def GetHeight(self, MipMapLevel: int) -> int:
		pass # cpp source

	def GetDepth(self, MipMapLevel: int) -> int:
		pass # cpp source

	def GetFormat(self) -> any:
		pass # cpp source

	def GetSize(self) -> int:
		pass # cpp source

	def GetPixels(self) -> any:
		pass # cpp source

	def GetPixels(self, MipMapLevel: int) -> any:
		pass # cpp source

	def GetMipMapCount(self) -> int:
		pass # cpp source

	def GetMipMapCountFromDimensions(self) -> int:
		pass # cpp source

	def GetDimension(self) -> any:
		pass # cpp source

	def SwapChannels(self, Ch0: int, Ch1: int) -> bool:
		pass # cpp source

	def RemoveChannels(self, KeepCh0: bool, KeepCh1: bool = True, KeepCh2: bool = True, KeepCh3: bool = True) -> bool:
		pass # cpp source

	def InvertChannel(self, Ch: int) -> bool:
		pass # cpp source

	def CopyChannel(self, From: int, To: int) -> bool:
		pass # cpp source

	def ToFormat(self, Format: any) -> bool:
		pass # cpp source

	def Uncompress(self):
		'''
			
		 Dxt3, Dxt5 -> Rgba8
		
		'''
		pass # cpp source

	def Compress(self):
		'''
			
		 Rgba8 -> Dxt5
		
		'''
		pass # cpp source

	def ToGrayScale(self) -> bool:
		'''
			
		 Rgb16, Rgba16 -> R16
		
		'''
		pass # cpp source

	def ToNormalMap(self, Format: any, Z: float = 1.0, OldAlpha: bool = False) -> bool:
		'''
			
		 "OldAlpha" works only if(Rgba8 == m_Format && Rgba8 == Format)
		
		'''
		pass # cpp source

	def CreateMipMaps(self, MipMapCount: int) -> bool:
		'''
			
		Generates mipmaps for the image. Not supported for compressed formats.
		
		'''
		pass # cpp source

	def RemoveMipMaps(self):
		'''
			
		 !Compressed
		
		'''
		pass # cpp source

	def GetPixelR8(self, X: int, Y: int) -> any:
		'''
			
		Returns pixel intensity. Assumes R8 format.
		
		'''
		pass # cpp source

	def SetPixelR8(self, X: int, Y: int, p: any):
		pass # cpp source

	def MergeRgb8(self, From: cImage, X: int, Y: int):
		pass # cpp source

	def MergeRgba8(self, From: cImage, X: int, Y: int, ColorAsAlpha: bool):
		pass # cpp source

	def Flip(self) -> bool:
		'''
			
		Flips the image vertically. Supports Plain, Packed, and Compressed formats.
		
		'''
		pass # cpp source

	def Resize(self, Width: int, Height: int) -> bool:
		'''
			
		Resizes the image using resampling. Plain formats only.
		
		'''
		pass # cpp source

	def Decrease2X(self) -> bool:
		'''
			
		 Plain formats && !Cube
		
		'''
		pass # cpp source

	def MakePowerOfTwo(self) -> bool:
		'''
			
		Resizes the image to the nearest power of two dimensions.
		
		'''
		pass # cpp source

	def Make2D(self, Square: bool = True, DepthStep: int = 1) -> bool:
		'''
			
		Converts a 3D volume texture into a 2D strip of slices.
		
		'''
		pass # cpp source

	def CreateSevenLods(self, SaveAs: str = "data/textures/SevenLods.dds"):
		'''
			
		 Converts 3D texture to 2D set of depth slices
		
		'''
		pass # cpp source

	def _py_buffer_info(self) -> any:
		pass # cpp source

