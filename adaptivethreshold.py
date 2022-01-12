import cv2
import numpy as np
img = cv2.imread('sudoku.png',0)
# threshold (image, lowerthr, highrethres, thresh type)
# using simple threshold for image
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# adaptativeThreshold(image, maxvalue, adaptmethod, thresholdtype,block size,value of c
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
cv2.imshow("Image",img)
cv2.imshow("Thresh1",th1)
cv2.imshow("Thresh2",th2)
cv2.imshow("Thresh3",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()