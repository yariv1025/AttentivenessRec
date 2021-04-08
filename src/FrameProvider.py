import os
import cv2
from mtcnn import mtcnn


class FrameProvider(cv2.VideoCapture):

    def __init__(self, param):
        """
        Constructor:
        :param param - Video stream source.
        :return Boolean - If stream successfully initialized.
        """
        super().__init__(param)
        if not self.isOpened():
            raise IOError("Could not open video stream.")

    def get_frame(self):
        """
        Get frame from a video stream, if stream is open.
        """
        if not self.isOpened():
            raise IOError("Could not open video stream.")
        res, frame = self.read()
        return frame
