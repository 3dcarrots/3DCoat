import random
import coat
from coat import vec3
from coat import Mesh

# we take the current volume
v = coat.Scene.current().Volume()
m = Mesh()
# we create the mesh from the volume
m.fromVolume(v)
global_center = m.getCenterMass()
# initial mesh size
initial_mesh_scale = m.getBounds().GetDiagonal() / 2.0
# the scale of the Perlin noise
noise_scale = initial_mesh_scale / 3.0

# the class to edit and store the parameters
class Cuts:
    def __init__(self):
        self.Cuts = 16
        self.ExplodingDegree = 1.0
        self.RandomShuffle = 1.0
        self.RandomRotation = 4.0
        self.NoiseDegree = 100.0
        self.NoiseScale = 100.0
    def ui(self):
        return [
            'Cuts,[1,100]',
            'ExplodingDegree,[0,100]',
            'RandomShuffle,[0,100]',
            'RandomRotation,[0,90]',
            'NoiseDegree,[0,500]',
            'NoiseScale,[0,500]'
        ]

# if mesh is empty, we warn
if m.facesCount() == 0 :
    coat.dialog().ok().text("Please select any non-trivial surface-based volume.").show()
else:
    param = Cuts()
    # restore the parameters from the file
    coat.io.fromJsonFile(param, "data/Temp/Cuts.json")
    # the dialog to enter the parameters
    if coat.dialog().ok().cancel().params(param).text("Please enter the amount of cuts, exploding degree, noise parameters:").show() == 1 :
        # save the parameters to the file
        coat.io.toJson(param, "data/Temp/Cuts.json")
        # the scale of the Perlin noise
        noise_scale *= param.NoiseScale / 100.0
        #the meshes list, initially we put there the original mesh
        meshes = [m]
        # function to find the biggest piece approximately and randomly, we estimate by the mesh square
        def biggest_mesh() :
            num = len(meshes)
            # take the random mesh as the biggest
            mbest=index = random.randint(0, num-1)
            # calculate the square of the mesh
            biggest = meshes[mbest].getSquare()
            # sevearal times we take the random mesh and compare the square
            for i in range(3):
                index = random.randint(0, num-1)
                mesh = meshes[index]
                square = mesh.getSquare()
                if square > biggest :
                    biggest = square
                    mbest = index
            # we remove the biggest mesh from the list and return it
            return meshes.pop(mbest)
        
        # in cycle we find the approximately biggest piece and cut it in the middle by the random screwed plane
        for i in range(param.Cuts) :
            coat.io.progressBar(i, param.Cuts, "Cutting the mesh...")
            m0 = biggest_mesh()
            # we relax the mesh just a little to make booleans stable
            m0.relax(0.15,False,180)
            m1 = m0.MakeCopy()
            bestN = vec3.RandNormal()
            # we find the best direction to cut the mesh
            best_len = m0.getLengthAlongDirection(bestN)
            for j in range(20) :
                dir = vec3.RandNormal()
                axis_length = m0.getLengthAlongDirection(dir)
                # if the length is bigger than the previous one, we take it as the best
                if(axis_length > best_len) :
                    best_len = axis_length
                    bestN = coat.vec3(dir)

            # we cut the mesh by the plane at it's center mass
            center = m0.getCenterMass()
            N0 = m0.vertsCount()
            degree = noise_scale*0.1*param.NoiseDegree/100.0
            m0.cutByDistortedPlane(center, bestN, degree, noise_scale, 0)
            N1 = m0.vertsCount()
            # if vertices count changes, the mesh was cut successfully
            if N1 != N0 :
                m1.cutByDistortedPlane(center, -bestN, -degree, noise_scale, 0)
                meshes0 = m0.splitDisconnectedParts()
                meshes1 = m1.splitDisconnectedParts()
                meshes.extend(meshes0)
                meshes.extend(meshes1)
            else :
                # if the mesh was not cut, we return it back to the list
                meshes.append(m0)

        # clear the initial object
        v.clear()
        # merge meshes one-by-one  
        for ms in meshes :
            # we want to push the mesh out of the center
            mesh_center = ms.getCenterMass()
            shift = vec3(mesh_center)
            shift -= global_center
            shift *= param.ExplodingDegree / 100.0
            shift += vec3.RandNormal() * param.RandomShuffle * initial_mesh_scale / 100.0
            # transform the mesh (translate), you may add random rotation to improve the effect
            ms.transform(coat.mat4.Translation(shift))
            ms.transform(coat.mat4.RotationAt(mesh_center, vec3.RandNormal(), random.uniform(-param.RandomRotation, param.RandomRotation)))
            v.mergeMesh(ms)
