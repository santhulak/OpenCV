import cv2
import numpy as np
img = cv2.imread('lena.jpg')
layer = img.copy()

#gaussian pyramid

gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()