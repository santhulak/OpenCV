import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# CAP_PROP_FRAME_WIDTH= 3
cap.set(3,1200)
#CAP_PROP_FRAME_HEIGHT=4
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
# to check whether file is correct
#cap = cv2.VideoCapture(5)
#print(cap.isOpened())
#while(cap.isOpened()):
while True:
    ret, frame = cap.read()
    if ret == True:
    #get frame  properties

        out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("window", gray)
        if cv2.waitKey(1) & 0XFF == ord('q'):
           break
    else:
        break
cap.release()