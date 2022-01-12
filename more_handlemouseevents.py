import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' is i]
#print (events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(img,(x,y), 3,(0,0,255),-1)
        #second click appends the first point
        points.append((x,y))
        #if we click once again it create a line and again click which connects previous line
        if len(points)>=2 :
            cv2.line(img, points[-1],points[-2],(255,0,0),5)
        cv2.imshow('image',img)


#create a black image using numpy
img = np.zeros((512,512,3), np.uint8)
#img =cv2.imread('lena.jpg')
# window name 'image' should be same
cv2.imshow('image',img)
points = []
# to call click_event method
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()