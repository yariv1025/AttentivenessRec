import threading
import cv2
from datetime import datetime
from src.emotic_app import emotic


class EmoticLoop(threading.Thread):
    """
    The class of the emotic emotion recognition thread.
    """

    def __init__(self, tid, fp, locks, gui):
        """
        Creating of the emotic thread object.

        :param tid: the thread id
        :param fp: a FrameProvider object
        :param locks: main app's locks
        :param gui: GUI thread object
        :param exit_flag: an exit flag for the app
        """

        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks
        self.gui = gui

    def run(self):
        """
        The run method of the thread.
        Performing emotion recognition evaluation after a new frame has been provided by the FrameProvider thread.
        After the evaluation, this thread is updating the GUI thread on the results.
        """

        # initializing timer
        start_time = datetime.now()

        # start of the run loop
        while self.gui.exit_flag:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break
            try:
                self.locks[1].acquire()
                if self.gui.face:
                    results = emotic()
                    seconds = (datetime.now() - start_time).total_seconds()

                    self.gui.update_emotion_textbox(results[0])
                    value = self.gui.attention_bar_calc(results)
                    self.gui.statistics.save_emotion(results[0])

                    # update attentive tracking chart
                    self.gui.statistics.add_value(int(seconds), value)
                    self.gui.add_charts()

                    # update GUI features
                    self.gui.update_attention(value)
                    self.gui.update_valence(results[1][0])
                    self.gui.update_arousal(results[1][1])
                    self.gui.update_dominance(results[1][2])

                self.locks[0].release()
            except Exception as e:
                if not self.gui.exit_flag:
                    return
                else:
                    raise e
