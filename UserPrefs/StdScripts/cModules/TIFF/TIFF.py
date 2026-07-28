import sys
import os
import time
import cPy.cCore
import cPy.CoreAPI
import coat

import numpy as np
import tifffile as tiff

import cPy.cImage
import cPy.cIO

from pathlib import Path

from cTemplates.Structs import d_class

@d_class
class TIFFSettings(cPy.cCore.BaseClass):
    def __init__(self):
        cPy.cCore.BaseClass.__init__(self)        
        self.compression = cPy.cCore.cSInt("Compression (0=None, 1=Deflate, 2=LZW)", 1, 0, 2)
        self.tile_size = cPy.cCore.cSInt("Tile Size", 2048, 128, 4096)

    def pySerialize(self):
        cPy.cCore.cREG.slider_int(self.compression)
        cPy.cCore.cREG.slider_int(self.tile_size)

tiffSettings = TIFFSettings()

class TIFFCodec(cPy.cIO.cImageCodec):
    def __init__(self):
        cPy.cIO.cImageCodec.__init__(self)

    def Decode(self, Src: cPy.cIO.cFile, To: cPy.cImage.cImage):
        try:            
            path = Src.GetFilePn().ToCharPtr()
            img_array = tiff.imread(path)
            
            if img_array is None:
                return False

            # Залишаємо лише 2D або 3D масив для окремого кадру
            while img_array.ndim > 3:
                img_array = img_array[0]
                
            # Перевірка на планарне розташування (C, H, W)
            if img_array.ndim == 3 and img_array.shape[0] in [1, 2, 3, 4] and img_array.shape[2] > 4:
                img_array = np.transpose(img_array, (1, 2, 0))

            if img_array.ndim == 3:
                channels = img_array.shape[2]
                if channels > 4:
                    # Беремо тільки перші 4 канали (RGBA)
                    img_array = img_array[:, :, :4]
            elif img_array.ndim == 2:
                # 3DCoat очікує 3D масив: (H, W, Channels)
                img_array = img_array[:, :, np.newaxis]
            elif img_array.ndim < 2:
                print("TIFF Decode Error: Image has less than 2 dimensions.")
                return False

            # Приведення до підтримуваного dtype (за специфікацією 3DCoat)
            valid_dtypes = (np.uint8, np.uint16, np.float16, np.float32)
            
            if img_array.dtype not in valid_dtypes:
                if img_array.dtype == np.float64:
                    img_array = img_array.astype(np.float32)
                elif img_array.dtype == bool:
                    img_array = img_array.astype(np.uint8) * 255
                elif np.issubdtype(img_array.dtype, np.integer):
                    # Приведення int32/int64 до float32 для захисту від втрати даних
                    if img_array.itemsize > 2:
                        img_array = img_array.astype(np.float32)
                    elif img_array.dtype == np.uint8 or img_array.dtype == np.int8:
                        img_array = img_array.astype(np.uint8)
                    else:
                        img_array = img_array.astype(np.uint16)
                else:
                    img_array = img_array.astype(np.float32)

            # print(f"Decoded TIFF: dtype={img_array.dtype}, shape={img_array.shape}")     
            
            # 3DCoat очікує перевернуте зображення по Y
            img_array = np.flip(img_array, axis=0)

            if not img_array.flags.c_contiguous:
                img_array = np.ascontiguousarray(img_array)

            cPy.CoreAPI.Image.cImageFromArray(img_array, To)
            return True 
        except Exception as e:
            print(f"TIFF Decode Error: {e}")
            import traceback
            traceback.print_exc()
            return False

    def Encode(self, Image: cPy.cImage.cImage, To: cPy.cIO.cFile):
        try:
            path = To.GetFilePn().ToCharPtr()
            # Отримання масиву numpy з внутрішнього формату 3DCoat
            img_array = np.asarray(Image)

            # Розворот назад
            img_array = np.flip(img_array, axis=0)
            
            compression_map = {
                0: None,
                1: 'zlib',
                2: 'lzw'
            }
            comp_choice = tiffSettings.compression.Value
            comp = compression_map.get(comp_choice, 'zlib')
            
            # Збереження за допомогою tifffile
            tiff.imwrite(path, img_array, compression=comp)

            return True

        except Exception as e:
            print(f"TIFF Encode Error: {e}")
            import traceback
            traceback.print_exc()
            return False       

    def CheckMagic(self, Magic: int, ext: str):
        if ext.lower() in ["tif", "tiff"]:
            return 100
        return -1        

def convert_to_tiff(src_path: str, dst_path: str = None):
    try:
        if dst_path is None:
            dst_path = os.path.splitext(src_path)[0] + ".tiff"

        img = cPy.cImage.cImage()
        cPy.cIO.cIO.LoadImage(src_path, img)
        cPy.cIO.cIO.SaveImage(dst_path, img)

    except Exception as e:
        print(f"Conversion Error for {src_path}: {e}")
        return False

class TIFFExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)

    def onStart(self):
        self.tiffCodec = TIFFCodec()
        cPy.cIO.cIO.AddCodec("TIFF", self.tiffCodec)
        cPy.cIO.cIO.AddCodec("TIF", self.tiffCodec)

tiffExtension = TIFFExtension()
