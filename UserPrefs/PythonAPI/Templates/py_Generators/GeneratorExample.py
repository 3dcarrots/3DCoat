# The basic generator example, just to demonstrate the principles of generators, look the \ref TreesGenerator.cpp for the more sophisticated example. 

import coat
import random

# This is the simplest non-destructive generator example.
# It is registered as tool in the Sculpt->Objects tools section.
# The tool name is the same as the class name

class SimpleGenerator:
	# initialize the parameters
	def __init__(self):
		super().__init__()
		self.numSpheres = 200
		self.FigureRadius = 30
		self.FigureRadiusVariation = 0.1
		self.SpheresRadius = 10
		self.SpheresRadiusVariation = 0.5
		self.Seed = 0
		# load the sphere mesh
		self.m = coat.Mesh()
		self.m.Read("data/Samples/Sphere.obj")
	
	# the default names alias for the generated objects
	def getDefaultObjectName(self) :
		return "Spheres"

	# expose the generator parameters
	def ui(self) :
		return [
			"numSpheres,[1,1000]",
			"FigureRadius,[1,100]",
			"FigureRadiusVariation,[0,100]",
			"SpheresRadius,[1,100]",
			"SpheresRadiusVariation,[0,100]",
			"Seed,[0,10000]"
		]
	
	# generate random value with variation, it is just helper
	def random_var(value, variation) :
		return random.uniform(value, value * (1.0 + variation))

	# generate the example object, in this case it are the random spheres
	def generate(self, v) :
		random.seed(self.Seed)
		# Coat's random generator used in coat.vec3.RandNormal(), so need to set seed for it too 
		coat.math.Randomize(self.Seed)
		# the mesh shere we collect objects
		summ = coat.Mesh()
		for i in range(self.numSpheres) :
			# create transformation matrix.
			# scaling to the sphere radius
			transform = coat.mat4.Scaling(SimpleGenerator.random_var(self.SpheresRadius, self.SpheresRadiusVariation))
			# translate using the random vector
			dv = coat.vec3.RandNormal() * SimpleGenerator.random_var(self.FigureRadius, self.FigureRadiusVariation)
			tr=coat.mat4.Translation(dv)
			transform = transform * tr
			# add the sphere to the summary mesh
			summ.addTransformed(self.m, transform)
		# insert the collection into the scene
		v.mergeMesh(summ, coat.mat4.Identity, coat.BoolOpType.BOOL_MERGE)

	# fast and rough generating, the function is overriden from the SculptGenerator
	def GeneratePreview(self, scene) :
		# we remove previously generates object
		scene.removeSubtree()
		# we add the new object as sub-object to the current 
		t = scene.addChild("Simple")
		v = t.Volume()
		# turn the new volume to surface
		v.toSurface()
		# resore to the identoty transform
		t.setTransform(coat.mat4.Identity)
		# we generate as if there is no transform
		self.generate(t.Volume())
		# we apply the transform that user made manually 
		t.setTransform(t.getTransform() * scene.getTransform())
		# we select the generated object
		scene.selectOne()
	
	# generage the object in "final quality", the function is overriden from the SculptGenerator
	def GenerateFinalObject(self, scene) :
		# in simplest case the final quality object is same as preview
		self.GeneratePreview(scene)

# there we check if generator with same name already registered
present = coat.ui.checkIfExtensionPresent("SimpleGenerator")
# this command inserts the generatior into the toolset, Sculpt->Objects->SimpleGenerator
# if generater already registered, it is replaced with the new one
coat.ui.addExtension("Voxels","Objects",SimpleGenerator())
# we do it only first time when we register the tool:
if not present :
	coat.ui.toRoom("Sculpt")
	# activate the tool
	coat.ui.cmd("$SimpleGenerator")
