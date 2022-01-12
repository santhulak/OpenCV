import numpy as np
import cv2

# create a call back function
def nothing(x):
    print(x)

# to create a named window
cv2.namedWindow('Image')

#To create trackbar (name,namewindow, start,end, callbackfunction
# to print current value on the image
cv2.createTrackbar('CP','Image', 10, 400, nothing)

switch = 'color/gray'
cv2.createTrackbar(switch,'Image',0,1,nothing)
while(1):

     img = cv2.imread('lena.jpg')
     pos = cv2.getTrackbarPos('CP', 'Image')
     font = cv2.FONT_HERSHEY_SIMPLEX
     cv2.putText(img, str(pos),(50,150),font,4,(0,0,255))
     k = cv2.waitKey(1) & 0xFF
     if k == 27:
         break

     s= cv2.getTrackbarPos(switch,'Image')

     if s==0:
         pass
     else:
         img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     cv2.imshow('Image',img)
cv2.destroyAllWindows()