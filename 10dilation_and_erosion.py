#Dilation and Erosion
#Dilation - add pixels to the boundaries of objects in an image.
#Erosion - Removes pixels at the boundaries of objects in an image.
#Opening - Erosion followed by dilation
#Closing - Dilation followed by erosion

import cv2
import numpy as np

image = cv2.imread('./images/opencv_inv.png',0)

cv2.imshow('Orginal',image)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(image,kernel,iterations=1)
cv2.imshow('Erosion',erosion)

dilation = cv2.dilate(image,kernel,iterations=1)
cv2.imshow('Dilation',dilation)

opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
cv2.imshow('Opening',opening)

closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow('Closing',closing)

cv2.waitKey(0)
cv2.destroyAllWindows()