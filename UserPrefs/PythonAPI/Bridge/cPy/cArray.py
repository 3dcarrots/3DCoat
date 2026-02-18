from __future__ import annotations
import cPy.cTypes
#cArray
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class cArray_int():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: int, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> int:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> int:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> int:
		pass # cpp source

	def GetAt(self, Index: int) -> int:
		pass # cpp source

	def GetFirst(self) -> int:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> int:
		pass # cpp source

	def GetLast(self) -> int:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> int:
		pass # cpp source

	def GetAndRemoveLast(self) -> int:
		pass # cpp source

	def SetAt(self, Index: int, Value: int):
		pass # cpp source

	def ToPtr(self) -> int:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> int:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: int) -> int:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: int, defvalue: int):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: int):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: int):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: int, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: int, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: int, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: int, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: int, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: int) -> int:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: int) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: int) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> int:
		pass # cpp source

	def pop_back(self) -> int:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_float():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: float, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> float:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> float:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> float:
		pass # cpp source

	def GetAt(self, Index: int) -> float:
		pass # cpp source

	def GetFirst(self) -> float:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> float:
		pass # cpp source

	def GetLast(self) -> float:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> float:
		pass # cpp source

	def GetAndRemoveLast(self) -> float:
		pass # cpp source

	def SetAt(self, Index: int, Value: float):
		pass # cpp source

	def ToPtr(self) -> float:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> float:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: float) -> float:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: float, defvalue: float):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: float):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: float):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: float, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: float, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: float, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: float, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: float, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: float) -> float:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: float) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: float) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> float:
		pass # cpp source

	def pop_back(self) -> float:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_double():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: float, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> float:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> float:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> float:
		pass # cpp source

	def GetAt(self, Index: int) -> float:
		pass # cpp source

	def GetFirst(self) -> float:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> float:
		pass # cpp source

	def GetLast(self) -> float:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> float:
		pass # cpp source

	def GetAndRemoveLast(self) -> float:
		pass # cpp source

	def SetAt(self, Index: int, Value: float):
		pass # cpp source

	def ToPtr(self) -> float:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> float:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: float) -> float:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: float, defvalue: float):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: float):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: float):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: float, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: float, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: float, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: float, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: float, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: float) -> float:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: float) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: float) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> float:
		pass # cpp source

	def pop_back(self) -> float:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_DWORD():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: int, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> int:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> int:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> int:
		pass # cpp source

	def GetAt(self, Index: int) -> int:
		pass # cpp source

	def GetFirst(self) -> int:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> int:
		pass # cpp source

	def GetLast(self) -> int:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> int:
		pass # cpp source

	def GetAndRemoveLast(self) -> int:
		pass # cpp source

	def SetAt(self, Index: int, Value: int):
		pass # cpp source

	def ToPtr(self) -> int:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> int:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: int) -> int:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: int, defvalue: int):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: int):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: int):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: int, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: int, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: int, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: int, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: int, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: int) -> int:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: int) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: int) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> int:
		pass # cpp source

	def pop_back(self) -> int:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_char():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: str, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> any:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> any:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> any:
		pass # cpp source

	def GetAt(self, Index: int) -> any:
		pass # cpp source

	def GetFirst(self) -> any:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> any:
		pass # cpp source

	def GetLast(self) -> any:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> any:
		pass # cpp source

	def GetAndRemoveLast(self) -> any:
		pass # cpp source

	def SetAt(self, Index: int, Value: any):
		pass # cpp source

	def ToPtr(self) -> str:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> str:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: any) -> any:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: any, defvalue: any):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: any):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: any):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: any, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: str, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: str, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: any, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: str, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: any) -> any:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: any) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: any) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> any:
		pass # cpp source

	def pop_back(self) -> any:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_cVec2():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: cPy.cTypes.cVec2, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> cPy.cTypes.cVec2:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> cPy.cTypes.cVec2:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> cPy.cTypes.cVec2:
		pass # cpp source

	def GetAt(self, Index: int) -> cPy.cTypes.cVec2:
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cVec2:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cVec2:
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cVec2:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cVec2:
		pass # cpp source

	def GetAndRemoveLast(self) -> cPy.cTypes.cVec2:
		pass # cpp source

	def SetAt(self, Index: int, Value: cPy.cTypes.cVec2):
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cVec2:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cVec2:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: cPy.cTypes.cVec2) -> cPy.cTypes.cVec2:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: cPy.cTypes.cVec2, defvalue: cPy.cTypes.cVec2):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: cPy.cTypes.cVec2):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: cPy.cTypes.cVec2):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: cPy.cTypes.cVec2, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: cPy.cTypes.cVec2, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: cPy.cTypes.cVec2, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: cPy.cTypes.cVec2, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: cPy.cTypes.cVec2, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: cPy.cTypes.cVec2) -> cPy.cTypes.cVec2:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: cPy.cTypes.cVec2) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: cPy.cTypes.cVec2) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> cPy.cTypes.cVec2:
		pass # cpp source

	def pop_back(self) -> cPy.cTypes.cVec2:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_cVec3():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: cPy.cTypes.cVec3, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> cPy.cTypes.cVec3:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> cPy.cTypes.cVec3:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetAt(self, Index: int) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cVec3:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cVec3:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetAndRemoveLast(self) -> cPy.cTypes.cVec3:
		pass # cpp source

	def SetAt(self, Index: int, Value: cPy.cTypes.cVec3):
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cVec3:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cVec3:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: cPy.cTypes.cVec3) -> cPy.cTypes.cVec3:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: cPy.cTypes.cVec3, defvalue: cPy.cTypes.cVec3):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: cPy.cTypes.cVec3):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: cPy.cTypes.cVec3):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: cPy.cTypes.cVec3, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: cPy.cTypes.cVec3, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: cPy.cTypes.cVec3, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: cPy.cTypes.cVec3, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: cPy.cTypes.cVec3, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: cPy.cTypes.cVec3) -> cPy.cTypes.cVec3:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: cPy.cTypes.cVec3) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: cPy.cTypes.cVec3) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> cPy.cTypes.cVec3:
		pass # cpp source

	def pop_back(self) -> cPy.cTypes.cVec3:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_cVec4():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: cPy.cTypes.cVec4, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> cPy.cTypes.cVec4:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> cPy.cTypes.cVec4:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> cPy.cTypes.cVec4:
		pass # cpp source

	def GetAt(self, Index: int) -> cPy.cTypes.cVec4:
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cVec4:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cVec4:
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cVec4:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cVec4:
		pass # cpp source

	def GetAndRemoveLast(self) -> cPy.cTypes.cVec4:
		pass # cpp source

	def SetAt(self, Index: int, Value: cPy.cTypes.cVec4):
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cVec4:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cVec4:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: cPy.cTypes.cVec4) -> cPy.cTypes.cVec4:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: cPy.cTypes.cVec4, defvalue: cPy.cTypes.cVec4):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: cPy.cTypes.cVec4):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: cPy.cTypes.cVec4):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: cPy.cTypes.cVec4, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: cPy.cTypes.cVec4, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: cPy.cTypes.cVec4, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: cPy.cTypes.cVec4, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: cPy.cTypes.cVec4, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: cPy.cTypes.cVec4) -> cPy.cTypes.cVec4:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: cPy.cTypes.cVec4) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: cPy.cTypes.cVec4) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> cPy.cTypes.cVec4:
		pass # cpp source

	def pop_back(self) -> cPy.cTypes.cVec4:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_cMat3():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: cPy.cTypes.cMat3, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> cPy.cTypes.cMat3:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> cPy.cTypes.cMat3:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> cPy.cTypes.cMat3:
		pass # cpp source

	def GetAt(self, Index: int) -> cPy.cTypes.cMat3:
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cMat3:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cMat3:
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cMat3:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cMat3:
		pass # cpp source

	def GetAndRemoveLast(self) -> cPy.cTypes.cMat3:
		pass # cpp source

	def SetAt(self, Index: int, Value: cPy.cTypes.cMat3):
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cMat3:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cMat3:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: cPy.cTypes.cMat3) -> cPy.cTypes.cMat3:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: cPy.cTypes.cMat3, defvalue: cPy.cTypes.cMat3):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: cPy.cTypes.cMat3):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: cPy.cTypes.cMat3):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: cPy.cTypes.cMat3, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: cPy.cTypes.cMat3, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: cPy.cTypes.cMat3, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: cPy.cTypes.cMat3, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: cPy.cTypes.cMat3, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: cPy.cTypes.cMat3) -> cPy.cTypes.cMat3:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: cPy.cTypes.cMat3) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: cPy.cTypes.cMat3) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> cPy.cTypes.cMat3:
		pass # cpp source

	def pop_back(self) -> cPy.cTypes.cMat3:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_cMat4():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: cPy.cTypes.cMat4, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> cPy.cTypes.cMat4:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> cPy.cTypes.cMat4:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> cPy.cTypes.cMat4:
		pass # cpp source

	def GetAt(self, Index: int) -> cPy.cTypes.cMat4:
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cMat4:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cMat4:
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cMat4:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cMat4:
		pass # cpp source

	def GetAndRemoveLast(self) -> cPy.cTypes.cMat4:
		pass # cpp source

	def SetAt(self, Index: int, Value: cPy.cTypes.cMat4):
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cMat4:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cMat4:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: cPy.cTypes.cMat4) -> cPy.cTypes.cMat4:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: cPy.cTypes.cMat4, defvalue: cPy.cTypes.cMat4):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: cPy.cTypes.cMat4):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: cPy.cTypes.cMat4):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: cPy.cTypes.cMat4, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: cPy.cTypes.cMat4, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: cPy.cTypes.cMat4, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: cPy.cTypes.cMat4, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: cPy.cTypes.cMat4, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: cPy.cTypes.cMat4) -> cPy.cTypes.cMat4:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: cPy.cTypes.cMat4) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: cPy.cTypes.cMat4) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> cPy.cTypes.cMat4:
		pass # cpp source

	def pop_back(self) -> cPy.cTypes.cMat4:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_tri_DWORD():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: any, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> any:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> any:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> any:
		pass # cpp source

	def GetAt(self, Index: int) -> any:
		pass # cpp source

	def GetFirst(self) -> any:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> any:
		pass # cpp source

	def GetLast(self) -> any:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> any:
		pass # cpp source

	def GetAndRemoveLast(self) -> any:
		pass # cpp source

	def SetAt(self, Index: int, Value: any):
		pass # cpp source

	def ToPtr(self) -> any:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> any:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: any) -> any:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: any, defvalue: any):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: any):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: any):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: any, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: any, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: any, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: any, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: any, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: any) -> any:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: any) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: any) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> any:
		pass # cpp source

	def pop_back(self) -> any:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source



class cArray_cStr():
	def begin(self) -> any:
		'''
			
		Returns an iterator to the beginning of the list.
		
		'''
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def begin(self) -> any:
		pass # cpp source

	def end(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Size(self) -> int:
		'''
			
		Returns the total size in bytes of the used elements.
		
		'''
		pass # cpp source

	def SizeCapacity(self) -> int:
		'''
			
		Returns the total size in bytes of the allocated memory.
		
		'''
		pass # cpp source

	def Copy(self, Src: cPy.cTypes.cStr, Count: int):
		'''
			
		Copies contents from a raw array.
		
		'''
		pass # cpp source

	def Move(self, from_idx: int, to_idx: int) -> bool:
		'''
			
		Moves an element within the list from one index to another.
		
		'''
		pass # cpp source

	def __assign__(self, _0: any, Src: any):
		return super().__assign__(_0, Src)

	def __getitem__(self, Index: int) -> cPy.cTypes.cStr:
		return super().__getitem__(Index)

	def __setitem__(self, Index: int) -> cPy.cTypes.cStr:
		return super().__setitem__(Index)

	def GetAt(self, Index: int) -> cPy.cTypes.cStr:
		pass # cpp source

	def GetAt(self, Index: int) -> cPy.cTypes.cStr:
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cStr:
		'''
			
		Returns reference to the first element.
		
		'''
		pass # cpp source

	def GetFirst(self) -> cPy.cTypes.cStr:
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cStr:
		'''
			
		Returns reference to the last element.
		
		'''
		pass # cpp source

	def GetLast(self) -> cPy.cTypes.cStr:
		pass # cpp source

	def GetAndRemoveLast(self) -> cPy.cTypes.cStr:
		pass # cpp source

	def SetAt(self, Index: int, Value: cPy.cTypes.cStr):
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cStr:
		'''
			
		Returns a const pointer to the raw array.
		
		'''
		pass # cpp source

	def ToPtr(self) -> cPy.cTypes.cStr:
		'''
			
		Returns a mutable pointer to the raw array.
		
		'''
		pass # cpp source

	def uGet(self, Index: int, defvalue: cPy.cTypes.cStr) -> cPy.cTypes.cStr:
		'''
			
		Unlimited get - get value at index Index, if beyoud range - return defvalue
		
		'''
		pass # cpp source

	def uSet(self, Index: int, value: cPy.cTypes.cStr, defvalue: cPy.cTypes.cStr):
		'''
			
		Unlimited set - set value at index Index, if beyoud range - add correcsponding count of defvalue-s
		
		'''
		pass # cpp source

	def Count(self) -> int:
		'''
			
		Gets the number of elements actually contained in the list.
		
		'''
		pass # cpp source

	def SetCount(self, Count: int):
		'''
			
		Sets the number of elements (resizes if necessary).
		
		'''
		pass # cpp source

	def SetCount(self, Count: int, Value: cPy.cTypes.cStr):
		'''
			
		Sets the count and initializes new elements with a value.
		
		'''
		pass # cpp source

	def Capacity(self) -> int:
		'''
			
		Gets the current allocated capacity.
		
		'''
		pass # cpp source

	def SetCapacity(self, Capacity: int):
		'''
			
		Pre-allocates memory for a specific capacity.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the list has no elements.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Sets count to 0 (does not free memory).
		
		'''
		pass # cpp source

	def Fill(self, Value: cPy.cTypes.cStr):
		'''
			
		Fills the entire list with a specific value.
		
		'''
		pass # cpp source

	def Add(self, Value: cPy.cTypes.cStr, Count: int = 1) -> int:
		'''
			
		Adds "Count" elements to the end of the list.

		Returns:
			int: The index of the first added element.
		
		'''
		pass # cpp source

	def AddValues(self, Values: cPy.cTypes.cStr, N: int):
		'''
			
		 \todo fine  Copied from class DynArray<>. Remove or rename it.
		
		'''
		pass # cpp source

	def AddRange(self, Src: cPy.cTypes.cStr, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Value: cPy.cTypes.cStr, Count: int = 1):
		'''
			
		Inserts element(s) at a specified position.
		
		'''
		pass # cpp source

	def InsertRange(self, Index: int, Src: cPy.cTypes.cStr, Count: int):
		'''
			
		Inserts an array at a specified position.
		
		'''
		pass # cpp source

	def ExpandTo(self, Index: int, _1: cPy.cTypes.cStr) -> cPy.cTypes.cStr:
		'''
			
		Ensures list is large enough for Index, then sets the value.
		
		'''
		pass # cpp source

	def InsertFirstOrRemove(self, _0: cPy.cTypes.cStr) -> bool:
		'''
			
		Toggles presence: inserts at 0 if missing, removes if present.
		
		'''
		pass # cpp source

	def RemoveAt(self, Index: int, Count: int = 1):
		'''
			
		Removes a range of elements starting at Index.
		
		'''
		pass # cpp source

	def RemoveLast(self):
		'''
			
		Removes the last element.
		
		'''
		pass # cpp source

	def find(self, Value: cPy.cTypes.cStr) -> int:
		'''
			
		Linear search using memcmp (warning: raw memory comparison).
		
		'''
		pass # cpp source

	def pop_front(self) -> cPy.cTypes.cStr:
		pass # cpp source

	def pop_back(self) -> cPy.cTypes.cStr:
		pass # cpp source

	def Reverse(self):
		pass # cpp source

	def Reverse(self, Index: int, Count: int):
		'''
			
		Reverses the order of the elements in the specified range.
		
		'''
		pass # cpp source

	def EnsureCapacity(self, size: int):
		'''
			
		Reserves memory for a specific size.
		
		'''
		pass # cpp source

