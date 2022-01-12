import cv2
import numpy as np
def nothing(x):
    pass

#cv2.namedWindow("Tracking")
while True:
    frame = cv2.imread("smarties.png")
    #convert image from BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # find the lower blue color value
    l_b = np.array((110,50,50))
    u_b = np.array((130,255,255))
    #image threshold
    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2. bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("reuslt", res)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
