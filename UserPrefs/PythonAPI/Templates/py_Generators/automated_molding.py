# the simplest example of automatic molding
import coat

# act over the current volume
cur = coat.Scene.current().Volume()
# remove all previously generated molding shapes for this volume
cur.removeMoldingShapes()
# set the molding parameters
cur.setMoldingParams(coat.vec3.AxisY, tapering_angle = 10)
# perform the automatic molding
cur.automaticMolding()
# find the top and bottom molding shapes
top = cur.findMoldingTop()
bottom = cur.findMoldingBottom()
# hide the top
top.setVisibility(False)
# make the current object semi-transparent for better visibility
cur.inScene().setGhost(True)
# print their names
print(f"top: {top.name()}")
print(f"bottom: {bottom.name()}")
