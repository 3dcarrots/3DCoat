from __future__ import annotations
import cPy.cTypes
import cPy.cCore
#CoreAPI
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class BoolOpType(Enum):
	'''
			
		Boolean operations type
		
	'''
	BOOL_MERGE = Coat_CPP.BoolOpType.BOOL_MERGE.value
	BOOL_ADD = Coat_CPP.BoolOpType.BOOL_ADD.value
	BOOL_SUBTRACT = Coat_CPP.BoolOpType.BOOL_SUBTRACT.value
	BOOL_INTERSECT = Coat_CPP.BoolOpType.BOOL_INTERSECT.value

def start_main_menu(id: str):
		'''
			
	strat the main menu root items, this command may be called only from the menu making script

	Args:
		id (str): the menu id, see examples in the `UserPrefs/Rooms/menu.py` or `cpp`
	
		'''
		pass # cpp source

def menu_item(id: str):
		'''
			
	add the item to the menu, this command may be called only from the menu making script

	Args:
		id (str): the item id, see examples in the `UserPrefs/Rooms/menu.py` or `cpp`. If you want to trigger some script by this menu item
	you may use '$execute:path/to/your/script.py' as the id.
	
		'''
		pass # cpp source

def menu_info(id: str):
		'''
			
	add the information item to the menu (without any action, just message), this command may be called only from the menu making script

	Args:
		id (str): the item text identifier
	
		'''
		pass # cpp source

def menu_submenu(id: str):
		'''
			
	add the submenu to the current menu, this command may be called only from the menu making script

	Args:
		id (str): the submenu id/text

	Returns:
		always True, just for structuring the script
	
		'''
		pass # cpp source

def menu_exit():
		'''
			
	finish the current submenu, this command may be called only from the menu making script
	
		'''
		pass # cpp source

def menu_separator():
		'''
			
	add the separator to the current menu, this command may be called only from the menu making script
	
		'''
		pass # cpp source

def menu_hotkey(id: str, Shift: int, Ctrl: int, Alt: int):
		'''
			
	set the hotkey for the menu item, this command may be called only from the menu making script

	Args:
		id (str): the item id, see examples in the `UserPrefs/Rooms/menu.py` or `cpp`
		Shift (int): set true if Shift should be pressed
		Ctrl (int): set true if Ctrl should be pressed
		Alt (int): set true if Alt should be pressed
	
		'''
		pass # cpp source

def menu_no_hotkey(id: str, Shift: int, Ctrl: int, Alt: int):
		'''
			
	Don't allow this hotkey for this action
	
		'''
		pass # cpp source

def iconic_submenu(id: str, size: int):
		'''
			
	start the menu that will be shown on the icon click, like the navigation menu

	Args:
		id (str): the text identifier
		size (int): the size of the icon

	Returns:
		always True to structure the script
	
		'''
		pass # cpp source

def is_new_scene():
		'''
			
	is the scene new/empty?

	Returns:
		True if empty
	
		'''
		pass # cpp source

def is_steam_app():
		'''
			
	is it steam app?

	Returns:
		True if it is
	
		'''
		pass # cpp source

def is_medical():
		'''
			
	check if the app is medical

	Returns:
		True if it is
	
		'''
		pass # cpp source

def is_ppp():
		'''
			
	chack if there are any ppp objects in scene

	Returns:
		True if there are
	
		'''
		pass # cpp source

def is_proxy():
		'''
			
	check if current sculpt object is in proxy mode

	Returns:
		True if it is
	
		'''
		pass # cpp source

def is_multires():
		'''
			
	check if the current sculpt object is on some multiresolution level

	Returns:
		True if it is
	
		'''
		pass # cpp source

def is_surface():
		'''
			
	check if the current sculpt object is in surface mode

	Returns:
		True if it is
	
		'''
		pass # cpp source

def IsInRoom(name: str):
		'''
			
	check if you are in some room

	Args:
		name (str): the room name

	Returns:
		True if you are in that room
	
		'''
		pass # cpp source

def RoomExists(name: str):
		'''
			
	check if the room exists

	Args:
		name (str): the room name/identifier

	Returns:
		True if the room exists
	
		'''
		pass # cpp source

def CheckIfExists(path: str):
		'''
			
	check if the file exists

	Args:
		path (str): the file path, full or relative to Coat's documents

	Returns:
		True if exists
	
		'''
		pass # cpp source

def UseRecordScript():
		'''
			
	check is scripts recording available

	Returns:
		True if available
	
		'''
		pass # cpp source

def is_mv():
		'''
			
	check if mv objects available in scene

	Returns:
		True if available
	
		'''
		pass # cpp source

def is_ptex():
		'''
			
	check if ptex is used in the current scene

	Returns:
		True if used
	
		'''
		pass # cpp source

def show_rmb_panel():
		'''
			
	show the rmb panel
	
		'''
		pass # cpp source

def show_space_panel(Subset: str, NumColumns: int):
		'''
			
	show the space panel (with limitations if need)

	Args:
		Subset (str): the subset, if need
		NumColumns (int): amount of columns
	
		'''
		pass # cpp source

def gltf_support():
		'''
			
	gltf export supported

	Returns:
		True if supported
	
		'''
		pass # cpp source

def tex_approach():
		'''
			
	returns the texturing approach index (from the Textures menu)

	Returns:
		the index
	
		'''
		pass # cpp source

def menu_insert_extensions(id: str):
		'''
			
	insert extension into the main menu (may be called only from the menu making script)

	Args:
		id (str): the extension id
	
		'''
		pass # cpp source

def extensions_main_menu():
		'''
			
	insert extension menu into the main menu
	
		'''
		pass # cpp source

def insert_extensions():
		'''
			
	insert extensions into the toolset (may be used only from the toolset.py)
	
		'''
		pass # cpp source

def set_space_panel_columns_count(num: int):
		'''
			
	set the space panel columns count (only for the toolset.py)

	Args:
		num (int): amount of columns
	
		'''
		pass # cpp source

def SetAutoSnapDefaults(value: bool):
		'''
			
	set the default value for auto-snapping, usually for the retopo/modeling rooms (in toolset.py)

	Args:
		value (bool): the default value
	
		'''
		pass # cpp source

def menu_property(id: str):
		'''
			
	returns boolean property value

	Args:
		id (str): the property id, available values: RMBObjectInCache, RMBObjectIsSurface, ObjectHasNodes, IsCurvePrimitive, IsCurveClosed, OverSculptObject

	Returns:
		the property value
	
		'''
		pass # cpp source

def tools_section(id: str):
		'''
			
	start the tools section in the toolset.py

	Args:
		id (str): the section id
	
		'''
		pass # cpp source

def tools_item(id: str):
		'''
			
	add the item to the tools section (toolset.py)

	Args:
		id (str): the tool identifier
	
		'''
		pass # cpp source

def page_suffix(suffix: str):
		'''
			
	set the additional suffix for the page in the toolset.py

	Args:
		suffix (str): usually "S" or "V"
	
		'''
		pass # cpp source

def default_tool(tool: str):
		'''
			
	set the default tool for the toolset.py

	Args:
		tool (str): the tool identifier
	
		'''
		pass # cpp source

def IsDebug():
		'''
			
	is Debug mode (for developers only)

	Returns:
		True if debug
	
		'''
		pass # cpp source

def start_rmb_panel():
		'''
			
	start the RNB panel. This command may be called only from the RMB response making script (curves.py, rmb.py)
	
		'''
		pass # cpp source

def menu_sort():
		'''
			
	sort items in the current menu
	
		'''
		pass # cpp source

def IsRecordScript():
		'''
			
	is the script recording enabled?

	Returns:
		True if enabled
	
		'''
		pass # cpp source

def IsInTool(ToolID: str):
		'''
			
	check if we are in some tool

	Args:
		ToolID (str): the tool identifier

	Returns:
		True if in that tool
	
		'''
		pass # cpp source

def voxtree_item_picked():
		'''
			
	check if the VoxTree item is picked

	Returns:
		true if picked
	
		'''
		pass # cpp source

def retopo_object_picked():
		'''
			
	the retopo object is picked

	Returns:
		True if picked
	
		'''
		pass # cpp source

def empty_space_picked():
		'''
			
	check if no object is picked

	Returns:
		True if no object is picked
	
		'''
		pass # cpp source

def voxtree_object_picked():
		'''
			
	check if the sculpt object is picked in the viewport

	Returns:
		True if picked
	
		'''
		pass # cpp source

def GetCurrentToolSubmode(id: str):
		'''
			
	get the current tool submode (usually for the uv/retopo tools)

	Args:
		id (str): the submode identifier

	Returns:
		the value
	
		'''
		pass # cpp source

def tools_comment(id: str):
		'''
			
	comment in toolset.py for auto-documentation (legacy)

	Args:
		id (str): the text of the comment
	
		'''
		pass # cpp source

def doc_mode():
		'''
			
	check if script is in auto-documenting mode (legacy)

	Returns:
		the state
	
		'''
		pass # cpp source

def PureIconic():
		'''
			
	enable the radial menu mode for the space panel
	
		'''
		pass # cpp source

def lock_ui_changes():
		'''
			
	check if UI changes locked (for specialized applications, like printing)

	Returns:
		the lock state
	
		'''
		pass # cpp source

def ue5_support():
		'''
			
	returns if ue5 support enabled

	Returns:
		True if enabled
	
		'''
		pass # cpp source

def run_extension(extension_name: str, auto_start: bool =  False):
		'''
			
	run extension
	
		'''
		pass # cpp source


class ClusterScale(Enum):
	'''
			
		the parameters to be used for cluster scaling in Model, scaleSelectedFacesClusters
		
	'''
	Uniform_Scaling = Coat_CPP.ClusterScale.Uniform_Scaling.value
	Axial_Normal = Coat_CPP.ClusterScale.Axial_Normal.value
	Axial_X = Coat_CPP.ClusterScale.Axial_X.value
	Axial_Y = Coat_CPP.ClusterScale.Axial_Y.value
	Axial_Z = Coat_CPP.ClusterScale.Axial_Z.value
	Radial_Normal = Coat_CPP.ClusterScale.Radial_Normal.value
	Radial_X = Coat_CPP.ClusterScale.Radial_X.value
	Radial_Y = Coat_CPP.ClusterScale.Radial_Y.value
	Radial_Z = Coat_CPP.ClusterScale.Radial_Z.value


class Mesh():
	'''
			
		The mesh reference
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def __init__(self, m: Mesh):
		pass # CPP source

	def __init__(self, m: any):
		pass # CPP source

	def __assign__(self, m: Mesh) -> Mesh:
		return super().__assign__(m)

	def __assign__(self, m: any) -> Mesh:
		return super().__assign__(m)

	def MakeCopy(self) -> Mesh:
		pass # cpp source

	def Read(self, name: str) -> bool:
		'''
			
		Load the mesh from the file.

		Args:
			name (str): the filename. May contain full path or relative to the coat's install or documents folder.

		Returns:
			bool: true if successful.
		
		'''
		pass # cpp source

	def Write(self, name: str) -> bool:
		'''
			
		Save the mesh to file

		Args:
			name (str): Full or relative path

		Returns:
			bool: true if successful
		
		'''
		pass # cpp source

	def valid(self) -> bool:
		'''
			
		Check if mesh is valid

		Returns:
			bool: true if mesh is valid
		
		'''
		pass # cpp source

	def clear(self):
		'''
			
		clear the mesh
		
		'''
		pass # cpp source

	def __iadd__(self, m: Mesh) -> Mesh:
		return super().__iadd__(m)

	def __iadd__(self, m: any) -> Mesh:
		return super().__iadd__(m)

	def addTransformed(self, m: Mesh, t: any):
		'''
			
		concatenate the transformed mesh with the current one

		Args:
			m (Mesh): the mesh
			t : the transform
		
		'''
		pass # cpp source

	def boolean(self, m: Mesh, op: BoolOpType):
		'''
			
		boolean operation

		Args:
			m (Mesh): the mesh to operate
		
		'''
		pass # cpp source

	def transform(self, transform: any):
		'''
			
		transform the mesh

		Args:
			transform : the transformation matrix
		
		'''
		pass # cpp source

	def rotateToXYAxis(self, axisX: any, axisY: any):
		'''
			
		rotate the mesh so that X axis will be aligned with axisX, Y axis will be aligned with axisY

		Args:
			axisX : the new X axis
			axisY : the new Y axis
		
		'''
		pass # cpp source

	def rotateToYZAxis(self, axisY: any, axisZ: any):
		'''
			
		rotate the mesh so that Y axis will be aligned with axisY, Z axis will be aligned with axisZ

		Args:
			axisY : the new Y axis
			axisZ : the new Z axis
		
		'''
		pass # cpp source

	def rotateToZXAxis(self, axisZ: any, axisX: any):
		'''
			
		rotate the mesh so that Z axis will be aligned with axisZ, X axis will be aligned with axisX

		Args:
			axisZ : the new Z axis
			axisX : the new X axis
		
		'''
		pass # cpp source

	def vertsCount(self) -> int:
		'''
			
		returns the amount of verts in the mesh

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	def vertsUvCount(self) -> int:
		'''
			
		returns the amount of UV - verts in the mesh

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	def vertsNormalCount(self) -> int:
		'''
			
		returns the amount of normal - verts in the mesh

		Returns:
			int: teh amount
		
		'''
		pass # cpp source

	def facesCount(self) -> int:
		'''
			
		returns the faces amount

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	def getVertex(self, idx: int) -> any:
		'''
			
		get the vertex coordinate

		Args:
			idx (int): the vertex index

		Returns:
			any: the coordinate
		
		'''
		pass # cpp source

	def setVertex(self, idx: int, v: any):
		'''
			
		set the vertex coordinate

		Args:
			idx (int): the vertex index
			v : the coordinate
		
		'''
		pass # cpp source

	def createNewVertex(self, position: any) -> int:
		'''
			
		create the positional vertex

		Args:
			position : the position

		Returns:
			int: the positional vertex index
		
		'''
		pass # cpp source

	def getVertexUV(self, idx: int) -> any:
		'''
			
		get the UV coordinate of the vertex, pay attention position verts and UV verts are different, they have different indices

		Args:
			idx (int): the UV vertex index, [0..vertsUvCount() - 1]

		Returns:
			any: the UV coordinate
		
		'''
		pass # cpp source

	def setVertexUV(self, idx: int, v: any):
		'''
			
		set the UV coordinate of the vertex, pay attention position verts and UV verts are different, they have different indices

		Args:
			idx (int): the UV vrertex index, [0..vertsUvCount() - 1]
			v : the UV coordinate
		
		'''
		pass # cpp source

	def createNewUvVertex(self, uv: any) -> int:
		'''
			
		create new UV vertex to be used for faces

		Args:
			uv : the texture coordinates

		Returns:
			int: the index
		
		'''
		pass # cpp source

	def getVertexNormal(self, idx: int) -> any:
		'''
			
		get the normal of the vertex, pay attention position verts and normal verts are different, they have different indices

		Args:
			idx (int): the normal vertex index, [0..vertsNormalCount() - 1]

		Returns:
			any: the normal
		
		'''
		pass # cpp source

	def setVertexNormal(self, idx: int, v: any):
		'''
			
		set the normal of the vertex, pay attention position verts and normal verts are different, they have different indices

		Args:
			idx (int): the normal vertex index, [0..vertsNormalCount() - 1]
			v : the normal
		
		'''
		pass # cpp source

	def calcNormals(self):
		'''
			
		re-calculate normals over the mesh
		
		'''
		pass # cpp source

	def calcNormalsIgnoreSharpEdges(self):
		'''
			
		re-calculate normals over the mesh, ignore the sharp edges
		
		'''
		pass # cpp source

	def getFaceVertsCount(self, face: int) -> int:
		'''
			
		get the amount of vertices over the face

		Args:
			face (int): the face index, should be in [0..facesCount() - 1]

		Returns:
			int: the verts amount
		
		'''
		pass # cpp source

	def getFaceUvVertsCount(self, face: int) -> int:
		'''
			
		get the amount of UV vertices over the face

		Args:
			face (int): the face index

		Returns:
			int: amount of vertices over the face, 0 if UV-s not assigned
		
		'''
		pass # cpp source

	def getFaceVertex(self, faceIndex: int, faceVertexIndex: int) -> int:
		'''
			
		get the positional vertex index over the face

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]
			faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]

		Returns:
			int: the positional vertex index
		
		'''
		pass # cpp source

	def getFaceVerts(self, face: int) -> list[int]:
		'''
			
		get the list of UV vertex indices over the face, pay attention UV vertices are not same as position vertices

		Args:
			face (int): the face index

		Returns:
			list[int]: the list of vertex indices
		
		'''
		pass # cpp source

	def setFaceVerts(self, face: int, vertices: list[int]):
		'''
			
		set the list of positional vertex indices over the face

		Args:
			face (int): the face index
			vertices (list[int]): the list of vertex indices
		
		'''
		pass # cpp source

	def getFaceUvVertex(self, faceIndex: int, faceVertexIndex: int) -> int:
		'''
			
		get the UV vertex index over the face

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]
			faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]

		Returns:
			int: the UV vertex index, -1 if no UVs over the face
		
		'''
		pass # cpp source

	def setFaceUvVertex(self, faceIndex: int, faceVertexIndex: int, uvVertexIndex: int):
		'''
			
		set the UV vertex index over the face

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]
			faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]
			uvVertexIndex (int): the UV vertex index, should be in [0..vertsUvCount() - 1]
		
		'''
		pass # cpp source

	def getFaceNormalVertex(self, faceIndex: int, faceVertexIndex: int) -> int:
		'''
			
		get the normal vertex index over the face

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]
			faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]

		Returns:
			int: the normal vertex index, -1 if no normals over the face
		
		'''
		pass # cpp source

	def setFaceNormalVertex(self, faceIndex: int, faceVertexIndex: int, normalVertexIndex: int):
		'''
			
		set the normal vertex index over the face

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]
			faceVertexIndex (int): the index of the vertex within the face, should be in [0..getFaceVertsCount(faceIndex) - 1]
			normalVertexIndex (int): the normal vertex index, should be in [0..vertsNormalCount() - 1]
		
		'''
		pass # cpp source

	def getFaceUvVerts(self, face: int) -> list[int]:
		'''
			
		get the list of UV vertices indices over the face

		Args:
			face (int): the face index

		Returns:
			list[int]: the list of UV vertices indices
		
		'''
		pass # cpp source

	def getFaceObject(self, faceIndex: int) -> int:
		'''
			
		get the object index over the face, see the getObjectsCount(), getObjectName()

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]

		Returns:
			int: the object index
		
		'''
		pass # cpp source

	def setFaceObject(self, faceIndex: int, objectIndex: int):
		'''
			
		set the object index for the face, see the getObjectsCount(), getObjectName()

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]
			objectIndex (int): the object index to set for the face
		
		'''
		pass # cpp source

	def getFaceMaterial(self, faceIndex: int) -> int:
		'''
			
		get the material index over the face, see the getMaterialsCount(), getMaterialName()

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]

		Returns:
			int: the material index
		
		'''
		pass # cpp source

	def setFaceMaterial(self, faceIndex: int, materialIndex: int):
		'''
			
		set the material index over the face, see the getMaterialsCount(), getMaterialName()

		Args:
			faceIndex (int): the face index, should be in [0..facesCount() - 1]
			materialIndex (int): the material index to set for the face
		
		'''
		pass # cpp source

	def getObjectsCount(self) -> int:
		'''
			
		returns the objects count in the mesh

		Returns:
			int: the count
		
		'''
		pass # cpp source

	def getObjectName(self, idx: int) -> str:
		'''
			
		get the name of the object

		Args:
			idx (int): the object index

		Returns:
			str: the name
		
		'''
		pass # cpp source

	def setObjectName(self, idx: int, name: str):
		'''
			
		set object name

		Args:
			idx (int): the object index
			name (str): the new name
		
		'''
		pass # cpp source

	def addObject(self, name: str) -> int:
		'''
			
		add new object to the mesh

		Args:
			name (str): the object name

		Returns:
			int: the object index
		
		'''
		pass # cpp source

	def removeObject(self, idx: int):
		'''
			
		remove object from the mesh

		Args:
			idx (int): the object index
		
		'''
		pass # cpp source

	def unifyAllObjects(self, name: str = ""):
		'''
			
		unify all objects in the mesh, i.e. make one object

		Args:
			name (str): the name of the new object, if empty, the name of the first object will be used
		
		'''
		pass # cpp source

	def getMaterialsCount(self) -> int:
		'''
			
		get the materials count in the mesh

		Returns:
			int: the count
		
		'''
		pass # cpp source

	def addMaterial(self, name: str) -> int:
		'''
			
		add new material to the mesh

		Args:
			name (str): the material name

		Returns:
			int: the material index
		
		'''
		pass # cpp source

	def removeMaterial(self, idx: int):
		'''
			
		remove the material (and corresponding faces) from the mesh

		Args:
			idx (int): the material index
		
		'''
		pass # cpp source

	def getMaterialName(self, idx: int) -> str:
		'''
			
		get the name of the material

		Args:
			idx (int): the material index

		Returns:
			str: the name
		
		'''
		pass # cpp source

	def setMaterialName(self, idx: int, name: str):
		'''
			
		set material name

		Args:
			idx (int): the material index
			name (str): the new name
		
		'''
		pass # cpp source

	def getMaterialTexture(self, idx: int, texture_layer: int) -> str:
		'''
			
		get the texture name of the material

		Args:
			idx (int): the material index
			texture_layer (int): the texture layer, 0 - color, 1 - gloss, 2 - bump/displacement, 3 - normalmap, 4 - specular color, 5 - emossive (color), 6 - emissive power

		Returns:
			str: the texture path (full or relative to 3DCoat documents folder)
		
		'''
		pass # cpp source

	def setMaterialTexture(self, idx: int, texture_layer: int, texture_path: str):
		'''
			
		set the texture layer filename of the material

		Args:
			idx (int): the material index
			texture_layer (int): the texture layer, 0 - color, 1 - gloss, 2 - bump/displacement, 3 - normalmap, 4 - specular color, 5 - emossive (color), 6 - emissive power
			texture_path (str): the texture path (full or relative to 3DCoat documents folder)
		
		'''
		pass # cpp source

	def fromVolume(self, v: any, with_subtree: bool = False, all_selected: bool = False):
		'''
			
		extract the mesh from the volume

		Args:
			v : the source volume
			with_subtree (bool): if true, the subtree will be extracted, otherwise the single volume taken
			all_selected (bool): if true, all selected volumes will be extracted, otherwise only the current volume
		
		'''
		pass # cpp source

	def fromReducedVolume(self, v: any, reduction_percent: float, with_subtree: bool = False, all_selected: bool = False):
		'''
			
		extract the mesh from the volume and reduce it by the given percent

		Args:
			v : the source volume
			reduction_percent (float): 0 means no reduction, 100 means 100% reduction, i.e. the mesh will be reduced to a single triangle
			with_subtree (bool): if true, the subtree will be extracted, otherwise the single volume taken
			all_selected (bool): if true, all selected volumes will be extracted, otherwise only the current volume
		
		'''
		pass # cpp source

	def fromVolumeWithMaxPolycount(self, v: any, max_polycount: int, with_subtree: bool = False, all_selected: bool = False):
		'''
			
		extract the mesh from the volume and reduce to the given polycount

		Args:
			v : the source volume
			max_polycount (int): the required polycount
			with_subtree (bool): if true, the subtree will be extracted, otherwise the single volume taken
			all_selected (bool): if true, all selected volumes will be extracted, otherwise only the current volume
		
		'''
		pass # cpp source

	def toVolume(self, v: any, transform: any = 4, op: BoolOpType = Coat_CPP.BoolOpType.BOOL_MERGE):
		'''
			
		merge this mesh to the volume object

		Args:
			v : the destination volume
			transform : the applied transformation
			op (BoolOpType): the boolean operation to be performed, -1 means no operation, raw merge, 0 - 1, 1 - subtract, 2 - intersect
		
		'''
		pass # cpp source

	def insertInVolume(self, v: any, transform: any = 4):
		'''
			
		insert without boolean operation, if the volume is not in surface mode (volumetric) the boolean ADD will be performed anyway

		Args:
			v : the destination volume
			transform : the transform
		
		'''
		pass # cpp source

	def addToVolume(self, v: any, transform: any = 4):
		'''
			
		boolean add to volume

		Args:
			v : the destination volume
			transform : the transform
		
		'''
		pass # cpp source

	def subtractFromVolume(self, v: any, transform: any = 4):
		'''
			
		boolean subtraction of the mesh from the volume

		Args:
			v : the destination volume
			transform : the transform
		
		'''
		pass # cpp source

	def intersectWithVolume(self, v: any, transform: any = 4):
		'''
			
		boolean intersection of the mesh with the volume

		Args:
			v : the destination volume
			transform : the transform
		
		'''
		pass # cpp source

	def fromRetopo(self):
		'''
			
		take the whole mesh from the retopo room
		
		'''
		pass # cpp source

	def fromPaintRoom(self):
		'''
			
		get the mesh from the paint room
		
		'''
		pass # cpp source

	def reduceToPolycount(self, destination_triangles_count: int):
		'''
			
		reduce the mesh to the given polycount, mesh will be triangulated

		Args:
			destination_triangles_count (int): the required triangles count, if it is above the existing, nothing happens
		
		'''
		pass # cpp source

	def triangulate(self):
		'''
			
		triangulate the mesh
		
		'''
		pass # cpp source

	def booleanOp(self, With: Mesh, op: BoolOpType):
		'''
			
		Perform the boolean operation with the given mesh

		Args:
			With (Mesh): the mesh to perform the operation with over the current mesh
			op (BoolOpType): the operation, see BoolOpType (-1 means no operation, 0 - add, 1 - subtract, 2 - intersect)
		
		'''
		pass # cpp source

	def getMeshVertices(self) -> list[vec3]:
		'''
			
		get the list of all positional vertices of the mesh

		Returns:
			list[vec3]: the list of vec3
		
		'''
		pass # cpp source

	def getMeshNormals(self) -> list[vec3]:
		'''
			
		get the list of all normal vertices of the mesh

		Returns:
			list[vec3]: the list of vec3
		
		'''
		pass # cpp source

	def getMeshUVs(self) -> list[vec2]:
		'''
			
		get the list of all UV vertices of the mesh

		Returns:
			list[vec2]: the list of vec2
		
		'''
		pass # cpp source

	def setMeshVertices(self, positions: list[vec3]):
		'''
			
		set the list of all positional vertices for the mesh

		Args:
			positions (list[vec3]): the list of positions
		
		'''
		pass # cpp source

	def setMeshNormals(self, normals: list[vec3]):
		'''
			
		set the list of all normal vertices for the mesh

		Args:
			normals (list[vec3]): the list of normals (vec3)
		
		'''
		pass # cpp source

	def setMeshUVs(self, uvs: list[vec2]):
		'''
			
		set the list of all UV vertices for the mesh

		Args:
			uvs (list[vec2]): the list of UVs (vec2)
		
		'''
		pass # cpp source

	def setMeshFaces(self, faces: list[int]):
		'''
			
		set the complete list of faces for the mesh

		Args:
			faces (list[int]): the format of faces is:\n
		amount_ot_vets_in_face1, vertex1_face1, vertex2_face1...vertexN-1_face1,\n
		amount_ot_vets_in_face2, vertex1_face2, vertex2_face2...\n
		...
		
		'''
		pass # cpp source

	def addMeshVertices(self, positions: list[vec3]):
		'''
			
		add the list of all positional vertices for the mesh

		Args:
			positions (list[vec3]): the list of positions
		
		'''
		pass # cpp source

	def addMeshNormals(self, normals: list[vec3]):
		'''
			
		add the list of all normal vertices for the mesh

		Args:
			normals (list[vec3]): the list of normals (vec3)
		
		'''
		pass # cpp source

	def addMeshUVs(self, uvs: list[vec2]):
		'''
			
		add the list of all UV vertices for the mesh

		Args:
			uvs (list[vec2]): the list of UVs (vec2)
		
		'''
		pass # cpp source

	def addMeshFaces(self, faces: list[int]):
		'''
			
		add the list of faces for the mesh, pay attention, all vertex indices are global over the whole mesh!

		Args:
			faces (list[int]): the format of faces is:\n
		amount_ot_vets_in_face1, vertex1_face1, vertex2_face1...vertexN-1_face1,\n
		amount_ot_vets_in_face2, vertex1_face2, vertex2_face2...\n
		...
		
		'''
		pass # cpp source

	def clearVerts(self):
		'''
			
		clear all positional vertices of the mesh
		
		'''
		pass # cpp source

	def clearUvVerts(self):
		'''
			
		clear all uv vertices of the mesh
		
		'''
		pass # cpp source

	def clearNormals(self):
		'''
			
		clear all normal vertices of the mesh
		
		'''
		pass # cpp source

	def clearFaces(self):
		'''
			
		clear all faces of the mesh
		
		'''
		pass # cpp source

	def removeFaces(self, faces: list[int]):
		'''
			
		remove the set of vertices from the mesh

		Args:
			faces (list[int]): the list of faces indices to remove
		
		'''
		pass # cpp source

	def clearObject(self):
		'''
			
		clear all objects
		
		'''
		pass # cpp source

	def clearMaterials(self):
		'''
			
		clear all materials
		
		'''
		pass # cpp source

	def ensureMaterialsAndObjectsExist(self):
		'''
			
		ensure that at least one material and one object exist in the mesh
		
		'''
		pass # cpp source

	def addObject(self, name: str) -> int:
		'''
			
		add the named object

		Args:
			name (str): the name for the object

		Returns:
			int: the index of new object in the objects list
		
		'''
		pass # cpp source

	def addMaterial(self, name: str) -> int:
		'''
			
		add the named material

		Args:
			name (str): the name for the material

		Returns:
			int: the index of new material in the materials list
		
		'''
		pass # cpp source

	def removeUnusedObjectsAndMaterials(self):
		'''
			
		remove all unused objects and materials
		
		'''
		pass # cpp source

	def removeUnusedVerts(self):
		'''
			
		remove all unused vertices
		
		'''
		pass # cpp source

	def removeUnusedFaces(self):
		'''
			
		remove all faces that contain zero vertices
		
		'''
		pass # cpp source

	def cutByPlane(self, start: any, NormalDirection: any):
		'''
			
		Cut off the mesh by the plane, the result is stored in the current mesh, the part of the mesh that is on the side of the negative normal direction is removed

		Args:
			start : the start point of the plane
			NormalDirection : the normal direction of the plane
		
		'''
		pass # cpp source

	def cutByDistortedPlane(self, start: any, NormalDirection: any, noise_degree: float, noise_scale: float, seed: int = 0):
		'''
			
		Cut off the mesh by the distorted plane (using the Perlin noise), the result is stored in the current mesh, the part of the mesh that is on the side of the negative normal direction is removed

		Args:
			start : the start point of the plane
			NormalDirection : the normal direction of the plane
			noise_degree (float): the degree of the noise
			noise_scale (float): the scale of the noise
			seed (int): the seed for the noise
		
		'''
		pass # cpp source

	def distortByPerlinNoise(self, noise_degree: float, noise_scale: float, anisotropic: bool = False, seed: int = 0):
		'''
			
		distort the mesh by the Perlin noise

		Args:
			noise_degree (float): the degree of the noise
			noise_scale (float): the scale of the noise
			anisotropic (bool): if false, the noise will be applied in the direction of the normals, othervice the noise directed in random direction regardless the normals
			seed (int): the seed for the noise
		
		'''
		pass # cpp source

	def splitDisconnectedParts(self) -> list[Mesh]:
		'''
			
		split the mesh into disconnected parts

		Returns:
			list[Mesh]: the list of meshes
		
		'''
		pass # cpp source

	def symmetry(self, start: any, NormalDirection: any, resultInQuads: bool):
		'''
			
		apply symmetry to the mesh

		Args:
			start : the start point of the plane
			NormalDirection : the negative part (regarding the plane normal) of the mesh is removed, replaced with positive part
			resultInQuads (bool): the cut faces will produce quads instead of triangles
		
		'''
		pass # cpp source

	def autodetectSymmetryPlanes(self) -> list[cPy.cTypes.cPlane]:
		'''
			
		Detect the symmetry planes of the mesh

		Returns:
			list[cPy.cTypes.cPlane]: the list of planes
		
		'''
		pass # cpp source

	def weld(self, minimal_relative_distance: float = 0.0001):
		'''
			
		weld the mesh, remove all vertices that are closer than minimal_relative_distance*mesh_bound_box_diagonal to each other

		Args:
			minimal_relative_distance (float): the minimal distance between vertices, relative to the mesh bound box diagonal
		
		'''
		pass # cpp source

	def getBounds(self) -> any:
		'''
			
		get the mesh bound box

		Returns:
			any: the bound box
		
		'''
		pass # cpp source

	def getVolume(self) -> float:
		'''
			
		get the volume of the mesh

		Returns:
			float: the volume
		
		'''
		pass # cpp source

	def getOpenSurfaceVolume(self, start: any, dir: any) -> float:
		'''
			
		calculate the volume even if the mesh is not closed, in this case we define plane that limits the integration

		Args:
			start : the point on that plane
			dir : the normalized vector, normal to the plane

		Returns:
			float: the volume
		
		'''
		pass # cpp source

	def getSquare(self) -> float:
		'''
			
		get square of the mesh

		Returns:
			float: the square (area)
		
		'''
		pass # cpp source

	def getFaceSquare(self, face: int) -> float:
		'''
			
		get the squareof the face

		Args:
			face (int): the face index

		Returns:
			float: the square
		
		'''
		pass # cpp source

	def getFaceUVSquare(self, face: int) -> float:
		'''
			
		get the face square in UV space

		Args:
			face (int): the face index

		Returns:
			float: the square
		
		'''
		pass # cpp source

	def getFaceNormal(self, face: int) -> any:
		'''
			
		get the face normal

		Args:
			face (int): the face index

		Returns:
			any: the face normal
		
		'''
		pass # cpp source

	def relax(self, degree: float, tangent: bool, crease_angle: float = 180):
		'''
			
		relax the mesh, keep the vertices count

		Args:
			degree (float): the degree of relax, may be  > 1
			tangent (bool): should be tangent relax
			crease_angle (float): the crease angle between faces (degrees), if the angle between faces is less than crease_angle, the edge relaxed
		
		'''
		pass # cpp source

	@staticmethod
	def box(center: any = 3, size: any = 3, xAxis: any = 3, yAxis: any = 3, zAxis: any = 3, detail_size: float = 1, fillet: float = 0.0, nx: int = 0, ny: int = 0, nz: int = 0) -> Mesh:
		'''
			
		create the box mesh

		Args:
			center : the box center
			size : the box size
			xAxis : the x-axis direction, if zero, the x-axis is default - (1,0,0)
			yAxis : the y-axis direction, if zero, the y-axis is default - (0,1,0)
			zAxis : the z-axis direction, if zero, the z-axis is default - (0,0,1)
			detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
			fillet (float): the fillet radius
			nx (int): the number of segments along the x-axis (if all of nx, ny, nz are above zero, it overrides the detail_size)
			ny (int): the number of segments along the y-axis (if all of nx, ny, nz are above zero, it overrides the detail_size)
			nz (int): the number of segments along the z-axis (if all of nx, ny, nz are above zero, it overrides the detail_size)

		Returns:
			Mesh: the box mesh
		
		'''
		pass # cpp source

	@staticmethod
	def sphere(center: any = 3, radius: float = 1.0, detail_size: float = 1) -> Mesh:
		'''
			
		create the sphere mesh

		Args:
			center : the sphere center
			radius (float): the sphere radius
			detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size

		Returns:
			Mesh: the sphere mesh
		
		'''
		pass # cpp source

	@staticmethod
	def cylinder(center: any = 3, radius: float = 1, height: float = 2, detail_size: float = 1, slices: int = 0, caps: int = 0, rings: int = 0, fillet: float = 0) -> Mesh:
		'''
			
		create the cylinder mesh

		Args:
			center : the center of the cylinder
			radius (float): the radius of the cylinder
			height (float): the height of the cylinder
			detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
			slices (int): the number of slices, it overrides the detail_size if all of slices, caps, rings are above zero
			caps (int): the number of caps, it overrides the detail_size if all of slices, caps, rings are above zero
			rings (int): the number of rings, it overrides the detail_size if all of slices, caps, rings are above zero
			fillet (float): the fillet radius

		Returns:
			Mesh: the cylinder mesh
		
		'''
		pass # cpp source

	@staticmethod
	def cone(center: any = 3, radius: float = 1, height: float = 2, detail_size: float = 1, topAxis: any = 3) -> Mesh:
		'''
			
		create the cone mesh

		Args:
			center : the center of the cone (the cone base center)
			radius (float): the cone radius
			height (float): the cone height
			detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
			topAxis : the top axis direction, if zero, the top axis is default - (0,1,0)

		Returns:
			Mesh: the cone mesh
		
		'''
		pass # cpp source

	@staticmethod
	def gear(center: any = 3, topR: float = 1, bottomR: float = 1, height: float = 2, detail_size: float = 1, depth: float = 0.1, sharpness: float = 0.5, teeth: int = 16) -> Mesh:
		'''
			
		create the gear mesh

		Args:
			center : the center of the gear (the gear base center)
			topR (float): the gear top radius
			bottomR (float): the gear bottom radius
			height (float): the gear height
			detail_size (float): the average length of the edge over the figure. The figure will be divided so that edges length will be approximately the detail_size
			depth (float): the gear depth
			sharpness (float): the gear sharpness
			teeth (int): the gear teeth

		Returns:
			Mesh: the cone mesh
		
		'''
		pass # cpp source

	@staticmethod
	def plane(center: any = 3, sizeX: float = 2, sizeY: float = 2, divisionsX: int = 2, divisionsY: int = 2, xAxis: any = 3, yAxis: any = 3) -> Mesh:
		'''
			
		create the single-side plane mesh, the faces normals are put toward the vec3.Cross(xAxis, yAxis)

		Args:
			center : the center of the plane
			sizeX (float): the plane size along the X-axis
			sizeY (float): the plane size along the Y-axis
			divisionsX (int): amount of divisions along the X-axis
			divisionsY (int): amount of divisions along the Y-axis
			xAxis : the vector of the X-axis
			yAxis : the vector of the Y-axis

		Returns:
			Mesh: the plane mesh
		
		'''
		pass # cpp source

	@staticmethod
	def hexagonal_plane(center: any = 3, sizeX: float = 2, sizeY: float = 2, divisionsX: int = 2, divisionsY: int = 2, xAxis: any = 3, yAxis: any = 3) -> Mesh:
		'''
			
		create the single-side triangular plane mesh that consists mostly of quasi equally-sided triangles

		Args:
			center : the center of the plane
			sizeX (float): the plane size along the X-axis
			sizeY (float): the plane size along the Y-axis
			divisionsX (int): amount of divisions along the X-axis
			divisionsY (int): amount of divisions along the Y-axis
			xAxis : the vector of the X-axis
			yAxis : the vector of the Y-axis

		Returns:
			Mesh: the hexagonal plane mesh
		
		'''
		pass # cpp source

	@staticmethod
	def text(string: str, font: str = "tahoma", height: float = 10.0, center: any = 3, text_direction: any = 3, text_normal: any = 3, thickness: float = 1, align: int = 1) -> Mesh:
		'''
			
		Create the text mesh

		Args:
			string (str): the text string
			font (str): the font name
			height (float): the text height
			center : the text center
			text_direction : the text direction left to right
			text_normal : the normal direction of the text
			thickness (float): the thickness of the text
			align (int): the text align, 0 - left, 1 - center, 2 - right

		Returns:
			Mesh: the text mesh
		
		'''
		pass # cpp source

	def createVDM(self, side: int, path_to_exr: str, center: any = 3, radius: float = 1, up: any = 3, x: any = 3, y: any = 3):
		'''
			
		Create the vector displacement map from the mesh and save it as EXR file. The mesh is put on plane at center and clamped by that plane.

		Args:
			side (int): the EXR  file side size
			path_to_exr (str): the path to the EXR file
			center : the center of the plane
			radius (float): the radius that should include the mesh
			up : the up vector of the plane
			x : the x vector of the plane
			y : the y vector of the plane
		
		'''
		pass # cpp source

	def shell(self, thickness_out: float, thickness_in: float, divisions: int = 1):
		'''
			
		add some thickness to the mesh (intrude a bit)

		Args:
			thickness_out (float): the thickness in the outer direction (extrusion)
			thickness_in (float): the thickness in the inner direction (intrusion)
			divisions (int): the amount of divisions of the edge
		
		'''
		pass # cpp source

	def extrudeOpenEdges(self, distance: float, direction: any = 3) -> list[int]:
		'''
			
		extrude open edges of the mesh

		Args:
			distance (float): the distance to extrude
			direction : the extrude direction, if zero , the direction is the local vertex normal

		Returns:
			list[int]: s the list of extruded edges, even is the start vertex, odd is the end vertex
		
		'''
		pass # cpp source

	def expandOpenEdges(self, distance: float) -> list[int]:
		'''
			
		extrude open edges of the mesh

		Args:
			distance (float): the distance to extrude

		Returns:
			list[int]: s the list of extruded edges, even is the start vertex, odd is the end vertex
		
		'''
		pass # cpp source

	def getOpenEdges(self) -> list[int]:
		'''
			
		get the list of open edges

		Returns:
			list[int]: the list of open edges, the even is the start vertex, the odd is the end vertex
		
		'''
		pass # cpp source

	def getLengthAlongDirection(self, dir: any) -> float:
		'''
			
		get the mesh size along some axis

		Args:
			dir : the axis direction

		Returns:
			float: the size along the axis
		
		'''
		pass # cpp source

	def getCenterMass(self) -> any:
		'''
			
		calculate the center mass of the mesh

		Returns:
			any: the center mass of the surface
		
		'''
		pass # cpp source



class Image():
	'''
			
		The image references. Look the cImage for the list of allowed operations
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, im: Image):
		pass # CPP source

	def Read(self, name: str) -> bool:
		'''
			
		Read the image from the file

		Args:
			name (str): the image name

		Returns:
			bool: true if loaded successfully
		
		'''
		pass # cpp source

	def Write(self, name: str) -> bool:
		'''
			
		Write the image to file

		Args:
			name (str): the filename

		Returns:
			bool: true if succeed
		
		'''
		pass # cpp source

	def FromTexture(self, texture_id: int) -> bool:
		'''
			
		Get image from texture

		Returns:
			bool: true if succeed
		
		'''
		pass # cpp source

	def ToTexture(self) -> int:
		'''
			
		Create texture from image

		Returns:
			int: true if succeed
		
		'''
		pass # cpp source

	def Paste(self, src_data: any, pasteLeft: int = 0, pasteTop: int = 0, cropLeft: int = 0, cropTop: int = 0, cropRight: int = 0, cropBottom: int = 0, flipY: bool = False) -> int:
		'''
			
		paste image to image

		Returns:
			int: true if succeed
		
		'''
		pass # cpp source

	def Pointer(self) -> int:
		'''
			
		Pointer to the data

		Returns:
			int: true if succeed
		
		'''
		pass # cpp source

	def FromArray(self, src_data: any) -> bool:
		'''
			
		Get image from texture

		Returns:
			bool: true if succeed
		
		'''
		pass # cpp source

	def FromArray(self, src_data: any) -> bool:
		pass # cpp source

	def FromArray(self, src_data: any) -> bool:
		pass # cpp source

	@staticmethod
	def cImageFromArray(src_data: any, image: any) -> bool:
		'''
			
		Get image from texture

		Returns:
			bool: true if succeed
		
		'''
		pass # cpp source

	@staticmethod
	def cImageFromArray(src_data: any, image: any) -> bool:
		pass # cpp source

	@staticmethod
	def cImageFromArray(src_data: any, image: any) -> bool:
		pass # cpp source

	def _py_buffer_info(self) -> any:
		pass # cpp source



class symm():
	@staticmethod
	def enable(_0: bool = True) -> symm:
		'''
			
		Enable the symmetry

		Args:
			_enable (bool): true to enable, false to disable

		Returns:
			symm: reference for the chain-like operations
		
		'''
		pass # cpp source

	@staticmethod
	def enabled() -> bool:
		pass # cpp source

	@staticmethod
	def disable() -> symm:
		'''
			
		disable the symmetry

		Returns:
			symm: reference
		
		'''
		pass # cpp source

	@staticmethod
	def xyz(x: bool, y: bool, z: bool) -> symm:
		'''
			
		Enable the XYZ-mirror symmetry

		Args:
			x (bool): true to enable x-symmetry, false to disable
			y (bool): true to enable y-symmetry, false to disable
			z (bool): true to enable z-symmetry, false to disable

		Returns:
			symm: reference
		
		'''
		pass # cpp source

	@staticmethod
	def is_xyz() -> bool:
		'''
			
		check if the XYZ symmetry enabled

		Returns:
			bool: true if this type of the symmetry active
		
		'''
		pass # cpp source

	@staticmethod
	def x() -> bool:
		'''
			
		check x symmetry state

		Returns:
			bool: reference to the x symmetry state
		
		'''
		pass # cpp source

	@staticmethod
	def y() -> bool:
		'''
			
		check y symmetry state

		Returns:
			bool: reference to the y symmetry state
		
		'''
		pass # cpp source

	@staticmethod
	def z() -> bool:
		'''
			
		check z symmetry state

		Returns:
			bool: reference to the z symmetry state
		
		'''
		pass # cpp source

	@staticmethod
	def axial(n: int, extraMirror: bool = False, stepSymmetry: bool = False) -> symm:
		'''
			
		Enable the axial symmetry

		Args:
			n (int): the order of the axial symmetry
			extraMirror (bool): add the extra mirror orthogonal to the axis
			stepSymmetry (bool): enable the step symmetry

		Returns:
			symm: reference
		
		'''
		pass # cpp source

	@staticmethod
	def is_axial() -> bool:
		'''
			
		Check if the axial symmetry enabled

		Returns:
			bool: true if the axial symmetry enabled
		
		'''
		pass # cpp source

	@staticmethod
	def axialOrder() -> int:
		'''
			
		returns the axial symmetry order if axial or axial mirror symmetry enabled

		Returns:
			int: the reference to the order of the axial symmetry
		
		'''
		pass # cpp source

	@staticmethod
	def extraMirror() -> bool:
		'''
			
		returns the state of extra mirror, this is valid only tor the axial symmetry

		Returns:
			bool: the reference to the extra mirror state
		
		'''
		pass # cpp source

	@staticmethod
	def stepSymmetry() -> bool:
		'''
			
		returns the state of step symmetry

		Returns:
			bool: the reference to the step symmetry state
		
		'''
		pass # cpp source

	@staticmethod
	def axialMirror(n: int, extraMirror: bool = False, stepSymmetry: bool = False) -> symm:
		'''
			
		Enable the axial mirror symmetry

		Args:
			n (int): the order of the symmetry
			extraMirror (bool): dd the extra mirror orthogonal to the axis
			stepSymmetry (bool): enable the step symmetry

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def isAxialMirror() -> bool:
		'''
			
		Check if the axial mirror symmetry enabled

		Returns:
			bool: true if the axial mirror symmetry enabled
		
		'''
		pass # cpp source

	@staticmethod
	def translation(numX: int, stepX: float, numY: int, stepY: float, numZ: int, stepZ: float) -> symm:
		'''
			
		Enable the translation symmetry

		Args:
			numX (int): number of x-repeats
			stepX (float): the step of the x-repeat
			numY (int): number of y-repeats
			stepY (float): the step of the y-repeat
			numZ (int): number of z-repeats
			stepZ (float): the step of the z-repeat

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def is_translation() -> bool:
		'''
			
		Check if the translation symmetry enabled

		Returns:
			bool: the state
		
		'''
		pass # cpp source

	@staticmethod
	def numX() -> int:
		'''
			
		returns the reference to the number of the x repeats if the translational symmetry used

		Returns:
			int: the bool reference
		
		'''
		pass # cpp source

	@staticmethod
	def stepX() -> float:
		'''
			
		returns the reference to the x-step if the translational symmetry used

		Returns:
			float: the value reference
		
		'''
		pass # cpp source

	@staticmethod
	def numY() -> int:
		'''
			
		returns the reference to the number of the y repeats if the translational symmetry used

		Returns:
			int: the bool reference
		
		'''
		pass # cpp source

	@staticmethod
	def stepY() -> float:
		'''
			
		returns the reference to the y-step if the translational symmetry used

		Returns:
			float: the value reference
		
		'''
		pass # cpp source

	@staticmethod
	def numZ() -> int:
		'''
			
		returns the reference to the number of the z repeats if the translational symmetry used

		Returns:
			int: the bool reference
		
		'''
		pass # cpp source

	@staticmethod
	def stepZ() -> float:
		'''
			
		returns the reference to the z-step if the translational symmetry used

		Returns:
			float: the value reference
		
		'''
		pass # cpp source

	@staticmethod
	def toGlobalSpace() -> symm:
		'''
			
		set the symmetry to be in global space

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def toLocalSpace() -> symm:
		'''
			
		set the symmetry to be in local space

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def toGeneral() -> symm:
		'''
			
		set the symmetry to general case

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def set_start(pos: any) -> symm:
		'''
			
		set the central point for the symmetry

		Args:
			pos : the position (in local or global space, see the localSpace() or globalSpace())

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def start() -> any:
		'''
			
		get the start point reference

		Returns:
			any: the point reference
		
		'''
		pass # cpp source

	@staticmethod
	def set_end(pos: any) -> symm:
		'''
			
		set the end point for the symmetry axis, calling this function enables the general case of the symmetry

		Args:
			pos : the position

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def end() -> any:
		'''
			
		the end point reference

		Returns:
			any: the point reference
		
		'''
		pass # cpp source

	@staticmethod
	def showSymmetryPlane(show: bool = True) -> symm:
		'''
			
		Show or hide the symmetry planes

		Args:
			show (bool): set true to show

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def setCustomSymetryTransforms(symmetryTransforms: any) -> symm:
		'''
			
		enable the custom symmetry, provide the symmetry transfoms

		Args:
			symmetryTransforms : the list of additional transforms (list of coat.mat4) that will be applied to the any user action

		Returns:
			symm: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def isCustomSymmetry() -> bool:
		'''
			
		Check if the custom symmetry used

		Returns:
			bool: true if the custom symmetry enabled
		
		'''
		pass # cpp source

	@staticmethod
	def getCurrentTransforms() -> list[mat4]:
		'''
			
		Returns all transforms using the current symmetry state

		Returns:
			list[mat4]: the resulting list of coat.mat4
		
		'''
		pass # cpp source

	@staticmethod
	def getCurrentPlanes() -> list[cPy.cTypes.cPlane]:
		'''
			
		Returns all symmetry planes using the current symmetry state

		Returns:
			list[cPy.cTypes.cPlane]: the resulting list of planes (coat.plane)
		
		'''
		pass # cpp source

	@staticmethod
	def disableGlobally():
		'''
			
		Totally disable symmetry, don't forget to enable after all operations!
		
		'''
		pass # cpp source

	@staticmethod
	def enableGlobally():
		'''
			
		Enable symmetry (preliminary disabled by disableGlobally)
		
		'''
		pass # cpp source



class SceneElement():
	'''
			
		The scene element, like sculpt object or curve
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, vo: any):
		pass # CPP source

	def __init__(self, c: any):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def __eq__(self, other: SceneElement) -> bool:
		return super().__eq__(other)

	def __ne__(self, other: SceneElement) -> bool:
		return super().__ne__(other)

	def parent(self) -> SceneElement:
		'''
			
		get the parent scene graph element

		Returns:
			SceneElement: the parent reference
		
		'''
		pass # cpp source

	def childCount(self) -> int:
		'''
			
		returns the child elements count

		Returns:
			int: child count
		
		'''
		pass # cpp source

	def child(self, index: int) -> SceneElement:
		'''
			
		returns child element by index

		Args:
			index (int): the index of the element in subtree

		Returns:
			SceneElement: the child reference
		
		'''
		pass # cpp source

	def isSculptObject(self) -> bool:
		'''
			
		Check if it is the sculpt object

		Returns:
			bool: true if this is the sculpt object
		
		'''
		pass # cpp source

	def isCurve(self) -> bool:
		'''
			
		Check if the element is curve

		Returns:
			bool: true if this is curve
		
		'''
		pass # cpp source

	def setTransform(self, Transform: any) -> SceneElement:
		'''
			
		Set the transform matrix

		Args:
			Transform : the transform matrix

		Returns:
			SceneElement: this element reference
		
		'''
		pass # cpp source

	def transform(self, Transform: any) -> SceneElement:
		'''
			
		Additional transform over the object

		Args:
			Transform : the matrix

		Returns:
			SceneElement: this element reference
		
		'''
		pass # cpp source

	def density(self, density_value: float) -> SceneElement:
		'''
			
		this command useful if you use voxels, it sets the scale for the volume so that there will be density_value of voxels per mm

		Args:
			density_value (float): the voxels per mm
		
		'''
		pass # cpp source

	def transform_single(self, Transform: any) -> SceneElement:
		'''
			
		Additional transform over the object, not applied to child objects

		Args:
			Transform : the matrix

		Returns:
			SceneElement: this element reference
		
		'''
		pass # cpp source

	def getTransform(self) -> any:
		'''
			
		get the scene element transform

		Returns:
			any: the transform matrix
		
		'''
		pass # cpp source

	def clear(self) -> SceneElement:
		'''
			
		Clear the element content

		Returns:
			SceneElement: this element reference
		
		'''
		pass # cpp source

	def name(self) -> str:
		'''
			
		get the element name

		Returns:
			str: the name
		
		'''
		pass # cpp source

	def getLinkedPath(self, id: int) -> str:
		'''
			
		get the linked file path

		Returns:
			str: the name
		
		'''
		pass # cpp source

	def linkedObjectCount(self) -> int:
		'''
			
		get the linked file path

		Returns:
			int: the name
		
		'''
		pass # cpp source

	def addLinkedPath(self, path: str):
		'''
			
		set the linked file path

		Returns:
			the name
		
		'''
		pass # cpp source

	def rename(self, name: str) -> SceneElement:
		'''
			
		rename the element

		Args:
			name (str): the new name

		Returns:
			SceneElement: this element reference
		
		'''
		pass # cpp source

	def addChild(self, name: str) -> SceneElement:
		'''
			
		add the child element of the same nature

		Args:
			name (str): the name

		Returns:
			SceneElement: the new element reference
		
		'''
		pass # cpp source

	def findInSubtree(self, name: str) -> SceneElement:
		'''
			
		find the element in subtree by name

		Args:
			name (str): the name t seek

		Returns:
			SceneElement: the element reference
		
		'''
		pass # cpp source

	def iterateSubtree(self, fn: any) -> bool:
		'''
			
		iterate over the subtree

		Args:
			fn : the function to call, return true if need to stop the iterations,
		function looks like\n
		
		::

			def fn(el):
			    ...code...
			    return False or True
			

			el is coat.SceneElement

		Returns:
			bool: true if the callback interrupted the iterations
		
		'''
		pass # cpp source

	def iterateVisibleSubtree(self, fn: any) -> bool:
		'''
			
		iterate over the visible subtree

		Args:
			fn : the function to call, return true if need to stop the iterations,
		function looks like\n
		
		::

			def fn(el):
			    ...code...
			    return False or True
			

			el is coat.SceneElement

		Returns:
			bool: True if the callback interrupted the iterations
		
		'''
		pass # cpp source

	def mergeSubtree(self, booleanMerge: bool = False):
		'''
			
		merge all subtree volumes into this

		Args:
			booleanMerge (bool): use boolean summ to merge. Othervice merge meshes without booleans.
		This option works only for surfave, in voxels it will always do boolean summ
		
		'''
		pass # cpp source

	def mergeTo(self, dest: SceneElement, op: BoolOpType):
		'''
			
		merge the volume to another one, delete this volume

		Args:
			dest (SceneElement): the destination
			op (BoolOpType): the boolean operation type
		
		'''
		pass # cpp source

	def copyMergeTo(self, dest: SceneElement, op: BoolOpType):
		'''
			
		copy and merge the volume to another one, delete this volume

		Args:
			dest (SceneElement): the destination
			op (BoolOpType): the boolean operation type
		
		'''
		pass # cpp source

	def removeSubtree(self):
		'''
			
		remove the whole subtree
		
		'''
		pass # cpp source

	def removeSubtreeItem(self, index: int):
		'''
			
		remove one child from the subtree

		Args:
			index (int): index of the child
		
		'''
		pass # cpp source

	def remove(self):
		'''
			
		remove this item and all child objects from the scene
		
		'''
		pass # cpp source

	def duplicate(self) -> SceneElement:
		'''
			
		diplicate the item

		Returns:
			SceneElement: the new item reference
		
		'''
		pass # cpp source

	def duplicateAsInstance(self) -> SceneElement:
		'''
			
		create the instance of the object if instancing supported

		Returns:
			SceneElement: the instance reference
		
		'''
		pass # cpp source

	def changeParent(self, newParent: SceneElement):
		'''
			
		change the parent element for the current one

		Args:
			newParent (SceneElement): the new parent reference. Pay attention, changing paren is not always possible!
		
		'''
		pass # cpp source

	def moveTo(self, newParent: SceneElement, indexInParent: int):
		'''
			
		move the element to another parent

		Args:
			newParent (SceneElement): the new parent reference
			indexInParent (int): the index in the parent
		
		'''
		pass # cpp source

	def isParentOf(self, child: SceneElement) -> bool:
		'''
			
		check if the element is parent of another one

		Args:
			child (SceneElement): the child element

		Returns:
			bool: true if this element is parent of the child
		
		'''
		pass # cpp source

	def visible(self) -> bool:
		'''
			
		returns own visibility state reference. It does not take into account that parent may be invisible.

		Returns:
			bool: item local visibility reference, you may get and set the visibility with the reference.
		
		'''
		pass # cpp source

	def setVisibility(self, visible: bool):
		'''
			
		set the visibility of the element

		Args:
			visible (bool): true if need to be visible
		
		'''
		pass # cpp source

	def ghost(self) -> bool:
		'''
			
		returs the state of ghosting (if available)

		Returns:
			bool: true if ghosted
		
		'''
		pass # cpp source

	def setGhost(self, ghost: bool):
		'''
			
		sets the ghosting state (if available)

		Args:
			ghost (bool): set true to ghost
		
		'''
		pass # cpp source

	def getReferenceColor(self) -> any:
		'''
			
		get the reference color for the element

		Returns:
			any: the color (r,g,b,a), each channel is 0..1
		
		'''
		pass # cpp source

	def setReferenceColor(self, color: any):
		'''
			
		set the reference color for the element

		Args:
			color : the (r, g, b, a) color, each channel is 0..1
		
		'''
		pass # cpp source

	def Volume(self) -> any:
		'''
			
		 returns the volume object to operate over voxels or surface
		
		'''
		pass # cpp source

	def select(self):
		'''
			
		 add the object to selected
		
		'''
		pass # cpp source

	def selectOne(self):
		'''
			
		 unselect all similar elements and select this one
		
		'''
		pass # cpp source

	def unselectAll(self):
		'''
			
		 unselect all similar objects
		
		'''
		pass # cpp source

	def selected(self) -> bool:
		'''
			
		 Check if the scene element is selected
		
		'''
		pass # cpp source

	def collectSelected(self) -> list[SceneElement]:
		'''
			
		 Collect the selected elements in the subtree (including this element if selected)
		
		'''
		pass # cpp source



class Volume():
	'''
			
		The class allows to operate over voxels/surface on the relatively low-level
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, tb: any):
		pass # CPP source

	def __init__(self, vo: any):
		pass # CPP source

	def __init__(self, vol: Volume):
		pass # CPP source

	def valid(self) -> bool:
		'''
			
		checks if object is valid

		Returns:
			bool: true if the volume exists
		
		'''
		pass # cpp source

	def isSurface(self) -> bool:
		'''
			
		Check if in surface mode

		Returns:
			bool: true if in surface mode
		
		'''
		pass # cpp source

	def isVoxelized(self) -> bool:
		'''
			
		Check if in voxel mode

		Returns:
			bool: true if in voxel mode
		
		'''
		pass # cpp source

	def toSurface(self):
		'''
			
		turn to surface mode, the triangles will be tangentially relaxed
		
		'''
		pass # cpp source

	def toVoxels(self):
		'''
			
		turn to voxels, auto-voxelize
		
		'''
		pass # cpp source

	@staticmethod
	def enableVoxelsColoring(enable: bool = True):
		'''
			
		enable or disable the voxel-based coloring. It is applied wherever possible - merging models, brushing, creating parametric voxel figures, etc

		Args:
			enable (bool): true to enable
		
		'''
		pass # cpp source

	@staticmethod
	def color(CL: int):
		'''
			
		set the default color to fill voxels if the voxel coloring enabled
		
		'''
		pass # cpp source

	@staticmethod
	def color(r: float, g: float, b: float, a: float):
		'''
			
		assign the color for the voxel operations

		Args:
			r (float): red value 0..255
			g (float): green value 0..255
			b (float): blue value 0..255
			a (float): alpha value 0..255
		
		'''
		pass # cpp source

	@staticmethod
	def color(r: float, g: float, b: float):
		'''
			
		assign the color for the voxel operations

		Args:
			r (float): red value 0..255
			g (float): green value 0..255
			b (float): blue value 0..255
		
		'''
		pass # cpp source

	@staticmethod
	def color(colorid: str):
		'''
			
		assign the color for the voxel operations

		Args:
			colorid (str): the color in any suitable form: "RGB", "ARGB", "RRGGBB", "AARRGGBB", "#RGB", "#ARGB", "#RRGGBB", "#AARRGGBB",
		any web-color common name as "red", "green", "purple", google "webcolors"
		
		'''
		pass # cpp source

	@staticmethod
	def gloss(value: float):
		'''
			
		assign the gloss for the voxel operations, it will work only if the color already assigned

		Args:
			value (float): the [0..1] value of the gloss
		
		'''
		pass # cpp source

	@staticmethod
	def roughness(value: float):
		'''
			
		assign the roughness for the voxel operations, it will work only if the color already assigned

		Args:
			value (float): the [0..1] value of the roughness
		
		'''
		pass # cpp source

	@staticmethod
	def metal(value: float):
		'''
			
		the metalliclty value for the voxel operations, it will work only if the color already assigned

		Args:
			value (float): the [0..1] metal value
		
		'''
		pass # cpp source

	def mergeMesh(self, mesh: Mesh, transform: any = 4, op: BoolOpType = Coat_CPP.BoolOpType.BOOL_MERGE):
		'''
			
		merge the mesh into scene

		Args:
			mesh (Mesh): the Mesh reference
			transform : the transform applied
			op (BoolOpType): the type of the merge
		
		'''
		pass # cpp source

	def insertMesh(self, mesh: Mesh, transform: any = 4):
		'''
			
		insert the mesh into the volume, in case of voxels this is identical to addMesh, in case of surface, mesh will be inserted without booleans

		Args:
			mesh (Mesh): the mesh reference
			transform : the transform applied
		
		'''
		pass # cpp source

	def addMesh(self, mesh: Mesh, transform: any = 4):
		'''
			
		add the mesh to volume (boolean)

		Args:
			mesh (Mesh): the mesh reference
			transform : the transform applied
		
		'''
		pass # cpp source

	def subtractMesh(self, mesh: Mesh, transform: any = 4):
		'''
			
		subtract the mesh from volume (boolean)

		Args:
			mesh (Mesh): the mesh reference
			transform : the transform applied
		
		'''
		pass # cpp source

	def intersectWithMesh(self, mesh: Mesh, transform: any = 4):
		'''
			
		intersect the volume with the mesh (boolean)

		Args:
			mesh (Mesh): the mesh reference
			transform : the transform applied
		
		'''
		pass # cpp source

	def mergeMeshWithTexture(self, mesh: Mesh, transform: any = 4, op: BoolOpType = Coat_CPP.BoolOpType.BOOL_MERGE):
		'''
			
		merge the mesh with facture, the volume polygons will be hidden, just the texture will be shown (like leafs in TreesGenerator)

		Args:
			mesh (Mesh): the mesh that refers texture
			transform : the transform applied
			op (BoolOpType): the boolean operation
		
		'''
		pass # cpp source

	def getExactDencity(self, x: int, y: int, z: int, fromBackup: bool, cache_ref: any) -> float:
		'''
			
		returns the exact voxel density in local space at the exact integer location

		Args:
			x (int): X-coordinate
			y (int): Y-coordinate (up)
			z (int): Z-coordinate
			fromBackup (bool): take the values from the backup (kept before the modifications started)
			cache_ref : define the variable coat::VolumeCache and pass there (in same thread) to speed up access;

		Returns:
			float: the density 0..1
		
		'''
		pass # cpp source

	def getInterpolatedValue(self, pos: any, fromBackup: bool) -> float:
		'''
			
		returns interolated voxels density

		Args:
			pos : position in local space
			fromBackup (bool): take from the backup

		Returns:
			float: linearly interplated value of the density
		
		'''
		pass # cpp source

	def getPolycount(self) -> int:
		'''
			
		get the volume triangles count

		Returns:
			int: triangles count
		
		'''
		pass # cpp source

	def getVolume(self) -> float:
		'''
			
		get the volume of this object in world coordinates

		Returns:
			float: volume
		
		'''
		pass # cpp source

	def getSquare(self) -> float:
		'''
			
		reg the square of this object in world coordinates

		Returns:
			float: square
		
		'''
		pass # cpp source

	def calcLocalSpaceAABB(self) -> any:
		'''
			
		Calculate the Axis - Aligned Bound Box of the object in local space

		Returns:
			any: the boundary as cBounds
		
		'''
		pass # cpp source

	def calcWorldSpaceAABB(self) -> any:
		'''
			
		Calculate the Axis - Aligned Bound Box of the object in world space

		Returns:
			any: the boundary as cBounds
		
		'''
		pass # cpp source

	def tree(self) -> any:
		'''
			
		returns the low-level object (VoxTreeBranch) for all low-level operations

		Returns:
			any: the VoxTreeBranch* pointer
		
		'''
		pass # cpp source

	def vo(self) -> any:
		'''
			
		returns the low-level object (VolumeObject) for all low-level operations

		Returns:
			any: the VolumeObject* pointer
		
		'''
		pass # cpp source

	def cell(self, cx: int, cy: int, cz: int, create: bool, backup: bool) -> any:
		'''
			
		get the cell by cell coordinates, each cell is 8*8*8

		Args:
			cx (int): cell x
			cy (int): cell y
			cz (int): cell z
			create (bool): pass true if you want to create the cell if it does not exist
			backup (bool): drop the cell to backup (if not already dropped)

		Returns:
			any: the pointer to the VolumeCell
		
		'''
		pass # cpp source

	def dirty(self, cx: int, cy: int, cz: int):
		'''
			
		mark the cell as dirty. This is required if you
		
		'''
		pass # cpp source

	def setOpacity(self, Opacity: float):
		'''
			
		set the volume opacity

		Args:
			Opacity (float): the 0..1 opacity value
		
		'''
		pass # cpp source

	def relaxGpu(self, center: any, Radius: float, degree: float):
		'''
			
		fast voxel-based relax within the sphere with the gradual falloff. It works only in voxel mode.

		Args:
			center : the center of
			Radius (float): the radius of the influence
			degree (float): the relax degree, < 1
		
		'''
		pass # cpp source

	def relaxVoxels(self, count: int):
		'''
			
		relax the whole volume, works only for voxels

		Args:
			count (int): the count of relax steps
		
		'''
		pass # cpp source

	def relaxSurface(self, degree: float, tangent: bool = False, keep_sharp_boolean_edges: bool = False):
		'''
			
		relax the object in surface mode

		Args:
			degree (float): the degree of smoothing, it may be >1 for the stronger relax
			tangent (bool): use tangent relax
			keep_sharp_boolean_edges (bool): keep the sharp edges appeared due to bolean operations
		
		'''
		pass # cpp source

	def relaxOpenEdges(self, nTimes: int):
		'''
			
		relax the open edges of the mesh, it is applicable only to the surface mode

		Args:
			nTimes (int): amount of iterations
		
		'''
		pass # cpp source

	def inScene(self) -> SceneElement:
		'''
			
		Get the Volume placement in the scene

		Returns:
			SceneElement: the SceneElement
		
		'''
		pass # cpp source

	def clear(self):
		'''
			
		Clear and pass to the Undo queue
		
		'''
		pass # cpp source

	def clearNoUndo(self):
		'''
			
		Clear quickly, without affecting the Undo queue
		
		'''
		pass # cpp source

	def assignShader(self, shaderName: str):
		'''
			
		set the shader for the Volume

		Args:
			shaderName (str): the shader name as it is shown in the shader's hint
		
		'''
		pass # cpp source

	def setBoolShaderProperty(self, property: str, value: bool):
		pass # cpp source

	def setFloatShaderProperty(self, property: str, value: float):
		pass # cpp source

	def setColorShaderProperty(self, property: str, value: int):
		pass # cpp source

	def closeHoles(self, maxSize: int):
		'''
			
		Close the holes

		Args:
			maxSize (int): max hole size (edges over the primeter)
		
		'''
		pass # cpp source

	@staticmethod
	def checkIfMoldingLicenseAvailable() -> bool:
		'''
			
		check if molding allowed

		Returns:
			bool: true if the molding license available
		
		'''
		pass # cpp source

	@staticmethod
	def setMoldingParams(direction: any, tapering_angle: float = 0, undercuts_density: float = 1.0, decimation_limit_millions: float = 10, perform_subtraction: bool = True):
		'''
			
		set the parameters for the molding

		Args:
			direction : the molding direction
			tapering_angle (float): the tapering angle in degrees
			undercuts_density (float): the additional density for the undercuts
			decimation_limit_millions (float): decimate the final shape if it has triangles count more than this value
			perform_subtraction (bool): set false if no need to subtract the molding from the molding shapes
		
		'''
		pass # cpp source

	def removeUndercuts(self):
		'''
			
		remove undercuts for the current volume
		
		'''
		pass # cpp source

	def basRelief(self, start_point: any = 3):
		'''
			
		perform the bas-relief for the current volume

		Args:
			start_point : the cut point
		
		'''
		pass # cpp source

	@staticmethod
	def setAutomaticMoldingBox():
		'''
			
		set the molding bound box to be automatic
		
		'''
		pass # cpp source

	@staticmethod
	def setMoldingBox(width: float, length: float, thickness: float):
		'''
			
		set the molding bound box to be user-defined, not automatic

		Args:
			width (float): the width of the box
			length (float): the length of the box
			thickness (float): the thickness of the box
		
		'''
		pass # cpp source

	@staticmethod
	def setMoldingBorder(width: float = 0):
		'''
			
		set the molding border around the parting line to fade to the plane, if it is zero, the final shape will not fade to plane

		Args:
			width (float): the width in mm or other default units
		
		'''
		pass # cpp source

	def generateMoldingCurves(self):
		'''
			
		generate the automatic molding curves
		
		'''
		pass # cpp source

	def automaticMolding(self):
		'''
			
		perform the automatic molding
		
		'''
		pass # cpp source

	def curveBasedMolding(self):
		'''
			
		perform the curve-based mold
		
		'''
		pass # cpp source

	def subtractWithoutUndecuts(self):
		'''
			
		subtract the current undercutted object from the preliminary generated molding shapes
		
		'''
		pass # cpp source

	def generateMoldingTest(self) -> SceneElement:
		'''
			
		generate the figure that fills the gap between the molding shapes

		Returns:
			SceneElement: the generated scene element reference
		
		'''
		pass # cpp source

	def findMoldingTop(self) -> SceneElement:
		'''
			
		find the top molding shape (that was previously generated)

		Returns:
			SceneElement: the top shape reference
		
		'''
		pass # cpp source

	def findMoldingBottom(self) -> SceneElement:
		'''
			
		find the bottom molding shape (that was previously generated)

		Returns:
			SceneElement: the bottom shape reference
		
		'''
		pass # cpp source

	def findMoldingTest(self) -> SceneElement:
		'''
			
		find the test molding test shape (that was previously generated)

		Returns:
			SceneElement: the test shape reference
		
		'''
		pass # cpp source

	def removeMoldingShapes(self):
		'''
			
		remove all molding intermediate shapes, tests, etc.
		
		'''
		pass # cpp source

	def assignLiveBooleans(self, operation: int):
		'''
			
		Apply the live booleans over the sculpt mesh, it is available for voxels only

		Args:
			operation (int): 0 - stop live booleans, 1 - subtract from the parent, 2 - intersect, 3 - union
		
		'''
		pass # cpp source

	def collapseBollTree(self):
		'''
			
		collapse the boolean tree, it is available for this volume
		
		'''
		pass # cpp source



class settings():
	@staticmethod
	def valueExists(ID: str) -> bool:
		'''
			
		returns true if the value in settings exists

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)

		Returns:
			bool: true if identifier exists
		
		'''
		pass # cpp source

	@staticmethod
	def getBool(ID: str) -> bool:
		'''
			
		get the boolen value from the settings

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)

		Returns:
			bool: the boolean value, false if not exists or casting impossible
		
		'''
		pass # cpp source

	@staticmethod
	def getString(ID: str) -> str:
		'''
			
		get the string value from the settings

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)

		Returns:
			str: the string value, empty if not exists
		
		'''
		pass # cpp source

	@staticmethod
	def getFloat(ID: str) -> float:
		'''
			
		get the float value from the settings

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)

		Returns:
			float: the float value, 0 if not exists or casting impossible
		
		'''
		pass # cpp source

	@staticmethod
	def getInt(ID: str) -> int:
		'''
			
		get the integer value from the settings

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)

		Returns:
			int: the integer value, 0 if not exists or casting impossible
		
		'''
		pass # cpp source

	@staticmethod
	def setBool(ID: str, value: bool) -> bool:
		'''
			
		set the boolean value to the settings

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
			value (bool): the value to set

		Returns:
			bool: true if the value was set successfully
		
		'''
		pass # cpp source

	@staticmethod
	def setString(ID: str, value: str) -> bool:
		'''
			
		set the string value to the settings

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
			value (str): the value to set

		Returns:
			bool: true if the value was set successfully
		
		'''
		pass # cpp source

	@staticmethod
	def setFloat(ID: str, value: float) -> bool:
		'''
			
		set the float value to the settings

		Args:
			ID (str): the identifier or English text of the option, take identifier from the UI as usual (RMB + MMB)
			value (float): the value to set

		Returns:
			bool: true if the value was set successfully
		
		'''
		pass # cpp source

	@staticmethod
	def setInt(ID: str, value: int) -> bool:
		'''
			
		set the integer value to the settings

		Args:
			value (int): the value to set

		Returns:
			bool: true if the value was set successfully
		
		'''
		pass # cpp source

	@staticmethod
	def saveSettings():
		'''
			
		save all changed settings
		
		'''
		pass # cpp source

	@staticmethod
	def resetSettings(ResetGeneralSettings: bool = True, ResetHiddenSet: bool = True, ResetHotkeys: bool = True, RestNavigation: bool = True, ResetPresets: bool = True, ResetTheme: bool = True, ResetWindows: bool = True):
		'''
			
		reset all settings to default values, application will restart

		Args:
			ResetGeneralSettings (bool): reset general settings
			ResetHiddenSet (bool): reset the hidden UI elements list
			ResetHotkeys (bool): reset the hotkeys
			RestNavigation (bool): reset the navigation settings
			ResetPresets (bool): reset the presets
			ResetTheme (bool): reset the theme
			ResetWindows (bool): reset the floating windows placement
		
		'''
		pass # cpp source

	@staticmethod
	def listAllSettings() -> list[str]:
		'''
			
		get the list of all available settings

		Returns:
			list[str]: the pairs of strings, first - option identifier, second - the value, pay attention boolean values are "true" and "false" (like in c++)
		
		'''
		pass # cpp source

	@staticmethod
	def pressButton(button_name: str):
		'''
			
		triger some action in settings

		Args:
			button_name (str): the button name, look the identifier in the listAllSettings() output
		
		'''
		pass # cpp source



class Scene():
	'''
			
		referes the roots of the scene graph
		
	'''

	@staticmethod
	def clearScene(askUser: bool = False):
		'''
			
		clear the whole scene

		Args:
			askUser (bool): set true to ask user for unsaved changes
		
		'''
		pass # cpp source

	@staticmethod
	def current() -> SceneElement:
		'''
			
		returns the current sculpt object

		Returns:
			SceneElement: current object reference
		
		'''
		pass # cpp source

	@staticmethod
	def sculptRoot() -> SceneElement:
		'''
			
		get the root of all sculpt objects

		Returns:
			SceneElement: the root reference
		
		'''
		pass # cpp source

	@staticmethod
	def curvesRoot() -> SceneElement:
		'''
			
		get the root of all curves

		Returns:
			SceneElement: the root reference
		
		'''
		pass # cpp source

	@staticmethod
	def getLayer(name: str, addIfNotExists: bool = True) -> int:
		'''
			
		get the Layer ID by name, add the layer if not exists

		Args:
			name (str): layer name
			addIfNotExists (bool): set true to add layer if it does not exist

		Returns:
			int: layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def getLayerName(LayerID: int) -> str:
		'''
			
		get the layer name

		Args:
			LayerID (int): the layer identifier

		Returns:
			str: the layer name
		
		'''
		pass # cpp source

	@staticmethod
	def setLayerName(LayerID: int, name: str):
		'''
			
		set the layer name

		Args:
			LayerID (int): the layer identifier
			name (str): the new name
		
		'''
		pass # cpp source

	@staticmethod
	def getLayerBlending(LayerID: int) -> int:
		'''
			
		get the layer blending mode

		Args:
			LayerID (int): the layer identifier

		Returns:
			int: the index of blending mode as it is ordered in the Layers UI
		
		'''
		pass # cpp source

	@staticmethod
	def setLayerBlending(LayerID: int, mode: int):
		'''
			
		set the layer blending mode

		Args:
			LayerID (int): the layer identifier
			mode (int): the index of blending mode as it is ordered in the Layers UI
		
		'''
		pass # cpp source

	@staticmethod
	def getCurrentLayer() -> int:
		'''
			
		get current layer identifier

		Returns:
			int: the current layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def setCurrentLayer(LayerID: int):
		'''
			
		set the current layer

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def mergeVisibleLayers():
		'''
			
		merge all visible layers
		
		'''
		pass # cpp source

	@staticmethod
	def mergeLayerDown(LayerID: int):
		'''
			
		merge the layer down

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def applyLayerBlending(LayerID: int):
		'''
			
		apply layer blending

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def invalidateLayer(LayerID: int):
		'''
			
		refresh the layer appearance in scene

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def setActiveLayer(LayerID: int):
		'''
			
		activate the layer

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def removeLayer(LayerID: int):
		'''
			
		remove the layer

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def layerIsEmpty(layerID: int) -> bool:
		'''
			
		Check if the layer is empty

		Args:
			layerID (int): the layer identifier

		Returns:
			bool: true if the layer is empty
		
		'''
		pass # cpp source

	@staticmethod
	def removeEmptyLayers():
		'''
			
		remove all unused layers
		
		'''
		pass # cpp source

	@staticmethod
	def layerVisible(LayerID: int) -> bool:
		'''
			
		return the layer visibility
		
		'''
		pass # cpp source

	@staticmethod
	def setLayerVisibility(LayerID: int, Visible: bool):
		'''
			
		set the layer visibility

		Args:
			Visible (bool): the visibility
		
		'''
		pass # cpp source

	@staticmethod
	def setLayerColorOpacity(LayerID: int, Opacity: float):
		'''
			
		set the layer opacity

		Args:
			LayerID (int): the layer identifier
			Opacity (float): the color opacity
		
		'''
		pass # cpp source

	@staticmethod
	def setLayerDepthOpacity(LayerID: int, Opacity: float):
		'''
			
		set the layer depth opacity

		Args:
			LayerID (int): the layer identifier
			Opacity (float): the depth opacity
		
		'''
		pass # cpp source

	@staticmethod
	def setLayerMetalnessOpacity(LayerID: int, Opacity: float):
		'''
			
		set the layer metalness opacity

		Args:
			LayerID (int): the layer identifier
			Opacity (float): the metalness opacity
		
		'''
		pass # cpp source

	@staticmethod
	def setLayerGlossOpacity(LayerID: int, Opacity: float):
		'''
			
		set the layer gloss/roughness opacity

		Args:
			LayerID (int): the layer identifier
			Opacity (float): the gloss/roughness opacity
		
		'''
		pass # cpp source

	@staticmethod
	def assignLayerMask(LayerID: int) -> int:
		'''
			
		assign the mask to the layer if it is not assigned before

		Args:
			LayerID (int): the layer identifier to assign the mask

		Returns:
			int: the mask identifier
		
		'''
		pass # cpp source

	@staticmethod
	def removeLayerMask(LayerID: int):
		'''
			
		remove the layer mask

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def extractMaskAsLayer(LayerID: int):
		'''
			
		If the layer has the mask attached, the mask will be extracted as a new layer and the masking disabled

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def setMaskForTheLayer(LayerID: int, MaskLayerID: int):
		'''
			
		set the MaskLayerID to be used as mask for the LayerID. The MaskLayerID will disappear among the layers list

		Args:
			LayerID (int): the layer to be masked
			MaskLayerID (int): the mask layer
		
		'''
		pass # cpp source

	@staticmethod
	def enableLayerMask(LayerID: int, enable: bool):
		'''
			
		enable or disable the layer mask

		Args:
			LayerID (int): the layer identifier
			enable (bool): true to enable, false to disable
		
		'''
		pass # cpp source

	@staticmethod
	def isLayerMaskEnabled(LayerID: int) -> bool:
		'''
			
		check if the mask is enabled for the layer

		Args:
			LayerID (int): the layer identifier

		Returns:
			bool: true if masking is enabled and assigned, false if disabled or not assigned
		
		'''
		pass # cpp source

	@staticmethod
	def invertLayerMask(LayerID: int):
		'''
			
		invert the layer mask (if assigned)

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def getLayerMaskLayer(LayerID: int) -> int:
		'''
			
		get the mask identifier assigned to the layer

		Args:
			LayerID (int): the layer identifier

		Returns:
			int: the mask layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def disableLayerMask(LayerID: int):
		'''
			
		disable the mask for the layer

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def enableLayerMask(LayerID: int):
		'''
			
		enable the mask for the layer

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def maskEnabled(LayerID: int) -> bool:
		'''
			
		check if the mask is enabled for the layer

		Args:
			LayerID (int): the layer identifier

		Returns:
			bool: true if enabled, false if disabled of not assigned
		
		'''
		pass # cpp source

	@staticmethod
	def setClippingLayer(LayerID: int):
		'''
			
		set this layer as clipping layer

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def disableClippingLayer(LayerID: int):
		'''
			
		disable the clipping layer

		Args:
			LayerID (int): the layer identifier
		
		'''
		pass # cpp source

	@staticmethod
	def PaintObjectsCount() -> int:
		'''
			
		Get the count of paint objects in scene

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	@staticmethod
	def PaintMaterialCount() -> int:
		'''
			
		Get the count of paint materials

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	@staticmethod
	def PaintUVSetsCount() -> int:
		'''
			
		Get the paint UV-sets (textures) count

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	@staticmethod
	def RemovePaintObject(idx: int):
		'''
			
		Remove the paint object

		Args:
			idx (int): the index of the object
		
		'''
		pass # cpp source

	@staticmethod
	def RemovePaintMaterial(idx: int):
		'''
			
		Remove the paint material

		Args:
			idx (int): the index of the material
		
		'''
		pass # cpp source

	@staticmethod
	def RemoveUVSet(idx: int):
		'''
			
		Remove the UV-set (texture)

		Args:
			idx (int): the index of the UV-set (texture)
		
		'''
		pass # cpp source

	@staticmethod
	def PaintObjectName(idx: int) -> str:
		'''
			
		Get the reference to the object name

		Args:
			idx (int): index of the object

		Returns:
			str: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def PaintMaterialName(idx: int) -> str:
		'''
			
		Get the reference to the material mane

		Args:
			idx (int): the index of the material

		Returns:
			str: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def PaintUVSetName(idx: int) -> str:
		'''
			
		Get the reference to the UV set name

		Args:
			idx (int): the index of the UV set

		Returns:
			str: the reference
		
		'''
		pass # cpp source

	@staticmethod
	def importMesh(filename: str, transform: any = 4) -> SceneElement:
		'''
			
		import mesh into scene, it is the same as File->Import->Import mesh for vertex painting/reference ... This is the optimal way to import mesh into the scene

		Args:
			filename (str): the filename, if it is empty, the dialog appears

		Returns:
			SceneElement: the scene element reference
		
		'''
		pass # cpp source

	@staticmethod
	def ScaleSceneVisually(scale: float):
		'''
			
		Scale the whole scene visually but keep the export size

		Args:
			scale (float): the scale, >1 means objects become bigger in scene
		
		'''
		pass # cpp source

	@staticmethod
	def ScaleSceneUnits(scale: float):
		'''
			
		Keep the scene visial size in scene, but scale the export size

		Args:
			scale (float): the scale, >1 means objects become bigger in export
		
		'''
		pass # cpp source

	@staticmethod
	def GetSceneScale() -> float:
		'''
			
		the length of 1 scene unit when you export the scene

		Returns:
			float: the 1 unit of scene length in the exported model
		
		'''
		pass # cpp source

	@staticmethod
	def GetSceneUnits() -> str:
		'''
			
		get the name of the current scene units

		Returns:
			str: the name as string
		
		'''
		pass # cpp source

	@staticmethod
	def setSceneUnits(units: str) -> bool:
		'''
			
		Set the scene units without actual scaling the scene to new units, just name change

		Args:
			units (str): the name of new units

		Returns:
			bool: false if units are not supported
		
		'''
		pass # cpp source

	@staticmethod
	def getSceneShift() -> any:
		'''
			
		get the scene shift value, look the Edit->Scale master->X,Y,Z
		
		'''
		pass # cpp source

	@staticmethod
	def setSceneShift(shift: any):
		'''
			
		set the scene shift value, look the Edit->Scale master->X,Y,Z

		Args:
			shift : the new shift value
		
		'''
		pass # cpp source

	@staticmethod
	def getAvailableUnits() -> list[str]:
		'''
			
		Get the list of all available units

		Returns:
			list[str]: the list of strings
		
		'''
		pass # cpp source

	@staticmethod
	def convertSceneUnits(destination_unit_name: str) -> bool:
		'''
			
		Convert the scene units to the new units, the scene scale will be changed, visual size will be kept

		Args:
			destination_unit_name (str): the name of new units

		Returns:
			bool: false if units are not supported
		
		'''
		pass # cpp source

	@staticmethod
	def stackUndo(nStack: int):
		'''
			
		Unify several previous undo operations into one

		Args:
			nStack (int): the amount of operations to unify
		
		'''
		pass # cpp source

	@staticmethod
	def resetTexTransform(type: int):
		'''
			
		reset the texture (stencil or material) transform

		Args:
			type (int): 0 - stencil, 1 - material
		
		'''
		pass # cpp source

	@staticmethod
	def scaleTex(type: int, scale: float):
		'''
			
		scale the texture (stencil or material)

		Args:
			type (int): 0 - stencil, 1 - material
			scale (float): the additional scale value
		
		'''
		pass # cpp source

	@staticmethod
	def scaleTexNonUniform(type: int, scale: any):
		'''
			
		scale the texture (stencil or material) non-uniformly

		Args:
			type (int): 0 - stencil, 1 - material
			scale : the 2d scale value
		
		'''
		pass # cpp source

	@staticmethod
	def rotateTex(type: int, angle: float):
		'''
			
		rotate the texture (stencil or material)

		Args:
			type (int): 0 - stencil, 1 - material
			angle (float): the angle in degrees
		
		'''
		pass # cpp source

	@staticmethod
	def moveTex(type: int, offset: any):
		'''
			
		move the texture (stencil or material)

		Args:
			type (int): 0 - stencil, 1 - material
			offset : the offset in 2d (screen plane, pixels)
		
		'''
		pass # cpp source

	@staticmethod
	def flipTexX(type: int):
		'''
			
		flip the texture (stencil or material) horizontally

		Args:
			type (int): 0 - stencil, 1 - material
		
		'''
		pass # cpp source

	@staticmethod
	def flipTexY(type: int):
		'''
			
		flip the texture (stencil or material) vertically

		Args:
			type (int): 0 - stencil, 1 - material
		
		'''
		pass # cpp source

	@staticmethod
	def setTexTiled(type: int, tiled: bool):
		'''
			
		make texture tiled or use single tile

		Args:
			type (int): 0 - stencil, 1 - material
			tiled (bool): the tiled state
		
		'''
		pass # cpp source

	@staticmethod
	def setTexPivot(type: int, pivot: any):
		'''
			
		sep the pivot for the texture (stencil or material)

		Args:
			type (int): 0 - stencil, 1 - material
			pivot : the screen coordinates of the pivot
		
		'''
		pass # cpp source

	@staticmethod
	def getViewportCenter() -> any:
		'''
			
		get the viewport center in screen coordinates

		Returns:
			any: the screen coordinates of the viewport center
		
		'''
		pass # cpp source



class RenderRoom():
	@staticmethod
	def toRenderRoom():
		'''
			
		get to the render room to be able to render
		
		'''
		pass # cpp source

	@staticmethod
	def restartRendering():
		'''
			
		if the realtime render enabled the command will restart the rendering from scratch
		
		'''
		pass # cpp source

	@staticmethod
	def setCustomRenderSize(width: int, height: int):
		'''
			
		set the render output width

		Args:
			width (int): the width
			height (int): the height
		
		'''
		pass # cpp source

	@staticmethod
	def setRenderResult(filename: str):
		'''
			
		set the render output filename

		Args:
			filename (str): the filename
		
		'''
		pass # cpp source

	@staticmethod
	def renderFrame():
		'''
			
		render to the output file
		
		'''
		pass # cpp source

	@staticmethod
	def enableRealtimeRendering(enable: bool):
		'''
			
		enable or disable the realtime rendering

		Args:
			enable (bool): set true to enable
		
		'''
		pass # cpp source

	@staticmethod
	def isRealtimeRenderingEnabled() -> bool:
		'''
			
		get the realtime rendering state

		Returns:
			bool: true if enabled
		
		'''
		pass # cpp source

	@staticmethod
	def setExposure(exposure: float):
		'''
			
		set the exposure value for the rendering (in render room)

		Args:
			exposure (float): the exposure value, usually 0..1, bigger values allowed as well
		
		'''
		pass # cpp source

	@staticmethod
	def getExposure() -> float:
		'''
			
		get the exposure value for the rendering (in render room)

		Returns:
			float: the exposure value, around (0..1)
		
		'''
		pass # cpp source

	@staticmethod
	def setEnvironmentLight(envlight: float):
		'''
			
		set the brightness of the environment light (spherical environment)

		Args:
			envlight (float): the brightness, usually 1
		
		'''
		pass # cpp source

	@staticmethod
	def getEnvironmentLight() -> float:
		'''
			
		get the brightness of the environment light (spherical environment)

		Returns:
			float: the brightness, usually 1
		
		'''
		pass # cpp source

	@staticmethod
	def setDOFDegree(degree: float):
		'''
			
		set the depth of field (DOF) degree

		Args:
			degree (float): the degree of DOF, 0 means no DOF, 1 means full DOF
		
		'''
		pass # cpp source

	@staticmethod
	def getDOFDegree() -> float:
		'''
			
		get the depth of field (DOF) degree

		Returns:
			float: the degree of DOF, 0 means no DOF, 1 means full DOF
		
		'''
		pass # cpp source

	@staticmethod
	def getLightsCount() -> int:
		'''
			
		get the amount of additional directional lighte

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	@staticmethod
	def addLight() -> int:
		'''
			
		add the additional directional light

		Returns:
			int: the index of the light for all further operations
		
		'''
		pass # cpp source

	@staticmethod
	def removeLight(idx: int):
		'''
			
		remove the additional directional light

		Args:
			idx (int): the index of the light
		
		'''
		pass # cpp source

	@staticmethod
	def removeAllLights():
		'''
			
		remove all additional directional lights
		
		'''
		pass # cpp source

	@staticmethod
	def setLightDirection(idx: int, dir: any):
		'''
			
		set the direction for the additional light

		Args:
			idx (int): the index of the light
			dir : the light direction
		
		'''
		pass # cpp source

	@staticmethod
	def getLightDirection(idx: int) -> any:
		'''
			
		get the direction for the additional light

		Args:
			idx (int): the index of the light

		Returns:
			any: the light direction
		
		'''
		pass # cpp source

	@staticmethod
	def setLightScattering(idx: int, scattering: float):
		'''
			
		set the light scattering for the additional light

		Args:
			idx (int): the index of the light
			scattering (float): the light scattering value
		
		'''
		pass # cpp source

	@staticmethod
	def getLightScattering(idx: int) -> float:
		'''
			
		get the light scattering for the additional light

		Args:
			idx (int): the index of the light

		Returns:
			float: the light scattering value
		
		'''
		pass # cpp source

	@staticmethod
	def setLightColor(idx: int, color: any = 3):
		'''
			
		set the light color for the additional light

		Args:
			idx (int): the index of the light
			color : the light color (r,g,b) wintin [0..1] range, if need more intensity, increase the light intensity value
		
		'''
		pass # cpp source

	@staticmethod
	def getLightColor(idx: int) -> any:
		'''
			
		get the light color for the additional light

		Args:
			idx (int): the index of the light

		Returns:
			any: the light color (r,g,b)
		
		'''
		pass # cpp source

	@staticmethod
	def setLightIntensity(idx: int, intensity: float):
		'''
			
		set the light intensity for the additional light

		Args:
			idx (int): the index of the light
			intensity (float): the light intensity value
		
		'''
		pass # cpp source

	@staticmethod
	def getLightIntensity(idx: int) -> float:
		'''
			
		get the light intensity for the additional light

		Args:
			idx (int): the index of the light

		Returns:
			float: the light intensity value
		
		'''
		pass # cpp source

	@staticmethod
	def setRaysPerFrame(count: int):
		'''
			
		set rays per frame for the rendering

		Args:
			count (int): the rays per frame count
		
		'''
		pass # cpp source

	@staticmethod
	def getRaysPerFrame() -> int:
		'''
			
		get rays per frame for the rendering

		Returns:
			int: the rays per frame count
		
		'''
		pass # cpp source

	@staticmethod
	def setAA(AA: bool):
		'''
			
		set the anti-aliasing (AA) rendering state

		Args:
			AA (bool): true to enable
		
		'''
		pass # cpp source

	@staticmethod
	def getAA() -> bool:
		'''
			
		get the anti-aliasing (AA) rendering state

		Returns:
			bool: true if enabled
		
		'''
		pass # cpp source



class Curve(SceneElement):
	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def __init__(self, ob: any):
		pass # CPP source

	def __init__(self, el: SceneElement):
		pass # CPP source

	def __assign__(self, el: SceneElement) -> Curve:
		return super().__assign__(el)

	def pointsCount(self) -> int:
		'''
			
		get the base points cout in the curve

		Returns:
			int: the points count
		
		'''
		pass # cpp source

	def point(self, idx: int) -> any:
		'''
			
		get the base point pointer

		Args:
			idx (int): the index in the points array

		Returns:
			any: the pointer to the point if it is in range, nullptr othervice
		
		'''
		pass # cpp source

	def removePoints(self, index: int, count: int):
		'''
			
		remove the points out of the curve base points list

		Args:
			index (int): the start point index
			count (int): points count to remove
		
		'''
		pass # cpp source

	def curve(self) -> any:
		'''
			
		get the low-level ObjeCurveObject pointer

		Returns:
			any: the OneCurveObject pointer
		
		'''
		pass # cpp source

	def renderPointsCount(self) -> int:
		'''
			
		returns the visual points count. Visual points used to render the curve in the viewport as set of straight lines.

		Returns:
			int: the count
		
		'''
		pass # cpp source

	def renderPoint(self, idx: int) -> any:
		'''
			
		returns the visual point reference

		Args:
			idx (int): the point index

		Returns:
			any: the pointer to the point if it is in range, nullptr othervice
		
		'''
		pass # cpp source

	def updatePoints(self):
		'''
			
		update the visual points if need. Use this function if you cahnge the curve. Change the multiple parameters and then call this function if you need visual points.
		Othervice they will be updated automatically later.
		
		'''
		pass # cpp source

	def closed(self) -> bool:
		'''
			
		returns the reference to the closed state of the curve to get or set the value

		Returns:
			bool: the reference
		
		'''
		pass # cpp source

	def add(self, p: cPy.cTypes.cVec3, normal: cPy.cTypes.cVec3, Radius: float):
		'''
			
		add the point to the curve without the direct options the tangents

		Args:
			p (cVec3): the point in space
			normal (cVec3): the normal to the point
			Radius (float): the point radius
		
		'''
		pass # cpp source

	def addSharp(self, p: cPy.cTypes.cVec3, normal: cPy.cTypes.cVec3, Radius: float):
		'''
			
		add the sharp point to the curve

		Args:
			p (cVec3): the point in space
			normal (cVec3): the normal to the point
			Radius (float): the point radius
		
		'''
		pass # cpp source

	def addSmooth(self, p: cPy.cTypes.cVec3, normal: cPy.cTypes.cVec3, Radius: float):
		'''
			
		add the smooth B-spline-like point to the curve

		Args:
			p (cVec3): the position
			normal (cVec3): the normal
			Radius (float): the radius
		
		'''
		pass # cpp source

	def addBothTangents(self, p: cPy.cTypes.cVec3, normal: cPy.cTypes.cVec3, inTangent: cPy.cTypes.cVec3, outTangent: cPy.cTypes.cVec3, Radius: float):
		'''
			
		add the point with two independent tangents.

		Args:
			p (cVec3): the position
			normal (cVec3): the normal
			inTangent (cVec3): input tangent, it is usually approximately directed from the current to the previous point
			outTangent (cVec3): output tangent, it is usually approximately directed from the current to the next point
			Radius (float): the radius
		
		'''
		pass # cpp source

	def addWithTangent(self, p: cPy.cTypes.cVec3, normal: cPy.cTypes.cVec3, inOutTangent: cPy.cTypes.cVec3, Radius: float):
		'''
			
		add the point with the opposite tangents

		Args:
			p (cVec3): the position
			normal (cVec3): the normal
			inOutTangent (cVec3): the tangent, it is usually approximately directed from the current to the next point
			Radius (float): the radius
		
		'''
		pass # cpp source

	def tubeToMesh(self, mesh: Mesh, hemisphere: bool):
		'''
			
		create the solid tube around the curve using the points radius

		Args:
			mesh (Mesh): this mesh will be created as the result of the operation
			hemisphere (bool): set true if need the ends of the rode to be hemispheres
		
		'''
		pass # cpp source

	def getPoint(self, idx: int) -> list:
		'''
			
		get the point of the curve

		Args:
			idx (int): the point index

		Returns:
			list: the point as tuple (position, normal, tangent1, tangent2, radius)
		
		'''
		pass # cpp source

	def setPointPosition(self, idx: int, p: any):
		'''
			
		set the point position

		Args:
			idx (int): the point index
			p : the position
		
		'''
		pass # cpp source

	def setPointNormal(self, idx: int, n: any):
		'''
			
		set the point normal

		Args:
			idx (int): the point index
			n : the normal
		
		'''
		pass # cpp source

	def setPointTangents(self, idx: int, t1: any, t2: any):
		'''
			
		set the point tangents

		Args:
			idx (int): the point index
			t1 : the first tangent
			t2 : the second tangent
		
		'''
		pass # cpp source

	def setPointRadius(self, idx: int, r: float):
		'''
			
		set the point radius

		Args:
			idx (int): the point index
			r (float): the radius
		
		'''
		pass # cpp source

	def isOpen(self) -> bool:
		'''
			
		check if the curve is open
		
		'''
		pass # cpp source

	def setOpen(self):
		'''
			
		set the curve to be open
		
		'''
		pass # cpp source

	def setClosed(self):
		'''
			
		set the curve to be closed
		
		'''
		pass # cpp source

	def unselectPoints(self):
		'''
			
		unselect all curve points
		
		'''
		pass # cpp source

	def selectPoint(self, idx: int):
		'''
			
		select the curve point

		Args:
			idx (int): the point index
		
		'''
		pass # cpp source

	def fill(self, mesh: Mesh, thickness: float, relax_count: float = 0, details_level: float = 1, extrusion: float = 0):
		'''
			
		Create the curved surface around the curve

		Args:
			mesh (Mesh): the resulting mesh
			thickness (float): the thickness of the object
			relax_count (float): the relaxation degree
			details_level (float): the details levels
			extrusion (float): the additional extrusion
		
		'''
		pass # cpp source



class SphericalCollision():
	'''
			
		The class intended to place spheres in space and identify if there are spheres around. It is important for
		random objects generating and avoiding self-intersection of objects
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, cellsize: float):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def setUnit(self, u: float):
		'''
			
		set the cell size, the cell space should be empty

		Args:
			u (float): the cell size that should be approximately around the average sphere size
		
		'''
		pass # cpp source

	def clear(self):
		'''
			
		remove all spheres
		
		'''
		pass # cpp source

	def addSphere(self, p: any, radius: float) -> int:
		'''
			
		add the sphere into the space

		Args:
			p : the position
			radius (float): the radius

		Returns:
			int: the sphere index, you may refer it later using the spher(index) function
		
		'''
		pass # cpp source

	def collides(self, p: any, radius: float) -> any:
		'''
			
		check if sphere intersects other spheres in the space

		Args:
			p : position
			radius (float): radius

		Returns:
			any: the repelling force, it is zero if no collision happened.
		
		'''
		pass # cpp source

	def sphere(self, idx: int) -> any:
		'''
			
		get the sphere parameters by index

		Args:
			idx (int): the sphere index (previously returned by addSphere)

		Returns:
			any: the position (xyz) and radius (w) as vec4
		
		'''
		pass # cpp source



class ui():
	'''
			
		operate over the Coat's ui
		
	'''

	@staticmethod
	def cmd(id: str, fn: any = None) -> bool:
		'''
			
		execute some action in UI as if you pressed on some control
		
		The ID may be taken from the UI by clicking RMB+MMB, then the ID will appear in the clipboard (look Edit->Prferences->General->Script info type).
		 If the element triggers modal dialog, the execution will be paused till the modal dialog will be closed, but the callback will be called each frame in modal dialog,
		 so you will be able to control what happens in the modal dialog.

		Args:
			id (str): the identifier taken from the UI
			fn : the callback/lambda that will be called each frame till you are within the modal dialog. It looks like\n
		
		::

			def _callback():
			    cmd("#id_to_press")
			    ...code...
			


		Returns:
			bool: True if the element found and the operation executed
		
		'''
		pass # cpp source

	@staticmethod
	def enableWindow(name: str, eflag: bool) -> bool:
		pass # cpp source

	@staticmethod
	def wait(id: str, max_seconds: float) -> bool:
		'''
			
		wait till the element id will appear in the UI. The element will not be clicked. The max wait time is max_seconds.

		Args:
			id (str): The ID we wait to appear
			max_seconds (float): the max wait time (seconds)

		Returns:
			bool: true if the element appeared
		
		'''
		pass # cpp source

	@staticmethod
	def presentInUI(id: str) -> bool:
		'''
			
		Check if the elemnt present in the UI

		Args:
			id (str): the identifier

		Returns:
			bool: true if the element is present
		
		'''
		pass # cpp source

	@staticmethod
	def highlight(id: str, milliseconds: float):
		'''
			
		highlight the UI element for a while

		Args:
			id (str): the ID of the element
			milliseconds (float): the time to highlight, milliseconds
		
		'''
		pass # cpp source

	@staticmethod
	def enablePenChannel(i: int, enabled: bool):
		'''
			
		enable or disable the pen channel

		Args:
			i (int): the channel: 0 - depth, 1 - color, 3 - gloss, 2 - currently unused
			enabled (bool): true to enable
		
		'''
		pass # cpp source

	@staticmethod
	def isEnabledPenChannel(i: int) -> bool:
		'''
			
		check if the pen channel is enabled

		Args:
			i (int): the cannel: 0 - depth, 1 - color, 3 - gloss, 2 - currently unused

		Returns:
			bool: true if the channel is enabled
		
		'''
		pass # cpp source

	@staticmethod
	def setSliderValue(id: str, value: float) -> bool:
		'''
			
		Set the value for the the slider (if exists in UI)

		Args:
			id (str): the ID of the element
			value (float): the value to set

		Returns:
			bool: true if successful
		
		'''
		pass # cpp source

	@staticmethod
	def getSliderValue(id: str) -> float:
		'''
			
		get the value of the slider

		Args:
			id (str): the ID of the element

		Returns:
			float: the value
		
		'''
		pass # cpp source

	@staticmethod
	def setEditBoxValue(id: str, value: str) -> bool:
		'''
			
		set the edit box value

		Args:
			id (str): the ID of the element
			value (str): the value to set

		Returns:
			bool: true if the element exists
		
		'''
		pass # cpp source

	@staticmethod
	def setEditBoxValue(id: str, value: int) -> bool:
		'''
			
		set the edit box value

		Args:
			id (str): the ID of the element
			value (int): the value to set

		Returns:
			bool: true if the element exists
		
		'''
		pass # cpp source

	@staticmethod
	def setEditBoxValue(id: str, value: float) -> bool:
		'''
			
		set the edit box value

		Args:
			id (str): the ID of the element
			value (float): the value to set

		Returns:
			bool: true if the element exists
		
		'''
		pass # cpp source

	@staticmethod
	def getEditBoxValue(id: str, result: any) -> bool:
		'''
			
		get the edit box value

		Args:
			id (str): the ID of the element
			result : the string the will get the result

		Returns:
			bool: true if the element exists
		
		'''
		pass # cpp source

	@staticmethod
	def getEditBoxValue(id: str) -> str:
		pass # cpp source

	@staticmethod
	def apply():
		'''
			
		pess ENTER, acts as Apply usually
		
		'''
		pass # cpp source

	@staticmethod
	def setFileForFileDialog(filename: str):
		'''
			
		Set the file for the next file dialog that will be triggered by user.
		If you will use coat::ui:cmd(...) to trigger some command that shows the file dialog
		this command allows to substitute the filename for that dialog instead of showing the dialog.
		This acts only for ONE next dialog.

		Args:
			filename (str): the filename to substitute.
		
		'''
		pass # cpp source

	@staticmethod
	def getBoolField(id: str) -> bool:
		'''
			
		Get the bool field from the checkbox in UI

		Args:
			id (str): the element identifier

		Returns:
			bool: the checkbox value
		
		'''
		pass # cpp source

	@staticmethod
	def setBoolValue(id: str, value: bool) -> bool:
		'''
			
		Set the value for the checkbox in UI

		Args:
			id (str): the element identifier
			value (bool): the value to set

		Returns:
			bool: true if successful and the element exists
		
		'''
		pass # cpp source

	@staticmethod
	def currentRoom() -> str:
		'''
			
		get the current room name

		Returns:
			str: the name
		
		'''
		pass # cpp source

	@staticmethod
	def isInRoom(name: str) -> bool:
		'''
			
		check if we are in the specified room

		Args:
			name (str): the room name to check

		Returns:
			bool: true if we are in that room
		
		'''
		pass # cpp source

	@staticmethod
	def toRoom(name: str, Force: bool = False):
		'''
			
		switch to the room

		Args:
			name (str): the room name. Pay attention, you may pass the name or identifier, but name has bigger priory.
			Force (bool): set true to switch even if we are in the tool that corresponds to the destination room
		
		'''
		pass # cpp source

	@staticmethod
	def roomsCount() -> int:
		'''
			
		returns the rooms count

		Returns:
			int: the number
		
		'''
		pass # cpp source

	@staticmethod
	def roomName(index: int) -> str:
		'''
			
		get the room name by index

		Args:
			index (int): the room index

		Returns:
			str: "" if index outside the range or the room name if the index is valid
		
		'''
		pass # cpp source

	@staticmethod
	def roomID(index: int) -> str:
		'''
			
		get the text identifier of the room

		Args:
			index (int): the room index

		Returns:
			str: "" if index outside the range or the room identifier if the index is valid
		
		'''
		pass # cpp source

	@staticmethod
	def toolParam(B: cPy.cCore.BaseClass):
		'''
			
		show the class B as the part of the tools params panel

		Args:
			B (BaseClass): the class pointer
		
		'''
		pass # cpp source

	@staticmethod
	def removeToolParam(B: cPy.cCore.BaseClass = None):
		'''
			
		remove the class from the tools params

		Args:
			B (BaseClass): the class pointer
		
		'''
		pass # cpp source

	@staticmethod
	def getOption(id: str) -> str:
		'''
			
		get the option from preferences

		Args:
			id (str): the identifier of english text of the option

		Returns:
			str: the value as string
		
		'''
		pass # cpp source

	@staticmethod
	def setOption(id: str, value: str) -> bool:
		'''
			
		set the value to preferences

		Args:
			id (str): the value identifier or english text
		
		'''
		pass # cpp source

	@staticmethod
	def setOption(id: str, value: bool) -> bool:
		pass # cpp source

	@staticmethod
	def setOption(id: str, value: float) -> bool:
		pass # cpp source

	@staticmethod
	def hideDontShowAgainMessage(id: str):
		'''
			
		Hides the "Don't show again dialog" for the current session (not forever)

		Args:
			id (str): the identifier, for example "AttachTextureHint", look the currently hidden list as files names in Docs/3DCoat/data/Temp/*.dontshow
		
		'''
		pass # cpp source

	@staticmethod
	def showInfoMessage(infoID: str, milliseconds: int):
		'''
			
		Show the floating information message for the some time period

		Args:
			infoID (str): the message or message identifier (from language files)
			milliseconds (int): how ling to display the message
		
		'''
		pass # cpp source

	@staticmethod
	def insertInMenu(Menu: str, ID_in_menu: str, script_path: str):
		'''
			
		Insert the scripted command into the main menu

		Args:
			Menu (str): One of main menu items, look the list in Documents/3DCoat/UserPrefs/Scripts/ExtraMenuItems/menu_sections.txt
			ID_in_menu (str): the ID of the command in the menu, it is the english text or the identifier of the command
			script_path (str): the full or relative path to the script file, if relative, it is relative to the 3DCoat root folder
		If it comes without path, it is assumed to be in same folder as the script that calls this function. If this parameter is empty,
		this script will be called.
		
		'''
		pass # cpp source

	@staticmethod
	def insertInToolset(roomID: str, section: str, toolID: str, script_path: str = ""):
		'''
			
		Insert the script-based tool into the toolset

		Args:
			roomID (str): the room identifier, same as folders names in Documents/3DCoat/UserPrefs/Rooms/CustomRooms/
			section (str): the section name. This string may be empty to add beyond sections (anyway, at the end) or in any existing section.
		To get section name, pres RMB+MMB over the section name in the toolset. You will get something like "*Adjust" in the clipboard.
		The "Adjust" in this case is the section name.
			toolID (str): the tool identifier, how it will appear in UI. You may provide the text for the identifier using the addTranslation(...)
		Also, if there is image in the data/Textures/icons64/ named as toolID.png, it will be used as the icon for the tool.
			script_path (str): the full or relative path to the script file, if relative, it is relative to the 3DCoat root folder
		If it comes without path, it is assumed to be in same folder as the script that calls this function. If this parameter is empty,
		this script will be called.
		
		'''
		pass # cpp source

	@staticmethod
	def removeCommandFromMenu(ID_in_menu: str):
		'''
			
		remove the command from the menu

		Args:
			ID_in_menu (str): the ID of the command in the menu, it is the english text or the identifier of the command
		
		'''
		pass # cpp source

	@staticmethod
	def checkIfMenuItemInserted(ID_in_menu: str) -> bool:
		'''
			
		Check if the command inserted somewhere into the menu

		Args:
			ID_in_menu (str): the ID of the command in the menu, look the list in C:/Users\andre\OneDrive\Documents\3DCoat/UserPrefs\Scripts\ExtraMenuItems\menu_sections.txt it is the english text or the identifier of the command

		Returns:
			bool: true if the command is inserted
		
		'''
		pass # cpp source

	@staticmethod
	def addExtension(roomID: str, section: str, obj: any):
		'''
			
		Add the extension (new tool) into the room. Look the \ref GeneratorExample.py

		Args:
			roomID (str): roomID the room identifier, same as folders names in Documents/3DCoat/UserPrefs/Rooms/CustomRooms/
			section (str): section the section name. This string may be empty to add beyond sections (anyway, at the end) or in any existing section.
		To get section name, pres RMB+MMB over the section name in the toolset. You will get something like "*Adjust" in the clipboard.
		The "Adjust" in this case is the section name.
			obj : the object that contains the extension. Look the \ref GeneratorExample.py
		
		'''
		pass # cpp source

	@staticmethod
	def checkIfExtensionPresent(extension_ID: str) -> bool:
		'''
			
		Check if extension named as extension_ID is present in the 3DCoat

		Args:
			extension_ID (str): the identifier of the extension

		Returns:
			bool: True if the extension installed
		
		'''
		pass # cpp source

	@staticmethod
	def addTranslation(id: str, text: str):
		'''
			
		Add the translation for the text identifier

		Args:
			id (str): the identifier
			text (str): the translation
		
		'''
		pass # cpp source

	@staticmethod
	def getIdTranslation(id: str) -> str:
		'''
			
		Get the translation for the text identifier

		Args:
			id (str): the text identifier

		Returns:
			str: the translation or the id
		
		'''
		pass # cpp source

	@staticmethod
	def getCurrentLanguage() -> str:
		'''
			
		Get the current language file name (without the XML extension)

		Returns:
			str: the language file name (without the XML extension)
		
		'''
		pass # cpp source

	@staticmethod
	def switchToLanguage(language: str):
		'''
			
		Switch the layout to the language

		Args:
			language (str): the language identifier, actually it is the file name (withot the XML extension) in the data/Languages/ folder
		
		'''
		pass # cpp source

	@staticmethod
	def scale() -> float:
		'''
			
		returns the scale in comparison to the smallest UI theme

		Returns:
			float: the scale factor > 1
		
		'''
		pass # cpp source

	@staticmethod
	def inputString(text: str, min_length: int = 0) -> str:
		'''
			
		input text under the mouse position

		Args:
			text (str): the initial text value
			min_length (int): the minimal width of the input field, if zero passed the width taken from the parent control (if exists)

		Returns:
			str: the changed text (if the user pressed OK) or the initial text other vice.
		
		'''
		pass # cpp source

	@staticmethod
	def stopNomodal():
		pass # cpp source

	@staticmethod
	def nomodalInputActive() -> bool:
		pass # cpp source

	@staticmethod
	def getInputPixelsHeight() -> int:
		pass # cpp source

	@staticmethod
	def inputInt(initial_value: int) -> int:
		'''
			
		input the integer value under the mouse position

		Args:
			initial_value (int): the initial integer value

		Returns:
			int: the changed value (if the user pressed OK) or the initial value other vice.
		
		'''
		pass # cpp source

	@staticmethod
	def inputFloat(initial_value: float) -> float:
		'''
			
		inputh the float value under the mouse position

		Args:
			initial_value (float): the initial float value

		Returns:
			float: the changed value (if the user pressed OK) or the initial value other vice.
		
		'''
		pass # cpp source



class Camera():
	@staticmethod
	def rotateToGradually(destination_dir: any):
		'''
			
		align the camera along the view

		Args:
			destination_dir : the view direction
		
		'''
		pass # cpp source

	@staticmethod
	def getForward() -> any:
		'''
			
		get the forward direction

		Returns:
			any: the direction
		
		'''
		pass # cpp source

	@staticmethod
	def getUp() -> any:
		'''
			
		get the camera up direction

		Returns:
			any: the direction
		
		'''
		pass # cpp source

	@staticmethod
	def getRight() -> any:
		'''
			
		get the camera right direction

		Returns:
			any: the direction
		
		'''
		pass # cpp source

	@staticmethod
	def isOrtho() -> bool:
		'''
			
		return true if the camera is in the ortho mode

		Returns:
			bool: the ortho mode state
		
		'''
		pass # cpp source

	@staticmethod
	def setOrtho(ortho: bool):
		'''
			
		switch the camera to the ortho or perspective mode

		Args:
			ortho (bool): set true if need ortho mode, false if need perspective mode
		
		'''
		pass # cpp source

	@staticmethod
	def getPivot() -> any:
		'''
			
		get the camera pivot position

		Returns:
			any: the position
		
		'''
		pass # cpp source

	@staticmethod
	def setPivot(pivot: any):
		'''
			
		set the camera pivot position

		Args:
			pivot : the pivot position
		
		'''
		pass # cpp source

	@staticmethod
	def getPosition() -> any:
		'''
			
		get the camera position

		Returns:
			any: the camera position
		
		'''
		pass # cpp source

	@staticmethod
	def getWorldToScreenSpace(world_pos: any) -> any:
		'''
			
		convert the world position to the screen position

		Args:
			world_pos : the world position

		Returns:
			any: the screen position
		
		'''
		pass # cpp source

	@staticmethod
	def getScreenToWorldSpace(screen_pos: any) -> any:
		'''
			
		convert the screen position to the world position

		Args:
			screen_pos : the screen position (pass z that you got using getWorldToScreenSpace)

		Returns:
			any: the world position
		
		'''
		pass # cpp source

	@staticmethod
	def setCamera(position: any, lookAt: any, fovY: float, up: any = 3):
		pass # cpp source



class dialog():
	'''
			
		the rich dialog. You may customize it, show your custom parameters and custom buttons.
		
	'''

	def __init__(self):
		pass # CPP source

	def text(self, id: str) -> dialog:
		'''
			
		pass the header text of the dialog

		Args:
			id (str): the text or text identifier that will be used to take the text from the language file. You may press F9 to localize it in UI.

		Returns:
			dialog: the reference to pass multiple options at chain.
		
		'''
		pass # cpp source

	def caption(self, id: str) -> dialog:
		'''
			
		pass the caption of the dialog

		Args:
			id (str): id the caption or caption identifier that will be used to take the text from the language file. You may press F9 to localize it in UI.

		Returns:
			dialog: the chain ref
		
		'''
		pass # cpp source

	def width(self, w: int) -> dialog:
		'''
			
		change the default width

		Args:
			w (int): the width will be scaled in correspondence with the font size, so you may pass absolute values like 500

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def modal(self) -> dialog:
		'''
			
		dialog will be modal. Generally, it is modal by default. Execution will be paused at show() till the user will press any dialog button.

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def noModal(self) -> dialog:
		'''
			
		dialog will be no modal. Execution will continue after you will call the show()
		
		'''
		pass # cpp source

	def buttons(self, list: str) -> dialog:
		'''
			
		pass the list of buttons for the dialog

		Args:
			list (str): list of buttons. |, .+; may be used as separators between identifiers

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def topRight(self) -> dialog:
		'''
			
		place the dialog at the top-right position of the viewport

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def ok(self) -> dialog:
		'''
			
		add Ok button

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def cancel(self) -> dialog:
		'''
			
		add Cancel button

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def yes(self) -> dialog:
		'''
			
		add Yes button

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def no(self) -> dialog:
		'''
			
		add No button

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def warn(self) -> dialog:
		'''
			
		add Warning icon

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def question(self) -> dialog:
		'''
			
		add Question icon

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def undoWorks(self) -> dialog:
		'''
			
		allow undo (CTR-Z) act even in modal dialog

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def transparentBackground(self) -> dialog:
		'''
			
		the background will not be faded

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	@staticmethod
	def fadeDialogsBackground() -> bool:
		'''
			
		returns the reference to the global property - fade modal dialogs background (true) or not (false)

		Returns:
			bool: the property reference
		
		'''
		pass # cpp source

	def dontShowAgainCheckbox(self) -> dialog:
		'''
			
		show the checkbox "Don't show again". If user checks if the dialog will net be shown next time and show() will return 0 immediately.

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def params(self, params: cPy.cCore.BaseClass) -> dialog:
		'''
			
		The important core feature. BaseClass allows to create the custom controls in the dialog. Look the dialog example to understand how to use it.

		Args:
			params (BaseClass): the pointer to the class derived from the BaseClass

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def params(self, params: any) -> dialog:
		'''
			
		The important core feature. Pass the object to display object parameters in UI. Look the dialog example to understand how to use it.

		Args:
			params : the class reference

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def process(self, callback: any) -> dialog:
		'''
			
		pass the function/lambda that will be called each frame.

		Args:
			callback : the callback/lambda called each frame within the dialog

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def onPress(self, press: any) -> dialog:
		'''
			
		pass the function/lambda that will be called when the button will be pressed. The button index (starts from 1) will be passed to the function

		Args:
			press : the callback/lambda

		Returns:
			dialog: itself
		
		'''
		pass # cpp source

	def show(self) -> int:
		'''
			
		Show the dialog. This is usually the last command in the chain.

		Returns:
			int: the button index. First button in the list has index 1
		
		'''
		pass # cpp source

	def widget(self, w: any) -> dialog:
		pass # cpp source



class resource():
	'''
			
		this class represents different resources accessible in UI - alphas, strips, materials, models, etc
		
	'''

	def __init__(self, id: str):
		pass # CPP source

	@staticmethod
	def listAllResourcesTypes() -> list[str]:
		'''
			
		list all available resources types

		Returns:
			list[str]: the list of resource types (any type may be passed to the resource constructor)
		
		'''
		pass # cpp source

	def listFolders(self) -> list[str]:
		'''
			
		list folders of the resource type referred by this object

		Returns:
			list[str]: the list of folders (short names without the full path)
		
		'''
		pass # cpp source

	def currentFolder(self) -> str:
		'''
			
		get the current folder short name

		Returns:
			str: the name of current folder of the resource type referred by this object
		
		'''
		pass # cpp source

	def currentFolderFullPath(self) -> str:
		'''
			
		full path (relative to the 3DCoat's documents) to the current folder files

		Returns:
			str: the path
		
		'''
		pass # cpp source

	def rootPath(self) -> str:
		'''
			
		the root path (relative to the 3DCoat's documents) to the resource type referred by this object

		Returns:
			str: the path
		
		'''
		pass # cpp source

	def supportedExtensions(self) -> list[str]:
		'''
			
		get the list of supported extensions for the resource type referred by this object

		Returns:
			list[str]: the list of strings with extensions
		
		'''
		pass # cpp source

	def setCurrentFolder(self, folder: str):
		'''
			
		set the current folder (short name without the full path)

		Args:
			folder (str): the folder name
		
		'''
		pass # cpp source

	def createFolder(self, folderName: str):
		'''
			
		create the folder and switch there

		Args:
			folderName (str): the folder name
		
		'''
		pass # cpp source

	def removeFolder(self, folderName: str):
		'''
			
		remove the folder and switch to the root folder if this is the current folder

		Args:
			folderName (str): the folder name
		
		'''
		pass # cpp source

	def listCurrentFolderItems(self) -> list[str]:
		'''
			
		get the list of all items in the current folder

		Returns:
			list[str]: the list of items (usually long names with the relative path)
		
		'''
		pass # cpp source

	def addItem(self, itemPath: str):
		'''
			
		add the item to the current folder

		Args:
			itemPath (str): the path to the item (full or relative to the 3DCoat's documents)
		
		'''
		pass # cpp source

	def removeItem(self, itemName: str):
		'''
			
		remove the item from the current folder

		Args:
			itemName (str): the item name as it is returned by listCurrentFolderItems()
		
		'''
		pass # cpp source

	def selectItem(self, itemName: str):
		'''
			
		select/activate the item in the current folder

		Args:
			itemName (str): the item name as it is returned by listCurrentFolderItems()
		
		'''
		pass # cpp source

	def moveItemToFolder(self, itemName: str, destFolderName: str):
		'''
			
		move the item to another folder

		Args:
			itemName (str): the item name as it is returned by listCurrentFolderItems()
			destFolderName (str): the short name of the destination folder
		
		'''
		pass # cpp source

	def getCurrentItem(self) -> str:
		'''
			
		returns the current item name (if possible)

		Returns:
			str: the string, current item name
		
		'''
		pass # cpp source



class io():
	'''
			
		General I/O access
		
	'''

	@staticmethod
	def installPath() -> str:
		'''
			
		the 3DCoat installation path

		Returns:
			str: the path
		
		'''
		pass # cpp source

	@staticmethod
	def dataPath() -> str:
		'''
			
		the 3DCoat data path

		Returns:
			str: the path
		
		'''
		pass # cpp source

	@staticmethod
	def documents(path: str) -> str:
		'''
			
		convert the relative path to the path in documents, if the path is absolute, just return the original path

		Args:
			path (str): the relative or absolute path

		Returns:
			str: the absolute path in user documents
		
		'''
		pass # cpp source

	@staticmethod
	def fileExists(path: str) -> bool:
		'''
			
		check if file exists

		Args:
			path (str): the path may be full or relative. If it is relative, the documents will be
		checked first, the the install folder will be checked for file.

		Returns:
			bool: true if the file exists
		
		'''
		pass # cpp source

	@staticmethod
	def copyFile(src: str, dest: str):
		'''
			
		copy the file from src to dest. If the src or dest is relative, it is relative to the documents folder. This function works correctly with relative paths, so it is recommended over the standard copy files routine.

		Args:
			src (str): the source filename
			dest (str): the destination filename
		
		'''
		pass # cpp source

	@staticmethod
	def copyFolder(src: str, dest: str):
		'''
			
		copy the whole folder from src to dest. If the src or dest is relative, it is relative to the documents folder. This function works correctly with relative paths, so it is recommended over the standard copy folder routine.

		Args:
			src (str): the source folder
			dest (str): the destination folder
		
		'''
		pass # cpp source

	@staticmethod
	def removeFile(filename: str):
		'''
			
		remove the file. If the filename is relative, it is relative to the documents folder. If the path is in install folder, the corresponding file in documents will be removed.
		Files in the install folder can't be removed.

		Args:
			filename (str): the file path
		
		'''
		pass # cpp source

	@staticmethod
	def removeFolder(folder: str):
		'''
			
		remove the folder. If the folder is relative, it is relative to the documents folder. If the path is in install folder, the corresponding folder in documents will be removed.

		Args:
			folder (str): the path to the folder
		
		'''
		pass # cpp source

	@staticmethod
	def toFullPathInDataFolder(path: str) -> str:
		'''
			
		convert the relative path to full path in documents folder. If the path is full and placed
		in the install folder, it will be converted to path in documents.

		Args:
			path (str): the path

		Returns:
			str: the fill path in documents
		
		'''
		pass # cpp source

	@staticmethod
	def toFullPathInDataFolder(path: any):
		pass # cpp source

	@staticmethod
	def toFullPathInInstallFolder(path: str) -> str:
		'''
			
		convert the relative path to the full path in the install folder.
		If the path is full, it remains untouched.

		Args:
			path (str): the relative path

		Returns:
			str: the full path in the install folder
		
		'''
		pass # cpp source

	@staticmethod
	def toFullPathInInstallFolder(path: any):
		pass # cpp source

	@staticmethod
	def convertToWritablePath(path: str) -> str:
		'''
			
		If the path is relative or points into some file in the install folder, it will be converted to the path in documents folder.

		Args:
			path (str): the path (full or relative)

		Returns:
			str: the write-able path
		
		'''
		pass # cpp source

	@staticmethod
	def convertToWritablePath(path: any):
		pass # cpp source

	@staticmethod
	def convertToWritablePathIfFileExists(path: str) -> str:
		'''
			
		If the path is relative or points into some file in the install folder, it will be converted to the path in documents folder.
		If the does not exist in the documents folder, but exists in the install folder, the resulting path will be in the install folder.

		Args:
			path (str): the path (full or relative)

		Returns:
			str: the path
		
		'''
		pass # cpp source

	@staticmethod
	def convertToWritablePathIfFileExists(path: any):
		pass # cpp source

	@staticmethod
	def getExtension(filepath: str) -> str:
		'''
			
		get the file extension (without .)

		Args:
			filepath (str): the file path - full or relative

		Returns:
			str: the extension
		
		'''
		pass # cpp source

	@staticmethod
	def getFileName(filepath: str) -> str:
		'''
			
		get the file name from the path

		Args:
			filepath (str): the full or relative path

		Returns:
			str: the filename without the path
		
		'''
		pass # cpp source

	@staticmethod
	def getFilePath(filepath: str) -> str:
		'''
			
		get the file path without the filename

		Args:
			filepath (str): the filepath

		Returns:
			str: the path that always ends with '/'
		
		'''
		pass # cpp source

	@staticmethod
	def getFileNameWithoutExtension(filepath: str) -> str:
		'''
			
		remove the file extension from the filename

		Args:
			filepath (str): the file name

		Returns:
			str: the filename without extension
		
		'''
		pass # cpp source

	@staticmethod
	def strFromFile(filename: str) -> str:
		'''
			
		read string from file.

		Args:
			filename (str): The path. If it is relative, it is relative to the documents folder.
		If there is no file, it will be taken from the install folder.

		Returns:
			str: true if file read succesful
		
		'''
		pass # cpp source

	@staticmethod
	def strToFile(text: str, filename: str):
		'''
			
		write the string to file

		Args:
			text (str): the text to save
			filename (str): The path. If it is relative, it is relative to the documents folder.
		
		'''
		pass # cpp source

	@staticmethod
	def getFileSize(filename: str) -> int:
		'''
			
		get the file size

		Args:
			filename (str): the filename, relative or full

		Returns:
			int: the file size
		
		'''
		pass # cpp source

	@staticmethod
	def cursorPos() -> any:
		'''
			
		returns the current cursor position

		Returns:
			any: the 2d vector
		
		'''
		pass # cpp source

	@staticmethod
	def snappedCursorPos() -> any:
		'''
			
		returns the snapped cursor position

		Returns:
			any: the 2d vector
		
		'''
		pass # cpp source

	@staticmethod
	def wholeScreen() -> any:
		'''
			
		get the whole screen rectangle

		Returns:
			any: the rectangle, top-left is (0,0)
		
		'''
		pass # cpp source

	@staticmethod
	def workArea() -> any:
		'''
			
		get the work area rectangle

		Returns:
			any: the rectangle, top-left is (0,0)
		
		'''
		pass # cpp source

	@staticmethod
	def progressBar(stage: float, max_stage: float, message: str):
		'''
			
		Show the progress bar

		Args:
			stage (float): the current stage
			max_stage (float): the maximal stage
			message (str): the text to display
		
		'''
		pass # cpp source

	@staticmethod
	def progressBarInWindowHeader(stage: float, max_stage: float, message: str):
		'''
			
		Show the progress bar only in the 3DCoat's window header

		Args:
			stage (float): the current stage
			max_stage (float): the maximal stage
			message (str): the text to display
		
		'''
		pass # cpp source

	@staticmethod
	def setWindowTitle(text: str, seconds: float):
		'''
			
		Override the 3DCoat's window title for some amount of time

		Args:
			text (str): the text to show
			seconds (float): the seconds to stay in title
		
		'''
		pass # cpp source

	@staticmethod
	def step(count: int = 1):
		'''
			
		perform rendering cycles

		Args:
			count (int): amount of cycles
		
		'''
		pass # cpp source

	@staticmethod
	def exec(command: str, arguments: str = None):
		'''
			
		execute command. It may be exe file, URL, batch command

		Args:
			command (str): the command to execute
			arguments (str): optional command line arguments
		
		'''
		pass # cpp source

	@staticmethod
	def execAndWait(command: str, arguments: str = None) -> str:
		'''
			
		execute and wait till finished, the console output will be returned as string

		Args:
			command (str): the command to execute
			arguments (str): optional arguments

		Returns:
			str: the console output of the executed program
		
		'''
		pass # cpp source

	@staticmethod
	def updateCoatPyi(folderOrFile: str):
		'''
			
		update the .pyi file for the given folder or py file

		Args:
			folderOrFile (str): the full or relative path to the folder or py file
		
		'''
		pass # cpp source

	@staticmethod
	def ListFiles(folder: str, mask: str, recursive: bool = True) -> list[str]:
		'''
			
		list files in the folder

		Args:
			folder (str): the start folder. It may be absolute or relative to 3DCoat documents/install folder.
			mask (str): the seek mask (wildcards)
			recursive (bool): set true if recursive

		Returns:
			list[str]: result the files list
		
		'''
		pass # cpp source

	@staticmethod
	def ListFolders(startFolder: str) -> list[str]:
		'''
			
		list folders within the folder, non-recursive, just plain list

		Args:
			startFolder (str): the start folder

		Returns:
			list[str]: the resulting list
		
		'''
		pass # cpp source

	@staticmethod
	def supportedImagesFormats() -> str:
		'''
			
		returns the currently supported mesh export formats

		Returns:
			str: the list like "*.obj;*.fbx;..."
		
		'''
		pass # cpp source

	@staticmethod
	def supportedMeshesFormats() -> str:
		'''
			
		returns the list of supported images formats

		Returns:
			str: the list like "*.png;*.jpg;..."
		
		'''
		pass # cpp source

	@staticmethod
	def openFileDialog(extensions: str, fileName: any) -> bool:
		'''
			
		show the file dialog

		Args:
			extensions (str): the list of supported extensions like *.txt;*.dat; etc...
			fileName : the resulting filename

		Returns:
			bool: true if user chosen the file successfully
		
		'''
		pass # cpp source

	@staticmethod
	def openFileDialog(extensions: str) -> str:
		pass # cpp source

	@staticmethod
	def openFilesDialog(extensions: str) -> list[str]:
		'''
			
		open multiple files dialog

		Args:
			extensions (str): the list of supported extensions like *.txt;*.dat; etc...

		Returns:
			list[str]: the resulting filenames list
		
		'''
		pass # cpp source

	@staticmethod
	def saveFileDialog(extensions: str, fileName: any) -> bool:
		'''
			
		show the save file dialog

		Args:
			extensions (str): extensions the list of supported extensions like *.txt;*.dat; etc...
			fileName : the resulting filename

		Returns:
			bool: true if user chosen the file successfully
		
		'''
		pass # cpp source

	@staticmethod
	def saveFileDialog(extensions: str) -> str:
		pass # cpp source

	@staticmethod
	def currentSceneFilepath() -> str:
		'''
			
		returns the current scene filename, empty if the scene was not saved/opened
		
		'''
		pass # cpp source

	@staticmethod
	def pipInstall(requirements: str):
		'''
			
		install one or multiple python packages

		Args:
			requirements (str): the list of packages to install, this is all what you write after "pip install"
		
		'''
		pass # cpp source

	@staticmethod
	def pipUninstall(requirements: str):
		pass # cpp source

	@staticmethod
	def pythonPath() -> str:
		'''
			
		get the python libraries folder

		Returns:
			str: the path
		
		'''
		pass # cpp source

	@staticmethod
	def showPythonConsole():
		'''
			
		Show the python console, clear it and pop up
		
		'''
		pass # cpp source

	@staticmethod
	def executeScript(path: str):
		'''
			
		execute python (.py file) or angelscript (c++ like), or CoreAPI (native C++) script

		Args:
			path (str): the full or relative path to the script file
		
		'''
		pass # cpp source

	@staticmethod
	def installRequirements(path_to_requirements_txt: str):
		'''
			
		Install all the requirements for the python script execution

		Args:
			path_to_requirements_txt (str): te full or relative path to the requirements.txt
		
		'''
		pass # cpp source

	@staticmethod
	def toJson(obj: any, filename: str = "") -> str:
		'''
			
		Store the object to the file or string as json

		Args:
			obj : the python object reference
			filename (str): the filename to save, if empty, the string will be returned

		Returns:
			str: the string that contains json data
		
		'''
		pass # cpp source

	@staticmethod
	def fromJsonFile(obj: any, filename: str):
		'''
			
		Restore the object from the json file

		Args:
			obj : the object to restore
			filename (str): the path to the json file, full or relative
		
		'''
		pass # cpp source

	@staticmethod
	def restoreObjectFormJsonString(obj: any, data: str):
		'''
			
		Restore the object from the json string

		Args:
			obj : the object to restore
			data (str): the json string
		
		'''
		pass # cpp source

	@staticmethod
	def createRedistributablePackageFromFolder(folder: str, package_name: str, excluded_folders_names: str = "", excluded_extensions: str = ""):
		'''
			
		Create the 3dcpack file from the folder placed in Documents

		Args:
			folder (str): the folder to pack, it should be relative to the 3DCoat's Documents folder
			package_name (str): the package name, the extension is .3dcpack
			excluded_folders_names (str): the folders names to be excluded from the package, separated by semicolon
			excluded_extensions (str): the file extensions to be excluded from the package, separated by semicolon
		
		'''
		pass # cpp source

	@staticmethod
	def getDownloadProgress() -> int:
		'''
			
		returns the overall download progress

		Returns:
			int: the progress in percents
		
		'''
		pass # cpp source

	@staticmethod
	def listBlenderInstallFolders() -> list[str]:
		'''
			
		list the blender install folders

		Returns:
			list[str]: the list of the blender install folders
		
		'''
		pass # cpp source

	@staticmethod
	def saveScreenshot(filename: str, x: int = 0, y: int = 0, width: int = 0, height: int = 0):
		'''
			
		save the screenshot to the file

		Args:
			filename (str): the filename
			x (int): the x coordinate of the screenshot
			y (int): the y coordinate of the screenshot
			width (int): the width of the screenshot, if 0 all to the right will be captured
			height (int): the height of the screenshot, if 0 all to the bottom will be captured
		
		'''
		pass # cpp source

	@staticmethod
	def removeBackground(image1: str, image2: str, result: str):
		pass # cpp source

	@staticmethod
	def ppp(filename: str):
		'''
			
		Opens model for PPP, if path is empty, shows open dialog

		Args:
			filename (str): the filename
		
		'''
		pass # cpp source



class utils():
	@staticmethod
	def dwordToVec4(d: int) -> any:
		'''
			
		convert DWORD (unsigned int) to vec4

		Args:
			d (int): the DWORD (unsigned int)

		Returns:
			any: the 4d vector
		
		'''
		pass # cpp source

	@staticmethod
	def vec4ToDword(v: any) -> any:
		'''
			
		convert vec4 to DWORD (unsigned int)

		Args:
			v : the 4d vector

		Returns:
			any: the DWORD (unsigned int)
		
		'''
		pass # cpp source

	@staticmethod
	def randomize(seed: int):
		'''
			
		set the random seed for all further random value generation

		Args:
			seed (int): the seed
		
		'''
		pass # cpp source

	@staticmethod
	def random01() -> float:
		'''
			
		get the random value 0..1

		Returns:
			float: the random value
		
		'''
		pass # cpp source

	@staticmethod
	def random(min: float, max: float) -> float:
		'''
			
		get the random value in range

		Args:
			min (float): low bound
			max (float): high bound

		Returns:
			float: the random value
		
		'''
		pass # cpp source

	@staticmethod
	def randomNormal() -> any:
		'''
			
		get the normalized random vector

		Returns:
			any: the 3d random vector
		
		'''
		pass # cpp source

	@staticmethod
	def perlin3d(p: any, seed: float = 0) -> any:
		'''
			
		returns the perlin noise 3d vector

		Args:
			p : the value in 3d space
			seed (float): the seed

		Returns:
			any: the perlin noise value
		
		'''
		pass # cpp source

	@staticmethod
	def perlin(p: any, seed: float = 0) -> float:
		'''
			
		generate the perlin noise value

		Args:
			p : the value in 3d space
			seed (float): the seed

		Returns:
			float: the perlin noise value
		
		'''
		pass # cpp source

	@staticmethod
	def getEnumValueByIndex(enumID: str, index: int) -> str:
		'''
			
		get the value from the global strings list by index. That lists used in dropdown boxes in UI

		Args:
			enumID (str): the enumerator ID
			index (int): the index of the value

		Returns:
			str: the string
		
		'''
		pass # cpp source

	@staticmethod
	def getEnumValue(enumID: str, key: str) -> int:
		'''
			
		get the integer value that corresponds to the string value from the global strings list.

		Args:
			enumID (str): the enumerator ID
			key (str): the string value fo find

		Returns:
			int: the integer value that corresponds to the string
		
		'''
		pass # cpp source

	@staticmethod
	def getEnumValueIndex(enumID: str, key: str) -> int:
		'''
			
		get the index of the value in the global strings list. That lists used in dropdown boxes in UI

		Args:
			enumID (str): the enumerator ID
			key (str): the value to find

		Returns:
			int: the index of the value, -1 means that value not found
		
		'''
		pass # cpp source

	@staticmethod
	def getEnumValuesCount(enumID: str) -> int:
		'''
			
		get the count of the values in the global strings list. That lists used in dropdown boxes in UI

		Args:
			enumID (str): the enumerator ID

		Returns:
			int: the count of the values
		
		'''
		pass # cpp source

	@staticmethod
	def clearEnum(enumID: str):
		'''
			
		clear the global strings list.

		Args:
			enumID (str): the enumerator ID
		
		'''
		pass # cpp source

	@staticmethod
	def addEnumValue(enumID: str, key: str, value: int = 1):
		'''
			
		add the value to the global strings list.

		Args:
			enumID (str): the enumerator ID
			key (str): the string to add
			value (int): the integer value that corresponds to the string, -1 means that the value will be the index of the string in the list, it is default value
		
		'''
		pass # cpp source

	@staticmethod
	def quit():
		'''
			
		exit the 3DCoat
		
		'''
		pass # cpp source

	@staticmethod
	def testSuccessful():
		'''
			
		report that the test was successful. In this case the file "InstallFolder/.installer/test_success.txt created
		
		'''
		pass # cpp source

	@staticmethod
	def testFailed(message: str):
		'''
			
		report that the test was successful. In this case the file "InstallFolder/.installer/test_failed.txt created

		Args:
			message (str): the message to put into that file
		
		'''
		pass # cpp source

	@staticmethod
	def signal(message: str):
		'''
			
		send some message to 3DCoat (usually used for internal purposes)

		Args:
			message (str): the message
		
		'''
		pass # cpp source

	@staticmethod
	def last_signals() -> list[str]:
		'''
			
		get the list of last signals sent to 3DCoat

		Returns:
			list[str]: the list reference
		
		'''
		pass # cpp source

	@staticmethod
	def getFPS() -> float:
		'''
			
		get the current FPS

		Returns:
			float: the fps value (averaged)
		
		'''
		pass # cpp source

	@staticmethod
	def getFrameTimeMs() -> float:
		'''
			
		get the frame time in milliseconds

		Returns:
			float: the milliseconds amount
		
		'''
		pass # cpp source

	@staticmethod
	def inRenderProcess() -> bool:
		'''
			
		check if the viewport is in render process in render room

		Returns:
			bool: true if in render
		
		'''
		pass # cpp source

	@staticmethod
	def set(key: str, value: str):
		'''
			
		Globally set the value for the key, it is even stored between sessions of the 3DCoat

		Args:
			key (str): the key
			value (str): the value to store
		
		'''
		pass # cpp source

	@staticmethod
	def get(key: str) -> str:
		'''
			
		Get previously stored value by the key

		Args:
			key (str): the key

		Returns:
			str: the value as string, empty string if not found
		
		'''
		pass # cpp source



class uv():
	'''
			
		The UV API. The mesh is taken from the current room. If paint or UV rooms is active, the mesh is taken from the paint room, otherwise the mesh is taken from the Retopo room
		
	'''

	@staticmethod
	def uvSetsCount() -> int:
		'''
			
		get the UV-sets count.

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	@staticmethod
	def setUnwrapIslandsDistance(distance: float):
		'''
			
		set the border around the islands when we pack it

		Args:
			distance (float): the border size in percents
		
		'''
		pass # cpp source

	@staticmethod
	def getUnwrapIslandsDistance() -> float:
		'''
			
		get the border around the islands when we pack it

		Returns:
			float: the border size in percents
		
		'''
		pass # cpp source

	@staticmethod
	def currentUvSet() -> int:
		'''
			
		get the current uv-set index

		Returns:
			int: the index
		
		'''
		pass # cpp source

	@staticmethod
	def islandsCount(uv_set: int) -> int:
		'''
			
		get the islands count over the current uv-set

		Args:
			uv_set (int): the uv-set index

		Returns:
			int: teh islands count
		
		'''
		pass # cpp source

	@staticmethod
	def islandToMesh(uv_set: int, island_index: int) -> Mesh:
		'''
			
		get the mesh that contains the island, xy of each point is the UV coordinate. The mesh contains only one island

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			Mesh: the flat mesh
		
		'''
		pass # cpp source

	@staticmethod
	def islandToMeshInSpace(uv_set: int, island_index: int) -> Mesh:
		'''
			
		get the mesh that contains the island, each point is the coordinate in space (not the uv coordinate!). The mesh contains only one island. The faces correspond to the faces of the mesh that was got by islandToMesh

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			Mesh: s mesh the 3D mesh
		
		'''
		pass # cpp source

	@staticmethod
	def getIslandVertexMapping(uv_set: int, island_index: int) -> list[int]:
		'''
			
		get the mapping from the vertex index in the mesh that was got by islandToMesh to the vertex index in the original mesh

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			list[int]: the list of the positional vertex indices of the original mesh in same order as the vertices in the mesh that was got by islandToMesh
		
		'''
		pass # cpp source

	@staticmethod
	def getIslandBorder(uv_set: int, island_index: int) -> list[int]:
		'''
			
		get unsorted list of edges on the border of the island

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			list[int]: the list of edges, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		
		'''
		pass # cpp source

	@staticmethod
	def getBorderBetweenIslands(uv_set1: int, island_index1: int, uv_set2: int, island_index2: int) -> list[int]:
		'''
			
		get the border between two islands

		Args:
			uv_set1 (int): the uv set index of the first island
			island_index1 (int): the island index within the uv set of the first island
			uv_set2 (int): the uv set index of the second island
			island_index2 (int): the island index within the uv set of the second island

		Returns:
			list[int]: the list of edges that are common for both islands, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		
		'''
		pass # cpp source

	@staticmethod
	def getIslandVertexUv(uv_set: int, island_index: int, vertex_index: int) -> any:
		'''
			
		get the uv coordinate of the positional vertex in the island

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
			vertex_index (int): the positional vertex index

		Returns:
			any: the uv coordinate of the vertex, vec2(0,0) if the vertex is not in the island
		
		'''
		pass # cpp source

	@staticmethod
	def flattenSingleIsland(mesh: Mesh, method: int, optimize_rotation: bool = True, scale_to_geometry: bool = True) -> Mesh:
		'''
			
		Flatten the mesh that consists of the single island

		Args:
			mesh (Mesh): the mesh that consists of the single island
			method (int): the flattening method. 0 - flatten to the plane, 1 - LSCM, 2 - ABF, 3 - GU, 4 - Stripe (if possible)
			optimize_rotation (bool): optimize the rotation of the island, place it approximately horizontally or vertically
			scale_to_geometry (bool): scale the island to keep average edge length equal to the average edge length of the original mesh

		Returns:
			Mesh: the flat mesh
		
		'''
		pass # cpp source

	@staticmethod
	def meshToIsland(mesh: Mesh, uv_set: int, island_index: int):
		'''
			
		use the mesh (that was previously got by islandToMesh) to replace the island in the current uv-set

		Args:
			mesh (Mesh): the mesh that was previously got by islandToMesh
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	@staticmethod
	def pack(uv_set: int, rotate: bool, shuffle: bool):
		'''
			
		pack the islands in the current uv-set

		Args:
			uv_set (int): the uv set index
			rotate (bool): allow rotation while packing
			shuffle (bool): shuffle the identical islands to avoid the exact overlapping
		
		'''
		pass # cpp source

	@staticmethod
	def unwrap(uv_set: int):
		'''
			
		unwrap the current uv-set

		Args:
			uv_set (int): the uv set index
		
		'''
		pass # cpp source

	@staticmethod
	def toAbf(uv_set: int, island_index: int):
		'''
			
		unwrap the island using the ABF approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	@staticmethod
	def toLscm(uv_set: int, island_index: int):
		'''
			
		unwrap the island using the LSCM approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	@staticmethod
	def toGu(uv_set: int, island_index: int):
		'''
			
		unwrap the island using the GU (Globally Uniform) approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	@staticmethod
	def toPlanar(uv_set: int, island_index: int):
		'''
			
		unwrap the island using the Planar approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	@staticmethod
	def toStripe(uv_set: int, island_index: int):
		'''
			
		try to uwrap the island as the regular stripe

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	@staticmethod
	def toUvSet(uv_set: int, island_index: int, destination_uv_set: int):
		'''
			
		move the island from one uv-set to another one

		Args:
			uv_set (int): the source uv set index
			island_index (int): the island index within the source uv set
			destination_uv_set (int): the destination uv set index
		
		'''
		pass # cpp source

	@staticmethod
	def getWholeMesh() -> Mesh:
		'''
			
		get the whole mesh from the paint/UV/Retopo room - in dependence on current room

		Returns:
			Mesh: the whole paint or retopo mesh (in dependence on current room)
		
		'''
		pass # cpp source

	@staticmethod
	def selectedToMesh() -> Mesh:
		'''
			
		get the selected faces as the Mesh object

		Returns:
			Mesh: the Mesh
		
		'''
		pass # cpp source

	@staticmethod
	def getSeams() -> list[int]:
		'''
			
		get all seams across the mesh

		Returns:
			list[int]: the list of integer values, each value is the index of the vertex in the mesh, the even index is start of the seam, the odd index is the end of the seam
		
		'''
		pass # cpp source

	@staticmethod
	def addSeam(start_vertex_index: any, end_vertex_index: int):
		'''
			
		add the seam to the mesh

		Args:
			start_vertex_index : the start positional vertex index
			end_vertex_index (int): the end positional vertex index
		
		'''
		pass # cpp source

	@staticmethod
	def removeSeam(start_vertex_index: int, end_vertex_index: int):
		'''
			
		remove the seam from the mesh

		Args:
			start_vertex_index (int): the start positional vertex index
			end_vertex_index (int): the end positional vertex index
		
		'''
		pass # cpp source

	@staticmethod
	def getSharpEdges() -> list[int]:
		'''
			
		get the sharp edges across the mesh

		Returns:
			list[int]: the list of integer values, each value is the index of the vertex in the mesh, the even index is start of the edge, the odd index is the end of the edge
		
		'''
		pass # cpp source

	@staticmethod
	def addSharpEdge(start_vertex_index: int, end_vertex_index: int):
		'''
			
		add the sharp edge to the mesh

		Args:
			start_vertex_index (int): the start positional vertex index
			end_vertex_index (int): the end positional vertex index
		
		'''
		pass # cpp source

	@staticmethod
	def removeSharpEdge(start_vertex_index: int, end_vertex_index: int):
		'''
			
		remove the sharp edge from the mesh

		Args:
			start_vertex_index (int): the start positional vertex index
			end_vertex_index (int): the end positional vertex index
		
		'''
		pass # cpp source

	@staticmethod
	def unwrapUnassigned():
		'''
			
		re-wrap/extend  islands in correspondence to the changed seams and inserted faces. Pay attention, that it may lead to islands intersection.
		
		'''
		pass # cpp source

	@staticmethod
	def applyUVSet():
		'''
			
		apply uv changes to the paint room mesh (if we use uv/paint context)
		
		'''
		pass # cpp source



class Model():
	'''
			
		The class that corresponds to the retopo/modeling rooms meshes. This is advanced version of the Mesh that allows essential topology changes on the fly.
		It is very similar to Mesh by basic functionality, may be easily converted to Mesh and vice versa. But it is more heavy structure, use Mesh if you don't need the advanced functionality.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, source: Model):
		pass # CPP source

	def __init__(self, source: Mesh):
		pass # CPP source

	def __assign__(self, source: Model) -> Model:
		return super().__assign__(source)

	def __assign__(self, source: Mesh) -> Model:
		return super().__assign__(source)

	def __iadd__(self, source: Model) -> Model:
		return super().__iadd__(source)

	def __iadd__(self, source: Mesh) -> Model:
		return super().__iadd__(source)

	def transform(self, m: any) -> Model:
		'''
			
		transform the whole Model with the matrix

		Args:
			m : the transformation matrix

		Returns:
			Model: the reference to the Model
		
		'''
		pass # cpp source

	def MakeCopy(self) -> Model:
		'''
			
		make a copy of the source mesh. Pay attention, if you taken it from the retopo/uv context, it will no longer refer to the retopo/uv mesh, it will be independent copy
		
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	@staticmethod
	def fromRetopo() -> Model:
		'''
			
		get the reference to the mesh in the retopo room

		Returns:
			Model: the reference to the mesh
		
		'''
		pass # cpp source

	@staticmethod
	def fromModeling() -> Model:
		'''
			
		get the reference to the mesh in the modeling room, currently it is the same mesh as in the retopo room

		Returns:
			Model: the reference to the mesh
		
		'''
		pass # cpp source

	@staticmethod
	def fromUv() -> Model:
		'''
			
		get the reference to the mesh in the uv room, pay attention that topology changes to that mesh may lead to instability!

		Returns:
			Model: the reference to the mesh
		
		'''
		pass # cpp source

	def UpdateMesh(self):
		'''
			
		Apply changes on the mesh
		
		'''
		pass # cpp source

	def displayOptions(self, showWireframe: bool = True, showColored: bool = True, showSeams: bool = True, showSharpEdges: bool = True, smoothView: bool = False):
		'''
			
		Set the display options for the retopo/modeling/uv meshes

		Args:
			showWireframe (bool): show the wireframe
			showColored (bool): show colored clusters
			showSeams (bool): show seams
			showSharpEdges (bool): show sharp edges
			smoothView (bool): smooth view
		
		'''
		pass # cpp source

	def getObjectsCount(self) -> int:
		'''
			
		get the retopo groups count

		Returns:
			int: the amount
		
		'''
		pass # cpp source

	def getCurrentObject(self) -> int:
		'''
			
		get the index of the current group

		Returns:
			int: the index
		
		'''
		pass # cpp source

	def setCurrentObject(self, index: int):
		'''
			
		set the current group index

		Args:
			index (int): the index
		
		'''
		pass # cpp source

	def getObjectName(self, group_index: int) -> str:
		'''
			
		get the retopo group name

		Args:
			group_index (int): the group index

		Returns:
			str: the name
		
		'''
		pass # cpp source

	def removeObject(self, group_index: int):
		'''
			
		remove the group by index
		
		'''
		pass # cpp source

	def setObjectName(self, index: int, name: str):
		'''
			
		rename the group by index

		Args:
			index (int): the group index to rename
			name (str): the new name
		
		'''
		pass # cpp source

	def setObjectVisibility(self, index: int, visible: bool):
		'''
			
		set the group visibility

		Args:
			index (int): the group index
			visible (bool): the visibility state
		
		'''
		pass # cpp source

	def getObjectVisibility(self, index: int) -> bool:
		'''
			
		get the group visibility

		Args:
			index (int): the group index

		Returns:
			bool: the visibility state
		
		'''
		pass # cpp source

	def addObject(self, name: str) -> int:
		'''
			
		add new retopo group

		Args:
			name (str): the group name

		Returns:
			int: the index of new group
		
		'''
		pass # cpp source

	def addMaterial(self, name: str) -> int:
		'''
			
		add the new UV set/Material

		Args:
			name (str): the name

		Returns:
			int: the new UV set/Material index
		
		'''
		pass # cpp source

	def removeUnusedMaterials(self):
		'''
			
		remove all unused UV sets (not referred within the mesh)
		
		'''
		pass # cpp source

	def getObjectReferenceColor(self, group_index: int) -> any:
		'''
			
		get the group reference color

		Args:
			group_index (int): the group index

		Returns:
			any: the (r,g,b,a) vector, 0..255
		
		'''
		pass # cpp source

	def setObjectReferenceColor(self, group_index: int, color: any):
		'''
			
		set the group reference color

		Args:
			group_index (int): the group index
			color : the (r,g,b,a) vector, 0..255
		
		'''
		pass # cpp source

	def selectedToObject(self, group_index: int):
		'''
			
		move the selected faces to the group

		Args:
			group_index (int): the group index
		
		'''
		pass # cpp source

	def getWholeMesh(self) -> Mesh:
		'''
			
		get the whole mesh from the retopo room

		Returns:
			Mesh: the Mesh object
		
		'''
		pass # cpp source

	def selectedToMesh(self) -> Mesh:
		'''
			
		get the selected faces as the Mesh object

		Returns:
			Mesh: the Mesh
		
		'''
		pass # cpp source

	def visibleToMesh(self) -> Mesh:
		'''
			
		get the visible faces as the Mesh object

		Returns:
			Mesh: teh Mesh
		
		'''
		pass # cpp source

	def addTransformed(self, mesh: Mesh, Transform: any = 4, b: BoolOpType = Coat_CPP.BoolOpType.BOOL_MERGE, select: bool = False, snap_to_existing: bool = False):
		'''
			
		insert the mesh to the retopo/modeling room, each object of the mesh treated as the new retopo layer

		Args:
			mesh (Mesh): the Mesh object
			Transform : the transformation matrix
			b (BoolOpType): the boolean operation type
			select (bool): the flag that indicates if we need to select faces of the the inserted mesh, used only if b is BOOL_MERGE
			snap_to_existing (bool): the flag that indicates if we need to snap the mesh to the existing sculpt/paint objects
		
		'''
		pass # cpp source

	def getObjectMesh(self, group_index: int) -> Mesh:
		'''
			
		get the mesh from some retopo group

		Args:
			group_index (int): the group index

		Returns:
			Mesh: the Mesh object
		
		'''
		pass # cpp source

	def setObjectMesh(self, group_index: int, mesh: Mesh, transform: any = 4):
		'''
			
		replace the retopo layer with mesh

		Args:
			group_index (int): the group index
			mesh (Mesh): the Mesh object to insert
			transform : the transformation matrix
		
		'''
		pass # cpp source

	def duplicateObject(self, group_index: int, name: str = None, transform: any = 4, select: bool = False) -> int:
		'''
			
		duplicate the object (retopo group)

		Args:
			group_index (int): the object/group index
			name (str): the new name, if not passed the name will be generated automatically
			transform : the additional transformation matrix
			select (bool): the flag that indicates if we need to select the new object's faces (in addition to existing selection)

		Returns:
			int: the new object index
		
		'''
		pass # cpp source

	def generateName(self, base: str) -> str:
		'''
			
		generate unique name for the object, it will start as the string in base base

		Args:
			base (str): the base name

		Returns:
			str: the unique name
		
		'''
		pass # cpp source

	def clearObjectMesh(self, group_index: int):
		'''
			
		remove all faces from the group

		Args:
			group_index (int): the group index
		
		'''
		pass # cpp source

	def clear(self):
		'''
			
		clear the whole mesh
		
		'''
		pass # cpp source

	def dropUndo(self):
		'''
			
		Drop the whole mesh to the undo queue, it is important if you want allow the user to undo your mesh changes, call it before your changes. It works for UV room too.
		
		'''
		pass # cpp source

	def getSelectedFaces(self) -> list[int]:
		'''
			
		get the list of selected faces

		Returns:
			list[int]: the list of selected faces
		
		'''
		pass # cpp source

	def setSelectedFaces(self, faces: list[int]):
		'''
			
		set the selected faces list

		Args:
			faces (list[int]): the faces indices list
		
		'''
		pass # cpp source

	def selectFace(self, face: int):
		'''
			
		select the face by index

		Args:
			face (int): the face index
		
		'''
		pass # cpp source

	def selectObject(self, group_index: int, add_to_selected: bool = True):
		'''
			
		select all feces in the group

		Args:
			group_index (int): the group index
		
		'''
		pass # cpp source

	def getObjectFaces(self, group_index: int) -> list[int]:
		'''
			
		get the list of faces in the group

		Args:
			group_index (int): the group index

		Returns:
			list[int]: the list of faces
		
		'''
		pass # cpp source

	def isFaceSelected(self, face: int) -> bool:
		'''
			
		check if the face selected

		Args:
			face (int): the face index

		Returns:
			bool: the selection state
		
		'''
		pass # cpp source

	def unselectAllFaces(self):
		'''
			
		unselect all faces
		
		'''
		pass # cpp source

	def expandSelection(self):
		'''
			
		expand the faces/vertices/edges selection to the connected geometry
		
		'''
		pass # cpp source

	def contractSelection(self):
		'''
			
		contract the faces/vertices/edges selection to the connected geometry
		
		'''
		pass # cpp source

	def selectedToEdges(self):
		'''
			
		convert faces/vertices selection to edges selection
		
		'''
		pass # cpp source

	def selectedToFaces(self):
		'''
			
		convert edges/vertices selection to faces selection
		
		'''
		pass # cpp source

	def selectedToVertices(self):
		'''
			
		convert faces/edges selection to vertices selection
		
		'''
		pass # cpp source

	def getSelectedEdges(self) -> list[int]:
		'''
			
		returns even amount of vertex indices, pairs os start and end vertices of the selected edges

		Returns:
			list[int]: the list of vertex indices (pairs)
		
		'''
		pass # cpp source

	def setSelectedEdges(self, edges: list[int]):
		'''
			
		set the selected edges list

		Args:
			edges (list[int]): the edges indices list (should be even amount of indices)
		
		'''
		pass # cpp source

	def selectEdge(self, vertex1: int, vertex2: int):
		'''
			
		select the edge by vertex indices (add to selection)

		Args:
			vertex1 (int): the first vertex index
			vertex2 (int): the second vertex index
		
		'''
		pass # cpp source

	def isEdgeSelected(self, vertex1: int, vertex2: int) -> bool:
		'''
			
		check if the edge is selected, order of vertices has no matter

		Args:
			vertex1 (int): the first vertex index
			vertex2 (int): the second vertex index

		Returns:
			bool: true if the edge is selected
		
		'''
		pass # cpp source

	def unselectAllEdges(self):
		'''
			
		unselect all edges
		
		'''
		pass # cpp source

	def getSelectedVertices(self) -> list[int]:
		'''
			
		get the list of selected vertices

		Returns:
			list[int]: the list of selected vertices
		
		'''
		pass # cpp source

	def getSelectedVerticesWeights(self) -> list[float]:
		'''
			
		get the soft selection weights of the selected vertices, 1 is maximum value

		Returns:
			list[float]: the list of weights, the size of the list is equal to the size of the selected vertices list
		
		'''
		pass # cpp source

	def setSelectedVertices(self, vertices: list[int], weights: list[float]):
		'''
			
		set the selected vertices list

		Args:
			vertices (list[int]): the list of vertices indices
			weights (list[float]): the list of soft selection weights, the size of the list should be zero or equal to the size of the vertices list. If it is empty, the vertices will be selected with the maximal weight
		
		'''
		pass # cpp source

	def selectVertex(self, vertex: int, weight: float = 1.0):
		'''
			
		add the vertex to the selection

		Args:
			vertex (int): the vertex index
			weight (float): the soft selection weight, 1 is maximum value
		
		'''
		pass # cpp source

	def isVertexSelected(self, vertex: int) -> bool:
		'''
			
		check if the vertex is selected

		Args:
			vertex (int): the vertex index

		Returns:
			bool: true if the vertex is selected
		
		'''
		pass # cpp source

	def unselectAllVertices(self):
		'''
			
		unselect all vertices
		
		'''
		pass # cpp source

	def facesCount(self) -> int:
		'''
			
		get the faces count

		Returns:
			int: the faces count
		
		'''
		pass # cpp source

	def vertsCount(self) -> int:
		'''
			
		get the positional vertices count

		Returns:
			int: the vertices count
		
		'''
		pass # cpp source

	def vertsUvCount(self) -> int:
		'''
			
		get the uv vertices count

		Returns:
			int: the uv vertices count
		
		'''
		pass # cpp source

	def removeFace(self, face: int):
		'''
			
		remove the face by index

		Args:
			face (int): the face index
		
		'''
		pass # cpp source

	def createNewFace(self, Group: int, UVSet: int) -> int:
		'''
			
		create empty face, you need to call setFaceVertices to set the vertices, setFaceUVVerts to set the UV vertices

		Args:
			Group (int): the face group index
			UVSet (int): the UV set index

		Returns:
			int: the new face index
		
		'''
		pass # cpp source

	def getFaceVertsCount(self, face: int) -> int:
		'''
			
		get the vertices count over the face

		Args:
			face (int): the face index

		Returns:
			int: the vertices count
		
		'''
		pass # cpp source

	def getFaceVertex(self, face: int, vertex_index: int) -> int:
		'''
			
		get the vertex index over the face

		Args:
			face (int): the face index
			vertex_index (int): the vertex index over the face

		Returns:
			int: the vertex index, -1 if the vertex/face index is out of range
		
		'''
		pass # cpp source

	def getFaceVerts(self, face: int) -> list[int]:
		'''
			
		get the list of UV vertex indices over the face, pay attention UV vertices are not same as position vertices

		Args:
			face (int): the face index

		Returns:
			list[int]: the list of vertex indices
		
		'''
		pass # cpp source

	def setFaceVerts(self, face: int, vertices: list[int]):
		'''
			
		set the list of positional vertex indices over the face

		Args:
			face (int): the face index
			vertices (list[int]): the list of vertex indices
		
		'''
		pass # cpp source

	def getFaceVisibility(self, face: int) -> bool:
		'''
			
		get the face visibility

		Args:
			face (int): the face index

		Returns:
			bool: the visibility state
		
		'''
		pass # cpp source

	def setFaceVisibility(self, face: int, visibility: bool):
		'''
			
		set the face visibility

		Args:
			face (int): the face index
			visibility (bool): the visibility state
		
		'''
		pass # cpp source

	def getFaceSquare(self, face: int) -> float:
		'''
			
		get the face square

		Args:
			face (int): the face index

		Returns:
			float: the square
		
		'''
		pass # cpp source

	def getFaceUVSquare(self, face: int) -> float:
		'''
			
		get the face square in UV space

		Args:
			face (int): the face index

		Returns:
			float: the square
		
		'''
		pass # cpp source

	def getFaceNormal(self, face: int) -> any:
		'''
			
		get the face normal

		Args:
			face (int): the face index

		Returns:
			any: the face normal
		
		'''
		pass # cpp source

	def getFaceObject(self, face: int) -> int:
		'''
			
		get the group index of the face

		Args:
			face (int): the face index

		Returns:
			int: the group index
		
		'''
		pass # cpp source

	def setFaceObject(self, face: int, group: int):
		'''
			
		set the group index of the face

		Args:
			face (int): the face index
			group (int): the group index
		
		'''
		pass # cpp source

	def getFaceMaterial(self, face: int) -> int:
		'''
			
		get the UV set index for the face

		Args:
			face (int): the face index

		Returns:
			int: the UV set index, -1 if out of range
		
		'''
		pass # cpp source

	def setFaceMaterial(self, face: int, uv_set: int):
		'''
			
		set the UV set for the face

		Args:
			face (int): the face index
			uv_set (int): the UV set index
		
		'''
		pass # cpp source

	def getFaceUvVertsCount(self, face: int) -> int:
		'''
			
		get the amount of UV vertices over the face

		Args:
			face (int): the face index

		Returns:
			int: amount of vertices over the face, 0 if UV-s not assigned
		
		'''
		pass # cpp source

	def getFaceUvVertex(self, face: int, vertex_index: int) -> int:
		'''
			
		get the UV vertex index over the face

		Args:
			face (int): the face index
			vertex_index (int): the vertex index over the face

		Returns:
			int: the UV vertex index, -1 if the vertex/face index is out of range
		
		'''
		pass # cpp source

	def getFaceUvVerts(self, face: int) -> list[int]:
		'''
			
		get the list of UV vertices indices over the face

		Args:
			face (int): the face index

		Returns:
			list[int]: the list of UV vertices indices
		
		'''
		pass # cpp source

	def setFaceUvVerts(self, face: int, vertices: list[int]):
		'''
			
		set the UV vertices for the face

		Args:
			face (int): the face index
			vertices (list[int]): the UV vertices list
		
		'''
		pass # cpp source

	def getVertex(self, vertex: int) -> any:
		'''
			
		get the vertex position in space

		Args:
			vertex (int): the vertex index

		Returns:
			any: the position
		
		'''
		pass # cpp source

	def setVertex(self, vertex: int, position: any):
		'''
			
		set the vertex position in space

		Args:
			vertex (int): the vertex index
			position : the position
		
		'''
		pass # cpp source

	def createNewVertex(self, position: any) -> int:
		'''
			
		create the positional vertex

		Args:
			position : the position

		Returns:
			int: the positional vertex index
		
		'''
		pass # cpp source

	def getVertexUV(self, uv_vertex: int) -> any:
		'''
			
		get the UV coordinates of the UV vertex

		Args:
			uv_vertex (int): the uv vertex index

		Returns:
			any: teh UV coordinates
		
		'''
		pass # cpp source

	def setVertexUV(self, uv_vertex: int, uv: any):
		'''
			
		set the UV for the UV vertex

		Args:
			uv_vertex (int): the uv vertex index
			uv : the UV coordinates
		
		'''
		pass # cpp source

	def createNewUvVertex(self, uv: any) -> int:
		'''
			
		create new UV vertex to be used for faces

		Args:
			uv : the texture coordinates

		Returns:
			int: the index
		
		'''
		pass # cpp source

	def getVertexNormal(self, vertex: int) -> any:
		'''
			
		get vertex normal, calculated as average of adjacent faces normals

		Args:
			vertex (int): the vertex index

		Returns:
			any: the normal
		
		'''
		pass # cpp source

	def updateNormals(self, for_snapping: bool = True):
		'''
			
		update the vertex normals

		Args:
			for_snapping (bool): if true, the normals will lay in the middle of faces, ne respecting the faces square.
		
		'''
		pass # cpp source

	def updateTopology(self):
		'''
			
		update the connectivity information, it should be called sometimes if you feel that the connectivity information lost due to some heavy operations
		
		'''
		pass # cpp source

	def cleanup(self):
		'''
			
		complete cleanul from non-manifolds or other problems, some faces may be removed
		
		'''
		pass # cpp source

	def getVertsNearVertex(self, vertex: int) -> list[int]:
		'''
			
		get the list of vertices that are adjacent to the vertex

		Args:
			vertex (int): the vertex index

		Returns:
			list[int]: the list of adjacent vertices
		
		'''
		pass # cpp source

	def getFacesNearVertex(self, vertex: int) -> list[int]:
		'''
			
		get the list of faces that are adjacent to the vertex

		Args:
			vertex (int): the vertex index

		Returns:
			list[int]: the list of adjacent faces
		
		'''
		pass # cpp source

	def getFaceNeighbors(self, face: int) -> list[int]:
		'''
			
		get the list of faces that are adjacent to the face

		Args:
			face (int): the face index

		Returns:
			list[int]: the list of adjacent faces
		
		'''
		pass # cpp source

	def getFacesNearEdge(self, vertex1: int, vertex2: int) -> list[int]:
		'''
			
		get the list of faces that are adjacent to the edge

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)

		Returns:
			list[int]: the list of adjacent faces
		
		'''
		pass # cpp source

	def isOpenEdge(self, vertex1: int, vertex2: int) -> bool:
		'''
			
		check if the edge is open

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)

		Returns:
			bool: true if open
		
		'''
		pass # cpp source

	def isSharpEdge(self, vertex1: int, vertex2: int) -> bool:
		'''
			
		check if the edge is sharp

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)

		Returns:
			bool: true if sharp
		
		'''
		pass # cpp source

	def setEdgeSharpness(self, vertex1: int, vertex2: int, sharp: bool):
		'''
			
		set the sharpness state for the edge

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)
			sharp (bool): the sharpness state
		
		'''
		pass # cpp source

	def isSeam(self, vertex1: int, vertex2: int) -> bool:
		'''
			
		check if edge is seam

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)

		Returns:
			bool: true if seam
		
		'''
		pass # cpp source

	def setEdgeSeam(self, vertex1: int, vertex2: int, seam: bool):
		'''
			
		set or clear the seam state for the edge

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)
			seam (bool): the seam state
		
		'''
		pass # cpp source

	def collapseEdge(self, vertex1: int, vertex2: int):
		'''
			
		collapse the edge to the middle of the edge

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)
		
		'''
		pass # cpp source

	def islandsCount(self, uv_set: int) -> int:
		'''
			
		get the islands count over the current uv-set

		Args:
			uv_set (int): the uv-set index

		Returns:
			int: teh islands count
		
		'''
		pass # cpp source

	def islandToMesh(self, uv_set: int, island_index: int) -> Mesh:
		'''
			
		get the mesh that contains the island, xy of each point is the UV coordinate. The mesh contains only one island

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			Mesh: the flat mesh
		
		'''
		pass # cpp source

	def islandToMeshInSpace(self, uv_set: int, island_index: int) -> Mesh:
		'''
			
		get the mesh that contains the island, each point is the coordinate in space (not the uv coordinate!). The mesh contains only one island. The faces correspond to the faces of the mesh that was got by islandToMesh

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			Mesh: s mesh the 3D mesh
		
		'''
		pass # cpp source

	def getIslandVertexMapping(self, uv_set: int, island_index: int) -> list[int]:
		'''
			
		get the mapping from the vertex index in the mesh that was got by islandToMesh to the vertex index in the original mesh

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			list[int]: the list of the positional vertex indices of the original mesh in same order as the vertices in the mesh that was got by islandToMesh
		
		'''
		pass # cpp source

	def getIslandBorder(self, uv_set: int, island_index: int) -> list[int]:
		'''
			
		get unsorted list of edges on the border of the island

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set

		Returns:
			list[int]: the list of edges, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		
		'''
		pass # cpp source

	def getBorderBetweenIslands(self, uv_set1: int, island_index1: int, uv_set2: int, island_index2: int) -> list[int]:
		'''
			
		get the border between two islands

		Args:
			uv_set1 (int): the uv set index of the first island
			island_index1 (int): the island index within the uv set of the first island
			uv_set2 (int): the uv set index of the second island
			island_index2 (int): the island index within the uv set of the second island

		Returns:
			list[int]: the list of edges that are common for both islands, even amount of elements, each pair of elements is the positional vertex indices of the original mesh
		
		'''
		pass # cpp source

	def getIslandVertexUv(self, uv_set: int, island_index: int, vertex_index: int) -> any:
		'''
			
		get the uv coordinate of the positional vertex in the island

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
			vertex_index (int): the positional vertex index

		Returns:
			any: the uv coordinate of the vertex, vec2(0,0) if the vertex is not in the island
		
		'''
		pass # cpp source

	@staticmethod
	def flattenSingleIsland(mesh: Mesh, method: int, optimize_rotation: bool = True, scale_to_geometry: bool = True) -> Mesh:
		'''
			
		Flatten the mesh that consists of the single island

		Args:
			mesh (Mesh): the mesh that consists of the single island
			method (int): the flattening method. 0 - flatten to the plane, 1 - LSCM, 2 - ABF, 3 - GU, 4 - Stripe (if possible)
			optimize_rotation (bool): optimize the rotation of the island, place it approximately horizontally or vertically
			scale_to_geometry (bool): scale the island to keep average edge length equal to the average edge length of the original mesh

		Returns:
			Mesh: the flat mesh
		
		'''
		pass # cpp source

	def meshToIsland(self, mesh: Mesh, uv_set: int, island_index: int):
		'''
			
		use the mesh (that was previously got by islandToMesh) to replace the island in the current uv-set

		Args:
			mesh (Mesh): the mesh that was previously got by islandToMesh
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	def pack(self, uv_set: int, rotate: bool, shuffle: bool):
		'''
			
		pack the islands in the current uv-set

		Args:
			uv_set (int): the uv set index
			rotate (bool): allow rotation while packing
			shuffle (bool): shuffle the identical islands to avoid the exact overlapping
		
		'''
		pass # cpp source

	def unwrap(self, uv_set: int):
		'''
			
		unwrap the current uv-set

		Args:
			uv_set (int): the uv set index
		
		'''
		pass # cpp source

	def toAbf(self, uv_set: int, island_index: int):
		'''
			
		unwrap the island using the ABF approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	def toLscm(self, uv_set: int, island_index: int):
		'''
			
		unwrap the island using the LSCM approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	def toGu(self, uv_set: int, island_index: int):
		'''
			
		unwrap the island using the GU (Globally Uniform) approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	def toPlanar(self, uv_set: int, island_index: int):
		'''
			
		unwrap the island using the Planar approach

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	def toStripe(self, uv_set: int, island_index: int):
		'''
			
		try to uwrap the island as the regular stripe

		Args:
			uv_set (int): the uv set index
			island_index (int): the island index within the uv set
		
		'''
		pass # cpp source

	def extrudeSelected(self):
		'''
			
		Extrude the selected edges or selected faces without the actual moving of the extruded elements. They stay selected, so you amy apply some transform to the selected elements
		
		'''
		pass # cpp source

	def moveSelectedFacesAlongFacesNormals(self, displacement: float):
		'''
			
		move selected faces along the faces normals, trying to keep faces parallel to the original direction

		Args:
			displacement (float): the displacement value
		
		'''
		pass # cpp source

	def moveSelectedFacesAlongVertexNormals(self, displacement: float):
		'''
			
		move selected faces along the vertex normals, each vertex displace on the same distance

		Args:
			displacement (float): the displacement value
		
		'''
		pass # cpp source

	def subdivideSelectedFaces(self, apply_catmull_clark: bool = False):
		'''
			
		subdivide the selected faces

		Args:
			apply_catmull_clark (bool): apply the catmull-clark subdivision
		
		'''
		pass # cpp source

	def subdivide(self, apply_catmull_clark: bool = True):
		'''
			
		subdivide the whole mesh

		Args:
			apply_catmull_clark (bool): apply the catmull-clark subdivision
		
		'''
		pass # cpp source

	def transformSelected(self, transform: any, apply_symmetry: bool):
		'''
			
		apply the transformation to the selected elements

		Args:
			transform : the transformation matrix
			apply_symmetry (bool): apply the global symmetry
		
		'''
		pass # cpp source

	def scaleSelectedFacesClusters(self, scale: float, method: ClusterScale = Coat_CPP.ClusterScale.Uniform_Scaling):
		'''
			
		scale each selection cluster separately, to own center mass

		Args:
			scale (float): the scale coefficient
		
		'''
		pass # cpp source

	def bevelOverSelectedVertices(self, size: float):
		'''
			
		perform the bevel over the selected vertices. As result, new faces will be selected

		Args:
			size (float): the bevel size
		
		'''
		pass # cpp source

	def bevelOverSelectedEdges(self, size: float, segments: int = 1, OldVariant: bool = False):
		'''
			
		perform the bevel over the selected edges.

		Args:
			size (float): the bevel width
			OldVariant (bool): if true the older variant of the bevel (splits edges in strightforward way), in some cases it works more stable.
		
		'''
		pass # cpp source

	def splitEdge(self, vertex1: int, vertex2: int, position: float) -> int:
		'''
			
		split existing edge somewhere between vertices.

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)
			position (float): the position to split the edge, [0..1], 0 - near the vertex1, 1 - near the vertex2

		Returns:
			int: the new vertex index
		
		'''
		pass # cpp source

	def connect(self, vertex1: int, vertex2: int) -> bool:
		'''
			
		split existing edge somewhere between vertices.

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)

		Returns:
			bool: true if succeeed to connect
		
		'''
		pass # cpp source

	def checkConnectivity(self, vertex1: int, vertex2: int) -> bool:
		'''
			
		check if connecting the two vertices is possible

		Args:
			vertex1 (int): the positional vertex index (1)
			vertex2 (int): the positional vertex index (2)

		Returns:
			bool: true if connection is possible
		
		'''
		pass # cpp source

	def connectSelectedVerts(self):
		'''
			
		connect selected vertices in smart way
		
		'''
		pass # cpp source

	def invertSelectedFacesTopoplogically(self):
		'''
			
		invert selected faces only within the connective area, if some objects has no selected faces, the selection there will not change
		
		'''
		pass # cpp source

	def inset(self, distance: float):
		'''
			
		perform the inset over the selected faces
		
		'''
		pass # cpp source

	def shell(self):
		'''
			
		perform the shell operation over the selected faces. After calling the shell() you should call the moveSelectedFacesAlongFacesNormals or moveSelectedFacesAlongVertexNormals
		to give some thickness to the resulting figure
		
		'''
		pass # cpp source

	def intrude(self):
		'''
			
		perform the intrude operation over the selected faces. After calling the intrude() you should call the moveSelectedFacesAlongFacesNormals or moveSelectedFacesAlongVertexNormals
		to give some thickness to the resulting figure
		
		'''
		pass # cpp source

	def relaxSelected(self):
		'''
			
		relax selected vergtices
		
		'''
		pass # cpp source

	def selectPath(self, vertex1: int, vertex2: int):
		'''
			
		select all edges on the path from vertex1 to vertex2 (add to existing edges selection)

		Args:
			vertex1 (int): the first vertex
			vertex2 (int): the second vertex
		
		'''
		pass # cpp source

	def getPath(self, vertex1: int, vertex2: int) -> list[int]:
		'''
			
		get all vertices on the path from vertex1 to vertex2

		Args:
			vertex1 (int): the first vertex
			vertex2 (int): the second vertex
		
		'''
		pass # cpp source



class logger():
	def __init__(self):
		pass # CPP source

	def __init__(self, filename: str):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def open(self):
		'''
			
		open the accumulated log in the default text editor
		
		'''
		pass # cpp source

	def showMessage(self):
		'''
			
		show the accumulated log in the message box
		
		'''
		pass # cpp source

	def directTo(self, filename: str) -> logger:
		'''
			
		Direct the log output to the file

		Args:
			filename (str): the filename to log there. The filename may be relative path.

		Returns:
			logger: the logger reference
		
		'''
		pass # cpp source

	def getFullPath(self) -> any:
		'''
			
		Returns the absolute path to the log file.

		Returns:
			any: the absolute path even if you passed the relative path.
		
		'''
		pass # cpp source

	def flush(self) -> logger:
		'''
			
		save all acumulated text to the file

		Returns:
			logger: the chain reference
		
		'''
		pass # cpp source

	def newline(self) -> logger:
		'''
			
		start newline in the text file

		Returns:
			logger: the chain reference
		
		'''
		pass # cpp source

	def timestamp(self) -> logger:
		'''
			
		add the timestamp to the log as the

		Returns:
			logger: the reference
		
		'''
		pass # cpp source

	def startTimer(self) -> logger:
		'''
			
		start the timer to profile some operation

		Returns:
			logger: the reference
		
		'''
		pass # cpp source

	def endTimer(self) -> logger:
		'''
			
		stop the timer and output the time into the log as amount of microseconds

		Returns:
			logger: the reference
		
		'''
		pass # cpp source

	def floatPrecission(self, signs: int = 2) -> logger:
		'''
			
		set the precission of floating-point output

		Returns:
			logger: the reference
		
		'''
		pass # cpp source

