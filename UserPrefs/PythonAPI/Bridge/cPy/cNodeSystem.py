from __future__ import annotations
import cPy.cTypes
import cPy.cList
import cPy.ClassArray
import cPy.cCore
#cNodeSystem
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class NodeGraph(cPy.cCore.BaseClass):
	'''
			
		
		
	'''


	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->NodeGraph:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NodeGraph class or its descendant, and if so, returns the specified object, but of the NodeGraph type.
		'''
		pass # cpp source

	Category: cPy.cTypes.cStr #: cStr (T)  
	Folder: cPy.cTypes.cStr #: cStr (T)  
	Name: cPy.cTypes.cStr #: cStr (T)  
	LayerName: cPy.cTypes.cStr #: cStr (T)  
	KeepIconsFBO: bool = Coat_CPP.NodeGraph.KeepIconsFBO #: static bool (T)  
	OpenGLInitialized: bool = Coat_CPP.NodeGraph.OpenGLInitialized #: static bool (T)  
	UVFilter: cPy.cList.cList_int #: cList_int (T)  
	previewRender: any #: NGPresetsPreviewer (T)  
	ndHash: int #: DWORD (T)  
	ndHashOffset: int #: DWORD (T)  
	NeedMakeScript: bool #: bool (T)  
	NeedRefreshResult: bool #: bool (T)  
	HasCompileError: bool #: bool (T)  
	CompileLog: cPy.cTypes.cStr #: cStr (T)  
	RampListTexture: any #: comms :: cImage (T)  
	RampListGLTexture: int #: int (T)  
	def RenderPreview(self, node: any):
		pass # cpp source

	def __init__(self, _0: any, AutoDestroy: bool):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Clear(self):
		pass # cpp source

	def SetCanvas(self, _0: any, AutoDestroy: bool):
		pass # cpp source

	def GetCanvas(self) -> any:
		pass # cpp source

	NodeGraphInEditor: NodeGraph = Coat_CPP.NodeGraph.NodeGraphInEditor #: static NodeGraph * (T)  
	NodeAllowGizmo: bool = Coat_CPP.NodeGraph.NodeAllowGizmo #: static bool (T)  
	GlobalPropertyVisibilityLevel: int = Coat_CPP.NodeGraph.GlobalPropertyVisibilityLevel #: static int (T)  
	BuildTimeKnotId: int = Coat_CPP.NodeGraph.BuildTimeKnotId #: static int (T)  
	LMB: bool #: bool (T)  
	sLMB: bool = Coat_CPP.NodeGraph.sLMB #: static bool (T)  
	HasAlbedoOut: bool #: bool (T)  
	HasMetalOut: bool #: bool (T)  
	HasNormalOut: bool #: bool (T)  
	HasGlossOut: bool #: bool (T)  
	HasDisplacementOut: bool #: bool (T)  
	HasPositionOut: bool #: bool (T)  
	HasReflectionColorOut: bool #: bool (T)  
	HasEmissiveOut: bool #: bool (T)  
	HasOpacityOut: bool #: bool (T)  
	HasCavityOut: bool #: bool (T)  
	HasOcclusionOut: bool #: bool (T)  
	HasBugleOut: bool #: bool (T)  
	Nodes: cPy.ClassArray.ClassArray_BaseNode #: ClassArray_BaseNode (T)  nodes and knots in scene 
	LayersList: any #: comms :: cList<NodeGraph *>(T)  
	PropertiesHash: int #: int (T)  
	PropertiesHashShift: int #: int (T)  
	CodeNodeDefine: cPy.cTypes.cStr #: cStr (T)  
	iNodeCode: cPy.cTypes.cStr #: cStr (T)  
	iUsedFunctionsCode: cPy.cTypes.cStr #: cStr (T)  
	isActive: bool #: bool (T)  
	SkipValidator: bool = Coat_CPP.NodeGraph.SkipValidator #: static bool (T)  
	isAnyActive: bool = Coat_CPP.NodeGraph.isAnyActive #: static bool (T)  
	isAVUsed: bool #: bool (T)  
	UsedCavity: bool #: bool (T)  
	UsedAO: bool #: bool (T)  
	OutArrays: dict[cPy.cTypes.cStr, int] #: std :: map<cStr, int>(T)  
	ComputeShaderID: int #: int (T)  index of defined texture(FBO) by array define name 
	NeedRecenterNodes: bool #: bool (T)  
	NeedCheckAOCavity: bool #: bool (T)  
	def ReCenterNodes(self):
		pass # cpp source

	def RefreshResult(self):
		pass # cpp source

	def EditNodes(self):
		pass # cpp source

	def MakeScript(self):
		pass # cpp source

	def InsertKnotNamesToScript(self, aScript: cPy.cTypes.cStr) -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def GetDefaultVarsCode() -> cPy.cTypes.cStr:
		pass # cpp source

	NodeSystemHashOffset: int #: int (T)  
	ShaderVarHashOffset: int #: int (T)  
	def GetNodeSystemHash(self) -> int:
		pass # cpp source

	def GetShaderVarsHash(self) -> int:
		pass # cpp source

	def BuildRampListTexture(self):
		pass # cpp source

	def FindElement(self, point: cPy.cTypes.cVec2, res: any, find_in_knots: bool, find_out_knots: bool, findnodes: bool, exceptcaptured: bool, Type: any = None) -> bool:
		pass # cpp source

	def HandleFlyingKnots(self):
		pass # cpp source

	def ClearSelected(self):
		pass # cpp source

	def FindKnot(self, id: str) -> any:
		pass # cpp source

	def NumSelectedNodes(self) -> int:
		pass # cpp source

	def BuildAllLayersNodeList(self):
		pass # cpp source

	def OnLmbDown(self) -> bool:
		pass # cpp source

	def OnLmbUp(self) -> bool:
		pass # cpp source

	def OnRmbDown(self) -> bool:
		pass # cpp source

	def OnRmbUp(self) -> bool:
		pass # cpp source

	def OnMmbDown(self) -> bool:
		pass # cpp source

	def OnMmbUp(self) -> bool:
		pass # cpp source

	def OnKey(self) -> bool:
		pass # cpp source

	def OnDblClick(self) -> bool:
		pass # cpp source

	def OnWheel(self) -> bool:
		pass # cpp source

	BreakRender: bool #: bool (T)  
	def Render(self):
		pass # cpp source

	def Process(self):
		pass # cpp source

	def CreateUI(self, Rect: any) -> any:
		'''
			
		void CreateDefaultCategories();
		
		'''
		pass # cpp source

	def OnCreateControlFromScratch(self, Context: any, Rect: any) -> any:
		pass # cpp source

	def NodeIdByOutUniqueName(self, aUniqueName: cPy.cTypes.cStr) -> int:
		pass # cpp source

	def CalcPropertyHash(self) -> int:
		pass # cpp source

	def MakeNodeCode(self, aCodeLang: any, aNodeCode: cPy.cTypes.cStr, aUsedFunctionsCode: cPy.cTypes.cStr):
		pass # cpp source

	def WriteToLog(self, aCodeLang: any):
		pass # cpp source

	def ComputeRender(self):
		pass # cpp source

	def DefineTexture(self, texture_name: str, texture_id: int) -> bool:
		pass # cpp source

	nodeAllowGizmo: bool #: bool (T)  
	def SetupReferences(self, AllLayers: bool = True):
		pass # cpp source

	def MadeUniqNodeName(self, node_name: cPy.cTypes.cStr, exclude_node: any) -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def System() -> NodeGraph:
		'''
			
		extract NodeGraph from curent UI context - should be called within any UI callback
		
		'''
		pass # cpp source

	@staticmethod
	def Node(pos: cPy.cTypes.cVec2) -> any:
		'''
			
		extract BaseNode from curent UI context - should be called within any UI callback
		
		'''
		pass # cpp source

	def RemoveNode(self, n: any):
		'''
			
		void AddNodesCategory(const char* n);
		
		'''
		pass # cpp source

	def NodesAffectResult(self, aIONodeName: cPy.cTypes.cStr = "") -> bool:
		pass # cpp source

	def Save(self, xml: any, ClassPtr: any, Extra: any):
		pass # cpp source

	def Load(self, xml: any, ClassPtr: any, Extra: any) -> bool:
		pass # cpp source

	def CheckDirectCasting(self) -> bool:
		pass # cpp source

	def Drop(self):
		pass # cpp source

	def DuplicateSelected(self, Shift: bool):
		pass # cpp source

	def DeleteIfNeed(self):
		pass # cpp source

	def DeleteSelected(self):
		pass # cpp source

	def ToggleDisabled(self):
		pass # cpp source

	def LoadNGLFile(self, file_name: str, node_name: str) -> bool:
		pass # cpp source

	def LoadFromFile(self, file_name: str) -> bool:
		pass # cpp source

	def SaveToFile(self, file_name: str) -> bool:
		pass # cpp source

	def IgnoreAllErrors(self):
		pass # cpp source

	def Rebuild(self) -> int:
		pass # cpp source

	def SetProperty(self, node_name: str, property_name: str, value: float, value_2: float = 0, value_3: float = 0, value_4: float = 0) -> int:
		pass # cpp source

	def WriteResultScriptToLog(self) -> int:
		pass # cpp source



class BaseNode(cPy.cCore.BaseClass):
	'''
			
		
		
	'''


	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->BaseNode:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a BaseNode class or its descendant, and if so, returns the specified object, but of the BaseNode type.
		'''
		pass # cpp source

	NodeTypes: dict[str, BaseNode] = Coat_CPP.BaseNode.NodeTypes #: static std :: map<std :: string, BaseNode *>(T)  
	@staticmethod
	def RegNodeType(node_path: str, node_sample: BaseNode):
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self) -> any:
		pass # CPP source

	ShowPreview: bool #: bool (T)  
	ShowInObjectInspector: bool #: bool (T)  
	NodeGraphLayerIdx: int #: int (T)  
	NGLSrcPropertiesHash: int #: int (T)  
	DefinesHash: int #: int (T)  
	SourceRevisionID: int #: int (T)  
	def CalcPropertyHash(self) -> int:
		pass # cpp source

	AllowSubNodes: bool #: bool (T)  
	def SubNodes(self) -> any:
		pass # cpp source

	ParentNodeSystem: NodeGraph #: NodeGraph * (T)  
	NGLNodeReference: any #: NGLNodeSourceResult * (T)  
	NodeFilePath: cPy.cTypes.cStr #: cStr (T)  Node source file path (NGL for materials) 
	UICompilerMessage: cPy.cTypes.cStr #: cStr (T)  An error or warning message for a node 
	UICompilerERROR: bool #: bool (T)  An error or warning message for a node 
	NodeIdx: int #: int (T)  position on local space of the canvas 
	Position: any #: Rct (T)  
	NeedDelete: bool #: bool (T)  
	Selected: bool #: bool (T)  
	Disabled: bool #: bool (T)  disabled, should not be used incalculations 
	Captured: bool #: bool (T)  the node is catured to be draged 
	TextWithShadow: bool #: bool (T)  Draw txt with shadows 
	ShowKnotsNames: bool #: bool (T)  Display knots names in UI 
	LoadSaveExtension: cPy.cTypes.cStr #: cStr (T)  set extension there if you need Load/Save botton in node editor triggered by doubleclick 
	WithoutHeader: bool #: bool (T)  optional feature - node without header 
	CentralImage: int #: int (T)  central image over the node, -1 means no image 
	CentralImageIsFBO: bool #: bool (T)  
	CentralImagePreviewHash: int #: DWORD (T)  
	IconStyle: bool #: bool (T)  wrap central image to the whole node 
	WrapCentralImage: bool #: bool (T)  wrap central image to the whole node 
	ImageSize: cPy.cTypes.cVec2 #: cVec2 (T)  if ImageSize 
	Color: int #: DWORD (T)  color of the node below the header 
	HeaderColor: int #: DWORD (T)  color of the header 
	CommentColor: int #: DWORD (T)  
	NodesDistance: int #: int (T)  vertical distance between the knots 
	TypeName: cPy.cTypes.cStr #: cStr (T)  Text in the node header, this is also listed in RMB menu. You may change it after adding node to the scene. 
	NodeName: cPy.cTypes.cStr #: cStr (T)  
	NodeUIName: cPy.cTypes.cStr #: cStr (T)  
	Comment: cPy.cTypes.cStr #: cStr (T)  
	Subcategory: cPy.cTypes.cStr #: cStr (T)  category of the node for the RMB menu 
	Text: cPy.cTypes.cStr #: cStr (T)  text drawn within the node 
	HelperText: cPy.cTypes.cStr #: cStr (T)  The ID used in editor of the node (if available) as desciption text in the message box. Should be filled in the constructor. 
	In: cPy.ClassArray.ClassArray_knProperty #: ClassArray_knProperty (T)  input connections 
	Out: cPy.ClassArray.ClassArray_knProperty #: ClassArray_knProperty (T)  output connections 
	def GetInProperty(self, aPropertyName: cPy.cTypes.cStr) -> any:
		pass # cpp source

	def GetOutProperty(self, aPropertyName: cPy.cTypes.cStr) -> any:
		pass # cpp source

	def FixNodeName(self):
		pass # cpp source

	def SetupInPointers(self):
		pass # cpp source

	def SetupInNamesByPointers(self):
		pass # cpp source

	def SetInKnot(self, aPropertyName: cPy.cTypes.cStr, aKnot: any) -> bool:
		pass # cpp source

	def SetInProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: cPy.cTypes.cVec4) -> bool:
		pass # cpp source

	def SetOutProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: cPy.cTypes.cVec4, aCreatePropety: bool = False) -> bool:
		pass # cpp source

	def SetInProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: cPy.cTypes.cVec3) -> bool:
		pass # cpp source

	def SetOutProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: cPy.cTypes.cVec3, aCreatePropety: bool = False) -> bool:
		pass # cpp source

	def SetInProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: any) -> bool:
		pass # cpp source

	def SetOutProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: any, aCreatePropety: bool = False) -> bool:
		pass # cpp source

	def SetInProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: float) -> bool:
		pass # cpp source

	def SetOutProperty(self, aPropertyName: cPy.cTypes.cStr, aKnaValueot: float, aCreatePropety: bool = False) -> bool:
		pass # cpp source

	def SetInProperty(self, aPropertyName: cPy.cTypes.cStr, aValue: any) -> bool:
		pass # cpp source

	def SetDefine(self, aDefineName: cPy.cTypes.cStr, aValue: int) -> bool:
		pass # cpp source

	def SetStringDefine(self, aDefineName: cPy.cTypes.cStr, aValue: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	UserDefines: any #: NodeNGLUserDefines (T)  Values of Defines that have been set by the user for this node. 
	def GetInVarType(self, aInId: int) -> cPy.cTypes.cStr:
		pass # cpp source

	def GetOutVarType(self, aOutId: int) -> cPy.cTypes.cStr:
		pass # cpp source

	def NodeSource(self) -> any:
		'''
			
		Render node itself.
		
		'''
		pass # cpp source

	def UpdatePropertiesByNodeType(self):
		pass # cpp source

	def OnProcess(self):
		'''
			
		Render node itself.
		
		'''
		pass # cpp source

	def Render(self, canvas: any):
		'''
			
		Render node itself.
		
		'''
		pass # cpp source

	def RenderCurve(self, canvas: any, p0: cPy.cTypes.cVec2, p1: cPy.cTypes.cVec2, p2: cPy.cTypes.cVec2, p3: cPy.cTypes.cVec2, aColor: int = 044):
		'''
			
		render in/out links for the node
		
		'''
		pass # cpp source

	def RenderLink(self, canvas: any, p0: cPy.cTypes.cVec2, p1: cPy.cTypes.cVec2, aOffset: float, aOffset2: float, aColor: int = 044):
		pass # cpp source

	def RenderLinks(self, canvas: any):
		pass # cpp source

	def EditContent(self, show: bool) -> bool:
		'''
			
		show editor if show == true. Othervice return true if editor available
		
		'''
		pass # cpp source

	def EditClass(self, bc: cPy.cCore.BaseClass):
		'''
			
		by default, EditContent just calls EditClass(this)
		
		'''
		pass # cpp source

	def GetDimensions(self, canvas: any) -> cPy.cTypes.cVec3:
		'''
			
		return cVec3(width, header_height,bottom_height)
		
		'''
		pass # cpp source

	def SetLook(self, canvas: any, WithHeader: bool, Semitransparent: bool):
		'''
			
		set style of the node. It is better to call it in each Render cycle as first command.
		
		'''
		pass # cpp source

	def GetUsedFunctions(self, aFuncCode: cPy.cTypes.cStr, aCodeLang: any, aRevisionId: int):
		'''
			
		virtual void CheckTypes();
		
		'''
		pass # cpp source

	def MakeCode(self, aCode: cPy.cTypes.cStr, aCodeLang: any):
		pass # cpp source

	def GetShaderVarHash(self) -> int:
		pass # cpp source

	def GetVarIdsInShader(self, aShaderIdx: int, aOutIds: int):
		pass # cpp source

	def SetShaderVars(self, aShaderIdx: int, aVarIds: int):
		'''
			
		 Set var value in result shader
		
		'''
		pass # cpp source

	def ImpactToNodeSystem(self, aNodeSystem: NodeGraph):
		'''
			
		 Make changes in parent NodeSystem if need
		
		'''
		pass # cpp source

	def findNodeInPrevs(self, pNode: BaseNode) -> bool:
		pass # cpp source

	def getFirstInKnotVarType(self, aCodeLang: any) -> cPy.cTypes.cStr:
		pass # cpp source

	def IN_K(self, aInKnotID: int) -> cPy.cTypes.cStr:
		pass # cpp source

	def OUT_K(self, aOutKnotID: int) -> cPy.cTypes.cStr:
		pass # cpp source

	def SetupKnotsUsage(self):
		pass # cpp source

	def Save(self, xml: any, ClassPtr: any = None, Extra: any = None):
		pass # cpp source

	def Load(self, xml: any, ClassPtr: any = None, Extra: any = None) -> bool:
		pass # cpp source

	def LoadBody(self, xml: any, ClassPtr: any = None, Extra: any = None) -> bool:
		pass # cpp source



class ndNGLNode(BaseNode):

	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->ndNGLNode:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a ndNGLNode class or its descendant, and if so, returns the specified object, but of the ndNGLNode type.
		'''
		pass # cpp source

	NeedSecondBuild: bool #: bool (T)  
	def NodeSource(self) -> any:
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def GetUsedFunctions(self, aFuncCode: cPy.cTypes.cStr, aCodeLang: any, aRevisionId: int):
		pass # cpp source

	def MakeCode(self, aCode: cPy.cTypes.cStr, aCodeLang: any):
		pass # cpp source

	def PreprocessCurves(self, aCode: cPy.cTypes.cStr):
		pass # cpp source

	def Render(self, canvas: any):
		pass # cpp source

	def OnProcess(self):
		pass # cpp source

	@staticmethod
	def GetSourceByFilePath(aFilePath: cPy.cTypes.cStr, aUserDefines: any, aNodeIdx: int) -> any:
		pass # cpp source

	@staticmethod
	def LoadAllNodesFromFiles():
		pass # cpp source

	def GetClassMask(self) -> int:
		pass # cpp source

	def UpdatePropertiesByNodeType(self):
		pass # cpp source

	def LoadFromFile(self):
		pass # cpp source

	def LoadFromFilePath(self, aFileName: cPy.cTypes.cStr):
		pass # cpp source

	def AddCustomProperty(self):
		pass # cpp source

	def EditSource(self):
		pass # cpp source

	def SaveFile(self):
		pass # cpp source

	def SaveAs(self):
		pass # cpp source



class BaseKnot(cPy.cCore.BaseClass):
	'''
			
		
		
	'''


	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->BaseKnot:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a BaseKnot class or its descendant, and if so, returns the specified object, but of the BaseKnot type.
		'''
		pass # cpp source

	CurrentOIPaddingCount: int #: int (T)  
	def __init__(self):
		pass # CPP source

	Image: int #: int (T)  
	isInputKnot: bool #: bool (T)  
	HiddenWOKnot: bool #: bool (T)  
	Captured: bool #: bool (T)  
	HasConnection: bool #: bool (T)  
	AllowEditKnotColor: bool #: bool (T)  
	KnotUsage: int #: int (T)  
	Position: cPy.cTypes.cVec2 #: cVec2 (T)  0 - free knot, 1 - in-knot, 2 - out-knot 
	KnotName: cPy.cTypes.cStr #: cStr (T)  
	KnotUIName: cPy.cTypes.cStr #: cStr (T)  
	CustomUIName: cPy.cTypes.cStr #: cStr (T)  
	UniqueName: cPy.cTypes.cStr #: cStr (T)  
	Color: int #: DWORD (T)  
	PropertyType: any #: knPropertyType (T)  
	CodeFuncAttrType: cPy.cTypes.cStr #: cStr (T)  0 - no default value; 1 - Float; 2 - Vector2D; 3 - Vector3D; 4 - Vector4D; 5 - Color; 
	ParentNode: BaseNode #: BaseNode * (T)  
	InNodeName: cPy.cTypes.cStr #: cStr (T)  each knot may have one input connection 
	InKnotName: cPy.cTypes.cStr #: cStr (T)  
	PInConnection: any #: knProperty * (T)  
	def SetInConnection(self, aInConnection: any):
		pass # cpp source

	def CompatibleWithOutput(self, InKnot: BaseKnot) -> bool:
		'''
			
		check if knot may accept this type of output knots, no need to override it if you written own MayBeCastedTo function
		
		'''
		pass # cpp source

	def CompatibleWithInput(self, OutKnot: BaseKnot) -> bool:
		'''
			
		check if knot may accept this type of input knots, no need to override it if you written own MayBeCastedTo function
		
		'''
		pass # cpp source

	def CastTo(self, type: str) -> bool:
		'''
			
		try to cast this knot to the specified type, returns true if successfull. If empty string passed the node should be untyped if it is allowed
		
		'''
		pass # cpp source

	def MayBeCastedTo(self, aKnot: BaseKnot) -> bool:
		'''
			
		check if this type may be casted to type
		
		'''
		pass # cpp source

	def StrictlyTyped(self) -> bool:
		'''
			
		return false if this knot may be casted to other types in general
		
		'''
		pass # cpp source

	def AlreadyTyped(self) -> bool:
		'''
			
		return true if knot already casted to some defined type
		
		'''
		pass # cpp source

	def RemoveLink(self):
		pass # cpp source

	def Render(self, canvas: any):
		pass # cpp source

	def Process(self):
		pass # cpp source



class knProperty(BaseKnot):

	@staticmethod
	def dynamic_cast(pObject : cPy.cCore.BaseClass)->knProperty:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a knProperty class or its descendant, and if so, returns the specified object, but of the knProperty type.
		'''
		pass # cpp source

	PropertyIdx: int #: int (T)  
	NodeSystemRampIdx: int #: int (T)  
	isOutProperty: bool #: bool (T)  
	CustomProperty: bool #: bool (T)  
	inlineExpression: bool #: bool (T)  
	AllowCurve: bool #: bool (T)  
	AllowDefineTexture: bool #: bool (T)  
	Invert: bool #: bool (T)  
	IsExpandedInOI: int #: int (T)  
	VisLevel: int #: int (T)  
	CodeFuncAttrID: int #: int (T)  For whom to show this attribute (for everyone, favorite, for experts or hide) 
	ElementCount: int #: int (T)  
	ShowCurveUI: bool #: bool (T)  
	CustomExpression: bool #: bool (T)  
	def SetInConnection(self, aInConnection: knProperty):
		pass # cpp source

	def GetV4(self) -> cPy.cTypes.cVec4:
		'''
			
		knPropertyType PropertyType = ptDefault; // 0 - no default value; 1 - Float; 2 - Vector2D; 3 - Vector3D; 4 - Vector4D; 5 - Color;
		
		'''
		pass # cpp source

	Deform: any #: PropertyRamp (T)  
	spHash: int #: DWORD (T)  
	legacy: cPy.cTypes.cStr #: cStr (T)  
	Expression: any #: ndNGLNodeSource (T)  
	UserDefines: any #: NodeNGLUserDefines (T)  
	DefKnot: cPy.cTypes.cStr #: cStr (T)  
	DefaultMin: float #: float (T)  
	DefaultMax: float #: float (T)  
	def __init__(self):
		pass # CPP source

	def __init__(self, _0: str, aResultType: any, CL: int = 00000):
		pass # CPP source

	def __init__(self, CL: int, _1: str, aDefaultValue: float, aMin: float = 0, aMax: float = 10, aKnot: cPy.cTypes.cStr = "", aAllowCurves: bool = False, aAllowDefineTexture: bool = False):
		pass # CPP source

	def __init__(self, CL: int, _1: str, aDefaultValue: any, aKnot: cPy.cTypes.cStr = "", aAllowCurves: bool = False, aAllowDefineTexture: bool = False):
		pass # CPP source

	def __init__(self, CL: int, _1: str, aDefaultValue: any, aMin: float = 0, aMax: float = 10, aKnot: cPy.cTypes.cStr = "", aAllowCurves: bool = False, aAllowDefineTexture: bool = False):
		pass # CPP source

	def __init__(self, CL: int, _1: str, aDefaultValue: cPy.cTypes.cVec3, aMin: float = 0, aMax: float = 10, aKnot: cPy.cTypes.cStr = "", aAllowCurves: bool = False, aAllowDefineTexture: bool = False):
		pass # CPP source

	def __init__(self, CL: int, _1: str, aDefaultValue: cPy.cTypes.cVec4, aMin: float = 0, aMax: float = 10, aKnot: cPy.cTypes.cStr = "", aAllowCurves: bool = False, aAllowDefineTexture: bool = False):
		pass # CPP source

	def CopyTypeTo(self, aDst: knProperty):
		pass # cpp source

	def UpdateTypeTo(self, aDst: knProperty):
		pass # cpp source

	def Process(self):
		pass # cpp source

	def Render(self, canvas: any):
		pass # cpp source

	def MakeCode(self, aCode: cPy.cTypes.cStr, aCodeLang: any):
		pass # cpp source

	def GetUsedFunctions(self, aFuncCode: cPy.cTypes.cStr, aCodeLang: any):
		pass # cpp source

	def GetUsedGlobalVars(self, aGVarsCode: cPy.cTypes.cStr, aCodeLang: any):
		pass # cpp source

	def SetShaderAttr(self, aShaderId: int, aShaderVarId: int):
		pass # cpp source

	def EditExpression(self):
		pass # cpp source

	def RemoveProperty(self):
		pass # cpp source

	def EditProperty(self):
		pass # cpp source

	def EditCurve(self):
		pass # cpp source

	def ToggleInvert(self):
		pass # cpp source

	def LoadTexture(self):
		pass # cpp source

	def ChangeVisibilityLevel(self):
		pass # cpp source

	def OpenInOI(self):
		pass # cpp source

	def OpenOnClickOI(self):
		pass # cpp source

	def MayBeCastedTo(self, aKnot: BaseKnot) -> bool:
		pass # cpp source

	def Save(self, xml: any, ClassPtr: any = None, Extra: any = None):
		pass # cpp source

	def Load(self, xml: any, ClassPtr: any = None, Extra: any = None) -> bool:
		pass # cpp source

	def GetClassMask(self) -> int:
		pass # cpp source

