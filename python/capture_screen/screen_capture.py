import numpy as np # matrices and math
from PIL import ImageGrab # get image on screen
# import cv2
import time
import thread # running multiple operations at the same time
import ctypes # sending keys

import matplotlib as plot
import matplotlib.pyplot as mpplt # generating image to screen
import matplotlib.image as mpimg

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Enter = 0x0D


def show_screen():
    t = time.time()
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    implot = mpplt.imshow(screen)
    mpplt.show()

def reset_img():
    send_key(Enter)


class send_input():
    def __init__(self):
        self.intialized = True
    def send_key(self,hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    def release_key(self,hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

while (1):
    thread.start_new_thread(show_screen,())
    thread.start_new_thread(reset_img,())
