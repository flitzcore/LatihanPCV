import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np


init_red = 0
init_green = 0
init_blue = 0
vid = cv.VideoCapture(0)
while(True):
    _, videoCam= vid.read()
    f_height,f_width,_=videoCam.shape
    blank_image = np.zeros((f_height,f_width*2,3), np.uint8)
    blank_image[:,0:f_width] = videoCam     # (B, G, R)
    blank_image[:,f_width:f_width*2] = (0,255,0)
    
    cv.imshow('',blank_image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

vid.release()
cv.destroyAllWindows()