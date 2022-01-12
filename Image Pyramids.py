import cv2
import numpy as np
img = cv2.imread('lena.jpg')
# decrease the resolution of original image
lr1 =cv2.pyrDown(img)
# decrease the resolution of lr1 image further
lr2=cv2.pyrDown(lr1)
# bit increase the resolution of lr2 image
lr3 =cv2.pyrUp(lr2)
cv2.imshow('Original Image',img)
cv2.imshow('Pyrdown1 Image',lr1)
cv2.imshow('Pyrdown2 Image',lr2)
cv2.imshow('Pyrup Image',lr3)
cv2.waitKey(0)
cv2.destroyAllWindows()