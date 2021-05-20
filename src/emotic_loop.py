import threading
from datetime import datetime
import cv2
from src.emotic_app import emotic


class EmoticLoop(threading.Thread):

    def __init__(self, tid, fp, locks, gui, exit_flag):
        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks
        self.gui = gui
        self.exit_flag = exit_flag

    def run(self):
        start_time = datetime.now()

        while self.exit_flag:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break

            self.locks[1].acquire()
            results = emotic()
            seconds = (datetime.now() - start_time).total_seconds()

            self.gui.updateEmotionTextBox(results[0])
            value = self.gui.emotionBarCalc(results[0])
            self.gui.statistics.addValue(int(seconds), value)
            self.gui.addCharts()

            self.gui.updateEmotion(value)
            self.gui.updateValence(results[1][0])
            self.gui.updateArousal(results[1][1])
            self.gui.updateDominance(results[1][2])

            self.locks[0].release()
