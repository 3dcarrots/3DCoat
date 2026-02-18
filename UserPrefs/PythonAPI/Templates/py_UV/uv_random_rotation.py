# In this example we rotate all islands randomly and then pack them.
import coat

# go to the uv-room to set the context
coat.ui.toRoom("UV")

current_uv_set = coat.uv.currentUvSet()
n_islands = coat.uv.islandsCount(current_uv_set)
# run through all islands
for i in range(n_islands):
    island_mesh = coat.uv.islandToMesh(current_uv_set,i)
    # rotate the island randomly
    center = island_mesh.getBounds().GetCenter()
    island_mesh.transform(coat.mat4.RotationAt(center, coat.vec3.AxisZ, coat.math.Rand(0,360)))
    # update the island
    coat.uv.meshToIsland(island_mesh, current_uv_set, i)
coat.uv.pack(current_uv_set, False, True)
   