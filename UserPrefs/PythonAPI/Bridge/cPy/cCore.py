from __future__ import annotations
import cPy.cTypes
#cCore
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class BaseClass():
	'''
			
		Use this class for build a class for UI or serialization.
		see class_reg.h for details about the class registration
		
	'''

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

	def OnCreateControlFromScratch(self, Context: any, Rect: any) -> any:
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
	def Rect(rect: any):
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

