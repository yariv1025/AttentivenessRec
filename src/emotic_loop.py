import threading
from random import randrange
import cv2
from src.emotic_app import emotic


class EmoticLoop(threading.Thread):

    def __init__(self, tid, fp, locks, gui):
        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks
        self.gui = gui

    def run(self):
        while self.fp.isOpened():
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break
            self.locks[1].acquire()
            results = emotic()
            self.gui.updateEmotionTextBox(results[0])
            self.gui.updateEmotion(randrange(11))
            self.gui.updateValence(results[1][0])
            self.gui.updateArousal(results[1][1])
            self.gui.updateDominance(results[1][2])
            self.locks[0].release()
