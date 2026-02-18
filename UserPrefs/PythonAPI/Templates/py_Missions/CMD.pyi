#CMD
from typing import Any
from enum import Enum
def ModalDialog(ID: any, Caption: any) :
	'''
	Show model dialog with text identified ID. ID used to take translation from language xml or just may be shown directly if translation not found.
	'''
def GetLastDialogButtonIndex() :
	'''
	Show model dialog with text identified ID. ID used to take translation from language xml or just may be shown directly if translation not found.
	'''
def DontShowAgain(ID: any, Caption: any) :
	'''
	Show dialog with text identified ID. ID used to take translation from language xml or just may be shown directly if translation not found.
	'''
def ModalDialogOkCancel(ID: any, Caption: any) :
	'''
	Show dialog with text identified ID and two buttons - Ok and Cancel. Returns true if OK pressed, false if Cancel pressed. ID used to take translation from language xml or just may be shown directly if translation not found.
	'''
def ModalDialogYesNo(ID: any, Caption: any) :
	'''
	Show dialog with text identified ID and two buttons - Yes and No. Returns true if OK pressed, false if Cancel pressed. ID used to take translation from language xml or just may be shown directly if translation not found.
	'''
def PressInNextModalDialogs(ButtonIndex: int) :
	'''
	You should call PressInNextDialogs(-1) to stop automatical pressing of buttons.
	'''
def SetModalDialogCallback(name: any) :
	'''
	You may get name of current dialog name using next function
	'''
def RemoveModalDialogCallbacks() :
	'''
	remove all dialog callbacks
	'''
def GetCurrentDialog(ID: any, Caption: any) :
	'''
	returns true if you are in dialog now, also it retuns text and cation in current dialog to identify it
	'''
def ShowFloatingText(ID: any, FID: int) :
	'''
	show non-modal message on screen that will be hidden after some period of time
	'''
def GetFontID(ID: any, size: int, weight: int) :
	'''
	 gets the font id by font name
	'''
def GetFontFileID(fileNameID: any) :
	'''
	 gets the font id by font name
	'''
def GetTextID(ID: any) :
	'''
	 gets the string by id name
	'''
def SetScriptMessage(msg: any, sparam: any) :
	'''
	set script message and params that will be executed 
	'''
def SetFloatingMessage(x: int, y: int, strMessage: any, strColor: any) :
	'''
	set script floating message at point (x,y) 
	'''
def SetFloatingMessageBox(x: int, y: int, strMessage: any, strColor: any, uType: int) :
	'''
	set script floating message box at point (x,y) with uType (windows styles) 
	'''
def GetCommandStringMessageBox(x: int, y: int, strMessage: any, strColor: any, uType: int) :
	'''
	 get script floating message box at point (x,y) with uType (windows styles)
	'''
def SetFloatingMessageBoxTime(x: int, y: int, strMessage: any, strColor: any, uType: int, Time: int) :
	'''
	set script floating message box at point (x,y) with uType (windows styles) Time - time in mls
	'''
def ShowMessageWhilePressKey(x: int, y: int, msg: any, tcolor: any, key: int, callback: any) :
	'''
	set script message while press key
	'''
def ShowMessageWhileTime(x: int, y: int, msg: any, tcolor: any, time: float) :
	'''
	set script message while time is present
	'''
def OpenWorkSpace() :
	'''
	 open work space. file name load automatical from UI ui; ui.file("file.workspace");
	'''
def SaveWorkSpace() :
	'''
	 save work space. file name save automatical from UI ui; ui.file("file.workspace");
	'''
def OpenDialog(extensions: any, result: any) :
	'''
	function returns true if file is successfully chosen
	'''
def SaveDialog(extensions: any, result: any) :
	'''
	function returns true if file is successfully chosen
	'''
def SetFileForFileDialogs(name: any) :
	'''
	Use empty name "" to stop automatic file dialogs skipping othervice all next file dialogs will be skipped and it may lead to loosing data.
	'''
def RemoveFilePath(s: any) :
	'''
	file path management routines
	'''
def RemoveExtension(s: any) :
	'''
	file path management routines
	'''
def EnsureAbsolutePth(s: any) :
	'''
	file path management routines
	'''
def GetFilePath(s: any) :
	'''
	file path management routines
	'''
def GetFileExtension(s: any) :
	'''
	file path management routines
	'''
def GetFileName(s: any) :
	'''
	file path management routines
	'''
def CheckIfExists(s: any) :
	'''
	file path management routines
	'''
def CheckFolderExist(: str) :
	'''
	file path management routines
	'''
def CreatePath(s: any) :
	'''
	file path management routines
	'''
def SaveScreenShot(s: any, cutStrip: int =  0) :
	'''
	file path management routines
	'''
def CombineImages(im1: any, im2: any, imres: any) :
	'''
	file path management routines
	'''
def CompareImages(im1: any, im2: any, tolerance: int =  1) :
	'''
	 then they are equal, otherwise not equal.
	'''
def CompareImagesEx(im1: any, im2: any, tolerance: int, result: any) :
	'''
	 The parameter result contains the list of points <Point_i(Xi,Yi) with different values.
	'''
def ForEachFileInFolder(Folder: any, ExtList: any, Callback: any) :
	'''
	Ext list contains list of extensions like "*.jpg;*.png"
	'''
def cmd(ID: any) :
	'''
	Performs any action from user interface. To get ID of command hover required item with mouse and press MMB. Command ID will be copied to clipboard. Pay attention that if command is not present in current UV layout it will not be performed.
	'''
def GetBoolField(ID: any) :
	'''
	Get bool field from UI. ID has same meaning as in cmd
	'''
def SetBoolField(ID: any, val: bool) :
	'''
	returns true if set value successfuly
	'''
def GetSliderValue(ID: any) :
	'''
	Get value of slider in UI. ID has same meaning as in cmd
	'''
def SetSliderValue(ID: any, val: float) :
	'''
	returns true if set value successfuly
	'''
def SubstituteInputText(val: any) :
	'''
	returns true if field found
	'''
def SubstituteInputText1(val: float) :
	'''
	returns true if field found
	'''
def Step(n: int) :
	'''
	 \see Wait()
	'''
def Wait(ms: int) :
	'''
	wait 'ms' milliseconds
	'''
def back(steps: int =  1) :
	'''
	Goes to one of previous dialogs in call stack
	'''
def __open(Path: any) :
	'''
	Opens window described by xml-file pointed by Path. If Path contains .3b file will be opened as 3B file.
	'''
def run_script(path: any) :
	'''
	 Run script by as-file pointed by Path
	'''
def ppp(path: any) :
	'''
	Opens model for PPP, if path is empty, shows open dialog
	'''
def mv(path: any) :
	'''
	Opens model for MV painting, if path is empty, shows open dialog
	'''
def ptex(path: any) :
	'''
	Opens model for Ptex, if path is empty, shows open dialog
	'''
def import3DforStemCell() :
	'''
	Import 3D model for stem cell certification
	'''
def imagemesh() :
	'''
	Import image as mesh, dialog will be shown
	'''
def refmesh(path: any) :
	'''
	Import mesh as reference, if path is empty dialog will be shown
	'''
def vertexpaint1() :
	'''
	Import mesh as reference, if path is empty dialog will be shown
	'''
def vertexpaint(path: any) :
	'''
	Import mesh for vertex painting, if path is empty dialog will be shown
	'''
def autopo(path: any) :
	'''
	Perform autopo over the mesh chosen in dialog
	'''
def autopo1() :
	'''
	Perform autopo over the mesh chosen in dialog
	'''
def repair1() :
	'''
	Perform autopo over the mesh chosen in dialog
	'''
def repair(id: any) :
	'''
	Opens mesh for repairing. If id contains "vox" then model will be voxelized, if there is substring "shell" then mesh will be imported as thin shell. Mesh Opening dialog will be shown.
	'''
def bass() :
	'''
	Activate bas-relief tool
	'''
def undercut() :
	'''
	Activale remove undercuts mode
	'''
def autoscale() :
	'''
	Activate perform autoscaling current mesh in voxel room
	'''
def activate(id: any) :
	'''
	Activate special voxel tool. id may be found in English.xml between <ID>...</ID> if you will find name of tool between <Text>...</Text> tags 
	'''
def retopo() :
	'''
	Activate retopo tool
	'''
def retopopen() :
	'''
	Open mesh using dialog and merge as retopo mesh
	'''
def ToRoom(name: any) :
	'''
	Activate any room - name is one of "Paint", "Tweak", "UV", "Retopo", "Render"
	'''
def RoomExists(name: any) :
	'''
	check if specified room exists
	'''
def AddNewVolume(name: any) :
	'''
	add new volume in voxel room. If name is empty name will be assigned automatically.
	'''
def activate_uv() :
	'''
	Activate UV room
	'''
def stem() :
	'''
	Activate StemTool
	'''
def vox() :
	'''
	Activate voxel room and add new volume
	'''
def ResetPrimTransform() :
	'''
	reset additional transformation for low-level primitives
	'''
def PrimTranslate(dx: float, dy: float, dz: float) :
	'''
	translate all further low-level promiteives
	'''
def PrimScaleAt(x: float, y: float, z: float, scalex: float, scaley: float, scalez: float) :
	'''
	scale all further low-level primitives using pivot point x,y,z
	'''
def PrimRotateX(x: float, y: float, z: float, Angle: float) :
	'''
	Rotate further primitives at xyz point around X-axis 
	'''
def PrimRotateY(x: float, y: float, z: float, Angle: float) :
	'''
	Rotate further primitives at xyz point around Y-axis
	'''
def PrimRotateZ(x: float, y: float, z: float, Angle: float) :
	'''
	Rotate further primitives at xyz point around Z-axis
	'''
def PrimRotateAroundRode(x: float, y: float, z: float, xend: float, yend: float, zend: float, Angle: float) :
	'''
	Rotate further primitives around rode (x,y,z)->(xend,yend,zend) on given Angle
	'''
def PrimStretchBetweenPoints(x: float, y: float, z: float, xend: float, yend: float, zend: float) :
	'''
	be actually applied as primitive stretched between points (x,y,z) and (xend,yend,zend)
	'''
def PrimDensity(density: float) :
	'''
	set additional density factor for low-level primitives. 1 means default density.
	'''
def GetPrimTransform() :
	'''
	store current transform for primitives as string to be kept for future usage
	'''
def SetPrimTransform(M: any) :
	'''
	restore current primitives transform from string that was previously kept using GetPrimTransform
	'''
def sphere1(r: float) :
	'''
	restore current primitives transform from string that was previously kept using GetPrimTransform
	'''
def mk_sphere(x: float, y: float =  0, z: float =  0, r: float =  0, mode: int =  -1) :
	'''
	mode==0 - add, 1 - subtract, 2 - intersect
	'''
def mk_ellipse(x: float, y: float, z: float, rx: float, ry: float, rz: float, mode: int) :
	'''
	mode==0 - add, 1 - subtract, 2 - intersect
	'''
def mk_cube(x: float, y: float, z: float, sizex: float, sizey: float, sizez: float, mode: int) :
	'''
	mode==0 - add, 1 - subtract, 2 - intersect
	'''
def mk_cylinder(x: float, y: float, z: float, topradius: float, bottomradius: float, height: float, mode: int) :
	'''
	create cylinder
	'''
def mk_cone(x: float, y: float, z: float, radius: float, height: float, mode: int) :
	'''
	create cone
	'''
def mk_ngon(x: float, y: float, z: float, sides: int, topradius: float, bottomradius: float, height: float, mode: int) :
	'''
	create nngon
	'''
def mk_tube(x: float, y: float, z: float, topradius: float, bottomradius: float, height: float, wallthickness: float, mode: int) :
	'''
	create tube
	'''
def mk_ngontube(x: float, y: float, z: float, sides: int, topradius: float, bottomradius: float, height: float, wallthickness: float, mode: int) :
	'''
	create n-gonal tube 
	'''
def mk_capsule(x: float, y: float, z: float, xend: float, yend: float, zend: float, startradius: float, endradius: float, mode: int) :
	'''
	creates capsule between points
	'''
def surf() :
	'''
	Turn all volumes to surface mode
	'''
def cursurf() :
	'''
	Turn current volume to the surface mode
	'''
def voxelize() :
	'''
	Turn current volume to voxel mode, voxelize if need
	'''
def mergeopt(opt: any) :
	'''
	example: mergeopt("[voxelize=true][as_skin=true][skin=4.5]");
	'''
def merge1() :
	'''
	example: mergeopt("[voxelize=true][as_skin=true][skin=4.5]");
	'''
def merge(model: any) :
	'''
	Merge model in voxel room. Empty string means that dialog will be shown.
	'''
def mk_prim(id: str) :
	'''
	Merge model in voxel room. Empty string means that dialog will be shown.
	'''
def apply() :
	'''
	Apply in Voxel room (press enter) 
	'''
def ApplyAndKeepScale() :
	'''
	Apply in Merge tool withous asking "Keep scale?". Scale will not be kept and scene scale will not be changed 
	'''
def mapply() :
	'''
	Apply in Voxel room (press enter) - with Medical=true 
	'''
def recent3b() :
	'''
	open recent 3B file
	'''
def GetLastButtonIndex() :
	'''
	get index of button pressed in last dialog. Usually OK=1, Cancel=2
	'''
def FileDialogCancelPressed() :
	'''
	returns true if Cancel pressed in last file dialod
	'''
def WasRecentlyPressed(ID: any, Time: float) :
	'''
	Was widget with identifier ID recently (within last Time sec) pressed?
	'''
def WasRecentlyRMBPressed(ID: any, Time: float) :
	'''
	Was widget with identifier ID recently (within last Time sec) pressed via RMB?
	'''
def IsInTool(ToolID: any) :
	'''
	Is user in tool identified as ID? To get current tool identifier press RMB+MMB over empty field 
	'''
def IsDoubleClick(reset: bool =  false) :
	'''
	 Is used double click ?
	'''
def IsPressKeyID(keyID: int) :
	'''
	Is press key ID?
	'''
def Alt() :
	'''
	 Is Alt pressed
	'''
def GetCurrentToolID() :
	'''
	Get active tool ID
	'''
def GetTimeSinceStart() :
	'''
	get time (sec) since script started
	'''
def FindRecentlyPressed(IDS: any, Time: float) :
	'''
	Find the widget that was pressed recently. IDS - strings ids. Return index of widget.
	'''
def GetBottomBackgroundColor() :
	'''
	App Options methods
	'''
def GetTopBackgroundColor() :
	'''
	App Options methods
	'''
def SetBottomBackgroundColor(color: int) :
	'''
	App Options methods
	'''
def SetTopBackgroundColor(color: int) :
	'''
	App Options methods
	'''
def GetScreenWidth() :
	'''
	Screen drawing functions
	'''
def GetScreenHeight() :
	'''
	Screen drawing functions
	'''
def GetWorkAreaTop() :
	'''
	Screen drawing functions
	'''
def GetWorkAreaLeft() :
	'''
	Screen drawing functions
	'''
def GetWorkAreaWidth() :
	'''
	Screen drawing functions
	'''
def GetWorkAreaHeight() :
	'''
	Screen drawing functions
	'''
def DrawScreenLine(x1: float, y1: float, x2: float, y2: float, Color1: int, Color2: int) :
	'''
	Draw line on screen - only to use after Step() instruction in cycle, othervice use will not see anything
	'''
def DrawScreenFrame(x1: float, y1: float, x2: float, y2: float, Color: int) :
	'''
	Draw frame
	'''
def DrawScreenRect(x1: float, y1: float, x2: float, y2: float, Color: int) :
	'''
	Draw filled rectangle
	'''
def DrawScreenCircle(x: float, y: float, Radius: float, FillColor: int, LineColor: int) :
	'''
	draw circle
	'''
def DrawTextOnScreen(x: float, y: float, Color: int, align: int, text: any) :
	'''
	draw text on screen, align=0 - left aligned, 1 - central align, 2 - right align 
	'''
def HighlightUIElements(IDS: any, time: float, explain: any, utype: int, Callback: any, callPressed: bool =  true) :
	'''
	highlighting the ui elements
	'''
def HighlightUIBoolTreeElement(type: int, i: int, time: float) :
	'''
	highlighting the bool element in tree branch (type & index = i)
	'''
def HighlightUIBoolTreeElements(type: int, time: float, explain: any, uType: int, Callback: any, callPressed: bool =  true) :
	'''
	highlighting the ui bool elements in the tree branch
	'''
def WaitWhileNoExecuteCommand(CmdID: any, explain: any) :
	'''
	 wait while command does'not executed 
	'''
def WasDragNDropVoxTree(explain: any, dragMode: int) :
	'''
	 Was drag&drop vox tree (dragmode = 1 add, 2 sub,3 - duplicate)
	'''
def WasDroppedUIElement() :
	'''
	Was dropped Ui element?
	'''
def HighlightUIElement(IDS: any, time: float) :
	'''
	highlight element with red rectangle
	'''
def DeHighlightUIElement(ds: any) :
	'''
	highlight element with red rectangle
	'''
def GetTimeTickCount() :
	'''
	highlight element with red rectangle
	'''
def PenDrawVertex(icode: int, Callback: any) :
	'''
	highlight element with red rectangle
	'''
def IsSurface() :
	'''
	returns true if current volume is in surface mode
	'''
def CurVolumeIsEmpty() :
	'''
	checks if volume is empty
	'''
def GetCurVolumePolycount() :
	'''
	Get current volume polycount
	'''
def GetCurVolumeTransform() :
	'''
	Get current volume polycount
	'''
def SetCurVolumeTransform(str: any) :
	'''
	Get current volume polycount
	'''
def SetVolumesScaling(S: any) :
	'''
	get/set current volume transform
	'''
def GetCurVolumeSquare() :
	'''
	get square
	'''
def GetCurVolumeVolume() :
	'''
	get volume
	'''
def GetVoxSceneVisiblePolycount() :
	'''
	Get polycount of whole voxel scene
	'''
def GetVoxScenePolycount() :
	'''
	Get polycount of visible volumes
	'''
def IsInCache() :
	'''
	Check if volume cached
	'''
def ToCache() :
	'''
	move current volume to cache
	'''
def FromCache() :
	'''
	restore current volume from cache
	'''
def GetCurVolume() :
	'''
	get current volume name
	'''
def GetCurVolumeShader() :
	'''
	get current volume shader name
	'''
def SetCurVolumeShader(Name: any) :
	'''
	set current volume shader name
	'''
def RenameCurVolume(Name: any) :
	'''
	rename current volume
	'''
def GetVolumesCount() :
	'''
	 volumes count 
	'''
def GetVolumeLevel(name: any) :
	'''
	 Get volume level by volume name
	'''
def PlainMergeVisible(name: any) :
	'''
	 Merge visible (no booleans)
	'''
def SetCurVolumeMode(Surf: bool, Silent: bool, suggestedpoly: int =  0) :
	'''
	If silent=true then no dialogs will be shown, all will be done by default
	'''
def SetCurVolume(name: any) :
	'''
	set current volume by name, returns true if succeed
	'''
def IsCurVolume(name: any) :
	'''
	check current volume by name, returns true if existed
	'''
def IsChangeName(name: any, i: int) :
	'''
	check current change volume by index from  name, returns true if changed
	'''
def IsVisibleVolume(i: int) :
	'''
	 check the visible volume by index i
	'''
def IsVoxSurfVolume(i: int) :
	'''
	 check the vox surface volume by index i
	'''
def FindCurVolumeIndex() :
	'''
	 find current index volume in vox tree branch
	'''
def SelectFirstVolume(OnlyVisible: bool) :
	'''
	select first volume in scene, if OnlyVisible==true then first visible volume will be selected
	'''
def SelectNextVolume(OnlyVisible: bool) :
	'''
	select next volume after current in tree, if OnlyVisible==true then next visible volume will be selected. Returns false if current volume is last in list
	'''
def SetVolumeVisibility(vis: bool) :
	'''
	sets volume visibility
	'''
def GetVolumeVisibility() :
	'''
	returns current volume visibility
	'''
def SetVolumeGhosting(Ghosting: bool) :
	'''
	sets Ghost property to volume
	'''
def GetVolumeGhosting() :
	'''
	get Ghost property from the volume
	'''
def SetVolumeOpacity(Opacity: float) :
	'''
	set opacity to current volume if the shader has corresponding property
	'''
def SetVolumeColor(Color: int) :
	'''
	set current volume color if this property of shader is available
	'''
def SetShaderProperty(ID: any, val: any) :
	'''
	assign val to current object shader field
	'''
def AddPaintLayer(ID: any) :
	'''
	add new paint layer
	'''
def DeletePaintLayers() :
	'''
	 delete all paint layers
	'''
def DeletePaintLayer(ID: int) :
	'''
	delete paint layer ID
	'''
def GetCurrentPaintLayerName() :
	'''
	get current paint layer name
	'''
def PaintLayerNames() :
	'''
	get the list of the layer names
	'''
def GetLayerName(id: int) :
	'''
	 get layer name by id
	'''
def GetPaintLayersCount() :
	'''
	 get count of paint layers
	'''
def RenameCurrentPaintLayer(Name: any) :
	'''
	 get count of paint layers
	'''
def SelectPaintLayer(ID: any) :
	'''
	select paint layer with name ID. Returns false if layer not found.
	'''
def SelectFirstPaintLayer(visible: bool) :
	'''
	select lowest paint layer. If visible=true, first visible paint layer will be selected
	'''
def SelectNextPaintLayer(visible: bool) :
	'''
	select next paint layer. Returns false if current layer is last and no new layer was selected. 
	'''
def GetPaintLayerVisibility() :
	'''
	get visibility of the current paint layer
	'''
def SetPaintLayerVisibility(visible: bool) :
	'''
	set visibility of current paint layer
	'''
def SetPaintLayerOpacity(Percents: float) :
	'''
	set opacity of the current paint layer
	'''
def SetPaintLayerDepthOpacity(Percents: float) :
	'''
	set opacity of the current paint layer
	'''
def SetPaintLayerBlendingMode(ID: any) :
	'''
	set blending mode of the current paint layer - ID-s are same as in English version
	'''
def SetPaintLayerDepthBlendingMode(ID: any) :
	'''
	set depth blending mode of the current paint layer - ID-s are same as in English version
	'''
def AddRetopoLayer(ID: any) :
	'''
	add new retopo layer
	'''
def DeleteRetopoLayer() :
	'''
	delete the current retopo layer
	'''
def GetCurrentRetopoLayerName() :
	'''
	 get current retopo layer name
	'''
def RenameCurrentRetopoLayer(Name: any) :
	'''
	 rename the current retopo layer
	'''
def SelectRetopoLayer(ID: any) :
	'''
	select retopo layer with name ID. Returns false if layer not found.
	'''
def SelectFirstRetopoLayer(visible: bool) :
	'''
	select lowest retopo layer. If visible=true, first visible retopo layer will be selected
	'''
def SelectNextRetopoLayer(visible: bool) :
	'''
	select next retopo layer. Returns false if current layer is last and no new layer was selected. 
	'''
def GetRetopoLayerVisibility() :
	'''
	get visibility of the current retopo layer
	'''
def SetRetopoLayerVisibility(visible: bool) :
	'''
	set visibility of current retopo layer
	'''
def Execute(command: any, parameters: any) :
	'''
	execute exe file or perform some action like open browser window etc
	'''
def ReadFromFile(filename: any) :
	'''
	file operations
	'''
def WriteToFile(filename: any, text: any, append: bool) :
	'''
	file operations
	'''
def CheckIfFileExists1(filename: any) :
	'''
	file operations
	'''
def RemoveFile(filename: any) :
	'''
	file operations
	'''
def LogMessage(line: any) :
	'''
	pring text to MyDocuments/3D-CoatV4/log.txt
	'''
def _rand(min: int, max: int) :
	'''
	generate integer random number min..max
	'''
def _randF(min: float, max: float) :
	'''
	generate floating random number min..max
	'''
def _seed(val: int) :
	'''
	set random generator seed
	'''
def ProgressBar(message: any, pos: int) :
	'''
	show progress bar pos = 0..100
	'''
def SetOrthoMode(value: bool) :
	'''
	Set orthogonal (true) or perspective (false) view mode
	'''
def InstallToMenu(path: any, ItemName: any) :
	'''
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	'''
def AddFloatSlider(VariableName: any, Min: float, Max: float) :
	'''
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	'''
def AddIntSlider(VariableName: any, Min: int, Max: int) :
	'''
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	'''
def AddFloatInput(VariableName: any, EmptyName: bool) :
	'''
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	'''
def AddIntInput(VariableName: any, EmptyName: bool) :
	'''
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	'''
def AddStringInput(VariableName: any, EmptyName: bool) :
	'''
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	'''
def AddTextField(TextID: any, Align: int) :
	'''
	creates new menu item and will run this script. Path is just path to menu like File.Export or Voxels or Retopo
	'''
def AddDelimiter() :
	'''
	1-center,0-left
	'''
def AddButton(FuncName: any) :
	'''
	1-center,0-left
	'''
def Columns(nc: int) :
	'''
	1-center,0-left
	'''
def AddCheckBox(BoolVarRef: any) :
	'''
	1-center,0-left
	'''
def AddRadioButton(BoolVarRef: any, Group: int) :
	'''
	1-center,0-left
	'''
def AddDroplist(IntVarRef: any, CaseList: any) :
	'''
	1-center,0-left
	'''
def ClearControls() :
	'''
	CaseList is list of possible values for droplist, delimiters are ,;|
	'''
def AddTranslation(ID: any, Text: any) :
	'''
	CaseList is list of possible values for droplist, delimiters are ,;|
	'''
def UICondition(function: any) :
	'''
	CaseList is list of possible values for droplist, delimiters are ,;|
	'''
def StopUICondition() :
	'''
	CaseList is list of possible values for droplist, delimiters are ,;|
	'''
def GetMouseX() :
	'''
	Screen - based direct control over mouse
	'''
def GetMouseY() :
	'''
	Screen - based direct control over mouse
	'''
def GetPressure() :
	'''
	Screen - based direct control over mouse
	'''
def LMBPressed() :
	'''
	Screen - based direct control over mouse
	'''
def RMBPressed() :
	'''
	Screen - based direct control over mouse
	'''
def MMBPressed() :
	'''
	Screen - based direct control over mouse
	'''
def WheelPressed() :
	'''
	Screen - based direct control over mouse
	'''
def GetVisiblePenRadius() :
	'''
	Screen - based direct control over mouse
	'''
def StartStroke(x: float, y: float, Pressure: float) :
	'''
	Screen - based direct control over mouse
	'''
def DrawStrokeTo(x: float, y: float, Pressure: float) :
	'''
	Screen - based direct control over mouse
	'''
def EndStroke() :
	'''
	Screen - based direct control over mouse
	'''
def ScreenRayPicksObject(x: float, y: float) :
	'''
	Screen - based direct control over mouse
	'''
def ScriptMessagePressButton(x: float, y: float) :
	'''
	Screen - based direct control over mouse
	'''
def MoveCursorTo(x: int, y: int) :
	'''
	Screen - based direct control over mouse
	'''
def ClickAtCurrentPosition() :
	'''
	Screen - based direct control over mouse
	'''
def GetMaterialsCount() :
	'''
	objects/materials management
	'''
def GetMaterialName(Index: int) :
	'''
	objects/materials management
	'''
def RenameMaterial(Index: int, Name: any) :
	'''
	objects/materials management
	'''
def DeleteMaterial(Index: int) :
	'''
	objects/materials management
	'''
def LockMaterial(Index: int, Locked: bool) :
	'''
	objects/materials management
	'''
def SetMaterialVisibility(Index: int, Visibility: bool) :
	'''
	objects/materials management
	'''
def AddMaterial(Name: any) :
	'''
	objects/materials management
	'''
def GetMaterialIndex(Name: any) :
	'''
	objects/materials management
	'''
def GetObjectsCount() :
	'''
	objects/materials management
	'''
def GetObjectName(Index: int) :
	'''
	objects/materials management
	'''
def RenameObject(Index: int, Name: any) :
	'''
	objects/materials management
	'''
def DeleteObject1(Index: int) :
	'''
	objects/materials management
	'''
def LockObject(Index: int, Locked: bool) :
	'''
	objects/materials management
	'''
def SetObjectVisibility(Index: int, Visibility: bool) :
	'''
	objects/materials management
	'''
def AddObject(Name: any) :
	'''
	objects/materials management
	'''
def GetObjectIndex(Name: any) :
	'''
	objects/materials management
	'''
def InRetopo() :
	'''
	objects/materials management
	'''
def GetUVSetsCount() :
	'''
	objects/materials management
	'''
def GetFacesCount() :
	'''
	objects/materials management
	'''
def GetUVSetName(Index: int) :
	'''
	objects/materials management
	'''
def RenameUVSet(Index: int, Name: any) :
	'''
	objects/materials management
	'''
def SelectAllFacesInCurrentUVSet() :
	'''
	int GetUVSetIndex(const cstring& Name);
	'''
def SelectAllFacesInCurrentUVSetAndGroup() :
	'''
	int GetUVSetIndex(const cstring& Name);
	'''
def SelectAllVisibleFaces() :
	'''
	int GetUVSetIndex(const cstring& Name);
	'''
def UvSetForExportImport(Name: any) :
	'''
	 Call it each time you need to perform the command from Textures->Import
	'''
def ImportTexture(CommandInMenu: any, UvSetName: any, PathToTexture: any) :
	'''
	The command allows to use all commands from Texture->Import without triggering the dialog
	Parameters:
	    CommandInMenu - command from Textures->Import menu, for example $LOADTEX, $LOADROUGHNESS, etc, anything from Textures->Import
	    UvSetName - Uv set name where you want to import texture
	    PathToTexture - full path to the texture
	'''
def ExportObjectsAndTextures(Name: any) :
	'''
	
	'''
def DecimateToRetopo() :
	'''
	
	'''
def GetExportMeshName() :
	'''
	
	'''
def GetExportPathTextures() :
	'''
	
	'''
def SkipUndo(flag: bool) :
	'''
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	'''
def getCommandLine() :
	'''
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	'''
def SetGlobalVar(Name: any, Value: any) :
	'''
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	'''
def GetGlobalVar(Name: any) :
	'''
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	'''
def GetSceneFileName() :
	'''
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	'''
def SetSceneFileName(Name: any) :
	'''
	The command allows to skip undo
	Parameters:
	        flag to skip (true/false)
	'''
def GetGameIndex() :
	'''
	games management
	'''
def SetGameIndex(idx: int) :
	'''
	0-regular coat, 1-cs:go, 2- rust
	'''
def SetShowModalDlg() :
	'''
	 show modal dialog; // true show, false hide
	'''
def IsApprenticeBeginner() :
	'''
	 is Apprentice begginer
	'''
def IsRecordScript() :
	'''
	 is Script recorder
	'''
def UseRecordScript() :
	'''
	 Use Script recorder
	'''
def installPath() :
	'''
	 \return A path where 3D-Coat was installed.
	'''
def rwPath(userPath: any) :
	'''
	 \return An absolute path with write folder of 3D-Coat plus 'userPath'.
	'''
def homePath() :
	'''
	 \return A path to home directory "~" (for example "/home/YourUserName")
	'''
def EnablePenChannel(i: int, enabled: bool =  true) :
	'''
	 enable/disable pen channels
	'''
def IsEnabledPenChannel(i: int) :
	'''
	 0 - is disabled, 1 - enabled
	'''
def RegisterScriptFunctions(: any) :
	'''
	 0 - is disabled, 1 - enabled
	'''
def RegisterScriptClasses(: any) :
	'''
	 0 - is disabled, 1 - enabled
	'''
def add_modal_callback() :
	'''
	 add_modal_callback
	'''
def remove_modal_callback() :
	'''
	 remove_modal_callback
	'''
def doc_mode() :
	'''
	 doc_mode
	'''
