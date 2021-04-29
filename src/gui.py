# # attentive-gui
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import cv2
import PIL.Image, PIL.ImageTk
import time


class App:
    """"
    Create our GUI app.
    """
    def __init__(self, window, window_title, video_stream=None, video_source=0):
        """"
        :param: window - tk.Tk() object.
        :param: window_title - String - our GUI title.
        :param: video_stream - frameProvider object.
        :param: video_source - zero by default to import video stream from our computer camera.
        """
        self.window = window
        self.window.title(window_title)

        # TODO: Change this logic - use only with video_stream.
        if not video_stream:
            self.video_source = video_source
            # open video source (by default this will try to open the computer webcam)
            self.vid = MyVideoCapture(self.video_source)
        else:
            self.vid = video_stream
            self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.text = tk.Text(window, height=5, width=80)
        self.text.insert(tk.END, "")
        self.text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.text.config(state=DISABLED)

        # # Button that lets the user take a snapshot
        # self.btn_snapshot = tk.Button(window, text="Snapshot", width=50, command=self.snapshot)
        # self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)
        # self.btn_snapshot.grid(row=1, column=2, rowspan=3, padx=5, pady=5)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1
        self.update()

        # create progress bars
        self.createProgressBars(window)

    def start(self):
        """"
        Create our GUI loop (Thread).
        """
        self.window.mainloop()

    def snapshot(self):
        """"
        # Get a frame from the video source
        """
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def update(self):
        """"
        Update our video streaming.
        """

        # Get a frame from the video source
        frame = self.vid.get_frame()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if True:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def updateEmotionTextBox(self, newText):
        """"
        With every iteration, we update our emotions in our text box.
        :param: newText - our new text for update.
        """
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.insert(tk.END, newText)
        self.text.config(state=DISABLED)

    def createProgressBars(self, window):
        """"
        Creating the progress bars and all labels.
        :param: window - tk.TK() object
        """
        self.emotionPB = Progressbar(window, orient=tk.HORIZONTAL,
                                     length=300, mode='determinate', maximum=10, value=0)
        self.valencePB = Progressbar(window, orient=tk.HORIZONTAL,
                                     length=300, mode='determinate', maximum=10, value=0)
        self.arousalPB = Progressbar(window, orient=tk.HORIZONTAL,
                                     length=300, mode='determinate', maximum=10, value=0)
        self.dominancePB = Progressbar(window, orient=tk.HORIZONTAL,
                                       length=300, mode='determinate', maximum=10, value=0)

        self.emotionPB.grid(row=1, column=1, padx=5, pady=5)
        self.valencePB.grid(row=2, column=1, padx=5, pady=5)
        self.arousalPB.grid(row=3, column=1, padx=5, pady=5)
        self.dominancePB.grid(row=4, column=1, padx=5, pady=5)

        emotionLabel = tk.Label(window, text='Emotion').grid(row=1, column=0, padx=5, pady=5)
        valenceLabel = tk.Label(window, text='Valence').grid(row=2, column=0, padx=5, pady=5)
        arousalLabel = tk.Label(window, text='Arousal').grid(row=3, column=0, padx=5, pady=5)
        dominanceLabel = tk.Label(window, text='Dominance').grid(row=4, column=0, padx=5, pady=5)

    def updateEmotion(self, value):
        """"
        Update Emotion bar value.
        :param: value - number.
        """
        self.emotionPB['value'] = value
        self.window.update_idletasks()

    def updateValence(self, value):
        """"
        Update Valence bar value.
        :param: value - number.
        """
        self.valencePB['value'] = value
        self.window.update_idletasks()

    def updateArousal(self, value):
        """"
        Update Arousal bar value.
        :param: value - number.
        """
        self.arousalPB['value'] = value
        self.window.update_idletasks()

    def updateDominance(self, value):
        """"
        Update Dominance bar value.
        :param: value - number.
        """
        self.dominancePB['value'] = value
        self.window.update_idletasks()


class MyVideoCapture:
    """"
    Used for import video stream from our computer camera.
    """
    def __init__(self, video_source=0):
        """"
        Constructor - create 'vid' variable = video stream.
        :param: video_source - Zero by default to import video stream from our computer camera.
        """
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        """"
        By calling this method we close the video streaming.
        """
        if self.vid.isOpened():
            self.vid.release()

    # def bar(self, root):
    #     import time
    #     self.progress['value'] = 20
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     self.progress['value'] = 40
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     self.progress['value'] = 50
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     self.progress['value'] = 60
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     self.progress['value'] = 80
    #     root.update_idletasks()
    #     time.sleep(1)
    #     self.progress['value'] = 100
    #     root.update_idletasks()
    #     time.sleep(1)
    #     self.progress['value'] = 80
