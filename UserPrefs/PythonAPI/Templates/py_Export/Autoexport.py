import coat
import os

# Set this to True to enable debug output
_debugmode = False

# the debug print function
def _print(*args, **kwargs):
    if _debugmode:
        print(*args, **kwargs)
        
# the autoexport class
class AutoExport:
    def __init__(self):
        # Initialize variables with default values
        # the texture resolution
        self.TexRes = 4
        # the desirable reduced polycount
        self.ReducedPolycount = 40000
        self.pReducedPolycount = self.ReducedPolycount
        
        # the default export preset
        self.expPreset = coat.utils.getEnumValue("EXPPRESETS", "PBR+EXR-displacement",)

        # the default reduction percent
        self.ReductionPercent = 80
        self.pReductionPercent = self.ReductionPercent
        # decumate from all volumes or from the current volume
        self.DecimateFromAllVolumes = False
        self.pDecimateFromAllVolumes = False
        
        vol = coat.Scene.current().Volume()
        self.CurrentPolycount = vol.getPolycount()

        # export each volume to separate asset
        self.EachVolumeToSeparateAsset = False
        # center each asset around its bound box
        self.CenterEachAssetAroundBoundBox = False
        # export each asset to its own folder
        self.EachAssetToOwnFolder = False
        # drop export result directly to blender
        self.DropToBlender = False
        # export mesh optimized for UE5
        self.UE5_optimized = False
        # the regular export
        self.RegularExport = True
        # skip the filename preffix
        self.SkipFilenamePreffix = True
        # the scan depth percent (in percents of the diagonal of the bound box)
        self.ScanDepthPercent = 2.0

        # the mesh export path
        self.exportMesh = ""  
        # the textures export path (optional)
        self.texturesExportPath = "" 

    # called each frame
    def process(self):
        if self.ReductionPercent != self.pReductionPercent:
            self.ReducedPolycount = int(self.CurrentPolycount * (100.0 - self.ReductionPercent) / 100.0)
            self.pReducedPolycount = self.ReducedPolycount

        # Update the reduction percent based on the current polycount
        if self.CurrentPolycount > 0:
            self.ReductionPercent = int(100.0 - (self.ReducedPolycount * 100.0) / self.CurrentPolycount)
            if self.ReductionPercent < 0:
                self.ReductionPercent = 0

        # Check for changes in DecimateFromAllVolumes and update accordingly
        if self.DecimateFromAllVolumes != self.pDecimateFromAllVolumes:
            self.pDecimateFromAllVolumes = self.DecimateFromAllVolumes

            # If DecimateFromAllVolumes is true, calculate the total polycount
            if self.DecimateFromAllVolumes:
                self.CurrentPolycount = 0
                root = coat.Scene.sculptRoot()
                root.iterateVisibleSubtree(lambda e: self._update_polycount(e))

            # Otherwise, use the polycount of the current volume
            else:
                vol = coat.Scene.current().Volume()
                self.CurrentPolycount = vol.getPolycount()
        self.pReductionPercent = self.ReductionPercent
        self.pReducedPolycount = self.ReducedPolycount
        return False
    def UE5_YouTube():
        coat.io.exec(coat.ui.getIdTranslation("UE5_ExportTutorial"))
    def ui(self):
        self.process()
        items = []
        items.append("RegularExport, group1")
        items.append("DropToBlender, group1")
        if self.UE5_optimized :
            items.append("[2 1]")
		
        items.append("UE5_optimized,group1")
        if self.UE5_optimized :
               items.append("UE5_YouTube")
        
        items.append("---")
        items.append("EachVolumeToSeparateAsset")
        items.append("CenterEachAssetAroundBoundBox")
        if  not self.EachVolumeToSeparateAsset :
            items.append("DecimateFromAllVolumes")
        else:
            items.append("EachAssetToOwnFolder")
            if not self.EachAssetToOwnFolder :
                items.append("SkipFilenamePreffix")
		
		# gather all supported export extensions
        if self.UE5_optimized :
            items.append("exportMesh,save:*.usdz,*.usd")
        elif self.DropToBlender :
            items.append("exportMesh,save:*.fbx")
        else:
            items.append("exportMesh,save:" + coat.io.supportedMeshesFormats())
        items.append("texturesExportPath,folder")
        items.append("TexRes,[#256x256|#512x512|#1024x1024|#2048x2048|#4096x4096|#8192x8192]")

        if self.RegularExport :
            items.append("expPreset,[EXPPRESETS|]")
        items.append("---")
        items.append("#" + str(self.CurrentPolycount))
        items.append("ReductionPercent,[0,99]")
        items.append("[[] 6]")
        items.append("#{maticon arrow_forward}")
        items.append("ReducedPolycount")
        items.append("ScanDepthPercent,[0.01,100]")
        return items

def RemovePaintObjects():
    # Get the count of paint objects in the scene
    n = coat.Scene.PaintObjectsCount()

    # Loop through the paint objects and remove them
    for k in range(n):
        coat.Scene.RemovePaintObject(0)

def DecimateAutoMapExport():
    se = AutoExport()
    if coat.io.fileExists("UserPrefs/CoreAPI/auto_export_py.json"):
        coat.io.fromJsonFile(se, "UserPrefs/CoreAPI/auto_export_py.json")
    # show the parameters dialog
    if coat.dialog().ok().cancel().text("SimpSculptExportHint").caption("SimpSculptExportHintCap").params(se).show() == 1 :
        if coat.dialog().ok().cancel().text("RunBakeScriptInfo").caption("SimpSculptExportHintCap").dontShowAgainCheckbox().show() <= 1:
            # save settings
            coat.io.toJson(se, "UserPrefs/CoreAPI/auto_export_py.json")
            # hide annoying message about textures locking
            coat.ui.hideDontShowAgainMessage("AttachTextureHint")
            # don't fade background, but keep it' state, auto_keep allows to save that value in the current scope,
            fade = coat.settings.getBool("GreyOutBgInModalDialogs")
            coat.settings.setBool("GreyOutBgInModalDialogs", False)
            if se.DropToBlender :
               # the blender applink toes not support embedding
                coat.settings.setBool("EmbedTexturesToFBX", False)
                # set blender's specific normalmapping settings
                # Generally, you may use just English text itens below
                # but I decided to use the identifiers instead
                coat.settings.setString("SoftwarePreset", "Blender")
                coat.settings.setString("NormalsCalculationMethod", "nm_AngleWeighed")
                coat.settings.setString("NMAP_EXPORT_TYPE", "NM_MAYA")
                coat.settings.setString("TriangulationMethod", "DelaunayTriangulation")
                coat.settings.setString("TBNMethod", "MikkTSpace")
            if se.UE5_optimized :
                # set UE5 specific normalmapping settings
                coat.settings.setString("SoftwarePreset", "UnrealEngine")
                coat.settings.setString("NormalsCalculationMethod", "nm_AngleWeighed")
                coat.settings.setString("NMAP_EXPORT_TYPE", "NM_3DMAX")
                coat.settings.setString("TriangulationMethod", "NaiveTriangulation")
                coat.settings.setString("TBNMethod", "MikkTSpace")
                # set the export preset
                coat.settings.setString("ExportPreset", "PBR+EXR-displacement")
                se.expPreset = coat.utils.getEnumValue("EXPPRESETS", "USD (PBR Standard)")
			# create the list of volumes we want to handle
            volumes = []
            if se.EachVolumeToSeparateAsset :
                se.DecimateFromAllVolumes = False
                coat.Scene.sculptRoot().iterateVisibleSubtree(lambda e: volumes.append(e.Volume()))
            else :
                volumes.append(coat.Scene.current().Volume())
            # go through all volumes we want to operate
            for i in range (len(volumes)):
                vol = volumes[i]
                _print("Processing volume: " + vol.inScene().name())
                # select the volume
                if se.EachVolumeToSeparateAsset :
                    vol.inScene().selectOne()
                ab = coat.boundbox()
                ab.SetEmpty()
                if not se.DecimateFromAllVolumes :
                    ab = vol.calcWorldSpaceAABB()
                else :
                    coat.Scene.sculptRoot().iterateVisibleSubtree(lambda e: ab.AddBounds(e.Volume().calcWorldSpaceAABB()))
                center = ab.GetCenter()
                _print("Center: " + str(center))
                def transform(t):
                    if se.CenterEachAssetAroundBoundBox :
                        if not se.DecimateFromAllVolumes :
                            vol.inScene().transform_single(t)
                        else :
                            coat.Scene.sculptRoot().iterateVisibleSubtree(lambda e: e.transform_single(t))
                transform(coat.mat4.Translation(-center))
                d = ab.GetDiagonal() * se.ScanDepthPercent / 100.0
                cp = vol.getPolycount()
                _print("Polycount: " + str(cp))
                if se.DecimateFromAllVolumes:
                    cp = 0
                    def accum(e):
                        cp += e.Volume().getPolycount()
                        return False
                    coat.Scene.sculptRoot().iterateVisibleSubtree(accum)
                if cp > 0 :
                    # calculating the decimation percent
                    per = 100.0 - se.ReducedPolycount * 100.0 / float(cp)
                    if per > 100.0 :
                        per = 99.0
                    if per < 0.0 :
                        per = 0.0
                    # get the name of the export preset, there is index
                    # of the preset in the se.expPreset
                    preset = coat.utils.getEnumValueByIndex("EXPPRESETS",se.expPreset)
                    RemovePaintObjects()
                    coat.ui.toRoom("Retopo")
                    coat.io.step(4)
                    _print("In room: " + coat.ui.currentRoom())
                    nameCorr = coat.ui.getBoolField("$UseNamesCorrespondence")
                    coat.ui.setBoolValue("$UseNamesCorrespondence", True)
                    coat.ui.cmd("$ClearTM")
                    coat.ui.toRoom("Sculpt")
                    coat.ui.cmd("$DecimateAllToRetopo" if se.DecimateFromAllVolumes else "$DecimateToRetopo", lambda: coat.ui.cmd("$DialogButton#1"))
                    # switch to retopo room
                    coat.ui.toRoom("Retopo")
                    # refresh UI
                    coat.io.step(4)
                    # closest along normal to keep shape
                    coat.ui.cmd("$SnapToNearestAlongNormal")
                    # relax the mesh, snapping rurned ON
                    coat.ui.cmd("$ApplyTSm")
                    # refresh UI
                    coat.io.step(4)
                    # the string that contains decimation percent
                    texSize = str(256 << se.TexRes)
                    # set the baking scan depth, the depth is auto-cacculated and substituted by Coat
                    coat.ui.setOption("BakeScanDepthOut", d)
                    coat.ui.setOption("BakeScanDepthIn", d)
                    # call Bake->Bake with normal map+flat displacement
                    def inbake():
                        # set texture width when the field accessible
                        b1 = coat.ui.cmd("$COMBOBOX_TEXTURE_SIZE_X" + texSize)
                        _print("inbake1: " + str(b1))
                        # set texture height
                        b1 = coat.ui.cmd("$COMBOBOX_TEXTURE_SIZE_Y" + texSize)
                        _print("inbake2: " + str(b1))
                        # press OK at the end
                        coat.ui.cmd("$DialogButton#1")
                    _print("Baking...")
                    coat.ui.cmd("$MergeForDPNM_flatdisp", inbake)
                    coat.ui.setBoolValue("$UseNamesCorrespondence", nameCorr)
                    coat.ui.toRoom("Paint")
					# fill the mesh name
                    name = se.exportMesh
                    if se.EachVolumeToSeparateAsset :
                        name, ext = os.path.splitext(name)
                        if se.EachAssetToOwnFolder :
                            name += "/"
                            name += vol.inScene().name()
                            name += "/"
                            name += vol.inScene().name()
                            name += ext
                        else :
                            if se.SkipFilenamePreffix :
                                name = os.path.dirname(name)
                                name += "/"
                            else :
                                name += "_"
                            name += vol.inScene().name()
                            name += ext
                    if se.UE5_optimized :
                        name, ext = os.path.splitext(name)
                        if not ("usd" in ext.lower()):
                            name += ".usdz"
                    if se.DropToBlender :
                        # remove file extension
                        name = os.path.splitext(name)[0]
                        name += ".fbx"
                        # call the export dialog
                        coat.ui.setFileForFileDialog(name)
                        coat.ui.cmd("$Blender", lambda: coat.ui.cmd("$DialogButton#1"))
                    else :
                        def inexport() :
                            # set export preset
                            b1 = coat.ui.cmd("$COMBOBOX_" + preset)
                            _print("inexport: " + "$COMBOBOX_" + preset + " : " + str(b1))
                            coat.io.step(2)
                            b1 = coat.ui.setEditBoxValue("$ExportOpt::ExportMeshName", name)
                            _print("inexport: $ExportOpt::ExportMeshName " + name + " : " + str(b1))
                            # enable mesh export
                            b1 = coat.ui.setBoolValue("$ExportOpt::ExportTextures", True)
                            _print("inexport: $ExportOpt::ExportTextures : " + str(b1))
                            # enable textures export
                            b1 = coat.ui.setBoolValue("$ExportOpt::ExportGeometry", True)
                            _print("inexport: $ExportOpt::ExportGeometry : " + str(b1))
                            # set the textures folder path
                            if coat.ui.setEditBoxValue("$ExportOpt::PathForTextures", se.texturesExportPath) :
                                # press Export at the end
                                coat.ui.cmd("$DialogButton#1")
                                _print("inexport: $DialogButton#1 : " + str(b1))
                        _print("Export...")
                        coat.ui.cmd("$EXPORTOBJECT", inexport)
                    # remove all paint objects
                    RemovePaintObjects()
                    coat.ui.toRoom("Retopo")
                    coat.io.step(2)
                    # clear all retopo objects
                    coat.ui.cmd("$ClearTM")
                    coat.ui.toRoom("Sculpt")
                transform(coat.mat4.Translation(center))
            # restore the background fade state
            coat.settings.setBool("GreyOutBgInModalDialogs", fade)

if _debugmode : coat.io.showPythonConsole()

DecimateAutoMapExport()