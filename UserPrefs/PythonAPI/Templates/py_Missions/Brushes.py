# Mission 2 : The brush selection.
import coat
import CMD
import logging
import math
from coat import vec3
from coat import Mesh

_debugmode = False

logging.basicConfig(filename='pyLogger.log', format='%(asctime)s %(message)s', filemode ='w')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def log(x):
    if _debugmode:
        logger.debug(x)

mission_Explain_ID = "Brushes_Explain"
mission_Complete_ID = "Mission_Complete"
mission_No_Complete_ID = "Mission_Not_Complete"
mission_Abort = "Mission_Abort"

orange_Color = "4292730333"
cmd_MSG = ""
codeDone = 0
X0 = 0
Y0 = 0

def GoToStartMission():
    CMD.SetShowModalDlg(False)
    coat.ui.cmd("$SETPAGE_Sculpt")
    coat.ui.cmd("$CLEARSCENE")
    coat.ui.cmd("$START_MENU_smMission")
    CMD.SetShowModalDlg(True)
		
#check press 
def GetPressButton():
    Status = -1
    if CMD.LMBPressed():
        x=float(CMD.GetMouseX()) 
        y=float(CMD.GetMouseY())
        Status = CMD.ScriptMessagePressButton(x,y)
    return Status

def DrawBrush(idx): 
    ds = 100
    if idx == 0:
       msg_draw = "Change_Brush_Size_Draw"
    elif idx==1:
         msg_draw = "Change_Brush_Depth_Draw"
         ds = 120
    else:
       msg_draw = "Change_Brush_Smooth_Draw"
       ds = 150
      
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
        
    CMD.SetFloatingMessageBox(XX, YY, msg_draw, orange_Color,4)
    noExit = True
    iret = 0
    nstatus = 0
    bFirst = True
      
    while noExit:
        CMD.Step(1)
        istatus = GetPressButton()
        if istatus!=-1:
            noExit = False
            iret = istatus
        elif nstatus > 1:
             noExit = False
             iret = nstatus
        while CMD.LMBPressed(): 
            CMD.Step(1)
            x=float(CMD.GetMouseX()) 
            y=float(CMD.GetMouseY())
            bObj = bool(CMD.ScreenRayPicksObject(x,y))
            if bObj:
                if bFirst:
                    xStart=float(CMD.GetMouseX()) 
                    yStart=float(CMD.GetMouseY())
                    bFirst=False
                x=float(CMD.GetMouseX()) 
                y=float(CMD.GetMouseY())
                if abs(x-xStart) > ds or abs(y-yStart) > ds:
                    nstatus = nstatus + 1
                    bFirst=True
                    break
            if CMD.IsPressKeyID(0x1B):
                noExit = False
        bFirst=True

    if nstatus > 0:
       CMD.SetScriptMessage("reset","")
       CMD.SetFloatingMessage(XX,YY,"Well_Done",orange_Color)
       CMD.Wait( 2000 )
     
    CMD.SetScriptMessage("reset","")
    return iret
    
#1 method
def CheckBrushSize():
  global codeDone
  bFirst = True
  noExit = True
  statusOK = 0
  explain = "Change_Brush_Size"
  
  iret = 2
  #2 method next 
	
  XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
  YY = int(8 * CMD.GetWorkAreaHeight() / 100)
  
  coat.ui.cmd("$[Page4]Buildup")
  CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color,3)
  
  while noExit:
    CMD.Step(2)
    istatus = GetPressButton()
    bObj = True
    if istatus!=-1:
        noExit = False
        iret = istatus
    if CMD.RMBPressed():
        if bFirst:
            xStart = float(CMD.GetMouseX()) 
            yStart = float(CMD.GetMouseY())
            bObj = CMD.ScreenRayPicksObject(xStart,yStart)
            bFirst = False
            
    while CMD.RMBPressed():
        CMD.Step(1)
        x=float(CMD.GetMouseX()) 
        y=float(CMD.GetMouseY())
        if bObj: 
            x1=float(CMD.GetMouseX()) 
            y1=float(CMD.GetMouseY())
            if abs(x1-xStart) > 20:
                statusOK |= 1
                break
        if CMD.IsPressKeyID(0x1B):
            noExit = False
            
    while CMD.WheelPressed():  
        CMD.Step(1)
        x=float(CMD.GetMouseX()) 
        y=float(CMD.GetMouseY())
        bObj = bool(CMD.ScreenRayPicksObject(x,y))
        if bObj:
           statusOK |= 2
           break
    bFirst = True
    if CMD.IsPressKeyID(0x1B):
        noExit = False
    if statusOK == 0x03: 
        CMD.SetScriptMessage("reset","")
        CMD.SetFloatingMessage(XX,YY,"Well_Done",orange_Color)
        CMD.Wait( 2000 )
        CMD.SetScriptMessage("reset","")
        noExit = False
        codeDone = codeDone + 1
    if noExit == False:
       break
  CMD.SetScriptMessage("reset","")
  return iret
  
#2 method
def CheckBrushDepth():
    global codeDone
    bFirst = True
    noExit = True
    statusOK = 0
    explain = "Change_Brush_Depth"
      
    iret = 3  #next method
      
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
      
    coat.ui.cmd("$[Page4]Buildup")
    CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color,4)
    while noExit:
        CMD.Step(1) 
        istatus = GetPressButton()
        bObj = True
        if istatus!=-1: 
            noExit = False
            if istatus == 1: 
                iret = 1
            if istatus == 2: 
                iret = 3
            if istatus == 0: 
                iret = 0
        if CMD.RMBPressed():
            if bFirst:
                xStart = float(CMD.GetMouseX()) 
                yStart = float(CMD.GetMouseY())
                bObj = CMD.ScreenRayPicksObject(xStart,yStart)
                bFirst = False
        while CMD.RMBPressed(): 
            CMD.Step(1)
            if bObj:
                x=float(CMD.GetMouseX()) 
                y=float(CMD.GetMouseY())
                if abs(y-yStart) > 40:
                    statusOK = 1
                    noExit = False
                    break
            if CMD.IsPressKeyID(0x1B):
               noExit = False
        bFirst = True
        if CMD.IsPressKeyID(0x1B): 
            noExit = False
    if (statusOK & 0x01) == 0x01:
        CMD.SetScriptMessage("reset","")
        CMD.SetFloatingMessage(XX,YY,"Very_Good",orange_Color)
        codeDone = codeDone + 2
        CMD.Wait( 2000 )
    CMD.SetScriptMessage("reset","")
    return iret

#3 method
def CheckBrushSmoothing():
    global codeDone
    bFirst = True
    noExit = True
    explain = "Change_Brush_Smooth" 
      
    iret = 4 # next 4 method
      
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
      
    statusOK = 0
      
    coat.ui.cmd("$[Page4]Draw")
    CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color,4)
    while noExit:
        CMD.Step(1)
        shiftKey = bool(CMD.IsPressKeyID(0x10))
        istatus = GetPressButton()
        bObj = True
        if istatus!=-1:
            noExit = False
            if istatus == 1: 
               iret = 2
            if istatus == 2: 
               iret = 4
            if istatus == 0: 
               iret = 0
        if CMD.RMBPressed():
            if bFirst:
                xStart = float(CMD.GetMouseX()) 
                yStart = float(CMD.GetMouseY())
                bObj = CMD.ScreenRayPicksObject(xStart,yStart)
                bFirst = False
        
        while CMD.RMBPressed() and shiftKey:
            CMD.Step(1)
            if bObj:
                x = float(CMD.GetMouseX()) 
                y = float(CMD.GetMouseY())
                if abs(y-yStart) > 40:
                    statusOK = 1
                    noExit = False
                    break
            if CMD.IsPressKeyID(0x1B):
               noExit = False
        bFirst = True
        if CMD.IsPressKeyID(0x1B): 
            noExit = False
    if (statusOK & 0x01) == 0x01:
        CMD.SetScriptMessage("reset","")
        CMD.SetFloatingMessage(XX,YY,"Kudos",orange_Color)
        codeDone = codeDone + 4
        CMD.Wait( 2000 )
    CMD.SetScriptMessage("reset","")
    return iret

#4 method
def CheckBrushRotation():
    global codeDone
    bFirst = True
    noExit = True
    explain = "Change_Brush_Rotation"
      
    iret = 5 #exit success
      
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
    statusOK = 0
    #Show non-modal message
    CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color,2)
    while noExit:
        CMD.Step(1)
        ZeroKey = bool(CMD.IsPressKeyID(48))
        NineKey = bool(CMD.IsPressKeyID(57))
        istatus = GetPressButton()
        if istatus!=-1:
            noExit = False
            if istatus == 1: 
                iret = 3  #pred
            if istatus == 0:
                iret = 0  #abort
        while ZeroKey or NineKey: 
            CMD.Step(1)
            x = float(CMD.GetMouseX()) 
            y = float(CMD.GetMouseY())
            bObj = bool(CMD.ScreenRayPicksObject(x,y))
            if bObj:
                if ZeroKey: 
                    statusOK |= 1
                if NineKey: 
                    statusOK |= 2
            ZeroKey = CMD.IsPressKeyID(48)
            NineKey = CMD.IsPressKeyID(57)
            if CMD.IsPressKeyID(0x1B):
                noExit = False
        
        if CMD.IsPressKeyID(0x1B): 
            noExit = False

        if (statusOK & 0x03) == 0x03:
            CMD.SetScriptMessage("reset","")
            CMD.SetFloatingMessage(XX,YY,"Excellent",orange_Color)
            CMD.Wait( 2000 )
            noExit = False
            codeDone = codeDone + 8
            
    CMD.SetScriptMessage("reset","")
    return iret
 
X0 = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
Y0 = int(8 * CMD.GetWorkAreaHeight() / 100)

FontID = CMD.GetFontFileID("Fira_Sans_Condensed_16")
CMD.ShowMessageWhilePressKey(X0, Y0, mission_Explain_ID, orange_Color, 0x0D,"")

log("Start CLEARSCENE")

coat.ui.enableWindow("STARTMENU", False)
coat.ui.cmd ("$SETPAGE_Sculpt")
coat.ui.cmd ("$StopEditCurves")

# add the sculpt volume named "Gear"
root = coat.Scene.sculptRoot().clear().addChild("Gear").Volume()
# turn into the surface mode
root.toSurface()

# first, we create the gear
mesh = Mesh.gear(center=vec3(0,0,0), topR = 200, bottomR = 200, height = 400,depth = 0.1,sharpness = 0.5,teeth=16)
root.mergeMesh(mesh)

coat.ui.cmd("$VoxTreeBtn6")
coat.ui.cmd("$PENOP0")
coat.ui.cmd("$SCULP_SCLAY")

istatus = 1
idraw = 0
Quit = False
state = 0
while not Quit:
    CMD.Step(1)
    if istatus == 1: 
       istatus = CheckBrushSize()
    if istatus == 2:
       if state!=2:
          idraw = DrawBrush(0)
          if idraw==2: 
             istatus = CheckBrushDepth()
          elif idraw==1:
             istatus = 1 
          else: istatus=0
       else:
          istatus = CheckBrushDepth()
       state = 1
    if istatus == 3: 
        if state!=3: 
            idraw = DrawBrush(1)
            if idraw==2: 
               istatus = CheckBrushSmoothing()
            elif idraw==1:
                istatus = 2
            else: 
                istatus = 0
        else:
            istatus = CheckBrushSmoothing()
        state = 2
    if istatus == 4: 
        idraw = DrawBrush(2)
        if idraw == 2: 
            istatus = CheckBrushRotation()
        elif idraw == 1: 
             istatus = 3 
        else: 
            istatus = 0
        state = 3
    if istatus == 0 or istatus == 5:
        Quit == True
        break
   
log(str(istatus))

X = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
Y = int(CMD.GetWorkAreaHeight() / 2)
if istatus > 0:
    CMD.Wait( 1000 )
    if codeDone == 15: 
        CMD.SetFloatingMessageBoxTime(X, Y, mission_Complete_ID, orange_Color,0,5000)		
    else:
        CMD.SetFloatingMessageBoxTime(X, Y, mission_No_Complete_ID, orange_Color,0,5000)
    log("End Mission")
    root.clear()
    GoToStartMission()
else: 
    CMD.SetFloatingMessage(X, Y, mission_Abort, orange_Color)
    CMD.Wait( 3000 )
    CMD.SetScriptMessage("reset","")
    log("Abort Mission")
    root.clear()
    GoToStartMission()
