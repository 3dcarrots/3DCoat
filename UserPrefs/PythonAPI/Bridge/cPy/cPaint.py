from __future__ import annotations
import cPy.cCore
#cPaint
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class PPPObject(cPy.cCore.BaseClass):
	'''
			
		Paint Object
		
	'''


	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->PPPObject:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a PPPObject class or its descendant, and if so, returns the specified object, but of the PPPObject type.
		'''
		pass # cpp source

	def Delete(self):
		pass # cpp source

	def GetName(self) -> str:
		pass # cpp source

	def SetName(self, new_name: str):
		pass # cpp source

	def GetVisible(self) -> bool:
		pass # cpp source

	def SetVisible(self, value: bool):
		pass # cpp source

	def GetLocked(self) -> bool:
		pass # cpp source

	def SetLocked(self, value: bool):
		pass # cpp source



class PaintRoom():
	'''
			
		Paint Room
		
	'''

	@staticmethod
	def LoadMesh(file_name: str) -> bool:
		'''
			
		Load poly object for painting room from file

		Returns:
			bool: True if success
		
		'''
		pass # cpp source

	@staticmethod
	def LoadColorTexture(file_name: str) -> bool:
		'''
			
		Load texture from file and put it to a new layer

		Returns:
			bool: True if success
		
		'''
		pass # cpp source

	@staticmethod
	def ForceMapCPUQuadsToGPU():
		'''
			
		Force UpdateDirtyQuadsGPU to remap all CPU quads to GPU
		
		'''
		pass # cpp source

	@staticmethod
	def ForceBlendGPUQuads():
		'''
			
		Force blending of all GPU quads for all layers
		
		'''
		pass # cpp source

	@staticmethod
	def ExportMesh(filename: str, fromRetopoRoom: bool = False, transformToSelectedObjectSpace: bool = False) -> bool:
		'''
			
		Export mesh the object from the painting room to a file

		Returns:
			bool: True if success
		
		'''
		pass # cpp source

	@staticmethod
	def PPPObjectsCount() -> int:
		'''
			
		Get the count of paint objects in scene

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	@staticmethod
	def GetPPPObject(idx: int) -> PPPObject:
		pass # cpp source

	@staticmethod
	def GetUVSetsCount() -> int:
		pass # cpp source

	@staticmethod
	def GetUVSetName(index: int) -> str:
		'''
			
		Get the name of a UV set by its index.

		Args:
			index (int): Index of the UV set.

		Returns:
			str: The name of the UV set.
		
		'''
		pass # cpp source

	@staticmethod
	def RenameUVSet(index: int, newName: str):
		'''
			
		Rename an existing UV set.

		Args:
			index (int): Index of the UV set.
			newName (str): New name.
		
		'''
		pass # cpp source

	@staticmethod
	def GetUVSetResolutionX(index: int) -> int:
		'''
			
		Get the current texture resolution X for the specified UV set.

		Args:
			index (int): Index of the UV set.

		Returns:
			int: width.
		
		'''
		pass # cpp source

	@staticmethod
	def GetUVSetResolutionY(index: int) -> int:
		'''
			
		Get the current texture resolution Y for the specified UV set.

		Args:
			index (int): Index of the UV set.

		Returns:
			int: height.
		
		'''
		pass # cpp source

	@staticmethod
	def ResizeUVSet(index: int, width: int, height: int) -> bool:
		'''
			
		Change the texture resolution of the UV set.

		Args:
			index (int): Index of the UV set.
			width (int): New width.
			height (int): New height.

		Returns:
			bool: True on success.
		
		'''
		pass # cpp source

	@staticmethod
	def CalculateUVSpace(index: int) -> float:
		'''
			
		Calculate the total UV space area occupied by polygons in this UV set.

		Args:
			index (int): Index of the UV set.

		Returns:
			float: Area in UV coordinates.
		
		'''
		pass # cpp source

	@staticmethod
	def GetUVSetFaceCount(index: int) -> int:
		'''
			
		Get the number of polygons (faces) belonging to the specified UV set.

		Args:
			index (int): Index of the UV set.

		Returns:
			int: Number of polygons.
		
		'''
		pass # cpp source

