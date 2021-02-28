class FaceDetector:
    """
    :param frame - frame from the stream.
    :param model - the model used to cut the frame.
    """

    def __init__(self, frame, model):
        self.frame = frame
        self.model = model

    """
    returns the location of identified face.
    :param frame - identified frame.
    """

    def findFace(self, frame):
        pass

    """
    crop only the identified face.
    @param face_location - gets the face position in the frame.
    """

    def cropFace(self, face_location):
        pass

    """
    :return - returns a face object.
    :param face_location - ets the face position in the frame.
    """

    def getFace(self, face_location):
        return self.cropFace(face_location)

    """
    :return - returns the “informal” (readable) string representation of the object.
    """

    def str(self):
        return 'class {}'.format("FaceDetector")

    """
    :return
    """

    def __repr__(self):
        pass
