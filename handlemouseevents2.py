import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' is i]
#print (events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorimage=np.zeros((512,512,3),np.uint8)
        #fill color for screen
        mycolorimage[:] =[blue,green,red]
        cv2.imshow('color',mycolorimage)


#create a black image using numpy
#img = np.zeros((512,512,3), np.uint8)
img =cv2.imread('lena.jpg')
# window name 'image' should be same
cv2.imshow('image',img)
points = []
# to call click_event method
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()