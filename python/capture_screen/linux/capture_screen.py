#!/usr/bin/python3
# initial code courtesy of sentdex (youtube)

import numpy as np
import pyscreenshot as ImageGrab
import cv2
import time



def __main__():
	last_time = time.time()
	while(True):
		screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
		print("Loop took {} seconds".format(time.time()-last_time))
		last_time=time.time()
		cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)) # bgr (blue green red) to rgb (red green blue)
		if cv2.waitKey(25) & 0xFF ==ord('q'):
			cv2.destroyAllWindows()
			break

__main__()

