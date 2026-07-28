import os
import sys
import pygltflib
from pygltflib import GLTF2

def gltf_to_glb(input_path, output_path):
    gltf = GLTF2().load(input_path)
    gltf.save_binary(output_path)
    print("Conversion complete:", output_path)

file_path = ""
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Arguments are always strings, so you might need to convert them
        file_path = sys.argv[1]
        print(f"The first argument is: {file_path}")
    else:
        print("No arguments provided.")
        quit

# Example usage
dir_name = os.path.dirname(file_path)
file_name = os.path.basename(file_path)
file = os.path.splitext(file_name)

print("file:", file_name)
print("file base:", file[0])
print("file ext:", file[1])
file_out_path = dir_name + "\\" + file[0] + ".glb"
file_in_path = file_path;

gltf_to_glb(file_in_path, file_out_path)
