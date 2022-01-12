import numpy as np
import cv2
img = cv2.imread("messi5.jpg")
img2 =  cv2.imread("opencv-logo.png")
# returns a tuple of no of rows, columns, channels
print(img.shape)
# returns total number of pixels is accessed
print(img.size)
#returns Image datatype is obtaines
print(img.dtype)
# split the three channels b,g,r
b,g,r =  cv2.split(img)
img = cv2.merge((b,g,r))
#copy the image of ball
ball = img[280:340,330:390]
#paste the image of ball
img[273:333,100:160] = ball
# resize the img image
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
# to add two images
#det = cv2.add(img,img2)
# add weightage to the image
det= cv2.addWeighted(img2,.6,img,.4,0)

cv2.imshow("image",det)
cv2.waitKey(0)
cv2.destroyAllWindows()