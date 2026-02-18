#Mission 3: Drawing modes (Select from E-panel) 
import coat
import logging
import math
from coat import Mesh
from enum import Enum

_debugmode = False

logging.basicConfig(filename='pyLogger.log', format='%(asctime)s %(message)s', filemode ='w')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def log(x):
    if _debugmode:
        logger.debug(x)

cmd_press_e_key = "Press_E_key"
cmd_press_e_next_key = "Press_E_key_next"
cmd_select_e_mode = "Select_E_mode"
mission_Explain = "Pen_Drawing"
mission_Complete = "Mission_Complete"
mission_Abort = "Mission_Abort"
orange_Color = "4292730333"
cmd_strings = "$PENOP0,$PENOP1,$PENOP2,$PENOP3,$PENOP4,$PENOP5,$PENOP6,$PENOP7,$PENOP8,$PENOP9,$PENOP10,$PENOP11,$PENOP12,$PENOP13,$PENOP14,$PENOP15,$PENOP16,$PENOP17,$PENOP18,$PENOP20"

status_OK = 0
X0 = 0
Y0 = 0
CODE_START = 5
CMD_Code = 0

class PENMODE(Enum):
    OP_None = -1
    OP_RD=0
    OP_DO=1
    OP_RDO=2
    OP_Droplet=3
    OP_Constant=4
    OP_DotStroke=5
    OP_VertexLine=6
    OP_VertexCurve=7
    OP_CurveStroke=8
    OP_StampMode=9
    OP_StampDragMode=10
    OP_SquareLasso=11
    OP_RectangleLasso=12
    OP_VertexLasso=13
    OP_StrokeLasso=14
    OP_CircleLasso=15
    OP_EllipseLasso=16
    OP_ClosedSpline=17
    OP_3DClosedSpline=18
    OP_SinglePolygon=19
    OP_ALL=20
 
 def GoToStartMission()
    coat.ui.cmd("$SETPAGE_Paint")
    coat.ui.cmd("$StopEditCurves")
    coat.ui.cmd("$CLEARSCENE")
    coat.ui.cmd("$START_MENU_smMission")
    coat.ui.cmd("$StopEditCurves")
    
 def HighlightingItem()
    CMD.Step(1)
    CMD.HighlightUIElement("$ID_PENOPS",0.1)

 def WhileLMBPressed()
    while CMD.LMBPressed(): 
        CMD.Step(10)  

 def PEN_DrawPressed(i):
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
    if i == 1:
	   CMD.SetScriptMessage("reset","")
	   CMD.SetFloatingMessage(XX,YY,"Closed_Spline",orange_Color)
	   CMD.Wait( 2000 )
    CMD.SetScriptMessage("reset","")
    CMD.SetFloatingMessage(XX,YY,"Press_Curve_Exit_Draw",orange_Color)
    return 1
 
 def PEN_DrawVertex(icode):
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
    if icode == PENMODE['OP_VertexLasso'].value or icode ==PENMODE['OP_CurveStroke'].value:
        CMD.SetScriptMessage("reset","")
        if icode == PENMODE['OP_VertexLasso'].value:
            CMD.SetFloatingMessage(XX,YY,"Press_DBL_Exit_Draw",orange_Color)
        else: 
            CMD.SetFloatingMessage(XX,YY,"Press_DBL_Enter_Exit_Draw",orange_Color)
        CMD.Wait( 2000 )
    return 1
 
def CommandIsDone(code):
    noExit = True
    bDone = False
 
    XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
    drawCount = 0
    bExitDraws = False
    wasPressed = False
    isEscape = False
 	if code == PENMODE['OP_DotStroke'].value:
	 	log(str(code))
        while not bDone:
            CMD.Step(1)
            X=float(CMD.GetMouseX()) 
            Y=float(CMD.GetMouseY()) 
            bObj = bool(CMD.ScreenRayPicksObject(X,Y))
            while CMD.LMBPressed() and bObj:
                CMD.Step(1)
                wasPressed = True
            if wasPressed:
                drawCount++ 
                wasPressed = False
            if drawCount > 3:
                bDone = True
                drawCount = 0
    elif code == PENMODE['OP_VertexLine'].value or 
	     code == PENMODE['OP_VertexCurve'].value:
        drawCount = 0
        bExitDraws = False
        bFirst = True
        isDraw = False
        while not bDone:
            CMD.Step(1)
            X=float(CMD.GetMouseX()) 
            Y=float(CMD.GetMouseY()) 
            bObj = bool(CMD.ScreenRayPicksObject(X,Y))
            if CMD.IsPressKeyID(0x1b):
                bExitDraws = True
                CMD.SetScriptMessage("reset","")
            while CMD.LMBPressed() and bObj:
                CMD.Step(1)
                wasPressed = True
                if CMD.IsPressKeyID(0x1b):
                    bExitDraws = True
                    CMD.SetScriptMessage("reset","")
                if bFirst:
                    xStart=float(CMD.GetMouseX()) 
                    yStart=float(CMD.GetMouseY())
                    bFirst=False
                x=float(CMD.GetMouseX()) 
                y=float(CMD.GetMouseY())
                r = float(math.sqrt( (x-xStart)*(x-xStart) + (y-yStart)*(y-yStart)))
                if r > 10 and (not isDraw):
                    CMD.SetScriptMessage("reset","")
                    CMD.SetFloatingMessage(XX,YY,"Press_Esc_Exit_Draw",orange_Color)
                    isDraw = True
            bFirst=True			
            if  wasPressed:
                drawCount++
                wasPressed = False
            if drawCount > 0  and bExitDraws: 
                bDone = True
    elif code == PENMODE['OP_ClosedSpline'].value:
        bExitDraws = False
        isEscape = False
        drawCount = 0
        CMD.SetScriptMessage("reset","")
        CMD.SetFloatingMessage(XX,YY,"Press_Curve_Exit_Draw",orange_Color)
        bFirst = True
        bEnter = False
        vertCount = 0
	
        while not bDone:
            CMD.Step(1)
            x = float(CMD.GetMouseX())
            y = float(CMD.GetMouseY())
            bObj = bool(CMD.ScreenRayPicksObject(x, y))
            if CMD.IsPressKeyID(0x1b):
                if drawCount > 1:
                    bDone = True
                else:
				    isEscape = True
                bFirst = True
            while CMD.LMBPressed() and bObj:
                coat.io.step(1)
                wasPressed = True
                X = float(CMD.GetMouseX())
                Y = float(CMD.GetMouseY())
                if bFirst:
                    xStart = X
                    yStart = Y
                    bFirst = False
                if CMD.IsPressKeyID(0x1b):
                    isEscape = True
                    bFirst = True
                    break
            if wasPressed:
                vertCount++
                wasPressed = False
            if vertCount > 1:
                if abs(X - xStart) < 20.0 and abs(Y - yStart) < 20.0:
				   isEscape = True
            if CMD.IsPressKeyID(0x0D) and isEscape:
                bEnter = True
                drawCount++
    elif code == PENMODE['OP_CurveStroke'].value or code == PENMODE['OP_VertexLasso'].value:
          bExitDraws = False
		  drawCount = CMD.PenDrawVertex(code,"PEN_DrawVertex")
		  if drawCount > 0:
            bDone = True
    elif code == PENMODE['OP_StampMode'].value or
         code == PENMODE['OP_StampDragMode'].value or
         code == PENMODE['OP_SquareLasso'].value or
		 code == PENMODE['OP_RectangleLasso'].value or
		 code == PENMODE['OP_CircleLasso'].value or
         code == PENMODE['OP_EllipseLasso'].value or
		 code == PENMODE['OP_StrokeLasso'].value or
		 code == PENMODE['OP_3DClosedSpline'].value or
		 code == PENMODE['OP_SinglePolygon'].value:
         xStart = 0.0
         yStart = 0.0
		 while not bDone:
            CMD.Step(1)
            bFirst = True
            bAlt = Alt()
            X=float(CMD.GetMouseX()) 
            Y=float(CMD.GetMouseY())
            bObj = bool(CMD.ScreenRayPicksObject(X,Y))
            while CMD.LMBPressed() and bObj:
                coat.io.step(1)
				wasPressed = True
				if bFirst:
					xStart=float(CMD.GetMouseX()) 
					yStart=float(CMD.GetMouseY())
					bFirst=False
				if (not bAlt) and 
					code != PENMODE['OP_StampMode'].value and 
				    code != PENMODE['OP_StampDragMode'].value and
					code != PENMODE['OP_SinglePolygon'].value: 
					x=float(CMD.GetMouseX())
					y=float(CMD.GetMouseY())
					r = float(math.sqrt( (x-xStart)*(x-xStart) + (y-yStart)*(y-yStart) ))
					if r > 10:
					   bExitDraws = True
			bFirst = True
			if  wasPressed:
				if False==bAlt: 
                   drawCount++
				wasPressed = False
			if code == OP_StampMode || code == OP_StampDragMode || code == OP_SinglePolygon:
               bExitDraws = True if drawCount > 2 else False
            else:
                if drawCount>1: bExitDraws = bExitDraws
                else: bExitDraws = False
			if bExitDraws:
				bDone = True
				drawCount = 0
	 elif  code == PENMODE['OP_RD'].value or
		   code == PENMODE['OP_DO'].value or
		   code == PENMODE['OP_RDO'].value or
		   code == PENMODE['OP_Droplet'].value or
		   code == PENMODE['OP_Constant)'].value:
		   bFirst = True
		   xStart = 0
		   yStart = 0
		   log(str(code))
                while not bDone:
					CMD.Step(10)
					bAlt = bool(CMD.Alt())
					X=float(CMD.GetMouseX()) 
					Y=float(CMD.GetMouseY()) 
					bObj = bool(CMD.ScreenRayPicksObject(X,Y))
					while CMD.LMBPressed() and bObj:
						CMD.Step(10)
						if bFirst:
							xStart=float(CMD.GetMouseX()) 
							yStart=float(CMD.GetMouseY())
							bFirst=False
						if not bAlt:
							x=float(CMD.GetMouseX()) 
							y=float(CMD.GetMouseY())
							r = float(math.sqrt( (x-xStart)*(x-xStart) + (y-yStart)*(y-yStart) ))
							if r > 20:
							    bDone = True
								bObj = False
								drawCount = 0
								log("code 0-4")
								break
    return bDone

    missionDone = 0
	inSculptRoom = False
	bAbort = False
	
	coat.ui.enableWindow("STARTMENU",False)
    coat.ui.enableWindow("Layers_SINGLE",False)
   
    coat.ui.cmd ("$SETPAGE_Paint")
	coat.ui.cmd ("$PENOP0")
	coat.ui.cmd ("$StdPen")
	
	
    FontID = int(CMD.GetFontFileID("Fira_Sans_Condensed_16"))
	 
	X0 = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
	Y0 = int(8 * CMD.GetWorkAreaHeight() / 100)
	
	CMD.SetFloatingMessageBox(X0, Y0, mission_Explain, orange_Color, 1)
	
	istatus = 1
	noExit = True
  
	while noExit:
		CMD.Step(1)
		CMD.HighlightUIElement("$ID_PENOPS",0.1)
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
	
	if  istatus == 0: 
		CMD.SetShowModalDlg(False)
		GoToStartMission()
		CMD.SetShowModalDlg(True)
		return
	
	CMD.SetShowModalDlg(False)
	
	CMD.DeletePaintLayers()
	
	coat.io.ppp("data/Samples/sphere.obj")
  
	CMD.SetShowModalDlg(True)
	
	coat.Scene.sculptRoot().clear().rename("Sphere")
	
	coat.ui.cmd ("$SETPAGE_Paint")
	
	CMD.EnablePenChannel(0,True)
	CMD.EnablePenChannel(1,True)
	CMD.EnablePenChannel(3,True)
	
	CMD.SetSliderValue("$PEN_RADIUS",20)
	
    for penmode in (PENMODE):
        if(penmode.value!=-1):
            missionDone |= (1 << penmode.value)
	
	noExit = True
	mission_codes = 0
	
	XX = int(CMD.GetWorkAreaWidth() / 2 + CMD.GetWorkAreaLeft())
    YY = int(8 * CMD.GetWorkAreaHeight() / 100)
  
    CMD.SetFloatingMessageBox(XX, YY, cmd_press_e_key, orange_Color,1)
	
	while noExit: 
		coat.io.step(1)
		if CMD.IsPressKeyID(0x45):
			CMD.SetScriptMessage("reset","")
			CMD.Wait( 1000 )
			CMD.SetFloatingMessageBox(XX, YY, cmd_select_e_mode, orange_Color,1)
		    noExit = False
		if CMD.LMBPressed():
			X = float(CMD.GetMouseX())
			Y = float(CMD.GetMouseY())
			Status = int(CMD.ScriptMessagePressButton(X,Y))
			if Status == 0: 
			   noExit = False 
			   bAbort = True
			   break
	if  bAbort:
		CMD.SetScriptMessage("reset","")
		CMD.Wait( 1000 )
		CMD.SetFloatingMessage(XX, YY, mission_Abort, orange_Color)
		log("Abort Mission")
		coat.ui.wait( 2000 )
		CMD.SetScriptMessage("reset","")
		
		CMD.DeletePaintLayers()
		
		CMD.SetShowModalDlg(False)
		GoToStartMission()
		CMD.SetShowModalDlg(True)
		return
	
	noExit = True
    while  noExit:
        cmd_Code = PENMODE['OP_None'].value
	
        CMD.Step(1)
   
        inSculptRoom = IsInRoom( "Sculpt" )
        if not inSculptRoom: 
            missionDone &= (~( 1 << PENMODE['OP_3DClosedSpline'].value))
        else:
            missionDone = missionDone | ( 1 << PENMODE['OP_3DClosedSpline'].value)
	
        X = float(CMD.GetMouseX())
        Y = float(CMD.GetMouseY())
        if CMD.LMBPressed():
            Status = int(CMD.ScriptMessagePressButton(X,Y))
            if Status == 0: 
                noExit = False 
                bAbort = True
                break
	
        if CMD.IsPressKeyID(0x45):
            CMD.SetScriptMessage("reset","")
            CMD.Wait( 500 )
        
        cmd_Code = CMD.FindRecentlyPressed(cmd_strings,3)
        
        log(str(cmd_Code))
        
        if cmd_Code == PENMODE['OP_3DClosedSpline'].value:
            if not inSculptRoom:
                cmd_Code = PENMODE['OP_None'].value
   
        if  cmd_Code >= 0:
            CMD_Code = cmd_Code 
            CMD.SetScriptMessage("reset","")
            CMD.Wait( 1000 )
            log("cmd_Code")
            if CommandIsDone(cmd_Code):
                mission_codes |= (1 << cmd_Code)
                str_msg =""
                if cmd_Code == PENMODE['OP_RD'].value:
                   str_msg = "Radius_Depth"
              	elif cmd_Code == PENMODE['OP_RDO'].value:
                    str_msg = "Radius_Depth_Opacity"
                elif cmd_Code == PENMODE['OP_DO'].value:
                    str_msg = "Depth_Opacity"
                elif cmd_Code == PENMODE['OP_Droplet'].value:
                    str_msg = "Droplet"
                elif cmd_Code == PENMODE['OP_Constant'].value:
                    str_msg = "Constant"
                elif cmd_Code == PENMODE['OP_DotStroke'].value:
                    str_msg = "Dot_Stroke"
                elif cmd_Code == PENMODE['OP_VertexLine'].value:
                    str_msg = "Vertex_Line"
                elif cmd_Code == PENMODE['OP_VertexCurve'].value:
                    str_msg = "Vertex_Curve"
                elif cmd_Code == PENMODE['OP_CurveStroke'].value:
                    str_msg = "Curve_Stroke"
                elif cmd_Code == PENMODE['OP_StampMode'].value:
                    str_msg = "Stamp_Mode"
                elif cmd_Code == PENMODE['OP_StampDragMode'].value:
                    str_msg = "Stamp_Drag_Mode"
                elif cmd_Code == PENMODE['OP_SquareLasso'].value:
                    str_msg = "Square_Lasso"
                elif cmd_Code == PENMODE['OP_RectangleLasso'].value:
                    str_msg = "Rectangle_Lasso"
                elif cmd_Code == PENMODE['OP_VertexLasso'].value:
                    str_msg = "Vertex_Lasso"
                elif cmd_Code == PENMODE['OP_StrokeLasso'].value:
                    str_msg = "Stroke_Lasso"
                elif cmd_Code == PENMODE['OP_CircleLasso'].value:
                    str_msg = "Circle_Lasso"   
                elif cmd_Code == PENMODE['OP_EllipseLasso'].value:
                    str_msg = "Ellipse_Lasso"
                elif cmd_Code == PENMODE['OP_ClosedSpline'].value:
                    str_msg = "Closed_Spline"
                elif cmd_Code == PENMODE['OP_3DClosedSpline'].value:
                    str_msg = "Closed_3D_Spline"  
                elif cmd_Code == PENMODE['OP_SinglePolygon'].value:
                    str_msg = "Single_Polygon" 
           
                CMD.SetScriptMessage("reset","")
                CMD.SetFloatingMessage(XX,YY,str_msg,orange_Color)
                CMD.Wait( 3000 )
                CMD.SetScriptMessage("reset","")
                CMD.SetFloatingMessageBox(XX, YY, cmd_press_e_next_key, orange_Color,1)
                CMD.Wait( 3000 )
		  
                cmd_Code = -1
                log("cmd_Code")
                if CMD.IsPressKeyID(0x1b):
                   noExit = False
                   CMD.SetScriptMessage("reset","")
                if mission_codes >= missionDone:
                   noExit = False
	if mission_codes >= missionDone:
		CMD.SetScriptMessage("reset","")
		CMD.SetFloatingMessageBoxTime(XX, YY, mission_Complete, orange_Color,0,3000)
		log("End Mission")
		
		CMD.DeletePaintLayers()
		
		coat.ui.enableWindow("Layers_SINGLE",False)
		CMD.SetShowModalDlg(False)
		GoToStartMission()
		CMD.SetShowModalDlg(True)
	 else:
		 nPenDraws = 0
		 CMD.SetScriptMessage("reset","")
         for penmode in (PENMODE):
            if(penmode.value!=-1):
                i = 1 << int(penmode.value)    
                if mission_codes & i == i:
                   nPenDraws++
		 rmsg = str(CMD.GetTextID("You_Done"))
		 rmsg += " "
		 rmsg += str(nPenDraws)
		 rmsg += " "
		 rmsg += str(CMD.GetTextID("Items")) 
		 if bAbort:
			CMD.SetFloatingMessage(XX, YY, mission_Abort, orange_Color)
			log("Abort Mission")
			CMD.Wait( 2000 )
			CMD.SetScriptMessage("reset","")
		 }
		 CMD.SetFloatingMessageBoxTime(XX, YY, rmsg, orange_Color,0,3000)
		 if bAbort:
	     	log("Abort Mission")
			coat.ui.wait( 2000 )
			SetScriptMessage("reset","")
		
		CMD.DeletePaintLayers()
		
		coat.ui.enableWindow("Layers_SINGLE",False)
		CMD.SetShowModalDlg(False)
		GoToStartMission()
		CMD.SetShowModalDlg(True)
