#Mission 5 : Painting Depth Color Gloss
import coat
import CMD
import logging
import math
from coat import Mesh

_debugmode = False

logging.basicConfig(filename='pyLogger.log', format='%(asctime)s %(message)s', filemode ='w')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def log(x):
    if _debugmode:
        logger.debug(x)

orange_Color = "4292730333"
mission_Abort = "Mission_Abort"
mission_Complete = "Mission_Complete"

codeDone  = 0
N0 = 0
NMAX = 1
NI = 0
NCount = 0

def GoToStartMission():
    coat.ui.cmd("$CLEARSCENE")
    coat.ui.cmd("$START_MENU_smMission")
    
def GetCommandMessage(explainMessage, idx):
  X0 = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
  Y0 = int(8 * CMD.GetWorkAreaHeight() / 100)
  abort = str(CMD.GetTextID("ABORT"))
  cmd_MSG = ""
  cmd_MSG += str(X0)
  cmd_MSG += ";"
  cmd_MSG += str(Y0)
  cmd_MSG += ";"
  cmd_MSG += str(CMD.GetTextID(explainMessage))
  cmd_MSG += ";1"
  cmd_MSG += ";"
  cmd_MSG += orange_Color
  cmd_MSG += ";0"
  if idx & 1 == 1:
    cmd_MSG += ";1,0,0,data//Textures//arrowback.png,0,"
    cmd_MSG += orange_Color
    cmd_MSG += ",0"
  cmd_MSG += ";0,0,0,"
  cmd_MSG += abort
  cmd_MSG += ",1,"
  cmd_MSG += orange_Color
  cmd_MSG += ",0"
  if idx & 2 == 2:
    cmd_MSG += ";2,0,0,data//Textures//arrowforward.png,2,"
    cmd_MSG += orange_Color
    cmd_MSG += ",0"
  return cmd_MSG
  
 
#Is drawing pen in object
def IsDrawPen():
  isDraw = False
  bFirst = True

  X = float(CMD.GetMouseX())
  Y = float(CMD.GetMouseY())
  
  bObj = bool(CMD.ScreenRayPicksObject(X,Y))
  bAlt = bool(CMD.Alt())
  
  while CMD.LMBPressed() and bObj and (not bAlt):
    CMD.Step(1)
    if bFirst :
        xStart=float(CMD.GetMouseX()) 
        yStart=float(CMD.GetMouseY())
        bFirst=False
    x=float(CMD.GetMouseX()) 
    y=float(CMD.GetMouseY())
    r = float(math.sqrt( (x-xStart)*(x-xStart) + (y-yStart)*(y-yStart) ))
    if r > 50:
       isDraw = True
       break
  return isDraw

def PEN_ChannelPressed(i):
    global NCount
    global NI
    if not CMD.IsEnabledPenChannel(NI): 
       return 0
    if IsDrawPen():
       NCount = NCount + 1
       log("PEN_DRAW")
    if NCount > NMAX:
       NCount = 0
       return 2
    else:
       return 1
    return 0
 
log("Start CLEARSCENE")
mission_Explain = "PaintModes_Explain"
explain_Depth = "PaintDraw_Depth"
explain_Color = "PaintDraw_Color"
explain_Specular = "PaintDraw_Specular"

CMD.SetShowModalDlg(False)

coat.ui.enableWindow("STARTMENU", False)
coat.ui.enableWindow("Layers_SINGLE",False)
coat.ui.cmd ("$SETPAGE_Paint")

CMD.DeletePaintLayers()
coat.io.ppp("data/Samples/sphere.obj")

CMD.SetShowModalDlg(True)

coat.ui.setSliderValue("$PEN_RADIUS",30)
coat.ui.setSliderValue("$PEN_DEPTH",50)
coat.ui.setSliderValue("$PEN_MASK",30)
coat.ui.cmd ("$PENOP0")
coat.ui.cmd ("$StdPen")
coat.ui.cmd ("$StopEditCurves")

FontID = int(CMD.GetFontFileID("Fira_Sans_Condensed_16"))

X0 = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
Y0 = int(8 * CMD.GetWorkAreaHeight() / 100)

CMD.SetFloatingMessageBox(X0, Y0, mission_Explain,orange_Color,1)

noExit = True
istatus = 3
while noExit: 
    CMD.Step(1)
    CMD.HighlightUIElement("$PEN_TOGGLE_MASK_HINT",0.1)
    CMD.HighlightUIElement("$PEN_TOGGLE_DEPTH_HINT",0.1)
    CMD.HighlightUIElement("$PEN_TOGGLE_SPEC_HINT",0.1)

    X = float(CMD.GetMouseX())
    Y = float(CMD.GetMouseY())
    
    if CMD.LMBPressed():
        istatus = CMD.ScriptMessagePressButton(X,Y)
        if istatus == 0:
           noExit = False
           break
    if CMD.IsPressKeyID(0x0D):
        noExit = False
        istatus = 1
CMD.SetScriptMessage("reset","")
if istatus > 0: 
   noExit = True
   istatus = 3
   CMD.EnablePenChannel(0,False)
   CMD.EnablePenChannel(1,False)
   CMD.EnablePenChannel(3,False)
   statusFinish = 0
while noExit and istatus > 0:
    CMD.Step( 2 )
    if istatus == 0 or istatus == 2:
       noExit = False 
       break
    if istatus == 3: 
        NI = 1
        CMD.EnablePenChannel(1,False)
        cmd_MSG = str(GetCommandMessage(explain_Color,2))
        istatus = CMD.HighlightUIElementsPY("$PEN_TOGGLE_MASK_HINT",2,cmd_MSG,1,PEN_ChannelPressed,False)
    if istatus == 4 or istatus == 2:
        NI = 0
        if istatus == 2:
           statusFinish |= 0x01
           CMD.SetFloatingMessage(X0,Y0,"Well_Done",orange_Color)
           CMD.Wait( 2000 )
           CMD.SetScriptMessage("reset","")
        else:
           CMD.Wait( 500 )
        CMD.EnablePenChannel(0,False)
        cmd_MSG = str(GetCommandMessage(explain_Depth,3))
        istatus = CMD.HighlightUIElementsPY("$PEN_TOGGLE_DEPTH_HINT",2,cmd_MSG,1,PEN_ChannelPressed,False)
    if  istatus == 4 or istatus == 2:
        NI = 3
        if istatus == 2:
           statusFinish |= 0x02
           CMD.SetFloatingMessage(X0,Y0,"Super",orange_Color)
           CMD.Wait( 2000 )
           CMD.SetScriptMessage("reset","")
        else: 
           CMD.Wait( 500 )
        CMD.EnablePenChannel(3,False)
        cmd_MSG = str(GetCommandMessage(explain_Specular,1))
        istatus = CMD.HighlightUIElementsPY("$PEN_TOGGLE_SPEC_HINT",2,cmd_MSG,1,PEN_ChannelPressed,False)
        if istatus == 3: 
            istatus = 4
        if istatus == 2:
            statusFinish |= 0x04
            CMD.SetFloatingMessage(X0,Y0,"Excellent",orange_Color)
            CMD.Wait( 2000 )
            CMD.SetScriptMessage("reset","")
            
XC = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
YC = int(CMD.GetWorkAreaHeight() / 2)

if statusFinish & 0x07 == 0x07: 
    CMD.Wait( 500 )
    CMD.SetFloatingMessageBoxTime(XC, YC, mission_Complete, orange_Color,0,3000)
    log("End Mission")
else:
    CMD.SetFloatingMessage(XC,YC,mission_Abort,orange_Color)
    
CMD.Wait( 1000 )

CMD.EnablePenChannel(0,True)
CMD.EnablePenChannel(1,True)
CMD.EnablePenChannel(3,True)

CMD.SetScriptMessage("reset","")

coat.ui.enableWindow("Layers_SINGLE",False)
CMD.SetShowModalDlg(False)
GoToStartMission()
CMD.SetShowModalDlg(True)
log("End Mission")
 