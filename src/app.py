import threading
import src.gui
import tkinter as tk

from src.face_detector import FaceDetector
from src.frame_provider import FrameProvider
from src.frame_saver import FrameSaver
from src.statistics_data_loader import Statistics
from src.emotic_loop import EmoticLoop
from src.class_details import ClassDetails


def app():
    # TODO: fix closing of the threads.

    """
    The main function for the app.
    This function creates the locks for the multi-threading execution, starts the threads
    and creating the GUI window.

    Emotic parameters:
    TRAIN
    --mode train --data_path PROJECT_PATH/data/emotic_pre --experiment_path PROJECT_PATH/debug_exp

    TEST
    --mode test --data_path PROJECT_PATH/data/emotic_pre --experiment_path PROJECT_PATH/debug_exp

    RUN
    --mode inference --inference_file PROJECT_PATH\debug_exp\inference_file.txt --experiment_path PROJECT_PATH\debug_exp
    """

    # set parameters for attention calculator
    cont_weights = [0.3, 0.3, 0.4]
    ratio = 0.6
    alpha = 0.3
    weights = [cont_weights, ratio, alpha]

    # locks creation
    p_lock = threading.Lock()
    c_lock = threading.Lock()
    locks = [p_lock, c_lock]

    # creation of misc variables for the app
    fd = FaceDetector()
    fp = FrameProvider(0)
    statistics = Statistics(class_data, fd)
    window = tk.Tk()

    # Create a gui window and pass it to the Application object
    gui = src.gui.App(window, "AttentivnessRec", statistics, fp, weights)

    # create the 2 other threads of the app
    thread_saver = FrameSaver(2, fp, locks, fd, gui)
    emotic_loop = EmoticLoop(3, fp, locks, gui)

    # initializing of the threads
    thread_saver.start()
    emotic_loop.start()
    gui.start()


# calling the app
if __name__ == "__main__":
    class_data = ClassDetails(lecture_value=167, lecturer_value='Tamar')
    app()
