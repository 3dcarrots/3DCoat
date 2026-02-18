# this examle takes the mesh from the paint or sculpt room, renders from above (a bit random direction, random light) and saves the rendered image to the
# specified path. This example demonstrates the camera manipulation and rendering.
# The object rendered as if it drops the shadow on the invisible plane.
# The shadow represented as the alpha channel of the final image.

from coat import *
import random

# the scene scale and shift, we need to create the correct render background
ssc = Scene.GetSceneScale()
shift = Scene.getSceneShift()

# the mesh from the paint room
m = Mesh()
m.fromPaintRoom()
m.transform(mat4.Translation(vec3(0, - shift.y * ssc,0)))

bb = m.getBounds()
# we need to scale bound box to get it in scene (nt world) units because sculpt objects measured in scene units as well
# but exported mesh is in world units
bb = boundbox.Transform(bb, mat4.Scaling(ssc))

# remove any existing background, calculate boundbox of sculpt objects in scene, if any
def removebg(x):
    if x.name() == "bg_round":
        x.clear()
        x.remove()
    else:
        bb.AddBounds(x.Volume().calcWorldSpaceAABB())
    return False
def removeBgObject():
    for i in range(2) : Scene.sculptRoot().iterateVisibleSubtree(removebg)

# remove any existing background
removeBgObject()

if(bb.IsEmpty()):
    dialog.text("The scene is empty").ok().show()
    exit(1)

bottom = bb.GetMin().y
m1 = bb.GetMin()
m2 = bb.GetMax()
# we set y to zero because we need object size from the above, so we measure diagonal from the above
m1.y = m2.y = 0
radius = m1.distance(m2) * 2

cyl = Mesh.cylinder(vec3(0,bottom - radius/20,0), radius, radius/10,0,16,128,128,0)

v=Volume()
# create background object
v = Scene.sculptRoot().addChild("bg_round").Volume()
v.toSurface()
cyl.toVolume(v)
# set the simplest possible flat shader for the background object
v.setBoolShaderProperty("UseColorTexture", False)
v.setBoolShaderProperty("UseGlossTexture", False)
v.setBoolShaderProperty("UseMetalnessTexture", False)
v.setBoolShaderProperty("UseNormalmapTexture", False)
v.setBoolShaderProperty("UseCavity", False)
v.setBoolShaderProperty("FlatShading", False)
v.setFloatShaderProperty("Gloss",0)
v.setFloatShaderProperty("Metalness",0)

RenderRoom.toRenderRoom()

base = io.currentSceneFilepath()
# get the file name without extension and full path
base = io.getFileName(base)
base = base[:base.rfind(".")]

#setup the render room, we take 512*512 images with 256 rays per frame
RenderRoom.setCustomRenderSize(512, 512)
RenderRoom.setRaysPerFrame(256)
height = io.workArea().GetHeight()

# we need just N frames to render
N = 4
for j in range(0, N):
    #setup the random light, random ambient light and random camera position (from above)
    value = random.random() * 0.5
    RenderRoom.removeAllLights()
    RenderRoom.addLight()
    RenderRoom.setEnvironmentLight(100 - value * 50)
    ldir = vec3.RandNormal()
    ldir += vec3.AxisY*2
    ldir.Normalize()
    RenderRoom.setLightDirection(0, ldir)
    RenderRoom.setLightColor(0)
    RenderRoom.setLightIntensity(0, value)
    RenderRoom.setLightScattering(0,0.1)
    
    # the direction from above with a bit random horizontal shift
    start = vec3.RandNormal() + vec3.AxisY*3
    start.Normalize()
    # distant anough to fit the object into the square image
    start *= radius*4*height/2000
    # FOV is 50 degrees
    Camera.setCamera(start, vec3(0,0,0), 50)

    # look the progress in the header
    io.progressBarInWindowHeader(j, N-1, "Rendering")
    
    # render the frame on the RED background
    v.setColorShaderProperty("Color",0xFFFF0000)
    RenderRoom.setRenderResult(f"UserPrefs/render/red.png")
    RenderRoom.renderFrame()
    
    # the GREEN background
    v.setColorShaderProperty("Color",0xFF00FF00)
    RenderRoom.setRenderResult(f"UserPrefs/render/green.png")
    RenderRoom.renderFrame()

    # we use 2 images with red and green background to remove the background and the the alpha channel (incliding shadow ovwr the invisible plane)
    io.removeBackground(f"UserPrefs/render/red.png",f"UserPrefs/render/green.png",f"UserPrefs/render/result/{base}/{j:04d}.png")
    io.removeFile(f"UserPrefs/render/red.png")
    io.removeFile(f"UserPrefs/render/green.png")

io.exec(io.documents("UserPrefs/render/result/"))
removeBgObject()