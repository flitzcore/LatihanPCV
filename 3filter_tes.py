import tkinter as tk
import cv2
from tkinter import CENTER, LEFT, Canvas, ttk
from PIL import ImageTk,Image 
# root window
root = tk.Tk()
root.geometry('800x600')
root.title('Button Demo')

# item
canvas = Canvas(root)      
 
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
first_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
second_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
canvas.pack() 
exit_button.pack(
    ipadx=0,
    ipady=0,
    expand=False
    
)
first_button.pack(
    ipadx=0,
    ipady=0,
    expand=False
)
second_button.pack(
    ipadx=0,
    ipady=0, 
    expand=False
)
#video

cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
      canvas.create_image(20, 20, image=frame) 
    else:
        break
cap.release()
cv2.destroyAllWindows()

root.mainloop()