# Low-poly virus modeling
from coat import *
import random

# switch to retopo room
ui.toRoom("Retopo")
# get to the select tool
ui.cmd("$TopToolSelectAndOperate")

# refer the mesh in retopo room, we will change the mesh in retopo room
mesh = Model.fromRetopo()
# we can undo the mesh changes by this script, so we drop the state to the undo queue
mesh.dropUndo()

# clear the mesh
mesh.clear()
# create the sphere mesh
sphere = Mesh.sphere(radius = 10)
# we insert it into the scene
mesh += sphere

#now we select random vertices
n = mesh.vertsCount()
# the list of vertices to select
verts = [] 

for i in range(0, 100):
    # random vertex index
    index = random.randint(0, n)
    # check if the selected vertex is not too close to already selected vertices
    pos = mesh.getVertex(index)
    fail = False
    for j in range(0, len(verts)):
        # we check distance to already selected vertices
        if mesh.getVertex(verts[j]).distance(pos) < 5:
            fail = True
            break
    # if not too close we add the vertex to the selection
    if not fail : verts.append(index)
# selecting by list is faster than one-by-one
mesh.setSelectedVertices(verts, [])

# vertex bevelk over the selected vertices, as result we got selected faces
mesh.bevelOverSelectedVertices(0.5)

# we want to extrude the selected faces, and then scale them, below is the profile for extrusion:[..., [extrusion, scale], ...]
profile = [[4,1], [1,4], [0.5,1], [0.25, 0.5]]

for r in profile:
    # we extride selected faces without the actual movement
    mesh.extrudeSelected()
    # we move the selected faces along normals
    mesh.moveSelectedFacesAlongFacesNormals(r[0])
    # we scale the selected faces
    mesh.scaleSelectedFacesClusters(r[1])
# unselect all faces
mesh.unselectAllFaces()
#subdivide twice
mesh.subdivide(True)
mesh.subdivide(True)
# display the mesh without color and wireframe
mesh.displayOptions(showWireframe=False, showColored=False, smoothView=True)

