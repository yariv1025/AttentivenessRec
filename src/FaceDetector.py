from mtcnn.mtcnn import MTCNN


class FaceDetector(MTCNN):
    """
    Perform facial detection.
    """
    def __init__(self):
        """
        Creating FaceDetector object by calling to the super class constructor (MTCNN).
        """
        super().__init__()

    def get_face(self, img):
        """
        Detects faces in an image.
        If faces has been detected, returning the bounding boxes for the faces relative to the specified image.
        Else, return an empty list.

        :param img: image/frame to process.
        :return: list containing all the bounding boxes detected with their key-points.
        """
        return self.detect_faces(img)

    def has_face(self, img):
        """
        Face verification within an image.

        :param img: image/frame to process.
        :return: boolean value - False if theres no face. Else, True.
        """
        faces = self.get_face(img)
        return False if len(faces) == 0 else faces
