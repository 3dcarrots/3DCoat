from __future__ import annotations
import cPy.cTypes
import cPy.cScene
#cUI
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class RoomBehavior():
	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	RoomName: str #: std :: string (T)  
	def SetRoomName(self, room_name: str):
		pass # cpp source

	def Room(self) -> any:
		pass # cpp source

	def Apply(self):
		pass # cpp source

	def UseScriptsForToolset(self) -> bool:
		pass # cpp source

	def UseScriptsForMenu(self) -> bool:
		pass # cpp source

	def UseScriptsForNavigation(self) -> bool:
		pass # cpp source

	def UseScriptsForRmb(self) -> bool:
		pass # cpp source

	def UseScriptsForCurves(self) -> bool:
		pass # cpp source

	def UpdateToolsList(self):
		pass # cpp source

	def UpdateNavigationControls(self):
		pass # cpp source

	def UpdateMainMenu(self):
		pass # cpp source

	def OnStartPage(self):
		pass # cpp source

	def ShowPopupMenu(self, propertytype: str):
		pass # cpp source



class CustomRoom():

	@staticmethod
	def dynamic_cast(pObject : any)->CustomRoom:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a CustomRoom class or its descendant, and if so, returns the specified object, but of the CustomRoom type.
		'''
		pass # cpp source

	RoomName: cPy.cTypes.cStr #: cStr (T)  
	RoomFolderName: cPy.cTypes.cStr #: cStr (T)  
	SourceFile: cPy.cTypes.cStr #: cStr (T)  
	def GetRoomName(self) -> str:
		pass # cpp source

	def SetRoomName(self, room_name: str):
		pass # cpp source

	UseScriptsForToolset: bool #: bool (T)  
	UseScriptsForMenu: bool #: bool (T)  
	UseScriptsForNavigation: bool #: bool (T)  
	UseScriptsForRmb: bool #: bool (T)  
	UseScriptsForCurves: bool #: bool (T)  
	MandatoryRenderRetopoObjects: bool #: bool (T)  
	MandatoryRenderPaintObjects: bool #: bool (T)  
	UsePythonByDefault: bool #: bool (T)  
	ToolsetScriptText: cPy.cTypes.cStr #: cStr (T)  
	MenuScriptText: cPy.cTypes.cStr #: cStr (T)  
	NavigationText: cPy.cTypes.cStr #: cStr (T)  
	RmbText: cPy.cTypes.cStr #: cStr (T)  
	CurvesText: cPy.cTypes.cStr #: cStr (T)  
	LayoutText: cPy.cTypes.cStr #: cStr (T)  
	LockName: bool #: bool (T)  
	IsDefault: bool #: bool (T)  
	PerformLocalization: bool #: bool (T)  
	Visible: bool #: bool (T)  
	pBehavior: RoomBehavior #: RoomBehavior * (T)  
	def Behavior(self) -> RoomBehavior:
		pass # cpp source

	RMBPropertyType: str = Coat_CPP.CustomRoom.RMBPropertyType #: static std :: string (T)  
	SaveMode: bool = Coat_CPP.CustomRoom.SaveMode #: static bool (T)  
	SkipRmbMenuAppearance: bool = Coat_CPP.CustomRoom.SkipRmbMenuAppearance #: static bool (T)  
	CallPageInit: bool = Coat_CPP.CustomRoom.CallPageInit #: static bool (T)  
	RoomsLoaded: bool = Coat_CPP.CustomRoom.RoomsLoaded #: static bool (T)  
	RoomChanged: bool = Coat_CPP.CustomRoom.RoomChanged #: static bool (T)  
	ToolsList: any #: StringsList (T)  
	HiddenElements: any #: StringsList (T)  
	TemporaryTools: any #: StringsList (T)  
	Order: int #: int (T)  
	SpacePanelColumns: int #: int (T)  
	def __init__(self):
		pass # CPP source

	@staticmethod
	def drop_undo():
		pass # cpp source

	@staticmethod
	def RefreshInterface():
		pass # cpp source

	@staticmethod
	def CreateNewRoom(Name: str) -> CustomRoom:
		pass # cpp source

	@staticmethod
	def FindRoom(Name: str) -> CustomRoom:
		pass # cpp source

	@staticmethod
	def FindRoomByFolder(Name: str) -> CustomRoom:
		pass # cpp source

	@staticmethod
	def IsInCustomRoom() -> bool:
		pass # cpp source

	@staticmethod
	def LoadCustomRooms():
		pass # cpp source

	@staticmethod
	def SaveCustomRooms():
		pass # cpp source

	@staticmethod
	def CurrentCustomRoom() -> CustomRoom:
		pass # cpp source

	@staticmethod
	def CurrentRoomName() -> str:
		pass # cpp source

	@staticmethod
	def GetRootPath() -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def RestoreDefaultRoomsVisibility():
		pass # cpp source

	@staticmethod
	def RestoreAllRoomsVisibility():
		pass # cpp source

	@staticmethod
	def RestoreDefaultRoomsLayout():
		pass # cpp source

	@staticmethod
	def HideCurrentRoom():
		pass # cpp source

	@staticmethod
	def AddNewPage():
		pass # cpp source

	@staticmethod
	def StoreThisPageLayout():
		pass # cpp source

	@staticmethod
	def RestoreThisPageLayout():
		pass # cpp source

	@staticmethod
	def StoreAllPagesLayout():
		pass # cpp source

	@staticmethod
	def RestoreAllPagesLayout():
		pass # cpp source

	@staticmethod
	def SetVoxTreeContext(tb: cPy.cScene.VoxTreeBranch):
		pass # cpp source

	@staticmethod
	def SetCurveContext(tb: any):
		pass # cpp source

	@staticmethod
	def GetVoxTreeContext() -> cPy.cScene.VoxTreeBranch:
		pass # cpp source

	@staticmethod
	def GetCurveContext() -> any:
		pass # cpp source

	@staticmethod
	def SetGlobalContextForHotkeyAction():
		'''
			
		 when the hotkey is pressid this function setups contexts for RMB actions with hotkeys
		
		'''
		pass # cpp source

	@staticmethod
	def RunCustomRmbMenu(propertytype: str = "rmb"):
		'''
			
		Handle RMB UP. Call it within RMB UP handling routines
		
		'''
		pass # cpp source

	@staticmethod
	def StartCustomRmb():
		'''
			
		This command shold be called from script, no need to call it directly from program code
		
		'''
		pass # cpp source

	@staticmethod
	def FinishAndShowCustomRmb():
		'''
			
		If you called StartCustomRmb(), use menu commands lime menu_item(...) and then call FinishAndShowCustomRmb(). If you will not call it 3D-Coat will not work correctly!!!
		
		'''
		pass # cpp source

	@staticmethod
	def StopAllContexts():
		'''
			
		Stop all contexts when RMB panel disappears
		
		'''
		pass # cpp source

	@staticmethod
	def RmbPropPanelActive() -> bool:
		'''
			
		returns true if properties (RMB) panel is active.
		
		'''
		pass # cpp source

	@staticmethod
	def ToolForPage(Page: str) -> cPy.cTypes.cStr:
		'''
			
		returns reference to the name of the current tool for the given page
		
		'''
		pass # cpp source

	@staticmethod
	def PrevToolForPage(Page: str) -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def SetToolForPage(Page: str, tool: str):
		pass # cpp source

	@staticmethod
	def AutoUpdateToolForPage(tool: any, SubMode: int):
		pass # cpp source

	@staticmethod
	def GetCurrrentDefaultTool() -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def TryToSetNewDefailtTool(Tool: str):
		pass # cpp source

	@staticmethod
	def ActivateToolCommandByName(name: str):
		'''
			
		find and activate tool by it's name
		
		'''
		pass # cpp source

	@staticmethod
	def ActivateLastCustomRoom():
		pass # cpp source

	ActivationSource: cPy.cTypes.cStr = Coat_CPP.CustomRoom.ActivationSource #: static cStr (T)  
	@staticmethod
	def IsPythonScript(text: str) -> bool:
		pass # cpp source

	def GetRoomFileInfo(self, idx: int, r: any) -> bool:
		pass # cpp source

	def EditRoomParameters(self):
		pass # cpp source

	def AddTool(self, ToolID: str, Section: str):
		pass # cpp source

	def AddSection(self, SectionName: str):
		pass # cpp source

	def RemoveThisRoom(self):
		pass # cpp source

	def HideThisRoom(self):
		pass # cpp source

	def Rename(self, NewName: str) -> bool:
		pass # cpp source

	def SaveRoomLayout(self, filename: str):
		pass # cpp source

	def LoadRoomLayout(self, filename: str):
		pass # cpp source

	def AutoSaveRoomLayout(self):
		pass # cpp source

	def EditCppItem(self, suffix: str):
		pass # cpp source

	def AskAboutBaseToolset(self):
		pass # cpp source

	def EditScript(self, path: str):
		pass # cpp source

	def GetRoomFileRef(self, alias: str = "room.xml") -> cPy.cTypes.cStr:
		pass # cpp source

	def CheckIfFilesChanged(self):
		pass # cpp source

	def GetScript(self, suffix: str, script: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	def GetPyScriptPath(self, suffix: str) -> cPy.cTypes.cStr:
		pass # cpp source

	def ExecuteScript(self, suffix: str, function: str = "main"):
		pass # cpp source

	def DefaultsAvailable(self) -> bool:
		pass # cpp source

	def RestoreDefaultScriptsAndLayout(self):
		pass # cpp source

	def OnRmbOverItemInCustomMode(self, w: any):
		pass # cpp source

	def CopyToolsetFromOtherRoom(self):
		pass # cpp source

	@staticmethod
	def Hide(ID: str):
		'''
			
		Hiding management
		
		'''
		pass # cpp source

	@staticmethod
	def CheckHidden(ID: str, L: int = 0) -> bool:
		pass # cpp source

	@staticmethod
	def RemoveHidden(ID: str):
		pass # cpp source

	@staticmethod
	def HideSection(ID: str):
		pass # cpp source

	@staticmethod
	def UnHideSection(ID: str):
		pass # cpp source

	@staticmethod
	def HasSculptTools() -> bool:
		'''
			
		 Check for specific toolsets
		
		'''
		pass # cpp source

	@staticmethod
	def HasPaintTools() -> bool:
		pass # cpp source

	@staticmethod
	def HasRetopoTools() -> bool:
		pass # cpp source

	@staticmethod
	def HasModelingTools() -> bool:
		pass # cpp source

	@staticmethod
	def HasRender() -> bool:
		pass # cpp source

	@staticmethod
	def HasUVTools() -> bool:
		pass # cpp source

	def GetPageID(self) -> str:
		pass # cpp source

	ToolsPriory: any #: StringsList (T)  Drag&dropped items 
	def SortDragNDropped(self, List: any):
		pass # cpp source

	def DragAndDropTool(self, Src: str, dst: str, before: int):
		pass # cpp source

	def RaisePriory(self, Tool: str):
		pass # cpp source

	def RestoreDefaultOrder(self):
		pass # cpp source

	def AddCustomSectionAbove(self, SectionName: str, AbboveTool: str):
		pass # cpp source

	def RenameSection(self, SectionName: str, NewName: str):
		pass # cpp source

	def RemoveSection(self, SectionName: str):
		pass # cpp source

	@staticmethod
	def get_alias(str: cPy.cTypes.cStr, alias: cPy.cTypes.cStr):
		pass # cpp source

	@staticmethod
	def de_alias(id: cPy.cTypes.cStr) -> str:
		pass # cpp source

	@staticmethod
	def pure_id(id: cPy.cTypes.cStr) -> str:
		pass # cpp source

