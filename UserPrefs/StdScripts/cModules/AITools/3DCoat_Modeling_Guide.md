# 3DCoat Modeling Scripting Guide (Python API)

This document is a comprehensive guide to modeling, generating primitives, boolean operations, and mesh manipulation using Python scripts in 3DCoat.
**YOU MUST read and use this document** whenever the user asks you to "model something", "write a generator", or "add a script that creates objects".

## 0. MANDATORY MCP WORKFLOW FOR AI AGENTS

**CRITICAL:** There are **NO dedicated MCP tools** (like `create_box` or `delete_layer`) for 3D modeling or manipulating the scene tree!
**ALL** modeling, geometry creation, and VoxTree (object tree) manipulation **MUST** be executed exclusively by writing Python scripts and passing them to the **`run_script_from_source`** MCP tool.
Do **NOT** try to search for or import external Python modeling libraries unless the `read_complex_modeling_guide` tool is explicitly available in your current toolset. If it's not, you must **ONLY** use the built-in `coat` module described below.

### How to Control the Object Tree (VoxTree)
The object tree in the Sculpt room is controlled via the `coat.Scene` module and the `VoxTreeBranch` class.
- **Get Current Layer:** `current = coat.Scene.current()`
- **Get Root Layer:** `root = coat.Scene.sculptRoot()`
- **Add New Layer:** `new_branch = root.addChild("MyNewLayer")`
- **Delete Layer:** `branch.Delete()`
- **Hide/Ghost Layer:** `branch.HideInViewport = True` or `branch.Ghost = True`
- **Change Layer Parent:** `branch.ChangeParent(new_parent_branch)`
- **Get Geometric Data (Volume):** `volume = branch.Volume()` (This is required to merge meshes or primitives into the scene).
- **Clear Volume Data (without deleting the tree layer):** `branch.Volume().clear()`
- **Transform Layer:** `branch.SetTransform(coat.mat4.Translation(coat.vec3(10, 0, 0)))`

**CRITICAL RULE:** If you are asked to model anything complex—where simple default primitives (like box, sphere, capsule, cone) are not sufficient—first check if the `read_complex_modeling_guide` tool is available to you. If it **IS AVAILABLE** (meaning the ModelingLibs module is enabled), you **MUST** call it and use external libraries (such as Trimesh, Open3D, PyOpenVDB, CadQuery, or Build123d) for the task. If the tool is **NOT AVAILABLE**, do **NOT** attempt to use external libraries, and instead rely solely on the built-in `coat.Mesh` composition and boolean operations.

---

## 1. THE GOLDEN MODELING TEMPLATE (USE THIS EXACTLY)

**NEVER** use `cPy.cScene` or `cPy.cTypes` imports. They do not exist or are deprecated.
**ALWAYS** start your modeling script with this exact boilerplate. It contains the correct imports and setup:

```python
import coat
from coat import vec3, mat4, Mesh, BoolOpType

# 1. Switch to the Sculpt room
coat.ui.toRoom("Sculpt")

# 2. Get the VoxTree Root (NEVER use cPy.cScene)
root = coat.Scene.sculptRoot()

# 3. Create a new layer
new_branch = root.addChild("MyObject_Name")
volume = new_branch.Volume()
volume.toSurface() # Surface mode for sharp primitive definition

# 4. Create the main mesh composition object
final_mesh = Mesh()

# --- ADD YOUR PRIMITIVES TO final_mesh HERE ---
# Available primitives: Mesh.box, Mesh.sphere, Mesh.cylinder, Mesh.cone, Mesh.text.
# IMPORTANT: Mesh.capsule DOES NOT EXIST! Do not use it.

# Example 1: Add a box
# box = Mesh.box(size=vec3(10, 20, 10), center=vec3(0,0,0), detail_size=2)
# final_mesh += box

# Example 2: Transform and subtract a sphere
# sphere = Mesh.sphere(center=vec3(0,0,0), radius=5, detail_size=2)
# IMPORTANT: Use mat4.Scaling(), NEVER mat4.Scale()
# sphere.transform(mat4.Translation(vec3(0,10,0)) * mat4.Scaling(vec3(1, 2, 1))) 
# final_mesh.booleanOp(sphere, BoolOpType.BOOL_SUBTRACT)

# 5. Merge the final mesh into the scene volume
volume.mergeMesh(final_mesh)

# DO NOT call coat.ui.step(). It does not exist and will crash.
```

---

## 1. Three Approaches to Geometry Generation

There are three primary ways to create geometry via Python in 3DCoat:
1. **Directly using primitives (`coat.<primitive>`)**: A quick way to create simple shapes and add them directly to a `Volume`.
2. **Using the `coat.Mesh` class**: A method for creating objects and combining them via basic boolean operations, then loading them into the scene tree.
3. **Using External Libraries (Trimesh, CadQuery, etc.)**: The **MANDATORY** method for all complex modeling tasks when basic primitives (`box`, `sphere`, `capsule`, `cone`, `text`) and simple boolean operations are not enough, **provided you have the `read_complex_modeling_guide` tool**. (If available, see the `read_complex_modeling_guide` tool for instructions).

### Method 1: Direct Primitives (coat.cone, coat.capsule, coat.box, coat.sphere)
This is the standard way to create simple shapes and add them directly to a `Volume`. All primitives inherit from a base `prim` class, meaning you can always call `.details(float)`, `.translate(vec3)`, `.scale(vec3)`, `.color(hex)`, and bake them using `.add(volume)`.

**Available Primitives and their properties:**
- **Box**: `b = coat.box(); b.size(coat.vec3(10,20,30))`
- **Sphere**: `s = coat.sphere(); s.radius(15.0)`
- **Cone**: `c = coat.cone(); c.radius(10.0); c.height(50.0)`
- **Capsule**: `cap = coat.capsule(); cap.radiusTop(10.0); cap.radiusBottom(10.0); cap.height(50.0)`

Example of creating an object and adding it to the scene:

```python
import coat

# 1. Switch to the Sculpt room
coat.ui.toRoom("Sculpt")

# 2. Create a new empty object in the VoxTree
current = coat.Scene.sculptRoot().addChild("MyCapsule")
volume = current.Volume()

# 3. It's recommended to switch to Surface mode for sharper primitives:
volume.toSurface()

# 4. Create the primitive
capsule = coat.capsule()
capsule.height(200)
capsule.radiusTop(30)
capsule.radiusBottom(30)
capsule.details(0.5)

# 5. Transform the primitive (optional)
# capsule.transform(coat.mat4.RotationZ(90))

# 6. Bake the primitive into the Volume
capsule.add(volume)
```

### Method 2: Using `coat.Mesh` (Composition and Boolean Operations)
`coat.Mesh` allows you to "assemble" the final model in memory by adding primitives and performing boolean operations, before finally adding the resulting mesh to the scene.

```python
import coat
from coat import vec3, Mesh

# 1. Create an empty Mesh
mesh = Mesh()

# 2. Add primitives using the += operator
# Note: we create primitives via `Mesh.box`, `Mesh.cylinder`, etc.
mesh += Mesh.box(size=vec3(10,20,30), yAxis=vec3(0,1,0), center=vec3(0,0,0), detail_size=2, fillet=2)

# 3. Perform boolean SUBTRACTION (BOOL_SUBTRACT) 
# Available types: coat.BoolOpType.BOOL_ADD, BOOL_SUBTRACT, BOOL_INTERSECT
cylinder = Mesh.cylinder(center=vec3(0,0,0), radius=5, height=30, detail_size=2)
mesh.booleanOp(cylinder, coat.BoolOpType.BOOL_SUBTRACT)

# 4. Add 3D text to the mesh
mesh += Mesh.text("My Box", height=15, center=vec3(20, 0, 0), align=2)

# 5. Create an object in the VoxTree and merge our mesh into it
root = coat.Scene.sculptRoot().addChild("CombinedObject").Volume()
root.toSurface()
root.mergeMesh(mesh)
```

---

## 2. Available Primitives for `coat.Mesh`

When calling mesh generation methods from `Mesh`, you pass arguments directly into the function call. Here are the most common shapes:

- **Box**: `Mesh.box(size=vec3(10,10,10), center=vec3(x,y,z), xAxis=..., yAxis=..., detail_size=2, fillet=0)`
- **Sphere**: `Mesh.sphere(center=vec3(0,0,0), radius=10)`
- **Cylinder**: `Mesh.cylinder(center=vec3(0,0,0), radius=10, height=30, detail_size=2)`
- **Cone**: `Mesh.cone(center=vec3(0,0,0), topAxis=vec3(0,1,0), radius=10, height=50, detail_size=2)`
- **Plane**: `Mesh.plane(center=vec3(0,0,0), sizeX=20, sizeY=20, divisionsX=5, divisionsY=5, xAxis=vec3.AxisX, yAxis=vec3.AxisZ)`
- **Text**: `Mesh.text("Something", height=15, center=vec3(0,0,0), align=2)`

---

## 3. Mesh Manipulation (Transformations, Cutting)

Often, you may need to slice a completed model or break it into pieces (e.g., for cracks or procedural destruction).

### Extracting a mesh from the scene and cutting it with a plane (cutByPlane)
```python
import coat
from coat import vec3, Mesh

# Get the current volume layer
volume = coat.Scene.current().Volume()

# Load data from the layer into a Mesh object
m0 = Mesh()
m0.fromVolume(volume)

if m0.facesCount() > 0:
    center = m0.getBounds().GetCenter()
    normal = vec3.RandNormal() # Or vec3(0,1,0)
    
    m1 = m0.MakeCopy()
    
    # Cut the original mesh (one half remains)
    m0.cutByPlane(center, normal)
    # Cut the copy in the opposite direction (the other half remains)
    m1.cutByPlane(center, -normal)
    
    # Clear the original layer in the VoxTree
    volume.clear()
    
    # Modify positions and return them to the scene
    m0.transform(coat.mat4.Translation(vec3(5, 0, 0)))
    m1.transform(coat.mat4.Translation(vec3(-5, 0, 0)))
    
    volume.mergeMesh(m0)
    volume.mergeMesh(m1)
```

There is also an advanced variant `cutByDistortedPlane(center, normal, degree, noise_scale, 0)`, which cuts the mesh with an uneven line (using Perlin noise).

---

## 4. The Generator Tools Paradigm (Generator Extension)

To create a fully-fledged tool that procedurally generates objects (and allows the user to tweak sliders in the UI), you need to create a class and register it via `coat.ui.addExtension`.

**REQUIRED GENERATOR CLASS METHODS:**
- `__init__(self)`: Initializes the script's parameters.
- `getDefaultObjectName(self)`: Returns the base name of the layer.
- `ui(self)`: Returns an array of strings outlining the UI elements (sliders, checkboxes).
- `GeneratePreview(self, scene)`: Quick generation for real-time feedback.
- `GenerateFinalObject(self, scene)`: Final, high-quality generation.

### Generator Tool Template:
```python
import coat
import random

class RandomSpheresGenerator:
    def __init__(self):
        super().__init__()
        self.numSpheres = 50
        self.radius = 10

    def getDefaultObjectName(self):
        return "RandomSpheres"

    def ui(self):
        # Format: "VariableName,[Minimum,Maximum]"
        return [
            "numSpheres,[1,200]",
            "radius,[1,50]"
        ]

    def _generate_mesh(self, volume):
        summ = coat.Mesh()
        base_sphere = coat.Mesh.sphere(radius=self.radius)
        
        for i in range(self.numSpheres):
            shift = coat.vec3.RandNormal() * random.uniform(20, 100)
            transform = coat.mat4.Translation(shift)
            summ.addTransformed(base_sphere, transform)
            
        # Merge into the scene
        volume.mergeMesh(summ, coat.mat4.Identity, coat.BoolOpType.BOOL_MERGE)

    def GeneratePreview(self, scene):
        scene.removeSubtree() # Clear the previous preview
        child = scene.addChild("PreviewLayer")
        child.Volume().toSurface()
        child.setTransform(coat.mat4.Identity)
        
        self._generate_mesh(child.Volume())
        
        # Apply user transformations (if they moved the gizmo)
        child.setTransform(child.getTransform() * scene.getTransform())
        scene.selectOne()

    def GenerateFinalObject(self, scene):
        # For simplicity, calling Preview is usually sufficient
        self.GeneratePreview(scene)

# Inject the tool into the "Objects" tab of the "Sculpt" room
coat.ui.addExtension("Voxels", "Objects", RandomSpheresGenerator())

# Automatically activate the tool if it's being run for the first time
if not coat.ui.checkIfExtensionPresent("RandomSpheresGenerator"):
    coat.ui.toRoom("Sculpt")
    coat.ui.cmd("$RandomSpheresGenerator")
```

---

## 5. Modeling in the Retopo Room (Polygonal)

If you need to manipulate polygons at the vertex, edge, and polygon level (Extrude, Bevel, Collapse), use the Retopo room:

```python
from coat import *
import random

ui.toRoom("Retopo")
ui.cmd("$TopToolSelectAndOperate") # Select the 'Select' tool

# Get the global mesh of the retopology room
mesh = Model.fromRetopo()
mesh.clear()

# Add a primitive
sphere = Mesh.sphere(radius=20)
mesh += sphere

# Select random faces
n = mesh.facesCount()
for i in range(int(n / 6)):
    index = int(random.random() * n)
    mesh.selectFace(index)

# Operations on selected faces
mesh.extrudeSelected()
mesh.moveSelectedFacesAlongFacesNormals(5)
mesh.scaleSelectedFacesClusters(0.7)

mesh.unselectAllFaces()
```

---

## 6. General Tips and Tricks

1.  **Always use `coat.mat4` for transformations**: 
    - `coat.mat4.Translation(vec3)`
    - `coat.mat4.RotationZ(degrees)`
    - `coat.mat4.Scaling(float_val)`
    - Matrix multiplication `transform = scaling * rotation * translation`.

2.  **Safe method for compiling a group of primitives**:
    First, add them all to a single `Mesh()` using the `+=` operator or `.addTransformed(mesh, mat)`, and then call `.mergeMesh()` only ONCE. This prevents slowdowns and unnecessary recalculation of the scene trees.

3.  **ToSurface vs ToVolume**: By default, new layers may be created as volumetric voxels (Voxels). For primitives (especially those requiring sharp edges, like boxes or cylinders), always call `volume.toSurface()` before generating. This preserves sharp corners.

4.  **UI Tool Macros**: Many operations can be executed not via direct API calls, but as macros mimicking user clicks: `coat.ui.cmd("$CommandName")`. Use this approach as a last resort if you cannot find the required method inside the `Mesh` class.

---

## 7. CRITICAL ERROR PREVENTION (COMMON MISTAKES TO AVOID)

**1. Do NOT import `vec3` or `mat4` directly from `cPy.cTypes`!**
The types `cVec3` and `cMat4` are exposed directly in the `coat` module as `coat.vec3` and `coat.mat4`. Always use them as `coat.vec3(x, y, z)` and `coat.mat4.Translation(...)`. Never try to import `vec3` or `mat4` using `from cPy.cTypes import vec3`.

**2. `coat.mat4.Identity` is a PROPERTY, not a function!**
Never write `coat.mat4.Identity()`. It is a static property representing the identity matrix. Writing it with parentheses will cause a `TypeError: __call__() incompatible function arguments`. The correct usage is without parentheses:
mesh += Mesh.text("My Box", height=15, center=vec3(20, 0, 0), align=2)

# 5. Create an object in the VoxTree and merge our mesh into it
root = coat.Scene.sculptRoot().addChild("CombinedObject").Volume()
root.toSurface()
root.mergeMesh(mesh)
```

---

## 2. Available Primitives for `coat.Mesh`

When calling mesh generation methods from `Mesh`, you pass arguments directly into the function call. Here are the most common shapes:

- **Box**: `Mesh.box(size=vec3(10,10,10), center=vec3(x,y,z), xAxis=..., yAxis=..., detail_size=2, fillet=0)`
- **Sphere**: `Mesh.sphere(center=vec3(0,0,0), radius=10)`
- **Cylinder**: `Mesh.cylinder(center=vec3(0,0,0), radius=10, height=30, detail_size=2)`
- **Cone**: `Mesh.cone(center=vec3(0,0,0), topAxis=vec3(0,1,0), radius=10, height=50, detail_size=2)`
- **Plane**: `Mesh.plane(center=vec3(0,0,0), sizeX=20, sizeY=20, divisionsX=5, divisionsY=5, xAxis=vec3.AxisX, yAxis=vec3.AxisZ)`
- **Text**: `Mesh.text("Something", height=15, center=vec3(0,0,0), align=2)`

---

## 3. Mesh Manipulation (Transformations, Cutting)

Often, you may need to slice a completed model or break it into pieces (e.g., for cracks or procedural destruction).

### Extracting a mesh from the scene and cutting it with a plane (cutByPlane)
```python
import coat
from coat import vec3, Mesh

# Get the current volume layer
volume = coat.Scene.current().Volume()

# Load data from the layer into a Mesh object
m0 = Mesh()
m0.fromVolume(volume)

if m0.facesCount() > 0:
    center = m0.getBounds().GetCenter()
    normal = vec3.RandNormal() # Or vec3(0,1,0)
    
    m1 = m0.MakeCopy()
    
    # Cut the original mesh (one half remains)
    m0.cutByPlane(center, normal)
    # Cut the copy in the opposite direction (the other half remains)
    m1.cutByPlane(center, -normal)
    
    # Clear the original layer in the VoxTree
    volume.clear()
    
    # Modify positions and return them to the scene
    m0.transform(coat.mat4.Translation(vec3(5, 0, 0)))
    m1.transform(coat.mat4.Translation(vec3(-5, 0, 0)))
    
    volume.mergeMesh(m0)
    volume.mergeMesh(m1)
```

There is also an advanced variant `cutByDistortedPlane(center, normal, degree, noise_scale, 0)`, which cuts the mesh with an uneven line (using Perlin noise).

---

## 4. The Generator Tools Paradigm (Generator Extension)

To create a fully-fledged tool that procedurally generates objects (and allows the user to tweak sliders in the UI), you need to create a class and register it via `coat.ui.addExtension`.

**REQUIRED GENERATOR CLASS METHODS:**
- `__init__(self)`: Initializes the script's parameters.
- `getDefaultObjectName(self)`: Returns the base name of the layer.
- `ui(self)`: Returns an array of strings outlining the UI elements (sliders, checkboxes).
- `GeneratePreview(self, scene)`: Quick generation for real-time feedback.
- `GenerateFinalObject(self, scene)`: Final, high-quality generation.

### Generator Tool Template:
```python
import coat
import random

class RandomSpheresGenerator:
    def __init__(self):
        super().__init__()
        self.numSpheres = 50
        self.radius = 10

    def getDefaultObjectName(self):
        return "RandomSpheres"

    def ui(self):
        # Format: "VariableName,[Minimum,Maximum]"
        return [
            "numSpheres,[1,200]",
            "radius,[1,50]"
        ]

    def _generate_mesh(self, volume):
        summ = coat.Mesh()
        base_sphere = coat.Mesh.sphere(radius=self.radius)
        
        for i in range(self.numSpheres):
            shift = coat.vec3.RandNormal() * random.uniform(20, 100)
            transform = coat.mat4.Translation(shift)
            summ.addTransformed(base_sphere, transform)
            
        # Merge into the scene
        volume.mergeMesh(summ, coat.mat4.Identity, coat.BoolOpType.BOOL_MERGE)

    def GeneratePreview(self, scene):
        scene.removeSubtree() # Clear the previous preview
        child = scene.addChild("PreviewLayer")
        child.Volume().toSurface()
        child.setTransform(coat.mat4.Identity)
        
        self._generate_mesh(child.Volume())
        
        # Apply user transformations (if they moved the gizmo)
        child.setTransform(child.getTransform() * scene.getTransform())
        scene.selectOne()

    def GenerateFinalObject(self, scene):
        # For simplicity, calling Preview is usually sufficient
        self.GeneratePreview(scene)

# Inject the tool into the "Objects" tab of the "Sculpt" room
coat.ui.addExtension("Voxels", "Objects", RandomSpheresGenerator())

# Automatically activate the tool if it's being run for the first time
if not coat.ui.checkIfExtensionPresent("RandomSpheresGenerator"):
    coat.ui.toRoom("Sculpt")
    coat.ui.cmd("$RandomSpheresGenerator")
```

---

## 5. Modeling in the Retopo Room (Polygonal)

If you need to manipulate polygons at the vertex, edge, and polygon level (Extrude, Bevel, Collapse), use the Retopo room:

```python
from coat import *
import random

ui.toRoom("Retopo")
ui.cmd("$TopToolSelectAndOperate") # Select the 'Select' tool

# Get the global mesh of the retopology room
mesh = Model.fromRetopo()
mesh.clear()

# Add a primitive
sphere = Mesh.sphere(radius=20)
mesh += sphere

# Select random faces
n = mesh.facesCount()
for i in range(int(n / 6)):
    index = int(random.random() * n)
    mesh.selectFace(index)

# Operations on selected faces
mesh.extrudeSelected()
mesh.moveSelectedFacesAlongFacesNormals(5)
mesh.scaleSelectedFacesClusters(0.7)

mesh.unselectAllFaces()
```

---

## 6. General Tips and Tricks

1.  **Always use `coat.mat4` for transformations**: 
    - `coat.mat4.Translation(vec3)`
    - `coat.mat4.RotationZ(degrees)`
    - `coat.mat4.Scaling(float_val)`
    - Matrix multiplication `transform = scaling * rotation * translation`.

2.  **Safe method for compiling a group of primitives**:
    First, add them all to a single `Mesh()` using the `+=` operator or `.addTransformed(mesh, mat)`, and then call `.mergeMesh()` only ONCE. This prevents slowdowns and unnecessary recalculation of the scene trees.

3.  **ToSurface vs ToVolume**: By default, new layers may be created as volumetric voxels (Voxels). For primitives (especially those requiring sharp edges, like boxes or cylinders), always call `volume.toSurface()` before generating. This preserves sharp corners.

4.  **UI Tool Macros**: Many operations can be executed not via direct API calls, but as macros mimicking user clicks: `coat.ui.cmd("$CommandName")`. Use this approach as a last resort if you cannot find the required method inside the `Mesh` class.

---

## 7. CRITICAL ERROR PREVENTION (COMMON MISTAKES TO AVOID)

**1. Do NOT import `vec3` or `mat4` directly from `cPy.cTypes`!**
The types `cVec3` and `cMat4` are exposed directly in the `coat` module as `coat.vec3` and `coat.mat4`. Always use them as `coat.vec3(x, y, z)` and `coat.mat4.Translation(...)`. Never try to import `vec3` or `mat4` using `from cPy.cTypes import vec3`.

**2. `coat.mat4.Identity` is a PROPERTY, not a function!**
Never write `coat.mat4.Identity()`. It is a static property representing the identity matrix. Writing it with parentheses will cause a `TypeError: __call__() incompatible function arguments`. The correct usage is without parentheses:
`volume.mergeMesh(mesh, coat.mat4.Identity, coat.BoolOpType.BOOL_MERGE)`

**3. DO NOT use `coat.ui.step()` in modeling scripts!**
The command `coat.ui.step(1)` does not exist and will crash your script. Operations like `volume.mergeMesh()` or `primitive.add(volume)` will automatically update the viewport and voxel tree. You do not need to forcefully update the UI.

**4. `cMat4` Constructor**
If you need a default identity matrix, just use `coat.mat4.Identity`. Do not try to instantiate an empty matrix via `coat.mat4()` unless you know the exact C++ signature.

**5. `Mesh.capsule` DOES NOT EXIST!**
The `coat.Mesh` class does not have a `capsule` method. If you need a capsule, use `coat.capsule()` via Method 1. If you absolutely must use Method 2 (`Mesh`), you can approximate a capsule by creating a `Mesh.cylinder` and attaching two `Mesh.sphere` primitives at its ends. Do NOT write `Mesh.capsule(...)` as it will cause an `AttributeError`.

**6. `coat.Mesh` objects do not have a `.color()` method!**
Only `prim` objects (Method 1) have the `.color()` method. Do NOT call `.color()` on `coat.Mesh` objects (Method 2) as it will raise an `AttributeError`.

**7. `prim.add(volume)` visibility issues (Use Method 2 instead)**
Using `prim.add(volume)` (Method 1) might create geometry in the VoxTree but fail to update the viewport correctly, making the object appear invisible. **Always prefer Method 2 (`coat.Mesh` and `volume.mergeMesh()`)** for any script that builds models, as `mergeMesh()` guarantees proper scene and viewport updates.

**8. `mat4.Scaling`, NOT `mat4.Scale`!**
The transformation method for scaling is `coat.mat4.Scaling(vec3)`. Do NOT use `mat4.Scale(vec3)` or `mat4.scale()`. This is a common hallucination that leads to `AttributeError: type object 'Coat_CPP.cMat4' has no attribute 'Scale'`.

**9. NEVER import `cPy.cScene`!**
Always access the scene tree via the `coat` module (e.g., `coat.Scene.sculptRoot()`). Do NOT write `import cPy.cScene` or attempt to call `cPy.cScene.sculptRoot()`, as this will cause an `AttributeError`.

_Save this guide and adhere to these structural patterns and rules when developing scripts to generate and manipulate geometry._
