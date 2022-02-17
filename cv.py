import cv2
import numpy as np
#img=cv2.imread('Lenna.png',-1)
#img=np.zeros([512,512,3],np.uint8)
#cv2.imshow('image',img)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    #img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

#img=cv2.line(img,(0,0),(400,400  ),(0,255,0),10)
#img=cv2.arrowedLine(img,(0,0),(400,400),(0,255,0),10)
#img=cv2.rectangle(cap,(0,0),(400,400  ),(0,255,0),10)
#cv2.circle(img,(45,80),65,(0,255,0),10)
#font=cv2.FONT_ITALIC
#cv2.putText(img,'movemoment',(10,30),font,4,(0,234,0),10,cv2.LINE_AA)
#cv2.imshow('image',img)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()