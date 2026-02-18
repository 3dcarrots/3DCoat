#Mission 1: The simple navigation.
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
    
mission_Explain_ID = "Navigation_Explain_Highlighting"
mission_Complete_ID = "Mission_Is_Complete"
mission_Not_Complete_ID = "Mission_Not_Complete"
Navigation_Explain_Highlighting_Rotate = "Navigation_Explain_Highlighting_1"
Navigation_Explain_Highlighting_Move = "Navigation_Explain_Highlighting_2"
Navigation_Explain_Highlighting_Scale = "Navigation_Explain_Highlighting_3"
mission_Abort = "Mission_Abort"
orange_Color = "4292730333"

FontID = 0

def GetCommandMessage(explainMessage):
  X0 = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
  Y0 = int(8 * CMD.GetWorkAreaHeight() / 100)
  MSG = ""
  MSG += str(X0)
  MSG += ";"
  MSG += str(Y0)
  MSG += ";"
  MSG += explainMessage
  MSG += ";1"
  MSG += ";"
  MSG += orange_Color
  MSG += ";0"
  MSG += ";0,0,0,"
  MSG += CMD.GetTextID("EXIT")
  MSG += ",1,"
  MSG += orange_Color
  MSG += ",0"
  return MSG

def GoToStartMission(): 
	CMD.SetShowModalDlg(False)
	coat.ui.cmd("$SETPAGE_Sculpt")
	coat.ui.cmd("$CLEARSCENE")
	coat.ui.cmd("$START_MENU_smMission")
	CMD.SetShowModalDlg(True)
    
def DoHighlightItems(_str, _i):
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
    iret = _i + 3 
    noExit = True
    bFirst = True
    boxType = 3
    i = _i
    if i > 0:
       boxType = 4
    CMD.SetFloatingMessageBox(XX, YY, _str, orange_Color, boxType)
    IDCmd = ""
    if i == 0 : 
       IDCmd = "$NAVY_RORATE"
    elif i == 1 :
       IDCmd = "$NAVY_MOVE"
    else:
       IDCmd = "$NAVY_SCALE"
    while noExit:
        coat.io.step(10)
        X = float(CMD.GetMouseX())
        Y = float(CMD.GetMouseY())
        CMD.HighlightUIElement(IDCmd, 0.5)
        if CMD.LMBPressed():
            Status = int(CMD.ScriptMessagePressButton(X,Y))
            #check status (<-,stop,->)
            if Status == 0: 
               noExit = False
               iret = 0
            elif Status == 1: 
                 noExit = False
                 iret=1 #pred
            elif Status == 2:
                 noExit = False 
                 iret=2 #next	
        while CMD.LMBPressed() and noExit: 
            coat.io.step( 10 ) 
            if bFirst and CMD.WasRecentlyPressed(IDCmd, 1):
               xStart=float(CMD.GetMouseX())
               yStart=float(CMD.GetMouseY())
               bFirst=False
            x=float(CMD.GetMouseX())
            y=float(CMD.GetMouseY())
            if not CMD.WasRecentlyPressed(IDCmd,2):
                if bFirst == False :
                   if abs(x-xStart) > 1 or abs(y-yStart) > 1:
                      CMD.SetScriptMessage("reset","")
                      CMD.SetFloatingMessage(XX,YY,"Well_Done",orange_Color)
                      CMD.Wait( 2000 )
                      iret = 5
                      noExit = False
                      break
        #while LMBPressed()
        bFirst = True
    #while noExit
    CMD.SetScriptMessage("reset","")
    return iret

#Left mouse
def LBMObject(inSide):
    bFirst = True
    noExit = True
    if inSide:
       explain = "Set_LBM_Inside_Move_Object"
    else:
       explain = "Set_LBM_Outside_Move_Object"
    
    iret = 5 if inSide else 2

    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
	
    boxtype = 4 if inSide else 3
    CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color, boxtype)
	
   #log("\n start while noExit")
    while noExit: 
        coat.io.step( 10 )
        X = float(CMD.GetMouseX())
        Y = float(CMD.GetMouseY())
	    #log("X Y " + str(X)+ " " + str(Y))
        bAlt = CMD.Alt() if inSide else True
        bObj = True
        #log("start while LMBPressed()")
        if CMD.LMBPressed():
           Status = int(CMD.ScriptMessagePressButton(X,Y))
            #check status (<-,stop,->)
           if Status == 0:
              noExit = False
              iret = 0 #abort
           elif Status == 1: 
                noExit = False
                iret=3   #back
           elif Status == 2: 
                noExit = False
                iret = 5 if inSide else 2 #next
           if bFirst:
              xStart=float(CMD.GetMouseX())
              yStart=float(CMD.GetMouseY())
			  #log("bFirst = true xStart yStart " + str(xStart) + " " + str(yStart))
              bFirst = False
              bObj = bool(CMD.ScreenRayPicksObject(xStart,yStart))
              if not inSide: 
                 bObj = not bObj
        while CMD.LMBPressed() and bAlt and noExit:
            coat.io.step( 10 ) 
            x=float(CMD.GetMouseX())
            y=float(CMD.GetMouseY())
            log("x y " + str(x) + " " + str(y))
            if bObj:
                if abs(x-xStart) > 50 or abs(y-yStart) > 50:
                    CMD.SetScriptMessage("reset","")
                    if inSide: 
                        CMD.SetFloatingMessage(XX,YY,"Well_Done",orange_Color)
                    else:
                        CMD.SetFloatingMessage(XX,YY,"Cool",orange_Color)
                    CMD.Wait( 2000 )
                    noExit = False
                    break
            bAlt = CMD.Alt() if inSide else True
        #while LMBPressed() 
        #log("stop while LMBPressed()")
        if CMD.IsPressKeyID(0x1B): 
            noExit = False
        bFirst = True
    #while noExit
    #log("stop while noExit\n")
    CMD.SetScriptMessage("reset","")
    return iret

#Right mouse
def RMBObject(inSide):
    bFirst = True
    noExit = True
    if inSide: 
        explain = "Set_RBM_Inside_Move_Object"
    else:
        explain = "Set_RBM_Outside_Move_Object"

    iret = 6 if inSide else 3

    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)

    CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color,4)
    while noExit:
        coat.io.step(10) 
        X = float(CMD.GetMouseX())
        Y = float(CMD.GetMouseY())
        bAlt = CMD.Alt() if inSide else True
        bObj = True
        if CMD.LMBPressed():
            Status = int(CMD.ScriptMessagePressButton(X,Y))
            #check status (<-,stop,->)
            if Status == 0: 
                noExit = False 
                iret = 0 #abort
            elif Status == 1: 
                noExit = False 
                iret= 4 if inSide else 1 #back
            elif Status == 2: 
                noExit = False
                iret = 6 if (inSide) else 3 #next	
        if CMD.RMBPressed():
            if bFirst:
                xStart = float(CMD.GetMouseX()) 
                yStart = float(CMD.GetMouseY())
                bObj = bool(CMD.ScreenRayPicksObject(xStart,yStart))
                if not inSide:
                   bObj = not bObj
                bFirst = False
        while CMD.RMBPressed() and bAlt:
            coat.io.step( 10 )
            x=float(CMD.GetMouseX()) 
            y=float(CMD.GetMouseY())
            if bObj:
                r = float(math.sqrt( (x-xStart)*(x-xStart) + (y-yStart)*(y-yStart) ))
                if  r > 50: 
                    CMD.SetScriptMessage("reset","")
                    if inSide: 
                        CMD.SetFloatingMessage(XX,YY,"Super",orange_Color)
                    else:
                        CMD.SetFloatingMessage(XX,YY,"Very_Good",orange_Color)
                    CMD.Wait( 2000 )
                    noExit = False
                    break
            bAlt = CMD.Alt() if inSide else True
        if CMD.IsPressKeyID(0x1B):
            noExit = False
        bFirst=True
    CMD.SetScriptMessage("reset","")
    return iret
    
#Medium mouse
def MMBObject(inSide):
    bFirst = True
    noExit = True
    if inSide:
        explain = "Set_WMB_Inside_Move_Object"
    else:
        explain = "Set_WMB_Outside_Move_Object"
        
    iret = 7 if inSide else 4

    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)

    CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color,4)
    while noExit:
        coat.io.step(1)
        X = float(CMD.GetMouseX())
        Y = float(CMD.GetMouseY())
        bAlt = CMD.Alt() if inSide else True
        bObj = True
        if CMD.LMBPressed():
            Status = int(CMD.ScriptMessagePressButton(X,Y))
            #check status (<-,stop,->)
            if Status == 0: 
               noExit = False
               iret = 0 #abort
            elif Status == 1: 
                noExit = False 
                iret = 5 if inSide else 2 #back
            elif Status == 2: 
                noExit = False
                iret = 7 if inSide else 4 #next	
        if CMD.MMBPressed():
            if bFirst:
                xStart = float(CMD.GetMouseX()) 
                yStart = float(CMD.GetMouseY())
                bObj = CMD.ScreenRayPicksObject(xStart,yStart)
                if not inSide:
                    bObj = not bObj
                bFirst = False
        while CMD.MMBPressed() and bAlt:
            coat.io.step( 10 )
            x=float(CMD.GetMouseX()) 
            y=float(CMD.GetMouseY())
            if bObj:
                r = float(math.sqrt( (x-xStart)*(x-xStart) + (y-yStart)*(y-yStart) ))
                if r > 50:
                    CMD.SetScriptMessage("reset","")
                    if inSide:
                       CMD.SetFloatingMessage(XX,YY,"Excellent",orange_Color)
                    else: 
                       CMD.SetFloatingMessage(XX,YY,"Kudos",orange_Color)
                    CMD.Wait( 2000 )
                    noExit = False
                    break
        if CMD.IsPressKeyID(0x1B):
            noExit = False
        bFirst=True
    CMD.SetScriptMessage("reset","")
    return iret

log("Start Mission")

#coat.ui.enableWindow("STARTMENU", False)
coat.ui.cmd ("$SETPAGE_Sculpt")
coat.ui.cmd ("$StopEditCurves")

# add the sculpt volume named "Cube"
root = coat.Scene.sculptRoot().clear().addChild("Cube").Volume()
# turn into the surface mode
root.toSurface()

# first, we create the box
mesh = Mesh.box(size=vec3(200,200,200), yAxis=vec3(0,1,0), center=vec3(0,0,0),detail_size=1, fillet=2)
root.mergeMesh(mesh)

coat.io.step( 2 )

mission_Explain = CMD.GetTextID(mission_Explain_ID)
Msg = GetCommandMessage(mission_Explain)

FontID = CMD.GetFontFileID("Fira_Sans_Condensed_16")
coat.ui.cmd ("$PENOP0")
coat.ui.cmd ("$SCULP_SCLAY")

X = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
Y = int(CMD.GetWorkAreaHeight() / 2)

istatus = 1
noExit = True

while noExit: 
    coat.io.step( 1 )
    if istatus == 0 or istatus == 6: 
        noExit = False 
        break

    #LBM processing (without ALT) ...
    if istatus == 1:
       istatus = LBMObject(False)
    
    #RBM processing (without ALT) ...
    if istatus == 2: 
       istatus = RMBObject(False)
    
    #MMB processing (without ALT) ...
    if istatus == 3: 
       istatus = MMBObject(False)

    #LBM processing (with ALT) ...
    if istatus == 4: 
       istatus = LBMObject(True)
    
    #RBM processing (with ALT) ...
    if istatus == 5: 
       istatus = RMBObject(True)

if  istatus > 0:
    iret = 1
    istatus = 0
    Quit = False
    while not Quit:
        coat.io.step(1)
        if (iret == 0 or istatus == 7 or iret == 8):
           Quit = True 
           break
        if iret == 1: 
           iret = DoHighlightItems(Navigation_Explain_Highlighting_Rotate,0)
        if iret == 5: 
           istatus |= 0x1
           iret = 2
        if iret == 2: 
           iret = DoHighlightItems(Navigation_Explain_Highlighting_Move,1)
        if iret == 2: 
            iret = 3
        if iret == 5: 
           istatus |= 0x2 
           iret = 3
        if iret == 3: 
           iret = DoHighlightItems(Navigation_Explain_Highlighting_Scale,2)
           if iret == 2: 
              iret = 8
           if iret == 1: 
              iret = 2
        if iret == 5: 
           istatus |= 0x4
           iret = 1
    if  iret == 0:
        log("Abort Mission")
        CMD.Wait( 1000 )
        CMD.SetFloatingMessageBoxTime(X, Y, mission_Abort, orange_Color,0,3000)
        CMD.SetScriptMessage("reset","")
        GoToStartMission()
    else:
        CMD.Wait( 500 )
        if (istatus & 0x07)==0x07: 
            CMD.SetFloatingMessageBoxTime(X, Y, mission_Complete_ID, orange_Color,0,5000)
        else:
            CMD.SetFloatingMessageBoxTime(X, Y, mission_Not_Complete_ID, orange_Color,0,5000)
        log("End Mission")
        GoToStartMission()
else:
    log("Abort Mission")
    CMD.Wait( 1000 )
    CMD.SetFloatingMessageBoxTime(X, Y, mission_Abort, orange_Color,0,3000)
    CMD.SetScriptMessage("reset","")
    GoToStartMission()