import cv2
import numpy as np
import pandas
from matplotlib import pyplot as plt

img =  cv2.imread("smarties.png",cv2.IMREAD_GRAYSCALE)
# masking to threshold the image
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
#dilation- to remove black dots inside the white sphere
#kernel creates a white square of 2,2
kernel =  np.ones((5,5),np.uint8)
# no of iteration to remove the remaining black dots
dilation =  cv2.dilate(mask,kernel,iterations=2)
# erodes the boundary of the foreground object
erosion = cv2.erode(mask,kernel,iterations=1)
#opening - same as erosion with dilation
opening =  cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
#closing - first dialtion then erosion
closing =cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)

titles = ['image','mask','dilation','erosion','opening','closing','gradient','top hat']
images = [img,mask,dilation,erosion,opening,closing,mg,th]
for i in range(8):
    #1-rows 1-cols index+1
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()