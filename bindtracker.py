import numpy as np
import cv2

# create a call back function
def nothing(x):
    print(x)
#create black window
img = np.zeros((300,512,3), np.uint8)
# to create a named window
cv2.namedWindow('Image')

#To create trackbar (name,namewindow, start,end, callbackfunction
cv2.createTrackbar('B','Image', 0, 255, nothing)
cv2.createTrackbar('G','Image', 0, 255, nothing)
cv2.createTrackbar('R','Image', 0, 255, nothing)

switch = '0 : OFF\n 1: ON'
cv2.createTrackbar(switch,'Image',0,1,nothing)
while(1):
     cv2.imshow('Image', img)
     k = cv2.waitKey(1) & 0xFF
     if k == 27:
         break
    #get the position of the trackbar shows the color of BGR value
     b = cv2.getTrackbarPos('B','Image')
     g = cv2.getTrackbarPos('G', 'Image')
     r = cv2.getTrackbarPos('R', 'Image')
     s= cv2.getTrackbarPos(switch,'Image')

     if s==0:
         img[:] = 0
     else:
         img[:] = [b,g,r]
cv2.destroyAllWindows()