#Segmentation - Partitioning images into different regions

import cv2
import numpy as np

image = cv2.imread('images/shapes.jpg')
cv2.imshow('Input Image', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
contours,hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  #Can replace with cv2.CHAIN_APPROX_SIMPLE
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)
print(contours) #OpenCV stores contours in a list of lists
print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0,255,0), 3) #-1 for all contours otherwise 1,2 or 3 to pring just some of the contours

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()