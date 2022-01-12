import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0);
cv2.namedWindow("Tracking")
cv2.createTrackbar("LowerHue", "Tracking" , 0 , 255 , nothing)
cv2.createTrackbar("Lowersat","Tracking", 0 , 255 ,nothing)
cv2.createTrackbar("Lowervalue", "Tracking", 0 , 255 , nothing)
cv2.createTrackbar("upperHue","Tracking", 255 , 255 , nothing)
cv2.createTrackbar("upperrsat", "Tracking", 255 , 255 , nothing)
cv2.createTrackbar("uppervalue", "Tracking", 255, 255, nothing)
while True:
    #frame = cv2.imread("smarties.png")
    #open video
    _,frame = cap.read()
    #convert image from BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Get trackbar position
    l_h = cv2.getTrackbarPos("LowerHue", "Tracking")
    l_s = cv2.getTrackbarPos("Lowersat", "Tracking")
    l_v = cv2.getTrackbarPos("Lowervalue","Tracking")

    u_h = cv2.getTrackbarPos("upperHue", "Tracking")
    u_s = cv2.getTrackbarPos("upperrsat", "Tracking")
    u_v = cv2.getTrackbarPos("uppervalue", "Tracking")

    # find the lower blue color value
    l_b = np.array((l_h,l_s,l_v))
    u_b = np.array((u_h,u_s,u_v))
    #image threshold
    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2. bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("reuslt", res)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
