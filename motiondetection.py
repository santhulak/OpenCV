import cv2
import numpy as np
cap= cv2.VideoCapture('vtest.avi')
#reading as two frames
ret,frame1 =cap.read()
ret,frame2 =cap.read()

while cap.isOpened():
    # finding absolute difference between two frames
    diff = cv2.absdiff(frame1,frame2)
    # convert to gray scale - because to find contours
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    #Blur the gray image
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #find threshold- first parameter is none so we have given _
    _,thresh =  cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #dilate
    dilated = cv2.dilate(thresh,None, iterations= 3)
    #finding contour, second is hierachy which we dont need now
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # iterating the corordinates
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        #if the area is less than 700 no rectangle will be drawn
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Status: {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
     #draw contours
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)

    cv2.imshow("feed",frame1)
    frame1 = frame2
    ret,frame2 = cap.read()


    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()