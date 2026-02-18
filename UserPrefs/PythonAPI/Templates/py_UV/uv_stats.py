# this example calculater square trash per-island
import coat

# go to the uv-room if we are not in the repopo-room
if coat.ui.currentRoom() != "Retopo":
    coat.ui.toRoom("UV")

n_sets = coat.uv.uvSetsCount()
print("UV sets count: " + str(n_sets) + "\n")
#first, re-wrap islands with bigger distance
# run through all uv-sets
for s in range(n_sets):
    # get the number of islands
    n_islands = coat.uv.islandsCount(s)
    print("Islands count: " + str(n_islands) + "\n")
    # run through all islands
    for i in range(n_islands):
        # convert the island to a mesh
        island_mesh = coat.uv.islandToMesh(s,i)
        # get the island to a mesh in 3D space
        island_3D = coat.uv.islandToMeshInSpace(s,i)
        square_2D = 0
        square_3D = 0
        min_2d_to_3D = 1000000
        max_2d_to_3D = 0
        # run through all faces of the island
        nfaces = island_mesh.facesCount()
        print ("Island #" + str(i) + ": Faces count: " + str(nfaces) + " / " + str(island_3D.facesCount()))
        for f in range(nfaces):
            # get the face area
            sq_2D = island_mesh.getFaceSquare(f)
            # get the face area in 3D space
            sq_3D = island_3D.getFaceSquare(f)
            if(sq_2D == 0 ): print ("Face #" + str(f) + ": 2D square = 0")
            if(sq_3D == 0 ): print ("Face #" + str(f) + ": 3D square = 0")
            square_2D += sq_2D
            square_3D += sq_3D
            _2d_to_3D = sq_2D / sq_3D
            if _2d_to_3D < min_2d_to_3D:
                min_2d_to_3D = _2d_to_3D
            if _2d_to_3D > max_2d_to_3D:
                max_2d_to_3D = _2d_to_3D
        print ("Square 2D: " + str(square_2D))
        print ("Square 3D: " + str(square_3D)) 
        if square_3D > 0 and square_2D > 0:
            _2D_to_3D = square_2D / square_3D
            min_2d_to_3D /= _2D_to_3D
            max_2d_to_3D /= _2D_to_3D
            print ("Square trash: " + str(min_2d_to_3D) + " - " + str(max_2d_to_3D))
        else:
            print ("The island is empty")

    print("\nBorders between islands:\n")
    # run through all pair of islands to find common edges and common chunks of edges
    for i in range(n_islands):
        for j in range(i+1,n_islands):
            # get the edges between each pair of islands
            edges = coat.uv.getBorderBetweenIslands(s,i,s,j)
            if len(edges) > 0 :
                print ("Islands #" + str(i) + " and #" + str(j) + " have " + str(int(len(edges)/2)) + " common edges")
                # we convert the list of edges to the list of couples
                chunks = [edges[i:i+2] for i in range(0, len(edges), 2)]
                #pay attention, that the list of edges is not sorted, now we combine the chunks of unsorted edges into the sequential chunks
                while True:
                    merged = False
                    for k in range(len(chunks)):
                        for p in range(len(chunks)):
                            # if the last vertex of the first chunk is equal to the first vertex of the second chunk, we combine them into the single chunk
                            if k != p and chunks[k][-1] == chunks[p][0]:
                                chunks[k].extend(chunks[p][1:])
                                del chunks[p]
                                merged = True
                                break
                        if merged:
                            break
                    if not merged:
                        break
                print("    Chunks: " + str(chunks))

