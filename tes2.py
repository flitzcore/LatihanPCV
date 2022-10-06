import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk()
win.title('Background Changer')
win.geometry("800x640")
win.bind('<Escape>', lambda e: win.quit())
lmain = tk.Label(win)
lmain.pack()
#ui = tk.Tk()
#ui.title('Select Background')
#ui.geometry("200x150")

cap = cv.VideoCapture()
cap.open(0)

bg = cv.imread('bg.jpeg')
bg2 = cv.imread('bg2.jpg')
bg3 = cv.imread('bg3.png')
bgre = cv.resize(bg, (640, 480))
bgre2 = cv.resize(bg2, (640, 480))
bgre3 = cv.resize(bg3, (640, 480))


def show():
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([105,50,50])
    upper_blue = np.array([135,255,255])

    mask = cv.inRange(hsv, lower_blue, upper_blue)
    res = cv.bitwise_and(frame,frame, mask= mask)

    res2 = frame + res

    img = Image.fromarray(res2)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show)

def show2():
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([105, 50, 50])
    upper_blue = np.array([135, 255, 255])

    mask = cv.inRange(hsv, lower_blue, upper_blue)
    res = cv.bitwise_and(frame, frame, mask=mask)

    res3 = frame - res

    img = Image.fromarray(res3)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show2)

A = tk.Button(win, text ="Anime 1", command = show)
A.place(x=5,y=5)
A.pack()
B = tk.Button(win, text ="Yae Miko", command = show2)
B.place(x=10,y=10)
B.pack()
#C = Button(win, text ="Sharpen", command = sharp)
#C.pack()
#D = Button(win, text ="Normal", command = normal)
#D.pack()
#win.mainloop()

#ui.mainloop()
win.mainloop()