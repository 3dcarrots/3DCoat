# This example demonstrates how to click any item in UI
import coat

# In our case we triggered "New scene", then
# created parallelepiped and pressed "Smooth All" in voxels.
# It shows the modal dialog that asks for parameters. We set the smoothing count to 50 and press Ok

# Call the "New" command from the menu.  We got the $CLEARSCENE identifier from UI, pressed RMB+MMB over "File->New",
#	then pasted it there from the clipboard

print(coat.ui.getSliderValue("$PEN_RADIUS"))
print(coat.ui.getEditBoxValue("$PEN_RADIUS"))
# The lambda below just presses Don't save - second button from the left
coat.ui.cmd("$CLEARSCENE", lambda: coat.ui.cmd("$DialogButton#2"))
# get to Sculpt room
coat.ui.toRoom("Sculpt")
# Get to primitives tool. No need lambda because modal dialog never triggers in this case.
coat.ui.cmd("$SCULP_PRIM")
# switch to cube primitive
coat.ui.cmd("$VoxelSculptTool::prm_CubPrim")
# Now we substitute values into the edit box.
# SizeX = 30, the $CubPrim::%$sa is the identifier of the size X, it got from UI as before.
# If you got something like $CubPrim::%$sa[172] it is better to leave only $CubPrim::%$sa,
# but the program will work correctly in both cases, for $CubPrim::%$sa and for $CubPrim::%$sa[172],
# this recomendation is just the cosmetic stuff.
coat.ui.setEditBoxValue("$CubPrim::%$sa", 30)
# SizeY = 60
coat.ui.setEditBoxValue("$CubPrim::%$sb", 60)
# SizeZ = 40
coat.ui.setEditBoxValue("$CubPrim::%$sc", 90)
# Press Apply
coat.ui.apply()
# Now we call the Smooth All dialog. We got the $SmAll identifier from UI, pressed RMB+MMB over "Smooth All"
# in the left tools panel, then paster it there from the clipboard

# this function (smooth_close) will be called when the modal dialog will appear
# in modal dialog we set the Smoothing steps to 50
# after that, press OK using the coat::ui::cmd("$DialogButton#1")
def smooth_close():
    print("Set smooth degree to 50")
    coat.ui.setSliderValue("$SmoothParams::SmoothingDegree", 50.0)
    print("Press OK")
    coat.ui.cmd("$DialogButton#1")
coat.ui.cmd("$SmAll",smooth_close)

# The execution continues there after we pressed OK in the modal dialog.
# now we got to BaseClay just to avoid yellow cube preview in primitives
coat.ui.cmd("$BaseVoxBrush")
