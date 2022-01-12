import numpy as np
import cv2
img= np.zeros([512,512,3],np.uint8)
#img = cv2.imread("lena.jpg",-1)

#draw a line above image
img=cv2.line(img,(0,0),(255,255),(255,100,50),5)
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),5)
img = cv2.rectangle(img,(310,20),(510,120),(0,0,255),-1)
img=cv2.circle(img,(250,250),63,(0,255,0),-1)
font = cv2.FONT_HERSHEY_COMPLEX
img =cv2.putText(img, "Welcome",(10,300),font,4,(0,255,255),10,cv2.LINE_AA)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
