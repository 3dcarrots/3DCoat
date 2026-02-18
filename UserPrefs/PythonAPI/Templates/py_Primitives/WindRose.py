# Generate the surface figure "windrose" that consists of cones
import coat
# get to sculpt room
coat.ui.toRoom("Sculpt");
# add new volume
current = coat.Scene.sculptRoot().addChild("Wind rose")
volume = current.Volume()
# turn to surface
volume.toSurface()
height = 100
radius = 20
cone1 = coat.cone(height,radius,0)
cone2 = coat.cone(height/2,radius/2,0)
matrix = coat.mat4.Identity
for i in range(4) :
	alpha = i*90
	#setup the transform for the cone
	matrix = coat.mat4.RotationZ(alpha)
	cone1.transform(matrix)
	# add into scene,
	cone1.add(volume)

	matrix = coat.mat4.RotationZ(alpha+45)
	cone2.transform(matrix)
	cone2.add(volume)