import os
import time

import cv2
import threading

from mtcnn import mtcnn

import src.FrameProvider


class FrameSaver(threading.Thread):

    def __init__(self, tid, fp, locks):
        """
        Initializing frame saver.
        :param tid - thread id number
        :param fp - the FrameProvider object
        """
        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks
        self.locks[1].acquire()

    def run(self):
        """
        A loop for storing frames from video.
        """
        while self.fp.isOpened():
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break
            self.locks[0].acquire()
            try:
                frame = self.fp.get_frame()
                # TODO: Perform check - if frame directory dosent exist -> create
                path = 'D:\PyCharmProjects\AttentivenessRec\debug_exp\\frames'
                cv2.imwrite(os.path.join(path, 'frame.jpg'), frame)
            except (IOError):
                print("now exiting")
                exit(0)
            print("img saved")
            img_path = os.path.join(os.path.join(path, 'frame.jpg'))

            detector = mtcnn.MTCNN()
            faces = detector.detect_faces(frame)
            if len(faces) > 0:
                x1 = faces[0]['box'][0]
                y1 = faces[0]['box'][1]
                x2 = faces[0]['box'][0] + faces[0]['box'][2]
                y2 = faces[0]['box'][1] + faces[0]['box'][3]
                faces = [x1, y1, x2, y2]

                with open('D:\PyCharmProjects\AttentivenessRec\debug_exp\inference_file.txt', 'w') as f:
                    f.write(
                        img_path + ' ' + str(faces[0]) + ' ' + str(faces[1]) + ' ' + str(faces[2]) + ' ' + str(
                            faces[3]))

            self.locks[1].release()
            time.sleep(5)
