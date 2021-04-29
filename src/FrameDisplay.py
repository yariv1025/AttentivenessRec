import cv2
import threading

# TODO: delete this class?
class FrameDisplay(threading.Thread):

    def __init__(self, tid, fp):
        """
        Initializing frame display.
        :param tid - thread id number
        :param fp - the FrameProvider object
        """
        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp

    def run(self):
        """
        A method that shows that camera input.
        """
        while self.fp.isOpened():
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break
            try:
                frame = self.fp.get_frame()
                cv2.imshow('frame', frame)
            except (IOError):
                print("now exiting")
                exit(0)
