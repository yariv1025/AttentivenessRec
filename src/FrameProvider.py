import cv2


class FrameProvider(cv2.VideoCapture):
    """
    The FrameProvider class role is to provide frames from a video stream so that the app will be able
    to send the frames to the ANN models.
    """

    def __init__(self, param):
        """
        Creating a FrameProvider object.

        :param param: Video stream source.
        :return Boolean: If stream successfully initialized.
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
