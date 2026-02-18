# This is example just to discover operations over meshes in the retop room.
# There we create random spheres in retopo rool, delete one of groups, select random faces, extrude them and move along normals
from coat import *
import random

# switch to retopo room
ui.toRoom("Retopo")
# get to the select tool
ui.cmd("$TopToolSelectAndOperate")

# refer the mesh in retopo room, we will change the mesh in retopo room
mesh = Model.fromRetopo()
# clear the mesh
mesh.clear()
# create the sphere mesh
sphere = Mesh.sphere(radius = 20)
mesh += sphere

#now we select random faces
n = mesh.facesCount()
print("Faces count: " + str(n))
for i in range(0, int(n / 6)):
    index = int(random.random() * n)
    #select random face
    mesh.selectFace(index)

for i in range(0, 12):
    mesh.extrudeSelected()
    mesh.moveSelectedFacesAlongFacesNormals(5)
    shift = vec3.RandNormal() + vec3.AxisNegY * i/2
    mesh.transformSelected(mat4.Translation(shift), False)
    mesh.scaleSelectedFacesClusters(0.7)

mesh.unselectAllFaces()
