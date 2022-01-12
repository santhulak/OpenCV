import cv2
import numpy as np
import pandas
from matplotlib import pyplot as plt
#img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
#laplasian
#64F is 64 float
#ksize is kernel size
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
#convert into unsigned int
lap = np.uint8(np.absolute(lap))

# sobel
#1 means sobelX method is used
#0 means order of y derivative
sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)

#convert into unsigned int
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#combine sobelX and sobelY
sobelCombined = cv2.bitwise_or(sobelX,sobelY)

#canny detection
#100- threshold1, 200-threshold2 which is edge tracking by hysteresis
canny = cv2.Canny(img,100,200)

titles = ['image', 'Laplacian','SobelX','SobelY','sobelCombined','canny']
images = [img,lap,sobelX,sobelY,sobelCombined,canny]
for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()