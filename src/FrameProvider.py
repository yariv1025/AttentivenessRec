class FrameProvider:
    """
    :param stream - .
    """

    def __init__(self, stream):
         pass

    """
    imports video stream.
    :param videoStream - get a stream of video.
    """

    def setStream(self, videoStream):
        pass

    """
    :param videoStream - video stream.
    """

    def cropFrame(self, videoStream):
        pass

    """
    :return - returns a single frame.
    :param videoStream - video stream.
    """

    def getFrame(self, videoStream):
        return self.cropFrame(videoStream)




