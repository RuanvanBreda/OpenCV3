#Understanding Color Spaces
#RGB Red Green Blue (0-255)
#HSV Hue (0-179) Saturation (0-255) Value/Brightness (0-255) - used for color filter
#CMYK Cyan Magenta Yello Black


import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

B,G,R = image[0,0]  #BGR values of pixel at 0,0 position
print(f'B = {B}, G = {G}, R = {R}')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)
print(gray_image.shape)

print(gray_image[0,0])

#HSV Color Space
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image',hsv_image)   #Remeber that imshow shows as RGB image
cv2.imshow('Hue Channel',hsv_image[:,:,0])
cv2.imshow('Saturation Channel',hsv_image[:,:,1])
cv2.imshow('Value Channel',hsv_image[:,:,2])

cv2.waitKey()
cv2.destroyAllWindows()

#RGB Individual Channels
