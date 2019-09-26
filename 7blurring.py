#Convolutions & blurring
#A convolution is a mathematicla operation performed on two functions producing a third function which is typically a modified version of one of the original functions.
#In computer vision we use kernel's to specify the size over which we run our manipulation fucntion over the image/.
#cv2.filter2D(image,-1,kernel)

import cv2
import numpy as np

image = cv2.imread('./images/elephant.jpg')
cv2.imshow('Original Image',image)
cv2.waitKey(0)

#Creating a 3x3 kernel
kernel_3x3 = np.ones((3,3),np.float32)/9

blurred_image = cv2.filter2D(image,-1,kernel_3x3)
cv2.imshow('Blurred Image 3x3 kernel',blurred_image)
cv2.waitKey(0)

kernel_7x7 = np.ones((7,7),np.float32)/49

blurred_image2 = cv2.filter2D(image,-1,kernel_7x7)
cv2.imshow('Blurred Image 7x7 kernel',blurred_image2)
cv2.waitKey(0)

cv2.destroyAllWindows()

#Other Blurring Methods
blur = cv2.blur(image,(3,3))
cv2.imshow('Averaging',blur)

gaussian = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Gaussian Blurring',gaussian)

median = cv2.medianBlur(image,5)
cv2.imshow('Median Blurring',median)

bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('Bilateral Blurring',bilateral)

dst = cv2.fastNlMeansDenoisingColored(image,None,6,6,7,21)
cv2.imshow('Fast Means Denoising',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()