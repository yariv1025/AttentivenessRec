# # attentive-gui
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import cv2
import PIL.Image, PIL.ImageTk
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import src.statistics_data_loader


class App:
    """"
    Create our GUI app.
    """

    def __init__(self, window, window_title, statistics, video_stream=None, video_source=0,):
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
        self.text.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
        self.text.config(state=DISABLED)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1
        self.update()

        # create progress bars
        self.createProgressBars(window)
        self.statistics = statistics
        self.addCharts()


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

        self.emotionText = tk.StringVar()
        self.emotionText.set('Emotion (%0)')

        self.valenceText = tk.StringVar()
        self.valenceText.set('Valence (%0)')

        self.arousalText = tk.StringVar()
        self.arousalText.set('Arousal (%0)')

        self.dominanceText = tk.StringVar()
        self.dominanceText.set('Dominance (%0)')

        self.emotionLabel = tk.Label(window, textvariable=self.emotionText).grid(row=1, column=0, padx=5, pady=5)
        self.valenceLabel = tk.Label(window, textvariable=self.valenceText).grid(row=2, column=0, padx=5, pady=5)
        self.arousalLabel = tk.Label(window, textvariable=self.arousalText).grid(row=3, column=0, padx=5, pady=5)
        self.dominanceLabel = tk.Label(window, textvariable=self.dominanceText).grid(row=4, column=0, padx=5, pady=5)

    def addCharts(self):
        """
        Adding chart to our gui.
        :param: window - tk.Tk() object.
        """
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        ax = figure.add_subplot(111)

        chart_type = FigureCanvasTkAgg(figure, self.window)
        chart_type.get_tk_widget().grid(row=1, column=2, rowspan=4, padx=5, pady=5)

        data_frame = self.statistics.get_data_frame()
        data_frame.plot(kind='line', legend=True, ax=ax)
        ax.set_title('Emotion tracking')

    def updateEmotion(self, value):
        """"
        Update Emotion bar value.
        :param: value - number.
        """
        self.emotionPB['value'] = value
        self.emotionText.set('Emotion (%{})'.format(value * 10))
        self.window.update_idletasks()

    def updateValence(self, value):
        """"
        Update Valence bar value.
        :param: value - number.
        """
        self.valencePB['value'] = value
        self.valenceText.set('Valence (%{:.0f})'.format(value * 10))
        self.window.update_idletasks()

    def updateArousal(self, value):
        """"
        Update Arousal bar value.
        :param: value - number.
        """
        self.arousalPB['value'] = value
        self.arousalText.set('Arousal (%{:.0f})'.format(value * 10))
        self.window.update_idletasks()

    def updateDominance(self, value):
        """"
        Update Dominance bar value.
        :param: value - number.
        """
        self.dominancePB['value'] = value
        self.dominanceText.set('Dominance (%{:.0f})'.format(value * 10))
        self.window.update_idletasks()

    def emotionBarCalc(self, emotions):
        bar = 5

        for emotion in emotions:
            bar += self.emotionValue(emotion)

        return max(0, min(10, bar))

    def emotionValue(self, emotion):
        pos = ['Affection', 'Anticipation', 'Confidence', 'Engagement', 'Esteem', 'Excitement',
               'Happiness', 'Peace', 'Pleasure', 'Surprise', 'Sympathy']

        neg = ['Anger', 'Annoyance', 'Aversion', 'Disapproval', 'Disconnection', 'Disquietment',
               'Doubt/Confusion', 'Embarrassment', 'Fatigue', 'Fear', 'Pain', 'Sadness',
               'Sensitivity', 'Suffering', 'Yearning']

        if emotion in pos:
            return 1
        elif emotion in neg:
            return -1
        else:
            raise ValueError("Emotion not found!")


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
