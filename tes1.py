import cv2 as cv
import numpy as np


def on_trackbar(val):
    return

bg=cv.imread('image.jpg')
vid = cv.VideoCapture(0)
cv.namedWindow('result')
cv.createTrackbar('g', 'result', 0, 255, on_trackbar)
#cv.createTrackbar('b', 'result', 0, 255, on_trackbar)

while(True):
    _, videoCam= vid.read()

    f_height,f_width,_=videoCam.shape
    bg = cv.resize(bg, (f_width,f_height), interpolation = cv.INTER_AREA)
    hsv = cv.cvtColor(videoCam, cv.COLOR_BGR2HSV)

    sensitivity=cv.getTrackbarPos('g','result')
   # b_sensitivity=cv.getTrackbarPos('b','result')
    
    low=(120 - sensitivity, 150, 0)  
    high= (180 + sensitivity, 255, 255)
    #low_blue = (105-b_sensitivity,100,50)
    #high_blue = (105+b_sensitivity,255,255)
    mask1= cv.inRange(hsv, low , high )
    #mask2= cv.inRange(hsv, low_blue , high_blue)
    mask1=cv.bitwise_not(mask1)
    #mask2=cv.bitwise_not(mask2)
    masked = cv.bitwise_and(videoCam, videoCam, mask = mask1)
   # masked = cv.bitwise_and(videoCam, videoCam, mask = mask2)
    res = np.where(masked == 0, bg, masked)

    mask1=mask1[:,:,np.newaxis]
   # mask2=mask2[:,:,np.newaxis]
   # mask_total=cv.bitwise_and(mask1, mask1, mask = mask2)
   # mask_total=mask_total[:,:,np.newaxis]
   # print(mask_total.shape)

    blank_image = np.zeros((f_height,f_width*2,3), np.uint8)


    ## isi masking
    

    blank_image[:,0:f_width] =res# ingat dalam BGR
    blank_image[:,f_width:f_width*2] = mask1
    
    cv.imshow('result',blank_image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

vid.release()
cv.destroyAllWindows()