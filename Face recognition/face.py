import cv2
import sys


faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path=sys.argv[1]
cap=cv2.VideoCapture(path)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
out = cv2.VideoWriter('output', fourcc, 20.0, (640, 480)) 

while(cap.isOpened()):
  ret,frame=cap.read()
  gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces=faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

  
  cv2.imshow('Video',frame)
  out.write(gray)

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  

cap.release()
cv2.destroyAllWindows()


