import cv2
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import PIL.Image, PIL.ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.attention_calculator import AttentionCalc


class App:
    """"
    Create our GUI app.
    """

    def __init__(self, window, window_title, statistics, video_stream, weights):
        """"
        Creating the GUI for the app.

        :param window: tk.Tk() object.
        :param window_title: String - our GUI title.
        :param statistics: a Statistics object.
        :param video_stream: frameProvider object.
        """

        # Initialize the attention weights
        self.attention_calc = AttentionCalc(weights[0], weights[1], weights[2])

        # Initialize exit flag
        self.exit_flag = True

        # Initialize face detection flag
        self.face = False

        # Root configuration
        self.window = window
        self.window.title(window_title)
        self.window.configure(bg='white')
        self.window.resizable(width=False, height=False)

        # Extract video source size
        self.vid = video_stream
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Face detection label
        self.label_text = tk.StringVar()
        self.label_text.set('')
        self.face_detection_label = tk.Label(self.window, textvariable=self.label_text, bg='white').grid(row=1,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         padx=5,
                                                                                                         pady=5)
        # Create progress bars, progress text, labels and text box for create_progress_bars() function
        self.attention_bar = None
        self.valence_bar = None
        self.arousal_bar = None
        self.dominance_bar = None

        self.attention_text = tk.StringVar()
        self.valence_text = tk.StringVar()
        self.arousal_text = tk.StringVar()
        self.dominance_text = tk.StringVar()

        self.attention_label = None
        self.valence_label = None
        self.arousal_label = None
        self.dominance_label = None

        self.text = tk.Text(window, height=5, width=45)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1
        self.photo = None
        self.update()

        # create progress bars
        self.create_progress_bars(window)

        # Create graph
        self.statistics = statistics
        self.add_charts()
        self.figure = None
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start(self):
        """"
        Start our GUI loop (Thread).
        """
        self.window.mainloop()

    def on_closing(self):
        """
        quit from program
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.exit_flag = False
            self.figure.savefig("../public/img/graph.png", bbox_inches='tight')
            self.statistics.save_to_pdf()
            self.window.destroy()
            exit(0)

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
        try:
            frame = self.vid.get_frame()
        except Exception as e:
            if self.exit_flag:
                raise e
            else:
                return

        if self.face:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.label_text.set('')
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = 'Face not detected!'
            self.label_text.set(text)

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(self.delay, self.update)

    def update_emotion_textbox(self, newText):
        """"
        With every iteration, we update our emotions in our text box.
        :param: newText - our new text for update.
        """
        if not self.exit_flag:
            return
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.insert(tk.END, newText)
        self.text.config(state=DISABLED)

    def create_progress_bars(self, window):
        """"
        Configure the progress bars and all labels.
        :param: window - tk.TK() object
        """
        self.attention_bar = Progressbar(window, orient=tk.HORIZONTAL,
                                         length=300, mode='determinate', maximum=10, value=0)
        self.valence_bar = Progressbar(window, orient=tk.HORIZONTAL,
                                       length=300, mode='determinate', maximum=10, value=0)
        self.arousal_bar = Progressbar(window, orient=tk.HORIZONTAL,
                                       length=300, mode='determinate', maximum=10, value=0)
        self.dominance_bar = Progressbar(window, orient=tk.HORIZONTAL,
                                         length=300, mode='determinate', maximum=10, value=0)

        self.attention_bar.grid(row=2, column=1, padx=5, pady=5)
        self.valence_bar.grid(row=3, column=1, padx=5, pady=5)
        self.arousal_bar.grid(row=4, column=1, padx=5, pady=5)
        self.dominance_bar.grid(row=5, column=1, padx=5, pady=5)

        self.attention_text.set('Attention (%0)')
        self.valence_text.set('Valence (%0)')
        self.arousal_text.set('Arousal (%0)')
        self.dominance_text.set('Dominance (%0)')

        self.attention_label = tk.Label(window, textvariable=self.attention_text, bg='white').grid(row=2, column=0,
                                                                                                   padx=5, pady=5)
        self.valence_label = tk.Label(window, textvariable=self.valence_text, bg='white').grid(row=3, column=0, padx=5,
                                                                                               pady=5)
        self.arousal_label = tk.Label(window, textvariable=self.arousal_text, bg='white').grid(row=4, column=0, padx=5,
                                                                                               pady=5)
        self.dominance_label = tk.Label(window, textvariable=self.dominance_text, bg='white').grid(row=5, column=0,
                                                                                                   padx=5, pady=5)

        self.text.insert(tk.END, "")
        self.text.grid(row=2, column=2, rowspan=4, padx=5, pady=5)
        self.text.config(state=DISABLED)

    def add_charts(self):
        """
        Adding attention levels chart to our gui.
        """
        if not self.exit_flag:
            return

        self.figure = plt.Figure(figsize=(4, 4), dpi=100)

        chart_type = FigureCanvasTkAgg(self.figure, self.window)
        chart_type.get_tk_widget().grid(row=0, column=2, rowspan=4, padx=5, pady=5)

        ax = self.figure.add_subplot(111)
        ax.set_title('Attention tracking')
        ax.set_ylim([0, 10])

        data_frame = self.statistics.get_data_frame()
        data_frame.plot(kind='line', legend=True, ax=ax)

    def update_attention(self, value):
        """"
        Update Attention bar value.
        :param: value - number.
        """
        self.attention_bar['value'] = value
        self.attention_text.set('Attention (%{:.2f})'.format(value * 10))
        self.window.update_idletasks()

    def update_valence(self, value):
        """"
        Update Valence bar value.
        :param: value - number.
        """
        self.valence_bar['value'] = value
        self.valence_text.set('Valence (%{:.0f})'.format(value * 10))
        self.window.update_idletasks()

    def update_arousal(self, value):
        """"
        Update Arousal bar value.
        :param: value - number.
        """
        self.arousal_bar['value'] = value
        self.arousal_text.set('Arousal (%{:.0f})'.format(value * 10))
        self.window.update_idletasks()

    def update_dominance(self, value):
        """"
        Update Dominance bar value.
        :param: value - number.
        """
        self.dominance_bar['value'] = value
        self.dominance_text.set('Dominance (%{:.0f})'.format(value * 10))
        self.window.update_idletasks()

    def attention_bar_calc(self, results):
        """
        Calculate the Attention level of the subject
        :param results: the results from the ANN model
        :return: the attention level
        """
        return self.attention_calc.attention_calc(results)
