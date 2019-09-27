import cv2
import numpy as np
import matplotlib.pyplot as plt

#PERSPECTIVE TRANSFORMATION - NON_AFFINE TRANSFORM
image = cv2.imread('images/scan.jpg')

cv2.imshow('Original', image)
cv2.waitKey(0)


points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])
points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

matrix= cv2.getPerspectiveTransform(points_A, points_B) #transformation matrix

warped = cv2.warpPerspective(image, matrix, (420, 594))

cv2.imshow('warpPerspective', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()


#AFFINE TRANSFORM - ONLY NEED 3 POINTS - Lines maintain parralleslism
image = cv2.imread('images/ex2.jpg')
rows, cols, ch = image.shape

cv2.imshow('Original', image)


points_A = np.float32([[320, 15], [700, 215], [85, 610]])
points_B = np.float32([[0, 0], [420, 0], [0, 594]])

matrix = cv2.getAffineTransform(points_A, points_B) #transformation matrix

warped = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow('warpPerspective', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
