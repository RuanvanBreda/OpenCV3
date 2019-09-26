#Arithmetic Operations
import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

matrix = np.ones(image.shape, dtype='uint8')*75

added = cv2.add(image,matrix)
subtracted = cv2.subtract(image,matrix)
cv2.imshow('Added',added)
cv2.imshow('Subtracted',subtracted)
cv2.waitKey(0)

#Clipping occurs at values above and below 255 and 0 respectively



#We use this concept for creating masks
#bitwise operations

square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-2)
cv2.imshow('Square',square)

ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,100,255,-1)
cv2.imshow('Ellipse',ellipse)

cv2.waitKey(0)

#BITWISE OPERATIONS
and_operation = cv2.bitwise_and(square,ellipse)
or_operation = cv2.bitwise_or(square,ellipse)
xor_operation = cv2.bitwise_xor(square,ellipse)
not_operation = cv2.bitwise_not(square)

cv2.imshow('AND',and_operation)
cv2.imshow('OR',or_operation)
cv2.imshow('XOR',xor_operation)
cv2.imshow('NOT',not_operation)
cv2.waitKey(0)




cv2.destroyAllWindows()