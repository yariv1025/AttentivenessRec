# # attentive-gui
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import cv2
import PIL.Image, PIL.ImageTk
import time


class App:
    def __init__(self, window, window_title, video_stream=None, video_source=0):
        self.window = window
        self.window.title(window_title)

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
        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def update(self):
        # Get a frame from the video source
        frame = self.vid.get_frame()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if True:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def updateEmotionTextBox(self, newText):
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.insert(tk.END, newText)
        self.text.config(state=DISABLED)

    def createProgressBars(self, window):

        self.emotionPB = ProgressBar(window, 'emotions: ')
        self.valencePB = ProgressBar(window, 'valence: ')
        self.arousalPB = ProgressBar(window, 'arousal: ')
        self.dominancePB = ProgressBar(window, 'dominance: ')

        self.emotionPB.progress.grid(row=1, column=1, padx=5, pady=5)
        self.valencePB.progress.grid(row=2, column=1, padx=5, pady=5)
        self.arousalPB.progress.grid(row=3, column=1, padx=5, pady=5)
        self.dominancePB.progress.grid(row=4, column=1, padx=5, pady=5)

        emotionLabel = tk.Label(window, text='Emotion').grid(row=1, column=0, padx=5, pady=5)
        valenceLabel = tk.Label(window, text='Valence').grid(row=2, column=0, padx=5, pady=5)
        arousalLabel = tk.Label(window, text='Arousal').grid(row=3, column=0, padx=5, pady=5)
        dominanceLabel = tk.Label(window, text='Dominance').grid(row=4, column=0, padx=5, pady=5)

    def updateEmotion(self, value):
        self.emotionPB.progress['value'] = value
        self.window.update_idletasks()

    def updateValence(self, value):
        self.valencePB.progress['value'] = value
        self.window.update_idletasks()

    def updateArousal(self, value):
        self.arousalPB.progress['value'] = value
        self.window.update_idletasks()

    def updateDominance(self, value):
        self.dominancePB.progress['value'] = value
        self.window.update_idletasks()


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


class ProgressBar():
    def __init__(self, window, pb_name):
        self.window = window
        # Create a progressbar widget
        self.progress = Progressbar(window, orient=tk.HORIZONTAL,
                                    length=300, mode='determinate', maximum=10, value=0)

        # label = tk.Label(root, text='Emotion').grid(row=1, column=0, padx=5, pady=5)

        # And a label for it
        # label_1 = tk.Label(root, text=pb_name).pack()

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
