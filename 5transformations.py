#Transformations
#Affine and non-affine transformations
#Affine retain parrallel lines, angles
#Non affine retain collinearity and incidence

#Translation Matrix
# [[1 0 Tx] [0 1 Ty]]
#use openCV cv2.warpaffine to implement

import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

height, width = image.shape[:2]

quarter_width, quarter_height = width/4, height/4

translation_matrix = np.float32([[1,0,quarter_width],[0,1,quarter_height]])

image_translation = cv2.warpAffine(image,translation_matrix,(width,height))
cv2.imshow('Original',image)
cv2.imshow('Translation',image_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(translation_matrix)

#Rotation
#[[cos -sin] [sin cos]]
image = cv2.imread('./images/input.jpg')
height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),90,1)

rotated_image = cv2.warpAffine(image,rotation_matrix, (width,height))

cv2.imshow('Original Image',image)
cv2.imshow('Rotated Image',rotated_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

#Alternative way to do rotations
rotated_image = cv2.transpose(image)    #does 90 degree rotations
cv2.imshow('Rotated image',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Re-sizing, scaling and interpolation
image = cv2.imread('./images/input.jpg')

#Make image 3/4 of original size
image_scaled = cv2.resize(image, None, fx =0.75, fy=0.75)
cv2.imshow('Scaling - Linear Interpolation',image_scaled)
cv2.waitKey()

#Double image size
image_scaled = cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation',image_scaled)
cv2.waitKey()


image_scaled = cv2.resize(image,(900,400), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size',image_scaled)
cv2.waitKey()

cv2.destroyAllWindows()

#Image Pyramids
smaller= cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)
cv2.imshow('Smaller',smaller)
cv2.imshow('Larger',larger)
cv2.waitKey()
cv2.destroyAllWindows()

#Cropping Images
height, width = image.shape[:2]
start_row, start_col = int(height*0.25),int(width*0.25)
end_row, end_col = int(height*0.75),int(width*0.75)

cropped_image = image[start_row:end_row,start_col:end_col]

cv2.imshow('Original Image',image)
cv2.imshow("Cropped Image",cropped_image)
cv2.waitKey()
cv2.destroyAllWindows()
