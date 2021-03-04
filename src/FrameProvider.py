import cv2


class FrameProvider(cv2.VideoCapture):

    def __init__(self, param):
        super().__init__(param)
        if not self.isOpened():
            raise IOError("Could not open video stream.")

    def get_frame(self):
        if not self.isOpened():
            raise IOError("Could not open video stream.")
        res, frame = self.read()
        return frame
