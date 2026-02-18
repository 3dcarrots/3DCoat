from typing import Any
from enum import Enum
class FieldClamp(Enum):
	fcWrap = ...
	fcClamp = ...
	fcZero = ...
class image_format(Enum):
	fmtNone = ...
	R8 = ...
	Rg8 = ...
	Rgb8 = ...
	Rgba8 = ...
	R16 = ...
	Rg16 = ...
	Rgb16 = ...
	Rgba16 = ...
	R16f = ...
	Rg16f = ...
	Rgb16f = ...
	Rgba16f = ...
	R32f = ...
	Rg32f = ...
	Rgb32f = ...
	Rgba32f = ...
	Depth16 = ...
	Depth24 = ...
	Depth24Stencil8 = ...
	Dxt1 = ...
	Dxt3 = ...
	Dxt5 = ...
	PVRTC4 = ...
	PVRTC4_Alpha = ...
	Count = ...
class BoolOpType(Enum):
	BOOL_MERGE = ...
	BOOL_ADD = ...
	BOOL_SUBTRACT = ...
	BOOL_INTERSECT = ...
def start_main_menu(id: str) :
	'''
	strat the main menu root items, this command may be called only from the menu making script
	### Parameters:
	- id (str): the menu id, see examples in the `UserPrefs/Rooms/menu.py` or `cpp`
	'''
def menu_item(id: str) :
	'''
	add the item to the menu, this command may be called only from the menu making script
	### Parameters:
	- id (str): the item id, see examples in the `UserPrefs/Rooms/menu.py` or `cpp`. If you want to trigger some script by this menu item
	you may use '$execute:path/to/your/script.py' as the id.
	'''
def menu_info(id: str) :
	'''
	add the information item to the menu (without any action, just message), this command may be called only from the menu making script
	### Parameters:
	- id (str): the item text identifier
	'''
def menu_submenu(id: str) :
	'''
	add the submenu to the current menu, this command may be called only from the menu making script
	### Parameters:
	- id (str): the submenu id/text
	### Returns:
	- always True, just for structuring the script
	'''
def menu_exit() :
	'''
	finish the current submenu, this command may be called only from the menu making script
	'''
def menu_separator() :
	'''
	add the separator to the current menu, this command may be called only from the menu making script
	'''
def menu_hotkey(id: str, Shift: int, Ctrl: int, Alt: int) :
	'''
	set the hotkey for the menu item, this command may be called only from the menu making script
	### Parameters:
	- id (str): the item id, see examples in the `UserPrefs/Rooms/menu.py` or `cpp`
	- Shift (int): set true if Shift should be pressed
	- Ctrl (int): set true if Ctrl should be pressed
	- Alt (int): set true if Alt should be pressed
	'''
def iconic_submenu(id: str, size: int) :
	'''
	start the menu that will be shown on the icon click, like the navigation menu
	### Parameters:
	- id (str): the text identifier
	- size (int): the size of the icon
	### Returns:
	- always True to structure the script
	'''
def is_new_scene() :
	'''
	is the scene new/empty?
	### Returns:
	- True if empty
	'''
def is_steam_app() :
	'''
	is it steam app?
	### Returns:
	- True if it is
	'''
def is_medical() :
	'''
	check if the app is medical
	### Returns:
	- True if it is
	'''
def is_ppp() :
	'''
	chack if there are any ppp objects in scene
	### Returns:
	- True if there are
	'''
def is_proxy() :
	'''
	check if current sculpt object is in proxy mode
	### Returns:
	- True if it is
	'''
def is_multires() :
	'''
	check if the current sculpt object is on some multiresolution level
	### Returns:
	- True if it is
	'''
def is_surface() :
	'''
	check if the current sculpt object is in surface mode
	### Returns:
	- True if it is
	'''
def IsInRoom(name: str) :
	'''
	check if you are in some room
	### Parameters:
	- name (str): the room name
	### Returns:
	- True if you are in that room
	'''
def RoomExists(name: str) :
	'''
	check if the room exists
	### Parameters:
	- name (str): the room name/identifier
	### Returns:
	- True if the room exists
	'''
def CheckIfExists(path: str) :
	'''
	check if the file exists
	### Parameters:
	- path (str): the file path, full or relative to Coat's documents
	### Returns:
	- True if exists
	'''
def UseRecordScript() :
	'''
	check is scripts recording available
	### Returns:
	- True if available
	'''
def is_mv() :
	'''
	check if mv objects available in scene
	### Returns:
	- True if available
	'''
def is_ptex() :
	'''
	check if ptex is used in the current scene
	### Returns:
	- True if used
	'''
def show_rmb_panel() :
	'''
	show the rmb panel
	'''
def show_space_panel(Subset: str, NumColumns: int) :
	'''
	show the space panel (with limitations if need)
	### Parameters:
	- Subset (str): the subset, if need
	- NumColumns (int): amount of columns
	'''
def gltf_support() :
	'''
	gltf export supported
	### Returns:
	- True if supported
	'''
def tex_approach() :
	'''
	returns the texturing approach index (from the Textures menu)
	### Returns:
	- the index
	'''
def menu_insert_extensions(id: str) :
	'''
	insert extension into the main menu (may be called only from the menu making script)
	### Parameters:
	- id (str): the extension id
	'''
def insert_extensions() :
	'''
	insert extensions into the toolset (may be used only from the toolset.py)
	'''
def set_space_panel_columns_count(num: int) :
	'''
	set the space panel columns count (only for the toolset.py)
	### Parameters:
	- num (int): amount of columns
	'''
def SetAutoSnapDefaults(value: bool) :
	'''
	set the default value for auto-snapping, usually for the retopo/modeling rooms (in toolset.py)
	### Parameters:
	- value (bool): the default value
	'''
def menu_property(id: str) :
	'''
	returns boolean property value
	### Parameters:
	- id (str): the property id, available values: RMBObjectInCache, RMBObjectIsSurface, ObjectHasNodes, IsCurvePrimitive, IsCurveClosed, OverSculptObject
	### Returns:
	- the property value
	'''
def tools_section(id: str) :
	'''
	start the tools section in the toolset.py
	### Parameters:
	- id (str): the section id
	'''
def tools_item(id: str) :
	'''
	add the item to the tools section (toolset.py)
	### Parameters:
	- id (str): the tool identifier
	'''
def page_suffix(suffix: str) :
	'''
	set the additional suffix for the page in the toolset.py
	### Parameters:
	- suffix (str): usually "S" or "V"
	'''
def default_tool(tool: str) :
	'''
	set the default tool for the toolset.py
	### Parameters:
	- tool (str): the tool identifier
	'''
def IsDebug() :
	'''
	is Debug mode (for developers only)
	### Returns:
	- True if debug
	'''
def start_rmb_panel() :
	'''
	start the RNB panel. This command may be called only from the RMB response making script (curves.py, rmb.py)
	'''
def menu_sort() :
	'''
	sort items in the current menu
	'''
def IsRecordScript() :
	'''
	is the script recording enabled?
	### Returns:
	- True if enabled
	'''
def IsInTool(ToolID: str) :
	'''
	check if we are in some tool
	### Parameters:
	- ToolID (str): the tool identifier
	### Returns:
	- True if in that tool
	'''
def voxtree_item_picked() :
	'''
	check if the VoxTree item is picked
	### Returns:
	- true if picked
	'''
def retopo_object_picked() :
	'''
	the retopo object is picked
	### Returns:
	- True if picked
	'''
def empty_space_picked() :
	'''
	check if no object is picked
	### Returns:
	- True if no object is picked
	'''
def voxtree_object_picked() :
	'''
	check if the sculpt object is picked in the viewport
	### Returns:
	- True if picked
	'''
def GetCurrentToolSubmode(id: str) :
	'''
	get the current tool submode (usually for the uv/retopo tools)
	### Parameters:
	- id (str): the submode identifier
	### Returns:
	- the value
	'''
def tools_comment(id: str) :
	'''
	comment in toolset.py for auto-documentation (legacy)
	### Parameters:
	- id (str): the text of the comment
	'''
def doc_mode() :
	'''
	check if script is in auto-documenting mode (legacy)
	### Returns:
	- the state
	'''
def PureIconic() :
	'''
	enable the radial menu mode for the space panel
	'''
def lock_ui_changes() :
	'''
	check if UI changes locked (for specialized applications, like printing)
	### Returns:
	- the lock state
	'''
def ue5_support() :
	'''
	returns if ue5 support enabled
	### Returns:
	- True if enabled
	'''
class ClusterScale(Enum):
	Uniform_Scaling = ...
	Axial_Normal = ...
	Axial_X = ...
	Axial_Y = ...
	Axial_Z = ...
	Radial_Normal = ...
	Radial_X = ...
	Radial_Y = ...
	Radial_Z = ...
class SpiralProfile(Enum):
	CIRCLE = ...
	RECTANGLE = ...
class FontStyle(Enum):
	Regular = ...
	Italic = ...
	Underline = ...
	StrikeThrough = ...
class FontWeight(Enum):
	Dont = ...
	Thin = ...
	ExtraLight = ...
	Light = ...
	Normal = ...
	Medium = ...
	DemiBold = ...
	Bold = ...
	ExtraBold = ...
	Black = ...
class ThreadProfile(Enum):
	ThreadNone = ...
	ThreadTriangle = ...
	ThreadTrapeze = ...
	ThreadRectangular = ...
	ThreadRound = ...
	ThreadPersistent = ...
class ThreadStudBodyType(Enum):
	StudCylinder = ...
	StudCone = ...
class SlitType(Enum):
	none = ...
	Slot = ...
	Phillipse = ...
	Pozidriv = ...
	Robertson = ...
	HexSocket = ...
	SecurityHexSocket = ...
	Torx = ...
	SecurityTorx = ...
	TriWing = ...
	TorqSet = ...
	TripleSquare = ...
	Polydrive = ...
	DoubleSquare = ...
	SplineDrive = ...
	DoubleHex = ...
	Bristol = ...
	Pentalobular = ...
	Frearson = ...
	SnakeEyes = ...
	TA = ...
	TP3 = ...
	MorTorq = ...
	ClutCHG = ...
	ClutCHA = ...
	GroupEyes = ...
class BoltHeadType(Enum):
	BoltNone = ...
	BoltHexa = ...
	Countersunk = ...
	BoltRound = ...
	Pan = ...
	Dome = ...
	Oval = ...
	Square = ...
	TShaped = ...
	Cylinder = ...
	Lamb = ...
	Rim = ...
	Eye = ...
	Bugle = ...
	Clop = ...
class NutType(Enum):
	NutNone = ...
	NutHexa = ...
	Quard = ...
	Acorn = ...
	Lowacorn = ...
	NutFlange = ...
	Slits = ...
	Radial = ...
	NutLamb = ...
	NutRim = ...
	Selflock = ...
	NutTShaped = ...
	Clamplever = ...
	NtCount = ...
class ThreadSurface(Enum):
	ThreadCylinder = ...
	ThreadCone = ...
	ThreadEdge = ...
class vec2:
	x: float
	y: float
	def __init__(self): ...
	def __init__(self, S: float) -> any: ...
	def __init__(self, X: float, Y: float): ...
	def __init__(self, v: vec2): ...
	def Copy (self, Src: float) : ...
	def SetZero (self) : ...
	def SetOne (self) : ...
	def Set (self, S: float) : ...
	def Set (self, X: float, Y: float) : ...
	def __getitem__ (self, index: int) -> float : ...
	def __setitem__ (self, index: int) -> float : ...
	def __neg__ (self) -> vec2 : ...
	def __iadd__ (self, _0: vec2) -> vec2 : ...
	def __isub__ (self, _0: vec2) -> vec2 : ...
	def __imul__ (self, _0: vec2) -> vec2 : ...
	def __imul__ (self, _0: float) -> vec2 : ...
	def __itruediv__ (self, _0: vec2) -> vec2 : ...
	def __itruediv__ (self, _0: float) -> vec2 : ...
	def Transform (self, _0: mat3) : ...
	def __imul__ (self, _0: mat3) : ...
	def TransformCoordinate (self, _0: mat4) : ...
	def TransformNormal (self, _0: mat4) : 
		'''
		 (x, y, 0, 1), projects the result back into w = 1
		'''

	def __add__ (self, _0: vec2) -> vec2 : ...
	def __sub__ (self, _0: vec2) -> vec2 : ...
	def __mul__ (self, _0: vec2) -> vec2 : ...
	def __mul__ (self, _0: float) -> vec2 : ...
	def __truediv__ (self, _0: vec2) -> vec2 : ...
	def __truediv__ (self, _0: float) -> vec2 : ...
	def __mul__ (self, _0: mat3) -> vec2 : ...
	def __eq__ (self, _0: vec2) -> bool : ...
	def __ne__ (self, _0: vec2) -> bool : ...
	@staticmethod
	def Equals (_0: vec2, _1: vec2, Eps: float) -> bool : ...
	def Length (self) -> float : ...
	def LengthSq (self) -> float : ...
	def Normalize (self) -> float : ...
	def NormalizeSafe (self, Fallback: vec2) -> float : ...
	def IsValid (self) -> bool : ...
	def IsNormalized (self, Eps: float) -> bool : ...
	def IsZero (self, Eps: float) -> bool : ...
	@staticmethod
	def Round (_0: vec2) -> vec2 : ...
	def ToRound (self) -> vec2 : ...
	@staticmethod
	def Abs (_0: vec2) -> vec2 : ...
	@staticmethod
	def Fract (_0: vec2) -> vec2 : ...
	@staticmethod
	def Angle (_0: vec2, _1: vec2) -> float : ...
	@staticmethod
	def AreaSigned (t0: vec2, t1: vec2, t2: vec2) -> float : ...
	@staticmethod
	def Ccw (_0: vec2, _1: vec2) -> float : ...
	@staticmethod
	def Clamp (Value: vec2, Lo: vec2, Hi: vec2) -> vec2 : ...
	@staticmethod
	def Distance (_0: vec2, _1: vec2) -> float : ...
	@staticmethod
	def DistanceSq (_0: vec2, _1: vec2) -> float : ...
	@staticmethod
	def Dot (_0: vec2, _1: vec2) -> float : ...
	@staticmethod
	def Lerp (_0: vec2, _1: vec2, _2: float) -> vec2 : ...
	@staticmethod
	def Lerp05 (_0: vec2, _1: vec2) -> vec2 : ...
	@staticmethod
	def Max (_0: vec2, _1: vec2) -> vec2 : ...
	@staticmethod
	def Min (_0: vec2, _1: vec2) -> vec2 : ...
	@staticmethod
	def PerpCw (_0: vec2) -> vec2 : ...
	@staticmethod
	def PerpCcw (_0: vec2) -> vec2 : ...
	@staticmethod
	def Reflect (RayDir: vec2, Normal: vec2) -> vec2 : ...
	@staticmethod
	def Refract (RayDir: vec2, Normal: vec2, Eta: float) -> vec2 : ...
	@staticmethod
	def Truncate (u: vec2, MaxLength: float) -> vec2 : ...
	@staticmethod
	def RandRange1 () -> vec2 : ...
	@staticmethod
	def RandNormal () -> vec2 : ...
	@staticmethod
	def Rand (Lo: vec2, Hi: vec2) -> vec2 : ...
	def distance2 (self, _0: vec2) -> float : ...
	def distance (self, _0: vec2) -> float : ...
	def DistanceToLineSegSq (self, A: vec2, B: vec2, pScale: float = None) -> float : ...
	@staticmethod
	def SegIntersection (L0: vec2, L1: vec2, R0: vec2, R1: vec2, l: float = None, r: float = None) -> bool : ...
	@staticmethod
	def FromBaryCentric (t0: vec2, t1: vec2, t2: vec2, u: float, v: float) -> vec2 : ...
	@staticmethod
	def FromPolar (Radius: float, Angle: float) -> vec2 : ...
	Zero: vec2
	One: vec2
	Infinity: vec2
	AxisX: vec2
	AxisY: vec2
	AxisNegX: vec2
	AxisNegY: vec2
	def GetDimension (self) -> int : ...
	def ToFloatPtr (self) -> float : ...
	def ToFloatPtr (self) -> float : ...
	def ToPolar (self, Radius: float, Angle: float) : ...
	def ToBaryCentric (self, t0: vec2, t1: vec2, t2: vec2, u: float, v: float) -> float : ...
	def IsInsideTri (self, t0: vec2, t1: vec2, t2: vec2) -> bool : ...
	def ToNormal (self) -> vec2 : ...
	def ToPerpCw (self) -> vec2 : ...
	def ToPerpCcw (self) -> vec2 : ...
	def Clear (self) : 
		'''
		 for compatibility with OpenSubdiv ////
		'''

	def AddWithWeight (self, src: vec2, weight: float) : ...
	def SetPosition (self, aX: float, aY: float) : ...
	def GetPosition (self) -> float : ...
class vec3:
	x: float
	y: float
	z: float
	def __init__(self): ...
	def __init__(self, S: float) -> any: ...
	def __init__(self, X: float, Y: float, Z: float): ...
	def __init__(self, XY: vec2, Z: float): ...
	def __init__(self, v: any): ...
	def __init__(self, v: vec3): ...
	def Copy (self, Src: float) : ...
	def SetZero (self) : ...
	def SetOne (self) : ...
	def SetRandRange1 (self) : ...
	def Set (self, S: float) : ...
	def Set (self, X: float, Y: float, Z: float) : ...
	def Set (self, XY: vec2, Z: float) : ...
	def __setitem__ (self, Index: int) -> float : ...
	def __getitem__ (self, Index: int) -> float : ...
	def __neg__ (self) -> vec3 : ...
	def __iadd__ (self, _0: vec3) -> vec3 : ...
	def __isub__ (self, _0: vec3) -> vec3 : ...
	def __imul__ (self, _0: vec3) -> vec3 : ...
	def __imul__ (self, _0: float) -> vec3 : ...
	def __itruediv__ (self, _0: vec3) -> vec3 : ...
	def __itruediv__ (self, _0: float) -> vec3 : ...
	def TransformCoordinate (self, _0: mat4) : ...
	def TransformNormal (self, _0: mat4) : ...
	def TransformNormalTransposed (self, _0: mat4) : ...
	def Transform (self, _0: mat3) : ...
	def __imul__ (self, _0: mat3) -> vec3 : ...
	def Rotate (self, _0: quat) : ...
	def __imul__ (self, _0: quat) : ...
	def Rotate (self, _0: rotation) : ...
	def __imul__ (self, _0: rotation) : ...
	def __assign__ (self, _0: vec4) -> vec3 : ...
	def distance (self, u: vec3) -> float : ...
	def distanceSq (self, u: vec3) -> float : ...
	def dot (self, u: vec3) -> float : ...
	def cross (self, u: vec3, v: vec3) : ...
	def Clear (self) : ...
	def AddWithWeight (self, src: vec3, weight: float) : ...
	def SetPosition (self, aX: float, aY: float, aZ: float) : ...
	def GetPosition (self) -> float : ...
	def __add__ (self, _0: vec3) -> vec3 : ...
	def __sub__ (self, _0: vec3) -> vec3 : ...
	def __mul__ (self, _0: vec3) -> vec3 : ...
	def __mul__ (self, _0: float) -> vec3 : ...
	def __truediv__ (self, _0: vec3) -> vec3 : ...
	def __truediv__ (self, _0: float) -> vec3 : ...
	def __mul__ (self, _0: mat3) -> vec3 : ...
	def __mul__ (self, _0: quat) -> vec3 : ...
	def __mul__ (self, _0: rotation) -> vec3 : ...
	def __eq__ (self, _0: vec3) -> bool : ...
	def __ne__ (self, _0: vec3) -> bool : ...
	@staticmethod
	def Equals (_0: vec3, _1: vec3, Eps: float) -> bool : ...
	def Length (self) -> float : ...
	def Length2 (self) -> float : ...
	def LengthSq (self) -> float : ...
	def LengthM (self) -> float : ...
	def Normalize (self) -> float : 
		'''
		Manhattan distance
		'''

	def Normalize2 (self) -> float : ...
	def NormalizeSafe (self, Fallback: vec3 = 3) -> float : ...
	def FixDegenerateNormal (self) -> bool : ...
	def FixDenormals (self) -> bool : ...
	def IsValid (self) -> bool : ...
	def IsNormalized (self, Eps: float) -> bool : ...
	def IsZero (self, Eps: float) -> bool : ...
	def Round (self) : ...
	@staticmethod
	def Abs (_0: vec3) -> vec3 : ...
	@staticmethod
	def Angle (_0: vec3, _1: vec3) -> float : ...
	@staticmethod
	def Angle (p1: vec3, p2: vec3, p3: vec3, normal: vec3) -> float : ...
	@staticmethod
	def AreaSigned (t0: vec3, t1: vec3, t2: vec3) -> float : ...
	@staticmethod
	def BaryCentric (t0: vec3, t1: vec3, t2: vec3, f: float, g: float) -> vec3 : ...
	@staticmethod
	def Clamp (_0: vec3, _1: vec3, _2: vec3) -> vec3 : ...
	@staticmethod
	def Cross (_0: vec3, _1: vec3) -> vec3 : ...
	def SetCross (self, _0: vec3, _1: vec3) : ...
	@staticmethod
	def Distance (_0: vec3, _1: vec3) -> float : ...
	@staticmethod
	def Distance2 (_0: vec3, _1: vec3) -> float : ...
	@staticmethod
	def DistanceSq (_0: vec3, _1: vec3) -> float : ...
	@staticmethod
	def Dot (_0: vec3, _1: vec3) -> float : ...
	@staticmethod
	def Lerp (_0: vec3, _1: vec3, _2: float) -> vec3 : ...
	@staticmethod
	def Lerp05 (_0: vec3, _1: vec3) -> vec3 : ...
	@staticmethod
	def Max (_0: vec3, _1: vec3) -> vec3 : ...
	@staticmethod
	def Min (_0: vec3, _1: vec3) -> vec3 : ...
	@staticmethod
	def Reflect (RayDir: vec3, Normal: vec3) -> vec3 : ...
	@staticmethod
	def Refract (RayDir: vec3, Normal: vec3, Eta: float) -> vec3 : 
		'''
		 \param Eta  Ratio of indices of refraction at the surface interface.
		'''

	@staticmethod
	def Slerp (n0: vec3, n1: vec3, s: float) -> vec3 : ...
	@staticmethod
	def Truncate (u: vec3, MaxLen: float) -> vec3 : ...
	@staticmethod
	def RandRange1 () -> vec3 : ...
	@staticmethod
	def RandNormal () -> vec3 : ...
	@staticmethod
	def Rand (Lo: vec3, Hi: vec3) -> vec3 : ...
	@staticmethod
	def Project (v1: vec3, v2: vec3) -> vec3 : ...
	@staticmethod
	def Perpendicular (v1: vec3) -> vec3 : ...
	def TriProjectionSolidAngle (self, a: vec3, b: vec3, c: vec3) -> float : ...
	Zero: vec3
	One: vec3
	Infinity: vec3
	AxisX: vec3
	AxisY: vec3
	AxisZ: vec3
	AxisNegX: vec3
	AxisNegY: vec3
	AxisNegZ: vec3
	def GetDimension (self) -> int : ...
	def ToFloatPtr (self) -> float : ...
	def ToFloatPtr (self) -> float : ...
	def ToVec2 (self) -> vec2 : ...
	def ToVec2 (self) -> vec2 : ...
	def ToAngles (self) -> angles : ...
	def GetOrthonormal (self) -> vec3 : ...
	def GetOrthonormalPair (self) -> list : ...
	def MakeOrthonormalTo (self, vec: vec3) : ...
	def ToPolarXZ (self, Radius: float, Angle: float) : ...
	@staticmethod
	def FromPolarXZ (Radius: float, Angle: float) -> vec3 : ...
	def ToBaryCentric (self, t0: vec3, t1: vec3, t2: vec3, f: float, g: float) -> float : ...
	def ToNormal (self) -> vec3 : ...
	def ToPerps (self, X: vec3, Y: vec3) : ...
	def ToPerp (self) -> vec3 : ...
	@staticmethod
	def RayTri (RayOrig: vec3, RayDir: vec3, t0: vec3, t1: vec3, t2: vec3, u: float, v: float, t: float, BackFaceCull: bool = False) -> bool : ...
	@staticmethod
	def PointInTriangle (p: vec3, t0: vec3, t1: vec3, t2: vec3) -> bool : ...
class vec4:
	x: float
	y: float
	z: float
	w: float
	def __init__(self): ...
	def __init__(self, S: float) -> any: ...
	def __init__(self, X: float, Y: float, Z: float, W: float): ...
	def __init__(self, XY: vec2, Z: float, W: float): ...
	def __init__(self, XY: vec2, ZW: vec2): ...
	def __init__(self, XYZ: vec3, W: float): ...
	def __init__(self, v: vec4): ...
	def SetZero (self) : ...
	def Set (self, S: float) : ...
	def Set (self, X: float, Y: float, Z: float, W: float) : ...
	def Set (self, XY: vec2, Z: float, W: float) : ...
	def Set (self, XY: vec2, ZW: vec2) : ...
	def Set (self, XYZ: vec3, W: float) : ...
	def Copy (self, pSrc: float) : ...
	def __setitem__ (self, index: int) -> float : ...
	def __getitem__ (self, index: int) -> float : ...
	def __neg__ (self) -> vec4 : ...
	def __iadd__ (self, _0: vec4) -> vec4 : ...
	def __isub__ (self, _0: vec4) -> vec4 : ...
	def __imul__ (self, _0: vec4) -> vec4 : ...
	def __imul__ (self, _0: float) -> vec4 : ...
	def __itruediv__ (self, _0: vec4) -> vec4 : ...
	def __itruediv__ (self, _0: float) -> vec4 : ...
	def Transform (self, _0: mat4) : ...
	def __imul__ (self, _0: mat4) : ...
	def __assign__ (self, _0: vec3) -> vec4 : ...
	def __add__ (self, _0: vec4) -> vec4 : ...
	def __sub__ (self, _0: vec4) -> vec4 : ...
	def __mul__ (self, _0: vec4) -> vec4 : ...
	def __mul__ (self, _0: float) -> vec4 : ...
	def __truediv__ (self, _0: vec4) -> vec4 : ...
	def __truediv__ (self, _0: float) -> vec4 : ...
	def __mul__ (self, _0: mat4) -> vec4 : ...
	def __eq__ (self, _0: vec4) -> bool : ...
	def __ne__ (self, _0: vec4) -> bool : ...
	@staticmethod
	def Equals (_0: vec4, _1: vec4, Eps: float) -> bool : ...
	def Length (self) -> float : ...
	def LengthSq (self) -> float : ...
	def Normalize (self) -> float : ...
	def NormalizeSafe (self, Fallback: vec4 = 4) -> float : ...
	def IsNormalized (self, Eps: float) -> bool : ...
	def IsZero (self, Eps: float) -> bool : ...
	@staticmethod
	def Abs (_0: vec4) -> vec4 : ...
	@staticmethod
	def Dot (_0: vec4, _1: vec4) -> float : ...
	@staticmethod
	def Lerp (_0: vec4, _1: vec4, _2: float) -> vec4 : 
		'''
			static cVec4 Cross(const cVec4 &, const cVec4 &, const cVec4 &);
		'''

	@staticmethod
	def Max (_0: vec4, _1: vec4) -> vec4 : ...
	@staticmethod
	def Min (_0: vec4, _1: vec4) -> vec4 : ...
	Zero: vec4
	One: vec4
	Infinity: vec4
	AxisX: vec4
	AxisY: vec4
	AxisZ: vec4
	AxisW: vec4
	AxisNegX: vec4
	AxisNegY: vec4
	AxisNegZ: vec4
	AxisNegW: vec4
	def ToFloatPtr (self) -> float : ...
	def ToFloatPtr (self) -> float : ...
	def ToVec2 (self) -> vec2 : ...
	def ToVec2 (self) -> vec2 : ...
	def ToVec3 (self) -> vec3 : ...
	def ToVec3 (self) -> vec3 : ...
	def GetDimension (self) -> int : ...
	def Clear (self) : 
		'''
		 for compatibility with OpenSubdiv ////
		'''

	def AddWithWeight (self, src: vec4, weight: float) : ...
	def SetPosition (self, aX: float, aY: float, aZ: float, aW: float) : ...
	def GetPosition (self) -> float : ...
class mat3:
	def __init__(self): ...
	def __init__(self, _00: float, _01: float, _02: float, _10: float, _11: float, _12: float, _20: float, _21: float, _22: float): ...
	def __init__(self, v: mat3): ...
	def Copy (self, Float9: float) : ...
	def CopyTransposed (self, Float9: float) : ...
	def SetZero (self) : ...
	def SetIdentity (self) : ...
	def GetRow (self, Index: int) -> vec3 : ...
	def GetRow0 (self) -> vec3 : ...
	def GetRow1 (self) -> vec3 : ...
	def GetRow2 (self) -> vec3 : ...
	def Row (self, Index: int) -> vec3 : ...
	def Row0 (self) -> vec3 : ...
	def Row1 (self) -> vec3 : ...
	def Row2 (self) -> vec3 : ...
	def SetRow (self, Index: int, _1: vec3) : ...
	def SetRow0 (self, _0: vec3) : ...
	def SetRow1 (self, _0: vec3) : ...
	def SetRow2 (self, _0: vec3) : ...
	def SetRow (self, Index: int, X: float, Y: float, Z: float) : ...
	def SetRow0 (self, X: float, Y: float, Z: float) : ...
	def SetRow1 (self, X: float, Y: float, Z: float) : ...
	def SetRow2 (self, X: float, Y: float, Z: float) : ...
	def GetCol (self, Index: int) -> vec3 : ...
	def GetCol0 (self) -> vec3 : ...
	def GetCol1 (self) -> vec3 : ...
	def GetCol2 (self) -> vec3 : ...
	def SetCol (self, Index: int, _1: vec3) : ...
	def SetCol0 (self, _0: vec3) : ...
	def SetCol1 (self, _0: vec3) : ...
	def SetCol2 (self, _0: vec3) : ...
	def SetCol (self, Index: int, X: float, Y: float, Z: float) : ...
	def SetCol0 (self, X: float, Y: float, Z: float) : ...
	def SetCol1 (self, X: float, Y: float, Z: float) : ...
	def SetCol2 (self, X: float, Y: float, Z: float) : ...
	def SetElem (self, Row: int, Col: int, Value: float) : ...
	def GetElem (self, Row: int, Col: int) -> float : ...
	def Elem (self, Row: int, Col: int) -> float : ...
	def __getitem__ (self, Row: int) -> vec3 : ...
	def __setitem__ (self, Row: int) -> vec3 : ...
	def __call__ (self, Row: int, Col: int) -> float : ...
	def __call__ (self, Row: int, Col: int) -> float : ...
	def Trace (self) -> float : ...
	def Determinant (self) -> float : ...
	def __eq__ (self, _0: mat3) -> bool : ...
	@staticmethod
	def Equals (_0: mat3, _1: mat3, Eps: float) -> bool : ...
	def IsZero (self, Eps: float) -> bool : ...
	def IsIdentity (self, Eps: float) -> bool : ...
	def IsSymmetric (self, Eps: float) -> bool : ...
	def IsOrthonormal (self, Eps: float) -> bool : ...
	def __neg__ (self) -> mat3 : ...
	def __iadd__ (self, R: mat3) -> mat3 : ...
	def __isub__ (self, R: mat3) -> mat3 : ...
	def __imul__ (self, R: mat3) -> mat3 : ...
	def __imul__ (self, _0: float) -> mat3 : ...
	def __itruediv__ (self, _0: float) -> mat3 : ...
	def __add__ (self, R: mat3) -> mat3 : ...
	def __sub__ (self, R: mat3) -> mat3 : ...
	def __mul__ (self, R: mat3) -> mat3 : ...
	def __mul__ (self, _0: float) -> mat3 : ...
	def __truediv__ (self, _0: float) -> mat3 : ...
	def Add (self, R: mat3) : ...
	def Sub (self, R: mat3) : ...
	def Mul (self, R: mat3) : ...
	def Mul (self, s: float) : ...
	Zero: mat3
	Identity: mat3
	@staticmethod
	def Transpose (_0: mat3) -> mat3 : ...
	@staticmethod
	def Invert (Fm: mat3, To: mat3) -> bool : ...
	@staticmethod
	def OrthoNormalize (Src: mat3) -> mat3 : ...
	@staticmethod
	def Rotation (Axis: vec3, Angle: float) -> mat3 : ...
	@staticmethod
	def RotationX (Angle: float) -> mat3 : ...
	@staticmethod
	def RotationY (Angle: float) -> mat3 : ...
	@staticmethod
	def RotationZ (Angle: float) -> mat3 : ...
	@staticmethod
	def RotationXYZ (Pitch: float, Yaw: float, Roll: float) -> mat3 : ...
	@staticmethod
	def EulerZYX (eulerX: float, eulerY: float, eulerZ: float) -> mat3 : ...
	@staticmethod
	def Scaling (XYZ: float) -> mat3 : ...
	@staticmethod
	def Scaling (X: float, Y: float) -> mat3 : ...
	@staticmethod
	def Scaling (X: float, Y: float, Z: float) -> mat3 : ...
	@staticmethod
	def Scaling (XY: vec2) -> mat3 : ...
	@staticmethod
	def Scaling (XYZ: vec3) -> mat3 : ...
	def ToFloatPtr (self) -> float : ...
	def ToFloatPtr (self) -> float : ...
	def ToMat4 (self) -> mat4 : ...
	def ToQuat (self) -> quat : ...
	def ToVectors (self, Forward: vec3, Right: vec3 = None, Up: vec3 = None) : ...
	@staticmethod
	def FromVectors (Forward: vec3, Right: vec3, Up: vec3) -> mat3 : ...
	@staticmethod
	def FromForward (Forward: vec3) -> mat3 : ...
	def ToForward (self) -> vec3 : ...
	def ToRight (self) -> vec3 : ...
	def ToUp (self) -> vec3 : ...
	def ToAngles (self) -> angles : ...
class mat4:
	def __init__(self): ...
	def __init__(self, Rotation: mat3, Translation: vec3): ...
	def __init__(self, Scaling: vec3, Translation: vec3): ...
	def __init__(self, _00: float, _01: float, _02: float, _03: float, _10: float, _11: float, _12: float, _13: float, _20: float, _21: float, _22: float, _23: float, _30: float, _31: float, _32: float, _33: float): ...
	def __init__(self, v: mat4): ...
	def Copy (self, Float16: float) : ...
	def CopyTransposed (self, Float16: float) : ...
	def SetZero (self) : ...
	def SetIdentity (self) : ...
	def GetRow (self, Index: int) -> vec4 : ...
	def GetRow0 (self) -> vec4 : ...
	def GetRow1 (self) -> vec4 : ...
	def GetRow2 (self) -> vec4 : ...
	def GetRow3 (self) -> vec4 : ...
	def Row (self, Index: int) -> vec4 : ...
	def Row0 (self) -> vec4 : ...
	def Row1 (self) -> vec4 : ...
	def Row2 (self) -> vec4 : ...
	def Row3 (self) -> vec4 : ...
	def SetRow (self, Index: int, _1: vec4) : ...
	def SetRow0 (self, _0: vec4) : ...
	def SetRow1 (self, _0: vec4) : ...
	def SetRow2 (self, _0: vec4) : ...
	def SetRow3 (self, _0: vec4) : ...
	def SetRow (self, Index: int, X: float, Y: float, Z: float, W: float) : ...
	def SetRow0 (self, X: float, Y: float, Z: float, W: float) : ...
	def SetRow1 (self, X: float, Y: float, Z: float, W: float) : ...
	def SetRow2 (self, X: float, Y: float, Z: float, W: float) : ...
	def SetRow3 (self, X: float, Y: float, Z: float, W: float) : ...
	def GetCol (self, Index: int) -> vec4 : ...
	def GetCol0 (self) -> vec4 : ...
	def GetCol1 (self) -> vec4 : ...
	def GetCol2 (self) -> vec4 : ...
	def GetCol3 (self) -> vec4 : ...
	def SetCol (self, Index: int, _1: vec4) : ...
	def SetCol0 (self, _0: vec4) : ...
	def SetCol1 (self, _0: vec4) : ...
	def SetCol2 (self, _0: vec4) : ...
	def SetCol3 (self, _0: vec4) : ...
	def SetCol (self, Index: int, X: float, Y: float, Z: float, W: float) : ...
	def SetCol0 (self, X: float, Y: float, Z: float, W: float) : ...
	def SetCol1 (self, X: float, Y: float, Z: float, W: float) : ...
	def SetCol2 (self, X: float, Y: float, Z: float, W: float) : ...
	def SetCol3 (self, X: float, Y: float, Z: float, W: float) : ...
	def SetElem (self, Row: int, Col: int, Value: float) : ...
	def GetElem (self, Row: int, Col: int) -> float : ...
	def Elem (self, Row: int, Col: int) -> float : ...
	def __getitem__ (self, Row: int) -> vec4 : ...
	def __setitem__ (self, Row: int) -> vec4 : ...
	def __call__ (self, Row: int, Col: int) -> float : ...
	def __call__ (self, Row: int, Col: int) -> float : ...
	def Trace (self) -> float : ...
	def Determinant (self) -> float : ...
	def __eq__ (self, _0: mat4) -> bool : ...
	@staticmethod
	def Equals (_0: mat4, _1: mat4, Eps: float) -> bool : ...
	def IsZero (self, Eps: float) -> bool : ...
	def IsIdentity (self, Eps: float) -> bool : ...
	def IsSymmetric (self, Eps: float) -> bool : ...
	def IsOrthonormal (self, Eps: float) -> bool : ...
	def __neg__ (self) -> mat4 : ...
	def __iadd__ (self, R: mat4) -> mat4 : ...
	def __isub__ (self, R: mat4) -> mat4 : ...
	def __imul__ (self, R: mat4) -> mat4 : ...
	def __imul__ (self, _0: float) -> mat4 : ...
	def __itruediv__ (self, _0: float) -> mat4 : ...
	def __add__ (self, R: mat4) -> mat4 : ...
	def __sub__ (self, R: mat4) -> mat4 : ...
	def __mul__ (self, R: mat4) -> mat4 : ...
	def __mul__ (self, _0: float) -> mat4 : ...
	def __truediv__ (self, _0: float) -> mat4 : ...
	def Add (self, R: mat4) : ...
	def Sub (self, R: mat4) : ...
	def Mul (self, R: mat4) : ...
	def Mul (self, s: float) : ...
	def ToFloatPtr (self) -> float : ...
	def ToFloatPtr (self) -> float : ...
	def ToMat3 (self) -> mat3 : ...
	def ToNormalMatrix (self) -> mat3 : ...
	def ToQuat (self) -> quat : ...
	def GetTranslation (self) -> vec3 : ...
	def SetTranslation (self, _0: vec3) : ...
	def GetScaling (self) -> vec3 : ...
	def SetScaling (self, _0: vec3) : ...
	def GetRotation (self) -> angles : ...
	def SetRotation (self, _0: angles) : ...
	@staticmethod
	def Transpose (_0: mat4) -> mat4 : ...
	@staticmethod
	def Invert (Fm: mat4, To: mat4) -> bool : ...
	Zero: mat4
	Identity: mat4
	@staticmethod
	def Translation (X: float, Y: float) -> mat4 : ...
	@staticmethod
	def Translation (X: float, Y: float, Z: float) -> mat4 : ...
	@staticmethod
	def Translation (XY: vec2) -> mat4 : ...
	@staticmethod
	def Translation (XYZ: vec3) -> mat4 : ...
	@staticmethod
	def Rotation (Axis: vec3, Angle: float) -> mat4 : ...
	@staticmethod
	def RotationX (Angle: float) -> mat4 : ...
	@staticmethod
	def RotationY (Angle: float) -> mat4 : ...
	@staticmethod
	def RotationZ (Angle: float) -> mat4 : ...
	@staticmethod
	def RotationXYZ (Pitch: float, Yaw: float, Roll: float) -> mat4 : ...
	@staticmethod
	def EulerZYX (eulerX: float, eulerY: float, eulerZ: float) -> mat4 : ...
	@staticmethod
	def RotationAt (Orig: vec2, Angle: float) -> mat4 : ...
	@staticmethod
	def RotationAt (Orig: vec3, Axis: vec3, Angle: float) -> mat4 : ...
	@staticmethod
	def Scaling (XYZ: float) -> mat4 : ...
	@staticmethod
	def Scaling (X: float, Y: float) -> mat4 : ...
	@staticmethod
	def Scaling (X: float, Y: float, Z: float) -> mat4 : ...
	@staticmethod
	def Scaling (XY: vec2) -> mat4 : ...
	@staticmethod
	def Scaling (XYZ: vec3) -> mat4 : ...
	@staticmethod
	def ScalingAt (OrigX: float, OrigY: float, ScaleXY: float) -> mat4 : ...
	@staticmethod
	def ScalingAt (OrigX: float, OrigY: float, ScaleX: float, ScaleY: float) -> mat4 : ...
	@staticmethod
	def ScalingAt (Orig: vec2, ScaleXY: float) -> mat4 : ...
	@staticmethod
	def ScalingAt (Orig: vec2, ScaleX: float, ScaleY: float) -> mat4 : ...
	@staticmethod
	def ScalingAt (Orig: vec2, Scale: vec2) -> mat4 : ...
	@staticmethod
	def ScalingAt (Orig: vec3, ScaleXYZ: float) -> mat4 : ...
	@staticmethod
	def ScalingAt (Orig: vec3, ScaleX: float, ScaleY: float, ScaleZ: float) -> mat4 : ...
	@staticmethod
	def ScalingAt (Orig: vec3, Scale: vec3) -> mat4 : ...
	@staticmethod
	def ScalingAt (Orig: vec3, Dir: vec3, Scale: float) -> mat4 : ...
	@staticmethod
	def Perspective (YFov: float, AspectWtoH: float, Znear: float, Zfar: float) -> mat4 : ...
	@staticmethod
	def PerspectiveInf (YFov: float, AspectWtoH: float, Znear: float) -> mat4 : ...
	@staticmethod
	def Ortho (Width: float, Height: float, Znear: float, Zfar: float) -> mat4 : ...
	@staticmethod
	def Ortho (Left: float, Right: float, Bottom: float, Top: float, Znear: float, Zfar: float) -> mat4 : ...
	@staticmethod
	def Ortho (B: boundbox) -> mat4 : ...
	@staticmethod
	def CubeViewProjection (Pos: vec3, Side: int, Radius: float, GL: bool) -> mat4 : 
		'''
		---------------
		'''

	@staticmethod
	def LookAtViewProjection (LookFrom: vec3, LookAt: vec3, FovY: float, AspectYtoH: float, Znear: float, Zfar: float) -> mat4 : ...
class rect:
	def __init__(self): ...
	def __init__(self, v: rect): ...
	def __eq__ (self, _0: rect) -> bool : ...
	def __ne__ (self, _0: rect) -> bool : ...
	@staticmethod
	def Equals (_0: rect, _1: rect, Eps: float) -> bool : ...
	def Set (self, MinX: float, MinY: float, MaxX: float, MaxY: float) : ...
	def Set (self, Min: vec2, Max: vec2) : ...
	def x (self) -> float : ...
	def y (self) -> float : ...
	def width (self) -> float : ...
	def height (self) -> float : ...
	def SetLeft (self, Left: float) : ...
	def AlignLeft (self, X: float) : ...
	def SetTop (self, Top: float) : ...
	def AlignTop (self, Y: float) : ...
	def SetRight (self, Right: float) : ...
	def AlignRight (self, X: float) : ...
	def SetBottom (self, Bottom: float) : ...
	def AlignBottom (self, Y: float) : ...
	def AlignInside (self, Parent: rect) : ...
	def GetTopLeft (self) -> vec2 : 
		'''
		 TopLeft
		'''

	def SetTopLeft (self, X: float, Y: float) : ...
	def SetTopLeft (self, TopLeft: vec2) : ...
	def AlignTopLeft (self, X: float, Y: float) : ...
	def AlignTopLeft (self, TopLeft: vec2) : ...
	def GetTopCenter (self) -> vec2 : ...
	def AlignTopCenter (self, X: float, Y: float) : ...
	def AlignTopCenter (self, TopCenter: vec2) : ...
	def GetTopRight (self) -> vec2 : ...
	def SetTopRight (self, X: float, Y: float) : ...
	def SetTopRight (self, TopRight: vec2) : ...
	def AlignTopRight (self, X: float, Y: float) : ...
	def AlignTopRight (self, TopRight: vec2) : ...
	def GetMiddleLeft (self) -> vec2 : ...
	def AlignMiddleLeft (self, X: float, Y: float) : ...
	def AlignMiddleLeft (self, MiddleLeft: vec2) : ...
	def GetMiddleCenter (self) -> vec2 : ...
	def AlignMiddleCenter (self, X: float, Y: float) : ...
	def AlignMiddleCenter (self, MiddleCenter: vec2) : ...
	def GetMiddleRight (self) -> vec2 : ...
	def AlignMiddleRight (self, X: float, Y: float) : ...
	def AlignMiddleRight (self, MiddleRight: vec2) : ...
	def GetBottomLeft (self) -> vec2 : ...
	def SetBottomLeft (self, X: float, Y: float) : ...
	def SetBottomLeft (self, BottomLeft: vec2) : ...
	def AlignBottomLeft (self, X: float, Y: float) : ...
	def AlignBottomLeft (self, BottomLeft: vec2) : ...
	def GetBottomCenter (self) -> vec2 : ...
	def AlignBottomCenter (self, X: float, Y: float) : ...
	def AlignBottomCenter (self, BottomCenter: vec2) : ...
	def GetBottomRight (self) -> vec2 : ...
	def SetBottomRight (self, X: float, Y: float) : ...
	def SetBottomRight (self, BottomRight: vec2) : ...
	def AlignBottomRight (self, X: float, Y: float) : ...
	def AlignBottomRight (self, BottomRight: vec2) : ...
	def GetPoint (self, Align: int) -> vec2 : ...
	def AlignPoint (self, Align: int, X: float, Y: float) : ...
	def AlignPoint (self, Align: int, With: vec2) : ...
	def AlignPoint (self, Align: int, Parent: rect) : ...
	def GetDockingAlign (self, Child: rect, DockingRegion: rect = None, RelPos: vec2 = None) -> int : 
		'''
		 GetDocking { Align, CRegion }
		'''

	def GetDockingRegion (self, Child: rect, Align: int) -> rect : ...
	def GetDockingAlign (self, Child: vec2, DockingRegion: rect = None, RelPos: vec2 = None) -> int : ...
	def GetDockingRegion (self, Child: vec2, Align: int) -> rect : ...
	def GetLeft (self) -> float : ...
	def GetTop (self) -> float : ...
	def GetRight (self) -> float : ...
	def GetBottom (self) -> float : ...
	def GetWidth (self) -> float : ...
	def GetHeight (self) -> float : ...
	def SetWidth (self, HoldPoint: int, Width: float) : ...
	def SetHeight (self, HoldPoint: int, Height: float) : ...
	def GetSize (self) -> vec2 : ...
	def SetSize (self, MinX: float, MinY: float, Width: float, Height: float) : ...
	def SetSize (self, Min: vec2, Size: vec2) : ...
	def SetSize (self, HoldPoint: int, Width: float, Height: float) : ...
	def SetSize (self, HoldPoint: int, Size: vec2) : ...
	def SetSize (self, HoldPoint: int, Side: float) : ...
	def GetCenterX (self) -> float : ...
	def GetCenterY (self) -> float : ...
	def AlignCenterX (self, X: float) : ...
	def AlignCenterY (self, Y: float) : ...
	def Inflate (self, DeltaXY: float) : ...
	def Inflate (self, DeltaX: float, DeltaY: float) : ...
	def Inflate (self, Delta: vec2) : ...
	def SetToPoint (self, X: float, Y: float) : ...
	def SetToPoint (self, P: vec2) : ...
	def ProjectPoint (self, _0: vec2) -> vec2 : ...
	def AddPoint (self, X: float, Y: float) -> bool : 
		'''
		 Returns closest point within rectangle
		'''

	def AddPoint (self, P: vec2) -> bool : ...
	def AddRect (self, Rc: rect) -> bool : ...
	def Translate (self, DeltaX: float, DeltaY: float) : 
		'''
		 Returns "true" if this rectangle is expanded
		'''

	def Translate (self, Delta: vec2) : ...
	def Contains (self, X: float, Y: float) -> bool : ...
	def Contains (self, P: vec2) -> bool : ...
	def Contains (self, Rc: rect) -> bool : ...
	@staticmethod
	def Union (l: rect, r: rect) -> rect : ...
	@staticmethod
	def Intersect (l: rect, r: rect) -> rect : ...
	def IntersectsWith (self, Rc: rect) -> bool : ...
	def Transform (self, R: mat3) : ...
	def __imul__ (self, R: mat3) : ...
	def Transform (self, T: mat4) : ...
	def __imul__ (self, T: mat4) : ...
	def __mul__ (self, R: mat3) -> rect : ...
	def __mul__ (self, T: mat4) -> rect : ...
	def ToRound (self) -> rect : ...
	def Round (self) : ...
	Zero: rect
	Empty: rect
	Unit: rect
	def IsEmpty (self) -> bool : ...
	def SetEmpty (self) : ...
	def SetZero (self) : ...
	@staticmethod
	def Inscribe (What: rect, Where: rect) -> rect : ...
class boundbox:
	def __init__(self): ...
	def __init__(self, p: vec3) -> any: ...
	def __init__(self, bMin: vec3, bMax: vec3): ...
	def __init__(self, v: boundbox): ...
	def __init__(self) -> any: ...
	def GetMin (self) -> vec3 : ...
	def GetMax (self) -> vec3 : ...
	def GetMin (self) -> vec3 : ...
	def GetMax (self) -> vec3 : ...
	def Set (self, Min: vec3, Max: vec3) : ...
	def SetMin (self, _0: vec3) : ...
	def SetMax (self, _0: vec3) : ...
	def GetSize (self) -> vec3 : ...
	def GetSizeX (self) -> float : ...
	def GetSizeY (self) -> float : ...
	def GetSizeZ (self) -> float : ...
	def GetDiagonal (self) -> float : ...
	def GetCenter (self) -> vec3 : ...
	def GetLargestAxis (self) -> int : ...
	def GetShortestAxis (self) -> int : ...
	def SetEmpty (self) : ...
	def SetZero (self) : ...
	def IsEmpty (self) -> bool : ...
	Empty: boundbox
	Zero: boundbox
	One: boundbox
	def AddPoint (self, _0: vec3) -> bool : 
		'''
		 m_Min = -cVec3::One, m_Max = cVec3::One
		'''

	def AddBounds (self, _0: boundbox) -> bool : ...
	def Inflate (self, DeltaX: float, DeltaY: float, DeltaZ: float) : ...
	def Inflate (self, DeltaXYZ: float) : ...
	def Inflate (self, Delta: vec3) : ...
	def Translate (self, _0: vec2) : ...
	def Translate (self, _0: vec3) : ...
	def DistanceToPointSq (self, p: vec2) -> float : ...
	def DistanceToPointSq (self, p: vec3) -> float : 
		'''
		 0.0f for inside
		'''

	def ContainsPoint (self, _0: vec2) -> bool : 
		'''
		 0.0f for inside
		'''

	def ContainsCircle (self, Center: vec2, Radius: float) -> bool : ...
	def ContainsPoint (self, _0: vec3) -> bool : ...
	def ContainsBounds (self, _0: boundbox) -> bool : ...
	def IntersectsBounds (self, _0: boundbox) -> bool : ...
	def IntersectsSphere (self, _0: any) -> bool : ...
	def RayIntersection (self, RayOrig: vec3, RayDir: vec3, Scale: float) -> bool : 
		'''
		 Intersection point is "RayOrig + RayDir * Scale"
		'''

	def RayIntersection (self, RayOrig: vec3, RayDir: vec3, Cross: vec3 = None) -> bool : ...
	def LineIntersection (self, RayOrig: vec3, RayDir: vec3, Scale: float) -> bool : ...
	@staticmethod
	def FromPoints (pPoints: vec2, nCount: int) -> boundbox : ...
	@staticmethod
	def FromPoints (pPoints: vec3, nCount: int) -> boundbox : ...
	def ToPoints (self, P8: vec3) : ...
	def ToSphere (self) -> any : 
		'''
		 Order is ready for "cFrustum" construction
		'''

	@staticmethod
	def Lerp (l: boundbox, r: boundbox, s: float) -> boundbox : ...
	@staticmethod
	def Transform (B: boundbox, T: mat4) -> boundbox : ...
	def ToRect (self) -> rect : ...
class rotation:
	def __init__(self): ...
	def __init__(self, Orig: vec3, Axis: vec3, Angle: float): ...
	def Set (self, Orig: vec3, Axis: vec3, Angle: float) -> rotation : ...
	def GetOrig (self) -> vec3 : ...
	def GetAxis (self) -> vec3 : ...
	def GetAngle (self) -> float : ...
	def SetOrig (self, Orig: vec3) : ...
	def SetAxis (self, Axis: vec3) : ...
	def SetAngle (self, Angle: float) : ...
	def ReCalcMatrix (self) : ...
	def __neg__ (self) -> rotation : ...
	def __imul__ (self, s: float) -> rotation : ...
	def __itruediv__ (self, s: float) -> rotation : ...
	def __mul__ (self, s: float) -> rotation : ...
	def __truediv__ (self, s: float) -> rotation : ...
	def Normalize180 (self) -> rotation : ...
	def Normalize360 (self) -> rotation : ...
	def ToAngles (self) -> angles : ...
	def ToQuat (self) -> quat : ...
	def ToMat3 (self) -> mat3 : ...
	def ToMat4 (self) -> mat4 : ...
	def ToAngularVelocity (self) -> vec3 : ...
class angles:
	Pitch: float
	Yaw: float
	Roll: float
	def __init__(self): ...
	def __init__(self, Pitch: float, Yaw: float, Roll: float): ...
	def Set (self, Pitch: float, Yaw: float, Roll: float) : ...
	def SetZero (self) : ...
	def Copy (self, Src: float) : ...
	def __setitem__ (self, Index: int) -> float : ...
	def __getitem__ (self, Index: int) -> float : ...
	def __neg__ (self) -> angles : ...
	def __iadd__ (self, _0: angles) : ...
	def __isub__ (self, _0: angles) : ...
	def __imul__ (self, _0: float) : ...
	def __itruediv__ (self, _0: float) : ...
	def __add__ (self, _0: angles) -> angles : ...
	def __sub__ (self, _0: angles) -> angles : ...
	def __mul__ (self, _0: float) -> angles : ...
	def __truediv__ (self, _0: float) -> angles : ...
	def __eq__ (self, _0: angles) -> bool : ...
	def __ne__ (self, _0: angles) -> bool : ...
	@staticmethod
	def Equals (_0: angles, _1: angles, Eps: float) -> bool : ...
	def Length (self) -> float : ...
	def LengthSq (self) -> float : ...
	def Normalize360 (self) : ...
	def Normalize180 (self) : ...
	def Round (self) : ...
	@staticmethod
	def Clamp (u: angles, Min: angles, Max: angles) -> angles : ...
	@staticmethod
	def Rand (Range: angles) -> angles : ...
	@staticmethod
	def Angle (l: angles, r: angles) -> float : ...
	@staticmethod
	def Distance (l: angles, r: angles) -> float : ...
	Zero: angles
	def ToVectors (self, Forward: vec3, Right: vec3 = None, Up: vec3 = None) : ...
	def ToForward (self) -> vec3 : ...
	def ToRight (self) -> vec3 : ...
	def ToUp (self) -> vec3 : ...
	def ToMat3 (self) -> mat3 : ...
	def ToMat4 (self) -> mat4 : ...
	def ToQuat (self) -> quat : ...
	def GetDimension (self) -> int : 
		'''
			cVec3 ToAngularVelocity() const;
		'''

	def ToFloatPtr (self) -> float : ...
	def ToFloatPtr (self) -> float : ...
	@staticmethod
	def EnsureShortestPath (l: angles, r: angles) : ...
	@staticmethod
	def Lerp (l: angles, r: angles, s: float) -> angles : ...
class quat:
	x: float
	y: float
	z: float
	w: float
	def __init__(self): ...
	def __init__(self, X: float, Y: float, Z: float, W: float): ...
	def __init__(self, v: quat): ...
	def SetIdentity (self) : ...
	def SetZero (self) : ...
	def IsZero (self, Eps: float) -> bool : ...
	def Set (self, X: float, Y: float, Z: float, W: float) : ...
	def Set (self, XYZ: vec3, W: float) : ...
	def __setitem__ (self, index: int) -> float : ...
	def __getitem__ (self, index: int) -> float : ...
	def __neg__ (self) -> quat : ...
	@staticmethod
	def Mul (_0: quat, _1: quat) -> quat : ...
	@staticmethod
	def Div (_0: quat, _1: quat) -> quat : ...
	def __iadd__ (self, _0: quat) -> quat : ...
	def __isub__ (self, _0: quat) -> quat : ...
	def __imul__ (self, _0: quat) -> quat : ...
	def __itruediv__ (self, _0: quat) -> quat : ...
	def __imul__ (self, _0: float) -> quat : ...
	def __itruediv__ (self, _0: float) -> quat : ...
	def __add__ (self, _0: quat) -> quat : ...
	def __sub__ (self, _0: quat) -> quat : ...
	def __mul__ (self, _0: quat) -> quat : ...
	def __truediv__ (self, _0: quat) -> quat : ...
	def __mul__ (self, _0: float) -> quat : ...
	def __truediv__ (self, _0: float) -> quat : ...
	def __eq__ (self, _0: quat) -> bool : ...
	def __ne__ (self, _0: quat) -> bool : ...
	@staticmethod
	def Equals (_0: quat, _1: quat, Eps: float) -> bool : ...
	@staticmethod
	def EqualRotations (_0: quat, _1: quat, Eps: float) -> bool : ...
	@staticmethod
	def SameHemisphere (_0: quat, _1: quat) -> bool : ...
	def Compress (self) : ...
	def CalcW (self) : ...
	def Length (self) -> float : ...
	def LengthSq (self) -> float : ...
	def Normalize (self) -> quat : ...
	def IsNormalized (self, Eps: float) -> bool : ...
	@staticmethod
	def Conjugate (_0: quat) -> quat : ...
	@staticmethod
	def Dot (_0: quat, _1: quat) -> float : ...
	@staticmethod
	def Exp (_0: quat) -> quat : ...
	@staticmethod
	def Invert (_0: quat) -> quat : ...
	@staticmethod
	def Lerp (q0: quat, q1: quat, s: float, ShortestPath: bool = True) -> quat : ...
	@staticmethod
	def Ln (_0: quat) -> quat : ...
	@staticmethod
	def LnDif (_0: quat, _1: quat) -> quat : ...
	@staticmethod
	def Slerp (q0: quat, q1: quat, s: float, ShortestPath: bool = True) -> quat : ...
	@staticmethod
	def Squad (q1: quat, A: quat, B: quat, C: quat, s: float) -> quat : ...
	@staticmethod
	def SquadSetup (q0: quat, q1: quat, q2: quat, q3: quat, A: quat, B: quat, C: quat) : ...
	Identity: quat
	Zero: quat
	def GetDimension (self) -> int : ...
	def ToAngles (self) -> angles : ...
	def ToRotation (self) -> rotation : ...
	def ToMat3 (self) -> mat3 : ...
	def ToMat4 (self) -> mat4 : ...
	def ToAngularVelocity (self) -> vec3 : ...
	def ToFloatPtr (self) -> float : ...
	def ToFloatPtr (self) -> float : ...
class cPlane:
	a: float
	b: float
	c: float
	d: float
	def __init__(self): ...
	def __init__(self, A: float, B: float, C: float, D: float): ...
	def __init__(self, t0: vec3, t1: vec3, t2: vec3): ...
	def __init__(self, Pt: vec3, Normal: vec3): ...
	def __init__(self, Normal: vec3, Offset: float): ...
	def SetNormalize (self, A: float, B: float, C: float, D: float) : 
		'''
		 From normal and distance to origin
		'''

	def GetNormal (self) -> vec3 : ...
	def SetNormal (self, _0: vec3) : ...
	def SetOffset (self, Offset: float) : ...
	def GetOffset (self) -> float : ...
	def MutableNormal (self) -> vec3 : ...
	def SetFromPoints (self, t0: vec3, t1: vec3, t2: vec3) -> float : ...
	def SetFromPointAndNormal (self, Pt: vec3, Normal: vec3) : ...
	def MoveToPoint (self, p: vec3) : ...
	def Distance (self, p: vec3) -> float : ...
	def ProjectPoint (self, p: vec3) -> vec3 : ...
	def ProjectVector (self, u: vec3) -> vec3 : ...
	def MirrorPoint (self, p: vec3) -> vec3 : ...
	def MirrorVector (self, u: vec3) -> vec3 : ...
	def MirrorOrient (self, q: quat) -> quat : ...
	def FlipNormal (self) : ...
	def BelowPlane (self, B: boundbox, T: mat4) -> bool : 
		'''
		 Returns "true" if all vertices of the bounds are on negative side of this plane
		'''

	def ClassifyPoint (self, p: vec3, Eps: float) -> any : ...
	def ClassifySphere (self, S: any, Eps: float) -> any : ...
	def IsFrontFacingTo (self, Dir: vec3) -> bool : ...
	def RayIntersection (self, RayOrig: vec3, RayDir: vec3, pScale: float = None, pCross: vec3 = None) -> bool : ...
	def SegIntersection (self, S0: vec3, S1: vec3, pCross: vec3 = None) -> bool : ...
	def PlaneIntersection (self, P: cPlane, pCross: vec3 = None, pDir: vec3 = None) -> bool : ...
	def ToPtr (self) -> float : ...
	def ToPtr (self) -> float : ...
	def ToVec4 (self) -> vec4 : ...
	def ToVec4 (self) -> vec4 : ...
class math:
	Pi: float
	TwoPi: float
	HalfPi: float
	QuarterPi: float
	RadsPerDeg: float
	DegsPerRad: float
	Epsilon: float
	EpsilonSq: float
	SpaceEpsilon: float
	MatrixEpsilon: float
	MatrixInvertEpsilon: float
	dMatrixInvertEpsilon: float
	dEpsilon: float
	Sqrt1Over2: float
	Sqrt1Over3: float
	SecsPerMs: float
	MsPerSec: float
	DoubleMinValue: float
	DoubleMaxValue: float
	FloatMinValue: float
	FloatMaxValue: float
	@staticmethod
	def IsInfinity (Value: float) -> bool : 
		'''
		 0x7f7fffff
		'''

	@staticmethod
	def IsPositiveInfinity (Value: float) -> bool : 
		'''
		 1.#INF000 or -1.#INF000
		'''

	@staticmethod
	def IsNegativeInfinity (Value: float) -> bool : 
		'''
		  1.#INF000
		'''

	IntMinValue: int
	IntMaxValue: int
	@staticmethod
	def MulDiv (Number: int, Numerator: int, Denominator: int) -> int : 
		'''
		 The same as Win32 API "MulDiv"
		'''

	@staticmethod
	def Rad (Deg: float) -> float : ...
	@staticmethod
	def Deg (Rad: float) -> float : ...
	@staticmethod
	def Rad (Deg: float) -> float : ...
	@staticmethod
	def Deg (Rad: float) -> float : ...
	@staticmethod
	def Sec (Ms: float) -> float : ...
	@staticmethod
	def Ms (Sec: float) -> float : ...
	@staticmethod
	def IsZero (eps: int = 0) -> bool : 
		'''
		 \todo fine  Add templates.
		'''

	@staticmethod
	def IsZero (f: float, Eps: float) -> bool : ...
	@staticmethod
	def IsOne (f: float, Eps: float) -> bool : ...
	@staticmethod
	def IsOne (f: float, Eps: float) -> bool : ...
	@staticmethod
	def IsMinusOne (f: float, Eps: float) -> bool : ...
	@staticmethod
	def IsZeroToOneExact (f: float) -> bool : ...
	@staticmethod
	def IsZeroToOneEps (f: float, Eps: float) -> bool : ...
	@staticmethod
	def IsInRange (i: int, Lo: int, Hi: int) -> bool : ...
	@staticmethod
	def IsInRangeExact (f: float, Lo: float, Hi: float) -> bool : ...
	@staticmethod
	def IsInRangeEps (f: float, Lo: float, Hi: float, Eps: float) -> bool : ...
	@staticmethod
	def Equals (x: float, y: float, Eps: float) -> bool : ...
	@staticmethod
	def IsValid (f: float) -> bool : ...
	@staticmethod
	def IsValid (f: float) -> bool : ...
	@staticmethod
	def IsZero (d: float, Eps: float) -> bool : ...
	@staticmethod
	def Equals (x: float, y: float, Eps: float) -> bool : ...
	@staticmethod
	def Clamp01 (f: float) -> float : ...
	@staticmethod
	def ClampRange1 (f: float) -> float : ...
	@staticmethod
	def ClampRange (f: float, l: float) -> float : ...
	@staticmethod
	def Lerp (a: float, b: float, s: float) -> float : ...
	@staticmethod
	def Cerp (a: float, b: float, s: float) -> float : ...
	@staticmethod
	def Lerp05 (a: float, b: float) -> float : ...
	@staticmethod
	def Lerper (Fm: float, To: float, x: float) -> float : ...
	@staticmethod
	def LerperClamp01 (Lo: float, Hi: float, x: float) -> float : ...
	@staticmethod
	def MidPointLerp (Start: float, Mid: float, End: float, s: float) -> float : ...
	@staticmethod
	def Abs (n: int) -> int : ...
	@staticmethod
	def Abs (x: float) -> float : ...
	@staticmethod
	def Abs (x: float) -> float : ...
	@staticmethod
	def Round (x: float) -> float : ...
	@staticmethod
	def Round (x: float) -> float : ...
	@staticmethod
	def Sqrt (x: float) -> float : ...
	@staticmethod
	def Sqrt (x: float) -> float : ...
	@staticmethod
	def FastInvSqrt (x: float) -> float : ...
	@staticmethod
	def FastSqrt (x: float) -> float : ...
	@staticmethod
	def Sin (a: float) -> float : ...
	@staticmethod
	def Cos (a: float) -> float : ...
	@staticmethod
	def Sin (a: float) -> float : ...
	@staticmethod
	def Cos (a: float) -> float : ...
	@staticmethod
	def SinCos (Angle: float, S: float, C: float) : ...
	@staticmethod
	def SinCos (Angle: float, S: float, C: float) : ...
	@staticmethod
	def Tan (a: float) -> float : ...
	@staticmethod
	def Tan (a: float) -> float : ...
	@staticmethod
	def ASin (x: float) -> float : ...
	@staticmethod
	def ASin (x: float) -> float : ...
	@staticmethod
	def ACos (x: float) -> float : ...
	@staticmethod
	def ACos (x: float) -> float : ...
	@staticmethod
	def ATan (x: float) -> float : ...
	@staticmethod
	def ATan (x: float) -> float : ...
	@staticmethod
	def ATan (y: float, x: float) -> float : ...
	@staticmethod
	def ATan (y: float, x: float) -> float : ...
	@staticmethod
	def Pow (x: float, y: float) -> float : ...
	@staticmethod
	def Pow (x: float, y: float) -> float : ...
	@staticmethod
	def Exp (x: float) -> float : ...
	@staticmethod
	def Exp (x: float) -> float : ...
	@staticmethod
	def Ldexp (x: float, exp: int) -> float : ...
	@staticmethod
	def Ldexp (x: float, exp: int) -> float : ...
	@staticmethod
	def Frexp (x: float, exp: int) -> float : ...
	@staticmethod
	def Frexp (x: float, exp: int) -> float : ...
	@staticmethod
	def Log (x: float) -> float : ...
	@staticmethod
	def Log (x: float) -> float : ...
	@staticmethod
	def Floor (f: float) -> float : ...
	@staticmethod
	def Ceil (f: float) -> float : ...
	@staticmethod
	def Frac (f: float) -> float : ...
	@staticmethod
	def Floor (d: float) -> float : ...
	@staticmethod
	def Ceil (d: float) -> float : ...
	@staticmethod
	def Frac (d: float) -> float : ...
	@staticmethod
	def Periodic (f: float, Lo: float, Hi: float, nPeriods: int = None) -> float : ...
	@staticmethod
	def IndexForInsert (f: float, Array: float, nCount: int, Stride: int = 0) -> int : ...
	@staticmethod
	def AngleNormalizeTwoPi (Angle: float) -> float : ...
	@staticmethod
	def AngleNormalizeTwoPi (Angle: float) -> float : 
		'''
		 0 <= Angle < TwoPi
		'''

	@staticmethod
	def AngleNormalizePi (Angle: float) -> float : 
		'''
		 0 <= Angle < TwoPi
		'''

	@staticmethod
	def AngleNormalize360 (Angle: float) -> float : 
		'''
		 - Pi < Angle <= Pi
		'''

	@staticmethod
	def AngleNormalize180 (Angle: float) -> float : ...
	@staticmethod
	def AngleEnsureShortestPath180 (Alpha: float, Beta: float) : ...
	@staticmethod
	def AngleDeltaRad (Alpha: float, Beta: float) -> float : ...
	@staticmethod
	def AngleLerpRad (Alpha: float, Beta: float, s: float) -> float : ...
	@staticmethod
	def AngleDeltaDeg (Alpha: float, Beta: float) -> float : ...
	@staticmethod
	def AngleLerpDeg (Alpha: float, Beta: float, s: float) -> float : ...
	@staticmethod
	def ClosestPowerOfTwo (X: int) -> int : ...
	@staticmethod
	def UpperPowerOfTwo (X: int) -> int : ...
	@staticmethod
	def LowerPowerOfTwo (X: int) -> int : ...
	@staticmethod
	def IsPowerOfTwo (X: int) -> bool : ...
	@staticmethod
	def Randomize (Seed: int) : ...
	@staticmethod
	def Rand01 () -> float : ...
	@staticmethod
	def RandBool () -> bool : ...
	@staticmethod
	def RandRange1 () -> float : ...
	@staticmethod
	def dRand (Lo: float, Hi: float) -> float : ...
	@staticmethod
	def Rand (Lo: float, Hi: float) -> float : ...
	@staticmethod
	def Rand (Lo: int, Hi: int) -> int : ...
	@staticmethod
	def SignBitSet (i: int) -> int : ...
	@staticmethod
	def SignBitNotSet (i: int) -> int : ...
	@staticmethod
	def TCBAdjInCoeff (tPrev: float, tCur: float, tNext: float) -> float : ...
	@staticmethod
	def TCBAdjOutCoeff (tPrev: float, tCur: float, tNext: float) -> float : ...
	@staticmethod
	def AlignToDword (i: int) -> int : ...
	@staticmethod
	def Checksum (Src: any, Size: int) -> int : ...
	@staticmethod
	def Float2Half (Float: float) -> int : ...
	@staticmethod
	def Half2Float (Half: int) -> float : ...
	@staticmethod
	def EndianSwap2 (Src: any, Count: int = 1) -> any : 
		'''
		 b (byte, char)
		'''

	@staticmethod
	def EndianSwap4 (Src: any, Count: int = 1) -> any : 
		'''
		 w (word, short)
		'''

	@staticmethod
	def EndianSwap8 (Src: any, Count: int = 1) -> any : 
		'''
		 d (dword, int, float)
		'''

	@staticmethod
	def EndianSwap (Src: any, Format: str, Count: int = 1) -> any : 
		'''
		 q (qword, double)
		'''

class ValuesField:
	def __init__(self): ...
	def __init__(self): ...
	def __init__(self, vf: ValuesField, x: int = 0, y: int = 0, w: int = 0, h: int = 0): ...
	def create (self, SizeX: int, SiezY: int, depth: int = 1, clampmode: FieldClamp = FieldClamp.fcWrap) : 
		'''
		Create the field
		### Parameters:
		- SizeX (int): width
		- SiezY (int): height
		- depth (int): channels count
		- clampmode (FieldClamp): clamp mode
		'''

	def createMips (self) : 
		'''
		create the mipmaps, decreasing twice with each level until it is possible
		'''

	def setClampMode (self, cl: FieldClamp) : 
		'''
		set the field clamp mode - how it acts beyond the boundaries
		### Parameters:
		- cl (FieldClamp): the clamp mode - fcWrap, fcClamp or fcZero
		'''

	def width (self) -> int : 
		'''
		get width
		### Returns:
		- (int) width of the field
		'''

	def height (self) -> int : 
		'''
		get height
		### Returns:
		- (int) height of the field
		'''

	def depth (self) -> int : 
		'''
		Get amount of channels
		### Returns:
		- (int) channels count
		'''

	def loadImage (self, name: str) : 
		'''
		read the image directly from the file
		### Parameters:
		- name (str): the filename
		'''

	def saveImage (self, name: str) : 
		'''
		save the field directly to file
		### Parameters:
		- name (str): the filename
		'''

	def clear (self) : 
		'''
		clear rthe field
		'''

	def torange (self, x: int, y: int) -> bool : 
		'''
		converts the (x,y) to range [0..Lx-1, 0..Ly-1]
		### Parameters:
		- x (int): x-coordinate
		- y (int): y-coordinate
		### Returns:
		- (bool) true if succeed and wrapping happened
		'''

	def set (self, value: float, x: int, y: int, channel: int = 0) : 
		'''
		set teh value to the field
		### Parameters:
		- value (float): the value to set
		- x (int): x-coordinate
		- y (int): y-coordinate
		- channel (int): the channel
		'''

	def add (self, value: float, x: int, y: int, channel: int = 0) : 
		'''
		add the value to the field
		### Parameters:
		- value (float): the value to add
		- x (int): x-coordinate
		- y (int): y-coordinate
		- channel (int): the channel
		'''

	def get (self, x: int, y: int, channel: int = 0) -> float : 
		'''
		get the value of the field by the integer coordinates
		### Parameters:
		- x (int): x-coordinate
		- y (int): y-coordinate
		- channel (int): the channel
		### Returns:
		- (float) the value of the field
		'''

	def value (self, x: int, y: int, channel: int = 0) -> float : 
		'''
		get the value reference of the field by the integer coordinates
		     *
		### Parameters:
		- x (int): x-coordinate
		     *
		- y (int): y-coordinate
		     *
		- channel (int): the channel
		     *
		### Returns:
		- (float) the value of the field
		'''

	def getV3 (self, x: int, y: int) -> vec3 : 
		'''
		get the reference to the values as 3d - vector. It has sense only if there are at least 3 channels
		### Parameters:
		- x (int): x-coordinate
		- y (int): y-coordinate
		### Returns:
		- (vec3) the reference to the vector
		'''

	def getV3 (self, x: int, y: int) -> vec3 : ...
	def getV4 (self, x: int, y: int) -> vec4 : 
		'''
		get the reference to the values as 4d - vector. It has sense only if there are at least 4 channels
		### Parameters:
		- x (int): x-coordinate
		- y (int): y-coordinate
		### Returns:
		- (vec4) the reference to the 4d-vector
		'''

	def getV4 (self, x: int, y: int) -> vec4 : ...
	def getV2 (self, x: int, y: int) -> vec2 : 
		'''
		get the reference to the values as 2d - vector. It has sense only if there are at least 2 channels
		### Parameters:
		- x (int): x-coordinate
		- y (int): y-coordinate
		### Returns:
		- (vec2) the reference to the vector
		'''

	def getV2 (self, x: int, y: int) -> vec2 : ...
	def get_linear (self, x: float, y: float, channel: int = 0) -> float : 
		'''
		get the linearly interpolated value
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		- channel (int): the channel
		### Returns:
		- (float) the interpolated value reference
		'''

	def get_linear_mip (self, x: float, y: float, channel: int, mip_level: float) -> float : 
		'''
		get the linearly interpolated value using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- channel (int): the channel
		- mip_level (float): the mip level
		### Returns:
		- (float) the interpolated value
		'''

	def get_linearV2 (self, x: float, y: float) -> vec2 : 
		'''
		get the linearly interpolated value as 2d-vector
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		### Returns:
		- (vec2) the interpolated 2d-value
		'''

	def get_linearV2_mip (self, x: float, y: float, mip_level: float) -> vec2 : 
		'''
		get the linearly interpolated value as 2d-vector using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- mip_level (float): the mip level
		### Returns:
		- (vec2) the interpolated value
		'''

	def get_linearV3 (self, x: float, y: float) -> vec3 : 
		'''
		get the linearly interpolated value as 3d-vector
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		### Returns:
		- (vec3) the interpolated 2d-value
		'''

	def get_linearV3_mip (self, x: float, y: float, mip_level: float) -> vec3 : 
		'''
		get the linearly interpolated value as 3d-vector using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- mip_level (float): the mip level
		### Returns:
		- (vec3) the interpolated value
		'''

	def get_linearV4 (self, x: float, y: float) -> vec4 : 
		'''
		get the linearly interpolated value as 4d-vector
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		### Returns:
		- (vec4) the interpolated 2d-value
		'''

	def get_linearV4_mip (self, x: float, y: float, mip_level: float) -> vec4 : 
		'''
		get the linearly interpolated value as 4d-vector using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- mip_level (float): the mip level
		### Returns:
		- (vec4) the interpolated value (assuming that w is the alpha channel)
		'''

	def get_bicubic (self, x: float, y: float, channel: int = 0) -> float : 
		'''
		get the bicubic interpolated value
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		- channel (int): the channel
		### Returns:
		- (float) the interpolated value
		'''

	def get_bicubic_mip (self, x: float, y: float, channel: int, mip_level: float) -> float : 
		'''
		get the bicubic interpolated value using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- channel (int): the channel
		- mip_level (float): the mip level
		### Returns:
		- (float) the interpolated value
		'''

	def get_bicubicV2 (self, x: float, y: float) -> vec2 : 
		'''
		get the bicubic interpolated value as the 2d-vector
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		### Returns:
		- (vec2) the interpolated value
		'''

	def get_bicubicV2_mip (self, x: float, y: float, mip_level: float) -> vec2 : 
		'''
		get the bicubic interpolated value as the 2d-vector using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- mip_level (float): the mip level
		### Returns:
		- (vec2) the interpolated value
		'''

	def get_bicubicV3 (self, x: float, y: float) -> vec3 : 
		'''
		get the bicubic interpolated value as the 3d-vector
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		### Returns:
		- (vec3) the interpolated value
		'''

	def get_bicubicV3_mip (self, x: float, y: float, mip_level: float) -> vec3 : 
		'''
		get the bicubic interpolated value as the 3d-vector using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- mip_level (float): the mip level
		### Returns:
		- (vec3) the interpolated value
		'''

	def get_bicubicV4 (self, x: float, y: float) -> vec4 : 
		'''
		get the bicubic interpolated value as the 4d-vector
		### Parameters:
		- x (float): x-coordinate
		- y (float): y-coordinate
		### Returns:
		- (vec4) the interpolated value
		'''

	def get_bicubicV4_mip (self, x: float, y: float, mip_level: float) -> vec4 : 
		'''
		get the bicubic interpolated value as the 4d-vector using the mipmaps
		### Parameters:
		- x (float): the x-coordinate
		- y (float): the y-coordinate
		- mip_level (float): the mip level
		### Returns:
		- (vec4) the interpolated value
		'''

	def resizeTo (self, dest: ValuesField) : 
		'''
		resize the field to other size using the bicubic interpolation
		### Parameters:
		- dest (ValuesField): the destination field
		'''

	def sharp2X (self, dest: ValuesField) : 
		'''
		Experimental: Increase the image 2X and sharpen
		### Parameters:
		- dest (ValuesField): the destination, should be empty
		'''

	def sharpEdges2X (self, dest: ValuesField) : 
		'''
		Experimental: Increase the image 2X and sharpen (sharpening edges so that edge width will be kept despite on the image size increasing)
		### Parameters:
		- dest (ValuesField): the destination, should be empty
		'''

	def sharpEdges2X1 (self, dest: ValuesField) : 
		'''
		Experimental, variation of the previous function: Increase the image 2X and sharpen (sharpening edges so that edge width will be kept despite on the image size increasing)
		### Parameters:
		- dest (ValuesField): the destination, should be empty
		'''

	def sharpResize (self, dest: ValuesField, scale: float) : 
		'''
		resize to bigger size keeping the edges sharpness
		### Parameters:
		- dest (ValuesField): destination image
		- scale (float): the scale > 1
		'''

	def relax (self, destination: ValuesField, degree: float, radius: float) : 
		'''
		relax the field
		### Parameters:
		- destination (ValuesField): the destination field. It is recommended to use swap for multiple relax steps
		- degree (float): the degree of the relaxation
		- radius (float): the radius of the kernel
		'''

	def relax (self, destination: ValuesField, degree: float, radius: float, x0: int, y0: int, x1: int, y1: int) : ...
	def sharpen (self, destination: ValuesField, degree: float, radius: float) : 
		'''
		sharpen the field
		### Parameters:
		- destination (ValuesField): the destination field. It is recommended to use swap for multiple relax steps
		- degree (float): the degree of the relaxation
		- radius (float): the radius of the kernel
		'''

	def monoTo (self, dest: ValuesField) : 
		'''
		convert multiple channels to one as an average-arithmetic
		'''

	def curvature (self, dest: ValuesField) : 
		'''
		calculate the curvature of the 2d-field
		### Parameters:
		- dest (ValuesField): the destination field (1 channel)
		'''

	def curvatureDir (self, dest: ValuesField) : 
		'''
		calculate the curvature principal directions
		### Parameters:
		- dest (ValuesField): the destination field (3channels)
		'''

	def normalmap (self, dest: ValuesField, byChannel: int = 0) : 
		'''
		calculate the normalmap
		### Parameters:
		- dest (ValuesField): the destination field (2 channels, only dx and dy will be written)
		- byChannel (int): the channel to be used as the depth source
		'''

	def normalmap3 (self, dest: ValuesField, heightmod: float = 1.0, channel: int = 0) : 
		'''
		calculate the normalmap as the 3d-vectors set
		### Parameters:
		- dest (ValuesField): the destination 3d-field
		- heightmod (float): the modulator for the heightmap
		- channel (int): the channel to be used as the depth source
		'''

	def gradientValue (self, dest: ValuesField) : 
		'''
		calculate the gradient length
		### Parameters:
		- dest (ValuesField): the 1d field
		'''

	def perlinMap (self, dest: ValuesField) : 
		'''
		experimental functions...
		'''

	def detectAnisotropy (self, dest: ValuesField) : ...
	def detectPerlin (self, x: int, y: int, channel: int) -> float : ...
	def __isub__ (self, field: ValuesField) : ...
	def __iadd__ (self, field: ValuesField) : ...
	def __iadd__ (self, value: float) : ...
	def __isub__ (self, value: float) : ...
	def __imul__ (self, value: float) : ...
	def __itruediv__ (self, value: float) : ...
	def max (self, other: ValuesField) : 
		'''
		calculated the maximum of two fields into hte current
		### Parameters:
		- other (ValuesField): the other field
		'''

	def swap (self, dest: ValuesField) : 
		'''
		swap two fields (dimensions may be different)
		### Parameters:
		- dest (ValuesField): the other field
		'''

	def LaplacianInterpolate (self, fixed: any) : 
		'''
		Interpolates the whole field so that it is maximally smooth (laplacian value minimized) and keeps the grid value at each locked point.
		This is heavy function, be careful with the timing. But it produces absolutely clean and smooth field.
		### Parameters:
		- fixed: The fixel points falgs, fixed.get(x+y*width) == true means that point is fixed
		'''

	def NormalizeColors (self, monochromatic: bool = False, mipsize: int = 64) : 
		'''
		Normalize the texture to be (128, 128, 128) in average using the mip-mapping algorithm
		### Parameters:
		- monochromatic (bool): set true to change the brightness only
		- mipsize (int): the mip-map size to be used to normalize the color
		'''

	def averageColor (self, x: int = 0, y: int = 0, w: int = 0, h: int = 0, alpha_threshold: float = 200) -> any : 
		'''
		get the average color of the texture piece
		### Parameters:
		- x (int): the x-coordinate of the piece
		- y (int): the y-coordinate of the piece
		- w (int): the width of the piece, iw w == 0, the whole texture width is taken
		- h (int): the height of the piece, if h == 0, the whole texture height is taken
		- alpha_threshold (float): the threshold for the alpha channel (if exists)
		### Returns:
		- (any) the average color, taken only the color of pixels with alpha > alpha_threshold
		'''

	def Decrease2X (self, dest: ValuesField) : 
		'''
		Decrease the field 2X times
		### Parameters:
		- dest (ValuesField): the destination field
		'''

	def toPower2 (self, dest: ValuesField) : 
		'''
		resize to the closest power of 2 (may increase, may decrease the size, we choose what is arithmetically closer)
		### Parameters:
		- dest (ValuesField): the destination
		'''

	def recoverBump (self, dest: ValuesField) : 
		'''
		recover the bump from the color/greyscale (heuristic)
		### Parameters:
		- dest (ValuesField): the destination depthmap
		'''

	def blendImage (self, other: ValuesField, transform: mat3, modulator: vec4 = 4) -> boundbox : 
		'''
		blend the image with the other image
		### Parameters:
		- other (ValuesField): the other image to blend with this image, it should be of the 4-channels in depth (color + alpha)
		- transform (mat3): the transformation matrix applied to the other image
		- modulator (vec4): the color/alpha modulator
		'''

	def blendImageM4 (self, other: ValuesField, transform: any, modulator: vec4 = 4) -> boundbox : 
		'''
		blend the image with the other image using the 4x4 matrix transformation
		### Parameters:
		- other (ValuesField): the other image to blend with this image, it should be of the 4-channels in depth (color + alpha)
		- transform: the transformation matrix applied to the other image
		- modulator (vec4): the color/alpha modulator
		### Returns:
		- (boundbox) the bounds of the blended image
		'''

	def rect (self, x0: int, y0: int, x1: int, y1: int, color: vec4) : 
		'''
		draw the filled rectangle
		### Parameters:
		- x0 (int): the left-top corner x
		- y0 (int): the left-top corner y
		- x1 (int): the right-bottom corner x
		- y1 (int): the right-bottom corner y
		- color (vec4): the color of the rectangle (r, g, b a), all values are in [0..255]
		'''

	def calc_featuremap (self, dest: ValuesField, radius: int) : ...
	def local_normalisation (self, dest: ValuesField, size: int) : ...
	def find_local_minmax (self, minmax: list) : ...
	def getEllipse (self, x: int, y: int, center: vec2, longer_axis: vec2, relation: float) : ...
class PaintRoom:
	@staticmethod
	def LoadMesh (file_name: str) -> bool : 
		'''
		Load poly object for painting room from file
		### Returns:
		- (bool) True if success
		'''

	@staticmethod
	def LoadColorTexture (file_name: str) -> bool : 
		'''
		Load texture from file and put it to a new layer
		### Returns:
		- (bool) True if success
		'''

	@staticmethod
	def ExportMesh (filename: str) -> bool : 
		'''
		Export mesh the object from the painting room to a file
		### Returns:
		- (bool) True if success
		'''

class Render:
	@staticmethod
	def CreateFBO (width: int, height: int, format: image_format) -> int : 
		'''
		Create frame buffer object. An FBO is a texture or data that can accept a rendered result
		### Parameters:
		- width (int): The size of the sampler in width
		- height (int): The size of the sampler in height
		- format (image_format): image_format - enum with the number of channels and the channel type. For example coat.image_format.Rgb8
		### Returns:
		- (int) texture id - can be used as texture id and as FBO for rendering target
		'''

	@staticmethod
	def clear (fbo_id: int, fill_color: any, clear_color: bool = True, clear_depth: bool = True, fill_depth: float = 1) -> int : 
		'''
		Clear the framebuffer object - fill each pixel of the FBO sample with the same data
		### Parameters:
		- fbo_id (int): FBO ID to be filled for clearing
		- fill_color: Color to fill each pixel
		- clear_color (bool): Do you want to clear the FBO color? if "true" the color of each pixel will be changed to fill_color, if "false" the color will not be changed.
		- clear_depth (bool): Do you want to clear the FBO depth? if "true" the depth of each pixel will be changed to fill_depth, if "false" the depth will not be changed.
		- fill_depth (float): Depth value for fill each pixel
		### Returns:
		- (int) true if successfully
		'''

	@staticmethod
	def draw_on_screen (texture: int = 1, left: int = 0, top: int = 0, right: int = 0, bottom: int = 0, red: int = 255, green: int = 255, blue: int = 255, opacity: int = 255) -> int : 
		'''
		Draw a texture rectangle in the main 3DCoat window
		### Parameters:
		- texture (int): The ID of the texture that will be rendered
		- left (int): The position of the left side of the rendered texture on the screen
		- top (int): The position of the top side of the rendered texture on the screen
		- right (int): The position of the right side of the rendered texture on the screen
		- bottom (int): The position of the bottom side of the rendered texture on the screen
		- red (int): Multiplier for the red channel of the texture
		- green (int): Multiplier for the green channel of the texture
		- blue (int): Multiplier for the blue channel of the texture
		### Returns:
		- (int) true if successfully
		'''

	@staticmethod
	def draw_text (x: float, y: float, text: str, color_r: float = 1, color_g: float = 1, color_b: float = 1, color_a: float = 1) -> int : 
		'''
		Draw the text in the main 3DCoat window
		### Parameters:
		- x (float): The position of the left side of the text block
		- y (float): The position of the top side of the text block
		- text (str): The content of the text block you want to display
		- color_r (float): Value of the red channel of the text color
		- color_g (float): Value of the gleen channel of the text color
		- color_b (float): Value of the blue channel of the text color
		- color_a (float): Opacity of the rendered text
		### Returns:
		- (int) true if successfully
		'''

	@staticmethod
	def CreateGPUTexture (src_data: any, format: image_format) -> int : 
		'''
		Create a 2D sampler in GPU memory from a numpy array
		### Parameters:
		- src_data: numpy array from which the 2d sampler will be created. A numpy array must have the correct width and height, type and number of channels as in OpenCV
		- format (image_format): The texture type must match the numpy structure and type. For example coat.image_format.Rgb8
		### Returns:
		- (int) the texture id of the new sampler
		'''

	@staticmethod
	def DeleteGPUTexture (texture_id: int) -> bool : 
		'''
		Remove sampler from GPU memory
		### Parameters:
		- texture_id (int): Texture ID
		### Returns:
		- (bool) true if successfully
		'''

	@staticmethod
	def work_area () -> any : 
		'''
		3DCoat workspace rectangle (viewport)
		'''

class Mesh:
	def __init__(self): ...
	def __init__(self): ...
	def __init__(self, m: Mesh): ...
	def __init__(self, m: any): ...
	def __assign__ (self, m: Mesh) -> Mesh : ...
	def __assign__ (self, m: any) -> Mesh : ...
	def MakeCopy (self) -> Mesh : ...
	def Read (self, name: str) -> bool : 
		'''
		Load the mesh from the file.
		### Parameters:
		- name (str): the filename. May contain full path or relative to the coat's install or documents folder.
		### Returns:
		- (bool) true if successful.
		'''

	def Write (self, name: str) -> bool : 
		'''
		Save the mesh to file
		### Parameters:
		- name (str): Full or relative path
		### Returns:
		- (bool) true if successful
		'''

	def valid (self) -> bool : 
		'''
		Check if mesh is valid
		### Returns:
		- (bool) true if mesh is valid
		'''

	def clear (self) : 
		'''
		clear the mesh
		'''

	def __iadd__ (self, m: Mesh) -> Mesh : ...
	def __iadd__ (self, m: any) -> Mesh : ...
	def addTransformed (self, m: Mesh, t: mat4) : 
		'''
		concatenate the transformed mesh with the current one
		### Parameters:
		- m (Mesh): the mesh
		- t (mat4): the transform
		'''

	def boolean (self, m: Mesh, op: BoolOpType) : 
		'''
		boolean operation
		### Parameters:
		- m (Mesh): the mesh to operate
		'''

	def transform (self, transform: mat4) : 
		'''
		transform the mesh
		### Parameters:
		- transform (mat4): the transformation matrix
		'''

	def rotateToXYAxis (self, axisX: vec3, axisY: vec3) : 
		'''
		rotate the mesh so that X axis will be aligned with axisX, Y axis will be aligned with axisY
		### Parameters:
		- axisX (vec3): the new X axis
		- axisY (vec3): the new Y axis
		'''

	def rotateToYZAxis (self, axisY: vec3, axisZ: vec3) : 
		'''
		rotate the mesh so that Y axis will be aligned with axisY, Z axis will be aligned with axisZ
		### Parameters:
		- axisY (vec3): the new Y axis
		- axisZ (vec3): the new Z axis
		'''

	def rotateToZXAxis (self, axisZ: vec3, axisX: vec3) : 
		'''
		rotate the mesh so that Z axis will be aligned with axisZ, X axis will be aligned with axisX
		### Parameters:
		- axisZ (vec3): the new Z axis
		- axisX (vec3): the new X axis
		'''

	def vertsCount (self) -> int : 
		'''
		returns the amount of verts in the mesh
		### Returns:
		- (int) the amount
		'''

	def vertsUvCount (self) -> int : 
		'''
		returns the amount of UV - verts in the mesh
		### Returns:
		- (int) the amount
		'''

	def vertsNormalCount (self) -> int : 
		'''
		returns the amount of normal - verts in the mesh
		### Returns:
		- (int) teh amount
		'''

	def facesCount (self) -> int : 
		'''
		returns the faces amount
		### Returns:
		- (int) the amount
		'''

	def getVertex (self, idx: int) -> vec3 : 
		'''
		get the vertex coordinate
		### Parameters:
		- idx (int): the vertex index
		### Returns:
		- (vec3) the coordinate
		'''

	def setVertex (self, idx: int, v: vec3) : 
		'''
		set the vertex coordinate
		### Parameters:
		- idx (int): the vertex index
		- v (vec3): the coordinate
		'''

	def createNewVertex (self, position: vec3) -> int : 
		'''
		create the positional vertex
		### Parameters:
		- position (vec3): the position
		### Returns:
		- (int) the positional vertex index
		'''

	def getVertexUV (self, idx: int) -> vec2 : 
		'''
		get the UV coordinate of the vertex, pay attention position verts and UV verts are different, they have different indices
		### Parameters:
		- idx (int): the UV vertex index, [0..vertsUvCount() - 1]
		### Returns:
		- (vec2) the UV coordinate
		'''

	def setVertexUV (self, idx: int, v: vec2) : 
		'''
		set the UV coordinate of the vertex, pay attention position verts and UV verts are different, they have different indices
		### Parameters:
		- idx (int): the UV vrertex index, [0..vertsUvCount() - 1]
		- v (vec2): the UV coordinate
		'''

	def createNewUvVertex (self, uv: vec2) -> int : 
		'''
		create new UV vertex to be used for faces
		### Parameters:
		- uv (vec2): the texture coordinates
		### Returns:
		- (int) the index
		'''

	def getVertexNormal (self, idx: int) -> vec3 : 
		'''
		get the normal of the vertex, pay attention position verts and normal verts are different, they have different indices
		### Parameters:
		- idx (int): the normal vertex index, [0..vertsNormalCount() - 1]
		### Returns:
		- (vec3) the normal
		'''

	def setVertexNormal (self, idx: int, v: vec3) : 
		'''
		set the normal of the vertex, pay attention position verts and normal verts are different, they have different indices
		### Parameters:
		- idx (int): the normal vertex index, [0..vertsNormalCount() - 1]
		- v (vec3): the normal
		'''

	def calcNormals (self) : 
		'''
		re-calculate normals over the mesh
		'''

	def calcNormalsIgnoreSharpEdges (self) : 
		'''
		re-calculate normals over the mesh, ignore the sharp edges
		'''

	def getFaceVertsCount (self, face: int) -> int : 
		'''
		get the amount of vertices over the face
		### Parameters:
		- face (int): the face index, should be in [0..facesCount() - 1]
		### Returns:
		- (int) the verts amount
		'''

	def getFaceUvVertsCount (self, face: int) -> int : 
		'''
		get the amount of UV vertices over the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (int) amount of vertices over the face, 0 if UV-s not assigned
		'''

	def getFaceVertex (self, faceIndex: int, faceVertexIndex: int) -> int : 
		'''
		get the positional vertex index over the face
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		- faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]
		### Returns:
		- (int) the positional vertex index
		'''

	def getFaceVerts (self, face: int) -> list : 
		'''
		get the list of UV vertex indices over the face, pay attention UV vertices are not same as position vertices
		### Parameters:
		- face (int): the face index
		### Returns:
		- (list) the list of vertex indices
		'''

	def setFaceVerts (self, face: int, vertices: list) : 
		'''
		set the list of positional vertex indices over the face
		### Parameters:
		- face (int): the face index
		- vertices (list): the list of vertex indices
		'''

	def getFaceUvVertex (self, faceIndex: int, faceVertexIndex: int) -> int : 
		'''
		get the UV vertex index over the face
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		- faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]
		### Returns:
		- (int) the UV vertex index, -1 if no UVs over the face
		'''

	def setFaceUvVertex (self, faceIndex: int, faceVertexIndex: int, uvVertexIndex: int) : 
		'''
		set the UV vertex index over the face
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		- faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]
		- uvVertexIndex (int): the UV vertex index, should be in [0..vertsUvCount() - 1]
		'''

	def getFaceNormalVertex (self, faceIndex: int, faceVertexIndex: int) -> int : 
		'''
		get the normal vertex index over the face
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		- faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]
		### Returns:
		- (int) the normal vertex index, -1 if no normals over the face
		'''

	def setFaceNormalVertex (self, faceIndex: int, faceVertexIndex: int, normalVertexIndex: int) : 
		'''
		set the normal vertex index over the face
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		- faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]
		- normalVertexIndex (int): the normal vertex index, should be in [0..vertsNormalCount() - 1]
		'''

	def getFaceUvVerts (self, face: int) -> list : 
		'''
		get the list of UV vertices indices over the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (list) the list of UV vertices indices
		'''

	def getFaceObject (self, faceIndex: int) -> int : 
		'''
		get the object index over the face, see the getObjectsCount(), getObjectName()
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		### Returns:
		- (int) the object index
		'''

	def setFaceObject (self, faceIndex: int, objectIndex: int) : 
		'''
		set the object index for the face, see the getObjectsCount(), getObjectName()
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		- objectIndex (int): the object index to set for the face
		'''

	def getFaceMaterial (self, faceIndex: int) -> int : 
		'''
		get the material index over the face, see the getMaterialsCount(), getMaterialName()
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		### Returns:
		- (int) the material index
		'''

	def setFaceMaterial (self, faceIndex: int, materialIndex: int) : 
		'''
		set the material index over the face, see the getMaterialsCount(), getMaterialName()
		### Parameters:
		- faceIndex (int): the face index, should be in [0..facesCount() - 1]
		- materialIndex (int): the material index to set for the face
		'''

	def getObjectsCount (self) -> int : 
		'''
		returns the objects count in the mesh
		### Returns:
		- (int) the count
		'''

	def getObjectName (self, idx: int) -> str : 
		'''
		get the name of the object
		### Parameters:
		- idx (int): the object index
		### Returns:
		- (str) the name
		'''

	def setObjectName (self, idx: int, name: str) : 
		'''
		set object name
		### Parameters:
		- idx (int): the object index
		- name (str): the new name
		'''

	def addObject (self, name: str) -> int : 
		'''
		add new object to the mesh
		### Parameters:
		- name (str): the object name
		### Returns:
		- (int) the object index
		'''

	def removeObject (self, idx: int) : 
		'''
		remove object from the mesh
		### Parameters:
		- idx (int): the object index
		'''

	def unifyAllObjects (self, name: str = "") : 
		'''
		unify all objects in the mesh, i.e. make one object
		### Parameters:
		- name (str): the name of the new object, if empty, the name of the first object will be used
		'''

	def getMaterialsCount (self) -> int : 
		'''
		get the materials count in the mesh
		### Returns:
		- (int) the count
		'''

	def addMaterial (self, name: str) -> int : 
		'''
		add new material to the mesh
		### Parameters:
		- name (str): the material name
		### Returns:
		- (int) the material index
		'''

	def removeMaterial (self, idx: int) : 
		'''
		remove the material (and corresponding faces) from the mesh
		### Parameters:
		- idx (int): the material index
		'''

	def getMaterialName (self, idx: int) -> str : 
		'''
		get the name of the material
		### Parameters:
		- idx (int): the material index
		### Returns:
		- (str) the name
		'''

	def setMaterialName (self, idx: int, name: str) : 
		'''
		set material name
		### Parameters:
		- idx (int): the material index
		- name (str): the new name
		'''

	def getMaterialTexture (self, idx: int, texture_layer: int) -> str : 
		'''
		get the texture name of the material
		### Parameters:
		- idx (int): the material index
		- texture_layer (int): the texture layer, 0 - color, 1 - gloss, 2 - bump/displacement, 3 - normalmap, 4 - specular color, 5 - emossive (color), 6 - emissive power
		### Returns:
		- (str) the texture path (full or relative to 3DCoat documents folder)
		'''

	def setMaterialTexture (self, idx: int, texture_layer: int, texture_path: str) : 
		'''
		set the texture layer filename of the material
		### Parameters:
		- idx (int): the material index
		- texture_layer (int): the texture layer, 0 - color, 1 - gloss, 2 - bump/displacement, 3 - normalmap, 4 - specular color, 5 - emossive (color), 6 - emissive power
		- texture_path (str): the texture path (full or relative to 3DCoat documents folder)
		'''

	def fromVolume (self, v: Volume, with_subtree: bool = False, all_selected: bool = False) : 
		'''
		extract the mesh from the volume
		### Parameters:
		- v (Volume): the source volume
		- with_subtree (bool): if true, the subtree will be extracted, otherwise the single volume taken
		- all_selected (bool): if true, all selected volumes will be extracted, otherwise only the current volume
		'''

	def fromReducedVolume (self, v: Volume, reduction_percent: float, with_subtree: bool = False, all_selected: bool = False) : 
		'''
		extract the mesh from the volume and reduce it by the given percent
		### Parameters:
		- v (Volume): the source volume
		- reduction_percent (float): 0 means no reduction, 100 means 100% reduction, i.e. the mesh will be reduced to a single triangle
		- with_subtree (bool): if true, the subtree will be extracted, otherwise the single volume taken
		- all_selected (bool): if true, all selected volumes will be extracted, otherwise only the current volume
		'''

	def fromVolumeWithMaxPolycount (self, v: Volume, max_polycount: int, with_subtree: bool = False, all_selected: bool = False) : 
		'''
		extract the mesh from the volume and reduce to the given polycount
		### Parameters:
		- v (Volume): the source volume
		- max_polycount (int): the required polycount
		- with_subtree (bool): if true, the subtree will be extracted, otherwise the single volume taken
		- all_selected (bool): if true, all selected volumes will be extracted, otherwise only the current volume
		'''

	def toVolume (self, v: Volume, transform: mat4 = mat4.Identity, op: BoolOpType = BoolOpType.BOOL_MERGE) : 
		'''
		merge this mesh to the volume object
		### Parameters:
		- v (Volume): the destination volume
		- transform (mat4): the applied transformation
		- op (BoolOpType): the boolean operation to be performed, -1 means no operation, raw merge, 0 - 1, 1 - subtract, 2 - intersect
		'''

	def insertInVolume (self, v: Volume, transform: mat4 = mat4.Identity) : 
		'''
		insert without boolean operation, if the volume is not in surface mode (volumetric) the boolean ADD will be performed anyway
		### Parameters:
		- v (Volume): the destination volume
		- transform (mat4): the transform
		'''

	def addToVolume (self, v: Volume, transform: mat4 = mat4.Identity) : 
		'''
		boolean add to volume
		### Parameters:
		- v (Volume): the destination volume
		- transform (mat4): the transform
		'''

	def subtractFromVolume (self, v: Volume, transform: mat4 = mat4.Identity) : 
		'''
		boolean subtraction of the mesh from the volume
		### Parameters:
		- v (Volume): the destination volume
		- transform (mat4): the transform
		'''

	def intersectWithVolume (self, v: Volume, transform: mat4 = mat4.Identity) : 
		'''
		boolean intersection of the mesh with the volume
		### Parameters:
		- v (Volume): the destination volume
		- transform (mat4): the transform
		'''

	def fromRetopo (self) : 
		'''
		take the whole mesh from the retopo room
		'''

	def fromPaintRoom (self) : 
		'''
		get the mesh from the paint room
		'''

	def reduceToPolycount (self, destination_triangles_count: int) : 
		'''
		reduce the mesh to the given polycount, mesh will be triangulated
		### Parameters:
		- destination_triangles_count (int): the required triangles count, if it is above the existing, nothing happens
		'''

	def triangulate (self) : 
		'''
		triangulate the mesh
		'''

	def booleanOp (self, With: Mesh, op: BoolOpType) : 
		'''
		Perform the boolean operation with the given mesh
		### Parameters:
		- With (Mesh): the mesh to perform the operation with over the current mesh
		- op (BoolOpType): the operation, see BoolOpType (-1 means no operation, 0 - add, 1 - subtract, 2 - intersect)
		'''

	def getMeshVertices (self) -> list : 
		'''
		get the list of all positional vertices of the mesh
		### Returns:
		- (list) the list of vec3
		'''

	def getMeshNormals (self) -> list : 
		'''
		get the list of all normal vertices of the mesh
		### Returns:
		- (list) the list of vec3
		'''

	def getMeshUVs (self) -> list : 
		'''
		get the list of all UV vertices of the mesh
		### Returns:
		- (list) the list of vec2
		'''

	def setMeshVertices (self, positions: list) : 
		'''
		set the list of all positional vertices for the mesh
		### Parameters:
		- positions (list): the list of positions
		'''

	def setMeshNormals (self, normals: list) : 
		'''
		set the list of all normal vertices for the mesh
		### Parameters:
		- normals (list): the list of normals (vec3)
		'''

	def setMeshUVs (self, uvs: list) : 
		'''
		set the list of all UV vertices for the mesh
		### Parameters:
		- uvs (list): the list of UVs (vec2)
		'''

	def setMeshFaces (self, faces: list) : 
		'''
		set the complete list of faces for the mesh
		### Parameters:
		- faces (list): the format of faces is:\n
		amount_ot_vets_in_face1, vertex1_face1, vertex2_face1...vertexN-1_face1,\n
		amount_ot_vets_in_face2, vertex1_face2, vertex2_face2...\n
		...
		'''

	def addMeshVertices (self, positions: list) : 
		'''
		add the list of all positional vertices for the mesh
		### Parameters:
		- positions (list): the list of positions
		'''

	def addMeshNormals (self, normals: list) : 
		'''
		add the list of all normal vertices for the mesh
		### Parameters:
		- normals (list): the list of normals (vec3)
		'''

	def addMeshUVs (self, uvs: list) : 
		'''
		add the list of all UV vertices for the mesh
		### Parameters:
		- uvs (list): the list of UVs (vec2)
		'''

	def addMeshFaces (self, faces: list) : 
		'''
		add the list of faces for the mesh, pay attention, all vertex indices are global over the whole mesh!
		### Parameters:
		- faces (list): the format of faces is:\n
		amount_ot_vets_in_face1, vertex1_face1, vertex2_face1...vertexN-1_face1,\n
		amount_ot_vets_in_face2, vertex1_face2, vertex2_face2...\n
		...
		'''

	def clearVerts (self) : 
		'''
		clear all positional vertices of the mesh
		'''

	def clearUvVerts (self) : 
		'''
		clear all uv vertices of the mesh
		'''

	def clearNormals (self) : 
		'''
		clear all normal vertices of the mesh
		'''

	def clearFaces (self) : 
		'''
		clear all faces of the mesh
		'''

	def removeFaces (self, faces: list) : 
		'''
		remove the set of vertices from the mesh
		### Parameters:
		- faces (list): the list of faces indices to remove
		'''

	def clearObject (self) : 
		'''
		clear all objects
		'''

	def clearMaterials (self) : 
		'''
		clear all materials
		'''

	def ensureMaterialsAndObjectsExist (self) : 
		'''
		ensure that at least one material and one object exist in the mesh
		'''

	def addObject (self, name: str) -> int : 
		'''
		add the named object
		### Parameters:
		- name (str): the name for the object
		### Returns:
		- (int) the index of new object in the objects list
		'''

	def addMaterial (self, name: str) -> int : 
		'''
		add the named material
		### Parameters:
		- name (str): the name for the material
		### Returns:
		- (int) the index of new material in the materials list
		'''

	def removeUnusedObjectsAndMaterials (self) : 
		'''
		remove all unused objects and materials
		'''

	def removeUnusedVerts (self) : 
		'''
		remove all unused vertices
		'''

	def removeUnusedFaces (self) : 
		'''
		remove all faces that contain zero vertices
		'''

	def cutByPlane (self, start: vec3, NormalDirection: vec3) : 
		'''
		Cut off the mesh by the plane, the result is stored in the current mesh, the part of the mesh that is on the side of the negative normal direction is removed
		### Parameters:
		- start (vec3): the start point of the plane
		- NormalDirection (vec3): the normal direction of the plane
		'''

	def cutByDistortedPlane (self, start: vec3, NormalDirection: vec3, noise_degree: float, noise_scale: float, seed: int = 0) : 
		'''
		Cut off the mesh by the distorted plane (using the Perlin noise), the result is stored in the current mesh, the part of the mesh that is on the side of the negative normal direction is removed
		### Parameters:
		- start (vec3): the start point of the plane
		- NormalDirection (vec3): the normal direction of the plane
		- noise_degree (float): the degree of the noise
		- noise_scale (float): the scale of the noise
		- seed (int): the seed for the noise
		'''

	def distortByPerlinNoise (self, noise_degree: float, noise_scale: float, anisotropic: bool = False, seed: int = 0) : 
		'''
		distort the mesh by the Perlin noise
		### Parameters:
		- noise_degree (float): the degree of the noise
		- noise_scale (float): the scale of the noise
		- anisotropic (bool): if false, the noise will be applied in the direction of the normals, othervice the noise directed in random direction regardless the normals
		- seed (int): the seed for the noise
		'''

	def splitDisconnectedParts (self) -> list : 
		'''
		split the mesh into disconnected parts
		### Returns:
		- (list) the list of meshes
		'''

	def symmetry (self, start: vec3, NormalDirection: vec3, resultInQuads: bool) : 
		'''
		apply symmetry to the mesh
		### Parameters:
		- start (vec3): the start point of the plane
		- NormalDirection (vec3): the negative part (regarding the plane normal) of the mesh is removed, replaced with positive part
		- resultInQuads (bool): the cut faces will produce quads instead of triangles
		'''

	def autodetectSymmetryPlanes (self) -> list : 
		'''
		Detect the symmetry planes of the mesh
		### Returns:
		- (list) the list of planes
		'''

	def weld (self, minimal_relative_distance: float = 0.0001) : 
		'''
		weld the mesh, remove all vertices that are closer than minimal_relative_distance*mesh_bound_box_diagonal to each other
		### Parameters:
		- minimal_relative_distance (float): the minimal distance between vertices, relative to the mesh bound box diagonal
		'''

	def getBounds (self) -> boundbox : 
		'''
		get the mesh bound box
		### Returns:
		- (boundbox) the bound box
		'''

	def getVolume (self) -> float : 
		'''
		get the volume of the mesh
		### Returns:
		- (float) the volume
		'''

	def getOpenSurfaceVolume (self, start: vec3, dir: vec3) -> float : 
		'''
		calculate the volume even if the mesh is not closed, in this case we define plane that limits the integration
		### Parameters:
		- start (vec3): the point on that plane
		- dir (vec3): the normalized vector, normal to the plane
		### Returns:
		- (float) the volume
		'''

	def getSquare (self) -> float : 
		'''
		get square of the mesh
		### Returns:
		- (float) the square (area)
		'''

	def getFaceSquare (self, face: int) -> float : 
		'''
		get the squareof the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (float) the square
		'''

	def getFaceUVSquare (self, face: int) -> float : 
		'''
		get the face square in UV space
		### Parameters:
		- face (int): the face index
		### Returns:
		- (float) the square
		'''

	def getFaceNormal (self, face: int) -> vec3 : 
		'''
		get the face normal
		### Parameters:
		- face (int): the face index
		### Returns:
		- (vec3) the face normal
		'''

	def relax (self, degree: float, tangent: bool, crease_angle: float = 180) : 
		'''
		relax the mesh, keep the vertices count
		### Parameters:
		- degree (float): the degree of relax, may be  > 1
		- tangent (bool): should be tangent relax
		- crease_angle (float): the crease angle between faces (degrees), if the angle between faces is less than crease_angle, the edge relaxed
		'''

	@staticmethod
	def box (center: vec3 = vec3.Zero, size: vec3 = vec3.One, xAxis: vec3 = vec3.Zero, yAxis: vec3 = vec3.Zero, zAxis: vec3 = vec3.Zero, detail_size: float = 1, fillet: float = 0.0, nx: int = 0, ny: int = 0, nz: int = 0) -> Mesh : 
		'''
		create the box mesh
		### Parameters:
		- center (vec3): the box center
		- size (vec3): the box size
		- xAxis (vec3): the x-axis direction, if zero, the x-axis is default - (1,0,0)
		- yAxis (vec3): the y-axis direction, if zero, the y-axis is default - (0,1,0)
		- zAxis (vec3): the z-axis direction, if zero, the z-axis is default - (0,0,1)
		- detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
		- fillet (float): the fillet radius
		- nx (int): the number of segments along the x-axis (if all of nx, ny, nz are above zero, it overrides the detail_size)
		- ny (int): the number of segments along the y-axis (if all of nx, ny, nz are above zero, it overrides the detail_size)
		- nz (int): the number of segments along the z-axis (if all of nx, ny, nz are above zero, it overrides the detail_size)
		### Returns:
		- (Mesh) the box mesh
		'''

	@staticmethod
	def sphere (center: vec3 = vec3.Zero, radius: float = 1.0, detail_size: float = 1) -> Mesh : 
		'''
		create the sphere mesh
		### Parameters:
		- center (vec3): the sphere center
		- radius (float): the sphere radius
		- detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
		### Returns:
		- (Mesh) the sphere mesh
		'''

	@staticmethod
	def cylinder (center: vec3 = vec3.Zero, radius: float = 1, height: float = 2, detail_size: float = 1, slices: int = 0, caps: int = 0, rings: int = 0, fillet: float = 0) -> Mesh : 
		'''
		create the cylinder mesh
		### Parameters:
		- center (vec3): the center of the cylinder
		- radius (float): the radius of the cylinder
		- height (float): the height of the cylinder
		- detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
		- slices (int): the number of slices, it overrides the detail_size if all of slices, caps, rings are above zero
		- caps (int): the number of caps, it overrides the detail_size if all of slices, caps, rings are above zero
		- rings (int): the number of rings, it overrides the detail_size if all of slices, caps, rings are above zero
		- fillet (float): the fillet radius
		### Returns:
		- (Mesh) the cylinder mesh
		'''

	@staticmethod
	def cone (center: vec3 = vec3.Zero, radius: float = 1, height: float = 2, detail_size: float = 1, topAxis: vec3 = vec3.AxisY) -> Mesh : 
		'''
		create the cone mesh
		### Parameters:
		- center (vec3): the center of the cone (the cone base center)
		- radius (float): the cone radius
		- height (float): the cone height
		- detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
		- topAxis (vec3): the top axis direction, if zero, the top axis is default - (0,1,0)
		### Returns:
		- (Mesh) the cone mesh
		'''

	@staticmethod
	def plane (center: vec3 = vec3.Zero, sizeX: float = 2, sizeY: float = 2, divisionsX: int = 2, divisionsY: int = 2, xAxis: vec3 = vec3.AxisX, yAxis: vec3 = vec3.AxisY) -> Mesh : 
		'''
		create the single-side plane mesh, the faces normals are put toward the vec3.Cross(xAxis, yAxis)
		### Parameters:
		- center (vec3): the center of the plane
		- sizeX (float): the plane size along the X-axis
		- sizeY (float): the plane size along the Y-axis
		- divisionsX (int): amount of divisions along the X-axis
		- divisionsY (int): amount of divisions along the Y-axis
		- xAxis (vec3): the vector of the X-axis
		- yAxis (vec3): the vector of the Y-axis
		### Returns:
		- (Mesh) the plane mesh
		'''

	@staticmethod
	def hexagonal_plane (center: vec3 = vec3.Zero, sizeX: float = 2, sizeY: float = 2, divisionsX: int = 2, divisionsY: int = 2, xAxis: vec3 = vec3.AxisX, yAxis: vec3 = vec3.AxisY) -> Mesh : 
		'''
		create the single-side triangular plane mesh that consists mostly of quasi equally-sided triangles
		### Parameters:
		- center (vec3): the center of the plane
		- sizeX (float): the plane size along the X-axis
		- sizeY (float): the plane size along the Y-axis
		- divisionsX (int): amount of divisions along the X-axis
		- divisionsY (int): amount of divisions along the Y-axis
		- xAxis (vec3): the vector of the X-axis
		- yAxis (vec3): the vector of the Y-axis
		### Returns:
		- (Mesh) the hexagonal plane mesh
		'''

	@staticmethod
	def text (string: str, font: str = "tahoma", height: float = 10.0, center: vec3 = vec3.Zero, text_direction: vec3 = vec3.AxisX, text_normal: vec3 = vec3.AxisY, thickness: float = 1, align: int = 1) -> Mesh : 
		'''
		Create the text mesh
		### Parameters:
		- string (str): the text string
		- font (str): the font name
		- height (float): the text height
		- center (vec3): the text center
		- text_direction (vec3): the text direction left to right
		- text_normal (vec3): the normal direction of the text
		- thickness (float): the thickness of the text
		- align (int): the text align, 0 - left, 1 - center, 2 - right
		### Returns:
		- (Mesh) the text mesh
		'''

	def createVDM (self, side: int, path_to_exr: str, center: vec3 = vec3.Zero, radius: float = 1, up: vec3 = vec3.AxisZ, x: vec3 = vec3.AxisX, y: vec3 = vec3.AxisY) : 
		'''
		Create the vector displacement map from the mesh and save it as EXR file. The mesh is put on plane at center and clamped by that plane.
		### Parameters:
		- side (int): the EXR  file side size
		- path_to_exr (str): the path to the EXR file
		- center (vec3): the center of the plane
		- radius (float): the radius that should include the mesh
		- up (vec3): the up vector of the plane
		- x (vec3): the x vector of the plane
		- y (vec3): the y vector of the plane
		'''

	def shell (self, thickness_out: float, thickness_in: float, divisions: int = 1) : 
		'''
		add some thickness to the mesh (intrude a bit)
		### Parameters:
		- thickness_out (float): the thickness in the outer direction (extrusion)
		- thickness_in (float): the thickness in the inner direction (intrusion)
		- divisions (int): the amount of divisions of the edge
		'''

	def extrudeOpenEdges (self, distance: float, direction: vec3 = vec3.Zero) -> list : 
		'''
		extrude open edges of the mesh
		### Parameters:
		- distance (float): the distance to extrude
		- direction (vec3): the extrude direction, if zero , the direction is the local vertex normal
		### Returns:
		- (list) s the list of extruded edges, even is the start vertex, odd is the end vertex
		'''

	def expandOpenEdges (self, distance: float) -> list : 
		'''
		extrude open edges of the mesh
		### Parameters:
		- distance (float): the distance to extrude
		### Returns:
		- (list) s the list of extruded edges, even is the start vertex, odd is the end vertex
		'''

	def getOpenEdges (self) -> list : 
		'''
		get the list of open edges
		### Returns:
		- (list) the list of open edges, the even is the start vertex, the odd is the end vertex
		'''

	def getLengthAlongDirection (self, dir: vec3) -> float : 
		'''
		get the mesh size along some axis
		### Parameters:
		- dir (vec3): the axis direction
		### Returns:
		- (float) the size along the axis
		'''

	def getCenterMass (self) -> vec3 : 
		'''
		calculate the center mass of the mesh
		### Returns:
		- (vec3) the center mass of the surface
		'''

class Image:
	def __init__(self): ...
	def __init__(self, im: Image): ...
	def Read (self, name: str) -> bool : 
		'''
		Read the image from the file
		### Parameters:
		- name (str): the image name
		### Returns:
		- (bool) true if loaded successfully
		'''

	def Write (self, name: str) -> bool : 
		'''
		Write the image to file
		### Parameters:
		- name (str): the filename
		### Returns:
		- (bool) true if succeed
		'''

	def FromTexture (self, texture_id: int) -> bool : 
		'''
		Get image from texture
		### Returns:
		- (bool) true if succeed
		'''

	def ToTexture (self) -> int : 
		'''
		Create texture from image
		### Returns:
		- (int) true if succeed
		'''

	def Paste (self, src_data: any, pasteLeft: int = 0, pasteTop: int = 0, cropLeft: int = 0, cropTop: int = 0, cropRight: int = 0, cropBottom: int = 0, flipY: bool = False) -> int : 
		'''
		paste image to image
		### Returns:
		- (int) true if succeed
		'''

	def Pointer (self) -> int : 
		'''
		Pointer to the data
		### Returns:
		- (int) true if succeed
		'''

	def FromArray (self, src_data: any) -> bool : 
		'''
		Get image from texture
		### Returns:
		- (bool) true if succeed
		'''

	def FromArray (self, src_data: any) -> bool : ...
	def FromArray (self, src_data: any) -> bool : ...
	def _py_buffer_info (self) -> any : ...
class symm:
	@staticmethod
	def enable (_enable: bool = True) -> symm : 
		'''
		Enable the symmetry
		### Parameters:
		- _enable (bool): true to enable, false to disable
		### Returns:
		- (symm) reference for the chain-like operations
		'''

	@staticmethod
	def enabled () -> bool : ...
	@staticmethod
	def disable () -> symm : 
		'''
		disable the symmetry
		### Returns:
		- (symm) reference
		'''

	@staticmethod
	def xyz (x: bool, y: bool, z: bool) -> symm : 
		'''
		Enable the XYZ-mirror symmetry
		### Parameters:
		- x (bool): true to enable x-symmetry, false to disable
		- y (bool): true to enable y-symmetry, false to disable
		- z (bool): true to enable z-symmetry, false to disable
		### Returns:
		- (symm) reference
		'''

	@staticmethod
	def is_xyz () -> bool : 
		'''
		check if the XYZ symmetry enabled
		### Returns:
		- (bool) true if this type of the symmetry active
		'''

	@staticmethod
	def x () -> bool : 
		'''
		check x symmetry state
		### Returns:
		- (bool) reference to the x symmetry state
		'''

	@staticmethod
	def y () -> bool : 
		'''
		check y symmetry state
		### Returns:
		- (bool) reference to the y symmetry state
		'''

	@staticmethod
	def z () -> bool : 
		'''
		check z symmetry state
		### Returns:
		- (bool) reference to the z symmetry state
		'''

	@staticmethod
	def axial (n: int, extraMirror: bool = False, stepSymmetry: bool = False) -> symm : 
		'''
		Enable the axial symmetry
		### Parameters:
		- n (int): the order of the axial symmetry
		- extraMirror (bool): add the extra mirror orthogonal to the axis
		- stepSymmetry (bool): enable the step symmetry
		### Returns:
		- (symm) reference
		'''

	@staticmethod
	def is_axial () -> bool : 
		'''
		Check if the axial symmetry enabled
		### Returns:
		- (bool) true if the axial symmetry enabled
		'''

	@staticmethod
	def axialOrder () -> int : 
		'''
		returns the axial symmetry order if axial or axial mirror symmetry enabled
		### Returns:
		- (int) the reference to the order of the axial symmetry
		'''

	@staticmethod
	def extraMirror () -> bool : 
		'''
		returns the state of extra mirror, this is valid only tor the axial symmetry
		### Returns:
		- (bool) the reference to the extra mirror state
		'''

	@staticmethod
	def stepSymmetry () -> bool : 
		'''
		returns the state of step symmetry
		### Returns:
		- (bool) the reference to the step symmetry state
		'''

	@staticmethod
	def axialMirror (n: int, extraMirror: bool = False, stepSymmetry: bool = False) -> symm : 
		'''
		Enable the axial mirror symmetry
		### Parameters:
		- n (int): the order of the symmetry
		- extraMirror (bool): dd the extra mirror orthogonal to the axis
		- stepSymmetry (bool): enable the step symmetry
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def isAxialMirror () -> bool : 
		'''
		Check if the axial mirror symmetry enabled
		### Returns:
		- (bool) true if the axial mirror symmetry enabled
		'''

	@staticmethod
	def translation (numX: int, stepX: float, numY: int, stepY: float, numZ: int, stepZ: float) -> symm : 
		'''
		Enable the translation symmetry
		### Parameters:
		- numX (int): number of x-repeats
		- stepX (float): the step of the x-repeat
		- numY (int): number of y-repeats
		- stepY (float): the step of the y-repeat
		- numZ (int): number of z-repeats
		- stepZ (float): the step of the z-repeat
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def is_translation () -> bool : 
		'''
		Check if the translation symmetry enabled
		### Returns:
		- (bool) the state
		'''

	@staticmethod
	def numX () -> int : 
		'''
		returns the reference to the number of the x repeats if the translational symmetry used
		### Returns:
		- (int) the bool reference
		'''

	@staticmethod
	def stepX () -> float : 
		'''
		returns the reference to the x-step if the translational symmetry used
		### Returns:
		- (float) the value reference
		'''

	@staticmethod
	def numY () -> int : 
		'''
		returns the reference to the number of the y repeats if the translational symmetry used
		### Returns:
		- (int) the bool reference
		'''

	@staticmethod
	def stepY () -> float : 
		'''
		returns the reference to the y-step if the translational symmetry used
		### Returns:
		- (float) the value reference
		'''

	@staticmethod
	def numZ () -> int : 
		'''
		returns the reference to the number of the z repeats if the translational symmetry used
		### Returns:
		- (int) the bool reference
		'''

	@staticmethod
	def stepZ () -> float : 
		'''
		returns the reference to the z-step if the translational symmetry used
		### Returns:
		- (float) the value reference
		'''

	@staticmethod
	def toGlobalSpace () -> symm : 
		'''
		set the symmetry to be in global space
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def toLocalSpace () -> symm : 
		'''
		set the symmetry to be in local space
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def toGeneral () -> symm : 
		'''
		set the symmetry to general case
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def set_start (pos: vec3) -> symm : 
		'''
		set the central point for the symmetry
		### Parameters:
		- pos (vec3): the position (in local or global space, see the localSpace() or globalSpace())
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def start () -> vec3 : 
		'''
		get the start point reference
		### Returns:
		- (vec3) the point reference
		'''

	@staticmethod
	def set_end (pos: vec3) -> symm : 
		'''
		set the end point for the symmetry axis, calling this function enables the general case of the symmetry
		### Parameters:
		- pos (vec3): the position
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def end () -> vec3 : 
		'''
		the end point reference
		### Returns:
		- (vec3) the point reference
		'''

	@staticmethod
	def showSymmetryPlane (show: bool = True) -> symm : 
		'''
		Show or hide the symmetry planes
		### Parameters:
		- show (bool): set true to show
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def setCustomSymetryTransforms (symmetryTransforms: any) -> symm : 
		'''
		enable the custom symmetry, provide the symmetry transfoms
		### Parameters:
		- symmetryTransforms: the list of additional transforms (list of coat.mat4) that will be applied to the any user action
		### Returns:
		- (symm) the reference
		'''

	@staticmethod
	def isCustomSymmetry () -> bool : 
		'''
		Check if the custom symmetry used
		### Returns:
		- (bool) true if the custom symmetry enabled
		'''

	@staticmethod
	def getCurrentTransforms () -> list : 
		'''
		Returns all transforms using the current symmetry state
		### Returns:
		- (list) the resulting list of coat.mat4
		'''

	@staticmethod
	def getCurrentPlanes () -> list : 
		'''
		Returns all symmetry planes using the current symmetry state
		### Returns:
		- (list) the resulting list of planes (coat.plane)
		'''

	@staticmethod
	def disableGlobally () : 
		'''
		Totally disable symmetry, don't forget to enable after all operations!
		'''

	@staticmethod
	def enableGlobally () : 
		'''
		Enable symmetry (preliminary disabled by disableGlobally)
		'''

class SceneElement:
	def __init__(self): ...
	def __init__(self, vo: any): ...
	def __init__(self, c: any): ...
	def __init__(self, other: SceneElement): ...
	def __init__(self): ...
	def __eq__ (self, other: SceneElement) -> bool : ...
	def __ne__ (self, other: SceneElement) -> bool : ...
	def parent (self) -> SceneElement : 
		'''
		get the parent scene graph element
		### Returns:
		- (SceneElement) the parent reference
		'''

	def childCount (self) -> int : 
		'''
		returns the child elements count
		### Returns:
		- (int) child count
		'''

	def child (self, index: int) -> SceneElement : 
		'''
		returns child element by index
		### Parameters:
		- index (int): the index of the element in subtree
		### Returns:
		- (SceneElement) the child reference
		'''

	def isSculptObject (self) -> bool : 
		'''
		Check if it is the sculpt object
		### Returns:
		- (bool) true if this is the sculpt object
		'''

	def isCurve (self) -> bool : 
		'''
		Check if the element is curve
		### Returns:
		- (bool) true if this is curve
		'''

	def setTransform (self, Transform: mat4) -> SceneElement : 
		'''
		Set the transform matrix
		### Parameters:
		- Transform (mat4): the transform matrix
		### Returns:
		- (SceneElement) this element reference
		'''

	def transform (self, Transform: mat4) -> SceneElement : 
		'''
		Additional transform over the object
		### Parameters:
		- Transform (mat4): the matrix
		### Returns:
		- (SceneElement) this element reference
		'''

	def density (self, density_value: float) -> SceneElement : 
		'''
		this command useful if you use voxels, it sets the scale for the volume so that there will be density_value of voxels per mm
		### Parameters:
		- density_value (float): the voxels per mm
		'''

	def transform_single (self, Transform: mat4) -> SceneElement : 
		'''
		Additional transform over the object, not applied to child objects
		### Parameters:
		- Transform (mat4): the matrix
		### Returns:
		- (SceneElement) this element reference
		'''

	def getTransform (self) -> mat4 : 
		'''
		get the scene element transform
		### Returns:
		- (mat4) the transform matrix
		'''

	def clear (self) -> SceneElement : 
		'''
		Clear the element content
		### Returns:
		- (SceneElement) this element reference
		'''

	def name (self) -> str : 
		'''
		get the element name
		### Returns:
		- (str) the name
		'''

	def getLinkedFile (self) -> str : 
		'''
		get the linked file path
		### Returns:
		- (str) the name
		'''

	def setLinkedFile (self, file_path: str) : 
		'''
		set the linked file path
		### Returns:
		- the name
		'''

	def rename (self, name: str) -> SceneElement : 
		'''
		rename the element
		### Parameters:
		- name (str): the new name
		### Returns:
		- (SceneElement) this element reference
		'''

	def addChild (self, name: str) -> SceneElement : 
		'''
		add the child element of the same nature
		### Parameters:
		- name (str): the name
		### Returns:
		- (SceneElement) the new element reference
		'''

	def findInSubtree (self, name: str) -> SceneElement : 
		'''
		find the element in subtree by name
		### Parameters:
		- name (str): the name t seek
		### Returns:
		- (SceneElement) the element reference
		'''

	def iterateSubtree (self, fn: any) -> bool : 
		'''
		iterate over the subtree
		### Parameters:
		- fn: the function to call, return true if need to stop the iterations,
		function looks like\n
		
		::

			def fn(el):
			    ...code...
			    return False or True
			

			el is coat.SceneElement
		### Returns:
		- (bool) true if the callback interrupted the iterations
		'''

	def iterateVisibleSubtree (self, fn: any) -> bool : 
		'''
		iterate over the visible subtree
		### Parameters:
		- fn: the function to call, return true if need to stop the iterations,
		function looks like\n
		
		::

			def fn(el):
			    ...code...
			    return False or True
			

			el is coat.SceneElement
		### Returns:
		- (bool) True if the callback interrupted the iterations
		'''

	def mergeSubtree (self, booleanMerge: bool = False) : 
		'''
		merge all subtree volumes into this
		### Parameters:
		- booleanMerge (bool): use boolean summ to merge. Othervice merge meshes without booleans.
		This option works only for surfave, in voxels it will always do boolean summ
		'''

	def mergeTo (self, dest: SceneElement, op: BoolOpType) : 
		'''
		merge the volume to another one, delete this volume
		### Parameters:
		- dest (SceneElement): the destination
		- op (BoolOpType): the boolean operation type
		'''

	def copyMergeTo (self, dest: SceneElement, op: BoolOpType) : 
		'''
		copy and merge the volume to another one, delete this volume
		### Parameters:
		- dest (SceneElement): the destination
		- op (BoolOpType): the boolean operation type
		'''

	def removeSubtree (self) : 
		'''
		remove the whole subtree
		'''

	def removeSubtreeItem (self, index: int) : 
		'''
		remove one child from the subtree
		### Parameters:
		- index (int): index of the child
		'''

	def remove (self) : 
		'''
		remove this item and all child objects from the scene
		'''

	def duplicate (self) -> SceneElement : 
		'''
		diplicate the item
		### Returns:
		- (SceneElement) the new item reference
		'''

	def duplicateAsInstance (self) -> SceneElement : 
		'''
		create the instance of the object if instancing supported
		### Returns:
		- (SceneElement) the instance reference
		'''

	def changeParent (self, newParent: SceneElement) : 
		'''
		change the parent element for the current one
		### Parameters:
		- newParent (SceneElement): the new parent reference. Pay attention, changing paren is not always possible!
		'''

	def isParentOf (self, child: SceneElement) -> bool : 
		'''
		check if the element is parent of another one
		### Parameters:
		- child (SceneElement): the child element
		### Returns:
		- (bool) true if this element is parent of the child
		'''

	def visible (self) -> bool : 
		'''
		returns own visibility state reference. It does not take into account that parent may be invisible.
		### Returns:
		- (bool) item local visibility reference, you may get and set the visibility with the reference.
		'''

	def setVisibility (self, visible: bool) : 
		'''
		set the visibility of the element
		### Parameters:
		- visible (bool): true if need to be visible
		'''

	def ghost (self) -> bool : 
		'''
		returs the state of ghosting (if available)
		### Returns:
		- (bool) true if ghosted
		'''

	def setGhost (self, ghost: bool) : 
		'''
		sets the ghosting state (if available)
		### Parameters:
		- ghost (bool): set true to ghost
		'''

	def getReferenceColor (self) -> vec4 : 
		'''
		get the reference color for the element
		### Returns:
		- (vec4) the color (r,g,b,a), each channel is 0..1
		'''

	def setReferenceColor (self, color: vec4) : 
		'''
		set the reference color for the element
		### Parameters:
		- color (vec4): the (r, g, b, a) color, each channel is 0..1
		'''

	def Volume (self) -> Volume : 
		'''
		 returns the volume object to operate over voxels or surface
		'''

	def select (self) : 
		'''
		 add the object to selected
		'''

	def selectOne (self) : 
		'''
		 unselect all similar elements and select this one
		'''

	def unselectAll (self) : 
		'''
		 unselect all similar objects
		'''

	def selected (self) -> bool : 
		'''
		 Check if the scene element is selected
		'''

	def collectSelected (self) -> list : 
		'''
		 Collect the selected elements in the subtree (including this element if selected)
		'''

class Volume:
	def __init__(self): ...
	def __init__(self, tb: any): ...
	def __init__(self, vo: any): ...
	def __init__(self, vol: Volume): ...
	def valid (self) -> bool : 
		'''
		checks if object is valid
		### Returns:
		- (bool) true if the volume exists
		'''

	def isSurface (self) -> bool : 
		'''
		Check if in surface mode
		### Returns:
		- (bool) true if in surface mode
		'''

	def isVoxelized (self) -> bool : 
		'''
		Check if in voxel mode
		### Returns:
		- (bool) true if in voxel mode
		'''

	def toSurface (self) : 
		'''
		turn to surface mode, the triangles will be tangentially relaxed
		'''

	def toVoxels (self) : 
		'''
		turn to voxels, auto-voxelize
		'''

	@staticmethod
	def enableVoxelsColoring (enable: bool = True) : 
		'''
		enable or disable the voxel-based coloring. It is applied wherever possible - merging models, brushing, creating parametric voxel figures, etc
		### Parameters:
		- enable (bool): true to enable
		'''

	@staticmethod
	def color (CL: int) : 
		'''
		set the default color to fill voxels if the voxel coloring enabled
		'''

	@staticmethod
	def color (r: float, g: float, b: float, a: float) : 
		'''
		assign the color for the voxel operations
		### Parameters:
		- r (float): red value 0..255
		- g (float): green value 0..255
		- b (float): blue value 0..255
		- a (float): alpha value 0..255
		'''

	@staticmethod
	def color (r: float, g: float, b: float) : 
		'''
		assign the color for the voxel operations
		### Parameters:
		- r (float): red value 0..255
		- g (float): green value 0..255
		- b (float): blue value 0..255
		'''

	@staticmethod
	def color (colorid: str) : 
		'''
		assign the color for the voxel operations
		### Parameters:
		- colorid (str): the color in any suitable form: "RGB", "ARGB", "RRGGBB", "AARRGGBB", "#RGB", "#ARGB", "#RRGGBB", "#AARRGGBB",
		any web-color common name as "red", "green", "purple", google "webcolors"
		'''

	@staticmethod
	def gloss (value: float) : 
		'''
		assign the gloss for the voxel operations, it will work only if the color already assigned
		### Parameters:
		- value (float): the [0..1] value of the gloss
		'''

	@staticmethod
	def roughness (value: float) : 
		'''
		assign the roughness for the voxel operations, it will work only if the color already assigned
		### Parameters:
		- value (float): the [0..1] value of the roughness
		'''

	@staticmethod
	def metal (value: float) : 
		'''
		the metalliclty value for the voxel operations, it will work only if the color already assigned
		### Parameters:
		- value (float): the [0..1] metal value
		'''

	def mergeMesh (self, mesh: Mesh, transform: mat4 = mat4.Identity, op: BoolOpType = BoolOpType.BOOL_MERGE) : 
		'''
		merge the mesh into scene
		### Parameters:
		- mesh (Mesh): the Mesh reference
		- transform (mat4): the transform applied
		- op (BoolOpType): the type of the merge
		'''

	def insertMesh (self, mesh: Mesh, transform: mat4 = mat4.Identity) : 
		'''
		insert the mesh into the volume, in case of voxels this is identical to addMesh, in case of surface, mesh will be inserted without booleans
		### Parameters:
		- mesh (Mesh): the mesh reference
		- transform (mat4): the transform applied
		'''

	def addMesh (self, mesh: Mesh, transform: mat4 = mat4.Identity) : 
		'''
		add the mesh to volume (boolean)
		### Parameters:
		- mesh (Mesh): the mesh reference
		- transform (mat4): the transform applied
		'''

	def subtractMesh (self, mesh: Mesh, transform: mat4 = mat4.Identity) : 
		'''
		subtract the mesh from volume (boolean)
		### Parameters:
		- mesh (Mesh): the mesh reference
		- transform (mat4): the transform applied
		'''

	def intersectWithMesh (self, mesh: Mesh, transform: mat4 = mat4.Identity) : 
		'''
		intersect the volume with the mesh (boolean)
		### Parameters:
		- mesh (Mesh): the mesh reference
		- transform (mat4): the transform applied
		'''

	def mergeMeshWithTexture (self, mesh: Mesh, transform: mat4 = mat4.Identity, op: BoolOpType = BoolOpType.BOOL_MERGE) : 
		'''
		merge the mesh with facture, the volume polygons will be hidden, just the texture will be shown (like leafs in TreesGenerator)
		### Parameters:
		- mesh (Mesh): the mesh that refers texture
		- transform (mat4): the transform applied
		- op (BoolOpType): the boolean operation
		'''

	def getExactDencity (self, x: int, y: int, z: int, fromBackup: bool, cache_ref: any) -> float : 
		'''
		returns the exact voxel density in local space at the exact integer location
		### Parameters:
		- x (int): X-coordinate
		- y (int): Y-coordinate (up)
		- z (int): Z-coordinate
		- fromBackup (bool): take the values from the backup (kept before the modifications started)
		- cache_ref: define the variable coat::VolumeCache and pass there (in same thread) to speed up access;
		### Returns:
		- (float) the density 0..1
		'''

	def getInterpolatedValue (self, pos: vec3, fromBackup: bool) -> float : 
		'''
		returns interolated voxels density
		### Parameters:
		- pos (vec3): position in local space
		- fromBackup (bool): take from the backup
		### Returns:
		- (float) linearly interplated value of the density
		'''

	def getPolycount (self) -> int : 
		'''
		get the volume triangles count
		### Returns:
		- (int) triangles count
		'''

	def getVolume (self) -> float : 
		'''
		get the volume of this object in world coordinates
		### Returns:
		- (float) volume
		'''

	def getSquare (self) -> float : 
		'''
		reg the square of this object in world coordinates
		### Returns:
		- (float) square
		'''

	def calcLocalSpaceAABB (self) -> boundbox : 
		'''
		Calculate the Axis - Aligned Bound Box of the object in local space
		### Returns:
		- (boundbox) the boundary as comms::cBounds
		'''

	def calcWorldSpaceAABB (self) -> boundbox : 
		'''
		Calculate the Axis - Aligned Bound Box of the object in world space
		### Returns:
		- (boundbox) the boundary as comms::cBounds
		'''

	def tree (self) -> any : 
		'''
		returns the low-level object (VoxTreeBranch) for all low-level operations
		### Returns:
		- (any) the VoxTreeBranch* pointer
		'''

	def vo (self) -> any : 
		'''
		returns the low-level object (VolumeObject) for all low-level operations
		### Returns:
		- (any) the VolumeObject* pointer
		'''

	def cell (self, cx: int, cy: int, cz: int, create: bool, backup: bool) -> any : 
		'''
		get the cell by cell coordinates, each cell is 8*8*8
		### Parameters:
		- cx (int): cell x
		- cy (int): cell y
		- cz (int): cell z
		- create (bool): pass true if you want to create the cell if it does not exist
		- backup (bool): drop the cell to backup (if not already dropped)
		### Returns:
		- (any) the pointer to the VolumeCell
		'''

	def dirty (self, cx: int, cy: int, cz: int) : 
		'''
		mark the cell as dirty. This is required if you
		'''

	def setOpacity (self, Opacity: float) : 
		'''
		set the volume opacity
		### Parameters:
		- Opacity (float): the 0..1 opacity value
		'''

	def relaxGpu (self, center: vec3, Radius: float, degree: float) : 
		'''
		fast voxel-based relax within the sphere with the gradual falloff. It works only in voxel mode.
		### Parameters:
		- center (vec3): the center of
		- Radius (float): the radius of the influence
		- degree (float): the relax degree, < 1
		'''

	def relaxVoxels (self, count: int) : 
		'''
		relax the whole volume, works only for voxels
		### Parameters:
		- count (int): the count of relax steps
		'''

	def relaxSurface (self, degree: float, tangent: bool = False, keep_sharp_boolean_edges: bool = False) : 
		'''
		relax the object in surface mode
		### Parameters:
		- degree (float): the degree of smoothing, it may be >1 for the stronger relax
		- tangent (bool): use tangent relax
		- keep_sharp_boolean_edges (bool): keep the sharp edges appeared due to bolean operations
		'''

	def relaxOpenEdges (self, nTimes: int) : 
		'''
		relax the open edges of the mesh, it is applicable only to the surface mode
		### Parameters:
		- nTimes (int): amount of iterations
		'''

	def inScene (self) -> SceneElement : 
		'''
		Get the Volume placement in the scene
		### Returns:
		- (SceneElement) the SceneElement
		'''

	def clear (self) : 
		'''
		Clear and pass to the Undo queue
		'''

	def clearNoUndo (self) : 
		'''
		Clear quickly, without affecting the Undo queue
		'''

	def assignShader (self, shaderName: str) : 
		'''
		set the shader for the Volume
		### Parameters:
		- shaderName (str): the shader name as it is shown in the shader's hint
		'''

	def setBoolShaderProperty (self, property: str, value: bool) : ...
	def setFloatShaderProperty (self, property: str, value: float) : ...
	def setColorShaderProperty (self, property: str, value: int) : ...
	def closeHoles (self, maxSize: int) : 
		'''
		Close the holes
		### Parameters:
		- maxSize (int): max hole size (edges over the primeter)
		'''

	@staticmethod
	def checkIfMoldingLicenseAvailable () -> bool : 
		'''
		check if molding allowed
		### Returns:
		- (bool) true if the molding license available
		'''

	@staticmethod
	def setMoldingParams (direction: vec3, tapering_angle: float = 0, undercuts_density: float = 1.0, decimation_limit_millions: float = 10, perform_subtraction: bool = True) : 
		'''
		set the parameters for the molding
		### Parameters:
		- direction (vec3): the molding direction
		- tapering_angle (float): the tapering angle in degrees
		- undercuts_density (float): the additional density for the undercuts
		- decimation_limit_millions (float): decimate the final shape if it has triangles count more than this value
		- perform_subtraction (bool): set false if no need to subtract the molding from the molding shapes
		'''

	def removeUndercuts (self) : 
		'''
		remove undercuts for the current volume
		'''

	def basRelief (self, start_point: vec3 = vec3.Zero) : 
		'''
		perform the bas-relief for the current volume
		### Parameters:
		- start_point (vec3): the cut point
		'''

	@staticmethod
	def setAutomaticMoldingBox () : 
		'''
		set the molding bound box to be automatic
		'''

	@staticmethod
	def setMoldingBox (width: float, length: float, thickness: float) : 
		'''
		set the molding bound box to be user-defined, not automatic
		### Parameters:
		- width (float): the width of the box
		- length (float): the length of the box
		- thickness (float): the thickness of the box
		'''

	@staticmethod
	def setMoldingBorder (width: float = 0) : 
		'''
		set the molding border around the parting line to fade to the plane, if it is zero, the final shape will not fade to plane
		### Parameters:
		- width (float): the width in mm or other default units
		'''

	def generateMoldingCurves (self) : 
		'''
		generate the automatic molding curves
		'''

	def automaticMolding (self) : 
		'''
		perform the automatic molding
		'''

	def curveBasedMolding (self) : 
		'''
		perform the curve-based mold
		'''

	def subtractWithoutUndecuts (self) : 
		'''
		subtract the current undercutted object from the preliminary generated molding shapes
		'''

	def generateMoldingTest (self) -> SceneElement : 
		'''
		generate the figure that fills the gap between the molding shapes
		### Returns:
		- (SceneElement) the generated scene element reference
		'''

	def findMoldingTop (self) -> SceneElement : 
		'''
		find the top molding shape (that was previously generated)
		### Returns:
		- (SceneElement) the top shape reference
		'''

	def findMoldingBottom (self) -> SceneElement : 
		'''
		find the bottom molding shape (that was previously generated)
		### Returns:
		- (SceneElement) the bottom shape reference
		'''

	def findMoldingTest (self) -> SceneElement : 
		'''
		find the test molding test shape (that was previously generated)
		### Returns:
		- (SceneElement) the test shape reference
		'''

	def removeMoldingShapes (self) : 
		'''
		remove all molding intermediate shapes, tests, etc.
		'''

	def assignLiveBooleans (self, operation: int) : 
		'''
		Apply the live booleans over the sculpt mesh, it is available for voxels only
		### Parameters:
		- operation (int): 0 - stop live booleans, 1 - subtract from the parent, 2 - intersect, 3 - union
		'''

	def collapseBollTree (self) : 
		'''
		collapse the boolean tree, it is available for this volume
		'''

class settings:
	@staticmethod
	def valueExists (ID: str) -> bool : 
		'''
		returns true if the value in settings exists
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		### Returns:
		- (bool) true if identifier exists
		'''

	@staticmethod
	def getBool (ID: str) -> bool : 
		'''
		get the boolen value from the settings
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		### Returns:
		- (bool) the boolean value, false if not exists or casting impossible
		'''

	@staticmethod
	def getString (ID: str) -> str : 
		'''
		get the string value from the settings
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		### Returns:
		- (str) the string value, empty if not exists
		'''

	@staticmethod
	def getFloat (ID: str) -> float : 
		'''
		get the float value from the settings
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		### Returns:
		- (float) the float value, 0 if not exists or casting impossible
		'''

	@staticmethod
	def getInt (ID: str) -> int : 
		'''
		get the integer value from the settings
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		### Returns:
		- (int) the integer value, 0 if not exists or casting impossible
		'''

	@staticmethod
	def setBool (ID: str, value: bool) -> bool : 
		'''
		set the boolean value to the settings
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		- value (bool): the value to set
		### Returns:
		- (bool) true if the value was set successfully
		'''

	@staticmethod
	def setString (ID: str, value: str) -> bool : 
		'''
		set the string value to the settings
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		- value (str): the value to set
		### Returns:
		- (bool) true if the value was set successfully
		'''

	@staticmethod
	def setFloat (ID: str, value: float) -> bool : 
		'''
		set the float value to the settings
		### Parameters:
		- ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
		- value (float): the value to set
		### Returns:
		- (bool) true if the value was set successfully
		'''

	@staticmethod
	def setInt (ID: str, value: int) -> bool : 
		'''
		set the integer value to the settings
		### Parameters:
		- value (int): the value to set
		### Returns:
		- (bool) true if the value was set successfully
		'''

	@staticmethod
	def saveSettings () : 
		'''
		save all changed settings
		'''

	@staticmethod
	def resetSettings (ResetGeneralSettings: bool = True, ResetHiddenSet: bool = True, ResetHotkeys: bool = True, RestNavigation: bool = True, ResetPresets: bool = True, ResetTheme: bool = True, ResetWindows: bool = True) : 
		'''
		reset all settings to default values, application will restart
		### Parameters:
		- ResetGeneralSettings (bool): reset general settings
		- ResetHiddenSet (bool): reset the hidden UI elements list
		- ResetHotkeys (bool): reset the hotkeys
		- RestNavigation (bool): reset the navigation settings
		- ResetPresets (bool): reset the presets
		- ResetTheme (bool): reset the theme
		- ResetWindows (bool): reset the floating windows placement
		'''

	@staticmethod
	def listAllSettings () -> list : 
		'''
		get the list of all available settings
		### Returns:
		- (list) the pairs of strings, first - option identifier, second - the value, pay attention boolean values are "true" and "false" (like in c++)
		'''

	@staticmethod
	def pressButton (button_name: str) : 
		'''
		triger some action in settings
		### Parameters:
		- button_name (str): the button name, look the identifier in the listAllSettings() output
		'''

class Scene:
	@staticmethod
	def clearScene (askUser: bool = False) : 
		'''
		clear the whole scene
		### Parameters:
		- askUser (bool): set true to ask user for unsaved changes
		'''

	@staticmethod
	def current () -> SceneElement : 
		'''
		returns the current sculpt object
		### Returns:
		- (SceneElement) current object reference
		'''

	@staticmethod
	def sculptRoot () -> SceneElement : 
		'''
		get the root of all sculpt objects
		### Returns:
		- (SceneElement) the root reference
		'''

	@staticmethod
	def curvesRoot () -> SceneElement : 
		'''
		get the root of all curves
		### Returns:
		- (SceneElement) the root reference
		'''

	@staticmethod
	def getLayer (name: str, addIfNotExists: bool = True) -> int : 
		'''
		get the Layer ID by name, add the layer if not exists
		### Parameters:
		- name (str): layer name
		- addIfNotExists (bool): set true to add layer if it does not exist
		### Returns:
		- (int) layer identifier
		'''

	@staticmethod
	def getLayerName (LayerID: int) -> str : 
		'''
		get the layer name
		### Parameters:
		- LayerID (int): the layer identifier
		### Returns:
		- (str) the layer name
		'''

	@staticmethod
	def setLayerName (LayerID: int, name: str) : 
		'''
		set the layer name
		### Parameters:
		- LayerID (int): the layer identifier
		- name (str): the new name
		'''

	@staticmethod
	def getLayerBlending (LayerID: int) -> int : 
		'''
		get the layer blending mode
		### Parameters:
		- LayerID (int): the layer identifier
		### Returns:
		- (int) the index of blending mode as it is ordered in the Layers UI
		'''

	@staticmethod
	def setLayerBlending (LayerID: int, mode: int) : 
		'''
		set the layer blending mode
		### Parameters:
		- LayerID (int): the layer identifier
		- mode (int): the index of blending mode as it is ordered in the Layers UI
		'''

	@staticmethod
	def getCurrentLayer () -> int : 
		'''
		get current layer identifier
		### Returns:
		- (int) the current layer identifier
		'''

	@staticmethod
	def setCurrentLayer (LayerID: int) : 
		'''
		set the current layer
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def mergeVisibleLayers () : 
		'''
		merge all visible layers
		'''

	@staticmethod
	def mergeLayerDown (LayerID: int) : 
		'''
		merge the layer down
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def applyLayerBlending (LayerID: int) : 
		'''
		apply layer blending
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def invalidateLayer (LayerID: int) : 
		'''
		refresh the layer appearance in scene
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def setActiveLayer (LayerID: int) : 
		'''
		activate the layer
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def removeLayer (LayerID: int) : 
		'''
		remove the layer
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def layerIsEmpty (layerID: int) -> bool : 
		'''
		Check if the layer is empty
		### Parameters:
		- layerID (int): the layer identifier
		### Returns:
		- (bool) true if the layer is empty
		'''

	@staticmethod
	def removeEmptyLayers () : 
		'''
		remove all unused layers
		'''

	@staticmethod
	def layerVisible (LayerID: int) -> bool : 
		'''
		return the layer visibility
		'''

	@staticmethod
	def setLayerVisibility (LayerID: int, Visible: bool) : 
		'''
		set the layer visibility
		### Parameters:
		- Visible (bool): the visibility
		'''

	@staticmethod
	def setLayerColorOpacity (LayerID: int, Opacity: float) : 
		'''
		set the layer opacity
		### Parameters:
		- LayerID (int): the layer identifier
		- Opacity (float): the color opacity
		'''

	@staticmethod
	def setLayerDepthOpacity (LayerID: int, Opacity: float) : 
		'''
		set the layer depth opacity
		### Parameters:
		- LayerID (int): the layer identifier
		- Opacity (float): the depth opacity
		'''

	@staticmethod
	def setLayerMetalnessOpacity (LayerID: int, Opacity: float) : 
		'''
		set the layer metalness opacity
		### Parameters:
		- LayerID (int): the layer identifier
		- Opacity (float): the metalness opacity
		'''

	@staticmethod
	def setLayerGlossOpacity (LayerID: int, Opacity: float) : 
		'''
		set the layer gloss/roughness opacity
		### Parameters:
		- LayerID (int): the layer identifier
		- Opacity (float): the gloss/roughness opacity
		'''

	@staticmethod
	def assignLayerMask (LayerID: int) -> int : 
		'''
		assign the mask to the layer if it is not assigned before
		### Parameters:
		- LayerID (int): the layer identifier to assign the mask
		### Returns:
		- (int) the mask identifier
		'''

	@staticmethod
	def removeLayerMask (LayerID: int) : 
		'''
		remove the layer mask
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def extractMaskAsLayer (LayerID: int) : 
		'''
		If the layer has the mask attached, the mask will be extracted as a new layer and the masking disabled
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def setMaskForTheLayer (LayerID: int, MaskLayerID: int) : 
		'''
		set the MaskLayerID to be used as mask for the LayerID. The MaskLayerID will disappear among the layers list
		### Parameters:
		- LayerID (int): the layer to be masked
		- MaskLayerID (int): the mask layer
		'''

	@staticmethod
	def enableLayerMask (LayerID: int, enable: bool) : 
		'''
		enable or disable the layer mask
		### Parameters:
		- LayerID (int): the layer identifier
		- enable (bool): true to enable, false to disable
		'''

	@staticmethod
	def isLayerMaskEnabled (LayerID: int) -> bool : 
		'''
		check if the mask is enabled for the layer
		### Parameters:
		- LayerID (int): the layer identifier
		### Returns:
		- (bool) true if masking is enabled and assigned, false if disabled or not assigned
		'''

	@staticmethod
	def invertLayerMask (LayerID: int) : 
		'''
		invert the layer mask (if assigned)
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def getLayerMaskLayer (LayerID: int) -> int : 
		'''
		get the mask identifier assigned to the layer
		### Parameters:
		- LayerID (int): the layer identifier
		### Returns:
		- (int) the mask layer identifier
		'''

	@staticmethod
	def disableLayerMask (LayerID: int) : 
		'''
		disable the mask for the layer
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def enableLayerMask (LayerID: int) : 
		'''
		enable the mask for the layer
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def maskEnabled (LayerID: int) -> bool : 
		'''
		check if the mask is enabled for the layer
		### Parameters:
		- LayerID (int): the layer identifier
		### Returns:
		- (bool) true if enabled, false if disabled of not assigned
		'''

	@staticmethod
	def setClippingLayer (LayerID: int) : 
		'''
		set this layer as clipping layer
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def disableClippingLayer (LayerID: int) : 
		'''
		disable the clipping layer
		### Parameters:
		- LayerID (int): the layer identifier
		'''

	@staticmethod
	def PaintObjectsCount () -> int : 
		'''
		Get the count of paint objects in scene
		### Returns:
		- (int) the amount
		'''

	@staticmethod
	def PaintMaterialCount () -> int : 
		'''
		Get the count of paint materials
		### Returns:
		- (int) the amount
		'''

	@staticmethod
	def PaintUVSetsCount () -> int : 
		'''
		Get the paint UV-sets (textures) count
		### Returns:
		- (int) the amount
		'''

	@staticmethod
	def RemovePaintObject (idx: int) : 
		'''
		Remove the paint object
		### Parameters:
		- idx (int): the index of the object
		'''

	@staticmethod
	def RemovePaintMaterial (idx: int) : 
		'''
		Remove the paint material
		### Parameters:
		- idx (int): the index of the material
		'''

	@staticmethod
	def RemoveUVSet (idx: int) : 
		'''
		Remove the UV-set (texture)
		### Parameters:
		- idx (int): the index of the UV-set (texture)
		'''

	@staticmethod
	def PaintObjectName (idx: int) -> str : 
		'''
		Get the reference to the object name
		### Parameters:
		- idx (int): index of the object
		### Returns:
		- (str) the reference
		'''

	@staticmethod
	def PaintMaterialName (idx: int) -> str : 
		'''
		Get the reference to the material mane
		### Parameters:
		- idx (int): the index of the material
		### Returns:
		- (str) the reference
		'''

	@staticmethod
	def PaintUVSetName (idx: int) -> str : 
		'''
		Get the reference to the UV set name
		### Parameters:
		- idx (int): the index of the UV set
		### Returns:
		- (str) the reference
		'''

	@staticmethod
	def importMesh (filename: str, transform: mat4 = mat4.Identity) -> SceneElement : 
		'''
		import mesh into scene, it is the same as File->Import->Import mesh for vertex painting/reference ... This is the optimal way to import mesh into the scene
		### Parameters:
		- filename (str): the filename, if it is empty, the dialog appears
		### Returns:
		- (SceneElement) the scene element reference
		'''

	@staticmethod
	def ScaleSceneVisually (scale: float) : 
		'''
		Scale the whole scene visually but keep the export size
		### Parameters:
		- scale (float): the scale, >1 means objects become bigger in scene
		'''

	@staticmethod
	def ScaleSceneUnits (scale: float) : 
		'''
		Keep the scene visial size in scene, but scale the export size
		### Parameters:
		- scale (float): the scale, >1 means objects become bigger in export
		'''

	@staticmethod
	def GetSceneScale () -> float : 
		'''
		the length of 1 scene unit when you export the scene
		### Returns:
		- (float) the 1 unit of scene length in the exported model
		'''

	@staticmethod
	def GetSceneUnits () -> str : 
		'''
		get the name of the current scene units
		### Returns:
		- (str) the name as string
		'''

	@staticmethod
	def setSceneUnits (units: str) -> bool : 
		'''
		Set the scene units without actual scaling the scene to new units, just name change
		### Parameters:
		- units (str): the name of new units
		### Returns:
		- (bool) false if units are not supported
		'''

	@staticmethod
	def getSceneShift () -> vec3 : 
		'''
		get the scene shift value, look the Edit->Scale master->X,Y,Z
		'''

	@staticmethod
	def setSceneShift (shift: vec3) : 
		'''
		set the scene shift value, look the Edit->Scale master->X,Y,Z
		### Parameters:
		- shift (vec3): the new shift value
		'''

	@staticmethod
	def getAvailableUnits () -> list : 
		'''
		Get the list of all available units
		### Returns:
		- (list) the list of strings
		'''

	@staticmethod
	def convertSceneUnits (destination_unit_name: str) -> bool : 
		'''
		Convert the scene units to the new units, the scene scale will be changed, visual size will be kept
		### Parameters:
		- destination_unit_name (str): the name of new units
		### Returns:
		- (bool) false if units are not supported
		'''

class RenderRoom:
	@staticmethod
	def toRenderRoom () : 
		'''
		get to the render room to be able to render
		'''

	@staticmethod
	def restartRendering () : 
		'''
		if the realtime render enabled the command will restart the rendering from scratch
		'''

	@staticmethod
	def setCustomRenderSize (width: int, height: int) : 
		'''
		set the render output width
		### Parameters:
		- width (int): the width
		- height (int): the height
		'''

	@staticmethod
	def setRenderResult (filename: str) : 
		'''
		set the render output filename
		### Parameters:
		- filename (str): the filename
		'''

	@staticmethod
	def renderFrame () : 
		'''
		render to the output file
		'''

	@staticmethod
	def enableRealtimeRendering (enable: bool) : 
		'''
		enable or disable the realtime rendering
		### Parameters:
		- enable (bool): set true to enable
		'''

	@staticmethod
	def isRealtimeRenderingEnabled () -> bool : 
		'''
		get the realtime rendering state
		### Returns:
		- (bool) true if enabled
		'''

	@staticmethod
	def setExposure (exposure: float) : 
		'''
		set the exposure value for the rendering (in render room)
		### Parameters:
		- exposure (float): the exposure value, usually 0..1, bigger values allowed as well
		'''

	@staticmethod
	def getExposure () -> float : 
		'''
		get the exposure value for the rendering (in render room)
		### Returns:
		- (float) the exposure value, around (0..1)
		'''

	@staticmethod
	def setEnvironmentLight (envlight: float) : 
		'''
		set the brightness of the environment light (spherical environment)
		### Parameters:
		- envlight (float): the brightness, usually 1
		'''

	@staticmethod
	def getEnvironmentLight () -> float : 
		'''
		get the brightness of the environment light (spherical environment)
		### Returns:
		- (float) the brightness, usually 1
		'''

	@staticmethod
	def setDOFDegree (degree: float) : 
		'''
		set the depth of field (DOF) degree
		### Parameters:
		- degree (float): the degree of DOF, 0 means no DOF, 1 means full DOF
		'''

	@staticmethod
	def getDOFDegree () -> float : 
		'''
		get the depth of field (DOF) degree
		### Returns:
		- (float) the degree of DOF, 0 means no DOF, 1 means full DOF
		'''

	@staticmethod
	def getLightsCount () -> int : 
		'''
		get the amount of additional directional lighte
		### Returns:
		- (int) the amount
		'''

	@staticmethod
	def addLight () -> int : 
		'''
		add the additional directional light
		### Returns:
		- (int) the index of the light for all further operations
		'''

	@staticmethod
	def removeLight (idx: int) : 
		'''
		remove the additional directional light
		### Parameters:
		- idx (int): the index of the light
		'''

	@staticmethod
	def removeAllLights () : 
		'''
		remove all additional directional lights
		'''

	@staticmethod
	def setLightDirection (idx: int, dir: vec3) : 
		'''
		set the direction for the additional light
		### Parameters:
		- idx (int): the index of the light
		- dir (vec3): the light direction
		'''

	@staticmethod
	def getLightDirection (idx: int) -> vec3 : 
		'''
		get the direction for the additional light
		### Parameters:
		- idx (int): the index of the light
		### Returns:
		- (vec3) the light direction
		'''

	@staticmethod
	def setLightScattering (idx: int, scattering: float) : 
		'''
		set the light scattering for the additional light
		### Parameters:
		- idx (int): the index of the light
		- scattering (float): the light scattering value
		'''

	@staticmethod
	def getLightScattering (idx: int) -> float : 
		'''
		get the light scattering for the additional light
		### Parameters:
		- idx (int): the index of the light
		### Returns:
		- (float) the light scattering value
		'''

	@staticmethod
	def setLightColor (idx: int, color: vec3 = vec3.One) : 
		'''
		set the light color for the additional light
		### Parameters:
		- idx (int): the index of the light
		- color (vec3): the light color (r,g,b) wintin [0..1] range, if need more intensity, increase the light intensity value
		'''

	@staticmethod
	def getLightColor (idx: int) -> vec3 : 
		'''
		get the light color for the additional light
		### Parameters:
		- idx (int): the index of the light
		### Returns:
		- (vec3) the light color (r,g,b)
		'''

	@staticmethod
	def setLightIntensity (idx: int, intensity: float) : 
		'''
		set the light intensity for the additional light
		### Parameters:
		- idx (int): the index of the light
		- intensity (float): the light intensity value
		'''

	@staticmethod
	def getLightIntensity (idx: int) -> float : 
		'''
		get the light intensity for the additional light
		### Parameters:
		- idx (int): the index of the light
		### Returns:
		- (float) the light intensity value
		'''

	@staticmethod
	def setRaysPerFrame (count: int) : 
		'''
		set rays per frame for the rendering
		### Parameters:
		- count (int): the rays per frame count
		'''

	@staticmethod
	def getRaysPerFrame () -> int : 
		'''
		get rays per frame for the rendering
		### Returns:
		- (int) the rays per frame count
		'''

	@staticmethod
	def setAA (AA: bool) : 
		'''
		set the anti-aliasing (AA) rendering state
		### Parameters:
		- AA (bool): true to enable
		'''

	@staticmethod
	def getAA () -> bool : 
		'''
		get the anti-aliasing (AA) rendering state
		### Returns:
		- (bool) true if enabled
		'''

class Curve(SceneElement):
	def __init__(self): ...
	def __init__(self): ...
	def __init__(self, ob: any): ...
	def __init__(self, el: SceneElement): ...
	def __assign__ (self, el: SceneElement) -> Curve : ...
	def pointsCount (self) -> int : 
		'''
		get the base points cout in the curve
		### Returns:
		- (int) the points count
		'''

	def point (self, idx: int) -> any : 
		'''
		get the base point pointer
		### Parameters:
		- idx (int): the index in the points array
		### Returns:
		- (any) the pointer to the point if it is in range, nullptr othervice
		'''

	def removePoints (self, index: int, count: int) : 
		'''
		remove the points out of the curve base points list
		### Parameters:
		- index (int): the start point index
		- count (int): points count to remove
		'''

	def curve (self) -> any : 
		'''
		get the low-level ObjeCurveObject pointer
		### Returns:
		- (any) the OneCurveObject pointer
		'''

	def renderPointsCount (self) -> int : 
		'''
		returns the visual points count. Visual points used to render the curve in the viewport as set of straight lines.
		### Returns:
		- (int) the count
		'''

	def renderPoint (self, idx: int) -> any : 
		'''
		returns the visual point reference
		### Parameters:
		- idx (int): the point index
		### Returns:
		- (any) the pointer to the point if it is in range, nullptr othervice
		'''

	def updatePoints (self) : 
		'''
		update the visual points if need. Use this function if you cahnge the curve. Change the multiple parameters and then call this function if you need visual points.
		Othervice they will be updated automatically later.
		'''

	def closed (self) -> bool : 
		'''
		returns the reference to the closed state of the curve to get or set the value
		### Returns:
		- (bool) the reference
		'''

	def add (self, p: vec3, normal: vec3, Radius: float) : 
		'''
		add the point to the curve without the direct options the tangents
		### Parameters:
		- p (vec3): the point in space
		- normal (vec3): the normal to the point
		- Radius (float): the point radius
		'''

	def addSharp (self, p: vec3, normal: vec3, Radius: float) : 
		'''
		add the sharp point to the curve
		### Parameters:
		- p (vec3): the point in space
		- normal (vec3): the normal to the point
		- Radius (float): the point radius
		'''

	def addSmooth (self, p: vec3, normal: vec3, Radius: float) : 
		'''
		add the smooth B-spline-like point to the curve
		### Parameters:
		- p (vec3): the position
		- normal (vec3): the normal
		- Radius (float): the radius
		'''

	def add (self, p: vec3, normal: vec3, inTangent: vec3, outTangent: vec3, Radius: float) : 
		'''
		add the point with two independent tangents.
		### Parameters:
		- p (vec3): the position
		- normal (vec3): the normal
		- inTangent (vec3): input tangent, it is usually approximately directed from the current to the previous point
		- outTangent (vec3): output tangent, it is usually approximately directed from the current to the next point
		- Radius (float): the radius
		'''

	def add (self, p: vec3, normal: vec3, inOutTangent: vec3, Radius: float) : 
		'''
		add the point with the opposite tangents
		### Parameters:
		- p (vec3): the position
		- normal (vec3): the normal
		- inOutTangent (vec3): the tangent, it is usually approximately directed from the current to the next point
		- Radius (float): the radius
		'''

	def tubeToMesh (self, mesh: Mesh, hemisphere: bool) : 
		'''
		create the solid tube around the curve using the points radius
		### Parameters:
		- mesh (Mesh): this mesh will be created as the result of the operation
		- hemisphere (bool): set true if need the ends of the rode to be hemispheres
		'''

	def fill (self, mesh: Mesh, thickness: float, relax_count: float = 0, details_level: float = 1, extrusion: float = 0) : 
		'''
		Create the curved surface around the curve
		### Parameters:
		- mesh (Mesh): the resulting mesh
		- thickness (float): the thickness of the object
		- relax_count (float): the relaxation degree
		- details_level (float): the details levels
		- extrusion (float): the additional extrusion
		'''

class SphericalCollision:
	def __init__(self): ...
	def __init__(self, cellsize: float): ...
	def __init__(self): ...
	def setUnit (self, u: float) : 
		'''
		set the cell size, the cell space should be empty
		### Parameters:
		- u (float): the cell size that should be approximately around the average sphere size
		'''

	def clear (self) : 
		'''
		remove all spheres
		'''

	def addSphere (self, p: vec3, radius: float) -> int : 
		'''
		add the sphere into the space
		### Parameters:
		- p (vec3): the position
		- radius (float): the radius
		### Returns:
		- (int) the sphere index, you may refer it later using the spher(index) function
		'''

	def collides (self, p: vec3, radius: float) -> vec3 : 
		'''
		check if sphere intersects other spheres in the space
		### Parameters:
		- p (vec3): position
		- radius (float): radius
		### Returns:
		- (vec3) the repelling force, it is zero if no collision happened.
		'''

	def sphere (self, idx: int) -> vec4 : 
		'''
		get the sphere parameters by index
		### Parameters:
		- idx (int): the sphere index (previously returned by addSphere)
		### Returns:
		- (vec4) the position (xyz) and radius (w) as vec4
		'''

class ui:
	@staticmethod
	def cmd (id: str, fn: any = None) -> bool : 
		'''
		execute some action in UI as if you pressed on some control
		
		The ID may be taken from the UI by clicking RMB+MMB, then the ID will appear in the clipboard (look Edit->Prferences->General->Script info type).
		 If the element triggers modal dialog, the execution will be paused till the modal dialog will be closed, but the callback will be called each frame in modal dialog,
		 so you will be able to control what happens in the modal dialog.
		### Parameters:
		- id (str): the identifier taken from the UI
		- fn: the callback/lambda that will be called each frame till you are within the modal dialog. It looks like\n
		
		::

			def _callback():
			    cmd("#id_to_press")
			    ...code...
			

		### Returns:
		- (bool) True if the element found and the operation executed
		'''

	@staticmethod
	def wait (id: str, max_seconds: float) -> bool : 
		'''
		wait till the element id will appear in the UI. The element will not be clicked. The max wait time is max_seconds.
		### Parameters:
		- id (str): The ID we wait to appear
		- max_seconds (float): the max wait time (seconds)
		### Returns:
		- (bool) true if the element appeared
		'''

	@staticmethod
	def presentInUI (id: str) -> bool : 
		'''
		Check if the elemnt present in the UI
		### Parameters:
		- id (str): the identifier
		### Returns:
		- (bool) true if the element is present
		'''

	@staticmethod
	def highlight (id: str, milliseconds: float) : 
		'''
		highlight the UI element for a while
		### Parameters:
		- id (str): the ID of the element
		- milliseconds (float): the time to highlight, milliseconds
		'''

	@staticmethod
	def enablePenChannel (i: int, enabled: bool) : 
		'''
		enable or disable the pen channel
		### Parameters:
		- i (int): the channel: 0 - depth, 1 - color, 3 - gloss, 2 - currently unused
		- enabled (bool): true to enable
		'''

	@staticmethod
	def isEnabledPenChannel (i: int) -> bool : 
		'''
		check if the pen channel is enabled
		### Parameters:
		- i (int): the cannel: 0 - depth, 1 - color, 3 - gloss, 2 - currently unused
		### Returns:
		- (bool) true if the channel is enabled
		'''

	@staticmethod
	def setSliderValue (id: str, value: float) -> bool : 
		'''
		Set the value for the the slider (if exists in UI)
		### Parameters:
		- id (str): the ID of the element
		- value (float): the value to set
		### Returns:
		- (bool) true if successful
		'''

	@staticmethod
	def getSliderValue (id: str) -> float : 
		'''
		get the value of the slider
		### Parameters:
		- id (str): the ID of the element
		### Returns:
		- (float) the value
		'''

	@staticmethod
	def setEditBoxValue (id: str, value: str) -> bool : 
		'''
		set the edit box value
		### Parameters:
		- id (str): the ID of the element
		- value (str): the value to set
		### Returns:
		- (bool) true if the element exists
		'''

	@staticmethod
	def setEditBoxValue (id: str, value: int) -> bool : 
		'''
		set the edit box value
		### Parameters:
		- id (str): the ID of the element
		- value (int): the value to set
		### Returns:
		- (bool) true if the element exists
		'''

	@staticmethod
	def setEditBoxValue (id: str, value: float) -> bool : 
		'''
		set the edit box value
		### Parameters:
		- id (str): the ID of the element
		- value (float): the value to set
		### Returns:
		- (bool) true if the element exists
		'''

	@staticmethod
	def getEditBoxValue (id: str, result: any) -> bool : 
		'''
		get the edit box value
		### Parameters:
		- id (str): the ID of the element
		- result: the string the will get the result
		### Returns:
		- (bool) true if the element exists
		'''

	@staticmethod
	def getEditBoxValue (id: str) -> str : ...
	@staticmethod
	def apply () : 
		'''
		pess ENTER, acts as Apply usually
		'''

	@staticmethod
	def setFileForFileDialog (filename: str) : 
		'''
		Set the file for the next file dialog that will be triggered by user.
		If you will use coat::ui:cmd(...) to trigger some command that shows the file dialog
		this command allows to substitute the filename for that dialog instead of showing the dialog.
		This acts only for ONE next dialog.
		### Parameters:
		- filename (str): the filename to substitute.
		'''

	@staticmethod
	def getBoolField (id: str) -> bool : 
		'''
		Get the bool field from the checkbox in UI
		### Parameters:
		- id (str): the element identifier
		### Returns:
		- (bool) the checkbox value
		'''

	@staticmethod
	def setBoolValue (id: str, value: bool) -> bool : 
		'''
		Set the value for the checkbox in UI
		### Parameters:
		- id (str): the element identifier
		- value (bool): the value to set
		### Returns:
		- (bool) true if successful and the element exists
		'''

	@staticmethod
	def currentRoom () -> str : 
		'''
		get the current room name
		### Returns:
		- (str) the name
		'''

	@staticmethod
	def isInRoom (name: str) -> bool : 
		'''
		check if we are in the specified room
		### Parameters:
		- name (str): the room name to check
		### Returns:
		- (bool) true if we are in that room
		'''

	@staticmethod
	def toRoom (name: str, Force: bool = False) : 
		'''
		switch to the room
		### Parameters:
		- name (str): the room name. Pay attention, you may pass the name or identifier, but name has bigger priory.
		- Force (bool): set true to switch even if we are in the tool that corresponds to the destination room
		'''

	@staticmethod
	def roomsCount () -> int : 
		'''
		returns the rooms count
		### Returns:
		- (int) the number
		'''

	@staticmethod
	def roomName (index: int) -> str : 
		'''
		get the room name by index
		### Parameters:
		- index (int): the room index
		### Returns:
		- (str) "" if index outside the range or the room name if the index is valid
		'''

	@staticmethod
	def roomID (index: int) -> str : 
		'''
		get the text identifier of the room
		### Parameters:
		- index (int): the room index
		### Returns:
		- (str) "" if index outside the range or the room identifier if the index is valid
		'''

	@staticmethod
	def getOption (id: str) -> str : 
		'''
		get the option from preferences
		### Parameters:
		- id (str): the identifier of english text of the option
		### Returns:
		- (str) the value as string
		'''

	@staticmethod
	def setOption (id: str, value: str) -> bool : 
		'''
		set the value to preferences
		### Parameters:
		- id (str): the value identifier or english text
		'''

	@staticmethod
	def setOption (id: str, value: bool) -> bool : ...
	@staticmethod
	def setOption (id: str, value: float) -> bool : ...
	@staticmethod
	def hideDontShowAgainMessage (id: str) : 
		'''
		Hides the "Don't show again dialog" for the current session (not forever)
		### Parameters:
		- id (str): the identifier, for example "AttachTextureHint", look the currently hidden list as files names in Docs/3DCoat/data/Temp/*.dontshow
		'''

	@staticmethod
	def showInfoMessage (infoID: str, milliseconds: int) : 
		'''
		Show the floating information message for the some time period
		### Parameters:
		- infoID (str): the message or message identifier (from language files)
		- milliseconds (int): how ling to display the message
		'''

	@staticmethod
	def insertInMenu (Menu: str, ID_in_menu: str, script_path: str) : 
		'''
		Insert the scripted command into the main menu
		### Parameters:
		- Menu (str): One of main menu items, look the list in Documents/3DCoat/UserPrefs/Scripts/ExtraMenuItems/menu_sections.txt
		- ID_in_menu (str): the ID of the command in the menu, it is the english text or the identifier of the command
		- script_path (str): the full or relative path to the script file, if relative, it is relative to the 3DCoat root folder
		If it comes without path, it is assumed to be in same folder as the script that calls this function. If this parameter is empty,
		this script will be called.
		'''

	@staticmethod
	def insertInToolset (roomID: str, section: str, toolID: str, script_path: str = "") : 
		'''
		Insert the script-based tool into the toolset
		### Parameters:
		- roomID (str): the room identifier, same as folders names in Documents/3DCoat/UserPrefs/Rooms/CustomRooms/
		- section (str): the section name. This string may be empty to add beyond sections (anyway, at the end) or in any existing section.
		To get section name, pres RMB+MMB over the section name in the toolset. You will get something like "*Adjust" in the clipboard.
		The "Adjust" in this case is the section name.
		- toolID (str): the tool identifier, how it will appear in UI. You may provide the text for the identifier using the addTranslation(...)
		Also, if there is image in the data/Textures/icons64/ named as toolID.png, it will be used as the icon for the tool.
		- script_path (str): the full or relative path to the script file, if relative, it is relative to the 3DCoat root folder
		If it comes without path, it is assumed to be in same folder as the script that calls this function. If this parameter is empty,
		this script will be called.
		'''

	@staticmethod
	def removeCommandFromMenu (ID_in_menu: str) : 
		'''
		remove the command from the menu
		### Parameters:
		- ID_in_menu (str): the ID of the command in the menu, it is the english text or the identifier of the command
		'''

	@staticmethod
	def checkIfMenuItemInserted (ID_in_menu: str) -> bool : 
		'''
		Check if the command inserted somewhere into the menu
		### Parameters:
		- ID_in_menu (str): the ID of the command in the menu, look the list in C:/Users\andre\OneDrive\Documents\3DCoat/UserPrefs\Scripts\ExtraMenuItems\menu_sections.txt it is the english text or the identifier of the command
		### Returns:
		- (bool) true if the command is inserted
		'''

	@staticmethod
	def addExtension (roomID: str, section: str, obj: any) : 
		'''
		Add the extension (new tool) into the room. Look the \ref GeneratorExample.py
		### Parameters:
		- roomID (str): roomID the room identifier, same as folders names in Documents/3DCoat/UserPrefs/Rooms/CustomRooms/
		- section (str): section the section name. This string may be empty to add beyond sections (anyway, at the end) or in any existing section.
		To get section name, pres RMB+MMB over the section name in the toolset. You will get something like "*Adjust" in the clipboard.
		The "Adjust" in this case is the section name.
		- obj: the object that contains the extension. Look the \ref GeneratorExample.py
		'''

	@staticmethod
	def checkIfExtensionPresent (extension_ID: str) -> bool : 
		'''
		Check if extension named as extension_ID is present in the 3DCoat
		### Parameters:
		- extension_ID (str): the identifier of the extension
		### Returns:
		- (bool) True if the extension installed
		'''

	@staticmethod
	def addTranslation (id: str, text: str) : 
		'''
		Add the translation for the text identifier
		### Parameters:
		- id (str): the identifier
		- text (str): the translation
		'''

	@staticmethod
	def getIdTranslation (id: str) -> str : 
		'''
		Get the translation for the text identifier
		### Parameters:
		- id (str): the text identifier
		### Returns:
		- (str) the translation or the id
		'''

	@staticmethod
	def getCurrentLanguage () -> str : 
		'''
		Get the current language file name (without the XML extension)
		### Returns:
		- (str) the language file name (without the XML extension)
		'''

	@staticmethod
	def switchToLanguage (language: str) : 
		'''
		Switch the layout to the language
		### Parameters:
		- language (str): the language identifier, actually it is the file name (withot the XML extension) in the data/Languages/ folder
		'''

	@staticmethod
	def scale () -> float : 
		'''
		returns the scale in comparison to the smallest UI theme
		### Returns:
		- (float) the scale factor > 1
		'''

	@staticmethod
	def inputString (text: str, min_length: int = 0) -> str : 
		'''
		input text under the mouse position
		### Parameters:
		- text (str): the initial text value
		- min_length (int): the minimal width of the input field, if zero passed the width taken from the parent control (if exists)
		### Returns:
		- (str) the changed text (if the user pressed OK) or the initial text other vice.
		'''

	@staticmethod
	def inputInt (initial_value: int) -> int : 
		'''
		input the integer value under the mouse position
		### Parameters:
		- initial_value (int): the initial integer value
		### Returns:
		- (int) the changed value (if the user pressed OK) or the initial value other vice.
		'''

	@staticmethod
	def inputFloat (initial_value: float) -> float : 
		'''
		inputh the float value under the mouse position
		### Parameters:
		- initial_value (float): the initial float value
		### Returns:
		- (float) the changed value (if the user pressed OK) or the initial value other vice.
		'''

class Camera:
	@staticmethod
	def rotateToGradually (destination_dir: vec3) : 
		'''
		align the camera along the view
		### Parameters:
		- destination_dir (vec3): the view direction
		'''

	@staticmethod
	def getForward () -> vec3 : 
		'''
		get the forward direction
		### Returns:
		- (vec3) the direction
		'''

	@staticmethod
	def getUp () -> vec3 : 
		'''
		get the camera up direction
		### Returns:
		- (vec3) the direction
		'''

	@staticmethod
	def getRight () -> vec3 : 
		'''
		get the camera right direction
		### Returns:
		- (vec3) the direction
		'''

	@staticmethod
	def isOrtho () -> bool : 
		'''
		return true if the camera is in the ortho mode
		### Returns:
		- (bool) the ortho mode state
		'''

	@staticmethod
	def setOrtho (ortho: bool) : 
		'''
		switch the camera to the ortho or perspective mode
		### Parameters:
		- ortho (bool): set true if need ortho mode, false if need perspective mode
		'''

	@staticmethod
	def getPivot () -> vec3 : 
		'''
		get the camera pivot position
		### Returns:
		- (vec3) the position
		'''

	@staticmethod
	def setPivot (pivot: vec3) : 
		'''
		set the camera pivot position
		### Parameters:
		- pivot (vec3): the pivot position
		'''

	@staticmethod
	def getPosition () -> vec3 : 
		'''
		get the camera position
		### Returns:
		- (vec3) the camera position
		'''

	@staticmethod
	def getWorldToScreenSpace (world_pos: vec3) -> vec3 : 
		'''
		convert the world position to the screen position
		### Parameters:
		- world_pos (vec3): the world position
		### Returns:
		- (vec3) the screen position
		'''

	@staticmethod
	def getScreenToWorldSpace (screen_pos: vec3) -> vec3 : 
		'''
		convert the screen position to the world position
		### Parameters:
		- screen_pos (vec3): the screen position (pass z that you got using getWorldToScreenSpace)
		### Returns:
		- (vec3) the world position
		'''

	@staticmethod
	def setCamera (position: vec3, lookAt: vec3, fovY: float, up: vec3 = vec3.Zero) : ...
class dialog:
	def __init__(self): ...
	def text (self, id: str) -> dialog : 
		'''
		pass the header text of the dialog
		### Parameters:
		- id (str): the text or text identifier that will be used to take the text from the language file. You may press F9 to localize it in UI.
		### Returns:
		- (dialog) the reference to pass multiple options at chain.
		'''

	def caption (self, id: str) -> dialog : 
		'''
		pass the caption of the dialog
		### Parameters:
		- id (str): id the caption or caption identifier that will be used to take the text from the language file. You may press F9 to localize it in UI.
		### Returns:
		- (dialog) the chain ref
		'''

	def width (self, w: int) -> dialog : 
		'''
		change the default width
		### Parameters:
		- w (int): the width will be scaled in correspondence with the font size, so you may pass absolute values like 500
		### Returns:
		- (dialog) itself
		'''

	def modal (self) -> dialog : 
		'''
		dialog will be modal. Generally, it is modal by default. Execution will be paused at show() till the user will press any dialog button.
		### Returns:
		- (dialog) itself
		'''

	def noModal (self) -> dialog : 
		'''
		dialog will be no modal. Execution will continue after you will call the show()
		'''

	def buttons (self, list: str) -> dialog : 
		'''
		pass the list of buttons for the dialog
		### Parameters:
		- list (str): list of buttons. |, .+; may be used as separators between identifiers
		### Returns:
		- (dialog) itself
		'''

	def topRight (self) -> dialog : 
		'''
		place the dialog at the top-right position of the viewport
		### Returns:
		- (dialog) itself
		'''

	def ok (self) -> dialog : 
		'''
		add Ok button
		### Returns:
		- (dialog) itself
		'''

	def cancel (self) -> dialog : 
		'''
		add Cancel button
		### Returns:
		- (dialog) itself
		'''

	def yes (self) -> dialog : 
		'''
		add Yes button
		### Returns:
		- (dialog) itself
		'''

	def no (self) -> dialog : 
		'''
		add No button
		### Returns:
		- (dialog) itself
		'''

	def warn (self) -> dialog : 
		'''
		add Warning icon
		### Returns:
		- (dialog) itself
		'''

	def question (self) -> dialog : 
		'''
		add Question icon
		### Returns:
		- (dialog) itself
		'''

	def undoWorks (self) -> dialog : 
		'''
		allow undo (CTR-Z) act even in modal dialog
		### Returns:
		- (dialog) itself
		'''

	def transparentBackground (self) -> dialog : 
		'''
		the background will not be faded
		### Returns:
		- (dialog) itself
		'''

	@staticmethod
	def fadeDialogsBackground () -> bool : 
		'''
		returns the reference to the global property - fade modal dialogs background (true) or not (false)
		### Returns:
		- (bool) the property reference
		'''

	def dontShowAgainCheckbox (self) -> dialog : 
		'''
		show the checkbox "Don't show again". If user checks if the dialog will net be shown next time and show() will return 0 immediately.
		### Returns:
		- (dialog) itself
		'''

	def params (self, params: any) -> dialog : 
		'''
		The important core feature. Pass the object to display object parameters in UI. Look the dialog example to understand how to use it.
		### Parameters:
		- params: the class reference
		### Returns:
		- (dialog) itself
		'''

	def process (self, callback: any) -> dialog : 
		'''
		pass the function/lambda that will be called each frame.
		### Parameters:
		- callback: the callback/lambda called each frame within the dialog
		### Returns:
		- (dialog) itself
		'''

	def onPress (self, press: any) -> dialog : 
		'''
		pass the function/lambda that will be called when the button will be pressed. The button index (starts from 1) will be passed to the function
		### Parameters:
		- press: the callback/lambda
		### Returns:
		- (dialog) itself
		'''

	def show (self) -> int : 
		'''
		Show the dialog. This is usually the last command in the chain.
		### Returns:
		- (int) the button index. First button in the list has index 1
		'''

	def widget (self, w: any) -> dialog : ...
class resource:
	def __init__(self, id: str): ...
	@staticmethod
	def listAllResourcesTypes () -> list : 
		'''
		list all available resources types
		### Returns:
		- (list) the list of resource types (any type may be passed to the resource constructor)
		'''

	def listFolders (self) -> list : 
		'''
		list folders of the resource type referred by this object
		### Returns:
		- (list) the list of folders (short names without the full path)
		'''

	def currentFolder (self) -> str : 
		'''
		get the current folder short name
		### Returns:
		- (str) the name of current folder of the resource type referred by this object
		'''

	def currentFolderFullPath (self) -> str : 
		'''
		full path (relative to the 3DCoat's documents) to the current folder files
		### Returns:
		- (str) the path
		'''

	def rootPath (self) -> str : 
		'''
		the root path (relative to the 3DCoat's documents) to the resource type referred by this object
		### Returns:
		- (str) the path
		'''

	def supportedExtensions (self) -> list : 
		'''
		get the list of supported extensions for the resource type referred by this object
		### Returns:
		- (list) the list of strings with extensions
		'''

	def setCurrentFolder (self, folder: str) : 
		'''
		set the current folder (short name without the full path)
		### Parameters:
		- folder (str): the folder name
		'''

	def createFolder (self, folderName: str) : 
		'''
		create the folder and switch there
		### Parameters:
		- folderName (str): the folder name
		'''

	def removeFolder (self, folderName: str) : 
		'''
		remove the folder and switch to the root folder if this is the current folder
		### Parameters:
		- folderName (str): the folder name
		'''

	def listCurrentFolderItems (self) -> list : 
		'''
		get the list of all items in the current folder
		### Returns:
		- (list) the list of items (usually long names with the relative path)
		'''

	def addItem (self, itemPath: str) : 
		'''
		add the item to the current folder
		### Parameters:
		- itemPath (str): the path to the item (full or relative to the 3DCoat's documents)
		'''

	def removeItem (self, itemName: str) : 
		'''
		remove the item from the current folder
		### Parameters:
		- itemName (str): the item name as it is returned by listCurrentFolderItems()
		'''

	def selectItem (self, itemName: str) : 
		'''
		select/activate the item in the current folder
		### Parameters:
		- itemName (str): the item name as it is returned by listCurrentFolderItems()
		'''

	def moveItemToFolder (self, itemName: str, destFolderName: str) : 
		'''
		move the item to another folder
		### Parameters:
		- itemName (str): the item name as it is returned by listCurrentFolderItems()
		- destFolderName (str): the short name of the destination folder
		'''

	def getCurrentItem (self) -> str : 
		'''
		returns the current item name (if possible)
		### Returns:
		- (str) the string, current item name
		'''

class io:
	@staticmethod
	def installPath () -> str : 
		'''
		the 3DCoat installation path
		### Returns:
		- (str) the path
		'''

	@staticmethod
	def dataPath () -> str : 
		'''
		the 3DCoat data path
		### Returns:
		- (str) the path
		'''

	@staticmethod
	def documents (path: str) -> str : 
		'''
		convert the relative path to the path in documents, if the path is absolute, just return the original path
		### Parameters:
		- path (str): the relative or absolute path
		### Returns:
		- (str) the absolute path in user documents
		'''

	@staticmethod
	def fileExists (path: str) -> bool : 
		'''
		check if file exists
		### Parameters:
		- path (str): the path may be full or relative. If it is relative, the documents will be
		checked first, the the install folder will be checked for file.
		### Returns:
		- (bool) true if the file exists
		'''

	@staticmethod
	def copyFile (src: str, dest: str) : 
		'''
		copy the file from src to dest. If the src or dest is relative, it is relative to the documents folder. This function works correctly with relative paths, so it is recommended over the standard copy files routine.
		### Parameters:
		- src (str): the source filename
		- dest (str): the destination filename
		'''

	@staticmethod
	def copyFolder (src: str, dest: str) : 
		'''
		copy the whole folder from src to dest. If the src or dest is relative, it is relative to the documents folder. This function works correctly with relative paths, so it is recommended over the standard copy folder routine.
		### Parameters:
		- src (str): the source folder
		- dest (str): the destination folder
		'''

	@staticmethod
	def removeFile (filename: str) : 
		'''
		remove the file. If the filename is relative, it is relative to the documents folder. If the path is in install folder, the corresponding file in documents will be removed.
		Files in the install folder can't be removed.
		### Parameters:
		- filename (str): the file path
		'''

	@staticmethod
	def removeFolder (folder: str) : 
		'''
		remove the folder. If the folder is relative, it is relative to the documents folder. If the path is in install folder, the corresponding folder in documents will be removed.
		### Parameters:
		- folder (str): the path to the folder
		'''

	@staticmethod
	def toFullPathInDataFolder (path: str) -> str : 
		'''
		convert the relative path to full path in documents folder. If the path is full and placed
		in the install folder, it will be converted to path in documents.
		### Parameters:
		- path (str): the path
		### Returns:
		- (str) the fill path in documents
		'''

	@staticmethod
	def toFullPathInDataFolder (path: any) : ...
	@staticmethod
	def toFullPathInInstallFolder (path: str) -> str : 
		'''
		convert the relative path to the full path in the install folder.
		If the path is full, it remains untouched.
		### Parameters:
		- path (str): the relative path
		### Returns:
		- (str) the full path in the install folder
		'''

	@staticmethod
	def toFullPathInInstallFolder (path: any) : ...
	@staticmethod
	def convertToWritablePath (path: str) -> str : 
		'''
		If the path is relative or points into some file in the install folder, it will be converted to the path in documents folder.
		### Parameters:
		- path (str): the path (full or relative)
		### Returns:
		- (str) the write-able path
		'''

	@staticmethod
	def convertToWritablePath (path: any) : ...
	@staticmethod
	def convertToWritablePathIfFileExists (path: str) -> str : 
		'''
		If the path is relative or points into some file in the install folder, it will be converted to the path in documents folder.
		If the does not exist in the documents folder, but exists in the install folder, the resulting path will be in the install folder.
		### Parameters:
		- path (str): the path (full or relative)
		### Returns:
		- (str) the path
		'''

	@staticmethod
	def convertToWritablePathIfFileExists (path: any) : ...
	@staticmethod
	def getExtension (filepath: str) -> str : 
		'''
		get the file extension (without .)
		### Parameters:
		- filepath (str): the file path - full or relative
		### Returns:
		- (str) the extension
		'''

	@staticmethod
	def getFileName (filepath: str) -> str : 
		'''
		get the file name from the path
		### Parameters:
		- filepath (str): the full or relative path
		### Returns:
		- (str) the filename without the path
		'''

	@staticmethod
	def getFilePath (filepath: str) -> str : 
		'''
		get the file path without the filename
		### Parameters:
		- filepath (str): the filepath
		### Returns:
		- (str) the path that always ends with '/'
		'''

	@staticmethod
	def getFileNameWithoutExtension (filepath: str) -> str : 
		'''
		remove the file extension from the filename
		### Parameters:
		- filepath (str): the file name
		### Returns:
		- (str) the filename without extension
		'''

	@staticmethod
	def strFromFile (filename: str) -> str : 
		'''
		read string from file.
		### Parameters:
		- filename (str): The path. If it is relative, it is relative to the documents folder.
		If there is no file, it will be taken from the install folder.
		### Returns:
		- (str) true if file read succesful
		'''

	@staticmethod
	def strToFile (text: str, filename: str) : 
		'''
		write the string to file
		### Parameters:
		- text (str): the text to save
		- filename (str): The path. If it is relative, it is relative to the documents folder.
		'''

	@staticmethod
	def getFileSize (filename: str) -> int : 
		'''
		get the file size
		### Parameters:
		- filename (str): the filename, relative or full
		### Returns:
		- (int) the file size
		'''

	@staticmethod
	def cursorPos () -> vec2 : 
		'''
		returns the current cursor position
		### Returns:
		- (vec2) the 2d vector
		'''

	@staticmethod
	def snappedCursorPos () -> vec2 : 
		'''
		returns the snapped cursor position
		### Returns:
		- (vec2) the 2d vector
		'''

	@staticmethod
	def wholeScreen () -> rect : 
		'''
		get the whole screen rectangle
		### Returns:
		- (rect) the rectangle, top-left is (0,0)
		'''

	@staticmethod
	def workArea () -> rect : 
		'''
		get the work area rectangle
		### Returns:
		- (rect) the rectangle, top-left is (0,0)
		'''

	@staticmethod
	def progressBar (stage: float, max_stage: float, message: str) : 
		'''
		Show the progress bar
		### Parameters:
		- stage (float): the current stage
		- max_stage (float): the maximal stage
		- message (str): the text to display
		'''

	@staticmethod
	def progressBarInWindowHeader (stage: float, max_stage: float, message: str) : 
		'''
		Show the progress bar only in the 3DCoat's window header
		### Parameters:
		- stage (float): the current stage
		- max_stage (float): the maximal stage
		- message (str): the text to display
		'''

	@staticmethod
	def setWindowTitle (text: str, seconds: float) : 
		'''
		Override the 3DCoat's window title for some amount of time
		### Parameters:
		- text (str): the text to show
		- seconds (float): the seconds to stay in title
		'''

	@staticmethod
	def step (count: int = 1) : 
		'''
		perform rendering cycles
		### Parameters:
		- count (int): amount of cycles
		'''

	@staticmethod
	def exec (command: str, arguments: str = None) : 
		'''
		execute command. It may be exe file, URL, batch command
		### Parameters:
		- command (str): the command to execute
		- arguments (str): optional command line arguments
		'''

	@staticmethod
	def execAndWait (command: str, arguments: str = None) -> str : 
		'''
		execute and wait till finished, the console output will be returned as string
		### Parameters:
		- command (str): the command to execute
		- arguments (str): optional arguments
		### Returns:
		- (str) the console output of the executed program
		'''

	@staticmethod
	def updateCoatPyi (folderOrFile: str) : 
		'''
		update the .pyi file for the given folder or py file
		### Parameters:
		- folderOrFile (str): the full or relative path to the folder or py file
		'''

	@staticmethod
	def ListFiles (folder: str, mask: str, recursive: bool = True) -> list : 
		'''
		list files in the folder
		### Parameters:
		- folder (str): the start folder. It may be absolute or relative to 3DCoat documents/install folder.
		- mask (str): the seek mask (wildcards)
		- recursive (bool): set true if recursive
		### Returns:
		- (list) result the files list
		'''

	@staticmethod
	def ListFolders (startFolder: str) -> list : 
		'''
		list folders within the folder, non-recursive, just plain list
		### Parameters:
		- startFolder (str): the start folder
		### Returns:
		- (list) the resulting list
		'''

	@staticmethod
	def supportedImagesFormats () -> str : 
		'''
		returns the currently supported mesh export formats
		### Returns:
		- (str) the list like "*.obj;*.fbx;..."
		'''

	@staticmethod
	def supportedMeshesFormats () -> str : 
		'''
		returns the list of supported images formats
		### Returns:
		- (str) the list like "*.png;*.jpg;..."
		'''

	@staticmethod
	def openFileDialog (extensions: str, fileName: any) -> bool : 
		'''
		show the file dialog
		### Parameters:
		- extensions (str): the list of supported extensions like *.txt;*.dat; etc...
		- fileName: the resulting filename
		### Returns:
		- (bool) true if user chosen the file successfully
		'''

	@staticmethod
	def openFileDialog (extensions: str) -> str : ...
	@staticmethod
	def openFilesDialog (extensions: str) -> list : 
		'''
		open multiple files dialog
		### Parameters:
		- extensions (str): the list of supported extensions like *.txt;*.dat; etc...
		### Returns:
		- (list) the resulting filenames list
		'''

	@staticmethod
	def saveFileDialog (extensions: str, fileName: any) -> bool : 
		'''
		show the save file dialog
		### Parameters:
		- extensions (str): extensions the list of supported extensions like *.txt;*.dat; etc...
		- fileName: the resulting filename
		### Returns:
		- (bool) true if user chosen the file successfully
		'''

	@staticmethod
	def saveFileDialog (extensions: str) -> str : ...
	@staticmethod
	def currentSceneFilepath () -> str : 
		'''
		returns the current scene filename, empty if the scene was not saved/opened
		'''

	@staticmethod
	def pipInstall (requirements: str) : 
		'''
		install one or multiple python packages
		### Parameters:
		- requirements (str): the list of packages to install, this is all what you write after "pip install"
		'''

	@staticmethod
	def pipUninstall (requirements: str) : ...
	@staticmethod
	def pythonPath () -> str : 
		'''
		get the python libraries folder
		### Returns:
		- (str) the path
		'''

	@staticmethod
	def showPythonConsole () : 
		'''
		Show the python console, clear it and pop up
		'''

	@staticmethod
	def executeScript (path: str) : 
		'''
		execute python (.py file) or angelscript (c++ like), or CoreAPI (native C++) script
		### Parameters:
		- path (str): the full or relative path to the script file
		'''

	@staticmethod
	def installRequirements (path_to_requirements_txt: str) : 
		'''
		Install all the requirements for the python script execution
		### Parameters:
		- path_to_requirements_txt (str): te full or relative path to the requirements.txt
		'''

	@staticmethod
	def toJson (obj: any, filename: str = "") -> str : 
		'''
		Store the object to the file or string as json
		### Parameters:
		- obj: the python object reference
		- filename (str): the filename to save, if empty, the string will be returned
		### Returns:
		- (str) the string that contains json data
		'''

	@staticmethod
	def fromJsonFile (obj: any, filename: str) : 
		'''
		Restore the object from the json file
		### Parameters:
		- obj: the object to restore
		- filename (str): the path to the json file, full or relative
		'''

	@staticmethod
	def restoreObjectFormJsonString (obj: any, data: str) : 
		'''
		Restore the object from the json string
		### Parameters:
		- obj: the object to restore
		- data (str): the json string
		'''

	@staticmethod
	def createRedistributablePackageFromFolder (folder: str, package_name: str, excluded_folders_names: str = "", excluded_extensions: str = "") : 
		'''
		Create the 3dcpack file from the folder placed in Documents
		### Parameters:
		- folder (str): the folder to pack, it should be relative to the 3DCoat's Documents folder
		- package_name (str): the package name, the extension is .3dcpack
		- excluded_folders_names (str): the folders names to be excluded from the package, separated by semicolon
		- excluded_extensions (str): the file extensions to be excluded from the package, separated by semicolon
		'''

	@staticmethod
	def getDownloadProgress () -> int : 
		'''
		returns the overall download progress
		### Returns:
		- (int) the progress in percents
		'''

	@staticmethod
	def listBlenderInstallFolders () -> list : 
		'''
		list the blender install folders
		### Returns:
		- (list) the list of the blender install folders
		'''

	@staticmethod
	def saveScreenshot (filename: str, x: int = 0, y: int = 0, width: int = 0, height: int = 0) : 
		'''
		save the screenshot to the file
		### Parameters:
		- filename (str): the filename
		- x (int): the x coordinate of the screenshot
		- y (int): the y coordinate of the screenshot
		- width (int): the width of the screenshot, if 0 all to the right will be captured
		- height (int): the height of the screenshot, if 0 all to the bottom will be captured
		'''

	@staticmethod
	def removeBackground (image1: str, image2: str, result: str) : ...
class utils:
	@staticmethod
	def dwordToVec4 (d: int) -> vec4 : 
		'''
		convert DWORD (unsigned int) to vec4
		### Parameters:
		- d (int): the DWORD (unsigned int)
		### Returns:
		- (vec4) the 4d vector
		'''

	@staticmethod
	def vec4ToDword (v: vec4) -> any : 
		'''
		convert vec4 to DWORD (unsigned int)
		### Parameters:
		- v (vec4): the 4d vector
		### Returns:
		- (any) the DWORD (unsigned int)
		'''

	@staticmethod
	def randomize (seed: int) : 
		'''
		set the random seed for all further random value generation
		### Parameters:
		- seed (int): the seed
		'''

	@staticmethod
	def random01 () -> float : 
		'''
		get the random value 0..1
		### Returns:
		- (float) the random value
		'''

	@staticmethod
	def random (min: float, max: float) -> float : 
		'''
		get the random value in range
		### Parameters:
		- min (float): low bound
		- max (float): high bound
		### Returns:
		- (float) the random value
		'''

	@staticmethod
	def randomNormal () -> vec3 : 
		'''
		get the normalized random vector
		### Returns:
		- (vec3) the 3d random vector
		'''

	@staticmethod
	def perlin3d (p: vec3, seed: float = 0) -> vec3 : 
		'''
		returns the perlin noise 3d vector
		### Parameters:
		- p (vec3): the value in 3d space
		- seed (float): the seed
		### Returns:
		- (vec3) the perlin noise value
		'''

	@staticmethod
	def perlin (p: vec3, seed: float = 0) -> float : 
		'''
		generate the perlin noise value
		### Parameters:
		- p (vec3): the value in 3d space
		- seed (float): the seed
		### Returns:
		- (float) the perlin noise value
		'''

	@staticmethod
	def getEnumValueByIndex (enumID: str, index: int) -> str : 
		'''
		get the value from the global strings list by index. That lists used in dropdown boxes in UI
		### Parameters:
		- enumID (str): the enumerator ID
		- index (int): the index of the value
		### Returns:
		- (str) the string
		'''

	@staticmethod
	def getEnumValue (enumID: str, key: str) -> int : 
		'''
		get the integer value that corresponds to the string value from the global strings list.
		### Parameters:
		- enumID (str): the enumerator ID
		- key (str): the string value fo find
		### Returns:
		- (int) the integer value that corresponds to the string
		'''

	@staticmethod
	def getEnumValueIndex (enumID: str, key: str) -> int : 
		'''
		get the index of the value in the global strings list. That lists used in dropdown boxes in UI
		### Parameters:
		- enumID (str): the enumerator ID
		- key (str): the value to find
		### Returns:
		- (int) the index of the value, -1 means that value not found
		'''

	@staticmethod
	def getEnumValuesCount (enumID: str) -> int : 
		'''
		get the count of the values in the global strings list. That lists used in dropdown boxes in UI
		### Parameters:
		- enumID (str): the enumerator ID
		### Returns:
		- (int) the count of the values
		'''

	@staticmethod
	def clearEnum (enumID: str) : 
		'''
		clear the global strings list.
		### Parameters:
		- enumID (str): the enumerator ID
		'''

	@staticmethod
	def addEnumValue (enumID: str, key: str, value: int = 1) : 
		'''
		add the value to the global strings list.
		### Parameters:
		- enumID (str): the enumerator ID
		- key (str): the string to add
		- value (int): the integer value that corresponds to the string, -1 means that the value will be the index of the string in the list, it is default value
		'''

	@staticmethod
	def quit () : 
		'''
		exit the 3DCoat
		'''

	@staticmethod
	def testSuccessful () : 
		'''
		report that the test was successful. In this case the file "InstallFolder/.installer/test_success.txt created
		'''

	@staticmethod
	def testFailed (message: str) : 
		'''
		report that the test was successful. In this case the file "InstallFolder/.installer/test_failed.txt created
		### Parameters:
		- message (str): the message to put into that file
		'''

	@staticmethod
	def signal (message: str) : 
		'''
		send some message to 3DCoat (usually used for internal purposes)
		### Parameters:
		- message (str): the message
		'''

	@staticmethod
	def last_signals () -> list : 
		'''
		get the list of last signals sent to 3DCoat
		### Returns:
		- (list) the list reference
		'''

	@staticmethod
	def getFPS () -> float : 
		'''
		get the current FPS
		### Returns:
		- (float) the fps value (averaged)
		'''

	@staticmethod
	def getFrameTimeMs () -> float : 
		'''
		get the frame time in milliseconds
		### Returns:
		- (float) the milliseconds amount
		'''

	@staticmethod
	def inRenderProcess () -> bool : 
		'''
		check if the viewport is in render process in render room
		### Returns:
		- (bool) true if in render
		'''

	@staticmethod
	def set (key: str, value: str) : 
		'''
		Globally set the value for the key, it is even stored between sessions of the 3DCoat
		### Parameters:
		- key (str): the key
		- value (str): the value to store
		'''

	@staticmethod
	def get (key: str) -> str : 
		'''
		Get previously stored value by the key
		### Parameters:
		- key (str): the key
		### Returns:
		- (str) the value as string, empty string if not found
		'''

class uv:
	@staticmethod
	def uvSetsCount () -> int : 
		'''
		get the UV-sets count.
		### Returns:
		- (int) the amount
		'''

	@staticmethod
	def setUnwrapIslandsDistance (distance: float) : 
		'''
		set the border around the islands when we pack it
		### Parameters:
		- distance (float): the border size in percents
		'''

	@staticmethod
	def getUnwrapIslandsDistance () -> float : 
		'''
		get the border around the islands when we pack it
		### Returns:
		- (float) the border size in percents
		'''

	@staticmethod
	def currentUvSet () -> int : 
		'''
		get the current uv-set index
		### Returns:
		- (int) the index
		'''

	@staticmethod
	def islandsCount (uv_set: int) -> int : 
		'''
		get the islands count over the current uv-set
		### Parameters:
		- uv_set (int): the uv-set index
		### Returns:
		- (int) teh islands count
		'''

	@staticmethod
	def islandToMesh (uv_set: int, island_index: int) -> Mesh : 
		'''
		get the mesh that contains the island, xy of each point is the UV coordinate. The mesh contains only one island
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (Mesh) the flat mesh
		'''

	@staticmethod
	def islandToMeshInSpace (uv_set: int, island_index: int) -> Mesh : 
		'''
		get the mesh that contains the island, each point is the coordinate in space (not the uv coordinate!). The mesh contains only one island. The faces correspond to the faces of the mesh that was got by islandToMesh
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (Mesh) s mesh the 3D mesh
		'''

	@staticmethod
	def getIslandVertexMapping (uv_set: int, island_index: int) -> list : 
		'''
		get the mapping from the vertex index in the mesh that was got by islandToMesh to the vertex index in the original mesh
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (list) the list of the positional vertex indices of the original mesh in same order as the vertices in the mesh that was got by islandToMesh
		'''

	@staticmethod
	def getIslandBorder (uv_set: int, island_index: int) -> list : 
		'''
		get unsorted list of edges on the border of the island
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (list) the list of edges, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		'''

	@staticmethod
	def getBorderBetweenIslands (uv_set1: int, island_index1: int, uv_set2: int, island_index2: int) -> list : 
		'''
		get the border between two islands
		### Parameters:
		- uv_set1 (int): the uv set index of the first island
		- island_index1 (int): the island index within the uv set of the first island
		- uv_set2 (int): the uv set index of the second island
		- island_index2 (int): the island index within the uv set of the second island
		### Returns:
		- (list) the list of edges that are common for both islands, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		'''

	@staticmethod
	def getIslandVertexUv (uv_set: int, island_index: int, vertex_index: int) -> vec2 : 
		'''
		get the uv coordinate of the positional vertex in the island
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		- vertex_index (int): the positional vertex index
		### Returns:
		- (vec2) the uv coordinate of the vertex, vec2(0,0) if the vertex is not in the island
		'''

	@staticmethod
	def flattenSingleIsland (mesh: Mesh, method: int, optimize_rotation: bool = True, scale_to_geometry: bool = True) -> Mesh : 
		'''
		Flatten the mesh that consists of the single island
		### Parameters:
		- mesh (Mesh): the mesh that consists of the single island
		- method (int): the flattening method. 0 - flatten to the plane, 1 - LSCM, 2 - ABF, 3 - GU, 4 - Stripe (if possible)
		- optimize_rotation (bool): optimize the rotation of the island, place it approximately horizontally or vertically
		- scale_to_geometry (bool): scale the island to keep average edge length equal to the average edge length of the original mesh
		### Returns:
		- (Mesh) the flat mesh
		'''

	@staticmethod
	def meshToIsland (mesh: Mesh, uv_set: int, island_index: int) : 
		'''
		use the mesh (that was previously got by islandToMesh) to replace the island in the current uv-set
		### Parameters:
		- mesh (Mesh): the mesh that was previously got by islandToMesh
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	@staticmethod
	def pack (uv_set: int, rotate: bool, shuffle: bool) : 
		'''
		pack the islands in the current uv-set
		### Parameters:
		- uv_set (int): the uv set index
		- rotate (bool): allow rotation while packing
		- shuffle (bool): shuffle the identical islands to avoid the exact overlapping
		'''

	@staticmethod
	def unwrap (uv_set: int) : 
		'''
		unwrap the current uv-set
		### Parameters:
		- uv_set (int): the uv set index
		'''

	@staticmethod
	def toAbf (uv_set: int, island_index: int) : 
		'''
		unwrap the island using the ABF approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	@staticmethod
	def toLscm (uv_set: int, island_index: int) : 
		'''
		unwrap the island using the LSCM approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	@staticmethod
	def toGu (uv_set: int, island_index: int) : 
		'''
		unwrap the island using the GU (Globally Uniform) approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	@staticmethod
	def toPlanar (uv_set: int, island_index: int) : 
		'''
		unwrap the island using the Planar approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	@staticmethod
	def toStripe (uv_set: int, island_index: int) : 
		'''
		try to uwrap the island as the regular stripe
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	@staticmethod
	def toUvSet (uv_set: int, island_index: int, destination_uv_set: int) : 
		'''
		move the island from one uv-set to another one
		### Parameters:
		- uv_set (int): the source uv set index
		- island_index (int): the island index within the source uv set
		- destination_uv_set (int): the destination uv set index
		'''

	@staticmethod
	def getWholeMesh () -> Mesh : 
		'''
		get the whole mesh from the paint/UV/Retopo room - in dependence on current room
		### Returns:
		- (Mesh) the whole paint or retopo mesh (in dependence on current room)
		'''

	@staticmethod
	def selectedToMesh () -> Mesh : 
		'''
		get the selected faces as the Mesh object
		### Returns:
		- (Mesh) the Mesh
		'''

	@staticmethod
	def getSeams () -> list : 
		'''
		get all seams across the mesh
		### Returns:
		- (list) the list of integer values, each value is the index of the vertex in the mesh, the even index is start of the seam, the odd index is the end of the seam
		'''

	@staticmethod
	def addSeam (start_vertex_index: any, end_vertex_index: int) : 
		'''
		add the seam to the mesh
		### Parameters:
		- start_vertex_index: the start positional vertex index
		- end_vertex_index (int): the end positional vertex index
		'''

	@staticmethod
	def removeSeam (start_vertex_index: int, end_vertex_index: int) : 
		'''
		remove the seam from the mesh
		### Parameters:
		- start_vertex_index (int): the start positional vertex index
		- end_vertex_index (int): the end positional vertex index
		'''

	@staticmethod
	def getSharpEdges () -> list : 
		'''
		get the sharp edges across the mesh
		### Returns:
		- (list) the list of integer values, each value is the index of the vertex in the mesh, the even index is start of the edge, the odd index is the end of the edge
		'''

	@staticmethod
	def addSharpEdge (start_vertex_index: int, end_vertex_index: int) : 
		'''
		add the sharp edge to the mesh
		### Parameters:
		- start_vertex_index (int): the start positional vertex index
		- end_vertex_index (int): the end positional vertex index
		'''

	@staticmethod
	def removeSharpEdge (start_vertex_index: int, end_vertex_index: int) : 
		'''
		remove the sharp edge from the mesh
		### Parameters:
		- start_vertex_index (int): the start positional vertex index
		- end_vertex_index (int): the end positional vertex index
		'''

	@staticmethod
	def unwrapUnassigned () : 
		'''
		re-wrap/extend  islands in correspondence to the changed seams and inserted faces. Pay attention, that it may lead to islands intersection.
		'''

	@staticmethod
	def applyUVSet () : 
		'''
		apply uv changes to the paint room mesh (if we use uv/paint context)
		'''

class Model:
	def __init__(self): ...
	def __init__(self, source: Model): ...
	def __init__(self, source: Mesh): ...
	def __assign__ (self, source: Model) -> Model : ...
	def __assign__ (self, source: Mesh) -> Model : ...
	def __iadd__ (self, source: Model) -> Model : ...
	def __iadd__ (self, source: Mesh) -> Model : ...
	def transform (self, m: mat4) -> Model : 
		'''
		transform the whole Model with the matrix
		### Parameters:
		- m (mat4): the transformation matrix
		### Returns:
		- (Model) the reference to the Model
		'''

	def MakeCopy (self) -> Model : 
		'''
		make a copy of the source mesh. Pay attention, if you taken it from the retopo/uv context, it will no longer refer to the retopo/uv mesh, it will be independent copy
		'''

	def __init__(self): ...
	@staticmethod
	def fromRetopo () -> Model : 
		'''
		get the reference to the mesh in the retopo room
		### Returns:
		- (Model) the reference to the mesh
		'''

	@staticmethod
	def fromModeling () -> Model : 
		'''
		get the reference to the mesh in the modeling room, currently it is the same mesh as in the retopo room
		### Returns:
		- (Model) the reference to the mesh
		'''

	@staticmethod
	def fromUv () -> Model : 
		'''
		get the reference to the mesh in the uv room, pay attention that topology changes to that mesh may lead to instability!
		### Returns:
		- (Model) the reference to the mesh
		'''

	def displayOptions (self, showWireframe: bool = True, showColored: bool = True, showSeams: bool = True, showSharpEdges: bool = True, smoothView: bool = False) : 
		'''
		Set the display options for the retopo/modeling/uv meshes
		### Parameters:
		- showWireframe (bool): show the wireframe
		- showColored (bool): show colored clusters
		- showSeams (bool): show seams
		- showSharpEdges (bool): show sharp edges
		- smoothView (bool): smooth view
		'''

	def getObjectsCount (self) -> int : 
		'''
		get the retopo groups count
		### Returns:
		- (int) the amount
		'''

	def getCurrentObject (self) -> int : 
		'''
		get the index of the current group
		### Returns:
		- (int) the index
		'''

	def setCurrentObject (self, index: int) : 
		'''
		set the current group index
		### Parameters:
		- index (int): the index
		'''

	def getObjectName (self, group_index: int) -> str : 
		'''
		get the retopo group name
		### Parameters:
		- group_index (int): the group index
		### Returns:
		- (str) the name
		'''

	def removeObject (self, group_index: int) : 
		'''
		remove the group by index
		'''

	def setObjectName (self, index: int, name: str) : 
		'''
		rename the group by index
		### Parameters:
		- index (int): the group index to rename
		- name (str): the new name
		'''

	def setObjectVisibility (self, index: int, visible: bool) : 
		'''
		set the group visibility
		### Parameters:
		- index (int): the group index
		- visible (bool): the visibility state
		'''

	def getObjectVisibility (self, index: int) -> bool : 
		'''
		get the group visibility
		### Parameters:
		- index (int): the group index
		### Returns:
		- (bool) the visibility state
		'''

	def addObject (self, name: str) -> int : 
		'''
		add new retopo group
		### Parameters:
		- name (str): the group name
		### Returns:
		- (int) the index of new group
		'''

	def addMaterial (self, name: str) -> int : 
		'''
		add the new UV set/Material
		### Parameters:
		- name (str): the name
		### Returns:
		- (int) the new UV set/Material index
		'''

	def removeUnusedMaterials (self) : 
		'''
		remove all unused UV sets (not referred within the mesh)
		'''

	def getObjectReferenceColor (self, group_index: int) -> vec4 : 
		'''
		get the group reference color
		### Parameters:
		- group_index (int): the group index
		### Returns:
		- (vec4) the (r,g,b,a) vector, 0..255
		'''

	def setObjectReferenceColor (self, group_index: int, color: vec4) : 
		'''
		set the group reference color
		### Parameters:
		- group_index (int): the group index
		- color (vec4): the (r,g,b,a) vector, 0..255
		'''

	def selectedToObject (self, group_index: int) : 
		'''
		move the selected faces to the group
		### Parameters:
		- group_index (int): the group index
		'''

	def getWholeMesh (self) -> Mesh : 
		'''
		get the whole mesh from the retopo room
		### Returns:
		- (Mesh) the Mesh object
		'''

	def selectedToMesh (self) -> Mesh : 
		'''
		get the selected faces as the Mesh object
		### Returns:
		- (Mesh) the Mesh
		'''

	def visibleToMesh (self) -> Mesh : 
		'''
		get the visible faces as the Mesh object
		### Returns:
		- (Mesh) teh Mesh
		'''

	def addTransformed (self, mesh: Mesh, Transform: mat4 = mat4.Identity, b: BoolOpType = BoolOpType.BOOL_MERGE, select: bool = False, snap_to_existing: bool = False) : 
		'''
		insert the mesh to the retopo/modeling room, each object of the mesh treated as the new retopo layer
		### Parameters:
		- mesh (Mesh): the Mesh object
		- Transform (mat4): the transformation matrix
		- b (BoolOpType): the boolean operation type
		- select (bool): the flag that indicates if we need to select faces of the the inserted mesh, used only if b is BOOL_MERGE
		- snap_to_existing (bool): the flag that indicates if we need to snap the mesh to the existing sculpt/paint objects
		'''

	def getObjectMesh (self, group_index: int) -> Mesh : 
		'''
		get the mesh from some retopo group
		### Parameters:
		- group_index (int): the group index
		### Returns:
		- (Mesh) the Mesh object
		'''

	def setObjectMesh (self, group_index: int, mesh: Mesh, transform: mat4 = mat4.Identity) : 
		'''
		replace the retopo layer with mesh
		### Parameters:
		- group_index (int): the group index
		- mesh (Mesh): the Mesh object to insert
		- transform (mat4): the transformation matrix
		'''

	def duplicateObject (self, group_index: int, name: str = None, transform: mat4 = mat4.Identity, select: bool = False) -> int : 
		'''
		duplicate the object (retopo group)
		### Parameters:
		- group_index (int): the object/group index
		- name (str): the new name, if not passed the name will be generated automatically
		- transform (mat4): the additional transformation matrix
		- select (bool): the flag that indicates if we need to select the new object's faces (in addition to existing selection)
		### Returns:
		- (int) the new object index
		'''

	def generateName (self, base: str) -> str : 
		'''
		generate unique name for the object, it will start as the string in base base
		### Parameters:
		- base (str): the base name
		### Returns:
		- (str) the unique name
		'''

	def clearObjectMesh (self, group_index: int) : 
		'''
		remove all faces from the group
		### Parameters:
		- group_index (int): the group index
		'''

	def clear (self) : 
		'''
		clear the whole mesh
		'''

	def dropUndo (self) : 
		'''
		Drop the whole mesh to the undo queue, it is important if you want allow the user to undo your mesh changes, call it before your changes. It works for UV room too.
		'''

	def getSelectedFaces (self) -> list : 
		'''
		get the list of selected faces
		### Returns:
		- (list) the list of selected faces
		'''

	def setSelectedFaces (self, faces: list) : 
		'''
		set the selected faces list
		### Parameters:
		- faces (list): the faces indices list
		'''

	def selectFace (self, face: int) : 
		'''
		select the face by index
		### Parameters:
		- face (int): the face index
		'''

	def selectObject (self, group_index: int, add_to_selected: bool = True) : 
		'''
		select all feces in the group
		### Parameters:
		- group_index (int): the group index
		'''

	def getObjectFaces (self, group_index: int) -> list : 
		'''
		get the list of faces in the group
		### Parameters:
		- group_index (int): the group index
		### Returns:
		- (list) the list of faces
		'''

	def isFaceSelected (self, face: int) -> bool : 
		'''
		check if the face selected
		### Parameters:
		- face (int): the face index
		### Returns:
		- (bool) the selection state
		'''

	def unselectAllFaces (self) : 
		'''
		unselect all faces
		'''

	def expandSelection (self) : 
		'''
		expand the faces/vertices/edges selection to the connected geometry
		'''

	def contractSelection (self) : 
		'''
		contract the faces/vertices/edges selection to the connected geometry
		'''

	def selectedToEdges (self) : 
		'''
		convert faces/vertices selection to edges selection
		'''

	def selectedToFaces (self) : 
		'''
		convert edges/vertices selection to faces selection
		'''

	def selectedToVertices (self) : 
		'''
		convert faces/edges selection to vertices selection
		'''

	def getSelectedEdges (self) -> list : 
		'''
		returns even amount of vertex indices, pairs os start and end vertices of the selected edges
		### Returns:
		- (list) the list of vertex indices (pairs)
		'''

	def setSelectedEdges (self, edges: list) : 
		'''
		set the selected edges list
		### Parameters:
		- edges (list): the edges indices list (should be even amount of indices)
		'''

	def selectEdge (self, vertex1: int, vertex2: int) : 
		'''
		select the edge by vertex indices (add to selection)
		### Parameters:
		- vertex1 (int): the first vertex index
		- vertex2 (int): the second vertex index
		'''

	def isEdgeSelected (self, vertex1: int, vertex2: int) -> bool : 
		'''
		check if the edge is selected, order of vertices has no matter
		### Parameters:
		- vertex1 (int): the first vertex index
		- vertex2 (int): the second vertex index
		### Returns:
		- (bool) true if the edge is selected
		'''

	def unselectAllEdges (self) : 
		'''
		unselect all edges
		'''

	def getSelectedVertices (self) -> list : 
		'''
		get the list of selected vertices
		### Returns:
		- (list) the list of selected vertices
		'''

	def getSelectedVerticesWeights (self) -> list : 
		'''
		get the soft selection weights of the selected vertices, 1 is maximum value
		### Returns:
		- (list) the list of weights, the size of the list is equal to the size of the selected vertices list
		'''

	def setSelectedVertices (self, vertices: list, weights: list) : 
		'''
		set the selected vertices list
		### Parameters:
		- vertices (list): the list of vertices indices
		- weights (list): the list of soft selection weights, the size of the list should be zero or equal to the size of the vertices list. If it is empty, the vertices will be selected with the maximal weight
		'''

	def selectVertex (self, vertex: int, weight: float = 1.0) : 
		'''
		add the vertex to the selection
		### Parameters:
		- vertex (int): the vertex index
		- weight (float): the soft selection weight, 1 is maximum value
		'''

	def isVertexSelected (self, vertex: int) -> bool : 
		'''
		check if the vertex is selected
		### Parameters:
		- vertex (int): the vertex index
		### Returns:
		- (bool) true if the vertex is selected
		'''

	def unselectAllVertices (self) : 
		'''
		unselect all vertices
		'''

	def facesCount (self) -> int : 
		'''
		get the faces count
		### Returns:
		- (int) the faces count
		'''

	def vertsCount (self) -> int : 
		'''
		get the positional vertices count
		### Returns:
		- (int) the vertices count
		'''

	def vertsUvCount (self) -> int : 
		'''
		get the uv vertices count
		### Returns:
		- (int) the uv vertices count
		'''

	def removeFace (self, face: int) : 
		'''
		remove the face by index
		### Parameters:
		- face (int): the face index
		'''

	def createNewFace (self, Group: int, UVSet: int) -> int : 
		'''
		create empty face, you need to call setFaceVertices to set the vertices, setFaceUVVerts to set the UV vertices
		### Parameters:
		- Group (int): the face group index
		- UVSet (int): the UV set index
		### Returns:
		- (int) the new face index
		'''

	def getFaceVertsCount (self, face: int) -> int : 
		'''
		get the vertices count over the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (int) the vertices count
		'''

	def getFaceVertex (self, face: int, vertex_index: int) -> int : 
		'''
		get the vertex index over the face
		### Parameters:
		- face (int): the face index
		- vertex_index (int): the vertex index over the face
		### Returns:
		- (int) the vertex index, -1 if the vertex/face index is out of range
		'''

	def getFaceVerts (self, face: int) -> list : 
		'''
		get the list of UV vertex indices over the face, pay attention UV vertices are not same as position vertices
		### Parameters:
		- face (int): the face index
		### Returns:
		- (list) the list of vertex indices
		'''

	def setFaceVerts (self, face: int, vertices: list) : 
		'''
		set the list of positional vertex indices over the face
		### Parameters:
		- face (int): the face index
		- vertices (list): the list of vertex indices
		'''

	def getFaceVisibility (self, face: int) -> bool : 
		'''
		get the face visibility
		### Parameters:
		- face (int): the face index
		### Returns:
		- (bool) the visibility state
		'''

	def setFaceVisibility (self, face: int, visibility: bool) : 
		'''
		set the face visibility
		### Parameters:
		- face (int): the face index
		- visibility (bool): the visibility state
		'''

	def getFaceSquare (self, face: int) -> float : 
		'''
		get the face square
		### Parameters:
		- face (int): the face index
		### Returns:
		- (float) the square
		'''

	def getFaceUVSquare (self, face: int) -> float : 
		'''
		get the face square in UV space
		### Parameters:
		- face (int): the face index
		### Returns:
		- (float) the square
		'''

	def getFaceNormal (self, face: int) -> vec3 : 
		'''
		get the face normal
		### Parameters:
		- face (int): the face index
		### Returns:
		- (vec3) the face normal
		'''

	def getFaceObject (self, face: int) -> int : 
		'''
		get the group index of the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (int) the group index
		'''

	def setFaceObject (self, face: int, group: int) : 
		'''
		set the group index of the face
		### Parameters:
		- face (int): the face index
		- group (int): the group index
		'''

	def getFaceMaterial (self, face: int) -> int : 
		'''
		get the UV set index for the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (int) the UV set index, -1 if out of range
		'''

	def setFaceMaterial (self, face: int, uv_set: int) : 
		'''
		set the UV set for the face
		### Parameters:
		- face (int): the face index
		- uv_set (int): the UV set index
		'''

	def getFaceUvVertsCount (self, face: int) -> int : 
		'''
		get the amount of UV vertices over the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (int) amount of vertices over the face, 0 if UV-s not assigned
		'''

	def getFaceUvVertex (self, face: int, vertex_index: int) -> int : 
		'''
		get the UV vertex index over the face
		### Parameters:
		- face (int): the face index
		- vertex_index (int): the vertex index over the face
		### Returns:
		- (int) the UV vertex index, -1 if the vertex/face index is out of range
		'''

	def getFaceUvVerts (self, face: int) -> list : 
		'''
		get the list of UV vertices indices over the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (list) the list of UV vertices indices
		'''

	def setFaceUvVerts (self, face: int, vertices: list) : 
		'''
		set the UV vertices for the face
		### Parameters:
		- face (int): the face index
		- vertices (list): the UV vertices list
		'''

	def getVertex (self, vertex: int) -> vec3 : 
		'''
		get the vertex position in space
		### Parameters:
		- vertex (int): the vertex index
		### Returns:
		- (vec3) the position
		'''

	def setVertex (self, vertex: int, position: vec3) : 
		'''
		set the vertex position in space
		### Parameters:
		- vertex (int): the vertex index
		- position (vec3): the position
		'''

	def createNewVertex (self, position: vec3) -> int : 
		'''
		create the positional vertex
		### Parameters:
		- position (vec3): the position
		### Returns:
		- (int) the positional vertex index
		'''

	def getVertexUV (self, uv_vertex: int) -> vec2 : 
		'''
		get the UV coordinates of the UV vertex
		### Parameters:
		- uv_vertex (int): the uv vertex index
		### Returns:
		- (vec2) teh UV coordinates
		'''

	def setVertexUV (self, uv_vertex: int, uv: vec2) : 
		'''
		set the UV for the UV vertex
		### Parameters:
		- uv_vertex (int): the uv vertex index
		- uv (vec2): the UV coordinates
		'''

	def createNewUvVertex (self, uv: vec2) -> int : 
		'''
		create new UV vertex to be used for faces
		### Parameters:
		- uv (vec2): the texture coordinates
		### Returns:
		- (int) the index
		'''

	def getVertexNormal (self, vertex: int) -> vec3 : 
		'''
		get vertex normal, calculated as average of adjacent faces normals
		### Parameters:
		- vertex (int): the vertex index
		### Returns:
		- (vec3) the normal
		'''

	def updateNormals (self, for_snapping: bool = True) : 
		'''
		update the vertex normals
		### Parameters:
		- for_snapping (bool): if true, the normals will lay in the middle of faces, ne respecting the faces square.
		'''

	def updateTopology (self) : 
		'''
		update the connectivity information, it should be called sometimes if you feel that the connectivity information lost due to some heavy operations
		'''

	def cleanup (self) : 
		'''
		complete cleanul from non-manifolds or other problems, some faces may be removed
		'''

	def getVertsNearVertex (self, vertex: int) -> list : 
		'''
		get the list of vertices that are adjacent to the vertex
		### Parameters:
		- vertex (int): the vertex index
		### Returns:
		- (list) the list of adjacent vertices
		'''

	def getFacesNearVertex (self, vertex: int) -> list : 
		'''
		get the list of faces that are adjacent to the vertex
		### Parameters:
		- vertex (int): the vertex index
		### Returns:
		- (list) the list of adjacent faces
		'''

	def getFaceNeighbors (self, face: int) -> list : 
		'''
		get the list of faces that are adjacent to the face
		### Parameters:
		- face (int): the face index
		### Returns:
		- (list) the list of adjacent faces
		'''

	def getFacesNearEdge (self, vertex1: int, vertex2: int) -> list : 
		'''
		get the list of faces that are adjacent to the edge
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		### Returns:
		- (list) the list of adjacent faces
		'''

	def isOpenEdge (self, vertex1: int, vertex2: int) -> bool : 
		'''
		check if the edge is open
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		### Returns:
		- (bool) true if open
		'''

	def isSharpEdge (self, vertex1: int, vertex2: int) -> bool : 
		'''
		check if the edge is sharp
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		### Returns:
		- (bool) true if sharp
		'''

	def setEdgeSharpness (self, vertex1: int, vertex2: int, sharp: bool) : 
		'''
		set the sharpness state for the edge
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		- sharp (bool): the sharpness state
		'''

	def isSeam (self, vertex1: int, vertex2: int) -> bool : 
		'''
		check if edge is seam
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		### Returns:
		- (bool) true if seam
		'''

	def setEdgeSeam (self, vertex1: int, vertex2: int, seam: bool) : 
		'''
		set or clear the seam state for the edge
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		- seam (bool): the seam state
		'''

	def collapseEdge (self, vertex1: int, vertex2: int) : 
		'''
		collapse the edge to the middle of the edge
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		'''

	def islandsCount (self, uv_set: int) -> int : 
		'''
		get the islands count over the current uv-set
		### Parameters:
		- uv_set (int): the uv-set index
		### Returns:
		- (int) teh islands count
		'''

	def islandToMesh (self, uv_set: int, island_index: int) -> Mesh : 
		'''
		get the mesh that contains the island, xy of each point is the UV coordinate. The mesh contains only one island
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (Mesh) the flat mesh
		'''

	def islandToMeshInSpace (self, uv_set: int, island_index: int) -> Mesh : 
		'''
		get the mesh that contains the island, each point is the coordinate in space (not the uv coordinate!). The mesh contains only one island. The faces correspond to the faces of the mesh that was got by islandToMesh
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (Mesh) s mesh the 3D mesh
		'''

	def getIslandVertexMapping (self, uv_set: int, island_index: int) -> list : 
		'''
		get the mapping from the vertex index in the mesh that was got by islandToMesh to the vertex index in the original mesh
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (list) the list of the positional vertex indices of the original mesh in same order as the vertices in the mesh that was got by islandToMesh
		'''

	def getIslandBorder (self, uv_set: int, island_index: int) -> list : 
		'''
		get unsorted list of edges on the border of the island
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		### Returns:
		- (list) the list of edges, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		'''

	def getBorderBetweenIslands (self, uv_set1: int, island_index1: int, uv_set2: int, island_index2: int) -> list : 
		'''
		get the border between two islands
		### Parameters:
		- uv_set1 (int): the uv set index of the first island
		- island_index1 (int): the island index within the uv set of the first island
		- uv_set2 (int): the uv set index of the second island
		- island_index2 (int): the island index within the uv set of the second island
		### Returns:
		- (list) the list of edges that are common for both islands, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		'''

	def getIslandVertexUv (self, uv_set: int, island_index: int, vertex_index: int) -> vec2 : 
		'''
		get the uv coordinate of the positional vertex in the island
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		- vertex_index (int): the positional vertex index
		### Returns:
		- (vec2) the uv coordinate of the vertex, vec2(0,0) if the vertex is not in the island
		'''

	@staticmethod
	def flattenSingleIsland (mesh: Mesh, method: int, optimize_rotation: bool = True, scale_to_geometry: bool = True) -> Mesh : 
		'''
		Flatten the mesh that consists of the single island
		### Parameters:
		- mesh (Mesh): the mesh that consists of the single island
		- method (int): the flattening method. 0 - flatten to the plane, 1 - LSCM, 2 - ABF, 3 - GU, 4 - Stripe (if possible)
		- optimize_rotation (bool): optimize the rotation of the island, place it approximately horizontally or vertically
		- scale_to_geometry (bool): scale the island to keep average edge length equal to the average edge length of the original mesh
		### Returns:
		- (Mesh) the flat mesh
		'''

	def meshToIsland (self, mesh: Mesh, uv_set: int, island_index: int) : 
		'''
		use the mesh (that was previously got by islandToMesh) to replace the island in the current uv-set
		### Parameters:
		- mesh (Mesh): the mesh that was previously got by islandToMesh
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	def pack (self, uv_set: int, rotate: bool, shuffle: bool) : 
		'''
		pack the islands in the current uv-set
		### Parameters:
		- uv_set (int): the uv set index
		- rotate (bool): allow rotation while packing
		- shuffle (bool): shuffle the identical islands to avoid the exact overlapping
		'''

	def unwrap (self, uv_set: int) : 
		'''
		unwrap the current uv-set
		### Parameters:
		- uv_set (int): the uv set index
		'''

	def toAbf (self, uv_set: int, island_index: int) : 
		'''
		unwrap the island using the ABF approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	def toLscm (self, uv_set: int, island_index: int) : 
		'''
		unwrap the island using the LSCM approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	def toGu (self, uv_set: int, island_index: int) : 
		'''
		unwrap the island using the GU (Globally Uniform) approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	def toPlanar (self, uv_set: int, island_index: int) : 
		'''
		unwrap the island using the Planar approach
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	def toStripe (self, uv_set: int, island_index: int) : 
		'''
		try to uwrap the island as the regular stripe
		### Parameters:
		- uv_set (int): the uv set index
		- island_index (int): the island index within the uv set
		'''

	def extrudeSelected (self) : 
		'''
		Extrude the selected edges or selected faces without the actual moving of the extruded elements. They stay selected, so you amy apply some transform to the selected elements
		'''

	def moveSelectedFacesAlongFacesNormals (self, displacement: float) : 
		'''
		move selected faces along the faces normals, trying to keep faces parallel to the original direction
		### Parameters:
		- displacement (float): the displacement value
		'''

	def moveSelectedFacesAlongVertexNormals (self, displacement: float) : 
		'''
		move selected faces along the vertex normals, each vertex displace on the same distance
		### Parameters:
		- displacement (float): the displacement value
		'''

	def subdivideSelectedFaces (self, apply_catmull_clark: bool = False) : 
		'''
		subdivide the selected faces
		### Parameters:
		- apply_catmull_clark (bool): apply the catmull-clark subdivision
		'''

	def subdivide (self, apply_catmull_clark: bool = True) : 
		'''
		subdivide the whole mesh
		### Parameters:
		- apply_catmull_clark (bool): apply the catmull-clark subdivision
		'''

	def transformSelected (self, transform: mat4, apply_symmetry: bool) : 
		'''
		apply the transformation to the selected elements
		### Parameters:
		- transform (mat4): the transformation matrix
		- apply_symmetry (bool): apply the global symmetry
		'''

	def scaleSelectedFacesClusters (self, scale: float, method: ClusterScale = ClusterScale.Uniform_Scaling) : 
		'''
		scale each selection cluster separately, to own center mass
		### Parameters:
		- scale (float): the scale coefficient
		'''

	def bevelOverSelectedVertices (self, size: float) : 
		'''
		perform the bevel over the selected vertices. As result, new faces will be selected
		### Parameters:
		- size (float): the bevel size
		'''

	def bevelOverSelectedEdges (self, size: float, segments: int = 1, OldVariant: bool = False) : 
		'''
		perform the bevel over the selected edges.
		### Parameters:
		- size (float): the bevel width
		- OldVariant (bool): if true the older variant of the bevel (splits edges in strightforward way), in some cases it works more stable.
		'''

	def splitEdge (self, vertex1: int, vertex2: int, position: float) -> int : 
		'''
		split existing edge somewhere between vertices.
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		- position (float): the position to split the edge, [0..1], 0 - near the vertex1, 1 - near the vertex2
		### Returns:
		- (int) the new vertex index
		'''

	def connect (self, vertex1: int, vertex2: int) -> bool : 
		'''
		split existing edge somewhere between vertices.
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		### Returns:
		- (bool) true if succeeed to connect
		'''

	def checkConnectivity (self, vertex1: int, vertex2: int) -> bool : 
		'''
		check if connecting the two vertices is possible
		### Parameters:
		- vertex1 (int): the positional vertex index (1)
		- vertex2 (int): the positional vertex index (2)
		### Returns:
		- (bool) true if connection is possible
		'''

	def connectSelectedVerts (self) : 
		'''
		connect selected vertices in smart way
		'''

	def invertSelectedFacesTopoplogically (self) : 
		'''
		invert selected faces only within the connective area, if some objects has no selected faces, the selection there will not change
		'''

	def inset (self, distance: float) : 
		'''
		perform the inset over the selected faces
		'''

	def shell (self) : 
		'''
		perform the shell operation over the selected faces. After calling the shell() you should call the moveSelectedFacesAlongFacesNormals or moveSelectedFacesAlongVertexNormals
		to give some thickness to the resulting figure
		'''

	def intrude (self) : 
		'''
		perform the intrude operation over the selected faces. After calling the intrude() you should call the moveSelectedFacesAlongFacesNormals or moveSelectedFacesAlongVertexNormals
		to give some thickness to the resulting figure
		'''

	def relaxSelected (self) : 
		'''
		relax selected vergtices
		'''

	def selectPath (self, vertex1: int, vertex2: int) : 
		'''
		select all edges on the path from vertex1 to vertex2 (add to existing edges selection)
		### Parameters:
		- vertex1 (int): the first vertex
		- vertex2 (int): the second vertex
		'''

	def getPath (self, vertex1: int, vertex2: int) -> list : 
		'''
		get all vertices on the path from vertex1 to vertex2
		### Parameters:
		- vertex1 (int): the first vertex
		- vertex2 (int): the second vertex
		'''

class logger:
	def __init__(self): ...
	def __init__(self, filename: str): ...
	def __init__(self): ...
	def open (self) : 
		'''
		open the accumulated log in the default text editor
		'''

	def showMessage (self) : 
		'''
		show the accumulated log in the message box
		'''

	def directTo (self, filename: str) -> logger : 
		'''
		Direct the log output to the file
		### Parameters:
		- filename (str): the filename to log there. The filename may be relative path.
		### Returns:
		- (logger) the logger reference
		'''

	def getFullPath (self) -> any : 
		'''
		Returns the absolute path to the log file.
		### Returns:
		- (any) the absolute path even if you passed the relative path.
		'''

	def flush (self) -> logger : 
		'''
		save all acumulated text to the file
		### Returns:
		- (logger) the chain reference
		'''

	def newline (self) -> logger : 
		'''
		start newline in the text file
		### Returns:
		- (logger) the chain reference
		'''

	def timestamp (self) -> logger : 
		'''
		add the timestamp to the log as the
		### Returns:
		- (logger) the reference
		'''

	def startTimer (self) -> logger : 
		'''
		start the timer to profile some operation
		### Returns:
		- (logger) the reference
		'''

	def endTimer (self) -> logger : 
		'''
		stop the timer and output the time into the log as amount of microseconds
		### Returns:
		- (logger) the reference
		'''

	def floatPrecission (self, signs: int = 2) -> logger : 
		'''
		set the precission of floating-point output
		### Returns:
		- (logger) the reference
		'''

class prim:
	def __init__(self): ...
	def class_name (self) -> any : 
		'''
		get the primitive class name.
		'''

	def name (self, s: str) -> prim : 
		'''
		set the primitive object name.
		### Parameters:
		- s (str): the object name
		### Returns:
		- (prim) the prim object reference
		'''

	def name (self) -> any : 
		'''
		get the primitive object name.
		'''

	def add (self, v: Volume) : 
		'''
		add the prim into scene
		### Parameters:
		- v (Volume): the scene volume reference
		'''

	def subtract (self, v: Volume) : 
		'''
		subtract the prim from scene
		### Parameters:
		- v (Volume): the scene volume reference
		'''

	def intersect (self, v: Volume) : 
		'''
		intersect the prim into scene
		### Parameters:
		- v (Volume): the scene volume reference
		'''

	def merge (self, v: Volume, op: BoolOpType) : 
		'''
		merge the prim into scene
		### Parameters:
		- v (Volume): the scene volume reference
		- op (BoolOpType): the type of the merge
		'''

	def mesh (self) -> Mesh : 
		'''
		get the mesh prim
		### Returns:
		- (Mesh) mesh object
		'''

	def color (self, CL: int) -> prim : 
		'''
		assign the color to the primitive (in voxels)
		### Parameters:
		- CL (int): color in hexadecimal form 0xAARRGGBB
		### Returns:
		- (prim) the reference
		'''

	def color (self, r: float, g: float, b: float, a: float) -> prim : 
		'''
		assign the color to the primitive (in voxels)
		### Parameters:
		- r (float): red value 0..255
		- g (float): green value 0..255
		- b (float): blue value 0..255
		- a (float): alpha value 0..255
		### Returns:
		- (prim) the reference
		'''

	def color (self, r: float, g: float, b: float) -> prim : 
		'''
		assign the color to the primitive (in voxels)
		### Parameters:
		- r (float): red value 0..255
		- g (float): green value 0..255
		- b (float): blue value 0..255
		### Returns:
		- (prim) the reference
		'''

	def color (self, colorid: str) -> prim : 
		'''
		assign the color to the primitive (in voxels)
		### Parameters:
		- colorid (str): the color in any suitable form: "RGB", "ARGB", "RRGGBB", "AARRGGBB", "#RGB", "#ARGB", "#RRGGBB", "#AARRGGBB",
		any web-color common name as "red", "green", "purple", google "webcolors"
		### Returns:
		- (prim) the reference
		'''

	def gloss (self, value: float) -> prim : 
		'''
		assign the gloss for the voxel primitive, it will work only if the color already assigned
		### Parameters:
		- value (float): the [0..1] value of the gloss
		### Returns:
		- (prim) the reference
		'''

	def roughness (self, value: float) -> prim : 
		'''
		assign the roughness for the voxel primitive, it will work only if the color already assigned
		### Parameters:
		- value (float): the [0..1] value of the roughness
		### Returns:
		- (prim) the reference
		'''

	def metal (self, value: float) -> prim : 
		'''
		the metalliclty value for the voxel primitive, it will work only if the color already assigned
		### Parameters:
		- value (float): the [0..1] metal value
		### Returns:
		- (prim) the reference
		'''

	def opacity (self, value: float) -> prim : 
		'''
		assign the opacity of the color over the voxel primitive. The color should be assigned before you assign the opacity,
		for example p.color("red").opacity(0.5)
		### Parameters:
		- value (float): the opacity value [0..1]
		### Returns:
		- (prim) the reference
		'''

	def details (self, det_level: float) -> prim : 
		'''
		set the detail level
		### Returns:
		- (prim) prim reference
		'''

	def details (self) -> float : 
		'''
		get the detail level
		### Returns:
		- (float) detail level
		'''

	def transform (self, t: mat4) -> prim : 
		'''
		set the transform matrix
		### Parameters:
		- t (mat4): the matrix
		### Returns:
		- (prim) prim reference
		'''

	def transform (self) -> mat4 : 
		'''
		get the transform matrix
		### Returns:
		- (mat4) matrix
		'''

	def scale (self, scale: float) -> prim : 
		'''
		set the scale
		### Parameters:
		- scale (float): the scale factor
		### Returns:
		- (prim) prim reference
		'''

	def scale (self, v: vec3) -> prim : 
		'''
		set the scale
		### Parameters:
		- v (vec3): the scale vector
		### Returns:
		- (prim) this primitive reference
		'''

	def scale (self) -> vec3 : 
		'''
		get the scale
		### Returns:
		- (vec3) the scale 3d vector
		'''

	def translate (self, _pos: vec3) -> prim : 
		'''
		Set the primitive translation
		### Parameters:
		- _pos (vec3): the new primitive position
		### Returns:
		- (prim) this primitive reference
		'''

	def translate (self) -> vec3 : 
		'''
		get the primitive translation
		### Returns:
		- (vec3) primitive translation
		'''

	def translate (self, x: float, y: float, z: float) -> prim : 
		'''
		Set the primitive translation
		### Parameters:
		- x (float): the new x primitive position
		- y (float): the new y primitive position
		- z (float): the new z primitive position
		### Returns:
		- (prim) this primitive reference
		'''

	def x (self, x: float) -> prim : 
		'''
		shift the primitive along the x - axis
		### Parameters:
		- x (float): the x value
		### Returns:
		- (prim) this primitive reference
		'''

	def y (self, y: float) -> prim : 
		'''
		shift the primitive along the y - axis
		### Parameters:
		- y (float): the y value
		### Returns:
		- (prim) this primitive reference
		'''

	def z (self, z: float) -> prim : 
		'''
		shift the primitive along the z - axis
		### Parameters:
		- z (float): the z value
		### Returns:
		- (prim) this primitive reference
		'''

	def auto_divide (self, average_div: float) -> prim : 
		'''
		set the auto devide
		### Parameters:
		- average_div (float): the average divide factor
		### Returns:
		- (prim) this prim reference
		'''

	def step_divide (self, step: float) -> prim : 
		'''
		set the step devide
		### Parameters:
		- step (float): the step divide factor
		### Returns:
		- (prim) primitive reference
		'''

	def fillet (self, radius: float) -> prim : 
		'''
		set the fillet
		### Parameters:
		- radius (float): the fillet radius
		### Returns:
		- (prim) this primitive reference
		'''

	@staticmethod
	def debug_on (isOn: bool = True) : 
		'''
		indicates whether to turn on or off the debug mode.
		### Parameters:
		- isOn (bool): if this parameter is true, the debug mode is on, otherwise the debug mode is off.
		'''

	@staticmethod
	def debug_clear () : 
		'''
		clear the debug info for primitive operations
		'''

	@staticmethod
	def push_transform (t: mat4) : 
		'''
		set the global transform matrix to all primitives
		### Parameters:
		- t (mat4): the matrix
		'''

	@staticmethod
	def push_translate (d: vec3) : 
		'''
		Set the translation to all primitives
		
		Not implemented yet
		### Parameters:
		- d (vec3): the new position of the primitives
		'''

	@staticmethod
	def push_scale (scale: float) : 
		'''
		Set the scale to all primitives
		
		Not implemented yet
		### Parameters:
		- scale (float): the new scale factor
		'''

	@staticmethod
	def push_scale (s: vec3) : 
		'''
		Set the scale to all primitives
		
		Not implemented yet
		'''

	@staticmethod
	def push_details (details_modulator: float) : 
		'''
		set the detail level to all primitives
		
		Not implemented yet
		### Parameters:
		- details_modulator (float): datail level
		'''

	@staticmethod
	def reset_transform () : 
		'''
		reset the global transform matrix
		
		Not implemented yet
		'''

	def fillet_relative (self) -> float : 
		'''
		calculates a fillet relative value (0..1).
		### Returns:
		- (float) fillet relative value
		'''

class box(prim):
	def __init__(self): ...
	def __init__(self, sizeX: float, sizeY: float, sizeZ: float): ...
	def __init__(self, size: vec3): ...
	def __init__(self, pos: vec3, size: vec3): ...
	def __init__(self, pos: vec3, size: vec3, fillet: float): ...
	def axis (self, directionX: vec3) -> box : 
		'''
		set the x-direction
		### Parameters:
		- directionX (vec3): the x-direction
		### Returns:
		- (box) box reference
		'''

	def axis (self, directionX: vec3, directionY: vec3) -> box : 
		'''
		set the x and y direction
		### Parameters:
		- directionX (vec3): the x-direction
		- directionY (vec3): the y-direction
		### Returns:
		- (box) box reference
		'''

	def axis (self, directionX: vec3, directionY: vec3, directionZ: vec3) -> box : 
		'''
		set the x, y and z direction
		### Parameters:
		- directionX (vec3): the x-direction
		- directionY (vec3): the y-direction
		- directionZ (vec3): the z-direction
		### Returns:
		- (box) box reference
		'''

	def reset_axis (self) -> box : 
		'''
		reset the x, y and z direction
		### Returns:
		- (box) box reference
		'''

	def axis_x (self) -> vec3 : 
		'''
		get the x-axis
		### Returns:
		- (vec3) vec3 axis
		'''

	def axis_y (self) -> vec3 : 
		'''
		get the y-axis
		### Returns:
		- (vec3) vec3 axis
		'''

	def axis_z (self) -> vec3 : 
		'''
		get the z-axis
		### Returns:
		- (vec3) vec3 axis
		'''

	def divide (self, nx: int, ny: int, nz: int) -> box : 
		'''
		set the number deviding
		### Parameters:
		- nx (int): number deviding along the x-axis
		- ny (int): number deviding along the y-axis
		- nz (int): number deviding along the z-axis
		### Returns:
		- (box) box reference
		'''

	def size (self, _size: vec3) -> box : 
		'''
		set the box size
		### Parameters:
		- _size (vec3): size
		### Returns:
		- (box) box reference
		'''

	def size (self, x: float, y: float, z: float) -> box : 
		'''
		set the box size
		### Parameters:
		- x (float): size x
		- y (float): size y
		- z (float): size z
		### Returns:
		- (box) box reference
		'''

	def size (self) -> vec3 : 
		'''
		get the box size.
		### Returns:
		- (vec3) size
		'''

	def fillet_relative (self) -> float : 
		'''
		calculates a fillet relative value (0..1).
		### Returns:
		- (float) fillet relative value
		'''

class torus(box):
	def __init__(self): ...
	def __init__(self, ringRadius: float, crossSectionRadius: float): ...
	def __init__(self, pos: vec3, ringRadius: float, crossSectionRadius: float): ...
	def slices (self, _slices: int) -> torus : 
		'''
		set the number of slices in the mesh.
		### Parameters:
		- _slices (int): number of slices.
		### Returns:
		- (torus) torus reference
		'''

	def slices (self) -> int : 
		'''
		get the number of slices in the mesh.
		### Returns:
		- (int) number of slices
		'''

	def rings (self, _rings: int) -> torus : 
		'''
		set the number of rings in the mesh.
		### Parameters:
		- _rings (int): number of rings.
		### Returns:
		- (torus) torus reference
		'''

	def rings (self) -> int : 
		'''
		get the number of rings in the mesh.
		### Returns:
		- (int) number of rings
		'''

	def radius (self, r: float) -> torus : 
		'''
		set the ring radius.
		### Parameters:
		- r (float): ring radius
		### Returns:
		- (torus) torus reference
		'''

	def radius (self) -> float : 
		'''
		get the ring radius.
		### Returns:
		- (float) ring radius
		'''

	def section_radius (self, section_r: float) -> torus : 
		'''
		set the cross section radius.
		### Parameters:
		- section_r (float): cross section radius
		### Returns:
		- (torus) torus reference
		'''

	def section_radius (self) -> float : 
		'''
		get the cross section radius.
		### Returns:
		- (float) cross section radius
		'''

	def diameter (self, d: float) -> torus : 
		'''
		set the ring diameter.
		### Parameters:
		- d (float): ring diameter
		### Returns:
		- (torus) torus reference
		'''

	def diameter (self) -> float : 
		'''
		get the ring diameter.
		### Returns:
		- (float) ring diameter
		'''

	def section_diameter (self, section_d: float) -> torus : 
		'''
		set the cross section diameter.
		### Parameters:
		- section_d (float): cross section diameter
		### Returns:
		- (torus) torus reference
		'''

	def section_diameter (self) -> float : 
		'''
		get the cross section diameter.
		### Returns:
		- (float) cross section diameter
		'''

	def sector_on (self, _switch: bool) -> torus : 
		'''
		set the flag to create a portion of torus.
		### Parameters:
		- _switch (bool): the boolean true/false value
		### Returns:
		- (torus) torus reference
		'''

	def sector_on (self) -> bool : 
		'''
		get the flag of creating a portion of torus. Default = false.
		### Returns:
		- (bool) the sector switch
		'''

	def slices_angle (self, angle: float) -> torus : 
		'''
		When sector is on, specifies the angle for torus slices. Default = 360 degrees.
		### Parameters:
		- angle (float): the angle for torus slices
		### Returns:
		- (torus) torus reference
		'''

	def slices_angle (self) -> float : 
		'''
		get the angle for torus slices
		### Returns:
		- (float) the slices angle
		'''

	def rings_angle (self, angle: float) -> torus : 
		'''
		When sector is on, specifies the angle for torus rings. Default = 360 degrees.
		### Parameters:
		- angle (float): the angle for torus rings
		### Returns:
		- (torus) torus reference
		'''

	def rings_angle (self) -> float : 
		'''
		get the angle for torus rings
		### Returns:
		- (float) the rings angle
		'''

class sphere(prim):
	def __init__(self): ...
	def __init__(self, radius: float): ...
	def __init__(self, pos: vec3, radius: float): ...
	def radius (self, r: float) -> sphere : 
		'''
		set the radius of the sphere.
		### Parameters:
		- r (float): radius.
		### Returns:
		- (sphere) sphere reference
		'''

	def radius (self) -> float : 
		'''
		get the radius of the sphere.
		### Returns:
		- (float) radius value
		'''

	def diameter (self, d: float) -> sphere : 
		'''
		set the diameter of the sphere.
		### Parameters:
		- d (float): diameter.
		### Returns:
		- (sphere) sphere reference
		'''

	def diameter (self) -> float : 
		'''
		get the diameter of the sphere.
		### Returns:
		- (float) diameter value
		'''

	def sub_division (self, subdiv: int) -> sphere : 
		'''
		set the degree for subdivision in the mesh.
		### Parameters:
		- subdiv (int): subdivision.
		### Returns:
		- (sphere) sphere reference
		'''

	def sub_division (self) -> int : 
		'''
		get the degree of subdivision triangular or cubic division of the sphere.
		### Returns:
		- (int) subdivision degree.
		'''

	def sub_div_mode (self, divmode: any) -> sphere : 
		'''
		set the division mode for the mesh.
		### Parameters:
		- divmode: mode of the mesh division.
		### Returns:
		- (sphere) sphere reference
		'''

	def sub_div_mode (self) -> any : 
		'''
		get the division mode for the mesh.
		### Returns:
		- (any) mode of the mesh division
		'''

	def rings (self, _rings: int) -> sphere : 
		'''
		set the number of rings in the mesh.
		### Parameters:
		- _rings (int): number of rings.
		### Returns:
		- (sphere) sphere reference
		'''

	def rings (self) -> int : 
		'''
		get the number of rings in the mesh.
		### Returns:
		- (int) number of rings
		'''

	def slices (self, _slices: int) -> sphere : 
		'''
		set the number of slices in the mesh.
		### Parameters:
		- _slices (int): number of slices.
		### Returns:
		- (sphere) sphere reference
		'''

	def slices (self) -> int : 
		'''
		get the number of slices in the mesh.
		### Returns:
		- (int) number of slices
		'''

	def sector_on (self, _switch: bool) -> sphere : 
		'''
		set the flag to create a portion of sphere.
		### Parameters:
		- _switch (bool): the boolean true/false value
		### Returns:
		- (sphere) sphere reference
		'''

	def sector_on (self) -> bool : 
		'''
		get the flag of creating a portion of sphere. Default = false.
		### Returns:
		- (bool) the sector switch
		'''

	def slice_from (self, angle: float) -> sphere : 
		'''
		When sector is on, specifies the angle where the sphere slice begins.
		### Parameters:
		- angle (float): the angle for sphere slice begin
		### Returns:
		- (sphere) sphere reference
		'''

	def slice_from (self) -> float : 
		'''
		get the angle where the sphere slice begins.
		### Returns:
		- (float) the slice begin angle
		'''

	def slice_to (self, angle: float) -> sphere : 
		'''
		When sector is on, specifies the angle where the sphere slice ends.
		### Parameters:
		- angle (float): the angle for sphere slice end
		### Returns:
		- (sphere) sphere reference
		'''

	def slice_to (self) -> float : 
		'''
		get the angle where the sphere slice ends.
		### Returns:
		- (float) the slice end angle
		'''

	def ring_from (self, angle: float) -> sphere : 
		'''
		When sector is on, specifies the angle where the sphere ring begins.
		### Parameters:
		- angle (float): the angle for sphere ring begin
		### Returns:
		- (sphere) sphere reference
		'''

	def ring_from (self) -> float : 
		'''
		get the angle where the sphere ring begins.
		### Returns:
		- (float) the ring begin angle
		'''

	def ring_to (self, angle: float) -> sphere : 
		'''
		When sector is on, specifies the angle where the sphere ring ends.
		### Parameters:
		- angle (float): the angle for sphere ring end
		### Returns:
		- (sphere) sphere reference
		'''

	def ring_to (self) -> float : 
		'''
		get the angle where the sphere ring ends.
		### Returns:
		- (float) the ring end angle
		'''

class ellipse(sphere):
	def __init__(self): ...
	def __init__(self, pos: vec3, rx: float, ry: float, rz: float): ...
	def __init__(self, pos: vec3, size: vec3): ...
	def __init__(self, size: vec3): ...
	def axis (self, directionX: vec3, directionY: vec3 = vec3.AxisY, directionZ: vec3 = vec3.AxisZ) -> ellipse : 
		'''
		set the axis x, y and z direction
		### Parameters:
		- directionX (vec3): the x-direction
		- directionY (vec3): the y-direction
		- directionZ (vec3): the z-direction
		### Returns:
		- (ellipse) ellipse reference
		'''

	def reset_axis (self) -> ellipse : 
		'''
		reset the x, y and z directions
		### Returns:
		- (ellipse) ellipse reference
		'''

	def size (self, _size: vec3) -> ellipse : 
		'''
		set the size of the ellipse.
		### Parameters:
		- _size (vec3): size
		### Returns:
		- (ellipse) ellipse reference
		'''

	def size (self) -> vec3 : 
		'''
		get the size of the ellipse.
		### Returns:
		- (vec3) ellipse size
		'''

class cylinder(prim):
	def __init__(self): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float, fillet: float = 0.0): ...
	def __init__(self, posTop: vec3, posBottom: vec3, radiusTop: float, radiusBottom: float, fillet: float = 0.0): ...
	def positionTop (self, pos: vec3) -> cylinder : 
		'''
		set the top position.
		### Parameters:
		- pos (vec3): position
		### Returns:
		- (cylinder) cylinder reference
		'''

	def positionTop (self) -> vec3 : 
		'''
		get the top position.
		### Returns:
		- (vec3) position
		'''

	def positionBottom (self, pos: vec3) -> cylinder : 
		'''
		set the bottom position.
		### Parameters:
		- pos (vec3): position
		### Returns:
		- (cylinder) cylinder reference
		'''

	def positionBottom (self) -> vec3 : 
		'''
		get the bottom position.
		### Returns:
		- (vec3) position
		'''

	def radiusTop (self, r: float) -> cylinder : 
		'''
		set the top radius.
		### Parameters:
		- r (float): radius
		### Returns:
		- (cylinder) cylinder reference
		'''

	def radiusTop (self) -> float : 
		'''
		get the top radius.
		### Returns:
		- (float) radius value
		'''

	def radiusBottom (self, r: float) -> cylinder : 
		'''
		set the bottom radius.
		### Parameters:
		- r (float): radius
		### Returns:
		- (cylinder) cylinder reference
		'''

	def radiusBottom (self) -> float : 
		'''
		get the bottom radius.
		### Returns:
		- (float) radius value
		'''

	def radius (self, r: float) -> cylinder : 
		'''
		set the radius.
		### Parameters:
		- r (float): radius
		### Returns:
		- (cylinder) cylinder reference
		'''

	def radius (self) -> float : 
		'''
		get the radius.
		### Returns:
		- (float) radius value
		'''

	def diameterTop (self, d: float) -> cylinder : 
		'''
		set the top diameter.
		### Parameters:
		- d (float): diameter
		### Returns:
		- (cylinder) cylinder reference
		'''

	def diameterTop (self) -> float : 
		'''
		get the top diameter.
		### Returns:
		- (float) diameter value
		'''

	def diameterBottom (self, r: float) -> cylinder : 
		'''
		set the bottom diameter.
		### Returns:
		- (cylinder) cylinder reference
		'''

	def diameterBottom (self) -> float : 
		'''
		get the bottom diameter.
		### Returns:
		- (float) diameter value
		'''

	def diameter (self, d: float) -> cylinder : 
		'''
		set the diameter.
		### Parameters:
		- d (float): diameter
		### Returns:
		- (cylinder) cylinder reference
		'''

	def diameter (self) -> float : 
		'''
		get the diameter.
		### Returns:
		- (float) diameter value
		'''

	def height (self, _height: float) -> cylinder : 
		'''
		set the height in the z-axis.
		### Parameters:
		- _height (float): height
		### Returns:
		- (cylinder) cylinder reference
		'''

	def height (self) -> float : 
		'''
		get the height.
		### Returns:
		- (float) height value
		'''

	def sectorAngle (self, angle: float) -> cylinder : 
		'''
		set the angle for cylinder with sector.
		### Parameters:
		- angle (float): the sector angle
		### Returns:
		- (cylinder) cylinder reference
		'''

	def sectorAngle (self) -> float : 
		'''
		get the sector angle.
		### Returns:
		- (float) angle value
		'''

	def topCapScale (self, scale: float) -> cylinder : 
		'''
		set the top cap scale.
		### Parameters:
		- scale (float): the scale value
		### Returns:
		- (cylinder) cylinder reference
		'''

	def topCapScale (self) -> float : 
		'''
		get the top cap scale.
		### Returns:
		- (float) the scale value
		'''

	def bottomCapScale (self, scale: float) -> cylinder : 
		'''
		set the bottom cap scale.
		### Parameters:
		- scale (float): the scale value
		### Returns:
		- (cylinder) cylinder reference
		'''

	def bottomCapScale (self) -> float : 
		'''
		get the bottom cap scale.
		### Returns:
		- (float) the scale value
		'''

	def slices (self, nslices: int) -> cylinder : 
		'''
		set the number of slices in the mesh.
		### Parameters:
		- nslices (int): number of slices.
		### Returns:
		- (cylinder) cylinder reference
		'''

	def slices (self) -> int : 
		'''
		get the number of slices in the mesh.
		### Returns:
		- (int) number of slices.
		'''

	def rings (self, nrings: int) -> cylinder : 
		'''
		set the number of rings in the mesh.
		### Parameters:
		- nrings (int): number of rings.
		### Returns:
		- (cylinder) cylinder reference
		'''

	def rings (self) -> int : 
		'''
		get the number of rings in the mesh.
		### Returns:
		- (int) number of rings.
		'''

	def caps (self, ncaps: int) -> cylinder : 
		'''
		set the number of caps in the mesh.
		### Parameters:
		- ncaps (int): number of caps.
		### Returns:
		- (cylinder) cylinder reference
		'''

	def caps (self) -> int : 
		'''
		get the number of caps in the mesh.
		### Returns:
		- (int) number of caps.
		'''

	def fillet_relative (self) -> float : 
		'''
		calculates a fillet relative value (0..1).
		### Returns:
		- (float) fillet relative value
		'''

class cone(cylinder):
	def __init__(self): ...
	def __init__(self, height: float, radiusBottom: float, fillet: float = 0.0): ...
	def __init__(self, posTop: vec3, posBottom: vec3, radiusBottom: float, fillet: float = 0.0): ...
	def radius (self, r: float) -> cone : 
		'''
		set the value of radius.
		### Parameters:
		- r (float): radius
		### Returns:
		- (cone) cone reference
		'''

	def radius (self) -> float : 
		'''
		get the value of radius.
		### Returns:
		- (float) radius value
		'''

	def diameter (self, d: float) -> cone : 
		'''
		set the value of diameter.
		### Parameters:
		- d (float): diameter
		### Returns:
		- (cone) cone reference
		'''

	def diameter (self) -> float : 
		'''
		get the value of diameter.
		### Returns:
		- (float) diameter value
		'''

	def fillet_relative (self) -> float : 
		'''
		calculates a fillet relative value (0..1).
		### Returns:
		- (float) fillet relative value
		'''

class tube(cylinder):
	def __init__(self): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float, fillet: float): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float, relativeHoleRadius: float, fillet: float): ...
	def __init__(self, posTop: vec3, posBottom: vec3, radiusTop: float, radiusBottom: float, relativeHoleRadius: float): ...
	def __init__(self, posTop: vec3, posBottom: vec3, radiusTop: float, radiusBottom: float, relativeHoleRadius: float, fillet: float): ...
	def relativeHoleRadius (self, r: float) -> tube : 
		'''
		set the relative value of the hole radius.
		### Parameters:
		- r (float): relative value
		### Returns:
		- (tube) tube reference
		'''

	def relativeHoleRadius (self) -> float : 
		'''
		get the relative value of the hole radius.
		### Returns:
		- (float) relative value (0..1)
		'''

	def thickness (self, w: float) -> tube : 
		'''
		set the wall thickness value.
		### Parameters:
		- w (float): thickness value
		### Returns:
		- (tube) tube reference
		'''

	def thickness (self) -> float : 
		'''
		get the relative value of the hole radius.
		### Returns:
		- (float) relative value (0..1)
		'''

	def fillet_relative (self) -> float : 
		'''
		calculates a fillet relative value (0..1).
		### Returns:
		- (float) fillet relative value
		'''

class gear(tube):
	def __init__(self): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float, depth: float, sharpness: float = 0.5, order: int = 16): ...
	def __init__(self, posTop: vec3, posBottom: vec3, radiusTop: float, radiusBottom: float, depth: float = 0.1, sharpness: float = 0.5, order: int = 16): ...
	def depth (self, __depth: float) -> gear : 
		'''
		set the depth value.
		### Parameters:
		- __depth (float): depth value
		### Returns:
		- (gear) gear reference
		'''

	def depth (self) -> float : 
		'''
		get the depth value.
		### Returns:
		- (float) depth value
		'''

	def sharpness (self, sharp: float) -> gear : 
		'''
		set the sharpness value.
		### Parameters:
		- sharp (float): sharpness value
		### Returns:
		- (gear) gear reference
		'''

	def sharpness (self) -> float : 
		'''
		get the depth value.
		### Returns:
		- (float) depth value
		'''

	def order (self, nteeth: int) -> gear : 
		'''
		set the number of teeth in gear.
		### Parameters:
		- nteeth (int): number of teeth
		### Returns:
		- (gear) gear reference
		'''

	def order (self) -> int : 
		'''
		get the number of teeth in gear.
		### Returns:
		- (int) the number of teeth
		'''

class ngon(gear):
	def __init__(self): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float, order: int): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float, fillet: float, order: int): ...
	def __init__(self, posTop: vec3, posBottom: vec3, radiusTop: float, radiusBottom: float, order: int): ...
	def fillet_relative (self) -> float : 
		'''
		calculates a fillet relative value (0..1).
		### Returns:
		- (float) fillet relative value
		'''

class capsule(cylinder):
	def __init__(self): ...
	def __init__(self, height: float, radiusTop: float, radiusBottom: float): ...
	def __init__(self, posTop: vec3, posBottom: vec3, radiusTop: float, radiusBottom: float): ...
class spiral(prim):
	def __init__(self): ...
	def __init__(self, out_radius: float, in_radius: float, _sstep: float, nturns: float): ...
	def radius (self, r: float) -> spiral : 
		'''
		set the outer radius of the spiral.
		### Parameters:
		- r (float): radius value
		### Returns:
		- (spiral) spiral reference
		'''

	def radius (self) -> float : 
		'''
		get the outer radius.
		### Returns:
		- (float) outer radius
		'''

	def profile_radius (self, r: float) -> spiral : 
		'''
		set the profile radius.
		### Parameters:
		- r (float): radius value
		### Returns:
		- (spiral) spiral reference
		'''

	def profile_radius (self) -> float : 
		'''
		get the profile radius.
		### Returns:
		- (float) profile radius
		'''

	def diameter (self, d: float) -> spiral : 
		'''
		set the outer diameter of the spiral.
		### Parameters:
		- d (float): diameter value
		### Returns:
		- (spiral) spiral reference
		'''

	def diameter (self) -> float : 
		'''
		get the outer diameter.
		### Returns:
		- (float) outer diameter
		'''

	def profile_diameter (self, d: float) -> spiral : 
		'''
		set the profile diameter.
		### Parameters:
		- d (float): diameter value
		### Returns:
		- (spiral) spiral reference
		'''

	def profile_diameter (self) -> float : 
		'''
		get the profile diameter.
		### Returns:
		- (float) profile diameter
		'''

	def turns (self, nturns: int) -> spiral : 
		'''
		set the number of turns.
		### Parameters:
		- nturns (int): turns count
		### Returns:
		- (spiral) spiral reference
		'''

	def turns (self) -> int : 
		'''
		get the number of turns.
		### Returns:
		- (int) turns count
		'''

	def step (self, vstep: float) -> spiral : 
		'''
		set the spiral step.
		### Parameters:
		- vstep (float): step value
		### Returns:
		- (spiral) spiral reference
		'''

	def step (self) -> float : 
		'''
		get the spiral step.
		### Returns:
		- (float) step value
		'''

	def profile_type (self, type: SpiralProfile) -> spiral : 
		'''
		set the type of profile (circle or rectangle).
		### Parameters:
		- type (SpiralProfile): profile type
		### Returns:
		- (spiral) spiral reference
		'''

	def profile_rect (self, width: float, height: float) -> spiral : 
		'''
		set the dimensions for the rectangle profile.
		### Parameters:
		- width (float): the width value
		- height (float): the height value
		### Returns:
		- (spiral) spiral reference
		'''

	def clock_wise (self, clockWise: bool) -> spiral : 
		'''
		set the clockwise direction of the spiral.
		### Parameters:
		- clockWise (bool): the indicator of the clockwise direction
		### Returns:
		- (spiral) spiral reference
		'''

	def clock_wise (self) -> bool : 
		'''
		get the clokwise direction of the spiral.
		### Returns:
		- (bool) the clokwise direction( true or false)
		'''

	def profile_height (self) -> float : 
		'''
		get the profile height for rectangle profile.
		### Returns:
		- (float) the profile height
		'''

	def profile_width (self) -> float : 
		'''
		get the profile width for rectangle profile.
		### Returns:
		- (float) the profile width
		'''

	def slices (self, nslices: int) -> spiral : 
		'''
		set the number of slices in the mesh.
		### Parameters:
		- nslices (int): number of slices.
		### Returns:
		- (spiral) spiral reference
		'''

	def slices (self) -> int : 
		'''
		get the number of slices in the mesh.
		### Returns:
		- (int) number of slices
		'''

	def rings (self, nrings: int) -> spiral : 
		'''
		set the number of rings in the mesh.
		### Parameters:
		- nrings (int): number of rings.
		### Returns:
		- (spiral) spiral reference
		'''

	def rings (self) -> int : 
		'''
		get the number of rings in the mesh.
		### Returns:
		- (int) number of rings
		'''

	def caps (self, ncaps: int) -> spiral : 
		'''
		set the number of caps in the mesh.
		### Parameters:
		- ncaps (int): number of caps.
		### Returns:
		- (spiral) spiral reference
		'''

	def caps (self) -> int : 
		'''
		get the number of caps in the mesh.
		### Returns:
		- (int) number of caps
		'''

class FontInfo:
	size: int
	weight: int
	style: int
	fname: any
class Font:
	def __init__(self): ...
	def __init__(self, _finfo: FontInfo): ...
	def __init__(self, _fname: str): ...
	def __init__(self, _fname: str, _st: int): ...
	def size (self, _size: int) -> Font : 
		'''
		set the font size
		### Parameters:
		- _size (int): font size property
		### Returns:
		- (Font) font reference
		'''

	def size (self) -> int : 
		'''
		get the font size
		### Returns:
		- (int) font size
		'''

	def weight (self, weight: int) -> Font : 
		'''
		set the font weight
		### Parameters:
		- weight (int): font weight property
		### Returns:
		- (Font) font reference
		'''

	def weight (self) -> int : 
		'''
		get the font weight
		### Returns:
		- (int) font weight
		'''

	def style (self, st: int) -> Font : 
		'''
		set the style of the font
		### Parameters:
		- st (int): the new font style
		### Returns:
		- (Font) font reference
		'''

	def style (self) -> int : 
		'''
		get the font style
		### Returns:
		- (int) the font style
		'''

	def name (self, _fname: str) -> Font : 
		'''
		set the font name
		### Parameters:
		- _fname (str): the font name
		### Returns:
		- (Font) font reference
		'''

	def name (self) -> str : 
		'''
		get the font name
		### Returns:
		- (str) the font name
		'''

	def select (self) : 
		'''
		selects a font object into the viewport
		'''

class text(prim):
	def __init__(self): ...
	def __init__(self, s: str): ...
	def string (self, s: str) -> text : 
		'''
		set the text's string.
		### Parameters:
		- s (str): the string
		'''

	def string (self) -> any : 
		'''
		get the text's string.
		### Returns:
		- (any) the string
		'''

	def font (self, f: Font) -> text : 
		'''
		set the text font
		### Parameters:
		- f (Font): font object
		### Returns:
		- (text) the text reference
		'''

	def font (self) -> Font : 
		'''
		get the font object
		### Returns:
		- (Font) font object
		'''

	def width (self, w: float) -> text : 
		'''
		set the text width in the pixels
		### Parameters:
		- w (float): width
		### Returns:
		- (text) the text reference
		'''

	def width (self) -> float : 
		'''
		get the text width
		### Returns:
		- (float) the width value
		'''

	def depth (self, d: float) -> text : 
		'''
		set the text depth in the pixels
		### Parameters:
		- d (float): depth
		### Returns:
		- (text) the text reference
		'''

	def depth (self) -> float : 
		'''
		get the text depth
		### Returns:
		- (float) the depth value
		'''

	def bendRadius (self, radius: float) -> text : 
		'''
		set the bend radius.
		### Parameters:
		- radius (float): bend radius of the text
		### Returns:
		- (text) the text reference
		'''

	def bendRadius (self) -> float : 
		'''
		get the bend radius.
		### Returns:
		- (float) the bend radius of the text
		'''

	def extraRotation (self, rotation: float) -> text : 
		'''
		set the rotate angle around the x-axis.
		### Returns:
		- (text) the text reference
		'''

	def extraRotation (self) -> float : 
		'''
		get the rotate angle around the x-axis.
		### Returns:
		- (float) the rotate angle
		'''

	def invertBending (self, _binvert: bool) -> text : 
		'''
		set the invert of the text bending.
		### Returns:
		- (text) the text reference
		'''

	def invertBending (self) -> float : 
		'''
		get the invert of the text bending.
		### Returns:
		- (float) the invert bending
		'''

class lathe(box):
	def __init__(self): ...
	def __init__(self): ...
	def type (self, t: any) -> lathe : 
		'''
		set the lathe type
		### Parameters:
		- t: type value (cylinder or rectangle)
		### Returns:
		- (lathe) the lathe reference
		'''

	def type (self) -> any : 
		'''
		get the lathe type.
		### Returns:
		- (any) the type value
		'''

	def add_point (self, point: vec2, st: int) -> lathe : 
		'''
		add the point into curve
		### Parameters:
		- point (vec2): the 2d point
		- st (int): the point state
		### Returns:
		- (lathe) lathe reference
		'''

	def profile (self) -> any : 
		'''
		get the pointer to the profile
		### Returns:
		- (any) the profile pointer
		'''

	def reset (self) -> lathe : 
		'''
		reset the curve points
		'''

	def clear (self) -> lathe : 
		'''
		clear points of the profile
		'''

class image(text):
	def __init__(self): ...
	def topTexture (self, _texture: str) -> image : 
		'''
		set the top texture
		### Parameters:
		- _texture (str): image file name
		### Returns:
		- (image) the image reference
		'''

	def topTexture (self) -> any : 
		'''
		get the top texture
		### Returns:
		- (any) the string of the image file name
		'''

	def topBumpTexture (self, _texture: str) -> image : 
		'''
		set the top bump texture
		### Parameters:
		- _texture (str): image file name
		### Returns:
		- (image) the image reference
		'''

	def topBumpTexture (self) -> any : 
		'''
		get the top bump texture
		### Returns:
		- (any) the string of the image file name
		'''

	def bottomTexture (self, _texture: str) -> image : 
		'''
		set the bottom texture
		### Parameters:
		- _texture (str): image file name
		### Returns:
		- (image) the image reference
		'''

	def bottomTexture (self) -> any : 
		'''
		get the bottom texture
		### Returns:
		- (any) the string of the image file name
		'''

	def bottomBumpTexture (self, _texture: str) -> image : 
		'''
		set the bottom bump texture
		### Parameters:
		- _texture (str): image file name
		### Returns:
		- (image) the image reference
		'''

	def bottomBumpTexture (self) -> any : 
		'''
		get the bottom bump texture
		### Returns:
		- (any) the string of the image file name
		'''

	def strencilTexture (self, _texture: str) -> image : 
		'''
		set the strencil texture
		### Parameters:
		- _texture (str): image file name
		### Returns:
		- (image) the image reference
		'''

	def strencilTexture (self) -> any : 
		'''
		get the strencil texture
		### Returns:
		- (any) the string of the image file name
		'''

	def bottomStrencilTexture (self, _texture: str) -> image : 
		'''
		set the bottom strencil texture
		### Parameters:
		- _texture (str): image file name
		### Returns:
		- (image) the image reference
		'''

	def bottomStrencilTexture (self) -> any : 
		'''
		get the bottom strencil texture
		### Returns:
		- (any) the string of the image file name
		'''

	def basicThickness (self, _thickness: float) -> image : 
		'''
		set the basic thickness of image
		### Parameters:
		- _thickness (float): thickness value
		### Returns:
		- (image) the image reference
		'''

	def basicThickness (self) -> float : 
		'''
		get the basic thickness of image
		### Returns:
		- (float) the thickness value
		'''

	def bumpThickness (self, _thickness: float) -> image : 
		'''
		set the bump thickness of image
		### Parameters:
		- _thickness (float): thickness value
		### Returns:
		- (image) the image reference
		'''

	def bumpThickness (self) -> float : 
		'''
		get the bump thickness of image
		### Returns:
		- (float) the thickness value
		'''

	def taperAngle (self, _angle: float) -> image : 
		'''
		set the angle of tapering
		### Parameters:
		- _angle (float): taper angle value
		### Returns:
		- (image) the image reference
		'''

	def taperAngle (self) -> float : 
		'''
		get the angle of tapering of image
		### Returns:
		- (float) the taper angle value
		'''

	def topBottomWeight (self, weight: float) -> image : 
		'''
		set the weight of the top and bottom image
		### Parameters:
		- weight (float): weight value
		### Returns:
		- (image) the image reference
		'''

	def topBottomWeight (self) -> float : 
		'''
		get the weight of the top and bottom image
		### Returns:
		- (float) the weight value
		'''

	def sizeInScene (self, _size: float) -> image : 
		'''
		set the size of image in the scene
		### Parameters:
		- _size (float): size value
		### Returns:
		- (image) the image reference
		'''

	def sizeInScene (self) -> float : 
		'''
		get the size of image in the scene
		### Returns:
		- (float) the size value
		'''

class thread(prim):
	def __init__(self): ...
	def diameter (self, d: float) -> thread : 
		'''
		set the diameter of the thread.
		### Parameters:
		- d (float): diameter value
		### Returns:
		- (thread) thread reference
		'''

	def diameter (self) -> float : 
		'''
		get the diameter of the thread.
		### Returns:
		- (float) thread diameter
		'''

	def pitch (self, p: float) -> thread : 
		'''
		set the pitch of the thread.
		### Parameters:
		- p (float): pitch value
		### Returns:
		- (thread) thread reference
		'''

	def pitch (self) -> float : 
		'''
		set the pitch of the thread.
		### Returns:
		- (float) pitch value
		'''

	def stub (self, l: float) -> thread : 
		'''
		set the stub length of the thread.
		### Parameters:
		- l (float): stub length value
		### Returns:
		- (thread) thread reference
		'''

	def stub (self) -> float : 
		'''
		get the stub length of the thread.
		### Returns:
		- (float) stub length value
		'''

	def height (self, h: float) -> thread : 
		'''
		set the height of the thread.
		### Parameters:
		- h (float): height value
		### Returns:
		- (thread) thread reference
		'''

	def height (self) -> float : 
		'''
		get the height of the thread.
		### Returns:
		- (float) height value
		'''

	def turns (self, n: int) -> thread : 
		'''
		set the number of the thread turns.
		### Parameters:
		- n (int): turns count
		### Returns:
		- (thread) thread reference
		'''

	def turns (self) -> int : 
		'''
		get the number of the thread turns.
		### Returns:
		- (int) turns count
		'''

	def clockwise (self, cw: bool) -> thread : 
		'''
		set the clockwise flag of the thread.
		### Parameters:
		- cw (bool): if value is true then thread direction is clockwise
		### Returns:
		- (thread) thread reference
		'''

	def clockwise (self) -> bool : 
		'''
		get the clockwise of the thread.
		### Returns:
		- (bool) clockwise flag
		'''

	def close (self, b: bool) -> thread : 
		'''
		set the closed thread.
		### Parameters:
		- b (bool): closed value
		### Returns:
		- (thread) thread reference
		'''

	def close (self) -> bool : 
		'''
		set the closed thread.
		### Returns:
		- (bool) closed flag
		'''

	def profile (self, prf: ThreadProfile) -> thread : 
		'''
		set the thread profile type.
		### Parameters:
		- prf (ThreadProfile): profile type
		### Returns:
		- (thread) thread reference
		'''

	def profile (self) -> ThreadProfile : 
		'''
		get the thread profile type.
		### Returns:
		- (ThreadProfile) profile type
		'''

class threadStud(thread):
	def __init__(self): ...
	def diameter (self, d: float) -> threadStud : 
		'''
		set the diameter of the thread.
		### Parameters:
		- d (float): diameter value
		### Returns:
		- (threadStud) thread stud reference
		'''

	def diameter (self) -> float : 
		'''
		get the diameter of the thread.
		### Returns:
		- (float) diameter value
		'''

	def diameterTop (self, d: float) -> threadStud : 
		'''
		get the top diameter of the thread.
		### Parameters:
		- d (float): diameter value
		### Returns:
		- (threadStud) thread stud reference
		'''

	def diameterTop (self) -> float : 
		'''
		get the top diameter of the thread.
		### Returns:
		- (float) diameter value
		'''

	def diameterBottom (self, d: float) -> threadStud : 
		'''
		set the bottom diameter of the thread.
		### Parameters:
		- d (float): diameter value
		### Returns:
		- (threadStud) thread stud reference
		'''

	def diameterBottom (self) -> float : 
		'''
		get the bottom diameter of the thread.
		### Returns:
		- (float) diameter value
		'''

	def length (self, l: float) -> threadStud : 
		'''
		set the stud length.
		### Parameters:
		- l (float): length value
		### Returns:
		- (threadStud) thread stud reference
		'''

	def length (self) -> float : 
		'''
		get the length of the stud.
		### Returns:
		- (float) length value
		'''

	def threadLength (self) -> float : 
		'''
		get the length of the thread.
		### Returns:
		- (float) length value
		'''

	def enableThread (self, enable: bool) -> threadStud : 
		'''
		enabled or disabled thread in the stud.
		### Returns:
		- (threadStud) thread stud reference
		'''

	def enableThread (self) -> bool : 
		'''
		get the indicator of the enabled thread.
		### Returns:
		- (bool) enabled/disabled value
		'''

	def bodyType (self, bt: ThreadStudBodyType) -> threadStud : 
		'''
		set the body type.
		### Parameters:
		- bt (ThreadStudBodyType): body type
		### Returns:
		- (threadStud) thread stud reference
		'''

	def bodyType (self) -> ThreadStudBodyType : 
		'''
		get the body type.
		### Returns:
		- (ThreadStudBodyType) type value
		'''

class Slit:
	def __init__(self): ...
	def __init__(self, w: float, h: float, d: float, t: SlitType): ...
	def type (self, _t: int) -> Slit : 
		'''
		set the slit type.
		### Parameters:
		- _t (int): type value
		### Returns:
		- (Slit) slit reference
		'''

	def type (self) -> int : 
		'''
		get the slit type.
		### Returns:
		- (int) type value
		'''

	def width (self, _w: float) -> Slit : 
		'''
		set the width.
		### Parameters:
		- _w (float): width value
		### Returns:
		- (Slit) slit reference
		'''

	def width (self) -> float : 
		'''
		get the width.
		### Returns:
		- (float) width value
		'''

	def height (self, _h: float) -> Slit : 
		'''
		set the height.
		### Parameters:
		- _h (float): height value
		### Returns:
		- (Slit) slit reference
		'''

	def height (self) -> float : 
		'''
		get the height.
		### Returns:
		- (float) height value
		'''

	def depth (self, _d: float) -> Slit : 
		'''
		set the depth.
		### Parameters:
		- _d (float): depth value
		### Returns:
		- (Slit) slit reference
		'''

	def depth (self) -> float : 
		'''
		get the depth.
		### Returns:
		- (float) depth value
		'''

class HeadParams:
	def __init__(self): ...
	def __init__(self, _type: int, _param: any): ...
	def __init__(self): ...
	def setData (self, _type: int, param: any) -> HeadParams : 
		'''
		set the parameters data with specified type.
		### Parameters:
		- _type (int): head type
		'''

	def getData (self) -> any : 
		'''
		get the head data
		### Returns:
		- (any) pointer to the head data
		'''

	def __assign__ (self, h: HeadParams) -> HeadParams : ...
	def copy (self, h: HeadParams) : 
		'''
		copies the HeadParams object
		'''

	def release (self) : 
		'''
		release the data
		'''

class HeadBaseParams:
	def __init__(self): ...
	def __init__(self, _d: float, _h: float): ...
	def diameter (self, _d: float) -> HeadBaseParams : 
		'''
		set the diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (HeadBaseParams) HeadBaseParams reference
		'''

	def height (self, _h: float) -> HeadBaseParams : 
		'''
		set the height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (HeadBaseParams) HeadBaseParams reference
		'''

	_diameter: float
	_height: float
class TShapedParams:
	def __init__(self): ...
	def __init__(self, _d: float, _h: float, _w: float): ...
	def diameter (self, _d: float) -> TShapedParams : 
		'''
		set the diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (TShapedParams) TShapedParams reference
		'''

	def height (self, _h: float) -> TShapedParams : 
		'''
		set the height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (TShapedParams) TShapedParams reference
		'''

	def width (self, _w: float) -> TShapedParams : 
		'''
		set the width.
		### Parameters:
		- _w (float): width
		### Returns:
		- (TShapedParams) TShapedParams reference
		'''

	_diameter: float
	_height: float
	_width: float
class LambParams:
	def __init__(self): ...
	def __init__(self, _l: float, _dtop: float, _dbottom: float, _hh: float, _h: float, _thick: float): ...
	def length (self, _l: float) -> LambParams : 
		'''
		set the length.
		### Parameters:
		- _l (float): length
		### Returns:
		- (LambParams) LambParams reference
		'''

	def diameterTop (self, _d: float) -> LambParams : 
		'''
		set the top diameter.
		### Parameters:
		- _d (float): top diameter
		### Returns:
		- (LambParams) LambParams reference
		'''

	def diameterBottom (self, _d: float) -> LambParams : 
		'''
		set the bottom diameter.
		### Parameters:
		- _d (float): bottom diameter
		### Returns:
		- (LambParams) LambParams reference
		'''

	def height (self, _h: float) -> LambParams : 
		'''
		set the height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (LambParams) LambParams reference
		'''

	def headHeight (self, _h: float) -> LambParams : 
		'''
		set the head height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (LambParams) LambParams reference
		'''

	def thickness (self, _t: float) -> LambParams : 
		'''
		set the thickness.
		### Parameters:
		- _t (float): thickness
		### Returns:
		- (LambParams) LambParams reference
		'''

	_length: float
	_diameterTop: float
	_diameterBottom: float
	_headHeight: float
	_height: float
	_thickness: float
class RimParams:
	def __init__(self): ...
	def __init__(self, _d: float, _h: float, _d1: float, _d2: float): ...
	def shoulderDiameter (self, _d: float) -> RimParams : 
		'''
		set the shoulder diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (RimParams) RimParams reference
		'''

	def shoulderHeight (self, _h: float) -> RimParams : 
		'''
		set the shoulder height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (RimParams) RimParams reference
		'''

	def inRingDiameter (self, _d: float) -> RimParams : 
		'''
		set the inner ring diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (RimParams) RimParams reference
		'''

	def outRingDiameter (self, _d: float) -> RimParams : 
		'''
		set the outer ring diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (RimParams) RimParams reference
		'''

	_shoulderDiameter: float
	_shoulderHeight: float
	_inRingDiameter: float
	_outRingDiameter: float
class EyeParams:
	def __init__(self): ...
	def __init__(self, _thick: float, _d1: float, _d2: float): ...
	def inRingDiameter (self, _d: float) -> EyeParams : 
		'''
		set the inner ring diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (EyeParams) EyeParams reference
		'''

	def outRingDiameter (self, _d: float) -> EyeParams : 
		'''
		set the outer ring diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (EyeParams) EyeParams reference
		'''

	def thickness (self, _t: float) -> EyeParams : 
		'''
		set the thickness.
		### Parameters:
		- _t (float): thickness
		### Returns:
		- (EyeParams) EyeParams reference
		'''

	_thickness: float
	_inRingDiameter: float
	_outRingDiameter: float
class boltHead(prim):
	def __init__(self): ...
	def head (self, _h: HeadParams) -> boltHead : 
		'''
		set the head object.
		### Parameters:
		- _h (HeadParams): head obj reference
		### Returns:
		- (boltHead) bolt head reference
		'''

	def head (self) -> HeadParams : 
		'''
		get the HeadParams object.
		### Returns:
		- (HeadParams) HeadParams object reference
		'''

	def head (self) -> HeadParams : 
		'''
		get the const HeadParams object.
		### Returns:
		- (HeadParams) HeadParams object reference
		'''

	def head (self, _type: int, data: any) -> boltHead : 
		'''
		set the head object with specified type and data.
		### Parameters:
		- _type (int): head type
		### Returns:
		- (boltHead) bolt head reference
		'''

	def slit (self, _s: Slit) -> boltHead : 
		'''
		set the slit object.
		### Parameters:
		- _s (Slit): slit reference.
		### Returns:
		- (boltHead) bolt head reference
		'''

	def slit (self) -> Slit : 
		'''
		get the slit object.
		### Returns:
		- (Slit) slit object reference
		'''

	def slit (self) -> Slit : 
		'''
		get the const slit object.
		### Returns:
		- (Slit) slit object reference
		'''

	def __assign__ (self, h: boltHead) -> boltHead : ...
class NutHeadBaseParams:
	def __init__(self): ...
	def __init__(self, t: NutType, d: float, h: float): ...
	def diameter (self, d: float) -> NutHeadBaseParams : 
		'''
		set the diameter.
		### Parameters:
		- d (float): diameter
		### Returns:
		- (NutHeadBaseParams) NutRadialParams reference
		'''

	def diameter (self) -> float : 
		'''
		get the diameter.
		### Returns:
		- (float) diameter
		'''

	def height (self, h: float) -> NutHeadBaseParams : 
		'''
		set the height.
		### Parameters:
		- h (float): height value.
		### Returns:
		- (NutHeadBaseParams) NutHeadBaseParams reference
		'''

	def height (self) -> float : 
		'''
		get the height.
		### Returns:
		- (float) height value
		'''

	def type (self, t: int) -> NutHeadBaseParams : 
		'''
		set the nut type.
		### Parameters:
		- t (int): type value.
		### Returns:
		- (NutHeadBaseParams) NutHeadBaseParams reference
		'''

	def type (self) -> int : 
		'''
		set the nut type.
		### Returns:
		- (int) type value.
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an object.
		'''

class NutHexaParams(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float): ...
class NutAcornParams(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float, h1: float): ...
	def facetHeight (self, _h: float) -> NutAcornParams : 
		'''
		set the facet height.
		### Parameters:
		- _h (float): height value.
		### Returns:
		- (NutAcornParams) NutAcornParams reference
		'''

	def facetHeight (self) -> float : 
		'''
		get the facet height.
		### Returns:
		- (float) facet height value.
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the NutAcornParams object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the NutAcornParams object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an NutAcornParams object.
		'''

class NutLowAcornParams(NutAcornParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float, h1: float): ...
class NutSelfLockParams(NutAcornParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float, h1: float): ...
class NutTShapedParams(NutAcornParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float, h1: float): ...
class NutFlangeParams(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float): ...
	def __init__(self, d: float, h: float, fw: float, fh: float): ...
	def facetWidth (self, w: float) -> NutFlangeParams : 
		'''
		set the width.
		### Parameters:
		- w (float): width value.
		### Returns:
		- (NutFlangeParams) NutFlangeParams reference
		'''

	def facetHeight (self, h: float) -> NutFlangeParams : 
		'''
		set the facet height.
		### Parameters:
		- h (float): height value.
		### Returns:
		- (NutFlangeParams) NutFlangeParams reference
		'''

	def facetWidth (self) -> float : 
		'''
		get the width.
		### Returns:
		- (float) width value.
		'''

	def facetHeight (self) -> float : 
		'''
		get the height.
		### Returns:
		- (float) height value.
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the NutFlangeParams object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the NutFlangeParams object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an NutFlangeParams object.
		'''

class NutRadialParams(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float): ...
	def __init__(self, d: float, h: float, d1: float, d2: float): ...
	def holeDiameter (self, d: float) -> NutRadialParams : 
		'''
		set the hole diameter.
		### Parameters:
		- d (float): diameter
		### Returns:
		- (NutRadialParams) NutRadialParams reference
		'''

	def holeDepth (self, d: float) -> NutRadialParams : 
		'''
		set the hole depth.
		### Parameters:
		- d (float): depth
		### Returns:
		- (NutRadialParams) NutRadialParams reference
		'''

	def holeDiameter (self) -> float : 
		'''
		set the hole diameter.
		### Returns:
		- (float) hole diameter
		'''

	def holeDepth (self) -> float : 
		'''
		get the hole depth.
		### Returns:
		- (float) NutRadialParams hole depth
		'''

	def holePlace (self, place: int) -> NutRadialParams : 
		'''
		set the hole place (0 - face, 1 - side).
		### Parameters:
		- place (int): place flag
		### Returns:
		- (NutRadialParams) NutRadialParams reference
		'''

	def holePlace (self) -> int : 
		'''
		get the hole place.
		### Returns:
		- (int) place flag 0 - face, 1 - side
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the radial object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the radial object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an radial object.
		'''

class NutLambParams(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float): ...
	def length (self, _l: float) -> NutLambParams : 
		'''
		set the length.
		### Parameters:
		- _l (float): length
		### Returns:
		- (NutLambParams) NutLambParams reference
		'''

	def diameterBottom (self, _d: float) -> NutLambParams : 
		'''
		set the bottom diameter.
		### Parameters:
		- _d (float): bottom diameter
		### Returns:
		- (NutLambParams) NutLambParams reference
		'''

	def diameterTop (self, _d: float) -> NutLambParams : 
		'''
		set the top diameter.
		### Parameters:
		- _d (float): top diameter
		### Returns:
		- (NutLambParams) NutLambParams reference
		'''

	def headHeight (self, _h: float) -> NutLambParams : 
		'''
		set the head height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (NutLambParams) NutLambParams reference
		'''

	def thickness (self, _t: float) -> NutLambParams : 
		'''
		set the thickness.
		### Parameters:
		- _t (float): thickness
		### Returns:
		- (NutLambParams) NutLambParams reference
		'''

	def length (self) -> float : 
		'''
		get the length.
		### Returns:
		- (float) length value
		'''

	def diameterBottom (self) -> float : 
		'''
		get the bottom diameter.
		### Returns:
		- (float) bottom diameter
		'''

	def diameterTop (self) -> float : 
		'''
		get the top diameter.
		### Returns:
		- (float) top diameter
		'''

	def headHeight (self) -> float : 
		'''
		get the head height.
		### Returns:
		- (float) height value
		'''

	def thickness (self) -> float : 
		'''
		get the thickness.
		### Returns:
		- (float) thickness value
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the NutLambParams object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the NutLambParams object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an NutLambParams object.
		'''

class NutSlitsParams(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float): ...
	def width (self, w: float) -> NutSlitsParams : 
		'''
		set the width.
		### Parameters:
		- w (float): width value.
		### Returns:
		- (NutSlitsParams) NutSlitsParams reference
		'''

	def length (self, l: float) -> NutSlitsParams : 
		'''
		set the length.
		### Parameters:
		- l (float): length value.
		### Returns:
		- (NutSlitsParams) NutSlitsParams reference
		'''

	def count (self, n: int) -> NutSlitsParams : 
		'''
		set the count of NutSlitsParams.
		### Parameters:
		- n (int): count value.
		### Returns:
		- (NutSlitsParams) NutSlitsParams reference
		'''

	def width (self) -> float : 
		'''
		get the width.
		### Returns:
		- (float) width value.
		'''

	def length (self) -> float : 
		'''
		get the length.
		### Returns:
		- (float) length value.
		'''

	def count (self) -> int : 
		'''
		get the count of NutSlitsParams.
		### Returns:
		- (int) count value.
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the NutSlitsParams object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the NutSlitsParams object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an NutSlitsParams object.
		'''

class NutRimParams(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float): ...
	def inRingDiameter (self, _d: float) -> NutRimParams : 
		'''
		set the inner ring diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (NutRimParams) NutRimParams reference
		'''

	def outRingDiameter (self, _d: float) -> NutRimParams : 
		'''
		set the outer ring diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (NutRimParams) NutRimParams reference
		'''

	def inRingDiameter (self) -> float : 
		'''
		get the inner ring diameter.
		### Returns:
		- (float) inner diameter
		'''

	def outRingDiameter (self) -> float : 
		'''
		get the outer ring diameter.
		### Returns:
		- (float) outer diameter
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the NutRimParams object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the NutRimParams object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an NutRimParams object.
		'''

class NutClampLever(NutHeadBaseParams):
	def __init__(self): ...
	def __init__(self, d: float, h: float): ...
	def holderDiameter (self, _d: float) -> NutClampLever : 
		'''
		set the diameter of the holder.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (NutClampLever) NutClampLever reference
		'''

	def length (self, _l: float) -> NutClampLever : 
		'''
		set the length.
		### Parameters:
		- _l (float): length
		### Returns:
		- (NutClampLever) NutClampLever reference
		'''

	def holderDiameter (self) -> float : 
		'''
		get the diameter of the holder.
		### Returns:
		- (float) holder diameter
		'''

	def length (self) -> float : 
		'''
		get the length.
		### Returns:
		- (float) length value
		'''

	def copy (self, p: NutHeadBaseParams = NutHeadBaseParams.nullptr) -> NutHeadBaseParams : 
		'''
		copies the NutClampLever object.
		### Parameters:
		- p (NutHeadBaseParams): pointer to the NutClampLever object to copy. If the pointer equals to null then the object is duplicated
		### Returns:
		- (NutHeadBaseParams) the pointer to a copy of an NutClampLever object.
		'''

class nut(prim):
	def __init__(self): ...
	def __init__(self): ...
	def setTypeData (self, data: any) -> nut : 
		'''
		set the typed data.
		### Parameters:
		- data: pointer to the data
		### Returns:
		- (nut) nut reference
		'''

	def getTypeData (self) -> any : 
		'''
		get the typed data.
		### Returns:
		- (any) pointer to the data
		'''

	def threadDiameter (self, d: float) -> nut : 
		'''
		set the hole thread diameter.
		### Returns:
		- (nut) nut reference
		'''

	def threadDiameter (self) -> float : 
		'''
		get the hole thread diameter.
		### Returns:
		- (float) diameter
		'''

	def pitch (self, p: float) -> nut : 
		'''
		set the thread pitch.
		### Returns:
		- (nut) nut reference
		'''

	def pitch (self) -> float : 
		'''
		get the thread pitch.
		### Returns:
		- (float) pitch
		'''

	def enableThread (self, f: bool) -> nut : 
		'''
		set the enabled thread.
		### Returns:
		- (nut) nut reference
		'''

	def enableThread (self) -> bool : 
		'''
		get the enabled thread.
		### Returns:
		- (bool) enabled flag
		'''

	def threadType (self, _t: int) -> nut : 
		'''
		set the nut thread profile.
		### Parameters:
		- _t (int): profile type value (triangle,trapeze,rectangular,round,persistent)
		### Returns:
		- (nut) nut reference
		'''

	def threadType (self) -> int : 
		'''
		get the nut thread profile.
		### Returns:
		- (int) thread type value.
		'''

class bolt(prim):
	def __init__(self): ...
	def head (self, _h: boltHead) -> bolt : 
		'''
		set the head object.
		### Parameters:
		- _h (boltHead): head obj reference
		### Returns:
		- (bolt) bolt reference
		'''

	def head (self) -> boltHead : 
		'''
		get the head object.
		### Returns:
		- (boltHead) head obj reference
		'''

	def diameter (self, _d: float) -> bolt : 
		'''
		set the bolt diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (bolt) bolt reference
		'''

	def diameter (self) -> float : 
		'''
		get the bolt diameter.
		### Returns:
		- (float) diameter
		'''

	def pitch (self, _p: float) -> bolt : 
		'''
		set the thread pitch.
		### Parameters:
		- _p (float): pitch
		### Returns:
		- (bolt) bolt reference
		'''

	def pitch (self) -> float : 
		'''
		get the thread pitch.
		### Returns:
		- (float) pitch
		'''

	def threadHeight (self, _h: float) -> bolt : 
		'''
		set the thread height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (bolt) bolt reference
		'''

	def threadHeight (self) -> float : 
		'''
		get the thread height.
		### Returns:
		- (float) height value
		'''

	def length (self, _l: float) -> bolt : 
		'''
		set the bolt length.
		### Parameters:
		- _l (float): length
		### Returns:
		- (bolt) bolt reference
		'''

	def length (self) -> float : 
		'''
		get the bolt length.
		'''

	def threadLength (self, _l: float) -> bolt : 
		'''
		set the thread length.
		### Parameters:
		- _l (float): length
		### Returns:
		- (bolt) bolt reference
		'''

	def threadLength (self) -> float : 
		'''
		get the thread length.
		### Returns:
		- (float) length
		'''

	def threadType (self, _t: int) -> bolt : 
		'''
		set the screw thread profile.
		### Parameters:
		- _t (int): profile type value (triangle,trapeze,rectangular,round,persistent)
		### Returns:
		- (bolt) bolt reference
		'''

	def threadType (self) -> int : 
		'''
		get the screw thread profile.
		### Returns:
		- (int) thread type value.
		'''

	def underhead (self, _uh: int) -> bolt : 
		'''
		set the under head type.
		### Parameters:
		- _uh (int): type value (0-cylinder,1-rect)
		### Returns:
		- (bolt) bolt reference
		'''

	def underhead (self) -> int : 
		'''
		get the under head type.
		### Returns:
		- (int) under head type value
		'''

	def uwidth (self, _uw: int) -> bolt : 
		'''
		set the underhead width.
		### Parameters:
		- _uw (int): width
		### Returns:
		- (bolt) bolt reference
		'''

	def uwidth (self) -> float : 
		'''
		get the underhead width.
		### Returns:
		- (float) width value
		'''

	def uheight (self, _uh: int) -> bolt : 
		'''
		set the underhead height.
		### Parameters:
		- _uh (int): height
		### Returns:
		- (bolt) bolt reference
		'''

	def uheight (self) -> float : 
		'''
		get the underhead height.
		### Returns:
		- (float) height value
		'''

	def nutType (self, _t: int) -> bolt : 
		'''
		set the nut type.
		### Parameters:
		- _t (int): type value (see nut::Type enumarate)
		### Returns:
		- (bolt) bolt reference
		'''

	def nutType (self) -> int : 
		'''
		get the nut type.
		### Returns:
		- (int) type value
		'''

	def nutLocation (self, _loc: float) -> bolt : 
		'''
		set the nut location on the bolt.
		### Parameters:
		- _loc (float): location value
		### Returns:
		- (bolt) bolt reference
		'''

	def nutLocation (self) -> float : 
		'''
		get the nut location on the bolt.
		### Returns:
		- (float) location value
		'''

	def nutHeight (self, _h: float) -> bolt : 
		'''
		set the nut height on the bolt.
		### Parameters:
		- _h (float): height value
		### Returns:
		- (bolt) bolt reference
		'''

	def nutHeight (self) -> float : 
		'''
		get the nut height on the bolt.
		### Returns:
		- (float) location value
		'''

class screw(prim):
	def __init__(self): ...
	def head (self, _h: boltHead) -> screw : 
		'''
		set the bolt head object.
		### Parameters:
		- _h (boltHead): bolt head obj reference
		### Returns:
		- (screw) screw reference
		'''

	def head (self) -> boltHead : 
		'''
		get the bolt head object.
		### Returns:
		- (boltHead) bolt head obj reference
		'''

	def diameter (self, _d: float) -> screw : 
		'''
		set the screw diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (screw) screw reference
		'''

	def diameter (self) -> float : 
		'''
		get the screw diameter.
		### Returns:
		- (float) diameter
		'''

	def pitch (self, _p: float) -> screw : 
		'''
		set the screw thread step(pitch).
		### Parameters:
		- _p (float): step
		### Returns:
		- (screw) screw reference
		'''

	def pitch (self) -> float : 
		'''
		get the screw thread step(pitch).
		### Returns:
		- (float) step value
		'''

	def threadDiameter (self, _d: float) -> screw : 
		'''
		set the thread diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (screw) screw reference
		'''

	def threadDiameter (self) -> float : 
		'''
		get the thread diameter.
		### Returns:
		- (float) diameter
		'''

	def threadHeight (self, _h: float) -> screw : 
		'''
		set the screw thread height.
		### Parameters:
		- _h (float): height
		### Returns:
		- (screw) screw reference
		'''

	def threadHeight (self) -> float : 
		'''
		get the screw thread height.
		### Returns:
		- (float) thread height value
		'''

	def threadLength (self, _l: float) -> screw : 
		'''
		set the screw thread length.
		### Parameters:
		- _l (float): length
		### Returns:
		- (screw) screw reference
		'''

	def threadLength (self) -> float : 
		'''
		get the screw thread length.
		### Returns:
		- (float) length value
		'''

	def length (self, _l: float) -> screw : 
		'''
		set the screw length.
		### Parameters:
		- _l (float): length
		### Returns:
		- (screw) screw reference
		'''

	def length (self) -> float : 
		'''
		get the screw length.
		### Returns:
		- (float) length
		'''

	def underhead (self, _uh: int) -> screw : 
		'''
		set the underhead type.
		### Parameters:
		- _uh (int): type (0-cylinder,1-rect)
		### Returns:
		- (screw) screw reference
		'''

	def underhead (self) -> int : 
		'''
		get the underhead type.
		### Returns:
		- (int) type value
		'''

	def uwidth (self, _uw: int) -> screw : 
		'''
		set the underhead width.
		### Parameters:
		- _uw (int): width
		### Returns:
		- (screw) screw reference
		'''

	def uwidth (self) -> float : 
		'''
		get the underhead width.
		### Returns:
		- (float) width value
		'''

	def uheight (self, _uh: int) -> screw : 
		'''
		set the underhead height.
		### Parameters:
		- _uh (int): height
		### Returns:
		- (screw) screw reference
		'''

	def uheight (self) -> float : 
		'''
		get the underhead height.
		### Returns:
		- (float) height value
		'''

class washer(prim):
	def __init__(self): ...
	def innerDiameter (self, _d: float) -> washer : 
		'''
		set the inner diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (washer) washer reference
		'''

	def innerDiameter (self) -> float : 
		'''
		get the inner diameter.
		### Returns:
		- (float) diameter
		'''

	def outerDiameter (self, _d: float) -> washer : 
		'''
		set the outer diameter.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (washer) washer reference
		'''

	def outerDiameter (self) -> float : 
		'''
		get the outer diameter.
		### Returns:
		- (float) diameter
		'''

	def conusDiameter (self, _d: float) -> washer : 
		'''
		set the diameter of the conus washer.
		### Parameters:
		- _d (float): diameter
		### Returns:
		- (washer) washer reference
		'''

	def conusDiameter (self) -> float : 
		'''
		get the diameter of the conus washer.
		### Returns:
		- (float) diameter
		'''

	def thickness (self, _s: float) -> washer : 
		'''
		set the washer thickness.
		### Parameters:
		- _s (float): thickness value
		### Returns:
		- (washer) washer reference
		'''

	def thickness (self) -> float : 
		'''
		get the washer thickness.
		### Returns:
		- (float) thickness value
		'''

	def height (self, _h: float) -> washer : 
		'''
		set the washer height.
		### Parameters:
		- _h (float): height value
		### Returns:
		- (washer) washer reference
		'''

	def height (self) -> float : 
		'''
		get the washer height.
		### Returns:
		- (float) height value
		'''

	def facet (self, _f: bool) -> washer : 
		'''
		indicates the facet usage.
		### Parameters:
		- _f (bool): facet flag
		### Returns:
		- (washer) washer reference
		'''

	def facet (self) -> bool : 
		'''
		get the facet flag.
		### Returns:
		- (bool) facet flag value
		'''

	def type (self, _t: any) -> washer : 
		'''
		set the washer type.
		### Parameters:
		- _t: type value
		### Returns:
		- (washer) washer reference
		'''

	def type (self) -> any : 
		'''
		get the washer type.
		### Returns:
		- (any) type value
		'''

class freeform(prim):
	def __init__(self): ...
	def __init__(self, _ffname: str, _ffsubname: str): ...
	def __init__(self): ...
	def symx (self, x: bool) -> freeform : 
		'''
		Enable the XYZ-mirror symmetry
		### Parameters:
		- x (bool): true to enable x-symmetry, false to disable
		### Returns:
		- (freeform) freeform reference
		'''

	def symy (self, y: bool) -> freeform : 
		'''
		Enable the XYZ-mirror symmetry
		### Parameters:
		- y (bool): true to enable y-symmetry, false to disable
		### Returns:
		- (freeform) freeform reference
		'''

	def symz (self, z: bool) -> freeform : 
		'''
		Enable the XYZ-mirror symmetry
		### Parameters:
		- z (bool): true to enable z-symmetry, false to disable
		### Returns:
		- (freeform) freeform reference
		'''

	def size (self, x: float, y: float, z: float) -> freeform : 
		'''
		set the free form size
		### Parameters:
		- x (float): size in the x - axis
		- y (float): size in the y - axis
		- z (float): size in the z - axis
		### Returns:
		- (freeform) freeform reference
		'''

	def size (self, v: vec3) -> freeform : 
		'''
		set the free form size
		### Parameters:
		- v (vec3): vector size
		### Returns:
		- (freeform) freeform reference
		'''

	def ffname (self, name: str) -> freeform : 
		'''
		set the free form name.
		
		set of names {"Cube","Patch,"Blob","Round","Ring",Torus","Tube2","Tube3","Disc","Cylinder"}
		### Parameters:
		- name (str): the name string
		### Returns:
		- (freeform) the freeform reference
		'''

	def ffname (self) -> str : 
		'''
		get the free form name.
		### Returns:
		- (str) the name
		'''

	def ffsubname (self, name: str) -> freeform : 
		'''
		set the free form sub name.
		### Parameters:
		- name (str): the name string
		### Returns:
		- (freeform) the freeform reference
		'''

	def ffsubname (self) -> str : 
		'''
		get the free form sub name.
		### Returns:
		- (str) the name
		'''

	def SetPoint (self, i: int, point: vec3) -> freeform : 
		'''
		set the knot point of the primitive.
		### Parameters:
		- i (int): point index
		- point (vec3): the coordinates of the point
		### Returns:
		- (freeform) the freeform reference
		'''

	def CountPoints (self) -> int : 
		'''
		get the account of the knot points
		### Returns:
		- (int) count of points
		'''

	def ResetPoints (self) : 
		'''
		reset the knot points
		'''

	def objsList (self) -> any : 
		'''
		gets the object's list.
		### Returns:
		- (any) objs list reference
		'''

	def ffControlPoints (self) -> any : 
		'''
		get the knot(control) points of the primitive.
		### Returns:
		- (any) the points reference
		'''

class cExtension:
	def __init__(self): ...
	def __init__(self): ...
	extensionHandler: any
	@staticmethod
	def Message (extension_name: str, message: str) -> bool : ...
	def onStop (self) : ...
	def onStart (self) : ...
	def onRestart (self) : ...
	def onMessage (self, message: str) : 
		'''
		Call if another module sent message to this extension using cExtension.Message
		'''

	def onStartup (self) : 
		'''
		Call on startup, right before tools initialisation.
		'''

	def afterInit (self) : 
		'''
		Call it after tools, graphics and shaders initialisation.
		'''

	def preprocess (self) : 
		'''
		Call it once per frame, before tools processing.
		'''

	def prerender (self) : 
		'''
		Call it once per frame, before the rendering stage.
		'''

	def postprocess (self) : 
		'''
		Call it once per frame, after tools processing.
		'''

	def postrender (self) : 
		'''
		Call it once per frame, after the rendering stage.
		'''

	def afterUI (self) : 
		'''
		Call it once per frame, after the ui rendering, before the topmost elements
		'''

	def thumbnail (self) : 
		'''
		Call it once per frame to draw thumbnails.
		'''

	def afterSettings (self) : 
		'''
		Call it once after settings loading.
		'''

	def onNew (self) : 
		'''
		Call it as soon as user starts new scene.
		'''

	def onKey (self) : 
		'''
		Call it as soon as user pressed the key, get the key value from Widgets::lastKey. Set it to 0 if the key captured and des not need to be propagated anymore.
		'''

	def onDropFile (self) : 
		'''
		Call if file dropped using drag&drop, filename is in Widgets::LastDroppedFile. Set it empty if you acquired the file.
		'''

	def onChangeTool (self) : 
		'''
		called when the current tool changes
		'''

	def onChangeRoom (self) : 
		'''
		called when the current room changes
		'''

	def onUndo (self) : 
		'''
		called when the undo triggered
		'''

	def onRedo (self) : 
		'''
		called when the redo triggered
		'''

	def onSaveScene (self) : 
		'''
		called before the saving the scene
		'''

	def onExit (self) : 
		'''
		called before the exit
		'''

	@staticmethod
	def begin_work_in_bg () -> int : ...
	@staticmethod
	def end_work_in_bg () -> int : ...
