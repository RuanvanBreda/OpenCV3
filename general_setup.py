import sys
print(sys.executable)

import os
print(os.getcwd())

import cv2
import numpy as np
import matplotlib

print(cv2.__version__)

#OpenCV (open source computer vision) stores RBG color space by default as three 8-bit integers (0-255)
#By mixing different values/intesities of each color the full color spectrum can be shown.
#Images are stored as multi-dimensional arrays
#OpenCV is written in C++
# opencv.org wikipedia.org/wiki/OpenCV
