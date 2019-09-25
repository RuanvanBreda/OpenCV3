import cv2
import numpy as np

input = cv2.imread('./images/input.jpg')


print(input.shape)
print(f'Height of the image is {input.shape[0]} pixels')
print(f'Width of the image is {input.shape[1]} pixels')

cv2.imshow('Original Image', input)
cv2.waitKey()
gray_image = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY) #Convert to grayscale
cv2.imshow('Grayscale Image',gray_image)
cv2.waitKey()

cv2.imwrite('output.jpg',input)

cv2.destroyAllWindows()

#Alternative method
img = cv2.imread('./images/input.jpg',0)

cv2.imshow('Grayscale Image 2', img)
cv2.waitKey()
cv2.destroyAllWindows()