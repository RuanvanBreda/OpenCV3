#Edge detection & image gradients
#Sudden changes in pixel intensities/densities

#Three main types of Edge Detection:
#Sobel - to emphasize  vertical or horizontal edges
#Laplacian - Gets all orientations
#Canny - Optimal due to low error rate, well defined edges and accurate detection. (1986)

#CANNY
#1. Applies Gaussian blurring
#2. Finds intensity gradient of the image
#3. Applies non-maximum supression (i.e. removes pixels that are not edges)
#4. Hysteresis - applies thresholds (i.e. if pixel is whithin upper and lower thresholds, it is considered an edge)

import cv2
import numpy as np

image = cv2.imread('./images/input.jpg',0)

#Extract Sobel Edges
sobel_x = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
sobel_y = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)

cv2.imshow('Original',image)
cv2.imshow('Sobel X',sobel_x)
cv2.imshow('Sobel Y',sobel_y)


sobel_OR = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Sobel OR',sobel_OR)

laplacian = cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow('Laplacian',laplacian)

canny_image = cv2.Canny(image,20,170)
cv2.imshow('Canny',canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

