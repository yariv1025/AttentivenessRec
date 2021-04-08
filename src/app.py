from src.FrameProvider import FrameProvider
from src.emotic_app import emotic
from src.FrameDisplay import FrameDisplay
from src.FrameSaver import FrameSaver
import threading
from src.emotic_loop import EmoticLoop


def app():
    # locks creation
    p_lock = threading.Lock()
    c_lock = threading.Lock()
    locks = [p_lock, c_lock]
    print('locks created')

    fp = FrameProvider(0)

    thread_display = FrameDisplay(1, fp)
    thread_saver = FrameSaver(2, fp, locks)
    emotic_loop = EmoticLoop(3, fp, locks)

    print(f"Lock P is locked: {locks[0].locked()}")
    print(f"Lock C is locked: {locks[1].locked()}")

    thread_display.start()
    thread_saver.start()
    emotic_loop.start()


app()
