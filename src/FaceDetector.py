from mtcnn.mtcnn import MTCNN


class FaceDetector(MTCNN):
    """
    Constructor:
    """

    def __init__(self):
        super().__init__()

    """"
    :return face image.
    :param img - an image from a static path. 
    """

    def get_face(self, img):
        return self.detect_faces(img)

    """"
    :return a frame Location.
    :param img - an image from a static path.
    """

    def has_face(self, img):
        return len(self.get_face(img)) > 0
