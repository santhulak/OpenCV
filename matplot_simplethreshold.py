import cv2
import numpy as np
import pandas
from matplotlib import pyplot as plt
img = cv2.imread('gradient.png',0)
# threshold (image, lowerthr, highrethres, thresh type)
# till 127 black after that white
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# till 127 white after that black
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# till the threshold value 127 pixel doesnt change after that it remains in 127 pixel
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# till the threshold vale 127 it is black after 127 pixel value remain same
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# till the threshold vale 127 pixel value remain same after 127 it is black
_,th5= cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,th1,th2,th3,th4,th5]
for i in range(6):
    # 2-rows 3-cols index+1
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""
cv2.imshow("Image",img)
cv2.imshow("Thresh1",th1)
cv2.imshow("Thresh2",th2)
cv2.imshow("Thresh3",th3)
cv2.imshow("Thresh4",th4)
cv2.imshow("Thresh5",th5)



cv2.waitKey(0)
cv2.destroyAllWindows()
"""