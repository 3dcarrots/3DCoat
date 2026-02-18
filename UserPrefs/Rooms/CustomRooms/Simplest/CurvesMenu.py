import coat
from cTemplates.Structs import *
from cTemplates.curves import *
from cTemplates.Rooms import reg_curves_rmb

@reg_curves_rmb
def curves_rmb(): pass

SimplestCurves = RMBMenu(curves_rmb)

SimplestCurves.Content.append(S_Edit)
SimplestCurves.Content.append(PutOnPlane)
SimplestCurves.Content.append(SM_CurvesOperations)
SimplestCurves.Content.append(S_Surface)
SimplestCurves.Content.append(S_Settings)

