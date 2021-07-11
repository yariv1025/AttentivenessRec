import unittest
import os
import threading
from datetime import datetime
import pandas
import cv2
import numpy

from src.class_details import ClassDetails
from src.frame_saver import FrameSaver
from src.statistics_data_loader import Statistics
from src.face_detector import FaceDetector
from src.frame_provider import FrameProvider


class FrameProviderTestCase(unittest.TestCase):
    fp = FrameProvider(0)

    def test_get_frame(self):
        frame = self.fp.get_frame()
        expected_type = type(numpy.ndarray([]))

        self.assertEqual(expected_type, type(frame))


class FaceDetectorTestCase(unittest.TestCase):
    fd = FaceDetector()

    main_path = os.path.dirname(os.getcwd())
    img_with_face = cv2.imread(main_path + "\public\\test_img\with_face.png")
    img_without_face = cv2.imread(main_path + "\public\\test_img\without_face.png")

    def test_get_face(self):
        result = self.fd.get_face(self.img_with_face)
        expected = True

        self.assertEqual(expected, len(result) > 0)

    def test_get_no_face(self):
        result = self.fd.get_face(self.img_without_face)
        expected = 0

        self.assertEqual(expected, len(result))

    def test_has_face(self):
        result = self.fd.has_face(self.img_with_face)
        expected = True
        self.assertEqual(expected, len(result) > 0)

    def test_has_no_face(self):
        result = self.fd.has_face(self.img_without_face)
        expected = False
        self.assertEqual(expected, result)

    def test_start_timer(self):
        result = self.fd.start_timer()
        expected = type(datetime.now())
        self.assertEqual(expected, type(result))

    def test_stop_timer(self):
        result = self.fd.stop_timer()
        expected = None

        self.assertEqual(expected, result)


class StatisticsTestCase(unittest.TestCase):
    class_data = ClassDetails(lecture_value=1, lecturer_value='Tamar Shrot')
    fd = FaceDetector()
    stat = Statistics(class_data, fd)

    def test_add_value(self):
        val = self.stat.values.copy()
        time = self.stat.times.copy()
        self.stat.add_value(datetime.now(), 10)

        expected_time = len(time) + 1
        expected_val = len(val) + 1

        time_result = len(self.stat.times)
        val_result = len(self.stat.values)

        self.assertEqual(expected_time, time_result)
        self.assertEqual(expected_val, val_result)

    def test_save_emotion(self):
        emotion_counter = self.stat.emotion_counter.copy()
        self.stat.save_emotion(['Affection'])

        expected = emotion_counter['Affection'] + 1
        result = self.stat.emotion_counter['Affection']

        self.assertEqual(expected, result)

    def test_get_top_3(self):
        emotions1 = ['Affection', 'Disconnection', 'Annoyance', 'Fatigue', 'Aversion']
        emotions2 = ['Affection', 'Disconnection', 'Annoyance', 'Doubt/Confusion']
        emotions3 = ['Disconnection', 'Excitement', 'Affection', 'Fear', 'Happiness', ]
        self.stat.save_emotion(emotions1)
        self.stat.save_emotion(emotions2)
        self.stat.save_emotion(emotions3)

        expected = sorted(['Disconnection', 'Affection', 'Annoyance'])
        result = sorted(self.stat.get_top_3())

        self.assertEquals(expected, result)

    def test_get_data_frame(self):
        expected = pandas.DataFrame()
        result = self.stat.get_data_frame()

        self.assertEqual(type(expected), type(result))


class FrameSaverTestCase(unittest.TestCase):
    # locks creation
    p_lock = threading.Lock()
    c_lock = threading.Lock()
    locks = [p_lock, c_lock]

    main_path = os.path.dirname(os.getcwd())
    img_path = main_path + "\debug_exp\\frames\\frame.jpg"
    img = cv2.imread(main_path + "\public\\test_img\\frame.png")

    fs = FrameSaver(2, None, locks, None, None)

    def test_save_frame(self):

        try:
            os.remove(self.img_path)
        except FileNotFoundError:
            pass

        self.fs.save_frame(self.img)
        result = os.path.isfile(self.img_path)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
