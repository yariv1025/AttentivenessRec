from datetime import datetime
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
        self.no_face_time = 0
        self.temp_timer = None
        self.prev = True

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

        if len(faces) > 0 and self.prev:
            return faces
        elif len(faces) > 0 and not self.prev:
            self.prev = True
            self.stop_timer()
            return faces
        elif len(faces) == 0 and self.prev:
            self.prev = False
            self.start_timer()
            return False
        elif len(faces) == 0 and not self.prev:
            return False

    def start_timer(self):
        """
        Initializes the timer to count when no faces are detected in the image.
        """
        self.temp_timer = datetime.now()
        return self.temp_timer

    def stop_timer(self):
        """
        Calculate the entire time theres no faces are detected in the image.
        """
        self.no_face_time = self.no_face_time + (datetime.now() - self.temp_timer).total_seconds()
        self.temp_timer = None
        return self.temp_timer