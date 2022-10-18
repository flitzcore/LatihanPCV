import cv2
import numpy as np

frame=np.array([[0,0,0,0,0,0,0],[0,0,2,2,0,0,0],[0,3,1,1,3,0,0],[0,3,1,1,3,0,0],[0,3,1,2,3,0,0],[0,0,3,4,0,0,0],[0,0,0,0,0,0,0]])
frame=np.float32(frame)
#k=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])                1a
#k=np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])   1b
#k=np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])            1c
kx=np.array([[-1,-2,-1], [0,0,0], [1,2,1]])         
ky=np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
gx=cv2.filter2D(src=frame,ddepth=-1,kernel=kx)
gy=cv2.filter2D(src=frame,ddepth=-1,kernel=ky)

gx=np.abs(gx)
gy=np.abs(gy)

g=gx+gy
print(g)