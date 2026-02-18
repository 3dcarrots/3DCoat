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
    Зберігає зображення з масиву Numpy у формат AVIF з автоматичним вибором бітової глибини.

    Параметри:
    image_arr (np.ndarray): Вхідний масив зображення.
    output_path (str): Шлях до вихідного файлу.
    quality (int): CRF (0-63). Менше = краща якість.
    speed (int): Швидкість кодування (0-8).
    """
    
    # --- Етап 1: Аналіз вхідних даних ---
    if not isinstance(image_arr, np.ndarray):
        raise ValueError("Вхідні дані повинні бути масивом numpy.")

    dtype = image_arr.dtype
    shape = image_arr.shape
    
    # Розпаковка розмірів (виправлено логіку)
    if len(shape) == 2:
        height, width = shape
        channels = 1
    elif len(shape) == 3:
        height, width, channels = shape
    else:
        raise ValueError(f"Непідтримувана розмірність масиву: {shape}")

    # --- Етап 2: Нормалізація даних ---
    working_arr = image_arr
    is_high_bit_depth = False

    if dtype.kind == 'f':
        # Конвертація float -> uint16
        working_arr = (image_arr * 65535).clip(0, 65535).astype(np.uint16)
        dtype = np.uint16
        is_high_bit_depth = True
    elif dtype == np.uint16:
        is_high_bit_depth = True
    elif dtype == np.uint8:
        is_high_bit_depth = False
    else:
        # Інші типи -> uint16
        working_arr = image_arr.astype(np.uint16)
        is_high_bit_depth = True

    # --- Етап 3: Вибір піксельного формату ---
    source_format = ""  
    target_pix_fmt = "" 

    if is_high_bit_depth:
        # 12-бітний режим
        if channels == 1:
            source_format = "gray16le" 
            target_pix_fmt = "gray12le"
        elif channels == 3:
            source_format = "rgb48le"
            target_pix_fmt = "yuv444p12le"
        elif channels == 4:
            source_format = "rgba64le"
            # AV1 часто не підтримує 12-бітну альфу в стандартному режимі stream
            # Відкидаємо альфу для стабільності
            working_arr = working_arr[:, :, :3]
            working_arr = np.ascontiguousarray(working_arr)
            source_format = "rgb48le"
            target_pix_fmt = "yuv444p12le"
            channels = 3
    else:
        # 8-бітний режим
        if channels == 1:
            source_format = "gray"
            target_pix_fmt = "gray"
        elif channels == 3:
            source_format = "rgb24"
            target_pix_fmt = "yuv444p"
        elif channels == 4:
            source_format = "rgba"
            target_pix_fmt = "yuva444p" # Спробуємо зберегти альфу

    # --- Етап 4: Налаштування контейнера ---
    container = None
    try:
        container = av.open(output_path, mode='w')
        stream = container.add_stream("libaom-av1", rate=1)
        
        stream.width = width
        stream.height = height
        
        # Перевірка підтримки формату
        try:
            stream.pix_fmt = target_pix_fmt
        except ValueError:
            # Якщо yuva444p не підтримується
            if "yuva" in target_pix_fmt:
                target_pix_fmt = "yuv444p"
                stream.pix_fmt = target_pix_fmt
                if channels == 4 and dtype == np.uint8:
                    working_arr = working_arr[:, :, :3]
                    working_arr = np.ascontiguousarray(working_arr)
                    source_format = "rgb24"
            else:
                raise RuntimeError("Неможливо підібрати сумісний піксельний формат.")

        tilesX = math.floor(width/tile_size)
        tilesY = math.floor(height/tile_size)
        if tilesX < 1: 
            tilesX = 1
        if tilesX < 2: 
            tilesX = 2

        stream.options = {
            'cpu-used': str(speed),
            'crf': str(quality),
            'usage': 'allintra',
            'row-mt': '1',
            'tiles': str(tilesX)+'x'+str(tilesY),
        }
        
        # --- Етап 5: Кодування ---
        frame = av.VideoFrame.from_ndarray(working_arr, format=source_format)
        
        # ВИПРАВЛЕННЯ: Використовуємо ціле число 1 замість 'I' для типу кадру
        # 1 = AV_PICTURE_TYPE_I (Intra/Keyframe)
        frame.pict_type = 1 
        
        # Кодування пакетів
        for packet in stream.encode(frame):
            container.mux(packet)
            
        # Завершення потоку
        for packet in stream.encode():
            container.mux(packet)
            
    except Exception as e:
        # Прокидаємо помилку далі для відлагодження у хості
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

    def pySerialize(self):
        cPy.cCore.cREG.slider_int(self.quality)
        cPy.cCore.cREG.slider_int(self.speed)
        cPy.cCore.cREG.slider_int(self.tile_size)
        # cPy.cCore.cREG.checkbox(self.greyscale)

avifSettings = AVIFSettings()

class AVIFCodec(cPy.cIO.cImageCodec):
    def __init__(self):
        cPy.cIO.cImageCodec.__init__(self)

    def Decode(self, Src: cPy.cIO.cFile, To: cPy.cImage.cImage):
        try:            
            container = av.open(Src.GetFilePn().ToCharPtr())
            
            img_array = None

            # Декодуємо перший кадр
            for frame in container.decode(video=0):
                # 1. Перевіряємо бітову глибину вхідного кадру
                # Зазвичай беремо глибину першого компонента (наприклад, Y або R)
                bit_depth = 8
                if frame.format and frame.format.components:
                    bit_depth = frame.format.components[0].bits
                
                # 2. Вибираємо цільовий формат на основі глибини
                if bit_depth > 8:
                    # Якщо 10 або 12 біт -> конвертуємо в 16 біт (uint16)
                    target_fmt = 'rgb48le'
                else:
                    # Якщо 8 біт -> залишаємо 8 біт (uint8)
                    target_fmt = 'rgb24'

                # 3. Отримуємо масив у потрібному форматі
                img_array = frame.to_ndarray(format=target_fmt)
                break
            
            if img_array is None:
                return False

            # Перевірка для налагодження
            print(f"Decoded AVIF: depth={bit_depth}, dtype={img_array.dtype}, shape={img_array.shape}")     
            
            # Фліп (дзеркальне відображення по вертикалі), якщо це потрібно для 3DCoat
            img_array = np.flip(img_array, axis=0)

            # Передаємо в CoreAPI (він повинен вміти приймати і uint8, і uint16)
            cPy.CoreAPI.Image.cImageFromArray(img_array, To)
            
            return True 
        except Exception as e:
            print(f"AVIF Decode Error: {e}")
            import traceback
            traceback.print_exc()
            return False

    def Encode(self, Image: cPy.cImage.cImage, To: cPy.cIO.cFile):
        # ... (Ваш код Encode без змін)
        try:
            path = To.GetFilePn().ToCharPtr()
            img_array = np.asarray(Image)

            CRF = math.floor((100-avifSettings.quality.Value)*63/100)
            img_array = np.flip(img_array, axis=0)
            
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

def convert_to_avif(src_path: str, dst_path: str = None):
    """
    Конвертує будь-який формат, підтримуваний imagecodecs, в AVIF.
    Якщо вхідні дані > 8 біт, зберігає як 12-бітний AVIF.
    """
    try:
        if dst_path is None:
            dst_path = os.path.splitext(src_path)[0] + ".avif"

        img = cPy.cImage.cImage()
        cPy.cIO.cIO.LoadImage(src_path, img)
        cPy.cIO.cIO.SaveImage(dst_path, img)

    except Exception as e:
        print(f"Conversion Error for {src_path}: {e}")
        return False



@d_slot
def ConvertToAvif():
    tmpFile = coat.io.openFileDialog("*.*")
    new_path = str(Path(tmpFile).with_suffix(".avif"))
    if cPy.cCore.cREG.modalMessageBox("MyDialog", "MyDialogCaption", "Ok,Cancel", 1, avifSettings) == 1:
        convert_to_avif(tmpFile, new_path)


@d_slot
def ConvertFolderToAvif():
    # 1. Ініціалізація Tkinter (приховуємо головне вікно, щоб показати лише діалог)

    print("Відкриваю діалог вибору теки...")

    # 2. Відкриття системного діалогу вибору теки
    folder_path = coat.io.openFileDialog("*.*")

    # Перевірка, чи користувач щось вибрав
    if not folder_path:
        print("Скасовано: Теку не вибрано.")
        return

    # 3. Налаштування шляху та розширень
    search_path = Path(folder_path).parent
    # Враховуємо різні регістри (.JPG, .png) та розширення jpeg
    target_extensions = {'.jpg', '.jpeg', '.png', '.avif'} 
    
    print(f"\nШукаю у: {folder_path}\n" + "-"*30)

    # 4. Перебір файлів у теці
    try:
        # iterdir() проходить тільки по поточній теці (не заходить у підпапки)
        if cPy.cCore.cREG.modalMessageBox("MyDialog", "MyDialogCaption", "Ok,Cancel", 1, avifSettings) == 1:
            flcnt = 0
            for file_path in search_path.iterdir():
                flcnt += 1

            flpos = 0    
            for file_path in search_path.iterdir():
                if file_path.is_file():
                    # Перевіряємо розширення (переводимо в нижній регістр для порівняння)
                    if file_path.suffix.lower() in target_extensions:
                        print(file_path.name)
                        tmpFile = file_path
                        # avifSettings.speed.Value = 3
                        # if file_path.suffix.lower() == ".png":
                        #     avifSettings.quality.Value = 98
                        # else:
                        #     avifSettings.quality.Value = 70
                        coat.io.progressBar(flpos, flcnt, "Convert "+str(file_path)+" to AVIF")
                        new_path = str(Path(file_path).with_suffix(".avif"))
                        convert_to_avif(str(tmpFile), str(new_path))
                        flpos += 1

    except PermissionError:
        print("Помилка: Немає прав доступу до цієї теки.")
        return


# Create a separate section for our extension in the View menu.
@d_menu_section(cTemplates.MainMenu.Scripts.Scripts_S_Useful)
def MouseInfoSection():
    # Add a menu item to this section that will enable and disable information about the mouse and cursor.
    coat.menu_item(ConvertToAvif.UICmd()) 
    coat.menu_item(ConvertFolderToAvif.UICmd()) 
    


# pillow_convert_12bit('input_16bit.png', 'output_12bit.avif')



class AVIFExtension(cPy.cCore.cExtension):
    def __init__(self):
        cPy.cCore.cExtension.__init__(self)


    def onStart(self):
        self.avifCodec = AVIFCodec()
        cPy.cIO.cIO.AddCodec("AVIF", self.avifCodec)

avifExtension = AVIFExtension()
