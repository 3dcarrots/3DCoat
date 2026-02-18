import os
import sys
import os.path

import numpy as np
import cv2

import coat
import multiprocessing
import threading


class frame_thread:
    sharpness: float
    frame: np.ndarray
    thread: threading.Thread

threads = []
save_threads = []

frames_sharp = []
frames_sharpMax = []


def estimateFrameSharpness(frame: np.ndarray) -> float:

    sigma = 0.33
    median = np.median(frame)

    vMin = int(max(0, (1.0 - sigma) * median))
    vMax = int(min(255, (1.0 + sigma) * median))

    mean, std = cv2.meanStdDev(cv2.Canny(frame, vMin, vMax))
    return mean[0][0] * std[0][0]

def calcSharpness(thread_id):     
    global threads      
    threads[thread_id].sharpness = estimateFrameSharpness(threads[thread_id].frame)




def VideoTo3D(inputVideo, output_path, shotCount):

        if not os.path.exists(inputVideo):
            return

        vidcap = cv2.VideoCapture(inputVideo)
        success, frame = vidcap.read()

        if not os.path.exists(output_path):
            os.makedirs(output_path)       

        frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

        window_size = frame_count / shotCount

        frame_available = True
        last_sharpness = 0

        
        next_check_point = window_size
        shot_id = 0
        frame_id = 0
        output_format = "jpg"
        thread_count = max(1, multiprocessing.cpu_count() // 2)
        sharp_frame = frame

        global frames_sharp
        global frames_sharpMax

        global threads, save_threads
        save_threads.clear()
        while frame_available:
            success, frameR = vidcap.read()

            if success:
                thread_id = frame_id % thread_count
                
                if len(threads) <= thread_id:
                    threads.append(frame_thread())


                if frame_id > thread_count:
                    threads[thread_id].thread.join()
                    frames_sharp.append(threads[thread_id].sharpness)

                    if last_sharpness < threads[thread_id].sharpness:
                        sharp_frame = threads[thread_id].frame
                        last_sharpness = threads[thread_id].sharpness

                    if frame_id > next_check_point:
                        frame_path = os.path.join(output_path, "shot%04d.%s" % (shot_id, output_format))
                        # cv2.imwrite(frame_path, sharp_frame)   
                        # shot_frame = np.array(sharp_frame, copy=True)  
                        while len(frames_sharpMax) < len(frames_sharp):
                            frames_sharpMax.append(last_sharpness)

                        thread = threading.Thread(target=lambda frame_path, sharp_frame: cv2.imwrite(frame_path, sharp_frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) , args=([frame_path, sharp_frame]))
                        thread.start()
                        save_threads.append(thread)
                        shot_id += 1
                        next_check_point = window_size*shot_id+window_size
                        coat.io.progressBar(shot_id, shotCount, "Getting sharp frames from the video")
                        last_sharpness = 0

                threads[thread_id].frame = frameR
                threads[thread_id].sharpness = -1

                # do_calc_sarp(thread_id)
                threads[thread_id].thread = threading.Thread(target=calcSharpness, args=([thread_id]))     
                threads[thread_id].thread.start()

                frame_id += 1
            else:
                frame_available = False
        vidcap.release()

