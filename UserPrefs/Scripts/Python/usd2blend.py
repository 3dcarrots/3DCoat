import os
import bpy
bpy.context.scene.render.engine = 'CYCLES'
bpy.data.filepath
file_path = bpy.data.filepath
file_name = bpy.path.display_name_from_filepath(file_path)
dir_name = os.path.dirname(file_path)

file_usd = ".usd"
file_blend = ".blend"

# Import USD
bpy.ops.wm.usd_import(filepath = dir_name + "\\" + file_name + file_usd)
# Export blend file
bpy.ops.file.make_paths_relative()
bpy.ops.wm.save_mainfile(filepath = dir_name + "\\" + file_name + file_blend)
# Close Blender
bpy.ops.wm.quit_blender()