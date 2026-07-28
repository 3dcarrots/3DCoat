# 3DCoat NodeGraph Creation Rules

## 1. Creating Color Effects or Adjustment Layers

If the user wants to create an effect for color or an Adjustment Layer, you must create and save the node schematic exactly according to the following example.

**Key concepts before you start:**
- `AddNode()`: Creates a new operational block (node).
- `LoadFromFilePath()`: Connects the node to its functional logic. Note that it reads the node logic from a `.glsl` file, and based on this file the node creates all of its input and output properties. Although the file extension is `.glsl` (used for syntax highlighting and IDE hints), the file actually contains NGL (NodeGraph Language), which has its own special syntax specifically designed for writing 3DCoat nodes.
- `Position.x` / `Position.y`: Adjusts visual placement in the Node Editor graph for readability.
- `SetInKnot("InputName", node.GetOutProperty("OutputName"))`: Connects nodes together.
- `SetInProperty("InputName", value)`: Sets a fallback hardcoded value when no knot is connected (e.g. `cVec4`, `cVec3`, `float`).
- `ShowInObjectInspector`: If True, the node's parameters can be edited directly in the 3DCoat UI immediately after creation.

```python
    # 1. Initialize a new empty NodeGraph
    nodeGraph = cPy.cNodeSystem.NodeGraph()

    # 2. Add an Input node that receives data from the layers below (Lower Layers)
    # This node provides the base color (AlbedoColor) that we will modify.
    sourceMaterial: cPy.cNodeSystem.ndNGLNode = nodeGraph.AddNode()
    sourceMaterial.LoadFromFilePath("UserPrefs/Scripts/GPUNodes/Layer/inLowerLayers.glsl")

    # 3. Add an Input node that provides the color of the current layer
    # This node gives us the color painted on the current layer (LayerColor)
    layerColorNode: cPy.cNodeSystem.ndNGLNode = nodeGraph.AddNode()
    layerColorNode.LoadFromFilePath("UserPrefs/Scripts/GPUNodes/Layer/inLayerColor.glsl")
    layerColorNode.Position.y += 250 # Move it down visually in the Node Editor so nodes don't overlap

    # 4. Add an Effect node (e.g., Multiply, Add, Overlay, etc.)
    # In this example, we use a Multiply node to combine colors.
    effectNode: cPy.cNodeSystem.ndNGLNode = nodeGraph.AddNode()
    effectNode.LoadFromFilePath("UserPrefs/Scripts/GPUNodes/Vector/Multiply.glsl")
    effectNode.Position.x += 250
    effectNode.Position.y += 175
    
    # Wire the Output of sourceMaterial ("AlbedoColor") to the Input of effectNode ("Value1")
    effectNode.SetInKnot("Value1", sourceMaterial.GetOutProperty("AlbedoColor"))
    
    # Set a default fallback value for "Value1" in case the user disconnects the knot
    effectNode.SetInProperty("Value1", cPy.cTypes.cVec4(1,1,1,1))

    # Wire the Output of layerColorNode ("LayerColor") to the Input of effectNode ("Value2")
    effectNode.SetInKnot("Value2", layerColorNode.GetOutProperty("LayerColor"))

    # Set a default fallback value for "Value2". The value can also be a float, cVec3, cVec4, etc.
    effectNode.SetInProperty("Value2", cPy.cTypes.cVec4(1,1,1,1)) 

    # Since we want the user to be able to interact with the parameters of this effect node 
    # (for example, tweak "Value2" if it was not connected via a knot, or other properties)
    # in the regular UI (Object Inspector), we set this to True.
    effectNode.ShowInObjectInspector = True 

    # 5. Add an Output Node to complete the graph
    # This node receives the final processed color and returns it to the system.
    resultNode: cPy.cNodeSystem.ndNGLNode = nodeGraph.AddNode()
    resultNode.LoadFromFilePath("UserPrefs/Scripts/GPUNodes/Out/outAlbedoColor.glsl")
    resultNode.Position.x += 500
    resultNode.Position.y += 175
    
    # Wire the Output of effectNode ("Result") to the Input of resultNode ("AlbedoColor")
    resultNode.SetInKnot("AlbedoColor", effectNode.GetOutProperty("Result"))
    
    # 6. Save the newly created diagram
    # Parameters for SaveAs(name, folder, window_type):
    #   - Name: The display name of the newly created node scheme (e.g., "Multiply")
    #   - Folder: The categorized folder in which it will be located (e.g., "ColorEffects")
    #   - Window/Type: The UI window in which this effect will show up.
    # 
    # CRITICAL: The type can ONLY be one of the following values: 
    #   "NGMasks", "NGMaterials", "NGModifiers", "NGFilters", "NGVolumes"
    # Otherwise, the saved NodeGraph will be invisible and not found in any generic window.
    nodeGraph.SaveAs("Multiply", "ColorEffects", "NGModifiers")    
```
