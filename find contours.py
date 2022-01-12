import cv2
import numpy as np
img = cv2.imread('apple.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# threshold value for gray image
ret, thresh = cv2.threshold(imgray,127,255,0)
# returns contours,hierarchy

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#returns the no of contours
print("Number of contours = " + str(len(contours)))
#return the (x,y) xordinate of 1st contour
print(contours[0])
#-1 will draw all contours
cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.imshow("Image",img)
cv2.imshow("Image gray",imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()