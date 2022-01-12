import cv2
import numpy as np
import pandas
from matplotlib import pyplot as plt
img = cv2.imread('filter.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25
#homogenous filter
dst = cv2.filter2D(img, -1,kernel)
#average algorithm- blurring algoriththm
blur =  cv2.blur(img,(5,5))
#gaussian blur
gblur =  cv2.GaussianBlur(img, (5,5),0)
#median filter with kernel 5
median = cv2.medianBlur(img,5)
#Bilateral filter - to preserve the edges as sharp
bilateralfilter = cv2.bilateralFilter(img,9,75,75)
titles= ['image','2d convolution','blur','Gblur','median','Bilateralfilter']
images = [img,dst,blur,gblur,median,bilateralfilter]

for i in range(6):
    # 2-rows 3-cols index+1
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()