from __future__ import annotations
import cPy.cTypes
import cPy.cList
import cPy.cCore
#cModel
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class JType(Enum):
	'''
			
		Flags and types for snapping joints.
		
	'''
	AxialMask = Coat_CPP.JType.AxialMask.value
	Vertical = Coat_CPP.JType.Vertical.value
	Horizontal = Coat_CPP.JType.Horizontal.value
	Free = Coat_CPP.JType.Free.value
	Tile = Coat_CPP.JType.Tile.value
	TypeMask = Coat_CPP.JType.TypeMask.value
	Type1 = Coat_CPP.JType.Type1.value
	Type2 = Coat_CPP.JType.Type2.value
	Type3 = Coat_CPP.JType.Type3.value
	Type4 = Coat_CPP.JType.Type4.value
	IsConnector = Coat_CPP.JType.IsConnector.value
	IsPlug = Coat_CPP.JType.IsPlug.value
	KeepDirection = Coat_CPP.JType.KeepDirection.value
	ManualRotate = Coat_CPP.JType.ManualRotate.value
	AutoFlipX = Coat_CPP.JType.AutoFlipX.value
	AutoFlipY = Coat_CPP.JType.AutoFlipY.value
	AutoFlipZ = Coat_CPP.JType.AutoFlipZ.value


class VolMarker():
	'''
			
		mark pints in space, used for inter-volume segmental selection
		
	'''

	def __init__(self):
		pass # CPP source

	Empty: bool #: bool (T)  
	Activated: bool #: bool (T)  
	T: cPy.cTypes.cMat4 #: cMat4 (T)  
	Ti: cPy.cTypes.cMat4 #: cMat4 (T)  
	Initial: any #: VolumeObject * (T)  
	def Clear(self):
		pass # cpp source

	def Check(self, pos: cPy.cTypes.cVec3) -> bool:
		pass # cpp source

	def Mark(self, pos: cPy.cTypes.cVec3):
		pass # cpp source

	def SetupMatrix(self, src: any):
		pass # cpp source



class ABOcTree():
	'''
			
		Axis-Aligned Box Octree for fast spatial lookups of volume cells.
		
	'''

	def __init__(self):
		pass # CPP source

	Depth: int #: int (T)  
	Levels: any #: ClassArray<ABOcTreeLevel>(T)  
	def Update(self, VO: any):
		pass # cpp source

	def AddDirtyCell(self, Level: int, tz: any, AB: any):
		pass # cpp source

	def Clear(self):
		pass # cpp source



class SpOcTree():
	'''
			
		Spatial Octree implementation for raycasting.
		
	'''

	def __init__(self):
		pass # CPP source

	L0: any #: SpOcTreeLevel (T)  
	Center: cPy.cTypes.cVec3 #: cVec3 (T)  
	Side: float #: float (T)  
	NeedFreeze: bool #: bool (T)  
	Root: any #: CellElmABNode (T)  
	Temp: any #: BigDynArray<CellElmAB>(T)  
	def AddCell(self, vo: any, vc: any):
		pass # cpp source

	def AddSmoothedVO(self, vo: any):
		pass # cpp source

	def Create(self, Smoothed: bool = True, Anyway: bool = False):
		pass # cpp source

	def Clear(self):
		'''
			
		void CreateForVO(VORenderQueue& RQ);
		
		'''
		pass # cpp source

	def PrepareToScan(self):
		pass # cpp source

	def Scan(self, Start: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Len: float, res: any) -> bool:
		pass # cpp source

	@staticmethod
	def ScanAll(Start: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Len: float, res: any, Sharp: bool = True) -> bool:
		pass # cpp source

	@staticmethod
	def CreateAll(Smoothed: bool = True):
		pass # cpp source

	@staticmethod
	def CreateVO(VO: any):
		pass # cpp source

	@staticmethod
	def RestoreAll():
		pass # cpp source

	@staticmethod
	def ClearAll():
		pass # cpp source



class VolumeColorizer():
	'''
			
		Helper class to handle volumetric color rendering and layer management.
		
	'''

	cells: any #: cList<cell *>(T)  
	SingleLayer: int #: int (T)  
	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def AddCell(self, vc: any):
		pass # cpp source

	def RenderToVolume(self, vo: any, MT: cPy.cTypes.cMat4):
		pass # cpp source

	@staticmethod
	def RenderAllVolumes(Layer: int):
		pass # cpp source

	@staticmethod
	def GetColorDebt(vo: any, L: int) -> any:
		pass # cpp source

	@staticmethod
	def FinishColorDebts():
		pass # cpp source



class VolumeObject(cPy.cCore.BaseClass):
	'''
			
		One layer without hierarchy in the SculptRoom.
		
		Represents volume object. Volume object may be in volume or surface
		representations depends on bool `InSurfaceRepresentation()`.
		In volume mode voxels are modified and then mesh is generated.
		In surface mode mesh is modified then voxels are generated.
		The transform matrix of volume corresponds to latest selected instance in `VoxTree`.
		There may be multiple references from `VoxTree` to the same `VolumeObject`.
		\n
		`VolumeObject` is voxel/surface object not placed in tree. `VoxTreeBranch` is the object reference.
		All active `VoxelObject`'s are kept as linear set in `VTree` array.
		`RootVTree` consists of hiererchial set of references of objects from this array.
		Each `VolumeObject` contains complete information about geometry in local space.
		Correct transform matrices are kept in `VoxTreeBranch` that refers this `VolumeObject`.
		Transform matrices in `VolumeObject` correspond to non-instanced `VoxTree` element.
		If object is instance transform matrix in `VolumeObject` is
		different form `VoxTreeBranch` transform.
		
		\see VoxTreeBranch
		
	'''

	linkedToRetopoObj: bool #: bool (T)  
	topologyLockedByLinkedObject: bool #: bool (T)  
	SpaceID: int #: int (T)  Unique ID of the volume, same as `VoxTreeBranch::SpaceID`. 
	LoadTimeSpaceID: int #: int (T)  
	SpaceName: cPy.cTypes.cStr #: cStr (T)  
	CacheName: cPy.cTypes.cStr #: cStr (T)  Cache reference. 
	Ghost: bool #: bool (T)  
	def cache(self) -> str:
		pass # cpp source

	boolean_root: any #: VoxTreeBranch * (T)  
	def GetGlobalSummaryCut(self, p: cPy.cTypes.cVec3, root: any = None) -> float:
		pass # cpp source

	def GetSummaryCutExcept(self, p: cPy.cTypes.cVec3, except_vo: VolumeObject, root: any = None, density: float = None) -> cPy.cTypes.cVec3:
		pass # cpp source

	CuttingOperation: int #: int (T)  0 - none, 1 - subtract, 2 - intersect, 3 - add 
	FlipFaces: bool #: bool (T)  
	BooleansDisabled: bool #: bool (T)  
	Subd: any #: ClassArray<SubdLevelRef>(T)  
	CurrentSubdLevel: int #: int (T)  
	def DestroySubdLevels(self) -> bool:
		pass # cpp source

	volumetricalGettter: any #: >(T)  
	linkedObjects: any #: ClassArray<LinkedObject>(T)  
	NGObjectIdx: int #: int (T)  
	AverageEdgeLengthInPen: float = Coat_CPP.VolumeObject.AverageEdgeLengthInPen #: static float (T)  
	BackBufferTextureID: int = Coat_CPP.VolumeObject.BackBufferTextureID #: static int (T)  
	BackBufferDepthID: int = Coat_CPP.VolumeObject.BackBufferDepthID #: static int (T)  
	BBSizeX: int = Coat_CPP.VolumeObject.BBSizeX #: static int (T)  
	BBSizeY: int = Coat_CPP.VolumeObject.BBSizeY #: static int (T)  
	RenderStamp: any = Coat_CPP.VolumeObject.RenderStamp #: static WORD (T)  static int VoxThreshold; // without implementation 
	LightColor: cPy.cTypes.cVec4 = Coat_CPP.VolumeObject.LightColor #: static cVec4 (T)  
	LightScatter: float = Coat_CPP.VolumeObject.LightScatter #: static float (T)  
	GloballyAllowVoxelColoring: bool = Coat_CPP.VolumeObject.GloballyAllowVoxelColoring #: static bool (T)  
	GloballyIntentVoxelColoring: bool = Coat_CPP.VolumeObject.GloballyIntentVoxelColoring #: static bool (T)  
	LightColor2: cPy.cTypes.cVec4 = Coat_CPP.VolumeObject.LightColor2 #: static cVec4 (T)  `111` for external light, `rgb` for panorama. 
	IsExternalLight: float = Coat_CPP.VolumeObject.IsExternalLight #: static float (T)  `1` for external light, `0` for panorama. 
	AllowBB: bool = Coat_CPP.VolumeObject.AllowBB #: static bool (T)  
	WholeDirty: bool = Coat_CPP.VolumeObject.WholeDirty #: static bool (T)  
	Incremental: bool = Coat_CPP.VolumeObject.Incremental #: static bool (T)  
	AllowProgress: bool = Coat_CPP.VolumeObject.AllowProgress #: static bool (T)  
	IgnoreDropUndo: bool = Coat_CPP.VolumeObject.IgnoreDropUndo #: static bool (T)  
	NoVoxMerge: bool = Coat_CPP.VolumeObject.NoVoxMerge #: static bool (T)  
	InvisibleMode: bool = Coat_CPP.VolumeObject.InvisibleMode #: static bool (T)  
	GlobalSortTriangles: bool = Coat_CPP.VolumeObject.GlobalSortTriangles #: static bool (T)  
	@staticmethod
	def SetCur(tb: any, Fast: bool = False, keepsym: bool = False, flash: bool = True):
		pass # cpp source

	@staticmethod
	def WarnIfSurface(HasCancel: bool) -> bool:
		pass # cpp source

	OldColor: any #: BakedLayersStorage * (T)  Color to be restored when volume will be turned back to surface mode. 
	ScaleChange: float #: float (T)  How scale is changed when passed to proxy mode. 
	VolumeExtrusion: float #: float (T)  
	bkCells: any #: BigDynArray<tri_DWORD>(T)  
	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	VoxOcTree: ABOcTree #: ABOcTree (T)  Represents `OcTree` structure for fast finding of volume cells. 
	LocalAABB: any #: AABoundBox (T)  
	PickFarPlane: float #: float (T)  < AABB in local space 
	PickNearPlane: float #: float (T)  < far plane position in picked radius 
	PickAvgPlane: float #: float (T)  < closest plane position in picked radius 
	PickPlane: float #: float (T)  < average plane position in picked radius 
	PickListDirty: int #: int (T)  < plane position of picked center 
	LastDrawn: any #: AABoundBox (T)  
	Border: int #: int (T)  < last drawn bound box of cells centers in local space 
	MinCell: any #: cVec3i (T)  < border for dencity falloff in voxel objects, usually is 4 
	MaxCell: any #: cVec3i (T)  < min for bound box of cell indices, x,y,z 
	Transform: cPy.cTypes.cMat4 #: cMat4 (T)  < max for bound box of cell indices, x,y,z 
	TransformInv: cPy.cTypes.cMat4 #: cMat4 (T)  < transform from local to global space 
	Visible: bool #: bool (T)  < transform from global to local space 
	InCache: bool #: bool (T)  < better refer visibility from VoxTreeBranch 
	SurfaceColorChanged: bool #: bool (T)  < is in cache state 
	RawObjTris: int #: int (T)  
	RawInSurfaceRepresentation: int #: int (T)  
	CurCacheMethod: int #: int (T)  
	LastPolycount: int #: int (T)  
	ScaleFactor: float #: float (T)  
	Environment: VolumeObject #: VolumeObject * (T)  < scale factor, it is like simplified transform from local to global space. If you need to get some distance approx in local space, divide it on ScaleFactor 
	HiddenVolume: VolumeObject #: VolumeObject * (T)  
	IdxAllocator: any #: MeshHelper (T)  Allows to allocate / free global indices for mesh represented by `MeshInVCell`. 
	TempRef: VolumeObject #: VolumeObject * (T)  
	CellsChanged: bool #: bool (T)  
	HasLeakyPos: bool #: bool (T)  
	CompletelyRebuilt: bool #: bool (T)  
	HasTransparency: bool #: bool (T)  < this is for undo, it indicates that structure of volume changed drastically, almost no correstondence between old and new 
	RenderJustFacture: bool #: bool (T)  < for render - nood to sort triangles or not 
	SomethingNewSelected: bool = Coat_CPP.VolumeObject.SomethingNewSelected #: static bool (T)  
	Joints: any #: cList<SnapJoint>(T)  Joints of all merged objects 
	BackupJoints: any #: cList<SnapJoint>(T)  
	def AddJoint(self, J: any, GlobalTransform: cPy.cTypes.cMat4):
		'''
			
		Add joint to volume, GlobalTransform is transform matrix for model in world space
		
		'''
		pass # cpp source

	def AddAllJoints(self):
		'''
			
		Add all joints registered in VoxelSculptTool
		
		'''
		pass # cpp source

	Color: int #: DWORD (T)  
	ApproxColor: int #: DWORD (T)  
	ApproxSpec: int #: DWORD (T)  < bot baking of approximate shader color 
	ApproxMet: int #: int (T)  
	Est: any #: ShaderEstimator * (T)  
	PbrEst: any #: PbrEstimator * (T)  < estimate hader approximately 
	Shader: any #: VoxShaderParams (T)  
	def SetTransform(self, M: cPy.cTypes.cMat4, symm: bool):
		pass # cpp source

	def TransformPt(self, P: cPy.cTypes.cVec3):
		pass # cpp source

	def TransformScalar(self, P: float):
		pass # cpp source

	def TransformVec(self, P: cPy.cTypes.cVec3):
		pass # cpp source

	def TransformNrm(self, P: cPy.cTypes.cVec3):
		pass # cpp source

	def TransformPtInv(self, P: cPy.cTypes.cVec3):
		pass # cpp source

	def TransformVecInv(self, P: cPy.cTypes.cVec3):
		pass # cpp source

	def TransformNrmInv(self, P: cPy.cTypes.cVec3):
		pass # cpp source

	def TransformScalarInv(self, P: float):
		pass # cpp source

	def CheckIfUseCUDA(self, Radius: float) -> bool:
		pass # cpp source

	def GenerateCavity(self):
		pass # cpp source

	def GenerateCavity2(self):
		pass # cpp source

	def DiscardCavity(self):
		pass # cpp source

	def GetCavity(self, gid: int) -> float:
		pass # cpp source

	def UsesLayer(self, L: int) -> bool:
		pass # cpp source

	def FlipNormals(self):
		pass # cpp source

	LastWorkPoint: cPy.cTypes.cVec3 #: cVec3 (T)  
	SubCellSize: int #: int (T)  
	DefCellSize: int #: int (T)  
	DefCellShift: int #: int (T)  
	NumBackups: int #: int (T)  
	SurfaceChanged: bool #: bool (T)  
	NeedOcTreeRefine: bool #: bool (T)  
	SimpleStampMode: bool #: bool (T)  
	HideMode: bool #: bool (T)  
	InSurfaceRepresentation: bool #: bool (T)  
	RenderOrder: any #: cList<MCMeshInCell *>(T)  
	OrderDir: cPy.cTypes.cVec3 #: cVec3 (T)  
	def GetCell(self, x: int, y: int, z: int, Create: bool, CreateBackup: bool = False, Multithreaded: bool = True) -> any:
		'''
			
		Gets or creates a VolumeCell at specific coordinates.
		
		'''
		pass # cpp source

	def GetCell(self, t: any, Create: bool, CreateBackup: bool = False, Multithreaded: bool = True) -> any:
		pass # cpp source

	def GetBackup(self, x: int, y: int, z: int) -> any:
		pass # cpp source

	def CreateBackup(self, x: int, y: int, z: int) -> any:
		pass # cpp source

	def MoveToBackup(self, x: int, y: int, z: int) -> any:
		pass # cpp source

	def DetachModifiers(self):
		pass # cpp source

	def ClearBackups(self):
		pass # cpp source

	def CreateCellsNearCells(self):
		pass # cpp source

	def Clear(self, KeepCache: bool = False):
		pass # cpp source

	def ClearWithUndo(self):
		pass # cpp source

	@staticmethod
	def ClearLeakyPos():
		pass # cpp source

	def RestoreColors(self):
		pass # cpp source

	def TotalSmooth(self, Times: int = 1):
		pass # cpp source

	def DeleteCell(self, x: int, y: int, z: int):
		pass # cpp source

	def CalcCellsAABB(self):
		pass # cpp source

	def CalcCellsAABBTransformed(self, by_tree: bool = True) -> any:
		pass # cpp source

	def EstimateObjectColor(self):
		pass # cpp source

	def CreateEstimateStructures(self):
		pass # cpp source

	def ClearEstimateStructures(self):
		pass # cpp source

	@staticmethod
	def ClearAllEstimateStructures():
		pass # cpp source

	def GetObjectColor(self, pos: cPy.cTypes.cVec3, Specular: int, spop: int, met: int, Normal: cPy.cTypes.cVec3, srs: any = None, Cavity: float = 0, PixSize: float = 0) -> cPy.cTypes.cVec4:
		pass # cpp source

	@staticmethod
	def EstimateAllObjectsColor():
		pass # cpp source

	def EnsureHiddenVolumeExists(self):
		pass # cpp source

	def GetAverageVoxelNormalInSphere(self, Center: cPy.cTypes.cVec3, Radius: float) -> cPy.cTypes.cVec3:
		'''
			
		Create shape in volume using getter and StartPoint recursively. All points are in local space
		
		'''
		pass # cpp source

	def GetAverageVoxelNormalAndPosInSphere(self, Center: cPy.cTypes.cVec3, Radius: float, nrmSampling: float = 1.0, posSampling: float = 1.0, FromBackup: bool = True, Preferred: cPy.cTypes.cVec3 = cPy.cTypes.cVec3.Zero) -> cPy.cTypes.cVec3:
		pass # cpp source

	def UpdateVixelNormalsInLocalTrajectory(self, pts: any):
		pass # cpp source

	def UpdateVixelNormalsAndAveragePositionsInLocalTrajectory(self, pts: any):
		pass # cpp source

	def CreateFuncShapeCUDA(self, fn: any, Pos: cPy.cTypes.cVec3, Where: any, Subtract: int, Additive: bool = False, ComplexCheck: bool = False, UseTemp: bool = False, Extrusion: int = 0):
		'''
			
		Creates the arbitrary volxels shape

		Args:
			fn : the callback that defines the shape. Gets position of the point returns the value 0..1 to be set as voxel value
			Subtract (int): Subtract = 0: add, 1:subtract, 255: replace
			UseTemp (bool): set true if you want modify the cell afterward, all passed values will be kept in temp location and placed into the cell after the whole operation will be completed.
		
		'''
		pass # cpp source

	def CreateFuncShapeWeighted(self, fn: any, Pos: cPy.cTypes.cVec3, Where: any, Subtract: bool, Additive: bool = False):
		pass # cpp source

	def ApplySurfChange(self, fn: any, Pos: cPy.cTypes.cVec3, Where: any, Reader: any = None, SmDeg: float = 0):
		pass # cpp source

	def ApplySurfChange(self, fn: any, Pos: cPy.cTypes.cVec3, Where: any, Reader: any = None, SmDeg: float = 0):
		pass # cpp source

	def CreateSphere(self, Pos: cPy.cTypes.cVec3, Radius: float, Subtract: bool, Additive: bool = False):
		pass # cpp source

	def CreateSphereSegment(self, Start: cPy.cTypes.cVec3, End: cPy.cTypes.cVec3, RadiusS: float, RadiusE: float, Subtract: int, Additive: bool = False):
		pass # cpp source

	def CopySphereSegment(self, Start: cPy.cTypes.cVec3, End: cPy.cTypes.cVec3, RadiusS: float, RadiusE: float):
		pass # cpp source

	def TransferCells(self, x: int, y: int, z: int) -> any:
		pass # cpp source

	def TransferSphereSegment(self, Dest: VolumeObject, Start: cPy.cTypes.cVec3, End: cPy.cTypes.cVec3, RadiusS: float, RadiusE: float):
		pass # cpp source

	def TransferSphereSegmentSymm(self, Hide: bool, Start: cPy.cTypes.cVec3, End: cPy.cTypes.cVec3, RadiusS: float, RadiusE: float):
		pass # cpp source

	def CreateSphereSegmentSymm(self, Start: cPy.cTypes.cVec3, End: cPy.cTypes.cVec3, RadiusS: float, RadiusE: float, Subtract: int, Additive: bool = False):
		pass # cpp source

	def CopySphereSegmentSymm(self, Start: cPy.cTypes.cVec3, End: cPy.cTypes.cVec3, RadiusS: float, RadiusE: float, Subtract: bool):
		pass # cpp source

	def CreateSegment(self, Start: cPy.cTypes.cVec3, NS: cPy.cTypes.cVec3, AspectS: float, End: cPy.cTypes.cVec3, NE: cPy.cTypes.cVec3, AspectE: float, R1: float, R2: float, ExtraLayerWidth: float, Subtract: bool):
		pass # cpp source

	def CreateSegmentSymm(self, Start: cPy.cTypes.cVec3, NS: cPy.cTypes.cVec3, AspectS: float, End: cPy.cTypes.cVec3, NE: cPy.cTypes.cVec3, AspectE: float, R1: float, R2: float, ExtraLayerWidth: float, Subtract: bool, DoubleSided: bool = False, PlaneLimit: bool = False):
		'''
			
			void CreateLimSegment(Vector3D Start,Vector3D NS,float AspectS,Vector3D End,Vector3D NE,float AspectE,float R1,float R2,cPlane PL,float ExtraLayerWidth,bool Subtract); // implementation not found
		
		'''
		pass # cpp source

	def PerformSmoothing(self, Pos: cPy.cTypes.cVec3, Radius: float, AddValue: float = 0, AddMode: int = 0):
		'''
			
			void CreateLimSegmentSymm(Vector3D Start,Vector3D NS,float AspectS,Vector3D End,Vector3D NE,float AspectE,float R1,float R2,cPlane PL,float ExtraLayerWidth,bool Subtract,bool DoubleSided=false); // implementation not found
		
		'''
		pass # cpp source

	def PerformSmoothingCUDA(self, Pos: cPy.cTypes.cVec3, Radius: float, AddValue: float = 0, AddMode: int = 0):
		pass # cpp source

	def PerformSmoothingSymm(self, Pos: cPy.cTypes.cVec3, Radius: float, AddValue: float = 0, AddMode: int = 0):
		pass # cpp source

	def PerformPinchVox(self, Pos1: cPy.cTypes.cVec3, Radius1: float, N1: cPy.cTypes.cVec3, Pos2: cPy.cTypes.cVec3, Radius2: float, N2: cPy.cTypes.cVec3, Degree: float, Shift: cPy.cTypes.cVec3):
		pass # cpp source

	def PerformPinchVoxSymm(self, Pos1: cPy.cTypes.cVec3, Radius1: float, N1: cPy.cTypes.cVec3, Pos2: cPy.cTypes.cVec3, Radius2: float, N2: cPy.cTypes.cVec3, Degree: float, Shift: cPy.cTypes.cVec3):
		pass # cpp source

	def GrowSurface(self, Start: cPy.cTypes.cVec3, NStart: cPy.cTypes.cVec3, StartD: float, End: cPy.cTypes.cVec3, NEnd: cPy.cTypes.cVec3, EndD: float, R1: float, R2: float, Subtract: bool, UsePen: bool, UseTemp: bool):
		pass # cpp source

	def GrowSurfaceSymm(self, Start: cPy.cTypes.cVec3, NStart: cPy.cTypes.cVec3, StartD: float, End: cPy.cTypes.cVec3, NEnd: cPy.cTypes.cVec3, EndD: float, R1: float, R2: float, Subtract: bool, UsePen: bool, UseTemp: bool):
		pass # cpp source

	def ApplyPlane(self, Start: cPy.cTypes.cVec3, N: cPy.cTypes.cVec3, Radius: float, disp: float):
		pass # cpp source

	def ApplyPlaneSymm(self, Start: cPy.cTypes.cVec3, N: cPy.cTypes.cVec3, Radius: float, disp: float):
		pass # cpp source

	def AddCellTriangulation(self, cx: int, cy: int, cz: int) -> any:
		'''
			
			void DrawPressStroke(Vector3D Start,Vector3D End,Vector3D NStart,Vector3D NEnd,float R1,float R2,float Pressure,bool Subtract); // implementation not found
		
		'''
		pass # cpp source

	def AddCellTriangulation2(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def AddGlobalCellQuads(self, cx: int, cy: int, cz: int, vc: any, TC: any):
		pass # cpp source

	def AddGlobalCellTriangulation(self, cx: int, cy: int, cz: int, vc: any, TC: any, M: cPy.cTypes.cMat4):
		pass # cpp source

	def AddGlobalCellTriangulation3(self, cx: int, cy: int, cz: int, vc: any, TC: any, M: cPy.cTypes.cMat4):
		pass # cpp source

	def AddIndexedCellTriangulation(self, cx: int, cy: int, cz: int) -> any:
		'''
			
			void AddGlobalCellTriangulationG(int cx, int cy, int cz, VolumeCell* vc, TriangulationContext* TC, const Matrix4D& M, cList_int * CellPos = NULL); // implementation not found
		
		'''
		pass # cpp source

	def AddIndexedCellTriangulation2(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def CreateFuncShapeInCell(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def CreateFuncShapeInCellW(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def CreateFuncShapeInCellUsingTemp(self, x: int, y: int, z: int) -> any:
		pass # cpp source

	def MakeSmoothingInCell(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def MakeSmoothingInCell3(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def MakeSmoothingInCell2(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def MakePinchInCell(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def GrowDensityInCell2(self, cx: int, cy: int, cz: int) -> any:
		'''
			
			VolumeCell* GrowSurfaceInCell(int cx,int cy,int cz); // implementation not found
		
		'''
		pass # cpp source

	def GrowDensityInCell(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def CutHullInCell(self, cx: int, cy: int, cz: int) -> any:
		pass # cpp source

	def ClearAllTemp(self):
		pass # cpp source

	@staticmethod
	def ClearAllTempForAll():
		pass # cpp source

	def MarkDirtyCell(self, cx: int, cy: int, cz: int, onlymesh: bool = False, MultiThread: bool = False):
		pass # cpp source

	def GetInterpValueThrough(self, Pos: cPy.cTypes.cVec3, Backup: bool = False) -> float:
		pass # cpp source

	def GetVolumetricValue(self, Pos: cPy.cTypes.cVec3) -> float:
		pass # cpp source

	def GetCutByParents(self, Pos: cPy.cTypes.cVec3, max_density: float = None, except_vo: VolumeObject = None) -> float:
		pass # cpp source

	def GetSummaryCut(self, Pos: cPy.cTypes.cVec3, max_density: float = None, except_vo: VolumeObject = None) -> float:
		pass # cpp source

	def GetInterpLSumm(self, dst: any, pos: cPy.cTypes.cVec3, con: any, TempStorage: any):
		'''
			
			static float GetCut(Vector3D Pos, float* max_density, VolumeObject* except); // implementation not found
		
		'''
		pass # cpp source

	def GetFastNormal(self, p: cPy.cTypes.cVec3, normalize: bool = True) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetInterpNormalThrough(self, Pos: cPy.cTypes.cVec3, dst: float) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetInterpColorThrough(self, Pos: cPy.cTypes.cVec3, Specular: int = None, me: int = None, Normal: cPy.cTypes.cVec3 = None, srs: any = None) -> int:
		pass # cpp source

	def GetInterpColorThroughLayered(self, Pos: cPy.cTypes.cVec3, Info: any, N1: cPy.cTypes.cVec3, srs: any = None, PixSize: float = 0):
		pass # cpp source

	def GetOcclusionThrough(self, Pos: cPy.cTypes.cVec3, dst: float) -> float:
		pass # cpp source

	def GetCavity(self, Pos: cPy.cTypes.cVec3, dst: float) -> float:
		pass # cpp source

	def GetInterpNormalSmThrough(self, Pos: cPy.cTypes.cVec3, dst: float) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetInterpEdgeValue(self, Pos: cPy.cTypes.cVec3, Cash: any) -> float:
		pass # cpp source

	def GetInterpValueSm(self, Pos: cPy.cTypes.cVec3) -> float:
		pass # cpp source

	def GetInterpValueSmNThrough(self, Pos: cPy.cTypes.cVec3, N: cPy.cTypes.cVec3) -> float:
		pass # cpp source

	def GetInterpValueSmThrough(self, Pos: cPy.cTypes.cVec3) -> float:
		pass # cpp source

	def GetCInterpValue(self, Pos: cPy.cTypes.cVec3, Backup: bool, Cash: any) -> float:
		pass # cpp source

	def GetPreciseValue(self, x: int, y: int, z: int, Cash: any, Backup: bool = False) -> any:
		pass # cpp source

	def GetPreciseValueRef(self, x: int, y: int, z: int, Cash: any) -> any:
		pass # cpp source

	def SetPreciseValue(self, x: int, y: int, z: int, V: any, Cash: any):
		pass # cpp source

	def GetInterpNormal(self, Pos: cPy.cTypes.cVec3, Backup: bool = False) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetInterpPreciseNormal(self, Pos: cPy.cTypes.cVec3, Dist: float) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetInterpEdgeNormal(self, Pos: cPy.cTypes.cVec3, Backup: bool = False) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetInterpNormal2(self, Pos: cPy.cTypes.cVec3, Backup: bool = False) -> cPy.cTypes.cVec3:
		pass # cpp source

	def UpdateMeshRect(self, cx: int, cy: int, cz: int, mc: any):
		pass # cpp source

	def UpdateFilling(self):
		pass # cpp source

	def CreateWholeMesh(self):
		pass # cpp source

	def UpdateMesh(self, NoCuda: bool = False):
		pass # cpp source

	@staticmethod
	def Render(IncludingPMS: bool = False, IncludingRtp: bool = False, ShadowOnly: bool = False):
		pass # cpp source

	def DrawPickPlane(self, invonly: bool = False):
		pass # cpp source

	def ScanRay(self, Orig: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Length: float) -> bool:
		pass # cpp source

	def OcScanRay(self, Orig: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Length: float, Quick: bool = False) -> bool:
		pass # cpp source

	def ScanCells(self, Orig: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Length: float) -> bool:
		pass # cpp source

	def ScanCellsGrad(self, Orig: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Length: float) -> bool:
		pass # cpp source

	def ScanCellsGradSmart(self, Orig: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Length: float, sm: bool) -> bool:
		pass # cpp source

	def ScanCellsGradSm(self, Orig: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Length: float) -> bool:
		pass # cpp source

	def Pick(self, Res: cPy.cTypes.cVec3, pic: any, OnlyPosition: bool = False) -> bool:
		pass # cpp source

	def SnapToVolume(self, pos: cPy.cTypes.cVec3, dir: cPy.cTypes.cVec3) -> cPy.cTypes.cVec3:
		pass # cpp source

	def StoreLayerToFile(self, y: float, Name: str):
		'''
			
			void ApplyToPickPool(Vector3D Pos,float Radius,fnGetSurfDisp4* fn,fnGetSurfDisp2* Reader,float SmDeg); // implementation not found
		
		'''
		pass # cpp source

	def Restore(self, BS: any, TryToFind: bool = False, CacheName: str = None):
		pass # cpp source

	def StoreGlobalIds(self, VO: VolumeObject, BS: any):
		pass # cpp source

	def RestoreGlobalIds(self, VO: VolumeObject, BS: any):
		pass # cpp source

	def MergePMS(self, PMS: any, Scale: float):
		pass # cpp source

	def ApplyHoleRect(self, Dest: VolumeObject = None, SplitBorder: float = 0, EraseOld: bool = True, Additive: bool = False):
		pass # cpp source

	def ApplyFilledRect(self, Start: cPy.cTypes.cVec3, N: cPy.cTypes.cVec3, Symm: cPy.cTypes.cMat4, neg: bool = False):
		pass # cpp source

	def ApplyFilledRectSymm(self, Start: cPy.cTypes.cVec3, N: cPy.cTypes.cVec3, neg: bool = False):
		pass # cpp source

	def EnsureNativeIfInVoxels(self):
		pass # cpp source

	def ApplyMeshChange(self, Forced: bool = False):
		pass # cpp source

	def ApplyMeshChangeAB(self, Forced: bool = False):
		pass # cpp source

	def DetectPureGeometry(self) -> int:
		pass # cpp source

	def VoxelizePureGeometry(self, Manually: bool, AsShell: bool, tovox: bool = True, suggestedpoly: int = 0):
		pass # cpp source

	def GetPolycount(self) -> int:
		pass # cpp source

	def DetectRealVoxels(self) -> bool:
		pass # cpp source

	def GetAverageEdgeLength(self, inGlobalSpace: bool) -> float:
		pass # cpp source

	def GetDimensionsInBasis(self, x: cPy.cTypes.cVec3 = cPy.cTypes.cVec3.AxisX, y: cPy.cTypes.cVec3 = cPy.cTypes.cVec3.AxisY, z: cPy.cTypes.cVec3 = cPy.cTypes.cVec3.AxisZ) -> any:
		pass # cpp source

	def MergeWithGivenPolycount(self, PolyCount: int, dest: VolumeObject, undo: bool, shelldepth: float = 0) -> float:
		pass # cpp source

	def MergeAdaptively(self, PolyCount: int, dest: VolumeObject) -> float:
		pass # cpp source

	def UpdateLayersFromVolumetricColor(self, vc: any, tm: cPy.cTypes.cMat4):
		pass # cpp source

	def ApplySimplifiedMeshChange(self, Subtract: int):
		pass # cpp source

	def ApplyMeshChangeOnTheFly(self):
		pass # cpp source

	def ProcessMeshChange(self):
		pass # cpp source

	def ApplyMeshChangeSimple(self):
		pass # cpp source

	def ApplyMeshChangeRough(self):
		pass # cpp source

	def ApplySurfaceDistortion(self, P: cPy.cTypes.cVec3, R: float, Dist: float, Method: int):
		pass # cpp source

	def ShrinkSurface(self, Pos1: cPy.cTypes.cVec3, Radius1: float, Pos2: cPy.cTypes.cVec3, Radius2: float, Dist: float):
		pass # cpp source

	def ApplySurfaceDistortionSymm(self, P: cPy.cTypes.cVec3, R: float, Dist: float, Method: int = 0):
		pass # cpp source

	def ShrinkSurfaceSymm(self, Pos1: cPy.cTypes.cVec3, Radius1: float, Pos2: cPy.cTypes.cVec3, Radius2: float, Dist: float):
		pass # cpp source

	def SetSurfClay(self, Pos: cPy.cTypes.cVec3, Radius: float, D: float):
		pass # cpp source

	def SetSurfPlane2(self, Pos: cPy.cTypes.cVec3, Radius: float, Dir: cPy.cTypes.cVec3, Softness: float):
		pass # cpp source

	def SetSurfPlaneSymm(self, Pos: cPy.cTypes.cVec3, Radius: float, D: float = 0, Dir: cPy.cTypes.cVec3 = cPy.cTypes.cVec3.Zero, SmDegree: float = 0):
		pass # cpp source

	def StrongSmooth(self, Pos: cPy.cTypes.cVec3, Radius: float, SmDegree: float, SmType: int):
		pass # cpp source

	def MoveSurfaceSymm(self, Start: cPy.cTypes.cVec3, Radius: float, Dist: cPy.cTypes.cVec3, Additive: bool):
		pass # cpp source

	def WrapCell(self, cx: int, cy: int, cz: int):
		pass # cpp source

	def WrapCell2(self, cx: int, cy: int, cz: int, AdditionalSource: VolumeObject):
		pass # cpp source

	def GrowDencity(self):
		pass # cpp source

	def SetEmplty(self):
		pass # cpp source

	def Symmetry(self):
		pass # cpp source

	def CleanSurface(self):
		pass # cpp source

	def LegacyFix(self):
		pass # cpp source

	def Decompose(self, MinCluster: int, DelSize: int):
		pass # cpp source

	def DeleteHidden(self):
		'''
			
		< Separate loose parts
		
		'''
		pass # cpp source

	def Decimate(self):
		pass # cpp source

	def DecimateEx(self, Degree: float, Undo: bool, rk: float) -> bool:
		pass # cpp source

	def Shell(self):
		pass # cpp source

	def Bevel(self):
		'''
			
		< Global operators
		
		'''
		pass # cpp source

	def RemoveSelfIntersections(self):
		pass # cpp source

	def CloseHolesFastAndGood(self, weld: bool, maxcontour: int = 100000) -> any:
		'''
			
		if maxcontour == 0 it just returns (HolesCount,MaxHole)
		
		'''
		pass # cpp source

	def CloseSurfHoles(self, interp: bool = True, type: int = 0, Accuracy: float = 0.22, MaxContourLength: int = 10000000):
		pass # cpp source

	def EstimateHoles(self, MaxHole: int, MinHole: int, NHoles: int):
		pass # cpp source

	def RenderAO(self, RenderPMS: bool = False):
		pass # cpp source

	def DelUnused(self):
		pass # cpp source

	def HideInRadius(self, Pos: cPy.cTypes.cVec3, Radius: float, Hide: bool):
		pass # cpp source

	def HideInRadiusSymm(self, Pos: cPy.cTypes.cVec3, Radius: float, Hide: bool):
		pass # cpp source

	def MarkFreezeInSurfMode(self, Pos: cPy.cTypes.cVec3, Radius: float, Pos1: cPy.cTypes.cVec3, Radius1: float, Inv: bool, Degree: float, Degree1: float, Additive: bool):
		pass # cpp source

	def MarkFreezeInSurfModeSymm(self, Pos: cPy.cTypes.cVec3, Radius: float, Pos1: cPy.cTypes.cVec3, Radius1: float, Inv: bool, Degree: float, Degree1: float, Additive: bool):
		pass # cpp source

	def SmoothFreezeInSurfMode(self, Pos: cPy.cTypes.cVec3, Radius: float, Degree: float):
		pass # cpp source

	def SmoothPoseInSurfMode(self, Pos: cPy.cTypes.cVec3, Radius: float, Degree: float):
		pass # cpp source

	def ExpandFreezeInSurfMode(self, Pos: cPy.cTypes.cVec3, Radius: float, inv: bool):
		pass # cpp source

	def SmoothColorInSurfMode(self, Pos: cPy.cTypes.cVec3, Radius: float, Degree: float, count: int = 1):
		pass # cpp source

	def SmoothColorInVoxelMode(self, Pos: cPy.cTypes.cVec3, Radius: float, Degree: float, count: int = 1):
		pass # cpp source

	def SmoothCavityInSurfMode(self, count: int, SharpDegree: float, SmoothDegree: float):
		pass # cpp source

	def SmoothFreezeInSurfModeSymm(self, Pos: cPy.cTypes.cVec3, Radius: float, Degree: float):
		pass # cpp source

	@staticmethod
	def SmoothFreezeInPaintRoom(Pos: cPy.cTypes.cVec3, Radius: float, Degree: float):
		pass # cpp source

	def InvertSurfFreeze(self):
		pass # cpp source

	@staticmethod
	def InvertPoseSelection():
		pass # cpp source

	@staticmethod
	def ApplyPoseSelection() -> bool:
		pass # cpp source

	def UpdateDirtyPoseSelection(self):
		pass # cpp source

	def ConvertPoseSelectionToFreeze(self):
		pass # cpp source

	def UnfreezeSurf(self):
		pass # cpp source

	def AllocVox(self) -> any:
		pass # cpp source

	def AllocVox(self, Filler: any) -> any:
		pass # cpp source

	def FreeVox(self, vc: any):
		pass # cpp source

	def AllocCell(self) -> any:
		pass # cpp source

	def FreeCell(self, vc: any):
		pass # cpp source

	def CreateSegSelection(self, P1: cPy.cTypes.cVec3, P2: cPy.cTypes.cVec3, EyeDir: cPy.cTypes.cVec3, PP: any, LSP: cPy.cTypes.cMat4, Mode: int, SubMode: int) -> cPy.cTypes.cVec3:
		pass # cpp source

	def CreateRectSelection(self, EyeDir: cPy.cTypes.cVec3, PP: any, LSP: cPy.cTypes.cMat4, Mode: int, SubMode: int, FreezeOnly: bool, WeightMod: float = 1.0) -> cPy.cTypes.cVec3:
		pass # cpp source

	def CreateSegSelectionSymm(self, P1: cPy.cTypes.cVec3, P2: cPy.cTypes.cVec3, EyeDir: cPy.cTypes.cVec3, PP: any, LSP: cPy.cTypes.cMat4, Mode: int, SubMode: int) -> cPy.cTypes.cVec3:
		pass # cpp source

	def CreateRectSelectionSymm(self, EyeDir: cPy.cTypes.cVec3, PP: any, LSP: cPy.cTypes.cMat4, Mode: int, SubMode: int, FreezeOnly: bool, WeightMod: float = 1.0) -> cPy.cTypes.cVec3:
		pass # cpp source

	def GetMainAxis(self, UseFreeze: bool, InvFreeze: bool, UseSymm: bool, RefPoint: cPy.cTypes.cVec3) -> cPy.cTypes.cMat4:
		pass # cpp source

	def GetSelBasis(self, UseFreeze: bool, InvFreeze: bool, UseSymm: bool, RefPoint: cPy.cTypes.cVec3) -> cPy.cTypes.cMat4:
		pass # cpp source

	def ExtrudeSurfInRect(self, EyeDir: cPy.cTypes.cVec3, Dist: float, AvgNormal: int):
		pass # cpp source

	def ExtrudeSurfInRectSymm(self, EyeDir: cPy.cTypes.cVec3, Dist: float):
		pass # cpp source

	def ClearSegSelection(self, PP: any, Remesh: bool = False, Undo: bool = False):
		pass # cpp source

	def ApplyPenSelection(self, P: cPy.cTypes.cVec3, R: float, Mode: bool, Transparency: float):
		pass # cpp source

	def ApplyPenSelectionSymm(self, P: cPy.cTypes.cVec3, R: float, Mode: bool, Transparency: float):
		pass # cpp source

	def PrintMemUsageReport(self):
		pass # cpp source

	def CopyTo(self, Dest: VolumeObject, Undo: bool = True):
		pass # cpp source

	def MergeToOtherVO(self, VO: VolumeObject, Sub: int = False):
		pass # cpp source

	def MergeToThisVO(self, ExtraTransform: cPy.cTypes.cMat4, ClearThis: bool, NoUndo: bool = False):
		pass # cpp source

	def ExtrudeVO(self, Value: float, Sub: int = 0, Clr: bool = False, forcevox: bool = False):
		pass # cpp source

	def CreateShell(self, Value: float):
		pass # cpp source

	def MakeHull(self, L: int):
		pass # cpp source

	def MergeHullToOtherVO(self, VO: VolumeObject, In: float, Out: float, ReScale: bool):
		pass # cpp source

	def RemoveConnectedParts(self, pt: cPy.cTypes.cVec3, remBB: any, MaxRadius: float):
		'''
			
		Remove parts, connected to nearest point
		
		'''
		pass # cpp source

	def ToSTL(self, OnlyThis: bool, BS: any, SingleM: cPy.cTypes.cMat4 = cPy.cTypes.cMat4.Identity, OnlySel: bool = False) -> bool:
		'''
			
		Throw to `cMeshContainer`.\n
		For example
		
		::

			cMeshContainer  mc;
			this->ToRawMesh( true, true, &mc, Matrix4D::Identity, false );
			

			\todo Note unobvious params.
		
		'''
		pass # cpp source

	def GetVoTNB(self, T: cPy.cTypes.cVec3, N: cPy.cTypes.cVec3, B: cPy.cTypes.cVec3, R: bool):
		pass # cpp source

	def RestoreFromBackup(self):
		pass # cpp source

	def Flip(self, x: bool, y: bool, z: bool):
		pass # cpp source

	def MakeUniform(self, global_space: bool):
		pass # cpp source

	def ExportRawVoxels(self, File: str, bits: int, CreateHeader: bool, color: bool, gloss: bool, layers: bool):
		pass # cpp source

	def ImportRawVoxels(self, File: str, offset: int, bits: int, Lx: int, Ly: int, Lz: int, Scale: float):
		pass # cpp source

	def EstimateInitialParameters(self, File: str, offset: int, bits: int, Lx: int, Ly: int, Lz: int) -> bool:
		pass # cpp source

	@staticmethod
	def ExportRawVoxelsWithDialog():
		pass # cpp source

	@staticmethod
	def ImportRawVoxelsWithDialog():
		pass # cpp source

	def SplitInTwo(self, InsertInTree: bool, EraseOld: bool, subtree: bool = False, changetool: bool = True) -> VolumeObject:
		pass # cpp source

	def HideVoxRect(self, Hide: bool):
		pass # cpp source

	def UnhideAllVoxels(self):
		pass # cpp source

	def SeparateHidden(self):
		pass # cpp source

	def ToCache(self):
		pass # cpp source

	def FromCache(self):
		pass # cpp source

	def FromCacheEx(self):
		pass # cpp source

	def ApplySketchToCell(self, x: int, y: int, z: int) -> any:
		pass # cpp source

	def CreateSketch(self, num_steps: int = 2, Softness: float = 0):
		pass # cpp source

	def Barelief(self, Org: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Coef: float, FreeEdges: bool = False, Tapering: float = 0, KeepScale: bool = False, Undo: bool = True, ExDensity: float = 1.0, KeepBottom: bool = False):
		pass # cpp source

	def LegacyBarelief(self, Org: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Coef: float, FreeEdges: bool = False, Tapering: float = 0, KeepScale: bool = False, Undo: bool = True, ExDensity: float = 1.0, KeepBottom: bool = False):
		pass # cpp source

	def RemoveUndercuts(self, Start: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3, Tapering: float, KeepBottom: bool = False):
		pass # cpp source

	def DirectionalNormalsSmoothing(self, LocalDir: cPy.cTypes.cVec3, divirvence: float):
		pass # cpp source

	def CutUnderPlane(self, Start: cPy.cTypes.cVec3, Dir: cPy.cTypes.cVec3):
		pass # cpp source

	def RemoveInvisibles(self):
		pass # cpp source

	def ToSurfMode(self, ask: bool = False):
		pass # cpp source

	def ToVoxMode(self):
		pass # cpp source

	def SurfSmoothAll(self):
		pass # cpp source

	def SmoothOpenEdgesDialog(self):
		pass # cpp source

	def SmoothOpenEdges(self, times: int):
		pass # cpp source

	def SurfIdeal(self):
		pass # cpp source

	def CloseInnerHoles(self):
		pass # cpp source

	def RemoveIndexedStructure(self):
		pass # cpp source

	def CreateIndexedStructure(self):
		pass # cpp source

	def CreateIndexedStructure2(self):
		'''
			
		< fills GlobalVertIndices for every cell, assigns global index for each vertex
		
		'''
		pass # cpp source

	def CreateAdjacent(self):
		'''
			
		< fills GlobalVertIndices for every cell, assigns global index for each vertex, the difference is that this function makes job basing on coordinates of vertices
		
		'''
		pass # cpp source

	def MergeRegularMesh(self, mc: any, Inv: bool):
		pass # cpp source

	def CreateGlobalVoxAABB(self, AB: any, Subtrct: bool):
		pass # cpp source

	def SubdivBkCellsIfNeed(self):
		pass # cpp source

	def SubdivAllCells(self):
		pass # cpp source

	def FixVCLayersErrors(self):
		pass # cpp source

	def FixVCLayersErrors(self, vc: any):
		pass # cpp source

	def PerformVolumeCSG(self, Fiels: any, gen: any):
		pass # cpp source

	def SurfaceRectCut(self, T: cPy.cTypes.cMat4, symidx: int = 1):
		pass # cpp source

	def SurfaceRectCloseHole(self, T: cPy.cTypes.cMat4):
		pass # cpp source

	def SurfaceRectMakeHole(self, T: cPy.cTypes.cMat4):
		pass # cpp source

	def BooleanMerge(self, bm: any, sub: int):
		pass # cpp source

	def SurfaceRectCut2(self, Field: any, ProjField: any):
		pass # cpp source

	def SurfaceRectCloseHole2(self, Field: any):
		pass # cpp source

	def SurfaceRectMakeHole2(self, Field: any):
		pass # cpp source

	def CheckLinearFit(self):
		pass # cpp source

	def RemoveUnusedVerts(self, vc: any):
		pass # cpp source

	def RemoveUnusedVerts(self):
		pass # cpp source

	@staticmethod
	def RemoveUnusedVertsForAllVolumes():
		pass # cpp source

	def ReorderCells(self, Undo: bool = True, Subcells: bool = True):
		pass # cpp source

	def CheckGlobals(self):
		pass # cpp source

	def ChecAttr(self):
		pass # cpp source

	def OptimizeTables(self):
		pass # cpp source

	def CheckDupIds(self):
		pass # cpp source

	def OptimizeIndicesUsage(self):
		pass # cpp source

	def Reproject(self, Center: cPy.cTypes.cVec3, Radius: float, Direction: cPy.cTypes.cVec3, T: cPy.cTypes.cVec3, B: cPy.cTypes.cVec3, method: int, normalsource: int, deepdeg: float, reprojectcolor: bool):
		pass # cpp source

	def Reproject(self, InDistance: float, OutDistance: float, method: int, reprojectcolor: bool):
		pass # cpp source

	def CalculateAllNormals(self):
		pass # cpp source

	def CalcSquare(self) -> float:
		pass # cpp source

	@staticmethod
	def EnsurePaintLayer():
		pass # cpp source

	@staticmethod
	def AutoPaintInVolume(operation: str) -> bool:
		pass # cpp source

	@staticmethod
	def AutoRectInVolume(operation: str) -> bool:
		pass # cpp source

	def SplitByCurve(self, cu: any, Thickness: float = 0, method: int = 0, make_shape: bool = False):
		pass # cpp source

	def SplitRich(self, cu: any):
		pass # cpp source

	def MakeBevelOverCurve(self, cu: any):
		pass # cpp source

	def GetClosestCell(self, pt: cPy.cTypes.cVec3, Global: bool) -> cPy.cTypes.cVec3:
		pass # cpp source

	def SurfSubdiv(self, calcGraph: any, layers: bool = True, scale: bool = True, linear: bool = False):
		pass # cpp source

	def StepDown(self, skipChanges: bool = False):
		pass # cpp source

	def ClearSubdLevels(self):
		pass # cpp source

	def TestMultiresolution(self, message: str = None) -> bool:
		pass # cpp source

	def CheckIfMultiresolutionUsed(self) -> bool:
		pass # cpp source

	def TopologyLocked(self) -> bool:
		pass # cpp source

	def CollapseBooleans(self):
		pass # cpp source



class SmoothParams(cPy.cCore.BaseClass):
	def __init__(self):
		pass # CPP source

	SmoothingDegree: float #: float (T)  
	Tangent: bool #: bool (T)  
	Relaxation: bool #: bool (T)  
	KeepSharpEdges: bool #: bool (T)  
	KeepOpenEdges: bool #: bool (T)  
	InvertFreeze: bool #: bool (T)  


class VolumeCell():
	'''
			
		Contains voxel values.
		
		Each volume / surface object consists of cells. In case of voxels all cells has same width
		in space - 8 voxels, array of voxels is 9x9x9 - last, 9's is from right neighbour cell.\n
		In voxel mode you are operating with voxels, surface will be generated by voxels using marshing cubes.\n
		In case of surface there is no voxel data (polygons / layers / colors) are kept in `VolumeCellAttrib`.
		
	'''

	def __init__(self, Ow: VolumeObject):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Destroy(self):
		pass # cpp source

	def Destroy2(self):
		pass # cpp source

	Attr: any #: VolumeCellAttrib * (T)  Represents cell's polygonal surface. If it is `nullptr`, there are no faces in the cell. 
	Owner: VolumeObject #: VolumeObject * (T)  
	BackupDropTick: int #: int (T)  Cells before this change. Undo will get to this state when applied. 
	Backup: VolumeCell #: VolumeCell * (T)  
	Temp: any #: VoxType * (T)  
	Values: any #: VoxType * (T)  Pointer to voxels array 9x9x9. Voxel values itself, <=32767 - empty space, >=32768 - filled space.\n For details, it may be zero if all voxels are the same. In this case `SameValue` contains this same value. Surface is determined by the value 32767 using marching cubes. 
	Layers: any #: cList<VolumetricLayer *>(T)  
	SameValue: any #: VoxType (T)   If cell is completely filled or empty and `Values == nullptr` the value is used as cell filler. 
	boolean_hash: float #: float (T)  
	RenderStamp: any #: WORD (T)  
	Nx: any #: BYTE (T)  < cell is locked for changes, rather used for temporary purposes 
	def AllocAttributes(self):
		'''
			
		< usually = 9, Cell is (Nx * Nx * Nx)
		
		'''
		pass # cpp source

	def FreeAttributes(self):
		pass # cpp source

	def TryToFreeAttributes(self):
		pass # cpp source

	def Compact(self, FreeCell: bool = True, Multithread: bool = False):
		pass # cpp source

	def Compact8(self):
		pass # cpp source

	def Explicit(self, WhatTodo: int = 3, Multithreaded: bool = False):
		'''
			
		< \param WhatTodo  1 - allocate, 2 - fill, 3 - all
		
		'''
		pass # cpp source

	def CalcABC(self):
		pass # cpp source

	def UpdateRect(self, RStamp: int):
		pass # cpp source

	def FreeVolLayers(self):
		pass # cpp source

	def GetVolumetricLayer(self, LayerID: int, type: int, create: bool) -> any:
		pass # cpp source



class VolumeCellAttrib():
	'''
			
		Main brick in voxel / surface structure.
		
		It contains polygonal geometry, color layers if given cell of the surface
		pointer to this structure kept in `VolumeCell`.
		
	'''

	RctX: int #: short (T)  
	RctY: int #: short (T)  
	RctW: int #: short (T)  
	RctH: int #: short (T)  
	VertsAB: any #: AABoundBox (T)  
	Verts: any #: cList<MCVertex>(T)  Vertices of the mesh in the cell. Of course, same vertex may be present in neighbour cells and sometimes you need to identify that 2 vertices from different cells represent single global index. There are two ways. Using `Status` field in `MCVertex` that represents edge status. It has global index for every vertex in cell. 
	BackupVerts: any #: cList<MCVertex>(T)  
	LeakyPos: any #: cList<vPosNorm>(T)  
	BackupIds: any #: cList<indtype>(T)  Verticies and indicies before this change. Undo will get to this state when applied. 
	OldVerts: any #: cList<MCVertex>(T)  Positions / normals of vertices before entering surface mode. 
	Indices: any #: cList<indtype>(T)  Indices of mesh in the cell. They refer vertices in this cell. Each three indices represent triangle. 
	TempVerts: any #: cList<MCVertex>(T)  
	GlobalVertIndices: cPy.cList.cList_DWORD #: cList_DWORD (T)  GlobalVertIndices are references of global vertices indices. GlobalVertIndices corresponds to vertex list Verts. Each vertex in Verts corresponds to item in GlobalVertIndices. If GlobalVertIndices is empty - there are no global indexation in the mesh. Each value is DWORD. Highest bit (0x80000000) is set up if the vertex is on the edge of the cell. The global index itself is GlobalVertIndices[i]&0x7FFFFFFFFF 
	Layers: any #: cList<VoxLayer>(T)  
	CurLayerInvisible: bool = Coat_CPP.VolumeCellAttrib.CurLayerInvisible #: static bool (T)  
	CurLayerDepthMod: float = Coat_CPP.VolumeCellAttrib.CurLayerDepthMod #: static float (T)  
	UseLayerScale: bool = Coat_CPP.VolumeCellAttrib.UseLayerScale #: static bool (T)  
	InvisLayerWarning: bool = Coat_CPP.VolumeCellAttrib.InvisLayerWarning #: static bool (T)  
	def SetVertexPos(self, index: int, newpos: cPy.cTypes.cVec3, inlayers: bool = False):
		pass # cpp source

	def IncVertexPos(self, index: int, add: cPy.cTypes.cVec3, inlayers: bool = False):
		pass # cpp source

	def EnsureLayerExists(self):
		pass # cpp source

	def RemoveLayer(self, LayerID: int):
		'''
			
		CompactArray<TexturedVertex> TVerts;//textured vertices
		
		'''
		pass # cpp source

	def Insertlayer(self, LayerID: int, MandatoryDepth: bool = False) -> any:
		pass # cpp source

	def GetLayer(self, LayerID: int) -> any:
		pass # cpp source

	def AddVertexToLayers(self, pv1: int = 1, pv2: int = 1, W: float = 0.5):
		pass # cpp source

	def AddVertexToLayers(self, pv1: int, pv2: int, pv3: int, u: float, v: float):
		pass # cpp source

	def AddDefaultVertexToLayers(self):
		pass # cpp source

	def UpdateLayersSumm(self, vo: VolumeObject):
		pass # cpp source

	def UpdateLayersSumm2(self):
		pass # cpp source

	def FreeLayers(self):
		pass # cpp source

	def ValidateColor(self, vl: any):
		pass # cpp source

	def DrewDbgTri(self, idx: int, m: cPy.cTypes.cMat4, Color: int = 0, coef: float = 0.9):
		pass # cpp source

	def DrawDbg(self, m: cPy.cTypes.cMat4 = cPy.cTypes.cMat4.Identity, Color: int = 0, coef: float = 0.9):
		pass # cpp source

	def GetVertexColor(self, p: int) -> int:
		pass # cpp source

	Temp4D: cPy.cTypes.cVec4 #: cVec4 * (T)  
	Dirty: any #: WORD (T)  For tracking persistent data. 
