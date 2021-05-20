from mtcnn.mtcnn import MTCNN


class FaceDetector(MTCNN):

    def __init__(self):
        """
        Initialize - calling to super class.
        """
        super().__init__()

    def get_face(self, img):
        """
        Detects bounding boxes from the specified image.
        :param img: image to process.
        :return: list containing all the bounding boxes detected with their keypoints.
        """
        return self.detect_faces(img)

    def has_face(self, img):
        """
        face verification in the image.
        :param img: image to process.
        :return: boolean
        """
        faces = self.get_face(img)
        return False if len(faces) == 0 else faces
