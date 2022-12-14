import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np
  
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.mode=0
 
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

       # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
   
        self.btn_highPass=tkinter.Button(window, text="High Pass", width=50, command=self.highPass)
        self.btn_highPass.pack(anchor=tkinter.CENTER, expand=True)
        self.btn_lowPass=tkinter.Button(window, text="Low Pass", width=50, command=self.lowPass)
        self.btn_lowPass.pack(anchor=tkinter.CENTER, expand=True)
        self.btn_sharp=tkinter.Button(window, text="Sharpning", width=50, command=self.sharp)
        self.btn_sharp.pack(anchor=tkinter.CENTER, expand=True)
        self.btn_ori=tkinter.Button(window, text="Original", width=50, command=self.original)
        self.btn_ori.pack(anchor=tkinter.CENTER, expand=True)
       # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def highPass(self):
        self.mode=1
    def lowPass(self):
        self.mode=2
    def sharp(self):
        self.mode=3
    def original(self):
        self.mode=0
    def update(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if (self.mode==1):
            k=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
            res=cv2.filter2D(src=frame,ddepth=-1,kernel=k)
        elif (self.mode==2):
            k=np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
            res=cv2.filter2D(src=frame,ddepth=-1,kernel=k)
        elif (self.mode==3):
            k=np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            res=cv2.filter2D(src=frame,ddepth=-1,kernel=k)
        else:
            res=frame

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(res))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)
class MyVideoCapture:
    def __init__(self, video_source=0):
         # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
         # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
     # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
 
 # Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")