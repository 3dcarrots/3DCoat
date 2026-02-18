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

