import sys

import os
import time
import cPy.cCore
import cPy.CoreAPI
import coat

import av
import numpy as np

import cPy.cImage
import cPy.cIO

import cTemplates.MainMenu.Scripts
from pathlib import Path
import math

from cTemplates.Structs import *

def save_numpy_to_avif(image_arr: np.ndarray, output_path: str, quality: int = 20, speed: int = 6, tile_size = 2048):
    """
    Saves an image from a Numpy array to AVIF format with automatic bit depth selection.

    Parameters:
    image_arr (np.ndarray): Input image array.
    output_path (str): Path to the output file.
    quality (int): CRF (0-63). Lower = better quality.
    speed (int): Encoding speed (0-8).
    """
    
    # --- Stage 1: Input data analysis ---
    if not isinstance(image_arr, np.ndarray):
        raise ValueError("Input data must be a numpy array.")

    dtype = image_arr.dtype
    shape = image_arr.shape
    
    # Unpack dimensions (fixed logic)
    if len(shape) == 2:
        height, width = shape
        channels = 1
    elif len(shape) == 3:
        height, width, channels = shape
    else:
        raise ValueError(f"Unsupported array dimension: {shape}")

    # --- Stage 2: Data normalization ---
    working_arr = image_arr
    is_high_bit_depth = False

    if dtype.kind == 'f':
        # Convert float -> uint16
        working_arr = (image_arr * 65535).clip(0, 65535).astype(np.uint16)
        dtype = np.uint16
        is_high_bit_depth = True
    elif dtype == np.uint16:
        is_high_bit_depth = True
    elif dtype == np.uint8:
        is_high_bit_depth = False
    else:
        # Other types -> uint16
        working_arr = image_arr.astype(np.uint16)
        is_high_bit_depth = True

    # --- Stage 3: Pixel format selection ---
    source_format = ""  
    target_pix_fmt = "" 

    if is_high_bit_depth:
        # 12-bit mode
        if channels == 1:
            source_format = "gray16le" 
            target_pix_fmt = "gray12le"
        elif channels == 3:
            source_format = "rgb48le"
            target_pix_fmt = "yuv444p12le"
        elif channels == 4:
            source_format = "rgba64le"
            # AV1 often does not support 12-bit alpha in standard stream mode
            # Discard alpha for stability
            working_arr = working_arr[:, :, :3]
            working_arr = np.ascontiguousarray(working_arr)
            source_format = "rgb48le"
            target_pix_fmt = "yuv444p12le"
            channels = 3
    else:
        # 8-bit mode
        if channels == 1:
            source_format = "gray"
            target_pix_fmt = "gray"
        elif channels == 3:
            source_format = "rgb24"
            target_pix_fmt = "yuv444p"
        elif channels == 4:
            # AV1 often does not support alpha in standard stream mode
            # Discard alpha for stability
            working_arr = working_arr[:, :, :3]
            working_arr = np.ascontiguousarray(working_arr)
            source_format = "rgb24"
            target_pix_fmt = "yuv444p"
            channels = 3

    # --- Stage 4: Container setup ---
    container = None
    try:
        container = av.open(output_path, mode='w')
        stream = container.add_stream("libaom-av1", rate=1)
        
        stream.width = width
        stream.height = height
        
        # Format support
        stream.pix_fmt = target_pix_fmt

        tilesX = math.floor(width/tile_size)
        tilesY = math.floor(height/tile_size)
        if tilesX < 1: 
            tilesX = 1
        if tilesX < 2: 
            tilesX = 2

        opts = {
            'cpu-used': str(speed),
            'crf': str(quality),
            'usage': 'allintra',
            'row-mt': '1'
        }
        
        if tilesX > 1:
            opts['tile-columns'] = str(int(math.log2(tilesX)))
        if tilesY > 1:
            opts['tile-rows'] = str(int(math.log2(tilesY)))
            
        # 12-bit formats require Profile 2 in libaom-av1
        if is_high_bit_depth:
            opts['profile'] = '2'
            
        stream.options = opts
        
        # --- Stage 5: Encoding ---
        frame = av.VideoFrame.from_ndarray(working_arr, format=source_format)
        
        # FIX: Use integer 1 instead of 'I' for frame type
        # 1 = AV_PICTURE_TYPE_I (Intra/Keyframe)
        frame.pict_type = 1 
        
        # Packet encoding
        for packet in stream.encode(frame):
            container.mux(packet)
            
        # End of stream
        for packet in stream.encode():
            container.mux(packet)
            
    except Exception as e:
        # Pass the error further for debugging in the host
        raise e
    finally:
        if container:
            container.close()

@d_class
class AVIFSettings(cPy.cCore.BaseClass):
    def __init__(self):
        cPy.cCore.BaseClass.__init__(self)        
        self.quality = cPy.cCore.cSInt("Quality", 80, 0, 100)
        self.speed = cPy.cCore.cSInt("speed", 3, 0, 10)
        self.tile_size = cPy.cCore.cSInt("tile_size", 2048, 128, 4096)
        self.greyscale = cPy.cCore.cSBool("greyscale")
        self.power_of_two = cPy.cCore.cSBool("Power of 2")
        self.power_of_two.Value = True

    def pySerialize(self):
        cPy.cCore.cREG.slider_int(self.quality)
        cPy.cCore.cREG.slider_int(self.speed)
        cPy.cCore.cREG.slider_int(self.tile_size)
        # cPy.cCore.cREG.checkbox(self.greyscale)
        cPy.cCore.cREG.checkbox(self.power_of_two)

avifSettings = AVIFSettings()

class AVIFCodec(cPy.cIO.cImageCodec):
    def __init__(self):
        cPy.cIO.cImageCodec.__init__(self)

    def Decode(self, Src: cPy.cIO.cFile, To: cPy.cImage.cImage):
        try:            
            container = av.open(Src.GetFilePn().ToCharPtr())
            
            img_array = None

            # Decode the first frame
            for frame in container.decode(video=0):
                # 1. Check the bit depth of the input frame
                # Usually take the depth of the first component (e.g., Y or R)
                bit_depth = 8
                if frame.format and frame.format.components:
                    bit_depth = frame.format.components[0].bits
                
                # 2. Select target format based on depth
                if bit_depth > 8:
                    # If 10 or 12 bit -> convert to 16 bit (uint16)
                    target_fmt = 'rgb48le'
                else:
                    # If 8 bit -> keep 8 bit (uint8)
                    target_fmt = 'rgb24'

                # 3. Get array in the required format
                img_array = frame.to_ndarray(format=target_fmt)
                break
            
            if img_array is None:
                return False

            if bit_depth > 8 and img_array.dtype == np.uint8:
                img_array = img_array.view(np.uint16)
                
            # Debug check
            print(f"Decoded AVIF: depth={bit_depth}, dtype={img_array.dtype}, shape={img_array.shape}")     
            
            # Flip (vertical mirroring), if needed for 3DCoat
            img_array = np.flip(img_array, axis=0)

            # Pass to CoreAPI (it should be able to accept both uint8 and uint16)
            cPy.CoreAPI.Image.cImageFromArray(img_array, To)
                        
            return True 
        except Exception as e:
            print(f"AVIF Decode Error: {e}")
            import traceback
            traceback.print_exc()
            return False

    def Encode(self, Image: cPy.cImage.cImage, To: cPy.cIO.cFile):
        # ... (Your Encode code unchanged)
        try:
            path = To.GetFilePn().ToCharPtr()
            img_array = np.asarray(Image)

            CRF = math.floor((100-avifSettings.quality.Value)*63/100)
            img_array = np.flip(img_array, axis=0)
            
            if getattr(avifSettings.power_of_two, 'Value', False):
                h, w = img_array.shape[:2]
                new_w = 2 ** round(math.log2(w))
                new_h = 2 ** round(math.log2(h))
                
                if new_w != w or new_h != h:
                    print(f"Resizing from {w}x{h} to {new_w}x{new_h} (Power of 2)")
                    try:
                        import cv2
                        img_contig = np.ascontiguousarray(img_array)
                        img_array = cv2.resize(img_contig, (new_w, new_h), interpolation=cv2.INTER_AREA)
                    except ImportError:
                        try:
                            from PIL import Image as PILImage
                            if img_array.dtype == np.uint8:
                                img_contig = np.ascontiguousarray(img_array)
                                img = PILImage.fromarray(img_contig)
                                resample_filter = PILImage.Resampling.LANCZOS if hasattr(PILImage, 'Resampling') else PILImage.LANCZOS
                                img = img.resize((new_w, new_h), resample_filter)
                                img_array = np.array(img)
                            else:
                                print("Warning: 16-bit resize requires OpenCV. Saving in original size.")
                        except ImportError:
                            print("Warning: Neither cv2 nor PIL is available. Cannot resize image.")

            speed = avifSettings.speed.Value
            # print(CRF)
            # print(speed)

            save_numpy_to_avif(img_array, path, CRF, speed, avifSettings.tile_size.Value)

            return True

        except Exception as e:
            print(f"AVIF Encode Error: {e}")
            import traceback
            traceback.print_exc()
            return False       

    def CheckMagic(self, Magic: int, ext: str):
        return -1        





class AVIFExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)


    def onStart(self):
        self.avifCodec = AVIFCodec()
        cPy.cIO.cIO.AddCodec("AVIF", self.avifCodec)

avifExtension = AVIFExtension()
