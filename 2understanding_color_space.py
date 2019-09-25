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
B,G,R = cv2.split(image)

cv2.imshow('Blue',B)
cv2.imshow('Green',G)
cv2.imshow('Red',R)
cv2.waitKey(0)
cv2.destroyAllWindows()

    #Remake original image
merged = cv2.merge([B,G,R])
cv2.imshow('Merged Image',merged)

    #Amplify the blue of the image
merged = cv2.merge([B+100,G,R])
cv2.imshow('Merged with Blue enhanced Image',merged)

cv2.waitKey(0)
cv2.destroyAllWindows()

#create a matrix of zeros
print(image.shape[:2])
zeros = np.zeros(image.shape[:2],dtype='uint8')
cv2.imshow('Red',cv2.merge([zeros,zeros,R]))
cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
cv2.imshow('Blue',cv2.merge([B,zeros,zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()