from src.FrameProvider import FrameProvider
from src.emotic_app import emotic
from src.FrameDisplay import FrameDisplay
from src.FrameSaver import FrameSaver


def app():
    fp = FrameProvider(0)

    thread_display = FrameDisplay(1, fp)
    thread_saver = FrameSaver(2, fp)

    thread_display.start()
    # print(emotic())


app()
