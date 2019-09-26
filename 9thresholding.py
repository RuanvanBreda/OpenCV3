#Thresholding, Binarizatio & Adaptive Thresholding

#Thresholding always uses greyscale images
#Thresholding is the act of converting an image to binary form.
#cv2.threshold(image,ThresholdValue, MAX_value, MIN_value, Threshold_type)

import cv2
import numpy as np

image = cv2.imread('./images/gradient.jpg',0)
cv2.imshow('Original',image)

ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('1 Threshold BINARY',thresh1)

ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold BINARY_INV',thresh2)

ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('3 Threshold TRUNC',thresh3)

ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow('4 Threshold TOZERO',thresh4)

ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('5 Threshold TOZERO_INV',thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('./images/Origin_of_Species.jpg',0)

cv2.imshow('Original Image',image)

gaussian_blur = cv2.GaussianBlur(image,(3,3),0)
cv2.imshow('Gaussian Blur',gaussian_blur)


adaptive_thresholding = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow('Adaptive Mean Thresholding',adaptive_thresholding)


_,th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu Thresholding',th2)

blur = cv2.GaussianBlur(image,(5,5),0)
_,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Gaussian Otsu\'s Thresholding',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()