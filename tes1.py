import cv2 as cv
import numpy as np
import tkinter as tk
from tk import *
sensitivity =30
low_green=(60 - sensitivity, 100, 50)  
high_green= (60 + sensitivity, 255, 255)
init_red = 0
init_green = 0
init_blue = 0

root=tk.Tk()
w = tk.Scale(root, from_=0, to=42)
w.pack()
vid = cv.VideoCapture(0)
while(True):
    _, videoCam= vid.read()

    f_height,f_width,_=videoCam.shape
    hsv = cv.cvtColor(videoCam, cv.COLOR_BGR2HSV)

    mask1= cv.inRange(hsv, low_green , high_green )

    mask1=cv.bitwise_not(mask1)
    res = cv.bitwise_and(videoCam, videoCam, mask = mask1)
    
    mask1=mask1[:,:,np.newaxis]
    

    blank_image = np.zeros((f_height,f_width*2,3), np.uint8)


    ## isi masking
    

    blank_image[:,0:f_width] =res # ingat dalam BGR
    blank_image[:,f_width:f_width*2] = mask1
    
    cv.imshow('',blank_image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

vid.release()
cv.destroyAllWindows()