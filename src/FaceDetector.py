from mtcnn.mtcnn import MTCNN


class FaceDetector(MTCNN):
    """
    Constructor:
    """

    def __init__(self):
        super().__init__()

    """"
    :return face image
    """

    def get_face(self, img):
        return self.detect_faces(img)

    """"
    :return the Location of the frame.
    """

    def has_face(self, img):
        return len(self.get_face(img)) > 0
