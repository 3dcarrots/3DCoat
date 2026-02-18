from __future__ import annotations
import cPy.cTypes
import cPy.cCore
#cOptions
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class OneHotKey(cPy.cCore.BaseClass):

	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->OneHotKey:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a OneHotKey class or its descendant, and if so, returns the specified object, but of the OneHotKey type.
		'''
		pass # cpp source

	ID: cPy.cTypes.cStr #: cStr (T)  
	NakedID1: cPy.cTypes.cStr #: cStr (T)  
	NakedID2: cPy.cTypes.cStr #: cStr (T)  
	nNakedStages: int #: int (T)  
	Room: cPy.cTypes.cStr #: cStr (T)  
	def __str__(self) -> str:
		pass # cpp source

	def __repr__(self) -> str:
		pass # cpp source

	Code: int #: int (T)  
	Stack: int #: int (T)  
	Firm: bool #: bool (T)  
	Ctrl: bool #: bool (T)  
	Alt: bool #: bool (T)  
	Shift: bool #: bool (T)  
	AllowStack: bool #: bool (T)  
	UserDefined: int #: int (T)  
	def Recognize(self, keys: str):
		pass # cpp source

	def SetupNaked(self):
		pass # cpp source



class OneToolPreset():

	@staticmethod
	def dynamic_cast(pObject : any)->OneToolPreset:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a OneToolPreset class or its descendant, and if so, returns the specified object, but of the OneToolPreset type.
		'''
		pass # cpp source

	def SetDefOptions(self):
		pass # cpp source

	ToolName: cPy.cTypes.cStr #: cStr (T)  


class PanoLightDir():
	D: cPy.cTypes.cVec3 #: cVec3 (T)  
	C: cPy.cTypes.cVec3 #: cVec3 (T)  Direction 


class AppOptions(cPy.cCore.BaseClass):

	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->AppOptions:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a AppOptions class or its descendant, and if so, returns the specified object, but of the AppOptions type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	@staticmethod
	def Choose():
		pass # cpp source

	AutoReloadChangedModules: bool = Coat_CPP.AppOptions.AutoReloadChangedModules #: static bool (T)  Auto Reload Changed Modules 
	HideAll: bool = Coat_CPP.AppOptions.HideAll #: static bool (T)  
	ShowBetaTools: bool = Coat_CPP.AppOptions.ShowBetaTools #: static bool (T)  Show Beta Tools 
	AllowGPULayerProcessing: bool = Coat_CPP.AppOptions.AllowGPULayerProcessing #: static bool (T)  
	AllowLiveBooleans: bool = Coat_CPP.AppOptions.AllowLiveBooleans #: static bool (T)  Add the child volume to any volume in the scene, press RMB over the child, and see the "Live.." items. 
	ShowMirrored: bool = Coat_CPP.AppOptions.ShowMirrored #: static bool (T)  This option is applicable only if symmetry enabled. In this mode you should create topology only on one side of symmetry. Opposite side will be shown as in mirror without actual creation of polygons. After you will finish you may ""Apply symmetry" to get real topology on both sides. If this mode is turned off polygons will be automatically created on both sides of the symmetry 
	rtMakeSculptMesh: bool = Coat_CPP.AppOptions.rtMakeSculptMesh #: static bool (T)  This tool allows to add coating over the layer in non-destructive way. It is similar to VoxLayer, but you may defune area using curves and change corner points later. 
	rtSubdivide1: bool = Coat_CPP.AppOptions.rtSubdivide1 #: static bool (T)  
	rtSubdivide2: bool = Coat_CPP.AppOptions.rtSubdivide2 #: static bool (T)  
	rtSubdivide3: bool = Coat_CPP.AppOptions.rtSubdivide3 #: static bool (T)  
	ShowUVOverlapping: bool = Coat_CPP.AppOptions.ShowUVOverlapping #: static bool (T)  Show/Hide UV faces overlapping 
	AllowVoxelsPaint: bool = Coat_CPP.AppOptions.AllowVoxelsPaint #: static bool (T)  Enable the Voxel Paint for all tools. It means that constructive sculpting brushes will not only grow the surface but also cover it with PBR paint material. All Additive merging (boolean) operations will be covered with the selected Paint as well, when Voxel Paint is enabled. Shapes with different paint, will maintain their respective paint values to the point where the shapes meet. 
	AllowPolyVoxels: bool = Coat_CPP.AppOptions.AllowPolyVoxels #: static bool (T)  
	AllowRetopoVoxels: bool = Coat_CPP.AppOptions.AllowRetopoVoxels #: static bool (T)  
	Medical: bool = Coat_CPP.AppOptions.Medical #: static bool (T)  
	LockUI_Changes: bool = Coat_CPP.AppOptions.LockUI_Changes #: static bool (T)  
	AutoUnwrapAttachedFaces: bool = Coat_CPP.AppOptions.AutoUnwrapAttachedFaces #: static bool (T)  Auto unwrap faces that was created nearby to already unwrapped island. Unwrapping will be performed each time when you switch new tool 
	BackfaceCulling: bool = Coat_CPP.AppOptions.BackfaceCulling #: static bool (T)  Backface Culling 
	ShowCommandsID: bool = Coat_CPP.AppOptions.ShowCommandsID #: static bool (T)  
	ExtrudeMaskBothSides: bool = Coat_CPP.AppOptions.ExtrudeMaskBothSides #: static bool (T)  
	RenderCurvesOnBackFaces: bool = Coat_CPP.AppOptions.RenderCurvesOnBackFaces #: static bool (T)  Render Curves on Back Faces_HINT 
	AutoZipScenes: bool = Coat_CPP.AppOptions.AutoZipScenes #: static bool (T)  This options allows to preserve disk space. At first, 3B scene will be saved as is. Then it will be gradually zipped, it will be done on background without interruption of your job. After siccessfull zipping the scene file will be replaced with the zipped one. 
	CorrectAlphaRendering: bool = Coat_CPP.AppOptions.CorrectAlphaRendering #: static bool (T)  To view semi-transparent models correctly, we need to sort faces from back to front. Generally, it is a fast process, but if you feel that it slows rendering down, you may turn it off. Pay attention, alpha ordering works only for paint objects currently. 
	GlobalEnablePrintingGrid: bool = Coat_CPP.AppOptions.GlobalEnablePrintingGrid #: static bool (T)  AppOpt.GlobalEnablePrintingGrid_HINT 
	SkipCacheQuest: bool = Coat_CPP.AppOptions.SkipCacheQuest #: static bool (T)  When you click on cache/uncache from the VoxTree you will be asked if you really need it. If this option is turned on the question will not appear. 
	RequestAO_mode: int = Coat_CPP.AppOptions.RequestAO_mode #: static int (T)  RequestAO_mode_HINT 
	RequestCavity_mode: int = Coat_CPP.AppOptions.RequestCavity_mode #: static int (T)  RequestCavity_mode_HINT 
	QWER_for_gizmo: bool = Coat_CPP.AppOptions.QWER_for_gizmo #: static bool (T)  QWER_for_gizmo_HINT 
	ActivityBarStyle: int = Coat_CPP.AppOptions.ActivityBarStyle #: static int (T)  Activity Bar Position 
	IgnoreOptSaving: bool = Coat_CPP.AppOptions.IgnoreOptSaving #: static bool (T)  
	ChangeLanguagesDirectly: bool = Coat_CPP.AppOptions.ChangeLanguagesDirectly #: static bool (T)  In case if you want to help with translation to your native language there are two options. First, default is to translate ID and then send it to us via the web form. Another option - you may translate the whole language file locally and then send it to us (to support@pilgway.com). Enable this option, translate, ensure that your ID-s appear in UI. Pay attention that the file InstallFolder/data/Languages/YourLanguage.xml will be modified, modification of the file in the install folder requires running the coat{CY} "as administrator"{C}. 
	AllowSplines49: bool = Coat_CPP.AppOptions.AllowSplines49 #: static bool (T)  Enable the old version of splines in the E-panel. The new version of splines will be available as well. 
	EModeAngleStep: float = Coat_CPP.AppOptions.EModeAngleStep #: static float (T)  This is the angle step if you press ALT+CTRL in the rectangle/lasso/ellipse E-mode (E is the default hotkey to trigger the panel) 
	PositiveAlpha: bool = Coat_CPP.AppOptions.PositiveAlpha #: static bool (T)  If enabled, the top left pixel value will not be subtracted from the alpha depth. 
	DontGroupObjVerts: bool = Coat_CPP.AppOptions.DontGroupObjVerts #: static bool (T)  This option may help when you need to keep vertices order unchanged in single heap. Even if 3DCoat tries to keep the vertex order unchanged, sometimes this is not enough. In this case, enable this option. 
	SubtractionShell: float = Coat_CPP.AppOptions.SubtractionShell #: static float (T)  This is an additional shell for subtractive Boolean operations. 
	UseSoftBooleansForVoxels: bool = Coat_CPP.AppOptions.UseSoftBooleansForVoxels #: static bool (T)  Use Soft Booleans for Voxels 
	VoxelsSoftBooleansRadius: float = Coat_CPP.AppOptions.VoxelsSoftBooleansRadius #: static float (T)  
	ApplinkSculptToImport: bool = Coat_CPP.AppOptions.ApplinkSculptToImport #: static bool (T)  With this checkbox, AppLink triggers the Import tool. Otherwise, the model will get to the new surface layer. 
	NotifyAboutUpdates: bool = Coat_CPP.AppOptions.NotifyAboutUpdates #: static bool (T)  Notify me about new updates 
	OnlyStableUpdates: bool = Coat_CPP.AppOptions.OnlyStableUpdates #: static bool (T)  Notify only about updates marked as {CY}Stable{C}. 
	UndercutsEdgeOpacity: float = Coat_CPP.AppOptions.UndercutsEdgeOpacity #: static float (T)  
	UndercutsTopBottomOpacity: float = Coat_CPP.AppOptions.UndercutsTopBottomOpacity #: static float (T)  
	BEdgeWidth: float = Coat_CPP.AppOptions.BEdgeWidth #: static float (T)  The edge corresponds to the tapering angle. The edge contrast regulates the sharpness of the border. 
	RollAngle: float = Coat_CPP.AppOptions.RollAngle #: static float (T)  
	HideViewGizmo: bool = Coat_CPP.AppOptions.HideViewGizmo #: static bool (T)  Hide the Viewport Navigation Gizmo 
	HideMaterialPreview: bool = Coat_CPP.AppOptions.HideMaterialPreview #: static bool (T)  Hide Material Preview 
	ShowHints: bool = Coat_CPP.AppOptions.ShowHints #: static bool (T)  Allows you to show or hide popup tooltips near your mouse cursor 
	ShowBottomHints: bool = Coat_CPP.AppOptions.ShowBottomHints #: static bool (T)  Show Expanded Tooltips (Bottom of 3D Viewport) 
	NarrowLeftPanel: bool = Coat_CPP.AppOptions.NarrowLeftPanel #: static bool (T)  You can hide left tool panels if you prefer to use "space" menu 
	ShowCurrentPointPos: bool = Coat_CPP.AppOptions.ShowCurrentPointPos #: static bool (T)  Show Current Pick Point Coordinate Preview 
	ShowGrid: bool = Coat_CPP.AppOptions.ShowGrid #: static bool (T)  Toggle 3D grid 
	ShowBuildVolume: bool = Coat_CPP.AppOptions.ShowBuildVolume #: static bool (T)  Show Build Volume 
	Snap3DGrid: bool = Coat_CPP.AppOptions.Snap3DGrid #: static bool (T)  Snap cursor to the projection of the 3D grid on the screen. If several grids are visible the most rotated toward screen will be chosen. It is recommended to use it in orthogonal projection. Gizmos and primitives positions and size will be snapped to discrete positions in space 
	GridZX: bool = Coat_CPP.AppOptions.GridZX #: static bool (T)  ZX Plane 
	GridXY: bool = Coat_CPP.AppOptions.GridXY #: static bool (T)  XY Plane 
	GridYZ: bool = Coat_CPP.AppOptions.GridYZ #: static bool (T)  YZ Plane 
	AutoGrid: bool = Coat_CPP.AppOptions.AutoGrid #: static bool (T)  Show corresponding grid plane automatically due to orientation in space 
	RareGrid: bool = Coat_CPP.AppOptions.RareGrid #: static bool (T)  
	NormalGrid: bool = Coat_CPP.AppOptions.NormalGrid #: static bool (T)  
	DenseGrid: bool = Coat_CPP.AppOptions.DenseGrid #: static bool (T)  
	CustomGrid: bool = Coat_CPP.AppOptions.CustomGrid #: static bool (T)  
	PalCellSize: int = Coat_CPP.AppOptions.PalCellSize #: static int (T)  
	UI_ExtraSize: int = Coat_CPP.AppOptions.UI_ExtraSize #: static int (T)  
	UI_FontYShift: int = Coat_CPP.AppOptions.UI_FontYShift #: static int (T)  
	UI_ClassEditorBorders: int = Coat_CPP.AppOptions.UI_ClassEditorBorders #: static int (T)  
	UserFontExtraLinesDistance: int = Coat_CPP.AppOptions.UserFontExtraLinesDistance #: static int (T)  The additional space between lines in UI. Useful if you are using custom fonts and want to adjust the visual appearance of the fonts. 
	UserFontDY: int = Coat_CPP.AppOptions.UserFontDY #: static int (T)  Shift the font up and down a bit for a better visual appearance. Usually helpful if custom fonts are used. 
	GridStep3D: float = Coat_CPP.AppOptions.GridStep3D #: static float (T)  Grid Step 
	GridSubSections: int = Coat_CPP.AppOptions.GridSubSections #: static int (T)  Grid Subdivisions 
	GridStepsCount: int = Coat_CPP.AppOptions.GridStepsCount #: static int (T)  Number of divisions in the grid 
	CachingMethod: int = Coat_CPP.AppOptions.CachingMethod #: static int (T)  
	SharpVoxExtrude: bool = Coat_CPP.AppOptions.SharpVoxExtrude #: static bool (T)  
	ProjectionThrough: bool = Coat_CPP.AppOptions.ProjectionThrough #: static bool (T)  Project the image through all object, even back faces 
	LockSymmetry: bool = Coat_CPP.AppOptions.LockSymmetry #: static bool (T)  Lock symmetry plane so that you will not be able to move it accidently with TAB key 
	ShowAxisX: bool = Coat_CPP.AppOptions.ShowAxisX #: static bool (T)  X 
	ShowAxisY: bool = Coat_CPP.AppOptions.ShowAxisY #: static bool (T)  Y 
	ShowAxisZ: bool = Coat_CPP.AppOptions.ShowAxisZ #: static bool (T)  Z 
	RtpObj: bool = Coat_CPP.AppOptions.RtpObj #: static bool (T)  Treat the retopo groups as materials instead on objects. Use this option on your own risk, it is not usual 3D-Coat's workflow. By default, retopo groups will be baked as objects. 
	AllowRmbProp: bool = Coat_CPP.AppOptions.AllowRmbProp #: static bool (T)  Enable or disable RMB properties window in Sculpt room. Window may be disabled as well by assigning hotkey in Windows->Popups->Trigger volume properties window 
	AllowRetopoRmbProp: bool = Coat_CPP.AppOptions.AllowRetopoRmbProp #: static bool (T)  Enable RMB Properties in the Retopo/Modeling/UV rooms 
	PanoRotation: float = Coat_CPP.AppOptions.PanoRotation #: static float (T)  
	PanoBlur: float = Coat_CPP.AppOptions.PanoBlur #: static float (T)  Drag to blur/sharp the environment texture in the viewport background 
	PreventDoublePainting: bool = Coat_CPP.AppOptions.PreventDoublePainting #: static bool (T)  This option is important if you have stacked or mirrored UV islands. If the opton is enabled the point on UV map may be painted only once per stroke. It is helpful if stacked islands have no boundary with each other (for example body - one island, arms and legs - other mirrored islands). If you enable symmetry and this option, arms and legs will not be pained twice. But if mirrored islands have common boundary between them, enabling this option will lead to artifacts near the common edges because same pixel is present on both sides of the edge. 
	ExpositionModulator: float = Coat_CPP.AppOptions.ExpositionModulator #: static float (T)  Exposure 
	NormalsDithering: bool = Coat_CPP.AppOptions.NormalsDithering #: static bool (T)  Bake Normals with Dithering 
	ShowWholeRoundGizmo: bool = Coat_CPP.AppOptions.ShowWholeRoundGizmo #: static bool (T)  Show Entire Circle of the Screen Space Rotation Gizmo 
	AllowLegacyProxyMode: bool = Coat_CPP.AppOptions.AllowLegacyProxyMode #: static bool (T)  Allow Proxy mode (the legacy tool) for Multi-Resolution, instead of Newer Levels-Based System 
	ShowMemoryInfo: bool = Coat_CPP.AppOptions.ShowMemoryInfo #: static bool (T)  It is useful if you hunt for memory leaks and investigate memory usage. 
	ArrayAndRoundingModifier: int = Coat_CPP.AppOptions.ArrayAndRoundingModifier #: static int (T)  E-mode Array and Rounding hotkeys 
	RecordTimelapse: bool = Coat_CPP.AppOptions.RecordTimelapse #: static bool (T)  Recording a timelapse of the process of working on a model without an interface. 
	TimelapseSmoothCamera: float = Coat_CPP.AppOptions.TimelapseSmoothCamera #: static float (T)  To prevent camera movement from flickering during timelapse, camera movement will be additionally smoothed to the specified degree. 
	TimelapseShotInterval: float = Coat_CPP.AppOptions.TimelapseShotInterval #: static float (T)  How often to take one snapshot of your work in seconds. 
	TimelapseHideGuides: bool = Coat_CPP.AppOptions.TimelapseHideGuides #: static bool (T)  
	TimelapseHidePMS: bool = Coat_CPP.AppOptions.TimelapseHidePMS #: static bool (T)  
	TimelapseDeleteShotsAfterConvert: bool = Coat_CPP.AppOptions.TimelapseDeleteShotsAfterConvert #: static bool (T)  
	BuildSizeX: float = Coat_CPP.AppOptions.BuildSizeX #: static float (T)  Build Size X 
	BuildSizeY: float = Coat_CPP.AppOptions.BuildSizeY #: static float (T)  Build Size Y 
	BuildSizeZ: float = Coat_CPP.AppOptions.BuildSizeZ #: static float (T)  Build Size Z 
	LayerThickness: float = Coat_CPP.AppOptions.LayerThickness #: static float (T)  Layer thickness is very important in 3D-print friendly mode. It defines the density of new volumes. The smaller Layer Thickness - the bigger is the density of voxel volumes. Bigger density means lower performance, but better quality. 
	UseFixedSceneScale: bool = Coat_CPP.AppOptions.UseFixedSceneScale #: static bool (T)  If you use a fixed scene scale the object will always be opened with this scale except scenes saved previously. This may be problematic in cases when objects are too huge or too small. It is recommended to keep scaled object size in the range 10-300. 
	FixedSceneScale: float = Coat_CPP.AppOptions.FixedSceneScale #: static float (T)  The scene scale to import objects. 
	SingleMaterialForSculptExport: bool = Coat_CPP.AppOptions.SingleMaterialForSculptExport #: static bool (T)  If it is set, then File->Export scene will export the mesh with multiple objects but a single material. 
	IslandsDistancePercent: float = Coat_CPP.AppOptions.IslandsDistancePercent #: static float (T)  Islands Distance Percentage_HINT 
	PreferredUVMethod: int = Coat_CPP.AppOptions.PreferredUVMethod #: static int (T)  Preferred unwrap method 
	AlwaysTryUvStripes: bool = Coat_CPP.AppOptions.AlwaysTryUvStripes #: static bool (T)  Use "To Strip" unwrapping whenever possible 
	BakeScanDepthIn: float = Coat_CPP.AppOptions.BakeScanDepthIn #: static float (T)  This value defines inner shell for baking. Scan ray will follow along normal direction inside the object on specified depth 
	BakeScanDepthOut: float = Coat_CPP.AppOptions.BakeScanDepthOut #: static float (T)  This value defines outer shell for baking. Scan ray will follow along normal direction outside the object on specified length 
	BakeOutmostSurface: bool = Coat_CPP.AppOptions.BakeOutmostSurface #: static bool (T)  
	OutmostBakingLimit: float = Coat_CPP.AppOptions.OutmostBakingLimit #: static float (T)  
	ShadersPreviewSize: int = Coat_CPP.AppOptions.ShadersPreviewSize #: static int (T)  
	ShapesPreviewSize: int = Coat_CPP.AppOptions.ShapesPreviewSize #: static int (T)  
	ShowFoldersAsButtons: bool = Coat_CPP.AppOptions.ShowFoldersAsButtons #: static bool (T)  Show Folders As Buttons 
	MaxAmountLinesOfFolders: int = Coat_CPP.AppOptions.MaxAmountLinesOfFolders #: static int (T)  Maximal amount of lines in folders list used for items lists like brushes, stencils, presets etc. 
	AllowMaterialNavigaion: bool = Coat_CPP.AppOptions.AllowMaterialNavigaion #: static bool (T)  Allow Material Navigation via LMB/RMB dragging in Viewport 
	AllowVolumetricPainting: bool = Coat_CPP.AppOptions.AllowVolumetricPainting #: static bool (T)  Allow Volumetric Painting 
	CustomMode: bool = Coat_CPP.AppOptions.CustomMode #: static bool (T)  
	GreyscalePano: bool = Coat_CPP.AppOptions.GreyscalePano #: static bool (T)  Use greyscale panoramas to avoid any color distortion 
	pGreyscalePano: bool = Coat_CPP.AppOptions.pGreyscalePano #: static bool (T)  
	VoxelPaintDepth: float = Coat_CPP.AppOptions.VoxelPaintDepth #: static float (T)  The depth of the voxel painting. Use caution when increasing depth of the color penetration, as it may cause artifacts (penetration to another side of the object, noise color spots over the noisy surfaces). So, we recommend lower paint depth values in general, but especially for thin and/or noisy surfaces. Additional, the larger depth values lead to slower performance. 
	EmbedTexturesToFBX: bool = Coat_CPP.AppOptions.EmbedTexturesToFBX #: static bool (T)  When you export FBX textures will be embedded directly into the FBX file. 
	csgo: int = Coat_CPP.AppOptions.csgo #: static int (T)  
	PhongExponent: float = Coat_CPP.AppOptions.PhongExponent #: static float (T)  
	PhongIntensity: float = Coat_CPP.AppOptions.PhongIntensity #: static float (T)  
	FontSize: int = Coat_CPP.AppOptions.FontSize #: static int (T)  Font Size 
	@staticmethod
	def LoadPano2(force: bool = False):
		'''
			
		0 - auto, 1 - small, 2 - medium, 3 - large
		
		'''
		pass # cpp source

	@staticmethod
	def RescaleScene(Scale: float, EvenEmpty: bool):
		pass # cpp source

	AutoUpdateRetopoPounts: bool = Coat_CPP.AppOptions.AutoUpdateRetopoPounts #: static bool (T)  
	@staticmethod
	def CheckHidden(id: str, IgnoreCustomMode: bool = False) -> bool:
		pass # cpp source

	@staticmethod
	def CheckHiddenD(id: str) -> bool:
		pass # cpp source

	@staticmethod
	def AddHidden(id: str):
		pass # cpp source

	@staticmethod
	def RemoveHidden(id: str):
		pass # cpp source

	@staticmethod
	def LoadHidden(name: str):
		pass # cpp source

	@staticmethod
	def SaveHidden(name: str):
		pass # cpp source

	@staticmethod
	def LoadRenamed():
		pass # cpp source

	@staticmethod
	def CheckRenamed(id: str) -> str:
		pass # cpp source

	AdditionalQuixelFolder: cPy.cTypes.cStr = Coat_CPP.AppOptions.AdditionalQuixelFolder #: static cStr (T)  AdditionalQuixelFolder_HINT 
	ShowAxis: bool = Coat_CPP.AppOptions.ShowAxis #: static bool (T)  Show/Hide Axis 
	Autosave: bool = Coat_CPP.AppOptions.Autosave #: static bool (T)  Enable AutoSave. Autosaved scenes stored as _autosave.3B in your folder's scene to avoid overwriting from different scenes and sessions. As soon as you load something like _autosaveN.3b, it gets name _recovered.3b in scene to prevent overwriting by newer autosaves. 
	SmallInterface: bool = Coat_CPP.AppOptions.SmallInterface #: static bool (T)  Toggle between the full or compact interface 
	AllowInertia: bool = Coat_CPP.AppOptions.AllowInertia #: static bool (T)  Allow inertia in scrollable dialogs 
	ColorConversionMode: bool = Coat_CPP.AppOptions.ColorConversionMode #: static bool (T)  
	LastAutosaveTime: int = Coat_CPP.AppOptions.LastAutosaveTime #: static int (T)  
	AutosaveTime: float = Coat_CPP.AppOptions.AutosaveTime #: static float (T)  Autosave Time 
	NumAutosaves: int = Coat_CPP.AppOptions.NumAutosaves #: static int (T)  Amount of autosave files to be sequentially stored 
	UseBackgrImage: int = Coat_CPP.AppOptions.UseBackgrImage #: static int (T)  Scene background style 
	BackgrImage: int = Coat_CPP.AppOptions.BackgrImage #: static int (T)  
	SkyBoxImage: int = Coat_CPP.AppOptions.SkyBoxImage #: static int (T)  
	SkyBoxNodesFBO: int = Coat_CPP.AppOptions.SkyBoxNodesFBO #: static int (T)  
	SkyBoxNodesFBOMid: int = Coat_CPP.AppOptions.SkyBoxNodesFBOMid #: static int (T)  
	SkyBoxNodesFBOMid2: int = Coat_CPP.AppOptions.SkyBoxNodesFBOMid2 #: static int (T)  
	SkyBoxNodesFBOMid3: int = Coat_CPP.AppOptions.SkyBoxNodesFBOMid3 #: static int (T)  
	SkyBoxNodesFBODiffuse: int = Coat_CPP.AppOptions.SkyBoxNodesFBODiffuse #: static int (T)  
	SkyBoxImageDiffuse: int = Coat_CPP.AppOptions.SkyBoxImageDiffuse #: static int (T)  
	SkyBoxImageName: cPy.cTypes.cStr = Coat_CPP.AppOptions.SkyBoxImageName #: static cStr (T)  Image to be used as a 360*180 skybox for background 
	SkyBoxMainDir: cPy.cTypes.cVec3 = Coat_CPP.AppOptions.SkyBoxMainDir #: static cVec3 (T)  
	@staticmethod
	def CreatePanoLights(csm: any):
		pass # cpp source

	@staticmethod
	def CheckSkyGreyscale():
		pass # cpp source

	LockPanorama: bool = Coat_CPP.AppOptions.LockPanorama #: static bool (T)  Lock Environment 
	CameraIsometricSnap45dg: bool = Coat_CPP.AppOptions.CameraIsometricSnap45dg #: static bool (T)  Hold down the Shift key during the rotation of the camera and it will snap to angle with 45 degrees relative to closest axis. 
	CameraIsometricSnapHexagon: bool = Coat_CPP.AppOptions.CameraIsometricSnapHexagon #: static bool (T)  Hold the Shift key while rotating the camera from top to lock the camera at an angle where the equilateral cubes look like equilateral hexagons. For get correct isometrics, please use orthographic view. 
	CameraIsometricSnapRhombus2x1: bool = Coat_CPP.AppOptions.CameraIsometricSnapRhombus2x1 #: static bool (T)  Hold the Shift key while rotating the camera from top to lock the camera at an angle where top side of the equilateral cubes look like rhombus 2x1. For get correct isometrics, please use orthographic view. 
	CameraInWorldCenter: bool = Coat_CPP.AppOptions.CameraInWorldCenter #: static bool (T)  Camera In World Center 
	CameraFor2DPaint: bool = Coat_CPP.AppOptions.CameraFor2DPaint #: static bool (T)  Camera For 2D Painting 
	CameraLock2DCanvas: bool = Coat_CPP.AppOptions.CameraLock2DCanvas #: static bool (T)  Camera Lock 2D Canvas. 
	Invert3DMouse: bool = Coat_CPP.AppOptions.Invert3DMouse #: static bool (T)  Invert 3D Mouse 
	Invert3DMouseForTransforms: bool = Coat_CPP.AppOptions.Invert3DMouseForTransforms #: static bool (T)  Invert 3D-Mouse For Transforms on objects transform mode. See Edit->Transform without gizmo->Transform with 3D-Connection/mouse. 
	TabletLibrary: int = Coat_CPP.AppOptions.TabletLibrary #: static int (T)  Tablet Interface 
	TreatEraserAsPen: bool = Coat_CPP.AppOptions.TreatEraserAsPen #: static bool (T)  Treat Eraser as Pen 
	IgnoreDoubleClicksFromPen: bool = Coat_CPP.AppOptions.IgnoreDoubleClicksFromPen #: static bool (T)  Ignore double clicks from pen 
	VSync: bool = Coat_CPP.AppOptions.VSync #: static bool (T)  Limit FPS by the display VSync frequency. It helps to decrease the GPU load. 
	GammaCorrectionRed: float = Coat_CPP.AppOptions.GammaCorrectionRed #: static float (T)  
	GammaCorrectionGreen: float = Coat_CPP.AppOptions.GammaCorrectionGreen #: static float (T)  
	GammaCorrectionBlue: float = Coat_CPP.AppOptions.GammaCorrectionBlue #: static float (T)  
	AcesTonemapping: bool = Coat_CPP.AppOptions.AcesTonemapping #: static bool (T)  Aces Tone Mapping is used widely in the Film & Game industry, and this mode will help the look in the viewport match more closely to the viewport in Game Engines or applications that employ it. 
	SoftwarePreset: int = Coat_CPP.AppOptions.SoftwarePreset #: static int (T)  Normal Map Software Preset 
	TBN_Normalisation: int = Coat_CPP.AppOptions.TBN_Normalisation #: static int (T)  Local space (TBN) normalization method 
	NormalsCalculationMethod: int = Coat_CPP.AppOptions.NormalsCalculationMethod #: static int (T)  Choose how normals of the mesh for painting will be calculated 
	TriangulationMethod: int = Coat_CPP.AppOptions.TriangulationMethod #: static int (T)  Triangulaton method is important for compatibility of normal maps. If triangulation method does not correspond to your modeling software and you will bake normal maps - cross-like artifacts may appear on quads 
	TBNMethod: int = Coat_CPP.AppOptions.TBNMethod #: static int (T)  Tangent space is important to render normal maps correctly. If you are using incorrect tangent space seams will be visible on baked model in your modeling software. So you need to choose method that is well compatible with your modeling software after exporting from 3DCoat. Difference is not too visible on organic models but may affect baking hardsurface models essentially 
	SwapTB: bool = Coat_CPP.AppOptions.SwapTB #: static bool (T)  Swap TB 
	DenormalizedTB: bool = Coat_CPP.AppOptions.DenormalizedTB #: static bool (T)  Denormalized TB 
	@staticmethod
	def GetSwapYZ() -> bool:
		pass # cpp source

	@staticmethod
	def SetSwapYZ(value: bool):
		pass # cpp source

	IconsHighlightColor: int = Coat_CPP.AppOptions.IconsHighlightColor #: static DWORD (T)  
	TopBackgroundColor: int = Coat_CPP.AppOptions.TopBackgroundColor #: static DWORD (T)  Top Background Color 
	BottomBackgroundColor: int = Coat_CPP.AppOptions.BottomBackgroundColor #: static DWORD (T)  Bottom Background Color 
	GridColor: int = Coat_CPP.AppOptions.GridColor #: static DWORD (T)  The 2D grid color, overlaid over the viewport 
	InterfaceColor: int = Coat_CPP.AppOptions.InterfaceColor #: static DWORD (T)  Overall interface color 
	DropdownColor: int = Coat_CPP.AppOptions.DropdownColor #: static DWORD (T)  Drop-down List Color 
	HeadersColor: int = Coat_CPP.AppOptions.HeadersColor #: static DWORD (T)  Menu and floating windows header color 
	ToolsHeadersColor: int = Coat_CPP.AppOptions.ToolsHeadersColor #: static DWORD (T)  The color of the headers of sections in left tool panel 
	ButtonsColor: int = Coat_CPP.AppOptions.ButtonsColor #: static DWORD (T)  This color will be used for buttons, sliders, and scrollers 
	ButtonDownColor: int = Coat_CPP.AppOptions.ButtonDownColor #: static DWORD (T)  
	ButtonMOverColor: int = Coat_CPP.AppOptions.ButtonMOverColor #: static DWORD (T)  
	HighlightColor: int = Coat_CPP.AppOptions.HighlightColor #: static DWORD (T)  This color will be used for highlighted elements; buttons, combo-boxes, and scrollers 
	MeshPreviewColor: int = Coat_CPP.AppOptions.MeshPreviewColor #: static DWORD (T)  The mesh preview color for primitives and import tools. 
	FontHighlightColor: int = Coat_CPP.AppOptions.FontHighlightColor #: static DWORD (T)  The color of font on the highlighted button 
	CurrLayerColor: int = Coat_CPP.AppOptions.CurrLayerColor #: static DWORD (T)  
	HintBGColor: int = Coat_CPP.AppOptions.HintBGColor #: static DWORD (T)  
	TopToolbarColor: int = Coat_CPP.AppOptions.TopToolbarColor #: static DWORD (T)  This color will be used for the toolbar tops 
	LeftToolbarColor: int = Coat_CPP.AppOptions.LeftToolbarColor #: static DWORD (T)  
	MenuColor: int = Coat_CPP.AppOptions.MenuColor #: static DWORD (T)  
	HintsColor: int = Coat_CPP.AppOptions.HintsColor #: static DWORD (T)  Hint Background 
	HintsTextColor: int = Coat_CPP.AppOptions.HintsTextColor #: static DWORD (T)  Hints Text Color 
	WireframeColor: int = Coat_CPP.AppOptions.WireframeColor #: static DWORD (T)  Wireframe Color 
	SeamsColor: int = Coat_CPP.AppOptions.SeamsColor #: static DWORD (T)  Seams color 
	SharpEdgesColor: int = Coat_CPP.AppOptions.SharpEdgesColor #: static DWORD (T)  Sharp edges color 
	SharpSeamsColor: int = Coat_CPP.AppOptions.SharpSeamsColor #: static DWORD (T)  Sharp Seams Color 
	DrawsColor: int = Coat_CPP.AppOptions.DrawsColor #: static DWORD (T)  Retopo strokes color 
	StartMenuHighlightColor: int = Coat_CPP.AppOptions.StartMenuHighlightColor #: static DWORD (T)  Start menu highlight color 
	SubfolderSelectionColor: int = Coat_CPP.AppOptions.SubfolderSelectionColor #: static DWORD (T)  Items folder selection color 
	SelectionContourColor: int = Coat_CPP.AppOptions.SelectionContourColor #: static DWORD (T)  The default contour color 
	RenderBackEdges: bool = Coat_CPP.AppOptions.RenderBackEdges #: static bool (T)  Render back edges (invisible due to Z-buffer) 
	UseReferenceColorForSelectionContour: bool = Coat_CPP.AppOptions.UseReferenceColorForSelectionContour #: static bool (T)  Use the volume reference color as the contour color 
	RenderSelectionContour: bool = Coat_CPP.AppOptions.RenderSelectionContour #: static bool (T)  Render the selection contour 
	ProjScaleFactor: int = Coat_CPP.AppOptions.ProjScaleFactor #: static int (T)  Additional scale that will be applied to the projection image to edit in external editor 
	TexApproach: int = Coat_CPP.AppOptions.TexApproach #: static int (T)  Texture Export/Import Workflow 
	StoreRGToMetAlpha: bool = Coat_CPP.AppOptions.StoreRGToMetAlpha #: static bool (T)  Store glossiness or roughness in alpha channel of metalness texture (in dependence on approach) 
	ComboDropdownAdjustment: float = Coat_CPP.AppOptions.ComboDropdownAdjustment #: static float (T)  
	ComboInnerAdjustment: float = Coat_CPP.AppOptions.ComboInnerAdjustment #: static float (T)  
	ComboArrowAdjustment: float = Coat_CPP.AppOptions.ComboArrowAdjustment #: static float (T)  
	DialogsHeaderAdjustment: float = Coat_CPP.AppOptions.DialogsHeaderAdjustment #: static float (T)  
	DialogsAdjustment: float = Coat_CPP.AppOptions.DialogsAdjustment #: static float (T)  
	DockDelimiterAdjustment: float = Coat_CPP.AppOptions.DockDelimiterAdjustment #: static float (T)  
	InputFieldAdjustment: float = Coat_CPP.AppOptions.InputFieldAdjustment #: static float (T)  
	LayersAdjustment: float = Coat_CPP.AppOptions.LayersAdjustment #: static float (T)  
	MenuAdjustment: float = Coat_CPP.AppOptions.MenuAdjustment #: static float (T)  
	MenuHighlightAdjustment: float = Coat_CPP.AppOptions.MenuHighlightAdjustment #: static float (T)  
	MenuDelimiterAdjustment: float = Coat_CPP.AppOptions.MenuDelimiterAdjustment #: static float (T)  
	QuickpanelButtonAdjustment: float = Coat_CPP.AppOptions.QuickpanelButtonAdjustment #: static float (T)  
	QuickpanelAdjustment: float = Coat_CPP.AppOptions.QuickpanelAdjustment #: static float (T)  
	ToolButtonsAdjustment: float = Coat_CPP.AppOptions.ToolButtonsAdjustment #: static float (T)  
	ToolsetButtonsAdjustment: float = Coat_CPP.AppOptions.ToolsetButtonsAdjustment #: static float (T)  
	ToolSelectButtonAdjustment: float = Coat_CPP.AppOptions.ToolSelectButtonAdjustment #: static float (T)  
	DockedAdjustment: float = Coat_CPP.AppOptions.DockedAdjustment #: static float (T)  
	UndockedAdjustment: float = Coat_CPP.AppOptions.UndockedAdjustment #: static float (T)  
	VoxtreeItemAdjustment: float = Coat_CPP.AppOptions.VoxtreeItemAdjustment #: static float (T)  
	VoxtreePlusAdjustment: float = Coat_CPP.AppOptions.VoxtreePlusAdjustment #: static float (T)  
	RenderExactViewsInPerspective: bool = Coat_CPP.AppOptions.RenderExactViewsInPerspective #: static bool (T)  Render front, back, left, right, top views in perspective. 
	AmountOfTurnableShots: int = Coat_CPP.AppOptions.AmountOfTurnableShots #: static int (T)  Amount of shots for the turnable rendering 
	AngleForTurnableShots: float = Coat_CPP.AppOptions.AngleForTurnableShots #: static float (T)  Angle over the horizon for the turnable rendering 
	UseMultiCore: bool = Coat_CPP.AppOptions.UseMultiCore #: static bool (T)  Use Multi-Core Optimization 
	UseMulticoreForSaving: bool = Coat_CPP.AppOptions.UseMulticoreForSaving #: static bool (T)  Use Multi-Core for Saving 
	UseMRT: bool = Coat_CPP.AppOptions.UseMRT #: static bool (T)  Use multiple render targets to speed up real time normal map updates 
	PickColorJustFromTheScreen: bool = Coat_CPP.AppOptions.PickColorJustFromTheScreen #: static bool (T)  Pick the color with the picker tool or hotkey (usually V) just from the screen not from objects or layers. 
	PickFromAllLayers: bool = Coat_CPP.AppOptions.PickFromAllLayers #: static bool (T)  If this option is checked, color will be chosen from all layers. Otherwise it will be chosen only from the current layer 
	PickDepthToo: bool = Coat_CPP.AppOptions.PickDepthToo #: static bool (T)  Pick depth with Sampler Tool when depth channel is enabled 
	PickFromCentralPoint: bool = Coat_CPP.AppOptions.PickFromCentralPoint #: static bool (T)  Pick color/depth/Glossiness from central point 
	ShowSoloMaterial: bool = Coat_CPP.AppOptions.ShowSoloMaterial #: static bool (T)  In this mode you can click somewhere and unhide all faces with the same material 
	WheelAction: int = Coat_CPP.AppOptions.WheelAction #: static int (T)  Select the parameter to change with the mouse wheel 
	CtrlWheelAction: int = Coat_CPP.AppOptions.CtrlWheelAction #: static int (T)  Select the parameter to change with CTRL+mouse wheel 
	ShiftWheelAction: int = Coat_CPP.AppOptions.ShiftWheelAction #: static int (T)  Select the parameter to change with SHIFT+mouse wheel 
	AltWheelAction: int = Coat_CPP.AppOptions.AltWheelAction #: static int (T)  Select the parameter to change with ALT+mouse wheel 
	WheelZoomPerspSpeed: float = Coat_CPP.AppOptions.WheelZoomPerspSpeed #: static float (T)  Wheel Zoom Perspective Speed 
	WheelZoomOrthoSpeed: float = Coat_CPP.AppOptions.WheelZoomOrthoSpeed #: static float (T)  Wheel Zoom Orthographic Speed 
	WheelZoomUVSpeed: float = Coat_CPP.AppOptions.WheelZoomUVSpeed #: static float (T)  Wheel Zoom UV Speed 
	UseShiftSnapping: bool = Coat_CPP.AppOptions.UseShiftSnapping #: static bool (T)  Use Shift Snapping_HINT 
	NormalmapExportType: int = Coat_CPP.AppOptions.NormalmapExportType #: static int (T)  Please select the default normal maps exporting options 
	RealtimePaddingMode: int = Coat_CPP.AppOptions.RealtimePaddingMode #: static int (T)  There are several methods for padding. First one linearly interpolates color between pixels from opposite island. Second one Takes nearest pixel from opposite island. Third one, the naive, takes nearest pixel from current island. 
	FillBordersMode: int = Coat_CPP.AppOptions.FillBordersMode #: static int (T)  When exporting textures you will be asked if you need a border around the texture clusters (padding). This option allows you to answer this question automatically 
	BorderEdgesWidth: int = Coat_CPP.AppOptions.BorderEdgesWidth #: static int (T)  Please select padding width 
	EditorPath: cPy.cTypes.cStr = Coat_CPP.AppOptions.EditorPath #: static cStr (T)  The path to your external graphics editor. This editor should support loading and saving files with the PSD extension 
	ScriptEditorPath: cPy.cTypes.cStr = Coat_CPP.AppOptions.ScriptEditorPath #: static cStr (T)  Please specify the external text editor. 
	MeshViewQuality: int = Coat_CPP.AppOptions.MeshViewQuality #: static int (T)  AppOptions::MeshViewQuality_HINT 
	PickerType: int = Coat_CPP.AppOptions.PickerType #: static int (T)  Use LMB to choose a color 
	PickColorMode: int = Coat_CPP.AppOptions.PickColorMode #: static int (T)  
	NearPlane: float = Coat_CPP.AppOptions.NearPlane #: static float (T)  Tweak the cameras near plane to be able to move closer to the surface 
	PivotType: int = Coat_CPP.AppOptions.PivotType #: static int (T)  Rotation pivot is current pick point on the object 
	SnappingMethod: int = Coat_CPP.AppOptions.SnappingMethod #: static int (T)  Snapping Method to be Used 
	HideScrollers: bool = Coat_CPP.AppOptions.HideScrollers #: static bool (T)  Hide Scrollers 
	DontUseStickyKeys: bool = Coat_CPP.AppOptions.DontUseStickyKeys #: static bool (T)  Disable the sticky keys mechanics 
	IconicUI: int = Coat_CPP.AppOptions.IconicUI #: static int (T)  
	MultiresScope: int = Coat_CPP.AppOptions.MultiresScope #: static int (T)  Please choose whether multiresolution acts over the current object, selected objects, or all visible objects. This simplifies multi-object multiresolution management. 
	NumProcessors: int = Coat_CPP.AppOptions.NumProcessors #: static int (T)  
	UsingProcessors: int = Coat_CPP.AppOptions.UsingProcessors #: static int (T)  
	PtexTextureSize: int = Coat_CPP.AppOptions.PtexTextureSize #: static int (T)  The size of textures that will be used to store PTEX quads. This size will be used for export if you export the PTEX model as regular model 
	FlipPtexQuads: bool = Coat_CPP.AppOptions.FlipPtexQuads #: static bool (T)  Flip ptex quads for better compatibility with Renderman 
	MillionsOfPolygons: float = Coat_CPP.AppOptions.MillionsOfPolygons #: static float (T)  Mesh resolution, in millions of polygons, after the mesh smoothing is applied during the loading. This amount should be greater than the number of pixels in the texture 
	TexSizeX: int = Coat_CPP.AppOptions.TexSizeX #: static int (T)  Texture width. If your video card has less than 256 megs of RAM you should avoid textures larger than 2000 x 2000 
	TexSizeY: int = Coat_CPP.AppOptions.TexSizeY #: static int (T)  Texture height. If your video card has less than 256 megs of RAM you should avoid textures larger than 2000 x 2000 
	ShowGrid2D: bool = Coat_CPP.AppOptions.ShowGrid2D #: static bool (T)  Show/Hide 2D Grid 
	SnapGrid2D: bool = Coat_CPP.AppOptions.SnapGrid2D #: static bool (T)  Snap the cursor to the grid 
	SnapOriginalVerts: bool = Coat_CPP.AppOptions.SnapOriginalVerts #: static bool (T)  Snap brush to low-poly mesh vertex positions 
	Grid2DSize: int = Coat_CPP.AppOptions.Grid2DSize #: static int (T)  Set the grid size in pixels 
	Grid2DSub: int = Coat_CPP.AppOptions.Grid2DSub #: static int (T)  This value represents the number of subdivisions in the screen grid. Use zero for none 
	Grid2DColor: int = Coat_CPP.AppOptions.Grid2DColor #: static DWORD (T)  Click the LMB here to change the 2D grid color 
	GreyOutBgInModalDialogs: bool = Coat_CPP.AppOptions.GreyOutBgInModalDialogs #: static bool (T)  Grey-out Background w/ Pop-Up Dialogs_HINT 
	GreyOutOpacity: float = Coat_CPP.AppOptions.GreyOutOpacity #: static float (T)  Grey-out Opacity reduces the opacity of the grey-out effect over the viewport, when a dialog pop-up appears 
	UseNaviLineForPages: bool = Coat_CPP.AppOptions.UseNaviLineForPages #: static bool (T)  Use Tabs instead of a Drop List to switch Workspaces. 
	OldStyleHotkeysInSpacePanel: bool = Coat_CPP.AppOptions.OldStyleHotkeysInSpacePanel #: static bool (T)  
	LightDirX: float = Coat_CPP.AppOptions.LightDirX #: static float (T)  
	LightDirY: float = Coat_CPP.AppOptions.LightDirY #: static float (T)  
	LightDirZ: float = Coat_CPP.AppOptions.LightDirZ #: static float (T)  
	LightContrast: float = Coat_CPP.AppOptions.LightContrast #: static float (T)  
	EnvMap: int = Coat_CPP.AppOptions.EnvMap #: static int (T)  
	LowShadersQuality: bool = Coat_CPP.AppOptions.LowShadersQuality #: static bool (T)  Select this option if you experience performance problems 
	MainColor: int = Coat_CPP.AppOptions.MainColor #: static DWORD (T)  
	BackColor: int = Coat_CPP.AppOptions.BackColor #: static DWORD (T)  
	ControlsIn3D: bool = Coat_CPP.AppOptions.ControlsIn3D #: static bool (T)  Use a 3D style for the buttons 
	ControlsWithGradient: bool = Coat_CPP.AppOptions.ControlsWithGradient #: static bool (T)  Use a gradient texture for menus and backgrounds 
	InverseVerticalZoom: bool = Coat_CPP.AppOptions.InverseVerticalZoom #: static bool (T)  Press ALT+LMB and slide the mouse upwards to zoom in the opposite direction 
	FontColor: int = Coat_CPP.AppOptions.FontColor #: static DWORD (T)  This color will be used for text and white icons, locks, and navigation controls 
	EditAreaColor: int = Coat_CPP.AppOptions.EditAreaColor #: static DWORD (T)  Edit Area Color 
	EditAreaBorderColor: int = Coat_CPP.AppOptions.EditAreaBorderColor #: static DWORD (T)  Edit Area Border Color 
	EditAreaBorderHighlightColor: int = Coat_CPP.AppOptions.EditAreaBorderHighlightColor #: static DWORD (T)  Edit Area Highlight Color 
	ActiveTabFontColor: int = Coat_CPP.AppOptions.ActiveTabFontColor #: static DWORD (T)  Active Tab Font Color 
	PassiveTabFontColor: int = Coat_CPP.AppOptions.PassiveTabFontColor #: static DWORD (T)  Passive Tab Font Color 
	PassiveTabColor: int = Coat_CPP.AppOptions.PassiveTabColor #: static DWORD (T)  Passive Tab Color 
	ActiveTabColor: int = Coat_CPP.AppOptions.ActiveTabColor #: static DWORD (T)  Active Tab Color 
	BackgroundTabColor: int = Coat_CPP.AppOptions.BackgroundTabColor #: static DWORD (T)  Tab Background Color 
	HeadersFontColor: int = Coat_CPP.AppOptions.HeadersFontColor #: static DWORD (T)  Use this color for the headers text 
	rtColorMode: int = Coat_CPP.AppOptions.rtColorMode #: static int (T)  
	rtNeedColorMode: int = Coat_CPP.AppOptions.rtNeedColorMode #: static int (T)  
	NeedLayersConvert: int = Coat_CPP.AppOptions.NeedLayersConvert #: static int (T)  
	PaintShaderType: int = Coat_CPP.AppOptions.PaintShaderType #: static int (T)  
	pPaintShaderType: int = Coat_CPP.AppOptions.pPaintShaderType #: static int (T)  
	BakeWithNamesCorrespondence: bool = Coat_CPP.AppOptions.BakeWithNamesCorrespondence #: static bool (T)  You may use this option to simplify Sculpt Object Baking if names of Retopo Objects correspond to Sculpt Object names. If you check the option each Retopo Object will be baked using only the Sculpt Object of same name and its children 
	ShowFocalShift: bool = Coat_CPP.AppOptions.ShowFocalShift #: static bool (T)  Show the 'Focal shift' slider in the top panel 
	ShowFalloff: bool = Coat_CPP.AppOptions.ShowFalloff #: static bool (T)  Show the 'Falloff' slider in the top panel 
	ShowThumbs: bool = Coat_CPP.AppOptions.ShowThumbs #: static bool (T)  Show Import Thumbnails on Start Page 
	ShowIThumbs: bool = Coat_CPP.AppOptions.ShowIThumbs #: static bool (T)  Show Interface Thumbnails on Start Page 
	DebugShadersMode: bool = Coat_CPP.AppOptions.DebugShadersMode #: static bool (T)  Shader debug mode allows you to see errors while shaders are compiling 
	StoreWindowState: bool = Coat_CPP.AppOptions.StoreWindowState #: static bool (T)  Store Window State 
	DontShowSurfaceHint: bool = Coat_CPP.AppOptions.DontShowSurfaceHint #: static bool (T)  Don't show this hint again 
	StorePenShapeForTools: bool = Coat_CPP.AppOptions.StorePenShapeForTools #: static bool (T)  Remember Brush/Strip For Every Tool 
	StorePenRadiusForTools: bool = Coat_CPP.AppOptions.StorePenRadiusForTools #: static bool (T)  Remember Own Brush Radius for Every Tool 
	PenSensivity: float = Coat_CPP.AppOptions.PenSensivity #: static float (T)  Brush sensitivity 
	PenPressureLevels: int = Coat_CPP.AppOptions.PenPressureLevels #: static int (T)  Please enter the number of pressure levels for your brush 
	Symmetry_point_opacity: float = Coat_CPP.AppOptions.Symmetry_point_opacity #: static float (T)  Symmetry Point Opacity 
	CamZoomSpeed: float = Coat_CPP.AppOptions.CamZoomSpeed #: static float (T)  Camera Zoom Speed 
	CamRotSpeed: float = Coat_CPP.AppOptions.CamRotSpeed #: static float (T)  Camera Rotation Speed 
	def ShouldSaveInShortForm(self) -> bool:
		pass # cpp source

	@staticmethod
	def SetupIslandsDistance():
		pass # cpp source

	@staticmethod
	def CheckAutosave() -> bool:
		pass # cpp source

	@staticmethod
	def PostponeAutosave():
		pass # cpp source

	def Read(self):
		pass # cpp source

	def Write(self, SaveLayout: bool = True, SavePresets: bool = True, SaveHotkeys: bool = True):
		pass # cpp source

	@staticmethod
	def getPos(wname: str) -> any:
		pass # cpp source

	@staticmethod
	def SaveColors():
		pass # cpp source

	@staticmethod
	def ReadColors():
		pass # cpp source

	@staticmethod
	def GetSliderState(ID: str, local: bool = False) -> any:
		pass # cpp source

	SymmSnapValue: float = Coat_CPP.AppOptions.SymmSnapValue #: static float (T)  
	UseOldNavAPI: bool = Coat_CPP.AppOptions.UseOldNavAPI #: static bool (T)  Use older version of 3D-Connexion API. It is not recommended because in some cases it may lead to additional lags if you use wireless devices (mouse, pen, keyboard). But if the new API does not work for you - please use older one. 
	ShowWorldCenter3DConnexion: bool = Coat_CPP.AppOptions.ShowWorldCenter3DConnexion #: static bool (T)  Show the pivot when you navigate 
	Use3DConnexionPivot: bool = Coat_CPP.AppOptions.Use3DConnexionPivot #: static bool (T)  Use the default 3DConnextion pivot picking algorithm - pick the pivot around the center of the viewport. 
	MovementSensitivity: float = Coat_CPP.AppOptions.MovementSensitivity #: static float (T)  Movement Sensitivity 
	ZoomModulator: float = Coat_CPP.AppOptions.ZoomModulator #: static float (T)  Zoom Speed Modulator 
	PanUDModulator: float = Coat_CPP.AppOptions.PanUDModulator #: static float (T)  Vertical Pan Modulator 
	PanRLModulator: float = Coat_CPP.AppOptions.PanRLModulator #: static float (T)  Horizontal Pan Modulator 
	RotationSensitivity: float = Coat_CPP.AppOptions.RotationSensitivity #: static float (T)  Rotation Sensitivity 
	SpinModulator: float = Coat_CPP.AppOptions.SpinModulator #: static float (T)  Spin Modulator 
	TiltModulator: float = Coat_CPP.AppOptions.TiltModulator #: static float (T)  Tilt Modulator 
	RollModulator: float = Coat_CPP.AppOptions.RollModulator #: static float (T)  Roll Modulator 
	OrthoZoomSpeed: float = Coat_CPP.AppOptions.OrthoZoomSpeed #: static float (T)  Orthographic mode zoom speed 
	OrthoPanSpeed: float = Coat_CPP.AppOptions.OrthoPanSpeed #: static float (T)  
	ObjectMovingSpeed3DM: float = Coat_CPP.AppOptions.ObjectMovingSpeed3DM #: static float (T)  The additional speed modulator for the translation when the object manipulation mode with the 3D-mouse turned on. 
	M3D_ActivationKey: int = Coat_CPP.AppOptions.M3D_ActivationKey #: static int (T)  Choose a key to activate the mode where you can change the radius, depth, opacity, and brush angle using a space mouse 
	PenIconSize: int = Coat_CPP.AppOptions.PenIconSize #: static int (T)  
	StripIconSize: int = Coat_CPP.AppOptions.StripIconSize #: static int (T)  
	MaskIconSize: int = Coat_CPP.AppOptions.MaskIconSize #: static int (T)  
	MtlIconSize: int = Coat_CPP.AppOptions.MtlIconSize #: static int (T)  
	ModelsIconSize: int = Coat_CPP.AppOptions.ModelsIconSize #: static int (T)  
	FacturesIconSize: int = Coat_CPP.AppOptions.FacturesIconSize #: static int (T)  
	PanIconSize: int = Coat_CPP.AppOptions.PanIconSize #: static int (T)  
	ScriptInfoType: int = Coat_CPP.AppOptions.ScriptInfoType #: static int (T)  When you press the RMB+MMB over the item in UI the code for scripting will be copied to the clipboard. This option allows to define what type of information will be copied there. 
	RotateAroundYAxis: bool = Coat_CPP.AppOptions.RotateAroundYAxis #: static bool (T)  Rotation will be constrained - space navigator will rotate around Y-axis in the same was as in standard navigation scheme 
	DisableRoll: bool = Coat_CPP.AppOptions.DisableRoll #: static bool (T)  Disable roll with 3D-Mouse. In many cases this is most convenient 
	RealtimeUVPreview: bool = Coat_CPP.AppOptions.RealtimeUVPreview #: static bool (T)  
	ZoomToVaryRadiusSensitivity: float = Coat_CPP.AppOptions.ZoomToVaryRadiusSensitivity #: static float (T)  Zoom to Radius Speed 
	UpDonToVaryDepthSensitivity: float = Coat_CPP.AppOptions.UpDonToVaryDepthSensitivity #: static float (T)  Vertical Pan to Depth Speed 
	RLToVaryTransparencySensitivity: float = Coat_CPP.AppOptions.RLToVaryTransparencySensitivity #: static float (T)  Horizontal Pan to Opacity Speed 
	SpinToVaryRotationSensitivity: float = Coat_CPP.AppOptions.SpinToVaryRotationSensitivity #: static float (T)  Spin to Rotation Speed 
	TiltToVaryFocalShiftSensitivity: float = Coat_CPP.AppOptions.TiltToVaryFocalShiftSensitivity #: static float (T)  Tilt to Focal Shift Speed 
	RollToVarySpecularSensitivity: float = Coat_CPP.AppOptions.RollToVarySpecularSensitivity #: static float (T)  Roll to Glossiness Speed 
	FreezeViewMode: int = Coat_CPP.AppOptions.FreezeViewMode #: static int (T)  Change the pattern used to indicate frozen areas 
	FreezePScrollSpeed: float = Coat_CPP.AppOptions.FreezePScrollSpeed #: static float (T)  Freeze pattern scroll speed. Change the pattern used to indicate frozen areas in the freeze menu 
	HidePenConstantlyInCapsMode: bool = Coat_CPP.AppOptions.HidePenConstantlyInCapsMode #: static bool (T)  If this option is checked brush will be hidden constantly in CAPS LOCK mode, otherwise it will be hidden only while drawing 
	HidePenConstantly: bool = Coat_CPP.AppOptions.HidePenConstantly #: static bool (T)  If this option is checked brush will be hidden when drawing 
	ShowPenShape: bool = Coat_CPP.AppOptions.ShowPenShape #: static bool (T)  Show Brush Curve 
	ShowPenAlpha: bool = Coat_CPP.AppOptions.ShowPenAlpha #: static bool (T)  Show Brush Alpha Texture 
	PenCircleColor: int = Coat_CPP.AppOptions.PenCircleColor #: static DWORD (T)  Brush Circle Color 
	PenShapeColor: int = Coat_CPP.AppOptions.PenShapeColor #: static DWORD (T)  Color of the brush curve. This color will be used for the dot in CAPS LOCK mode 
	PenShapeColorWithCTRL: int = Coat_CPP.AppOptions.PenShapeColorWithCTRL #: static DWORD (T)  Brush Curve Color w/ CTRL 
	PenShapeColorWithSHIFT: int = Coat_CPP.AppOptions.PenShapeColorWithSHIFT #: static DWORD (T)  Brush Curve Color w/ SHIFT 
	ShowCentralSpotInCapsMode: bool = Coat_CPP.AppOptions.ShowCentralSpotInCapsMode #: static bool (T)  Show Cental Dot in CAPS Mode While Drawing 
	PickVertMode: int = Coat_CPP.AppOptions.PickVertMode #: static int (T)  
	TopologicalPaintConstraints: bool = Coat_CPP.AppOptions.TopologicalPaintConstraints #: static bool (T)  Paint only in the topologically connective areas. Otherwise, paint tools act over the volumetric sphere. 
	MessageAbovePen: int = Coat_CPP.AppOptions.MessageAbovePen #: static int (T)  Message Above Brush 
	MessageBelowPen: int = Coat_CPP.AppOptions.MessageBelowPen #: static int (T)  Message Below Brush 
	MessagesColor: int = Coat_CPP.AppOptions.MessagesColor #: static DWORD (T)  Color of the messages below or above the brush 
	EdgeLoopFriendlyQuadrangulation: bool = Coat_CPP.AppOptions.EdgeLoopFriendlyQuadrangulation #: static bool (T)  In this case another method of quadrangulation will be used to get nice edgeloops. It is more time consuming 
	SteamApp: bool = Coat_CPP.AppOptions.SteamApp #: static bool (T)  
	ItemtestPath: cPy.cTypes.cStr = Coat_CPP.AppOptions.ItemtestPath #: static cStr (T)  
	SelectEdgesWhenFacesDeleted: bool = Coat_CPP.AppOptions.SelectEdgesWhenFacesDeleted #: static bool (T)  When you delete selected faces the bounding edges will be selected. Turn it off if you don't need edges selection. 
	AutoJoinCurvesEnds: bool = Coat_CPP.AppOptions.AutoJoinCurvesEnds #: static bool (T)  If you start new curve and click on the first or last point of an existing curve the curve will be extended with new points. Uncheck if you need to start new curve even if new point matches existing one exactly. 
	MoveOnlySlectedGroupFaces: bool = Coat_CPP.AppOptions.MoveOnlySlectedGroupFaces #: static bool (T)  
	SmoothJustOnce: bool = Coat_CPP.AppOptions.SmoothJustOnce #: static bool (T)  If this option turned ON the "Smooth all" dialog will not appear. Smoothing will be performed just once. 
	SpineToolOnlySplineMode: bool = Coat_CPP.AppOptions.SpineToolOnlySplineMode #: static bool (T)  
	UseRGBCavityByDefault: bool = Coat_CPP.AppOptions.UseRGBCavityByDefault #: static bool (T)  RGB Curvature is a multi-range Curvature texture map, where each channel corresponds to a different cavity scale. B is the local cavity, G is a middle-range cavity, R is the far-range cavity. 
	AutoExtrudeFaceByDefault: bool = Coat_CPP.AppOptions.AutoExtrudeFaceByDefault #: static bool (T)  Extrude auto commit after new Selection 
	SmartExtrudeConstSelection: bool = Coat_CPP.AppOptions.SmartExtrudeConstSelection #: static bool (T)  Selection enable all time 
	HideGizmoIfShiftPressed: bool = Coat_CPP.AppOptions.HideGizmoIfShiftPressed #: static bool (T)  Hide Gizmo w/ CTRL/SHIFT Hotkeys in the Retopo/Modeling Room, via the Select & Transform tool 
	ShowDensityNearVolumes: bool = Coat_CPP.AppOptions.ShowDensityNearVolumes #: static bool (T)  Show Density near the Volume's Name 
	ShowPolycountNearVolumes: bool = Coat_CPP.AppOptions.ShowPolycountNearVolumes #: static bool (T)  Show Polycount near the Volume's Name 
	RelaxSharpEdges: bool = Coat_CPP.AppOptions.RelaxSharpEdges #: static bool (T)  Moving or not the "Sharp Edges" during Relaxing 
	CentralRectExpansion: bool = Coat_CPP.AppOptions.CentralRectExpansion #: static bool (T)  Expand the rectangle, square, or shape from the center. 
	PanM: cPy.cTypes.cMat3 #: cMat3 (T)  
	WPanM: cPy.cTypes.cMat3 #: cMat3 (T)  
	@staticmethod
	def GetToolPreset(Name: str) -> OneToolPreset:
		pass # cpp source

	@staticmethod
	def FindToolPreset(Name: str) -> OneToolPreset:
		pass # cpp source

	@staticmethod
	def RemoveToolPreset(Name: str):
		pass # cpp source

	@staticmethod
	def ActivateToolPreset(Name: str):
		pass # cpp source

	@staticmethod
	def StoreToolPreset(Name: str):
		pass # cpp source

	@staticmethod
	def ChangeSoftwarePreset():
		pass # cpp source

	def AddFileToRecent(self, name: str):
		pass # cpp source

	def RestoreOptions(self):
		pass # cpp source

	SaveMask: int = Coat_CPP.AppOptions.SaveMask #: static int (T)  
	def GetClassMask(self) -> int:
		pass # cpp source

