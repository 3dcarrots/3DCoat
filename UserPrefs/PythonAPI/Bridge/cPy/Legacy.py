from __future__ import annotations
import cPy.cTypes
#Legacy
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum

def ModalDialog(ID: str, Caption: str):
		'''
			
	Show model dialog with text identified ID. ID used to take translation from language xml or just may be shown directly if translation not found.
	
		'''
		pass # cpp source

def GetLastDialogButtonIndex():
		'''
			
	Show model dialog with text identified ID. ID used to take translation from language xml or just may be shown directly if translation not found.
	
		'''
		pass # cpp source

def DontShowAgain(ID: str, Caption: str):
		'''
			
	Show dialog with text identified ID. ID used to take translation from language xml or just may be shown directly if translation not found.
	
		'''
		pass # cpp source

def ModalDialogOkCancel(ID: str, Caption: str):
		'''
			
	Show dialog with text identified ID and two buttons - Ok and Cancel. Returns true if OK pressed, false if Cancel pressed. ID used to take translation from language xml or just may be shown directly if translation not found.
	
		'''
		pass # cpp source

def ModalDialogYesNo(ID: str, Caption: str):
		'''
			
	Show dialog with text identified ID and two buttons - Yes and No. Returns true if OK pressed, false if Cancel pressed. ID used to take translation from language xml or just may be shown directly if translation not found.
	
		'''
		pass # cpp source

def PressInNextModalDialogs(ButtonIndex: int):
		'''
			
	You should call PressInNextDialogs(-1) to stop automatical pressing of buttons.
	
		'''
		pass # cpp source

def SetModalDialogCallback(name: str):
		'''
			
	You may get name of current dialog name using next function
	
		'''
		pass # cpp source

def RemoveModalDialogCallbacks():
		'''
			
	remove all dialog callbacks
	
		'''
		pass # cpp source

def GetCurrentDialog(ID: str, Caption: str):
		'''
			
	returns true if you are in dialog now, also it retuns text and cation in current dialog to identify it
	
		'''
		pass # cpp source

def ShowFloatingText(ID: str, FID: int):
		'''
			
	show non-modal message on screen that will be hidden after some period of time
	
		'''
		pass # cpp source

def GetFontID(ID: str, size: int, weight: int):
		'''
			
	 gets the font id by font name
	
		'''
		pass # cpp source

def GetFontFileID(fileNameID: str):
		'''
			
	 gets the font id by font name
	
		'''
		pass # cpp source

def GetTextID(ID: str):
		'''
			
	 gets the string by id name
	
		'''
		pass # cpp source

def SetScriptMessage(msg: str, sparam: str):
		'''
			
	set script message and params that will be executed 
	
		'''
		pass # cpp source

def SetFloatingMessage(x: int, y: int, strMessage: str, strColor: str):
		'''
			
	set script floating message at point (x,y) 
	
		'''
		pass # cpp source

def SetFloatingMessageBox(x: int, y: int, strMessage: str, strColor: str, uType: int):
		'''
			
	set script floating message box at point (x,y) with uType (windows styles) 
	
		'''
		pass # cpp source

def GetCommandStringMessageBox(x: int, y: int, strMessage: str, strColor: str, uType: int):
		'''
			
	 get script floating message box at point (x,y) with uType (windows styles)
	
		'''
		pass # cpp source

def SetFloatingMessageBoxTime(x: int, y: int, strMessage: str, strColor: str, uType: int, Time: int):
		'''
			
	set script floating message box at point (x,y) with uType (windows styles) Time - time in mls
	
		'''
		pass # cpp source

def ShowMessageWhilePressKey(x: int, y: int, msg: str, tcolor: str, key: int, callback: str):
		'''
			
	set script message while press key
	
		'''
		pass # cpp source

def ShowMessageWhileTime(x: int, y: int, msg: str, tcolor: str, time: float):
		'''
			
	set script message while time is present
	
		'''
		pass # cpp source

def OpenWorkSpace():
		'''
			
	 open work space. file name load automatical from UI ui; ui.file("file.workspace");
	
		'''
		pass # cpp source

def SaveWorkSpace():
		'''
			
	 save work space. file name save automatical from UI ui; ui.file("file.workspace");
	
		'''
		pass # cpp source

def OpenDialog(extensions: str, result: str):
		'''
			
	function returns true if file is successfully chosen
	
		'''
		pass # cpp source

def SaveDialog(extensions: str, result: str):
		'''
			
	function returns true if file is successfully chosen
	
		'''
		pass # cpp source

def SetFileForFileDialogs(name: str):
		'''
			
	Use empty name "" to stop automatic file dialogs skipping othervice all next file dialogs will be skipped and it may lead to loosing data.
	
		'''
		pass # cpp source

def RemoveFilePath(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def RemoveExtension(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def EnsureAbsolutePth(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def GetFilePath(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def GetFileExtension(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def GetFileName(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def CheckIfExists(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def CheckFolderExist(a_0: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def CreatePath(s: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def SaveScreenShot(s: str, cutStrip: int =  0):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def CombineImages(im1: str, im2: str, imres: str):
		'''
			
	file path management routines
	
		'''
		pass # cpp source

def CompareImages(im1: str, im2: str, tolerance: int =  1):
		'''
			
	 then they are equal, otherwise not equal.
	
		'''
		pass # cpp source

def CompareImagesEx(im1: str, im2: str, tolerance: int, result: str):
		'''
			
	 The parameter result contains the list of points <Point_i(Xi,Yi) with different values.
	
		'''
		pass # cpp source

def ForEachFileInFolder(Folder: str, ExtList: str, Callback: str):
		'''
			
	Ext list contains list of extensions like "*.jpg;*.png"
	
		'''
		pass # cpp source

def cmd(ID: str):
		'''
			
	Performs any action from user interface. To get ID of command hover required item with mouse and press MMB. Command ID will be copied to clipboard. Pay attention that if command is not present in current UV layout it will not be performed.
	
		'''
		pass # cpp source

def GetBoolField(ID: str):
		'''
			
	Get bool field from UI. ID has same meaning as in cmd
	
		'''
		pass # cpp source

def SetBoolField(ID: str, val: bool):
		'''
			
	returns true if set value successfuly
	
		'''
		pass # cpp source

def GetSliderValue(ID: str):
		'''
			
	Get value of slider in UI. ID has same meaning as in cmd
	
		'''
		pass # cpp source

def SetSliderValue(ID: str, val: float):
		'''
			
	returns true if set value successfuly
	
		'''
		pass # cpp source

def SubstituteInputText(val: str):
		'''
			
	returns true if field found
	
		'''
		pass # cpp source

def SubstituteInputText1(val: float):
		'''
			
	returns true if field found
	
		'''
		pass # cpp source

def Step(n: int):
		'''
			
	 \see Wait()
	
		'''
		pass # cpp source

def Wait(ms: int):
		'''
			
	wait 'ms' milliseconds
	
		'''
		pass # cpp source

def back(steps: int =  1):
		'''
			
	Goes to one of previous dialogs in call stack
	
		'''
		pass # cpp source

def __open(Path: str):
		'''
			
	Opens window described by xml-file pointed by Path. If Path contains .3b file will be opened as 3B file.
	
		'''
		pass # cpp source

def run_script(path: str):
		'''
			
	 Run script by as-file pointed by Path
	
		'''
		pass # cpp source

def ppp(path: str):
		'''
			
	Opens model for PPP, if path is empty, shows open dialog
	
		'''
		pass # cpp source

def mv(path: str):
		'''
			
	Opens model for MV painting, if path is empty, shows open dialog
	
		'''
		pass # cpp source

def ptex(path: str):
		'''
			
	Opens model for Ptex, if path is empty, shows open dialog
	
		'''
		pass # cpp source

def import3DforStemCell():
		'''
			
	Import 3D model for stem cell certification
	
		'''
		pass # cpp source

def imagemesh():
		'''
			
	Import image as mesh, dialog will be shown
	
		'''
		pass # cpp source

def refmesh(path: str):
		'''
			
	Import mesh as reference, if path is empty dialog will be shown
	
		'''
		pass # cpp source

def vertexpaint1():
		'''
			
	Import mesh as reference, if path is empty dialog will be shown
	
		'''
		pass # cpp source

def vertexpaint(path: str):
		'''
			
	Import mesh for vertex painting, if path is empty dialog will be shown
	
		'''
		pass # cpp source

def autopo(path: str):
		'''
			
	Perform autopo over the mesh chosen in dialog
	
		'''
		pass # cpp source

def autopo1():
		'''
			
	Perform autopo over the mesh chosen in dialog
	
		'''
		pass # cpp source

def repair1():
		'''
			
	Perform autopo over the mesh chosen in dialog
	
		'''
		pass # cpp source

def repair(id: str):
		'''
			
	Opens mesh for repairing. If id contains "vox" then model will be voxelized, if there is substring "shell" then mesh will be imported as thin shell. Mesh Opening dialog will be shown.
	
		'''
		pass # cpp source

def bass():
		'''
			
	Activate bas-relief tool
	
		'''
		pass # cpp source

def undercut():
		'''
			
	Activale remove undercuts mode
	
		'''
		pass # cpp source

def autoscale():
		'''
			
	Activate perform autoscaling current mesh in voxel room
	
		'''
		pass # cpp source

def activate(id: str):
		'''
			
	Activate special voxel tool. id may be found in English.xml between <ID>...</ID> if you will find name of tool between <Text>...</Text> tags 
	
		'''
		pass # cpp source

def retopo():
		'''
			
	Activate retopo tool
	
		'''
		pass # cpp source

def retopopen():
		'''
			
	Open mesh using dialog and merge as retopo mesh
	
		'''
		pass # cpp source

def ToRoom(name: str):
		'''
			
	Activate any room - name is one of "Paint", "Tweak", "UV", "Retopo", "Render"
	
		'''
		pass # cpp source

def RoomExists(name: str):
		'''
			
	check if specified room exists
	
		'''
		pass # cpp source

def AddNewVolume(name: str):
		'''
			
	add new volume in voxel room. If name is empty name will be assigned automatically.
	
		'''
		pass # cpp source

def activate_uv():
		'''
			
	Activate UV room
	
		'''
		pass # cpp source

def stem():
		'''
			
	Activate StemTool
	
		'''
		pass # cpp source

def vox():
		'''
			
	Activate voxel room and add new volume
	
		'''
		pass # cpp source

def ResetPrimTransform():
		'''
			
	reset additional transformation for low-level primitives
	
		'''
		pass # cpp source

def PrimTranslate(dx: float, dy: float, dz: float):
		'''
			
	translate all further low-level promiteives
	
		'''
		pass # cpp source

def PrimScaleAt(x: float, y: float, z: float, scalex: float, scaley: float, scalez: float):
		'''
			
	scale all further low-level primitives using pivot point x,y,z
	
		'''
		pass # cpp source

def PrimRotateX(x: float, y: float, z: float, Angle: float):
		'''
			
	Rotate further primitives at xyz point around X-axis 
	
		'''
		pass # cpp source

def PrimRotateY(x: float, y: float, z: float, Angle: float):
		'''
			
	Rotate further primitives at xyz point around Y-axis
	
		'''
		pass # cpp source

def PrimRotateZ(x: float, y: float, z: float, Angle: float):
		'''
			
	Rotate further primitives at xyz point around Z-axis
	
		'''
		pass # cpp source

def PrimRotateAroundRode(x: float, y: float, z: float, xend: float, yend: float, zend: float, Angle: float):
		'''
			
	Rotate further primitives around rode (x,y,z)->(xend,yend,zend) on given Angle
	
		'''
		pass # cpp source

def PrimStretchBetweenPoints(x: float, y: float, z: float, xend: float, yend: float, zend: float):
		'''
			
	be actually applied as primitive stretched between points (x,y,z) and (xend,yend,zend)
	
		'''
		pass # cpp source

def PrimDensity(density: float):
		'''
			
	set additional density factor for low-level primitives. 1 means default density.
	
		'''
		pass # cpp source

def GetPrimTransform():
		'''
			
	store current transform for primitives as string to be kept for future usage
	
		'''
		pass # cpp source

def SetPrimTransform(M: str):
		'''
			
	restore current primitives transform from string that was previously kept using GetPrimTransform
	
		'''
		pass # cpp source

def sphere1(r: float):
		'''
			
	restore current primitives transform from string that was previously kept using GetPrimTransform
	
		'''
		pass # cpp source

def mk_sphere(x: float, y: float =  0, z: float =  0, r: float =  0, mode: int =  -1):
		'''
			
	mode==0 - add, 1 - subtract, 2 - intersect
	
		'''
		pass # cpp source

def mk_ellipse(x: float, y: float, z: float, rx: float, ry: float, rz: float, mode: int):
		'''
			
	mode==0 - add, 1 - subtract, 2 - intersect
	
		'''
		pass # cpp source

def mk_cube(x: float, y: float, z: float, sizex: float, sizey: float, sizez: float, mode: int):
		'''
			
	mode==0 - add, 1 - subtract, 2 - intersect
	
		'''
		pass # cpp source

def mk_cylinder(x: float, y: float, z: float, topradius: float, bottomradius: float, height: float, mode: int):
		'''
			
	create cylinder
	
		'''
		pass # cpp source

def mk_cone(x: float, y: float, z: float, radius: float, height: float, mode: int):
		'''
			
	create cone
	
		'''
		pass # cpp source

def mk_ngon(x: float, y: float, z: float, sides: int, topradius: float, bottomradius: float, height: float, mode: int):
		'''
			
	create nngon
	
		'''
		pass # cpp source

def mk_tube(x: float, y: float, z: float, topradius: float, bottomradius: float, height: float, wallthickness: float, mode: int):
		'''
			
	create tube
	
		'''
		pass # cpp source

def mk_ngontube(x: float, y: float, z: float, sides: int, topradius: float, bottomradius: float, height: float, wallthickness: float, mode: int):
		'''
			
	create n-gonal tube 
	
		'''
		pass # cpp source

def mk_capsule(x: float, y: float, z: float, xend: float, yend: float, zend: float, startradius: float, endradius: float, mode: int):
		'''
			
	creates capsule between points
	
		'''
		pass # cpp source

def surf():
		'''
			
	Turn all volumes to surface mode
	
		'''
		pass # cpp source

def cursurf():
		'''
			
	Turn current volume to the surface mode
	
		'''
		pass # cpp source

def voxelize():
		'''
			
	Turn current volume to voxel mode, voxelize if need
	
		'''
		pass # cpp source

def mergeopt(opt: str):
		'''
			
	example: mergeopt("[voxelize=true][as_skin=true][skin=4.5]");
	
		'''
		pass # cpp source

def merge1():
		'''
			
	example: mergeopt("[voxelize=true][as_skin=true][skin=4.5]");
	
		'''
		pass # cpp source

def merge(model: str):
		'''
			
	Merge model in voxel room. Empty string means that dialog will be shown.
	
		'''
		pass # cpp source

def mk_prim(id: str):
		'''
			
	Merge model in voxel room. Empty string means that dialog will be shown.
	
		'''
		pass # cpp source

def apply():
		'''
			
	Apply in Voxel room (press enter) 
	
		'''
		pass # cpp source

def ApplyAndKeepScale():
		'''
			
	Apply in Merge tool withous asking "Keep scale?". Scale will not be kept and scene scale will not be changed 
	
		'''
		pass # cpp source

def mapply():
		'''
			
	Apply in Voxel room (press enter) - with Medical=true 
	
		'''
		pass # cpp source

def recent3b():
		'''
			
	open recent 3B file
	
		'''
		pass # cpp source

def GetLastButtonIndex():
		'''
			
	get index of button pressed in last dialog. Usually OK=1, Cancel=2
	
		'''
		pass # cpp source

def FileDialogCancelPressed():
		'''
			
	returns true if Cancel pressed in last file dialod
	
		'''
		pass # cpp source

def WasRecentlyPressed(ID: str, Time: float):
		'''
			
	Was widget with identifier ID recently (within last Time sec) pressed?
	
		'''
		pass # cpp source

def WasRecentlyRMBPressed(ID: str, Time: float):
		'''
			
	Was widget with identifier ID recently (within last Time sec) pressed via RMB?
	
		'''
		pass # cpp source

def IsInTool(ToolID: str):
		'''
			
	Is user in tool identified as ID? To get current tool identifier press RMB+MMB over empty field 
	
		'''
		pass # cpp source

def IsDoubleClick(reset: bool =  False):
		'''
			
	 Is used double click ?
	
		'''
		pass # cpp source

def IsPressKeyID(keyID: int):
		'''
			
	Is press key ID?
	
		'''
		pass # cpp source

def Alt():
		'''
			
	 Is Alt pressed
	
		'''
		pass # cpp source

def GetCurrentToolID():
		'''
			
	Get active tool ID
	
		'''
		pass # cpp source

def GetTimeSinceStart():
		'''
			
	get time (sec) since script started
	
		'''
		pass # cpp source

def FindRecentlyPressed(IDS: str, Time: float):
		'''
			
	Find the widget that was pressed recently. IDS - strings ids. Return index of widget.
	
		'''
		pass # cpp source

def GetBottomBackgroundColor():
		'''
			
	App Options methods
	
		'''
		pass # cpp source

def GetTopBackgroundColor():
		'''
			
	App Options methods
	
		'''
		pass # cpp source

def SetBottomBackgroundColor(color: int):
		'''
			
	App Options methods
	
		'''
		pass # cpp source

def SetTopBackgroundColor(color: int):
		'''
			
	App Options methods
	
		'''
		pass # cpp source

def GetScreenWidth():
		'''
			
	Screen drawing functions
	
		'''
		pass # cpp source

def GetScreenHeight():
		'''
			
	Screen drawing functions
	
		'''
		pass # cpp source

def GetWorkAreaTop():
		'''
			
	Screen drawing functions
	
		'''
		pass # cpp source

def GetWorkAreaLeft():
		'''
			
	Screen drawing functions
	
		'''
		pass # cpp source

def GetWorkAreaWidth():
		'''
			
	Screen drawing functions
	
		'''
		pass # cpp source

def GetWorkAreaHeight():
		'''
			
	Screen drawing functions
	
		'''
		pass # cpp source

def DrawScreenLine(x1: float, y1: float, x2: float, y2: float, Color1: int, Color2: int):
		'''
			
	Draw line on screen - only to use after Step() instruction in cycle, othervice use will not see anything
	
		'''
		pass # cpp source

def DrawScreenFrame(x1: float, y1: float, x2: float, y2: float, Color: int):
		'''
			
	Draw frame
	
		'''
		pass # cpp source

def DrawScreenRect(x1: float, y1: float, x2: float, y2: float, Color: int):
		'''
			
	Draw filled rectangle
	
		'''
		pass # cpp source

def DrawScreenCircle(x: float, y: float, Radius: float, FillColor: int, LineColor: int):
		'''
			
	draw circle
	
		'''
		pass # cpp source

def DrawTextOnScreen(x: float, y: float, Color: int, align: int, text: str):
		'''
			
	draw text on screen, align=0 - left aligned, 1 - central align, 2 - right align 
	
		'''
		pass # cpp source

def HighlightUIElementsPY(IDS: str, time: float, explain: str, uType: int, Callback: any, callPressed: bool):
		'''
			
	highlighting the ui elements in python
	
		'''
		pass # cpp source

def HighlightUIElements(IDS: str, time: float, explain: str, utype: int, Callback: str, callPressed: bool =  True):
		'''
			
	highlighting the ui elements
	
		'''
		pass # cpp source

def HighlightUIBoolTreeElement(type: int, i: int, time: float):
		'''
			
	highlighting the bool element in tree branch (type & index = i)
	
		'''
		pass # cpp source

def HighlightUIBoolTreeElements(type: int, time: float, explain: str, uType: int, Callback: str, callPressed: bool =  True):
		'''
			
	highlighting the ui bool elements in the tree branch
	
		'''
		pass # cpp source

def WaitWhileNoExecuteCommand(CmdID: str, explain: str):
		'''
			
	 wait while command does'not executed 
	
		'''
		pass # cpp source

def WasDragNDropVoxTree(explain: str, dragMode: int):
		'''
			
	 Was drag&drop vox tree (dragmode = 1 add, 2 sub,3 - duplicate)
	
		'''
		pass # cpp source

def WasDroppedUIElement():
		'''
			
	Was dropped Ui element?
	
		'''
		pass # cpp source

def HighlightUIElement(IDS: str, time: float):
		'''
			
	highlight element with red rectangle
	
		'''
		pass # cpp source

def DeHighlightUIElement(ds: str):
		'''
			
	highlight element with red rectangle
	
		'''
		pass # cpp source

def GetTimeTickCount():
		'''
			
	highlight element with red rectangle
	
		'''
		pass # cpp source

def PenDrawVertex(icode: int, Callback: any):
		'''
			
	highlight element with red rectangle
	
		'''
		pass # cpp source

def IsSurface():
		'''
			
	returns true if current volume is in surface mode
	
		'''
		pass # cpp source

def CurVolumeIsEmpty():
		'''
			
	checks if volume is empty
	
		'''
		pass # cpp source

def GetCurVolumePolycount():
		'''
			
	Get current volume polycount
	
		'''
		pass # cpp source

def GetCurVolumeTransform():
		'''
			
	Get current volume polycount
	
		'''
		pass # cpp source

def SetCurVolumeTransform(str: cPy.cTypes.cMat4):
		'''
			
	Get current volume polycount
	
		'''
		pass # cpp source

def SetVolumesScaling(S: str):
		'''
			
	get/set current volume transform
	
		'''
		pass # cpp source

def GetCurVolumeSquare():
		'''
			
	get square
	
		'''
		pass # cpp source

def GetCurVolumeVolume():
		'''
			
	get volume
	
		'''
		pass # cpp source

def GetVoxSceneVisiblePolycount():
		'''
			
	Get polycount of whole voxel scene
	
		'''
		pass # cpp source

def GetVoxScenePolycount():
		'''
			
	Get polycount of visible volumes
	
		'''
		pass # cpp source

def IsInCache():
		'''
			
	Check if volume cached
	
		'''
		pass # cpp source

def ToCache():
		'''
			
	move current volume to cache
	
		'''
		pass # cpp source

def FromCache():
		'''
			
	restore current volume from cache
	
		'''
		pass # cpp source

def GetCurVolume():
		'''
			
	get current volume name
	
		'''
		pass # cpp source

def GetCurVolumeShader():
		'''
			
	get current volume shader name
	
		'''
		pass # cpp source

def SetCurVolumeShader(Name: str):
		'''
			
	set current volume shader name
	
		'''
		pass # cpp source

def RenameCurVolume(Name: str):
		'''
			
	rename current volume
	
		'''
		pass # cpp source

def GetVolumesCount():
		'''
			
	 volumes count 
	
		'''
		pass # cpp source

def GetVolumeLevel(name: str):
		'''
			
	 Get volume level by volume name
	
		'''
		pass # cpp source

def PlainMergeVisible(name: str):
		'''
			
	 Merge visible (no booleans)
	
		'''
		pass # cpp source

def SetCurVolumeMode(Surf: bool, Silent: bool, suggestedpoly: int =  0):
		'''
			
	If silent=true then no dialogs will be shown, all will be done by default
	
		'''
		pass # cpp source

def SetCurVolume(name: str):
		'''
			
	set current volume by name, returns true if succeed
	
		'''
		pass # cpp source

def IsCurVolume(name: str):
		'''
			
	check current volume by name, returns true if existed
	
		'''
		pass # cpp source

def IsChangeName(name: str, i: int):
		'''
			
	check current change volume by index from  name, returns true if changed
	
		'''
		pass # cpp source

def IsVisibleVolume(i: int):
		'''
			
	 check the visible volume by index i
	
		'''
		pass # cpp source

def IsVoxSurfVolume(i: int):
		'''
			
	 check the vox surface volume by index i
	
		'''
		pass # cpp source

def FindCurVolumeIndex():
		'''
			
	 find current index volume in vox tree branch
	
		'''
		pass # cpp source

def SelectFirstVolume(OnlyVisible: bool):
		'''
			
	select first volume in scene, if OnlyVisible==true then first visible volume will be selected
	
		'''
		pass # cpp source

def SelectNextVolume(OnlyVisible: bool):
		'''
			
	select next volume after current in tree, if OnlyVisible==true then next visible volume will be selected. Returns false if current volume is last in list
	
		'''
		pass # cpp source

def SetVolumeVisibility(vis: bool):
		'''
			
	sets volume visibility
	
		'''
		pass # cpp source

def GetVolumeVisibility():
		'''
			
	returns current volume visibility
	
		'''
		pass # cpp source

def SetVolumeGhosting(Ghosting: bool):
		'''
			
	sets Ghost property to volume
	
		'''
		pass # cpp source

def GetVolumeGhosting():
		'''
			
	get Ghost property from the volume
	
		'''
		pass # cpp source

def SetVolumeOpacity(Opacity: float):
		'''
			
	set opacity to current volume if the shader has corresponding property
	
		'''
		pass # cpp source

def SetVolumeColor(Color: int):
		'''
			
	set current volume color if this property of shader is available
	
		'''
		pass # cpp source

def SetShaderProperty(ID: str, val: str):
		'''
			
	assign val to current object shader field
	
		'''
		pass # cpp source

def AddPaintLayer(ID: str):
		'''
			
	add new paint layer
	
		'''
		pass # cpp source

def DeletePaintLayers():
		'''
			
	 delete all paint layers
	
		'''
		pass # cpp source

def DeletePaintLayer(ID: int):
		'''
			
	delete paint layer ID
	
		'''
		pass # cpp source

def GetCurrentPaintLayerName():
		'''
			
	get current paint layer name
	
		'''
		pass # cpp source

def PaintLayerNames():
		'''
			
	get the list of the layer names
	
		'''
		pass # cpp source

def GetLayerName(id: int):
		'''
			
	 get layer name by id
	
		'''
		pass # cpp source

def GetPaintLayersCount():
		'''
			
	 get count of paint layers
	
		'''
		pass # cpp source

def RenameCurrentPaintLayer(Name: str):
		'''
			
	 get count of paint layers
	
		'''
		pass # cpp source

def SelectPaintLayer(ID: str):
		'''
			
	select paint layer with name ID. Returns false if layer not found.
	
		'''
		pass # cpp source

def SelectFirstPaintLayer(visible: bool):
		'''
			
	select lowest paint layer. If visible=true, first visible paint layer will be selected
	
		'''
		pass # cpp source

def SelectNextPaintLayer(visible: bool):
		'''
			
	select next paint layer. Returns false if current layer is last and no new layer was selected. 
	
		'''
		pass # cpp source

def GetPaintLayerVisibility():
		'''
			
	get visibility of the current paint layer
	
		'''
		pass # cpp source

def SetPaintLayerVisibility(visible: bool):
		'''
			
	set visibility of current paint layer
	
		'''
		pass # cpp source

def SetPaintLayerOpacity(Percents: float):
		'''
			
	set opacity of the current paint layer
	
		'''
		pass # cpp source

def SetPaintLayerDepthOpacity(Percents: float):
		'''
			
	set opacity of the current paint layer
	
		'''
		pass # cpp source

def SetPaintLayerBlendingMode(ID: str):
		'''
			
	set blending mode of the current paint layer - ID-s are same as in English version
	
		'''
		pass # cpp source

def SetPaintLayerDepthBlendingMode(ID: str):
		'''
			
	set depth blending mode of the current paint layer - ID-s are same as in English version
	
		'''
		pass # cpp source

def AddRetopoLayer(ID: str):
		'''
			
	add new retopo layer
	
		'''
		pass # cpp source

def DeleteRetopoLayer():
		'''
			
	delete the current retopo layer
	
		'''
		pass # cpp source

def GetCurrentRetopoLayerName():
		'''
			
	 get current retopo layer name
	
		'''
		pass # cpp source

def RenameCurrentRetopoLayer(Name: str):
		'''
			
	 rename the current retopo layer
	
		'''
		pass # cpp source

def SelectRetopoLayer(ID: str):
		'''
			
	select retopo layer with name ID. Returns false if layer not found.
	
		'''
		pass # cpp source

def SelectFirstRetopoLayer(visible: bool):
		'''
			
	select lowest retopo layer. If visible=true, first visible retopo layer will be selected
	
		'''
		pass # cpp source

def SelectNextRetopoLayer(visible: bool):
		'''
			
	select next retopo layer. Returns false if current layer is last and no new layer was selected. 
	
		'''
		pass # cpp source

def GetRetopoLayerVisibility():
		'''
			
	get visibility of the current retopo layer
	
		'''
		pass # cpp source

def SetRetopoLayerVisibility(visible: bool):
		'''
			
	set visibility of current retopo layer
	
		'''
		pass # cpp source

def Execute(command: str, parameters: str):
		'''
			
	execute exe file or perform some action like open browser window etc
	
		'''
		pass # cpp source

def ReadFromFile(filename: str):
		'''
			
	file operations
	
		'''
		pass # cpp source

def WriteToFile(filename: str, text: str, append: bool):
		'''
			
	file operations
	
		'''
		pass # cpp source

def CheckIfFileExists1(filename: str):
		'''
			
	file operations
	
		'''
		pass # cpp source

def RemoveFile(filename: str):
		'''
			
	file operations
	
		'''
		pass # cpp source

def LogMessage(line: str):
		'''
			
	pring text to MyDocuments/3D-CoatV4/log.txt
	
		'''
		pass # cpp source

def _rand(min: int, max: int):
		'''
			
	generate integer random number min..max
	
		'''
		pass # cpp source

def _randF(min: float, max: float):
		'''
			
	generate floating random number min..max
	
		'''
		pass # cpp source

def _seed(val: int):
		'''
			
	set random generator seed
	
		'''
		pass # cpp source

def ProgressBar(message: str, pos: int):
		'''
			
	show progress bar pos = 0..100
	
		'''
		pass # cpp source

def SetOrthoMode(value: bool):
		'''
			
	Set orthogonal (true) or perspective (false) view mode
	
		'''
		pass # cpp source

def InstallToMenu(path: str, ItemName: str):
		'''
			
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	
		'''
		pass # cpp source

def AddFloatSlider(VariableName: str, Min: float, Max: float):
		'''
			
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	
		'''
		pass # cpp source

def AddIntSlider(VariableName: str, Min: int, Max: int):
		'''
			
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	
		'''
		pass # cpp source

def AddFloatInput(VariableName: str, EmptyName: bool):
		'''
			
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	
		'''
		pass # cpp source

def AddIntInput(VariableName: str, EmptyName: bool):
		'''
			
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	
		'''
		pass # cpp source

def AddStringInput(VariableName: str, EmptyName: bool):
		'''
			
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	
		'''
		pass # cpp source

def AddTextField(TextID: str, Align: int):
		'''
			
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	
		'''
		pass # cpp source

def AddDelimiter():
		'''
			
	1-center,0-left
	
		'''
		pass # cpp source

def AddButton(FuncName: str):
		'''
			
	1-center,0-left
	
		'''
		pass # cpp source

def Columns(nc: int):
		'''
			
	1-center,0-left
	
		'''
		pass # cpp source

def AddCheckBox(BoolVarRef: str):
		'''
			
	1-center,0-left
	
		'''
		pass # cpp source

def AddRadioButton(BoolVarRef: str, Group: int):
		'''
			
	1-center,0-left
	
		'''
		pass # cpp source

def AddDroplist(IntVarRef: str, CaseList: str):
		'''
			
	1-center,0-left
	
		'''
		pass # cpp source

def ClearControls():
		'''
			
	CaseList is list of possible values for droplist, delimiters are ,;|
	
		'''
		pass # cpp source

def AddTranslation(ID: str, Text: str):
		'''
			
	CaseList is list of possible values for droplist, delimiters are ,;|
	
		'''
		pass # cpp source

def UICondition(function: str):
		'''
			
	CaseList is list of possible values for droplist, delimiters are ,;|
	
		'''
		pass # cpp source

def StopUICondition():
		'''
			
	CaseList is list of possible values for droplist, delimiters are ,;|
	
		'''
		pass # cpp source

def GetMouseX():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def GetMouseY():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def GetPressure():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def LMBPressed():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def RMBPressed():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def MMBPressed():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def WheelPressed():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def GetVisiblePenRadius():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def StartStroke(x: float, y: float, Pressure: float):
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def DrawStrokeTo(x: float, y: float, Pressure: float):
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def EndStroke():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def ScreenRayPicksObject(x: float, y: float):
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def ScriptMessagePressButton(x: float, y: float):
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def MoveCursorTo(x: int, y: int):
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def ClickAtCurrentPosition():
		'''
			
	Screen - based direct control over mouse
	
		'''
		pass # cpp source

def GetMaterialsCount():
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetMaterialName(Index: int):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def RenameMaterial(Index: int, Name: str):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def DeleteMaterial(Index: int):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def LockMaterial(Index: int, Locked: bool):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def SetMaterialVisibility(Index: int, Visibility: bool):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def AddMaterial(Name: str):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetMaterialIndex(Name: str):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetObjectsCount():
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetObjectName(Index: int):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def RenameObject(Index: int, Name: str):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def DeleteObject1(Index: int):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def LockObject(Index: int, Locked: bool):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def SetObjectVisibility(Index: int, Visibility: bool):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def AddObject(Name: str):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetObjectIndex(Name: str):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def InRetopo():
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetUVSetsCount():
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetFacesCount():
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def GetUVSetName(Index: int):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def RenameUVSet(Index: int, Name: str):
		'''
			
	objects/materials management
	
		'''
		pass # cpp source

def SelectAllFacesInCurrentUVSet():
		'''
			
	int GetUVSetIndex(const cstring& Name);
	
		'''
		pass # cpp source

def SelectAllFacesInCurrentUVSetAndGroup():
		'''
			
	int GetUVSetIndex(const cstring& Name);
	
		'''
		pass # cpp source

def SelectAllVisibleFaces():
		'''
			
	int GetUVSetIndex(const cstring& Name);
	
		'''
		pass # cpp source

def UvSetForExportImport(Name: str):
		'''
			
	 Call it each time you need to perform the command from Textures->Import
	
		'''
		pass # cpp source

def ImportTexture(CommandInMenu: str, UvSetName: str, PathToTexture: str):
		'''
			
	The command allows to use all commands from Texture->Import without triggering the dialog
	Parameters:
	    CommandInMenu - command from Textures->Import menu, for example $LOADTEX, $LOADROUGHNESS, etc, anything from Textures->Import
	    UvSetName - Uv set name where you want to import texture
	    PathToTexture - full path to the texture
	
		'''
		pass # cpp source

def ExportObjectsAndTextures(Name: str):
		'''
			
	
	
		'''
		pass # cpp source

def DecimateToRetopo():
		'''
			
	
	
		'''
		pass # cpp source

def GetExportMeshName():
		'''
			
	
	
		'''
		pass # cpp source

def GetExportPathTextures():
		'''
			
	
	
		'''
		pass # cpp source

def SkipUndo(flag: bool):
		'''
			
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	
		'''
		pass # cpp source

def getCommandLine():
		'''
			
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	
		'''
		pass # cpp source

def SetGlobalVar(Name: str, Value: str):
		'''
			
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	
		'''
		pass # cpp source

def GetGlobalVar(Name: str):
		'''
			
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	
		'''
		pass # cpp source

def GetSceneFileName():
		'''
			
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	
		'''
		pass # cpp source

def SetSceneFileName(Name: str):
		'''
			
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	
		'''
		pass # cpp source

def GetGameIndex():
		'''
			
	games management
	
		'''
		pass # cpp source

def SetGameIndex(idx: int):
		'''
			
	0-regular coat, 1-cs:go, 2- rust
	
		'''
		pass # cpp source

def SetShowModalDlg():
		'''
			
	 show modal dialog; // true show, false hide
	
		'''
		pass # cpp source

def IsApprenticeBeginner():
		'''
			
	 is Apprentice begginer
	
		'''
		pass # cpp source

def IsRecordScript():
		'''
			
	 is Script recorder
	
		'''
		pass # cpp source

def UseRecordScript():
		'''
			
	 Use Script recorder
	
		'''
		pass # cpp source

def installPath():
		'''
			
	 \return A path where 3D-Coat was installed.
	
		'''
		pass # cpp source

def rwPath(userPath: str):
		'''
			
	 \return An absolute path with write folder of 3D-Coat plus 'userPath'.
	
		'''
		pass # cpp source

def homePath():
		'''
			
	 \return A path to home directory "~" (for example "/home/YourUserName")
	
		'''
		pass # cpp source

def EnablePenChannel(i: int, enabled: bool =  True):
		'''
			
	 enable/disable pen channels
	
		'''
		pass # cpp source

def IsEnabledPenChannel(i: int):
		'''
			
	 0 - is disabled, 1 - enabled
	
		'''
		pass # cpp source

def add_modal_callback():
		'''
			
	 add_modal_callback
	
		'''
		pass # cpp source

def remove_modal_callback():
		'''
			
	 remove_modal_callback
	
		'''
		pass # cpp source

def doc_mode():
		'''
			
	 doc_mode
	
		'''
		pass # cpp source
