import coat

# go to the uv-room to set the context
coat.ui.toRoom("UV")
n_sets = coat.uv.uvSetsCount()
print("n_sets: " + str(n_sets) + "\n")

# run through all uv-sets
for s in range(n_sets):
    n_islands = coat.uv.islandsCount(s)
    # run through all islands
    for i in range(n_islands):
        print("uv_" + str(s) + "_island_"+str(i))
        # convert the island to a mesh
        island_mesh = coat.uv.islandToMesh(s,i)
        # create a volume and add the mesh to it
        v = coat.Scene.sculptRoot().addChild("uv_" + str(s) + "_island_"+str(i)).Volume()
        # turn the volume to surface mode
        v.toSurface()
        # add some thickness to the mesh, just for pretty look
        island_mesh.shell(0.02, 0.02, 4)
        # we scale 100X to make the mesh well visible
        island_mesh.toVolume(v, coat.mat4.Scaling(100))
        
# go to the sculpt-room, see the result
coat.ui.toRoom("Sculpt")