import os
import time
import cv2
import threading
from src.FaceDetector import FaceDetector


class FrameSaver(threading.Thread):
    """
    This class job is to get frames from the FrameProvider class and store them in the storage so that the ANN will be
    able to access it.
    """

    def __init__(self, tid, fp, locks, fd, gui):
        """
        Creating FrameSaver object.

        :param tid: thread id number
        :param fp: the FrameProvider object
        """

        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks
        self.locks[1].acquire()
        self.fd = fd
        self.gui = gui
        self.main_path = os.path.dirname(os.getcwd())
        self.frames_path = self.main_path + '\debug_exp\\frames'
        if not os.path.exists(self.frames_path):
            os.makedirs(self.frames_path)
            print("Directory frames has been created.")

    def saveFrame(self, frame, faces=None):
        """
        The main function for storing the images in the memory.

        :param frame: the image to be stored.
        :param faces: The location of the faces in the image.
        """

        img_path = os.path.join(os.path.join(self.frames_path, 'frame.jpg'))
        cv2.imwrite(os.path.join(self.frames_path, 'frame.jpg'), frame)

        if faces:
            x1 = faces[0]['box'][0]
            y1 = faces[0]['box'][1]
            x2 = faces[0]['box'][0] + faces[0]['box'][2]
            y2 = faces[0]['box'][1] + faces[0]['box'][3]
        else:
            x1, y1, x2, y2 = 0, 0, 1, 1

        faces = [x1, y1, x2, y2]

        with open(self.main_path + '\debug_exp\inference_file.txt', 'w') as f:
            f.write(
                img_path + ' ' + str(faces[0]) + ' ' + str(faces[1]) + ' ' + str(faces[2]) + ' ' + str(
                    faces[3]))

    def run(self):
        """
        A loop for storing frames from video.
        """
        self.saveFrame(self.fp.get_frame())

        while self.gui.exit_flag:
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     self.fp.release()
            #     break

            self.locks[0].acquire()
            try:
                frame = self.fp.get_frame()
                faces = self.fd.has_face(frame)

                if faces:
                    self.saveFrame(frame, faces)
                    self.gui.face = True
                    print("img saved")
                else:
                    self.gui.face = False
                    print("Face not detected!")

                self.locks[1].release()
                time.sleep(1)

            except Exception as e:
                if not self.gui.exit_flag:
                    print("now exiting")
                    return
                else:
                    raise e
