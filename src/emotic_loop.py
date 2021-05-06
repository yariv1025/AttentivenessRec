import threading
from datetime import datetime

import cv2
import matplotlib.pyplot as plt
from src.emotic_app import emotic
from src.statistics_data_loader import Statistics


class EmoticLoop(threading.Thread):

    def __init__(self, tid, fp, locks, gui):
        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks
        self.gui = gui

    def run(self):
        indexes = []
        values = []
        index = 0

        statistics = Statistics()
        start_time = datetime.now()

        while self.fp.isOpened():
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break

            self.locks[1].acquire()
            results = emotic()
            seconds = (datetime.now() - start_time).total_seconds()

            self.gui.updateEmotionTextBox(results[0])
            value = self.gui.emotionBarCalc(results[0])
            statistics.addValue(int(seconds), value)

            self.gui.updateEmotion(value)
            self.gui.updateValence(results[1][0])
            self.gui.updateArousal(results[1][1])
            self.gui.updateDominance(results[1][2])
            self.locks[0].release()

        plt.plot(indexes, values)
        plt.show()
