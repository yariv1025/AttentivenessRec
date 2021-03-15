import cv2


class FrameProvider(cv2.VideoCapture):
    """
    Constructor:
    :param param - Video stream source.
    :return Boolean - If stream successfully initialized.
    """

    def __init__(self, param):
        super().__init__(param)
        if not self.isOpened():
            raise IOError("Could not open video stream.")

    def get_frame(self):
        """
         Get frame from a video stream, if stream is open.
        :return: frame
        """

        if not self.isOpened():
            raise IOError("Could not open video stream.")
        res, frame = self.read()
        return frame
