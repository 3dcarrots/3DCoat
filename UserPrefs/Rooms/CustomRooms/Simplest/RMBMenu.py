
import coat
from cTemplates.Structs import *
from cTemplates.voxTreeRmb import *
from cTemplates.Rooms import reg_rmb

@reg_rmb
def SimplestRMB():
    if coat.voxtree_object_picked():
        global NoCache, Surface
        NoCache = not coat.menu_property("RMBObjectInCache")
        Surface = coat.menu_property("RMBObjectIsSurface")
        SetType(NoCache, Surface)
        SimplestRMBMenu()

SimplestRMBMenu = RMBMenu()

SimplestRMBMenu.Content.append(S_Show)
SimplestRMBMenu.Content.append(S_Voxtree)

@d_menu_section(SimplestRMBMenu)
def S_Vox_Simple_Tools():
        if NoCache:
            coat.menu_item("ToGlobalSpace")
            coat.menu_item("ToUniformSpace")
            coat.menu_separator()
            coat.menu_item("ExtrudeVO")
        elif Surface:
            coat.menu_item("CreateSurfaceShell")
            coat.menu_item("CloseSurfaceHoles")
            coat.menu_item("Decompose")
            coat.menu_item("DecomposeFrozen")
    
        else:
            MakeHull()
            coat.menu_item("CloseHoles")
        
@d_menu_section(SimplestRMBMenu)
def S_Vox_Simple_File():
        coat.menu_item("SaveVox3B")
        coat.menu_item("SaveVoxSubtree3B")
        coat.menu_item("MergeVox3B")
        coat.menu_item("ExportScene")

@d_menu_section(SimplestRMBMenu)
def S_EditShaderSettings():
        coat.menu_item("EditShaderSettings")

SimplestRMBMenu.Content.append(S_transform)

@d_submenu("Clone", SimplestRMBMenu)
def Simple_Clone():
            coat.menu_item("CloneVoxTree")
            coat.menu_item("CloneSymm")
            coat.menu_item("CloneSpace")
    
SimplestRMBMenu.Content.append(Flip)
SimplestRMBMenu.Content.append(MergeMove)
SimplestRMBMenu.Content.append(S_ops)
            
