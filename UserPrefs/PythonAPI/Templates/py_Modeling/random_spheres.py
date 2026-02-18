# create random spheres in retopo room, then remove one of groups, collapse edges randomly
from coat import *
import random

# switch to retopo room
ui.toRoom("Retopo")

# refer the mesh in retopo room, we will change the mesh in retopo room
mesh = Model.fromRetopo()
# clear the mesh
mesh.clear()
# create the sphere mesh
sphere = Mesh.sphere(radius = 10)

#place 10 spheres randomply
for i in range(0, 10):
    #set name for the retopo group, if we don't set the name, all objects will be in the same group
    sphere.setObjectName(0, "sphere" + str(i))
    #insert the sphere mesh into retopo room, and randomply place it
    mesh.addTransformed(sphere, mat4.Translation(vec3.RandNormal()*150))



#remove random group, just for understanding how it works
mesh.removeObject(4)

#collapse random edges, we do this to explain the access to the mesh
n = mesh.facesCount()
for i in range(0, int(n/8)):
    f = int(random.random() * mesh.facesCount())
    verts = mesh.getFaceVerts(f)
    print("verts: " + str(verts))
    if len(verts) > 0:
        mesh.collapseEdge(verts[0], verts[2])

# create the cube to demonstrate that you may replace the mesh in one of retopo groups 
cube = Mesh.box(size = vec3(20, 20, 20),nx = 8, ny = 8, nz = 8)
# we set cube instead of one of spheres
mesh.setObjectMesh(2, cube)
mesh.setObjectName(2, "cube")