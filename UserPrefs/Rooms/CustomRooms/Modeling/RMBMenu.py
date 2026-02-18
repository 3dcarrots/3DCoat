
import coat
from cTemplates.Structs import *
from cTemplates.voxTreeRmb import *
from cTemplates.Rooms import reg_rmb

@reg_rmb
def RetopoRMB():
    if coat.voxtree_object_picked():
        VoxTreeRmb()
    else: 
        coat.show_space_panel("*Selected*Commands*WholeMesh*Special", 7)

