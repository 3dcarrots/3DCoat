import cPy.cCore
import gc
import time
import cModules.AITools.AITools
from cModules.AITools.AITools import mcp, run_in_main_thread

@mcp.tool()
@run_in_main_thread
def read_complex_modeling_guide() -> str:
    """MANDATORY READING FOR COMPLEX 3D MODELING. Returns instructions on how to use external Python libraries (Trimesh, Open3D, PyOpenVDB, CadQuery, Build123d) for complex modeling tasks and importing the results into 3DCoat."""
    
    return """# Complex Modeling Guide leveraging External Libraries

For complex 3D modeling tasks (such as advanced boolean operations, voxelization, parametric CAD, or mesh processing), you can use the external Python libraries available in this module:
- **Trimesh**
- **Open3D**
- **PyOpenVDB**
- **CadQuery**
- **Build123d**

## Workflow: From External Library to 3DCoat
Because these libraries operate independently from 3DCoat's internal structures, you must follow this workflow to integrate their results into the 3DCoat scene:

1. **Generate/Process** the 3D model using the chosen external library.
2. **Export** the resulting mesh to a standard format: `.obj`, `.fbx`, or `.ply`. You can save it to a temporary location.
3. **Import** the exported file into 3DCoat using the `coat.Scene.importMesh(path_to_file)` function.

### Example Workflow (Trimesh):
```python
import trimesh
import coat
import os
import tempfile

# 1. Create or process a mesh using Trimesh
mesh1 = trimesh.creation.box(extents=[10, 10, 10])
mesh2 = trimesh.creation.icosphere(radius=6)
mesh2.apply_translation([5, 5, 5])

# Perform a boolean operation
result_mesh = mesh1.difference(mesh2)

# 2. Export the mesh to a temporary file
temp_dir = tempfile.gettempdir()
temp_obj_path = os.path.join(temp_dir, "temp_complex_model.obj")
result_mesh.export(temp_obj_path)

# 3. Import the mesh into 3DCoat
coat.Scene.importMesh(temp_obj_path)
```"""

class ModelingLibsExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)



modelingLibsExtension = ModelingLibsExtension()

