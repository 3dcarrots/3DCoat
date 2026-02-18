#Mission 2: Create the new layer and add primitive
import coat
import CMD
import math
import logging

orange_Color = "4292730333"
mission_Abort = "Mission_Abort"
mission_Done = "Well_Done"

_debugmode = False

logging.basicConfig(filename='pyLogger.log', format='%(asctime)s %(message)s', filemode ='w')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def log(x):
    if _debugmode:
        logger.debug(x)

def GoToStartMission(): 
    CMD.SetShowModalDlg(False)
    coat.ui.cmd("$SETPAGE_Sculpt")
    coat.ui.cmd("$CLEARSCENE")
    coat.ui.cmd("$START_MENU_smMission")
    CMD.SetShowModalDlg(True)

def LBMObject(): 
    bFirst = True
    noExit = True
    iret = 1
    explain = "Primitive_Show_Result"
    
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
	
    CMD.SetFloatingMessageBox(XX, YY, explain, orange_Color,3)
    log("\n start while noExit")
    while noExit: 
        coat.io.step( 10 )
        X = float(CMD.GetMouseX())
        Y = float(CMD.GetMouseY())
        logstr = "X Y " + str(X) + " " + str(Y)
        log(logstr)
        bAlt = bool(CMD.Alt())
        bObj = True
        if CMD.LMBPressed():
            Status = int(CMD.ScriptMessagePressButton(X,Y))
            #check status (<-,stop,->)
            if Status == 0:
               noExit = False
               iret = 0
            elif Status == 2:
                noExit = False
                iret = 2
                
            if bFirst:
               xStart=float(CMD.GetMouseX())
               yStart=float(CMD.GetMouseY())
               logStr = "bFirst xStart yStart " + str(xStart) + " " + str(yStart)
               log(logStr) 
               bFirst=False
               bObj = CMD.ScreenRayPicksObject(xStart,yStart)
               if bObj:
                    log("bObj true")
               else:
                    log("bObj false")

        while CMD.LMBPressed() and noExit:  
            coat.io.step( 10 ) 
            x=float(CMD.GetMouseX())
            y=float(CMD.GetMouseY())
            logStr = "x y " + str(x) + " " + str(y)
            log(logStr)
            if  (bObj and bAlt) or (not bObj): 
                if bAlt:
                    dMotion = 200
                else:
                    dMotion = 300
                    
                if abs(x-xStart) > dMotion: 
                    CMD.SetScriptMessage("reset","")
                    CMD.Wait( 2000 )
                    noExit = False
                    break
                    
            bAlt = CMD.Alt()
	    # while LMBPressed()
        
        log("stop while LMBPressed()")
        if CMD.IsPressKeyID(0x1B): 
           noExit = False
   
        bFirst = True
    #while noExit
    log("stop while noExit\n")
    CMD.SetScriptMessage("reset","")
    return iret

def CommandMessage(x, y, msg, i ):
    abort = CMD.GetTextID("ABORT")
    cmd_MSG = ""
    cmd_MSG += str(x)
    cmd_MSG += ";"
    cmd_MSG += str(y)
    cmd_MSG += ";";
    cmd_MSG += CMD.GetTextID(msg)
    cmd_MSG += ";1"
    cmd_MSG += ";"
    cmd_MSG += orange_Color
    cmd_MSG += ";0"
    if i == 1 or i == 2:
        cmd_MSG += ";1,0,0,data//Textures//arrowback.png,0,"
        cmd_MSG += orange_Color
        cmd_MSG += ",0"
 
    cmd_MSG += ";0,0,0,"
    cmd_MSG += abort
    cmd_MSG += ",1,"
    cmd_MSG += orange_Color
    cmd_MSG += ",0"
  
    if i == 0 or i == 1:
        cmd_MSG += ",0"
        cmd_MSG += ";2,0,0,data//Textures//arrowforward.png,2,"
        cmd_MSG += orange_Color
        cmd_MSG += ",0"
    return cmd_MSG 

def DoHighlightExecuteCommand(IDCmd, explain): 
    noExit = True
    retCode = -1
    CMD.SetScriptMessage("drawmessagebox", explain)
    while noExit: 
        coat.io.step(20)
        if CMD.LMBPressed():
            X = float(CMD.GetMouseX())
            Y = float(CMD.GetMouseY())
            retCode = CMD.ScriptMessagePressButton(X, Y)
            if retCode >= 0: 
               noExit = False
               
        CMD.HighlightUIElement(IDCmd, 0.5)
        if CMD.WasRecentlyPressed(IDCmd, 30):
            noExit = False
            retCode = 3

    CMD.SetScriptMessage("reset", "")
    return retCode

coat.ui.toRoom("Sculpt")

mission_Explain = "Primitive_Explain"

coat.ui.enableWindow("STARTMENU", False)

coat.ui.cmd ("$SETPAGE_Sculpt")
coat.ui.cmd ("$StopEditCurves")

coat.Scene.sculptRoot().clear()

FontID = int(CMD.GetFontFileID("Fira_Sans_Condensed_16"))

X0 = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
Y0 = int(8 * CMD.GetWorkAreaHeight() / 100)

coat.ui.cmd ("$SCULP_PRIM");

CMD.SetFloatingMessageBox(X0, Y0, mission_Explain,orange_Color,1)
istatus = 1
noExit = True

while noExit:
    coat.io.step(1)
    X = float(CMD.GetMouseX())
    Y = float(CMD.GetMouseY())
    if CMD.LMBPressed():
        istatus = CMD.ScriptMessagePressButton(X,Y)
        if istatus == 0: 
           noExit = False

    if CMD.IsPressKeyID(0x0D):
        noExit = False
        istatus = 1

CMD.SetScriptMessage("reset","")
    
if istatus==0:
    XC = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YC = int(CMD.GetWorkAreaHeight() / 2)
    CMD.SetFloatingMessage(XC, YC, mission_Abort, orange_Color)
    log("abort")
    CMD.Wait( 3000 )
    CMD.SetScriptMessage("reset","")
    GoToStartMission()
    exit()
else :
    noExit = True
coat.ui.cmd ("$SCULP_PRIM")
bret = 0
bEditBox = False
#add the sculpt volume named "Sphere"
root = coat.Scene.sculptRoot().clear().addChild("Sphere").Volume()
#turn into the surface mode
root.toSurface()
coat.ui.cmd ("$VoxelSculptTool::prm_SpherePrim")
coat.ui.cmd ("$SETPAGE_Sculpt");
coat.ui.cmd("$VoxTreeBtn6");
coat.ui.setSliderValue("$SpherePrim::DetailsLevel[233]",0.15)

while noExit: 
    coat.io.step( 2 )
    if istatus == 0 or istatus == 5: 
        noExit = False
        break
    elif istatus == 1: 
        istatus = DoHighlightExecuteCommand("$VoxelSculptTool::prm_CubPrim",CommandMessage(X0,Y0,"HL_Button_Select_Prim",0))
        if istatus == 3:  
            bret |= 0x1;
            CMD.Wait( 100 )
            coat.ui.setEditBoxValue("$CubPrim::[152]#%$sa",200.0)
            coat.ui.setEditBoxValue("$CubPrim::[152]#%$sb",200.0)
            coat.ui.setEditBoxValue("$CubPrim::[152]#%$sc",200.0)
            coat.io.step( 1 )
            CMD.Wait( 100 )
            istatus = DoHighlightExecuteCommand("$PrimitivesTool::Apply",CommandMessage(X0,Y0,"HL_Button_Apply_Prim",1))
            if istatus == 3 : 
                bret |= 0x2
                istatus = 4

    if istatus == 2 or istatus == 3: istatus = 4  

    if istatus == 4:
        istatus = DoHighlightExecuteCommand("$VoxelSculptTool::prm_EllipsePrim",CommandMessage(X0,Y0,"HL_Button_Select_Prim",1))

    if istatus == 3:
        CMD.Wait( 1000 )
        coat.ui.setEditBoxValue("$EllipsePrim::[152]#%$sa",200.0)
        coat.ui.setEditBoxValue("$EllipsePrim::[152]#%$sb",400.0)
        coat.ui.setEditBoxValue("$EllipsePrim::[152]#%$sc",200.0)
        coat.io.step( 1 )
        CMD.Wait( 100 )
        istatus = DoHighlightExecuteCommand("$PrimitivesTool::Apply",CommandMessage(X0,Y0,"HL_Button_Apply_Prim",1))
        if istatus == 3:  
            bret |= 0x4
    if istatus == 1: 
        istatus = 1
    else :
        if istatus == 2 or istatus == 3:
            istatus = DoHighlightExecuteCommand("$VoxelSculptTool::prm_WasherPrim",CommandMessage(X0,Y0,"HL_Button_Select_Prim",1));
        if istatus == 3: 
            CMD.Wait( 1000 )
            coat.ui.setSliderValue("$WasherPrim::OuterDiameter",400.0)
            coat.ui.setSliderValue("$WasherPrim::InnerDiameter",250.0)
            coat.ui.setSliderValue("$WasherPrim::Thickness",40.0)
            coat.io.step( 2 )
            CMD.Wait( 100 )
            istatus = DoHighlightExecuteCommand("$PrimitivesTool::Apply",CommandMessage(X0,Y0,"HL_Button_Apply_Prim",1));
            if istatus == 3: 
               bret |= 0x8
               istatus = 5
               
        if istatus == 2: 
            istatus = 5
    #else
#while

if istatus!=0 and (bret&0x0f)==0x0f: 
    coat.ui.cmd("$[Page4]Draw")
    coat.ui.cmd("$PENOP0")
    istatus = LBMObject()

Y = int(CMD.GetWorkAreaHeight() / 2)
X = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())

if istatus != 0:
    coat.ui.cmd("$[Page4]Grow")
    if (bret&0x0f)!=0x0f: 
        CMD.SetFloatingMessageBoxTime(X, Y,"Mission_Not_Complete",orange_Color,0,5000)
    else: 
        CMD.SetFloatingMessageBoxTime(X, Y, mission_Done, orange_Color,0,5000)
    log("End Mission")
else:
    CMD.SetFloatingMessage(X, Y, mission_Abort,orange_Color)
    CMD.Wait( 3000 )
    CMD.SetScriptMessage("reset","")
GoToStartMission()
   
