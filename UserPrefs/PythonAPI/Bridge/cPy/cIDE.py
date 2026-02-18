from __future__ import annotations
import cPy.cTypes
#cIDE
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class cIDEOneEditor():
	def Update(self):
		pass # cpp source



class cHostScriptSource():
	host: any #: ndNGLNodeSource * (T)  
	ideEditor: cIDEOneEditor #: cIDEOneEditor * (T)  
	def getSource(self) -> str:
		pass # cpp source

	def getFilePath(self) -> str:
		pass # cpp source

	def setSource(self, src: str):
		pass # cpp source

	def setFilePath(self, src: str):
		pass # cpp source

	ChangedFromHost: bool #: bool (T)  
	IsOpennedInEditor: bool #: bool (T)  
	def SetIsOpennedInEditor(self, new_value: bool):
		pass # cpp source

	def Ping(self):
		pass # cpp source

	def OnChange(self):
		pass # cpp source

	def OnSave(self):
		pass # cpp source

	def OnClose(self):
		pass # cpp source



class cIDE():
	def __init__(self):
		pass # CPP source

	DefaultIDE: cIDE = Coat_CPP.cIDE.DefaultIDE #: static cIDE * (T)  
	@staticmethod
	def SetDefaultIDE(defaultIDE: cIDE):
		pass # cpp source

	def EditSource(self, scriptSource: cHostScriptSource):
		pass # cpp source

	def sendMessage(self, scriptSource: cHostScriptSource, message: str):
		pass # cpp source



class PTRecord():
	time: any #: __int64 (T)  
	message_type: str #: std :: string (T)  
	message: str #: std :: string (T)  
	code: str #: std :: string (T)  
	def __init__(self):
		pass # CPP source

	def __init__(self, aType: str, aMessage: str, aCode: str):
		pass # CPP source

	@staticmethod
	def add(aType: str, aMessage: str, aCode: str):
		pass # cpp source

	@staticmethod
	def replaceLast(aType: str, aMessage: str, aCode: str):
		pass # cpp source

	@staticmethod
	def count() -> int:
		pass # cpp source

	@staticmethod
	def get(idx: int) -> PTRecord:
		pass # cpp source



class PythonTerminalOut():
	def __init__(self):
		pass # CPP source

	TypeName: str #: std :: string (T)  
	def setType(self, type_name: str):
		pass # cpp source

	def write(self, message: str):
		pass # cpp source

	def flush(self):
		pass # cpp source



class PythonTerminal():
	_currentPythonTerminal: PythonTerminal = Coat_CPP.PythonTerminal._currentPythonTerminal #: static PythonTerminal * (T)  
	@staticmethod
	def Set(pythonTerminal: PythonTerminal):
		pass # cpp source

	@staticmethod
	def Get() -> PythonTerminal:
		pass # cpp source

	def OnRunScript(self):
		pass # cpp source

	def OnActivate(self):
		pass # cpp source

	def OnShow(self):
		pass # cpp source

	def OnMessage(self, type_name: str, message: str, code: str, message_time: any, replace_last: bool):
		pass # cpp source

	def __init__(self):
		pass # CPP source

	LegacyOutput: bool #: bool (T)  


class DefaultTerminal(PythonTerminal):

	@staticmethod
	def dynamic_cast(pObject : PythonTerminal)->DefaultTerminal:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a DefaultTerminal class or its descendant, and if so, returns the specified object, but of the DefaultTerminal type.
		'''
		pass # cpp source

	defaultTerminal: DefaultTerminal = Coat_CPP.DefaultTerminal.defaultTerminal #: static DefaultTerminal (T)  
	def __init__(self):
		pass # CPP source

	def OnRunScript(self):
		pass # cpp source

	def OnActivate(self):
		pass # cpp source

	def OnMessage(self, type_name: str, message: str, code: str, message_time: any, replace_last: bool):
		pass # cpp source



class CLSPToken():
	name: str #: std :: string (T)  
	comment: str #: std :: string (T)  
	childs: any #: comms :: cList<CLSPToken>(T)  


class CLikeSourceProcessor():
	result: cPy.cTypes.cStr #: cStr (T)  cStr RawResult; 
	currentPos: int #: int (T)  
	def __init__(self):
		pass # CPP source

	def ConvertTokens(self):
		pass # cpp source

	def FindNextToken(self, fromIdx: int) -> int:
		pass # cpp source

	def FindPrevToken(self, fromIdx: int) -> int:
		pass # cpp source

	def IsFunction(self, fromIdx: int) -> bool:
		pass # cpp source

	def HasBlockAfterLine(self, fromIdx: int) -> bool:
		pass # cpp source

	def IsBracketNext(self, fromIdx: int) -> bool:
		pass # cpp source

	def IsObjectName(self, idx: int) -> bool:
		pass # cpp source

	def Begin(self):
		pass # cpp source

	def Next(self) -> bool:
		pass # cpp source

	def CurrentToken(self) -> str:
		pass # cpp source

	def getNextToken(self) -> str:
		pass # cpp source

	def prevItem(self) -> str:
		pass # cpp source

	def setCurrentToken(self, value: str):
		pass # cpp source

	def setToken(self, idx: int, value: str):
		pass # cpp source

	def getToken(self, idx: int) -> str:
		pass # cpp source

	def TokenCount(self) -> int:
		pass # cpp source

	def removeToken(self, idx: int):
		pass # cpp source

	def swapTokens(self, idx1: int, idx2: int):
		pass # cpp source

	def insertToken(self, idx: int, value: str):
		pass # cpp source

	def RemoveAt(self, from_idx: int, count: int = 1):
		pass # cpp source

	def Insert(self, idx: int, value: str):
		pass # cpp source

	def FormatResult(self) -> str:
		pass # cpp source

	def IsKeyWord(self, aToken: str) -> bool:
		pass # cpp source

	listOfStrings: any #: comms :: cList_cStr (T)  
	listOfComments: any #: comms :: cList_cStr (T)  
	@staticmethod
	def copyFromCommentBody(source: cPy.cTypes.cStr) -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def DoxygenToStrdoc(aDoxygenComment: str) -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def StrdocToOneLine(aDocStr: cPy.cTypes.cStr) -> cPy.cTypes.cStr:
		pass # cpp source

	def RemoveRawSpaces(self, source: str) -> str:
		pass # cpp source

	def StringsToTokens(self, source: cPy.cTypes.cStr) -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def write_file(filename: str, content: cPy.cTypes.cStr):
		pass # cpp source

	def Preprocess(self, cppSource: str, filePath: str, defines: str):
		pass # cpp source

