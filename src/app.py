import threading
import src.gui
import tkinter as tk
from src.FrameProvider import FrameProvider
from src.FrameSaver import FrameSaver
from src.statistics_data_loader import Statistics
from src.emotic_loop import EmoticLoop


def app():
    # TODO: fix closing of the threads.

    """
    The main function for the app.
    This function creates the locks for the multi-threading execution, starts the threads
    and creating the GUI window.
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
    fp = FrameProvider(0)
    statistics = Statistics()
    window = tk.Tk()
    exit_flag = True

    # Create a gui window and pass it to the Application object
    gui = src.gui.App(window, "AttentivnessRec", statistics, exit_flag, fp, weights)

    # create the 2 other threads of the app
    thread_saver = FrameSaver(2, fp, locks, gui, exit_flag)
    emotic_loop = EmoticLoop(3, fp, locks, gui, exit_flag)

    # initializing of the threads
    thread_saver.start()
    emotic_loop.start()
    gui.start()


# calling the app
if __name__ == "__main__":
    app()
