import cv2
import numpy as np

#create a black image
image = np.zeros((512,512,3), np.uint8)

#craete a one channel image
image_bw = np.zeros((512,512), np.uint8)

cv2.imshow('Black rectangle (Color)',image)
cv2.imshow('Black Rectangle (B&W)',image_bw)

cv2.waitKey(0)

#Draw a line over the images
cv2.line(image,(0,0),(511,511),(255,0,0),5)
cv2.imshow('Blue Line',image)

cv2.waitKey(0)

#Draw a rectangle
cv2.rectangle(image,(100,100),(300,250),(0,0,255),5)
cv2.imshow('Red Rectangle',image)
cv2.waitKey(0)

#Draw a circle
cv2.circle(image,(250,250),100,(0,255,0),-1)
cv2.imshow('Green Filled Circle',image)
cv2.waitKey(0)

#Draw a polygon
pts = np.array([[10,50],[40,70],[170,123]], np.int32)
print(pts)
pts = pts.reshape((-1,1,2))
print(pts)
cv2.polylines(image,[pts],True,(0,0,255,3))
cv2.imshow('Polygon',image)
cv2.waitKey(0)


#Adding text to images
cv2.putText(image, 'Hello World', (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow('Hello world',image)
cv2.waitKey(0)


cv2.destroyAllWindows()

