# this example converts uv islands to the cloth pieces with extra borders to be sewed together
import coat

# go to the uv-room to set the context
coat.ui.toRoom("UV")
border_percent = 0.5
n_sets = coat.uv.uvSetsCount()
#first, re-wrap islands with bigger distance
border = coat.uv.getUnwrapIslandsDistance()
coat.uv.setUnwrapIslandsDistance(border_percent + 0.2)

# run through all uv-sets
for s in range(n_sets):
    # unwrap the uv-set
    coat.uv.unwrap(s)
    # get the number of islands
    n_islands = coat.uv.islandsCount(s)
    print("n_islands: " + str(n_islands) + "\n")
    # run through all islands
    for i in range(n_islands):
        print("cloth_" + str(s) + "_"+str(i))
        # convert the island to a mesh
        island_mesh = coat.uv.islandToMesh(s,i)
        # expand the open edges to make the borders
        island_mesh.expandOpenEdges(border_percent / 100.0)        
        # create a volume and add the mesh to it
        v = coat.Scene.sculptRoot().addChild("uv_" + str(s) + "_island_"+str(i)).Volume()
        # turn the volume to surface mode
        v.toSurface()
        # add some thickness to the mesh, just for pretty look
        # we scale 100X to make the mesh well visible
        # we also rotate the mesh to make the normals look upwards
        island_mesh.toVolume(v, coat.mat4.Scaling(100) * coat.mat4.RotationX(90))
coat.uv.applyUVSet()     
coat.uv.setUnwrapIslandsDistance(border)
# go to the sculpt-room, see the result
coat.ui.toRoom("Sculpt")