#Sharpening strengthens and emphasizes edges in an image
import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')
cv2.imshow('Original Image',image)

kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

sharpened_image = cv2.filter2D(image,-1,kernel_sharpening)

cv2.imshow('Sharpened Image',sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()