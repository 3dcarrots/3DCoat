# This example demonstrate adding prumitives into the mesh, then we merge the mesh into the scene
import coat
from coat import vec3
from coat import Mesh

# add the new sculpt volume named "meshes"
root = coat.Scene.sculptRoot().addChild("meshes").Volume()
# turn into the surface mode
root.toSurface()

# first, we create the box
mesh = Mesh.box(size=vec3(10,20,30), yAxis=vec3(0.5,1,0), center=vec3(3,4,5),detail_size=2, fillet=2)
# subtract the cylinder from the box
mesh.booleanOp(Mesh.cylinder(radius = 5,height = 30, detail_size = 2),coat.BoolOpType.BOOL_SUBTRACT)

# this is the text near the box
mesh += Mesh.text("Rotated box, subtracted cylinder",height = 15, center = vec3(-10,0,0), align = 2)

# we add the cylinder to the mesh
mesh += Mesh.cylinder(center = vec3(0, 0, 50),radius = 10,height = 30, detail_size = 2)
mesh += Mesh.text("Cylinder",height = 15, center = vec3(-20, 0, 50), align = 2)

# the cone with the random direction
mesh += Mesh.cone(center = vec3(0, 0, 100), topAxis = vec3.RandNormal(), radius = 10, height = 50, detail_size = 2)
mesh += Mesh.text("Random cone",height = 15, center = vec3(-30, 0, 100), align = 2)

# plane
mesh += Mesh.plane(center = vec3(0, 0, 150), sizeX = 20, sizeY = 20, divisionsX = 7, divisionsY = 9, xAxis = vec3.AxisX, yAxis = vec3.AxisZ) 
mesh += Mesh.text("Plane",height = 15, center = vec3(-30, 0, 150), align = 2)

# sphere
mesh += Mesh.sphere(center = vec3(0, 0, 200), radius = 15)
mesh += Mesh.text("Sphere",height = 15, center = vec3(-30, 0, 200), align = 2)

# uncommend the line below to merge all objects into the single one
# mesh.unifyAllObjects()

# merge the summary mesh into scene
root.mergeMesh(mesh)