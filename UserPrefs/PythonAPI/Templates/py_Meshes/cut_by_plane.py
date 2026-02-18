import random
import coat
from coat import vec3
from coat import Mesh

# we take the current volume
v = coat.Scene.current().Volume()
m = Mesh()
# we create the mesh from the volume
m.fromVolume(v)

# the mesh bound box
bb = m.getBounds()
# the center of the bound box
center = bb.GetCenter()

# if mesh is empty, we warn
if m.facesCount() == 0 :
    coat.dialog().ok().text("Please select any non-trivial surface-based volume.").show()
else:
    #the meshes list, initially we put there the original mesh
    meshes = [m]
    # function to find the biggest piece, we estimate by the boud box diagonal
    def biggest() :
        biggest=0
        mbest=meshes[0]
        for mesh in meshes:
            b = mesh.getBounds()
            if not b.IsEmpty():
                L = b.GetDiagonal()
                if (L > biggest) :
                    biggest = L
                    mbest = mesh
        return mbest
    
    # in cycle we find the biggest piece and cut it in the middle by the random plane
    for i in range(16) :
        m0 = biggest()
        bb = m0.getBounds()
        m1 = m0.MakeCopy()
        nn = vec3.RandNormal()
        m0.cutByPlane(bb.GetCenter(), nn)
        m1.cutByPlane(bb.GetCenter(), -nn)
        meshes.append(m1)

    # clear the initial object
    v.clear()
    # merge meshes one-by-one  
    for ms in meshes :
        # we want to push the mesh out of the center
        bb_center = ms.getBounds().GetCenter()
        bb_center -= center
        bb_center *= 0.1
        # transform the mesh (translate), you may add random rotation to improve the effect
        ms.transform(coat.mat4.Translation(bb_center)) 
        v.mergeMesh(ms)
