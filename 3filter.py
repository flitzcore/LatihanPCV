import cv2 
import numpy as np


def on_clicked(val):
    print ('1')

vid = cv2.VideoCapture(0)
cv2.namedWindow('result')
cv2.createButton	('sharpning',on_clicked)
while(True):
    _, videoCam= vid.read()    
    cv2.imshow('result',videoCam)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

vid.release()
cv2.destroyAllWindows()