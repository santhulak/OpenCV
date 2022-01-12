import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# CAP_PROP_FRAME_WIDTH= 3
#cap.set(3,1200)
#CAP_PROP_FRAME_HEIGHT=4
#cap.set(4,720)
#print(cap.get(3))
#print(cap.get(4))

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
       font = cv2.FONT_HERSHEY_SIMPLEX
       text = 'Width:  ' + str(cap.get(3)) + 'Height:  ' + str(cap.get(4))
    # show date and time
       datet = str(datetime.datetime.now())
       frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        #out.write(frame)
       cv2.imshow("window", frame)
       if cv2.waitKey(1) & 0XFF == ord('q'):
           break
    else:
        break
cap.release()