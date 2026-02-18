# This example generates the surface figure that consists of capsule
import coat

class CapsulePrim:
	def __init__(self):
		self.Radius = 30
		self.Height = 200
	
	# this is class registration, look dialogs example
	def ui(self):
		return [
			"Radius,[10,100]",
			"Height,[20,200]"
		]
	def build(self) :
		voxId = coat.Scene.sculptRoot().childCount()
		current = coat.Scene.sculptRoot().addChild("Capsule" + str(voxId))
		volume = current.Volume()
		volume.toSurface()
		capsule = coat.capsule()
		capsule.height(self.Height)
		capsule.radiusTop(self.Radius)
		capsule.radiusBottom(self.Radius)
		capsule.details(0.5)
		capsule.add(volume)

# get to sculpt room
coat.ui.toRoom("Sculpt")
capsulePrim = CapsulePrim()
# show the dialog
if(coat.dialog().ok().cancel().params(capsulePrim).show() == 1) :# ok pressed, buttons start from 1
	# build the figure
	capsulePrim.build()
	