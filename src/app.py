from matplotlib import pyplot

from src.FrameProvider import FrameProvider
import cv2, time
from src.FaceDetector import FaceDetector


def hello_world():
    # # frame providing
    # fp = FrameProvider(0)
    #
    # while(True):
    #     frame = fp.get_frame()
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('frame', gray)
    #     time.sleep(1)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # # When everything done, release the capture
    # fp.release()
    # cv2.destroyAllWindows()

    # # face detecting
    # fd = FaceDetector()
    # img = pyplot.imread("../docs/ImagesForTests/3.jpg")
    # # detect faces in the image
    # faces = fd.has_face(img)
    #
    # print(faces)

    pass


if __name__ == '__main__':
    hello_world()
