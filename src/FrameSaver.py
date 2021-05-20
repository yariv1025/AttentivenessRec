import os
import time
import cv2
import threading
from src.FaceDetector import FaceDetector


class FrameSaver(threading.Thread):

    def __init__(self, tid, fp, locks, gui, exit_flag):
        """
        Initializing frame saver.
        :param tid - thread id number
        :param fp - the FrameProvider object
        """
        self.exit_flag = exit_flag

        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks
        self.locks[1].acquire()
        self.fd = FaceDetector()
        self.gui = gui

    def saveFrame(self, frame, faces=None):
        path = 'D:\GitProjects\AttentivenessRec\debug_exp\\frames'
        img_path = os.path.join(os.path.join(path, 'frame.jpg'))
        cv2.imwrite(os.path.join(path, 'frame.jpg'), frame)

        if faces:
            x1 = faces[0]['box'][0]
            y1 = faces[0]['box'][1]
            x2 = faces[0]['box'][0] + faces[0]['box'][2]
            y2 = faces[0]['box'][1] + faces[0]['box'][3]
        else:
            x1, y1, x2, y2 = 0, 0, 1, 1

        faces = [x1, y1, x2, y2]

        with open('D:\GitProjects\AttentivenessRec\debug_exp\inference_file.txt', 'w') as f:
            f.write(
                img_path + ' ' + str(faces[0]) + ' ' + str(faces[1]) + ' ' + str(faces[2]) + ' ' + str(
                    faces[3]))

    def run(self):
        """
        A loop for storing frames from video.
        """
        self.saveFrame(self.fp.get_frame())

        while self.exit_flag:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break

            self.locks[0].acquire()
            try:
                frame = self.fp.get_frame()
                faces = self.fd.has_face(frame)

                if faces:
                    # TODO: Perform check - if frame directory dosent exist -> create
                    self.saveFrame(frame, faces)
                    self.gui.face = True
                    print("img saved")
                else:
                    self.gui.face = False
                    print("Face not detected!")

            except IOError:
                print("now exiting")
                exit(0)

            self.locks[1].release()
            time.sleep(1)
