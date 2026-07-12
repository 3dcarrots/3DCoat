from __future__ import annotations
import cPy.cTypes
#cCore
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum

def VoxelExts():
		'''
			
	#ifndef PY_PARSER
	
		'''
		pass # cpp source

def VoxelMenuExts():
		'''
			
	#ifndef PY_PARSER
	
		'''
		pass # cpp source

def VoxelExt(idx: int):
		'''
			
	#ifndef PY_PARSER
	
		'''
		pass # cpp source

def GetExtByID(id: int):
		'''
			
	#ifndef PY_PARSER
	
		'''
		pass # cpp source


class BaseClass():
	'''
			
		Use this class for build a class for UI or serialization.
		see class_reg.h for details about the class registration
		
	'''

	is_py_owned: bool #: bool (T)  This variable tells who will delete the object if the object is owned by python (if it was created in python) - it will not be deleted automatically when deleting or clearing the ClassArray 
	def __init__(self):
		pass # CPP source

	def __init__(self) -> any:
		pass # CPP source

	def GetClassMask(self) -> int:
		'''
			
		 Masking elements of class. Each member has mask. Element is serializable/visible only if (it's_mask & hosting_class_mask) != 0
		
		'''
		pass # cpp source

	def ClassMask(self) -> int:
		pass # cpp source

	def runFunction(self, func: any):
		pass # cpp source

	def reset_class(self, DataPtr: any = None):
		pass # cpp source

	def CopyBaseClass(self, Dest: BaseClass, Add: bool = False) -> bool:
		'''
			
		Copy base class to other class uning names correspondence

		Args:
			Dest (BaseClass): The destination object
			Add (bool): Add members to class arrays or replace

		Returns:
			bool: true if successful
		
		'''
		pass # cpp source

	def Save(self, xml: any, ClassPtr: any, Extra: any = None):
		'''
			
		Save class to the XML structure

		Args:
			xml : The result
			ClassPtr : The pointer to the data, equals to this if class is directly castable
			Extra : Extra data pointer
		
		'''
		pass # cpp source

	def Load(self, xml: any, ClassPtr: any, Extra: any = None) -> bool:
		'''
			
		Load the class from the XML structure

		Args:
			xml : The source XML
			ClassPtr : The pointer to the data, equals to this if class is directly castable
			Extra : Extra data pointer

		Returns:
			bool: true if successful
		
		'''
		pass # cpp source

	def FullCopy(self, SrcData: any, SrcDataExtra: any, Dest: BaseClass, DestData: any, DstDataExtra: any, C: any) -> bool:
		'''
			
		Fast copy from one BaseClass to another. Names and types correspondence used to copy.

		Args:
			SrcData : Data data pointer
			SrcDataExtra : Src extra
			Dest (BaseClass): Destination class
			DestData : Destination data
			DstDataExtra : Destination extra
			C : copy context

		Returns:
			bool: true if successful
		
		'''
		pass # cpp source

	def SaveBin(self, Data: any, Extra: any, Out: any, ExDictionary: any, SkipList: any):
		'''
			
		Save in binaly form. Use only for temporary storage in memory!!!

		Args:
			Data : data pointer
			Extra : extra pointer
			Out : Output stream
			ExDictionary : Dictionary for enumerators
			SkipList : Skip list for enumerators
		
		'''
		pass # cpp source

	def LoadBin(self, Data: any, Extra: any, In: any, ExDictionary: any):
		'''
			
		Load the class from the memory. Use only for temporary storage in memory!!!

		Args:
			Data : Pointer to the class data
			Extra : Extra data
			In : binary stream to read data from
			ExDictionary : Additional dictionary
		
		'''
		pass # cpp source

	def GetAmountOfElementsInUI(self) -> int:
		'''
			
		return amount of elements represented in UI
		
		'''
		pass # cpp source

	def GetAmountOfElementsInXML(self) -> int:
		'''
			
		return amount of elements taht will be stored in XML
		
		'''
		pass # cpp source

	def pySerialize(self):
		'''
			
		serialize and UI for python
		
		'''
		pass # cpp source

	def pySerializeParentClass(self) -> bool:
		pass # cpp source

	def get_class_name(self) -> str:
		pass # cpp source

	def new_element(self) -> BaseClass:
		'''
			
		construct pointer to class of the same type like this. Elements will not be copied into the new place
		
		'''
		pass # cpp source

	def GetElement(self, res: any, idx: int, Ptr: any = None, Extra: any = None) -> bool:
		'''
			
		The The function returns complete information about the member by it's index. If you want to walk through all members use _EACH ... _EACH_END loop.

		Args:
			res : All data gathered there
			idx (int): Index of the member
			Ptr : Pointer to data (if class is direcly castable it is equal to this, othervice it points to placement of data in memory). If NULL passed, this will be used
			Extra : Extra data, used for enumerators and sliders (mostly)

		Returns:
			bool: return true if element exists and visible
		
		'''
		pass # cpp source

	def GetElementByName(self, Name: str, Ptr: any, Extra: any, res: any, UI: bool = False, Serialize: bool = True) -> bool:
		'''
			
		The function returns complete information about the member by it's name.

		Args:
			Name (str): Name of the member
			Ptr : Data ptr
			Extra : Extra
			res : All data gathered there

		Returns:
			bool: return true if element exists and visible
		
		'''
		pass # cpp source

	def GetElementByNameAndType(self, Name: str, Type: str, Ptr: any, Extra: any, res: any, UI: bool = False, Serialize: bool = True) -> bool:
		pass # cpp source

	def DeleteDefaultSubFields(self, xml: any, ClassPtr: any, Extra: any = None):
		'''
			
		 Short form saving. Fields that are unchanged in comparison to default will be skipped in XML.
		
		'''
		pass # cpp source

	def ShouldSaveInShortForm(self) -> bool:
		'''
			
		Return true if class should be saved in short form mandatory 
		
		'''
		pass # cpp source

	def ExpandWith(self, ElmName: str, base: any) -> int:
		pass # cpp source

	def DelElement(self, Index: int) -> bool:
		pass # cpp source

	def auto_cast(self, ptr: any) -> BaseClass:
		pass # cpp source

	def ReadFromFile(self, Name: str, very_safe_with_backup: bool = False) -> bool:
		'''
			
		Save the object to file or binary stream.
		Example
		
		::

			MyClass C;
			MyClass C1;
			    *
			// to stream
			MemoryBinStream BS;
			C.ToBS(BS, true);
			// copy from C to C1
			C1.FromBS(BS);
			    *
			// to file
			C.WriteToFile("file.xml");
			C1.ReadFromFile("file.xml");
			    *
			// to string
			cStr s;
			C.ToStr(s);
			C1.FromStr(s);
			

		
		'''
		pass # cpp source

	def WriteToFile(self, Name: str) -> bool:
		pass # cpp source

	def WriteToFileIfChanged(self, Name: str) -> bool:
		pass # cpp source

	def ToStr(self, bs: any):
		pass # cpp source

	def FromStr(self, bs: any):
		'''
			
		 \see ToBS()
		
		'''
		pass # cpp source

	def SetParent(self, Parent: BaseClass):
		'''
			
		set parent recursively
		
		'''
		pass # cpp source

	def SimplySetParent(self, Parent: BaseClass):
		'''
			
		set parent directly to this, not affecting members
		
		'''
		pass # cpp source

	def MayBeParent(self) -> bool:
		pass # cpp source

	def CheckCompartabilityWith(self, TypeName: str, TypeSize: int) -> bool:
		pass # cpp source

	def ProcessInEditor(self, Parent: BaseClass) -> bool:
		pass # cpp source

	def RenderInScene(self, Parent: BaseClass) -> bool:
		pass # cpp source

	def HandleKey(self, code: int) -> bool:
		pass # cpp source

	def OnChangeMember(self, MembClass: BaseClass, MembPtr: any, MembExtra: any, MembName: str) -> bool:
		pass # cpp source

	def BeforeChangeMember(self, MembClass: BaseClass, MembPtr: any, MembExtra: any, MembName: str):
		pass # cpp source

	def GetElementLevel(self, EName: str) -> int:
		pass # cpp source

	def OnCreateControlFromScratch(self, Context: any, Rect: cPy.cTypes.Rct) -> any:
		pass # cpp source

	def OnModifyControl(self, FieldName: str, W: any, Context: any):
		pass # cpp source

	def CanBeDragged(self, MemberID: str, dx: int, dy: int) -> bool:
		'''
			
		Use it for build a Drag & Drop element.
		\see CanAcceptDrag(), OnStartDrag(), OnEndDrag(), OnAcceptDrag()
		
		'''
		pass # cpp source

	def CanAcceptDrag(self, MemberID: str) -> bool:
		pass # cpp source

	def OnStartDrag(self, MemberID: str) -> bool:
		pass # cpp source

	def OnEndDrag(self, MemberID: str) -> bool:
		pass # cpp source

	def OnAcceptDrag(self, DraggedItemParent: BaseClass, DraggedMemberID: str, AcceptorMemberID: str, MyRect: any) -> bool:
		pass # cpp source

	def UsePointerInHashCalculation(self) -> bool:
		pass # cpp source

	def SkipHash(self) -> bool:
		pass # cpp source

	def IsArray(self) -> bool:
		pass # cpp source

	def GetCmdID(self) -> str:
		pass # cpp source

	def isNotParent(self) -> bool:
		pass # cpp source

	def SetParents(self):
		pass # cpp source

	def SetParentsSafe(self):
		'''
			
		set parents to this for all child members, each child will be tested for validity
		
		'''
		pass # cpp source

	@staticmethod
	def GetCurrentSaveFile() -> str:
		pass # cpp source

	CurrentSaveFile: str = Coat_CPP.BaseClass.CurrentSaveFile #: static const char * (T)  If user triggers saving class to file, last filename stored there 
	def UpdateClassMembersAndMask(self, recursive: bool):
		pass # cpp source

	SaveInShortForm: bool = Coat_CPP.BaseClass.SaveInShortForm #: static bool (T)  
	@staticmethod
	def UI_definition() -> bool:
		pass # cpp source

	@staticmethod
	def Serialization() -> bool:
		pass # cpp source



class cTool(BaseClass):
	'''
			
		Class for tools.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : BaseClass)->cTool:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cTool class or its descendant, and if so, returns the specified object, but of the cTool type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	ID: int #: int (T)  
	CustomName: cPy.cTypes.cStr #: cStr (T)  Custom name of the tool. 
	SourceIcon: cPy.cTypes.cStr #: cStr (T)  Path to the tool's icon. 
	CmdID: cPy.cTypes.cStr #: cStr (T)  Command identifier for calling the tool. 
	BaseParentTool: cPy.cTypes.cStr #: cStr (T)  Used if tool duplicated. This is very base of the tool, it does not changes when tool duplicated. This is like "grand-grand...father" 
	PreviousParentTool: cPy.cTypes.cStr #: cStr (T)  This is ID of parent, like "father" tool 
	key: cPy.cTypes.cStr #: cStr (T)  Encryption key for saving presets. 
	IsActive: bool #: bool (T)  Indicates whether the tool is currently active. 
	AppearsInSmoothActions: bool #: bool (T)  Indicates if the tool applies during smoothing actions. 
	Current: cTool = Coat_CPP.cTool.Current #: static cTool * (T)  Pointer to the currently active tool. 
	GeneralUsage: bool = Coat_CPP.cTool.GeneralUsage #: static bool (T)  `true` if `cTool` used outside of voxel room. 
	PrevInterpValue: float #: float (T)  Previous interpolation value. 
	PrevInterp: bool #: bool (T)  Previous interpolation state. 
	AbleToSnap: bool #: bool (T)  Indicates if the tool supports snapping. 
	ActivatedMandatory: bool #: bool (T)  Flag for mandatory tool activation. 
	SomethingChanged: bool = Coat_CPP.cTool.SomethingChanged #: static bool (T)  Global flag indicating changes in the scene. 
	ExtHash: int = Coat_CPP.cTool.ExtHash #: static int (T)  Extension hash. 
	TemporaryDisablePresetActivation: bool = Coat_CPP.cTool.TemporaryDisablePresetActivation #: static bool (T)  Temporarily disables preset activation. 
	def GetFullID(self) -> str:
		pass # cpp source

	def AssignExternalIcon(self, iconname: str):
		pass # cpp source

	def ChooseIcon(self):
		pass # cpp source

	def Activate(self):
		pass # cpp source

	@staticmethod
	def Register(ex: cTool) -> any:
		'''
			
		Call this function to register own extension.
		
		Go to cTool.cpp, include your header,
		call cTool::Register in function RegisterVoxelExtensions().
		
		'''
		pass # cpp source

	@staticmethod
	def GetHook() -> cTool:
		pass # cpp source

	@staticmethod
	def find(id: str) -> cTool:
		pass # cpp source

	@staticmethod
	def CheckFieldPresence(FieldName: str) -> bool:
		pass # cpp source

	def SwitchTo(self):
		'''
			
		 Please use this function to activate the tool
		
		'''
		pass # cpp source

	def GetID(self) -> str:
		'''
			
		 Define Textual ID in tools list.
		
		'''
		pass # cpp source

	def CheckParentTool(self, _0: int) -> bool:
		pass # cpp source

	def OnActivatePreset(self):
		pass # cpp source

	def NeedToStoreToolPreset(self) -> bool:
		pass # cpp source

	def RestoreExtensionPreset(self):
		pass # cpp source

	def StoreExtensionPreset(self, asPreset: bool = False):
		pass # cpp source

	def OnPlaceInUI(self):
		pass # cpp source

	def GetPresetFileName(self) -> cPy.cTypes.cStr:
		pass # cpp source

	def AllowUVIslandsPreview(self) -> bool:
		pass # cpp source

	def OverrideCluster(self, cl: int) -> any:
		pass # cpp source

	def GetPlacementPriory(self) -> int:
		pass # cpp source

	def GetPrevTool(self) -> str:
		pass # cpp source

	def PresentInVoxelTools(self) -> bool:
		pass # cpp source

	def MayModifyVoxelsAsSurface(self) -> bool:
		pass # cpp source

	def PresentInSurfaceTools(self) -> bool:
		'''
			
		 Returns `true` if the tool is present in voxel surface toolset.
		
		'''
		pass # cpp source

	def PresentInRetopoTools(self) -> bool:
		pass # cpp source

	def PresentInUvTools(self) -> bool:
		pass # cpp source

	def PresentInPaintTools(self) -> bool:
		pass # cpp source

	def PresentInTweakTools(self) -> bool:
		pass # cpp source

	def PresentInPhotogrammetryTools(self) -> bool:
		pass # cpp source

	def PresentInRoom(self, RoomName: str) -> bool:
		pass # cpp source

	def CreateToolset(self) -> bool:
		'''
			
		Create toolset on the top line.
		\see VoxelSculptTool::CreateToolset() as example
		
		'''
		pass # cpp source

	def CreateInterface(self, Where: any) -> bool:
		'''
			
		 Creates parameters plate of this tool.
		
		'''
		pass # cpp source

	def Process(self):
		pass # cpp source

	def Render(self):
		pass # cpp source

	def RenderPreviewAsVolume(self, Sh: int):
		pass # cpp source

	def OnLMB_Down(self) -> bool:
		pass # cpp source

	def OnLMB_Up(self) -> bool:
		pass # cpp source

	def OnDBL(self) -> bool:
		pass # cpp source

	def OnMMB_Down(self) -> bool:
		pass # cpp source

	def OnMMB_Up(self) -> bool:
		pass # cpp source

	def OnRMB_Down(self) -> bool:
		pass # cpp source

	def OnRMB_Up(self) -> bool:
		pass # cpp source

	def OnUndo(self) -> bool:
		pass # cpp source

	def OnRedo(self) -> bool:
		pass # cpp source

	def DisableRedo(self) -> bool:
		pass # cpp source

	def OnWheel(self, step: int) -> bool:
		pass # cpp source

	def AllowIncrementalRender(self) -> bool:
		pass # cpp source

	def OnKey(self, KeyCode: any) -> bool:
		pass # cpp source

	def AllowMMBNavigation(self) -> bool:
		pass # cpp source

	def AllowRMBNavigation(self) -> bool:
		pass # cpp source

	def AllowRadisRMBControl(self) -> bool:
		pass # cpp source

	def CanDrawInFreeSpace(self) -> bool:
		pass # cpp source

	def OnActivate(self):
		pass # cpp source

	def OnDeActivate(self):
		pass # cpp source

	def IsToolsAction(self) -> bool:
		pass # cpp source

	def OnClear(self):
		pass # cpp source

	def ClearMyToolPreset(self):
		pass # cpp source

	def OnClearVolume(self):
		pass # cpp source

	def OnIncRes(self) -> bool:
		pass # cpp source

	def OnResample(self) -> bool:
		pass # cpp source

	def OnSmoothAll(self) -> bool:
		pass # cpp source

	def OnChangeCurVolume(self, newCur: any):
		pass # cpp source

	def OnChangeCurVolumeManually(self, newCur: any):
		pass # cpp source

	def OnVoxelize(self):
		pass # cpp source

	def OnMakeSurface(self):
		pass # cpp source

	def DisableRadiusVariation(self) -> bool:
		pass # cpp source

	def DrawOnPlane(self) -> bool:
		pass # cpp source

	def AbleToDrawOnPlane(self) -> bool:
		pass # cpp source

	def OnRectSelectionEnd(self, R: cPy.cTypes.Rct) -> bool:
		pass # cpp source

	@staticmethod
	def SafeRectSelection(R: cPy.cTypes.Rct) -> bool:
		pass # cpp source

	def ApplyEnterInCurves(self) -> bool:
		'''
			
		 \brief Determines if the tool applies the 'Enter' key action specifically within curve editing.
		
		'''
		pass # cpp source

	def AllowRectSelection(self) -> bool:
		pass # cpp source

	def AllowOnlyRectSelection(self) -> bool:
		pass # cpp source

	def ApplyCurvesAsRectSelection(self) -> bool:
		pass # cpp source

	def AllowStamp(self) -> bool:
		pass # cpp source

	def AllowLinesDrawing(self) -> bool:
		pass # cpp source

	def AllowRectDrawing(self) -> bool:
		pass # cpp source

	def AllowLassoDrawing(self) -> bool:
		pass # cpp source

	def AllowCircleDrawing(self) -> bool:
		pass # cpp source

	def NeedToClearPointsOnDBLClick(self) -> bool:
		pass # cpp source

	def Use3DLasso(self) -> bool:
		pass # cpp source

	def Snap3DLasso(self) -> bool:
		pass # cpp source

	def AllowRemoveStretching(self) -> bool:
		pass # cpp source

	def AllowDrag(self) -> bool:
		pass # cpp source

	def OnDraw(self):
		pass # cpp source

	def NeedTrajectory(self) -> int:
		'''
			
		
		
		Returns `1` if you need to construct brush trajectory with `TMaster` including end points
		and `2` if you need to include start point in trajectory,
		`0` if you don't need `TMaster` at all.
		
		'''
		pass # cpp source

	def NeedConstructTrajectory(self) -> bool:
		pass # cpp source

	def AutoFadeOnEdge(self) -> bool:
		pass # cpp source

	def UseBezierTrajectorySmoothing(self) -> bool:
		pass # cpp source

	def NeedFirstPoint(self) -> bool:
		pass # cpp source

	def OverrideSpacing(self, Spots: bool) -> float:
		pass # cpp source

	def NeedGlobalIndexing(self) -> bool:
		pass # cpp source

	def NeedFacesAdjacensy(self) -> bool:
		pass # cpp source

	def NeedBrushMipmaps(self) -> bool:
		pass # cpp source

	def PickAveragePos(self) -> bool:
		pass # cpp source

	def PickCurrentPos(self) -> bool:
		pass # cpp source

	def NeedAutoCellsSubdivision(self) -> bool:
		pass # cpp source

	def CheckIfToolIsBeta(self) -> bool:
		pass # cpp source

	def MayActThroughVolumes(self) -> bool:
		pass # cpp source

	def NeedPenControls(self) -> bool:
		pass # cpp source

	def SkipFaloffControls(self) -> bool:
		pass # cpp source

	def OverridesBrushRotationJitterSpacing(self) -> bool:
		pass # cpp source

	def NeedDepthControls(self) -> bool:
		pass # cpp source

	def SupportRectSurfDistortion(self) -> bool:
		pass # cpp source

	def NeedBorderShape(self) -> bool:
		pass # cpp source

	def AllowGrowOnPenMotion(self) -> bool:
		pass # cpp source

	def PickOnlyFirstPoint(self) -> bool:
		pass # cpp source

	def PickEmptySpace(self) -> bool:
		pass # cpp source

	def MayChangeTopology(self) -> bool:
		pass # cpp source

	def UseInterpolationByDefault(self, _0: float) -> bool:
		pass # cpp source

	def OnEndOfStroke(self, ob: any):
		pass # cpp source

	def SnapMidPoints(self) -> bool:
		pass # cpp source

	def GetMimickTool(self) -> int:
		pass # cpp source

	def SkipSurfWarning(self) -> bool:
		pass # cpp source

	def AllowInvertAction(self) -> bool:
		pass # cpp source

	def NeedFlatternCurve(self, v0: float, v1: float) -> bool:
		pass # cpp source

	def NeedSplinesMenu(self) -> bool:
		pass # cpp source

	def RequiresPresetActivation(self) -> bool:
		pass # cpp source

	def GetTrackingSpacing(self) -> float:
		pass # cpp source

	def AllowSplineStroke(self) -> int:
		'''
			
		 0 - disable, 1 - allow, 2 - in 2D mode
		
		'''
		pass # cpp source

	def GetRadiusMod(self) -> float:
		pass # cpp source

	def SupportsSelCentering(self) -> bool:
		pass # cpp source

	def AllowAutoPick(self) -> int:
		pass # cpp source

	def GetPrim(self) -> any:
		pass # cpp source

	def AllowSamplingRadius(self) -> bool:
		pass # cpp source

	def OverridePositionalSamplingRadius(self) -> float:
		pass # cpp source

	def AllowBuildup(self) -> bool:
		pass # cpp source

	def AllowStrightHandler(self) -> bool:
		pass # cpp source

	def AllowCubeHandler(self) -> bool:
		pass # cpp source

	def AllowMixedPicking(self) -> bool:
		pass # cpp source

	def NeedCubicTrajectory(self) -> bool:
		pass # cpp source

	def NeedsDepthLimitInEPanel(self) -> bool:
		pass # cpp source

	def IgnoreNaviEvent(self, Event: any) -> bool:
		pass # cpp source

	def RequiresExtraTopLine(self) -> int:
		pass # cpp source

	def OnCreateTopToolPanel(self):
		pass # cpp source

	def AllowShiftSmooth(self) -> bool:
		'''
			
		 You may disable smoothing with shift.
		
		'''
		pass # cpp source

	def OnPresetActivation(self, PS: any):
		pass # cpp source

	def OnCreatePreset(self, PS: any):
		'''
			
		 Called when preset created manually by user.
		
		'''
		pass # cpp source

	def AllowAdditiveSelection(self) -> bool:
		'''
			
		called to add transformed proxy objects into scene
		
		'''
		pass # cpp source

	def TransformInRetopo(self, m: cPy.cTypes.cMat4):
		pass # cpp source

	def OnSelectModelInPalette(self, ModelName: str, RootPath: str, InCurrentTool: bool) -> bool:
		'''
			
		 Called when user chosen model in models palette, return `true` if model used and action captured.
		
		'''
		pass # cpp source

	def GetNumSaveChunks(self) -> int:
		pass # cpp source

	def GetSaveMagic(self, ChunkIdx: int) -> int:
		pass # cpp source

	def LoadData(self, ChunkIdx: int, BS: any):
		pass # cpp source

	def SaveData(self, ChunkIdx: int, BS: any):
		'''
			
		Store data to the 3B file using Bin stream.
		
		This function will be called 2 times during saving -
		once for size calculation, second - actually for saving.
		
		'''
		pass # cpp source

	def BeforeSave(self, filename: str):
		'''
			
		BeforeSave called each time before saving scene.
		
		'''
		pass # cpp source

	def onApply(self) -> bool:
		'''
			
		Perform action by ENTER key and return `true` if tool does not allow default ENTER action.
		
		'''
		pass # cpp source

	def GetBottomOffset(self) -> float:
		pass # cpp source

	def NeedPutPointOnSurfaceInSoftStrokeMode(self) -> bool:
		pass # cpp source

	def RenderGuides(self):
		pass # cpp source

	def GetClipPlane(self, pl: any) -> bool:
		pass # cpp source

	def SupportsMultithreadedePicking(self) -> bool:
		pass # cpp source

	def OnPick(self, x: float, y: float, pic: any):
		pass # cpp source

	def GetCmdID(self) -> str:
		pass # cpp source

	def SnapIsActive(self) -> bool:
		pass # cpp source

	def SnapPoint(self, pt: any) -> bool:
		pass # cpp source

	def NeedToClearLeakyPosDuringUndo(self) -> bool:
		pass # cpp source

	def ZeroPressureOutsideTheObject(self) -> bool:
		pass # cpp source

	def ZeroRadiusOutsideTheObject(self) -> bool:
		pass # cpp source

	def IgnoreFieldInTopPanel(self, FieldName: str) -> bool:
		pass # cpp source

	@staticmethod
	def IgnoreFieldInUI(FieldName: str) -> bool:
		pass # cpp source

	def SmoothAllSelectedOnly(self) -> bool:
		pass # cpp source

	def SupportsAutoRetopoMeshUpdate(self) -> bool:
		pass # cpp source

	def TopologyNeverChanges(self) -> bool:
		pass # cpp source

	def HasOwnStampModeHandler(self) -> bool:
		pass # cpp source

	def OnCreateNewCurve(self, cu: any):
		pass # cpp source

	def BeforeGizmolessTransform(self, dropUndo: bool, resPivot: cPy.cTypes.cVec3) -> bool:
		pass # cpp source

	def TransformSelected(self, OVR: cPy.cTypes.cMat4, InitialCapPoint: cPy.cTypes.cVec3) -> bool:
		pass # cpp source

	def OnSelectItem(self, Category: str):
		pass # cpp source

	def AnswerQuestion(self, question: str, data: BaseClass, answer: cPy.cTypes.cStr) -> int:
		'''
			
		 return the priority of the answer, 0 - the answer is unknown, anything above means higher priority
		
		'''
		pass # cpp source

	def OnTransformEverything(self, m_visual: cPy.cTypes.cMat4, m_export: cPy.cTypes.cMat4):
		pass # cpp source



class CommandButton(cTool):
	'''
			
		Register as usual cTool::Register(new MyButton);
		
	'''


	@staticmethod
	def dynamic_cast(pObject : BaseClass)->CommandButton:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a CommandButton class or its descendant, and if so, returns the specified object, but of the CommandButton type.
		'''
		pass # cpp source

	def IsToolsAction(self) -> bool:
		pass # cpp source

	def GetID(self) -> str:
		pass # cpp source

	def GetPrevTool(self) -> str:
		pass # cpp source

	def PresentInRoom(self, RoomName: str) -> bool:
		pass # cpp source

	def OnActivate(self):
		pass # cpp source



class MainMenuExtension(BaseClass):

	@staticmethod
	def dynamic_cast(pObject : BaseClass)->MainMenuExtension:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a MainMenuExtension class or its descendant, and if so, returns the specified object, but of the MainMenuExtension type.
		'''
		pass # cpp source

	@staticmethod
	def Register(ex: MainMenuExtension):
		'''
			
		 Call this function to register own extension
		
		'''
		pass # cpp source

	def GetNumLines(self) -> int:
		'''
			
		 Number of lines in Voxels RMB menu
		
		'''
		pass # cpp source

	def GetID(self, Line: int) -> str:
		pass # cpp source

	def GetHint(self, Line: int) -> str:
		pass # cpp source

	def GetSubmenuID(self) -> str:
		pass # cpp source

	def GetHostMenu(self) -> str:
		pass # cpp source

	def IsInRMBMenu(self) -> bool:
		pass # cpp source

	def IsInMainMenu(self) -> bool:
		pass # cpp source

	def GetPrevItemID(self) -> str:
		pass # cpp source

	def Perform(self, idx: int):
		pass # cpp source



class cSItem():
	def __init__(self):
		pass # CPP source

	Name: str #: std :: string (T)  
	Visible: bool #: bool (T)  
	def getName(self) -> str:
		pass # cpp source



class cSBool(cSItem):

	@staticmethod
	def dynamic_cast(pObject : cSItem)->cSBool:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cSBool class or its descendant, and if so, returns the specified object, but of the cSBool type.
		'''
		pass # cpp source

	Value: bool #: bool (T)  
	def __init__(self, name: str, value: bool = False, visible: bool = True):
		pass # CPP source



class cSColor(cSItem):

	@staticmethod
	def dynamic_cast(pObject : cSItem)->cSColor:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cSColor class or its descendant, and if so, returns the specified object, but of the cSColor type.
		'''
		pass # cpp source

	Value: int #: DWORD (T)  
	def __init__(self, name: str, value: int = 0, visible: bool = True):
		pass # CPP source



class cSString(cSItem):

	@staticmethod
	def dynamic_cast(pObject : cSItem)->cSString:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cSString class or its descendant, and if so, returns the specified object, but of the cSString type.
		'''
		pass # cpp source

	Value: str #: std :: string (T)  
	def __init__(self, name: str, value: str, visible: bool = True):
		pass # CPP source



class cSInt(cSItem):

	@staticmethod
	def dynamic_cast(pObject : cSItem)->cSInt:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cSInt class or its descendant, and if so, returns the specified object, but of the cSInt type.
		'''
		pass # cpp source

	Min: int #: int (T)  
	Max: int #: int (T)  
	Default: int #: int (T)  
	Value: int #: int (T)  
	def __init__(self, name: str, value: int = 0, min: int = 0, max: int = 10, visible: bool = True):
		pass # CPP source



class cSFloat(cSItem):

	@staticmethod
	def dynamic_cast(pObject : cSItem)->cSFloat:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cSFloat class or its descendant, and if so, returns the specified object, but of the cSFloat type.
		'''
		pass # cpp source

	Min: float #: float (T)  
	Max: float #: float (T)  
	Value: float #: float (T)  
	Default: float #: float (T)  
	def __init__(self, name: str, value: float = 0, min: float = 0, max: float = 10, visible: bool = True):
		pass # CPP source



class cREG():
	@staticmethod
	def modalMessageBox(text: str, Caption: str, Buttons: str, Flags: int, Class: BaseClass) -> int:
		pass # cpp source

	@staticmethod
	def reg_class(class_ref: BaseClass):
		pass # cpp source

	@staticmethod
	def function_call(ui_cmd: str):
		pass # cpp source

	@staticmethod
	def checkbox(cb: cSBool):
		pass # cpp source

	@staticmethod
	def delimiter():
		pass # cpp source

	def _droplist(self, field: cSInt, enum_id: str):
		pass # cpp source

	@staticmethod
	def droplist(field: cSInt, enum_id: str):
		'''
			
		REG_DROPLIST(fieldID, name, EnumID) adds the droplist to UI, list into XML. The referred variable should be int
		\hideinitializer
		
		Example:
		 
		::

			 class MyClass : public BaseClass{
			
			     int x1;
			     int x2;
			     SERIALIZE(){
			         ...
			         //create enumerator just now and use immediately
			         REG_DROPLIST(x1, "droplist1", "Item1|Item2|Item3");
			
			         //Other option is to create Enumerator right there or somewhere in code
			         _MAKE_ONCE{//use it to avoid multiple call of code
			             Enumerator* E = ENUM.Get("MYENUMERATOR");
			             if(E->GetAmount() == 0){
			                 E->Add("SomeItem1",Value1);
			                 E->Add("SomeItem1",Value2);
			                 ...
			             }
			         }
			         REG_DROPLIST(x2, "droplist2", "MYENUMERATOR");
			
			         //You may define Enumerator just in one line
			         MAKE_ENUMERATOR("MYENUMERATOR2","Item1|Item2|Item3");
			         REG_DROPLIST(x2, "droplist2", "MYENUMERATOR2");
			         ...
			     }
			 };
			 

		
		'''
		pass # cpp source

	@staticmethod
	def make_enumerator(enum_id: str, content: str):
		'''
			
		Make Enumerator in just one line
		\hideinitializer
		
		
		::

			MAKE_ENUMERATOR("MYENUMERATOR2","Item1|Item2|Item3");
			     *
			....somewhere...
			     *
			REG_DROPLIST(x2, "droplist2", "MYENUMERATOR2");
			


		Args:
			content (str): List of items "Item1,Item2,...."
		
		'''
		pass # cpp source

	@staticmethod
	def ui_layout(layout: str):
		'''
			
		UI_LAYOUT(str) splits ui elements to several columns with proportional or fixed width
		\hideinitializer
		
		UI_LAYOUT may use two additional keywords: TOP and BOTTOM. TOP moves controls to the tor of the window frame (header -like)\n
		 BOTTOM moves elements to the bottom of the frame, like toolset buttons. It is recommended to use ICON_BUTTON/3/4 for bottom toolset.\n
		 Example:
		 
		::

			 class MyClass : public BaseClass{
			
			        void button();
			        void long_button();
			        void X();
			
			        SERIALIZE(){
			            ...
			            //places next 3 controls in one line: [button][long_button][X], length of [button] is twice less than [long_button], [X] has fixed width 32
			            UI_LAYOUT("1 2 [32]");
			            CLASS_METHOD_CALL(button);//[button]
			            CLASS_METHOD_CALL(long_button);//[long_button]
			            CLASS_METHOD_CALL(X);//[X]
			            ...
			        }
			 };
			 

		
		'''
		pass # cpp source

	@staticmethod
	def slider_int(var: cSInt):
		'''
			
		SLIDER(var,name,minvalue,maxvalue) to add integer/float slider in UI. Only float and int supported
		\hideinitializer
		
		Example:
		
		::

			class MyClass : public BaseClass{
			      *
			    int x;
			    float y;
			      *
			    SERIALIZE(){
			        ...
			        SLIDER(x,"X",0,10);
			        SLIDER(y,"Y",0.0,10.0);
			        ...
			    }
			};
			


		Args:
			var (cSInt): variable ref
		
		'''
		pass # cpp source

	@staticmethod
	def slider_float(var: cSFloat):
		pass # cpp source

	@staticmethod
	def file_path(var: cSString, file_mask: str):
		'''
			
		use FILEPATH(str, name, mask) to add file selection control in UI. Only cStr supported
		\hideinitializer
		
		Example:
		
		::

			class MyClass : public BaseClass{
			      cStr path;
			      SERIALIZE(){
			          FILEPATH(path,"FilePath","save:*.tif;*.tiff;*.exr;*.tga;*.bmp;*.png");
			      }
			};
			

		
		'''
		pass # cpp source

	@staticmethod
	def vector2D(vec: cPy.cTypes.cVec2):
		'''
			
		register cVec2
		
		'''
		pass # cpp source

	@staticmethod
	def Rect(rect: cPy.cTypes.Rct):
		'''
			
		register Rct
		
		'''
		pass # cpp source

	@staticmethod
	def vector3D(vec: cPy.cTypes.cVec3):
		'''
			
		register Vector3D
		
		'''
		pass # cpp source

	@staticmethod
	def vector4D(vec: cPy.cTypes.cVec4):
		'''
			
		register Vector4D
		
		'''
		pass # cpp source

	@staticmethod
	def icon(path: str):
		'''
			
		 Insert icon if control supports.
		
		'''
		pass # cpp source

	@staticmethod
	def checkbox_group(group_name: str):
		'''
			
		 specify group for checkbox.
		
		'''
		pass # cpp source

	@staticmethod
	def hotkey(combo: str):
		'''
			
		 assign default hotkey to the UI element, like HOTKEY("CTRL E")
		
		'''
		pass # cpp source

	@staticmethod
	def left_align():
		'''
			
		 force left-align to the control
		
		'''
		pass # cpp source

	@staticmethod
	def element_color(color: str):
		'''
			
		 the element color
		
		'''
		pass # cpp source

	@staticmethod
	def font_color(color: str):
		'''
			
		 the font color
		
		'''
		pass # cpp source

	@staticmethod
	def reg_opt(opt: str):
		pass # cpp source

	@staticmethod
	def reg_coord(x: float, y: float, z: float):
		'''
			
		Place 3 lines of code in correspondence with current coordinate system - Y-up or Z-up
		\hideinitializer

		Args:
			x (float): X - related item
			y (float): Y - related item
			z (float): Z - related item
		     *
		
		'''
		pass # cpp source



class cAction():
	'''
			
		
		
	'''

	Enabled: bool #: bool (T)  
	def __init__(self):
		pass # CPP source

	Implementation: any #: pybind11 :: object (T)  cSlot Before; 
	def ExecImplementation(self) -> bool:
		pass # cpp source

	def Run(self) -> bool:
		pass # cpp source

	def __call__(self):
		'''
			
		virtual bool RunChilds();
		
		'''
		pass # cpp source

	def HasEnabledChild(self) -> bool:
		'''
			
		cAction* GetChild(int child_id);
		
		'''
		pass # cpp source



class cExAction():
	_name: str #: std :: string (T)  
	_hint: str #: std :: string (T)  
	_extension: str #: std :: string (T)  
	_message: str #: std :: string (T)  
	def __init__(self, name: str, extension: str, message: str, hint: str = ""):
		pass # CPP source



class LinkedObjectBaseType():
	@staticmethod
	def registerObjectType(objectType: LinkedObjectBaseType):
		pass # cpp source

	TopologyLocked: bool #: bool (T)  
	def SetTopologyLocked(self, newValue: bool):
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def OnModifyTreeItem(self, Name: str, BW: any):
		pass # cpp source

	actions: list[cExAction] #: std :: vector<cExAction>(T)  
	def addAction(self, extension: str, name: str, message: str = "", hint: str = ""):
		pass # cpp source

	def clearActions(self):
		pass # cpp source

	objectType: str #: std :: string (T)  
	IconTexture: int #: int (T)  extension for file 
	def setIconTexture(self, textureID: int):
		pass # cpp source

	def setObjectType(self, object_type: str):
		pass # cpp source



class LinkedObject(BaseClass):

	@staticmethod
	def dynamic_cast(pObject : BaseClass)->LinkedObject:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a LinkedObject class or its descendant, and if so, returns the specified object, but of the LinkedObject type.
		'''
		pass # cpp source

	def getType(self) -> LinkedObjectBaseType:
		pass # cpp source

	idx: int #: int (T)  
	Scaling: float #: float (T)  
	TopologyLocked: bool #: bool (T)  
	objectPath: any #: comms :: cStr (T)  


class WindowsManager(BaseClass):

	@staticmethod
	def dynamic_cast(pObject : BaseClass)->WindowsManager:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a WindowsManager class or its descendant, and if so, returns the specified object, but of the WindowsManager type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self) -> any:
		pass # CPP source

	def OnInit(self):
		pass # cpp source

	def OnUpdate(self):
		pass # cpp source

	def OnClose(self):
		pass # cpp source

	def RenderWidgetToTexture(self, widgetName: str, width: int, height: int) -> int:
		pass # cpp source

	def GetTexturePixels(self, fboID: int) -> any:
		pass # cpp source

	def RequestTexturePixels(self, fboID: int):
		pass # cpp source

	def GetTexturePixels(self, fboID: int, img: any) -> bool:
		pass # cpp source

	def FreeTexturePixelsBuffer(self, fboID: int):
		pass # cpp source

	def IsTexturePixelsReady(self, fboID: int) -> bool:
		pass # cpp source

	def InjectMouseEvent(self, widgetName: str, msg: int, x: int, y: int, flags: int):
		pass # cpp source

	def InjectWheelEvent(self, widgetName: str, delta: int, x: int, y: int, flags: int):
		pass # cpp source

	def InjectKeyEvent(self, widgetName: str, msgId: int, keyCode: int, flags: int):
		pass # cpp source

	def GetEditableWidgetAt(self, widgetName: str, x: int, y: int) -> any:
		pass # cpp source

	def InjectWidgetValue(self, widgetName: str, x: int, y: int, valStr: str):
		pass # cpp source

	def SetBlockNativeInput(self, block: bool):
		pass # cpp source

	def GetFocusedTextWidget(self, widgetName: str) -> any:
		pass # cpp source

	def GetWidgetScreenRect(self, widgetName: str) -> any:
		pass # cpp source

	def OnUndockToQt(self, widgetName: str):
		pass # cpp source

	m_fboID: int #: int (T)  
	m_fboWidth: int #: int (T)  
	m_fboHeight: int #: int (T)  
	WM_LMB: bool #: bool (T)  
	WM_MMB: bool #: bool (T)  
	WM_RMB: bool #: bool (T)  


class cColorSelectorInterface():
	ShowAlpha: bool #: bool (T)  
	Red: float #: float (T)  
	Green: float #: float (T)  
	Blue: float #: float (T)  
	Alpha: float #: float (T)  
	def __init__(self):
		pass # CPP source

	def ShowModal(self) -> bool:
		pass # cpp source

	def IsActive(self) -> bool:
		pass # cpp source



class pyRequirement():
	initialized: bool = Coat_CPP.pyRequirement.initialized #: static bool (T)  
	_installed: bool #: bool (T)  
	_installing: bool #: bool (T)  
	module_name: str #: std :: string (T)  
	module_version: str #: std :: string (T)  
	def installing(self) -> bool:
		pass # cpp source

	def checkIfInstalled(self) -> bool:
		pass # cpp source

	installing_name: str = Coat_CPP.pyRequirement.installing_name #: static std :: string (T)  
	installing_id: int = Coat_CPP.pyRequirement.installing_id #: static int (T)  
	@staticmethod
	def install_all():
		pass # cpp source

	@staticmethod
	def Check(name: str, install: bool = True, show_progress: bool = False, ask: bool = False, on_finish: any = None) -> pyRequirement:
		pass # cpp source

	@staticmethod
	def GetRequirementInfo(name: str) -> pyRequirement:
		pass # cpp source

	@staticmethod
	def EnsurePipInstalled():
		pass # cpp source



class cExtension():
	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	extensionHandler: any #: cExtensionHandler * (T)  
	@staticmethod
	def Message(extension_name: str, message: str) -> bool:
		pass # cpp source

	@staticmethod
	def ProcessID() -> int:
		pass # cpp source

	@staticmethod
	def DebugPort() -> int:
		pass # cpp source

	@staticmethod
	def getCoatInstallForder() -> str:
		pass # cpp source

	def refresh_menu(self) -> bool:
		pass # cpp source

	def add_menu_item(self, MenuPath: str, MenuItem: str, inRoom: str = "", inSection: str = "", Command: str = "") -> bool:
		pass # cpp source

	def onStop(self):
		pass # cpp source

	def onStart(self):
		pass # cpp source

	def onRestart(self):
		pass # cpp source

	def menu_item(self, item_name: str, on_click: any) -> bool:
		pass # cpp source

	def getSourcePath(self) -> str:
		'''
			
		SourcePaoth
		
		'''
		pass # cpp source

	def onMessage(self, message: str):
		'''
			
		Call if another module sent message to this extension using cExtension.Message
		
		'''
		pass # cpp source

	def onExtendMenu(self):
		'''
			
		insert some menu items to main menu
		
		'''
		pass # cpp source

	def onBuildMainMenu(self):
		'''
			
		on build the main menu
		
		'''
		pass # cpp source

	def onStartup(self):
		'''
			
		Call on startup, right before tools initialisation.
		
		'''
		pass # cpp source

	def afterInit(self):
		'''
			
		Call it after tools, graphics and shaders initialisation.
		
		'''
		pass # cpp source

	def preprocess(self):
		'''
			
		Call it once per frame, before tools processing.
		
		'''
		pass # cpp source

	def prerender(self):
		'''
			
		Call it once per frame, before the rendering stage.
		
		'''
		pass # cpp source

	def postprocess(self):
		'''
			
		Call it once per frame, after tools processing.
		
		'''
		pass # cpp source

	def postrender(self):
		'''
			
		Call it once per frame, after the rendering stage.
		
		'''
		pass # cpp source

	def afterUI(self):
		'''
			
		Call it once per frame, after the ui rendering, before the topmost elements
		
		'''
		pass # cpp source

	def thumbnail(self):
		'''
			
		Call it once per frame to draw thumbnails.
		
		'''
		pass # cpp source

	def afterSettings(self):
		'''
			
		Call it once after settings loading.
		
		'''
		pass # cpp source

	def onNew(self):
		'''
			
		Call it as soon as user starts new scene.
		
		'''
		pass # cpp source

	def onKey(self):
		'''
			
		Call it as soon as user pressed the key, get the key value from Widgets::lastKey. Set it to 0 if the key captured and des not need to be propagated anymore.
		
		'''
		pass # cpp source

	def onDropFile(self):
		'''
			
		Call if file dropped using drag&drop, filename is in Widgets::LastDroppedFile. Set it empty if you acquired the file.
		
		'''
		pass # cpp source

	def onChangeTool(self):
		'''
			
		called when the current tool changes
		
		'''
		pass # cpp source

	def onChangeRoom(self):
		'''
			
		called when the current room changes
		
		'''
		pass # cpp source

	def onUndo(self):
		'''
			
		called when the undo triggered
		
		'''
		pass # cpp source

	def onRedo(self):
		'''
			
		called when the redo triggered
		
		'''
		pass # cpp source

	def onSaveScene(self):
		'''
			
		called before the saving the scene
		
		'''
		pass # cpp source

	def onExit(self):
		'''
			
		called before the exit
		
		'''
		pass # cpp source

	@staticmethod
	def begin_work_in_bg() -> int:
		pass # cpp source

	@staticmethod
	def end_work_in_bg() -> int:
		pass # cpp source



class cExtensionHandler(BaseClass):

	@staticmethod
	def dynamic_cast(pObject : BaseClass)->cExtensionHandler:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cExtensionHandler class or its descendant, and if so, returns the specified object, but of the cExtensionHandler type.
		'''
		pass # cpp source

	name: cPy.cTypes.cStr #: cStr (T)  
	uiname: cPy.cTypes.cStr #: cStr (T)  
	path: cPy.cTypes.cStr #: cStr (T)  
	mainModule: any #: cPyModule * (T)  
	onStartUpModule: any #: cPyModule * (T)  
	Loaded: bool #: bool (T)  
	NeedRestartApp: bool #: bool (T)  
	extension: cExtension #: cExtension * (T)  
	Started: bool #: bool (T)  
	Active: bool #: bool (T)  
	AutoStart: bool #: bool (T)  
	StartAfterInstalls: bool #: bool (T)  
	Error: bool #: bool (T)  
	ErrorMessage: cPy.cTypes.cStr #: cStr (T)  
	dependencies: any #: comms :: cStrs (T)  
	def Start(self):
		pass # cpp source

	def Stop(self):
		pass # cpp source

	def Restart(self):
		pass # cpp source

	def OnState(self, state: cPy.cTypes.cStr):
		pass # cpp source



class ExtensionManager(BaseClass):

	@staticmethod
	def dynamic_cast(pObject : BaseClass)->ExtensionManager:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a ExtensionManager class or its descendant, and if so, returns the specified object, but of the ExtensionManager type.
		'''
		pass # cpp source

	ProcessID: int = Coat_CPP.ExtensionManager.ProcessID #: static int (T)  
	DebugPort: int = Coat_CPP.ExtensionManager.DebugPort #: static int (T)  
	@staticmethod
	def AutoReloadModules() -> bool:
		pass # cpp source

	@staticmethod
	def OnExtensionState(state: cPy.cTypes.cStr):
		pass # cpp source

	@staticmethod
	def SetExtensionManager(extensionManager: ExtensionManager):
		pass # cpp source

	MainColorSelector: cColorSelectorInterface = Coat_CPP.ExtensionManager.MainColorSelector #: static cColorSelectorInterface * (T)  
	NeedRefreshPyInstalledModuleList: bool = Coat_CPP.ExtensionManager.NeedRefreshPyInstalledModuleList #: static bool (T)  
	def AddInstalledPyModule(self, module_name: str):
		pass # cpp source

	def ClearInstalledPyModuleList(self):
		pass # cpp source

	def __init__(self):
		pass # CPP source

	@staticmethod
	def CommandToPy(command: str) -> str:
		pass # cpp source

	def Command(self, command: str) -> bool:
		pass # cpp source

	@staticmethod
	def ExecScriptFromCPPStatic(script: str) -> bool:
		pass # cpp source

	def ExecScript(self, script: str) -> bool:
		pass # cpp source

	def ExecByIdx(self, action_idx: int) -> bool:
		pass # cpp source

	def Expression(self, source: str) -> str:
		pass # cpp source

	def OnImport(self, module: str):
		pass # cpp source

	def ImportModule(self, module: str) -> bool:
		pass # cpp source

	def Run(self, file_path: str):
		pass # cpp source

	def RunPy(self, file_path: str) -> bool:
		pass # cpp source

	@staticmethod
	def RunPyFromCPPStatic(file_path: str) -> bool:
		pass # cpp source

	def LoadExtensions(self, rootFolderPath: cPy.cTypes.cStr):
		pass # cpp source

	def Refresh(self):
		pass # cpp source

	def OnProcess(self):
		pass # cpp source

	def RefreshInstalledList(self):
		pass # cpp source

	def IsAnyMouseButtonDown(self) -> bool:
		pass # cpp source

	def IsLMBDown(self) -> bool:
		pass # cpp source

	def IsRMBDown(self) -> bool:
		pass # cpp source

	def IsMMBDown(self) -> bool:
		pass # cpp source

	@staticmethod
	def currentDateTime() -> str:
		pass # cpp source

	@staticmethod
	def Init():
		pass # cpp source

	def ReloadChangedModules(self):
		pass # cpp source

	@staticmethod
	def SetupVSCodeProject(aProjectFolder: cPy.cTypes.cStr, aModulesInit: bool, aLibRoot: bool):
		pass # cpp source

	@staticmethod
	def StringFromFile(aFileName: cPy.cTypes.cStr) -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def StringToFile(aSource: cPy.cTypes.cStr, aFileName: cPy.cTypes.cStr):
		pass # cpp source

	def FindExtension(self, extName: cPy.cTypes.cStr) -> cExtensionHandler:
		pass # cpp source



class ExtPhotogrammetryEngine():
	Registred: bool #: bool (T)  
	hasHowToInstall: bool #: bool (T)  
	hasAutoInstall: bool #: bool (T)  
	hasSetPathToEngine: bool #: bool (T)  
	def engineName(self) -> str:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def Register(self, setDefault: bool = False) -> bool:
		pass # cpp source

	def NeedAutoReconstruction(self) -> bool:
		pass # cpp source

	def ShotsTo3D(self):
		pass # cpp source

	def ImportProject(self):
		pass # cpp source

	def BakeUVTextures(self):
		pass # cpp source

	def VideoTo3D(self):
		pass # cpp source

	def HowToInstall(self):
		pass # cpp source

	def AutoInstall(self):
		pass # cpp source

	def SetPathToEngine(self):
		pass # cpp source

	def CheckIfInstalled(self) -> bool:
		pass # cpp source

