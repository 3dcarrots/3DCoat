from __future__ import annotations
import cPy.cTypes
import cPy.ClassArray
import cPy.cCore
import cPy.cModel
#cScene
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class VoxMethadata():
	'''
			
		Base class for voxel metadata extensions.
		
		Allows attaching additional data or logic to a specific VoxTreeBranch.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : any)->VoxMethadata:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a VoxMethadata class or its descendant, and if so, returns the specified object, but of the VoxMethadata type.
		'''
		pass # cpp source

	@staticmethod
	def ProcessMethadata():
		pass # cpp source

	@staticmethod
	def SetZeroCur():
		pass # cpp source

	Parent: any #: VoxTreeBranch * (T)  
	def OnActivateVolume(self, T: any):
		'''
			
		Called when the associated volume becomes active.
		
		'''
		pass # cpp source

	def OnDeactivateVolume(self, T: any):
		pass # cpp source



class CutsCollector():
	'''
			
		Utility class for collecting intersection curves and processing boolean edges.
		
		Used for operations like creating curves from volume intersections,
		generating tubes along intersections, or splitting mesh boundaries.
		
	'''

	edges: list #: cList<std :: pair<cVec3, cVec3>>(T)  
	preferred_name: cPy.cTypes.cStr #: cStr (T)  
	def transform(self, m: cPy.cTypes.cMat4):
		pass # cpp source

	def fromVolumesIntersection(self, volume1: any, volume2: any):
		'''
			
		Collects intersection edges between two voxel volumes.
		
		'''
		pass # cpp source

	def makeCurves(self):
		'''
			
		Collects intersection edges between a voxel volume and a mesh.
		
		'''
		pass # cpp source

	def relaxInTube(self, volume: any, radius: float, symm: bool = True):
		'''
			
		Relaxes the collected curves inside a tubular volume.
		
		'''
		pass # cpp source

	def createWeightsVolume(self, dest: cPy.cModel.VolumeObject, radius: float, edges_transform: cPy.cTypes.cMat4):
		pass # cpp source

	def mergeTubeTo(self, dest: any, radius: float):
		pass # cpp source



class VoxTreeBranch():
	'''
			
		Hierarchical layers (voxel and surface) which you see in the SculptRoom.
		
		Every item in this object contains transform matrix and reference to the item in `VTree`.
		It refers `VolumeObject`. There may be multiple references on same `VolumeObject` from separate `VoxTreeBranch`-es.
		Root of all `VoxTreeBranches` kept in `RootVTree`.
		\see VolumeObject
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	Parent: VoxTreeBranch #: VoxTreeBranch * (T)  
	Obj: cPy.cModel.VolumeObject #: VolumeObject * (T)  Pointer to the actual volumetric or surface data. 
	StoreMode: bool = Coat_CPP.VoxTreeBranch.StoreMode #: static bool (T)  cStr Name; ///< name in tree 
	Ghost: bool #: bool (T)  bool Visible; ///< visibility 
	pVoxSurf: bool #: bool (T)  < ghosting mode 
	VoxSurf: bool #: bool (T)  < was in surface mode on previous frame? 
	HideInViewport: bool #: bool (T)  < true if object is in Surface mode, false if in Voxel mode. 
	Procesed: bool #: bool (T)  < Hidden in viewport, but pickable/visible in tree. 
	IsRef: bool #: bool (T)  bool OpenState; ///< branch is open 
	IsActive: bool #: bool (T)  
	IsInTransform: bool #: bool (T)  
	ToDestroy: bool #: bool (T)  
	InCache: bool #: bool (T)  < should be destroyed. Don't delete leafs manually, just set this flag! 
	Instance: bool #: bool (T)  < is in cache 
	SkipPick: bool #: bool (T)  < is Instance. It does not mean that it was actually instanced. Current selected object is never instance! It gives instance flag to other non-current leaf. 
	Inverse: bool #: bool (T)  
	SelectionTime: int #: int (T)  bool Selected; 
	CacheName: cPy.cTypes.cStr #: cStr (T)  
	ExData: cPy.cTypes.cStr #: cStr (T)  < reference to cache name 
	SymmetryData: cPy.cTypes.cStr #: cStr (T)  < metadata string 
	SpaceID: int #: int (T)  < symmetry data kept to be stored in undo routine 
	ProxyScale: float #: float (T)  int Level; ///< deph in VoxTree structure 
	Transform: cPy.cTypes.cMat4 #: cMat4 (T)  
	InvTransform: cPy.cTypes.cMat4 #: cMat4 (T)  < transform for local to global scale 
	LocalTransform: cPy.cTypes.cMat4 #: cMat4 (T)  \todo ??? 
	GizmoCenter: cPy.cTypes.cVec3 #: cVec3 (T)  Last used transform gizmo parameters. 
	GizmoCenrtified: bool #: bool (T)  
	GizmoDirected: bool #: bool (T)  
	GizmoX: cPy.cTypes.cVec3 #: cVec3 (T)  
	GizmoY: cPy.cTypes.cVec3 #: cVec3 (T)  
	GizmoZ: cPy.cTypes.cVec3 #: cVec3 (T)  
	Methadata: any #: ClassPtr<VoxMethadata>(T)  
	LockedVolumeChanged: VoxTreeBranch = Coat_CPP.VoxTreeBranch.LockedVolumeChanged #: static VoxTreeBranch * (T)  
	tmpLinkedObjects: any #: ClassArray<LinkedObject>* (T)  
	def GetLinkedObjects(self) -> any:
		pass # cpp source

	SceneNGObjects: cPy.ClassArray.ClassArray_NGObject = Coat_CPP.VoxTreeBranch.SceneNGObjects #: static ClassArray_NGObject (T)  
	NGObjectIdx: int #: int (T)  
	def GetNodeSystem(self) -> any:
		pass # cpp source

	LastTransformTick: int #: int (T)  
	MergeDisplacement: float = Coat_CPP.VoxTreeBranch.MergeDisplacement #: static float (T)  
	def ChildObjects(self, i: int) -> VoxTreeBranch:
		'''
			
		ClassArray<VoxTreeBranch> ChildObjects;
		
		'''
		pass # cpp source

	def ChildObjectsCount(self) -> int:
		pass # cpp source

	def GetObjectsCountRecursive(self) -> int:
		pass # cpp source

	def ChildObjectsAdd(self, tb: VoxTreeBranch):
		pass # cpp source

	def ChildObjectsInsert(self, Pos: int, tb: VoxTreeBranch):
		pass # cpp source

	def ChildObjectsClear(self):
		pass # cpp source

	def ChildObjectsDel(self, idx: int, count: int):
		pass # cpp source

	def ChildObjectsDelElement(self, idx: int):
		pass # cpp source

	def TransformedRecently(self) -> bool:
		pass # cpp source

	def NotifyTransformed(self):
		pass # cpp source

	PrimPresets: any #: ClassArray<OnePreset>(T)  primitives usage history 
	def Delete(self):
		'''
			
		 \see Del()
		
		'''
		pass # cpp source

	def _Add(self):
		pass # cpp source

	def CreateRmbMenu(self, Prop: any):
		'''
			
		overrides from ItemsTree
		
		'''
		pass # cpp source

	def DropTreeStructureToUndo(self):
		pass # cpp source

	def OnDuplicate(self, CopyPtr: any):
		pass # cpp source

	def AdditionalElementRenderingInUI(self, BaseBox: any):
		pass # cpp source

	def IgnoreAltIsolate(self) -> bool:
		pass # cpp source

	def ApplyBooleans(self, Source: any, shift: bool, ctrl: bool, Keep: bool):
		pass # cpp source

	def ChangeParentItem(self, NewParent: any):
		pass # cpp source

	def NotifyParentChange(self, NewParent: any):
		pass # cpp source

	def ProcessItem(self):
		'''
			
		end of overrides from ItemsTree
		
		'''
		pass # cpp source

	def Add(self, T: cPy.cTypes.cMat4, Name: str, undo: bool = True, ToSubtree: bool = True) -> VoxTreeBranch:
		'''
			
		Adds a new child branch.

		Args:
			T (cMat4): Transform matrix.
			Name (str): Name of the new layer.
			undo (bool): If true, registers undo action.
			ToSubtree (bool): If true, adds to the current object's subtree.

		Returns:
			VoxTreeBranch: Pointer to the new branch.
		
		'''
		pass # cpp source

	def Add(self, name: str, CheckExisting: bool, T: cPy.cTypes.cMat4 = None) -> VoxTreeBranch:
		pass # cpp source

	def CheckPresenceInSubTree(self, Element: VoxTreeBranch) -> bool:
		'''
			
		Restores the child structure from a helper list.
		
		'''
		pass # cpp source

	def InstanceToParentInstances(self):
		pass # cpp source

	def Insert(self, idx: int):
		pass # cpp source

	def EditShader(self) -> bool:
		pass # cpp source

	def ApplyNodes(self) -> bool:
		pass # cpp source

	@staticmethod
	def CreateNewShader(BaseShader: str, NewShaderName: str = None, Activate: bool = True):
		pass # cpp source

	def Rename(self):
		pass # cpp source

	def _Save3B(self, subtree: any) -> bool:
		'''
			
		  IO & caching 
		
		'''
		pass # cpp source

	def Save3B(self, subtree: bool, name: str, sel: bool = False):
		'''
			
		Saves the volume data to a 3B file.
		
		'''
		pass # cpp source

	def _Merge3B(self) -> bool:
		pass # cpp source

	def Merge3B(self, name: str):
		'''
			
		Merges a 3B file into the scene.
		
		'''
		pass # cpp source

	def CheckInstanceRemoving(self):
		pass # cpp source

	def Add1(self) -> bool:
		pass # cpp source

	def Decompose(self):
		pass # cpp source

	def DecomposeFrozen(self):
		pass # cpp source

	def _Resample(self):
		pass # cpp source

	def Resample(self, scale: float, Q: int):
		'''
			
		Resamples the volume (changes resolution).
		
		'''
		pass # cpp source

	def TransformIt(self) -> bool:
		pass # cpp source

	def Del(self, onlythis: bool) -> bool:
		pass # cpp source

	def DelSelected(self) -> bool:
		pass # cpp source

	def DelNoUndo(self) -> bool:
		pass # cpp source

	@staticmethod
	def validate_cur():
		pass # cpp source

	def ImportPointsCloud(self) -> bool:
		'''
			
		  Import/Export 
		
		'''
		pass # cpp source

	def ImportModel(self) -> bool:
		pass # cpp source

	def ExportScene(self) -> bool:
		pass # cpp source

	def ExportObject(self) -> bool:
		pass # cpp source

	def ExportPatternForMerge(self, idx: any) -> bool:
		pass # cpp source

	def ExportPatternAsPen(self) -> bool:
		pass # cpp source

	def ExportCurveProfile(self) -> bool:
		pass # cpp source

	def Approve(self, p: any) -> VoxTreeBranch:
		'''
			
		  Merging & Geometry 
		
		'''
		pass # cpp source

	def Approve(self, p: VoxTreeBranch) -> VoxTreeBranch:
		pass # cpp source

	def CheckMultiselectionCancel(self) -> bool:
		pass # cpp source

	def GetSelHighlight(self) -> cPy.cTypes.cVec4:
		pass # cpp source

	def HighlightIt(self, IfPassive: bool):
		pass # cpp source

	def Highlighted(self) -> bool:
		pass # cpp source

	def MergeObj(self, p: VoxTreeBranch) -> bool:
		pass # cpp source

	def PlainMergeObj(self, p: VoxTreeBranch) -> bool:
		pass # cpp source

	def Flip(self, x: any, y: any, z: any):
		'''
			
		Flips the object along specified axes.
		
		'''
		pass # cpp source

	def FlipSel(self, x: any, y: any, z: any):
		pass # cpp source

	@staticmethod
	def ApplyTransformToInstances(M: cPy.cTypes.cMat4, vo: cPy.cModel.VolumeObject, InstOnly: bool = False, R: bool = False, applyNGScale: bool = True):
		pass # cpp source

	def CombineChildren(self):
		pass # cpp source

	def FlipNormals(self):
		pass # cpp source

	def MakeUniform(self):
		pass # cpp source

	def MakeUniform2(self):
		pass # cpp source

	def AllUniform(self):
		pass # cpp source

	def isUniform(self) -> bool:
		pass # cpp source

	def MoveObj(self, p: VoxTreeBranch, KeepSource: bool) -> bool:
		'''
			
		  Boolean Operations 
		
		'''
		pass # cpp source

	def PlainMoveObj(self, p: VoxTreeBranch) -> bool:
		pass # cpp source

	def SubObj(self, p: VoxTreeBranch, KeepSource: bool) -> bool:
		pass # cpp source

	def IntrsObj(self, p: VoxTreeBranch, KeepSource: bool) -> bool:
		pass # cpp source

	def RemIntrsObj(self, p: VoxTreeBranch) -> bool:
		pass # cpp source

	def SplitObj(self, p: VoxTreeBranch) -> bool:
		pass # cpp source

	def MakeHull(self) -> bool:
		'''
			
		  Hull & Repair 
		
		'''
		pass # cpp source

	def MakeHull2(self) -> bool:
		pass # cpp source

	def CloseHoles(self) -> bool:
		pass # cpp source

	def CloseTunnels(self) -> bool:
		pass # cpp source

	def Extrude(self) -> bool:
		pass # cpp source

	def SetDirty(self):
		pass # cpp source

	def SetVoxShader(self, obj: any, id: any) -> bool:
		pass # cpp source

	def ApplyAxialSymmetry(self) -> bool:
		pass # cpp source

	def ChangeParent(self, p: VoxTreeBranch) -> bool:
		pass # cpp source

	def ShowHideButThis(self):
		'''
			
		  Visibility & Ghosting 
		
		'''
		pass # cpp source

	def GhostButThis(self):
		pass # cpp source

	def UnghostWithSubtree(self):
		pass # cpp source

	def GhostWithSubtree(self):
		pass # cpp source

	def InvertGhostWithSubtree(self):
		pass # cpp source

	def InvertVisibleWithSubtree(self):
		pass # cpp source

	def BakeColorsThere(self):
		pass # cpp source

	def ShowAll(self) -> bool:
		pass # cpp source

	def ShowSubtree(self) -> bool:
		pass # cpp source

	def PutOnGroundEx(self, minvt: cPy.cTypes.cVec3, cm: cPy.cTypes.cVec3):
		'''
			
		  Positioning 
		
		'''
		pass # cpp source

	def PutOnGround(self):
		pass # cpp source

	def LayOnGround(self):
		pass # cpp source

	def GlueToGround(self):
		pass # cpp source

	def InvertHiddenFaces(self):
		pass # cpp source

	def DeleteHiddenFaces(self, invert: bool):
		pass # cpp source

	def CalcHash(self, d: int = 1) -> int:
		pass # cpp source

	@staticmethod
	def valid(tb: VoxTreeBranch) -> bool:
		pass # cpp source

	@staticmethod
	def valid(ctb: any) -> bool:
		pass # cpp source

	def GetRoot(self) -> VoxTreeBranch:
		pass # cpp source

	def DeselectAll(self, R: VoxTreeBranch = None) -> bool:
		pass # cpp source

	def StoreSymm(self):
		pass # cpp source

	def RestoreSymm(self):
		pass # cpp source

	def GetUniqueName(self, takethisname: bool, suffix: str) -> cPy.cTypes.cStr:
		pass # cpp source

	def CreateUniqSpace(self, safe: bool, suffix: str) -> VoxTreeBranch:
		pass # cpp source

	def Clone(self, Recursive: bool = False, dest: VoxTreeBranch = None, Inst: bool = False, Subtree: bool = False, T: cPy.cTypes.cMat4 = cPy.cTypes.cMat4.Identity, ChangeTool: bool = True, CopyData: bool = True, SetCurr: bool = True, ForceReplaceDest: bool = False, SelectedOnly: bool = False) -> VoxTreeBranch:
		'''
			
		Clones the object/branch.

		Args:
			Recursive (bool): Clone children recursively.
			dest (VoxTreeBranch): Destination branch (parent).
			Inst (bool): Create as an instance (share volume data).
			Subtree (bool): Include full subtree.
			T (cMat4): Optional transform offset.

		Returns:
			VoxTreeBranch: Pointer to the cloned branch.
		
		'''
		pass # cpp source

	def Clone2(self):
		pass # cpp source

	def CloneInst2(self):
		pass # cpp source

	def CloneDegrade(self, Undo: bool) -> bool:
		pass # cpp source

	def CloneAndDegradeCur(self):
		pass # cpp source

	def SeparateHidden(self):
		pass # cpp source

	def MergeVisible(self):
		pass # cpp source

	def PlainMergeVisible(self):
		pass # cpp source

	def MergeSelected(self):
		pass # cpp source

	def PlainMergeSelected(self):
		pass # cpp source

	def MergeSubtree(self):
		'''
			
			void MergeDown(); // implementation not found
		
		'''
		pass # cpp source

	def PlainMergeSubtree(self):
		pass # cpp source

	def MergeTo(self, Dest: VoxTreeBranch, sub: int, ClearThis: bool, NoUndo: bool):
		pass # cpp source

	def PlainMergeTo(self, Dest: VoxTreeBranch, NoUndo: bool):
		pass # cpp source

	def find(self, vo: cPy.cModel.VolumeObject) -> VoxTreeBranch:
		'''
			
		Merges a mesh into the voxel/surface volume.
		
		'''
		pass # cpp source

	def find(self, gu: int, NonInstance: bool = True) -> VoxTreeBranch:
		pass # cpp source

	def GetParent(self, tb: VoxTreeBranch) -> VoxTreeBranch:
		pass # cpp source

	def CloneSpaceVT(self, changetool: bool = True, subtree: bool = False) -> VoxTreeBranch:
		pass # cpp source

	@staticmethod
	def Current() -> VoxTreeBranch:
		pass # cpp source

	def SeekByUserInt(self, val: int) -> VoxTreeBranch:
		pass # cpp source

	def SetupNewNodeSystem(self):
		pass # cpp source

	def CloneSpace(self) -> bool:
		pass # cpp source

	def IncDencity2X(self) -> bool:
		pass # cpp source

	def DecDencity2X(self) -> bool:
		pass # cpp source

	def CloneSymm2(self):
		pass # cpp source

	def CloneInstSymm2(self):
		pass # cpp source

	def SelectCurrent(self):
		pass # cpp source

	def SelectCurrentOnScreen(self):
		pass # cpp source

	def SimpleSelect(self):
		pass # cpp source

	def QuadrangulateAndMergeDP(self) -> bool:
		'''
			
		  Retopology / Quadrangulation 
		
		'''
		pass # cpp source

	def DecToRetopo(self):
		pass # cpp source

	def DecToRetopoAll(self):
		pass # cpp source

	def PushMatrix(self):
		pass # cpp source

	def PopMatrix(self):
		pass # cpp source

	def UnIstance(self, copy: bool = True):
		pass # cpp source

	def SaveTransforms(self, name: str):
		pass # cpp source

	def LoadTransforms(self, name: str):
		pass # cpp source

	def BlendTransforms(self, name1: str, name2: str, blend: float):
		pass # cpp source

	def SaveTransforms(self):
		pass # cpp source

	def LoadTransforms(self):
		pass # cpp source

	def SetTransform(self, m: cPy.cTypes.cMat4):
		pass # cpp source

	@staticmethod
	def BestCurentCandidate() -> VoxTreeBranch:
		pass # cpp source

	def SelectVisibleSubtree(self):
		pass # cpp source

	def ChooseRefColor(self):
		pass # cpp source

	def TopologyLocked(self) -> bool:
		pass # cpp source

	def OnChangeMember(self, mc: cPy.cCore.BaseClass, mp: any, me: any, mn: str) -> bool:
		pass # cpp source

	def OnScriptRecorder(self, mc: cPy.cCore.BaseClass, mp: any, me: any, mn: str) -> bool:
		pass # cpp source

	def ApproveThis(self) -> bool:
		pass # cpp source

	def OnModifyControl(self, Name: str, BW: any, Context: any):
		pass # cpp source

	def RMBHotkeysActiveForThisItem(self) -> bool:
		pass # cpp source

	def GetClassMask(self) -> int:
		pass # cpp source

	def GetElementLevel(self, name: str) -> int:
		pass # cpp source

	def ProcessNodeCleanup(self):
		pass # cpp source

	def ProcessNodeVisibility(self, MakeInvisible: bool = False):
		pass # cpp source

	def UpdateHash(self, H: any, data: any = None, extra: any = None):
		pass # cpp source

	def IsNameUniq(self, name: str) -> bool:
		pass # cpp source

	def StoreVOTree(self, B: any, bin: bool):
		pass # cpp source

	def CheckIfParent(self, child: VoxTreeBranch) -> bool:
		pass # cpp source

	def FindParent(self, root: VoxTreeBranch, index: int) -> VoxTreeBranch:
		pass # cpp source

	def RefreshLevels(self):
		pass # cpp source

	def SetupLevels(self, L: int):
		pass # cpp source

	def SetupVOMat(self):
		pass # cpp source

	def RestoreVOTree(self, B: any, Clear: bool = True):
		pass # cpp source

	def SetDestroyState(self):
		pass # cpp source

	def SetVIDS(self):
		pass # cpp source

	def SetInvM(self):
		pass # cpp source

	def FindVOBS(self):
		pass # cpp source

	def GetMainAxis(self, X: cPy.cTypes.cVec3, Y: cPy.cTypes.cVec3, Z: cPy.cTypes.cVec3, SelectedOnly: bool) -> cPy.cTypes.cVec3:
		pass # cpp source

	def ScrollTo(self):
		pass # cpp source

	def CheckLockedVolume(self) -> bool:
		pass # cpp source

	def removeThis(self):
		pass # cpp source

	def duplicate(self) -> any:
		pass # cpp source

	def setTransform(self, m: cPy.cTypes.cMat4):
		pass # cpp source

	def setTransformRecursive(self, m: cPy.cTypes.cMat4):
		pass # cpp source

	def duplicateAsInstance(self) -> any:
		pass # cpp source

	def instancingSupported(self) -> bool:
		pass # cpp source

	def getTransform(self) -> cPy.cTypes.cMat4:
		pass # cpp source

	def SemiBoolean(self, other: VoxTreeBranch, op_type: int):
		pass # cpp source

	@staticmethod
	def ApplySurfaceChangesToVoxelsVolumes():
		'''
			
			static float GetCut(cVec2& minmax, const Vector3D& p, VolumeObject* except, float* unitlen); // implementation not found
		
		'''
		pass # cpp source

	def createIntersectionCurveWith(self, with_vtb: VoxTreeBranch):
		pass # cpp source



class HullParams(cPy.cCore.BaseClass):
	def __init__(self):
		pass # CPP source

	EdgeThickness: float #: float (T)  


class VoxVisualTree(VoxTreeBranch):
	'''
			
		The root class representing the visual object tree structure.
		
		Manages global tree operations like adding new volumes, deleting selected, and cloning spaces.
		
	'''

	def __init__(self):
		pass # CPP source

	def AddNewVolume(self):
		pass # cpp source

	def DeleteSelectedVolumes(self):
		pass # cpp source

	def DuplicateSelectedVolumes(self):
		pass # cpp source

	def CloneSpaceDencity(self):
		pass # cpp source

	def SymmCopy(self):
		pass # cpp source

	def EditShader(self):
		pass # cpp source

	def IncRes(self):
		pass # cpp source

	def ClearCurrLayer(self):
		pass # cpp source

