import os
import bpy
bpy.data.filepath
file_path = bpy.data.filepath
file_name = bpy.path.display_name_from_filepath(file_path)
dir_name = os.path.dirname(file_path)

file_gltf = ".gltf"
file_blend = ".blend"

# Import GLTF
bpy.ops.import_scene.gltf(filepath = dir_name + "\\" + file_name + file_gltf)
# Export blend file
bpy.ops.file.make_paths_relative()
bpy.ops.wm.save_mainfile(filepath = dir_name + "\\" + file_name + file_blend)
# Close Blender
bpy.ops.wm.quit_blender()