from os import environ
import os.path
import coat
import cPy.cCore
import cPy.cRender

import subprocess
import os
import webbrowser

from cModules.VideoTo3D import VideoTo3D

RealityCapturePath = environ['PROGRAMFILES']+"/Capturing Reality/RealityCapture/RealityCapture.exe"

for ircv in range(0,9):
    RealityScan = environ['PROGRAMFILES']+"/Epic Games/RealityScan_2."+str(ircv)+"/RealityScan.exe"
    if os.path.exists(RealityScan):
        RealityCapturePath = RealityScan


RealityCapturePath = RealityCapturePath.replace("\\", "/")
	
class VideoTo3DDialog :
	def __init__(self) :
		self.shotCount = 300
		self.inputVideo = ''
		self.rcprojFile = ''

	def ui(self) :
		return [
			"shotCount", 
			"inputVideo,load:*.*",
			"rcprojFile,save:*.rcproj", # save file dialog
		]
	
videoTo3DDialog = VideoTo3DDialog()


class RealityCaptureEngine(cPy.cCore.ExtPhotogrammetryEngine):
    def __init__(self):
        cPy.cCore.ExtPhotogrammetryEngine.__init__(self)
        self._hasHowToInstall = True
        self._hasAutoInstall = False
        self._hasSetPathToEngine = True
        self.extSourcePath = ""

    def getProjectName(self):
        if coat.Scene.current().linkedObjectCount() > 0:
            rcprojFile = coat.Scene.current().getLinkedPath(0)
        
            return os.path.basename(rcprojFile).split(".")[0]
        else:
             return "unknown"


    def _ImportProject(self, rcprojFile):
        rcprojFolder = os.path.dirname(os.path.abspath(rcprojFile))
        self.projectName = os.path.basename(rcprojFile).split(".")[0]
        # if not os.path.exists(rcprojFolder+'/'+self.projectName+'.obj'):
        subprocess.run('"'+ RealityCapturePath +'" -load "'+ rcprojFile +'"  -selectMaximalComponent -renameSelectedModel "Export" -exportModel "Export" "'+rcprojFolder+'/'+self.projectName+'.obj" -quit')
        coat.Scene.importMesh(rcprojFolder+'/'+self.projectName+'.obj')
        # coat.Scene.sculptRoot().setLinkedFile(rcprojFile)
        # if coat.Scene.sculptRoot().childCount() > 0:
        #     coat.Scene.sculptRoot().child(0).setLinkedFile(rcprojFile)
        coat.Scene.current().addLinkedPath(rcprojFile)
        coat.Scene.current().rename(os.path.basename(rcprojFile))
        coat.Scene.current().setReferenceColor(coat.vec4(1,0,0,1))

    def _ShotsTo3D(self, imageFolder, rcprojFile):
        rcprojFolder = os.path.dirname(os.path.abspath(rcprojFile))
        self.projectName = os.path.basename(rcprojFile).split(".")[0]
        cmdLine =  '"'+ RealityCapturePath +'" -addFolder "' + imageFolder + '" -align -mergeComponents -selectMaximalComponent -setReconstructionRegionAuto -save "'+ rcprojFile
        # if self.NeedAutoReconstruction(): cmdLine = '"'+ RealityCapturePath +'" -addFolder "' + imageFolder + '" -align -mergeComponents -selectMaximalComponent -setReconstructionRegionAuto -calculateNormalModel -renameSelectedModel "Export" -calculateTexture "'+ cPy.cCore.cExtension.getCoatInstallForder() + "/" + self.extSourcePath +'/texture.xml' + '" -save "'+ rcprojFile +'" -exportModel "Export" "'+rcprojFolder+'/'+self.projectName+'.obj" -quit'
        if self.NeedAutoReconstruction(): cmdLine = '"'+ RealityCapturePath +'" -addFolder "' + imageFolder + '" -align -mergeComponents -selectMaximalComponent -setReconstructionRegionAuto -calculateNormalModel -renameSelectedModel "Export" -calculateTexture -save "'+ rcprojFile +'" -exportModel "Export" "'+rcprojFolder+'/'+self.projectName+'.obj" -quit'
        subprocess.run(cmdLine)
        self._ImportProject(rcprojFile)


    def ImportProject(self):
        rcprojFile = coat.io.openFileDialog("*.rcproj")
        self.projectName = os.path.basename(rcprojFile).split(".")[0]
        if len(rcprojFile) > 4:
            self._ImportProject(rcprojFile)

    def VideoTo3D(self):
        global videoTo3DDialog
        if(coat.dialog().ok().cancel().params(videoTo3DDialog).caption("caption").show() == 1): # the on_press will be called when used press ok(1) or cancel(2)		
            inputVideo = videoTo3DDialog.inputVideo
            rcprojFile = videoTo3DDialog.rcprojFile
            shotCount = videoTo3DDialog.shotCount
            self.projectName = os.path.basename(rcprojFile).split(".")[0]

            rcprojFolder = os.path.dirname(os.path.abspath(rcprojFile))
            imageFolder = rcprojFolder+"/"+self.projectName+"_shots/"
            VideoTo3D(inputVideo, imageFolder, shotCount)
            self._ShotsTo3D(imageFolder, rcprojFile)

    def ShotsTo3D(self):
        imagesFilename = coat.io.openFileDialog("*.*")
        if len(imagesFilename) > 1:
            rcprojFile = coat.io.saveFileDialog("*.rcproj")
            self.projectName = os.path.basename(rcprojFile).split(".")[0]

            if len(rcprojFile) > 1:
                imageFolder = os.path.dirname(os.path.abspath(imagesFilename))
                self._ShotsTo3D(imageFolder, rcprojFile)

    def BakeUVTextures(self, retopo):
        if coat.Scene.current().linkedObjectCount() > 0:
            rcprojFile = coat.Scene.current().getLinkedPath(0)
            self.projectName = os.path.basename(rcprojFile).split(".")[0]
        
            rcprojFolder = os.path.dirname(os.path.abspath(rcprojFile))
            coat.PaintRoom.ExportMesh(rcprojFolder + '/'+self.projectName+'R.obj', retopo, True)
            subprocess.run('"' + RealityCapturePath + '" -load "' + rcprojFile + '" -importModel "' + rcprojFolder+'/'+self.projectName+'R.obj" -calculateTexture -exportSelectedModel "'+rcprojFolder+'/'+self.projectName+'T.obj" -quit')
            coat.PaintRoom.LoadColorTexture(rcprojFolder+'/'+self.projectName+'T_u1_v1_diffuse_2.png')            

    def OpenExProject(self):
        if coat.Scene.current().linkedObjectCount() > 0:
            rcprojFile = coat.Scene.current().getLinkedPath(0)    
            self.projectName = os.path.basename(rcprojFile).split(".")[0]
    
            subprocess.run('"' + RealityCapturePath + '" -load "' + rcprojFile + '"')

    def ReloadModel(self):
        if coat.Scene.current().linkedObjectCount() > 0:
            rcprojFile = coat.Scene.current().getLinkedPath(0)     
            self.projectName = os.path.basename(rcprojFile).split(".")[0]
   
            coat.Scene.current().remove()
            self._ImportProject(rcprojFile)



    def CheckIfInstalled(self):
        return os.path.isfile(RealityCapturePath)


    def HowToInstall(self):
        path = os.path.dirname(os.path.abspath(__file__))+'/index.html'
        url = 'file://' + path
        webbrowser.open(url)

    def SetPathToEngine(self):
        newPath = coat.io.openFileDialog("*.exe")
        if len(newPath) > 4:
            RealityCapturePath = newPath
            RealityCapturePath = RealityCapturePath.replace("\\", "/")

    def engineName(self):
        return "RealityScan"

     

class PhotosTo3DExt(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)
        if not coat.ui.checkIfMenuItemInserted("MyPhotogrammetryTool"):
            coat.ui.insertInToolset("Photogrammetry","","test_tool")
        self.realityCaptureEngine = RealityCaptureEngine()
        self.realityCaptureEngine.Register(True)

    def afterInit(self):
        self.linkedType = cPy.cCore.LinkedObjectBaseType()
        iconPath = os.path.dirname(os.path.abspath(__file__))+'/logo.png'
        self.linkedType.setIconTexture(cPy.cRender.RenderUtils.GPUTextureFromFile(iconPath, True, False))

        self.linkedType.setObjectType("rcproj")
        self.linkedType.addAction("RealityCapture", "BakeUVTextures")
        self.linkedType.addAction("RealityCapture", "BakeUVUsingRetopoMesh")
        self.linkedType.addAction("RealityCapture", "OpenExProject")
        self.linkedType.addAction("RealityCapture", "ReloadModel")
        cPy.cCore.LinkedObjectBaseType.registerObjectType(self.linkedType)
        self.realityCaptureEngine.extSourcePath = self.getSourcePath()
        

    def onMessage(self, message):
         if message == "PicTo3D": 
              self.realityCaptureEngine.ShotsTo3D()

         if message == "BakeUVTextures": 
              self.realityCaptureEngine.BakeUVTextures(False)
         if message == "BakeUVUsingRetopoMesh": 
              self.realityCaptureEngine.BakeUVTextures(True)

         if message == "ReloadModel": 
              self.realityCaptureEngine.ReloadModel()

         if message == "VedeoTo3D": 
              self.realityCaptureEngine.VideoTo3D()

         if message == "ImportProject": 
              self.realityCaptureEngine.ImportProject()

         if message == "OpenExProject": 
              self.realityCaptureEngine.OpenExProject()

    # def onBuildMainMenu(self):
    #     # Picture to 3D
    #     # a photogrammetry extension that allows you to convert photos or videos into a 3D model
    #     coat.start_main_menu("PicTo3D")

    #     # coat.menu_insert_extensions("PicTo3D")
    #     self.menu_item("PhotosTo3D", self.PhotosTo3D)
    #     self.menu_item("PhotosToTexture", self.PhotosToTexture)
    #     self.menu_item("VedeoTo3D", self.VideoTo3D)
    #     self.menu_item("ImportProject", self.ImportProject)
    #     coat.menu_exit()



photosTo3DExt = PhotosTo3DExt()

