# Generate the text primitive
import coat
name = "Hello world"
# get to sculpt room
coat.ui.toRoom("Sculpt")
# add new volume
current = coat.Scene.sculptRoot().addChild(name)
volume = current.Volume()
# turn to surface
volume.toSurface()
# draw the text name with default font name = "Times New Roman",
# width equals 200 and depth equals 10 and scale 2
txt = coat.text()
txt.font(coat.Font())
txt.string(name)
txt.width(200)
txt.depth(10)
txt.scale(2)
txt.add(volume)
