# # locking the producer
# locks[0].acquire()
# print('producer locks')
#
# # locking our lock (consumer)
# locks[1].acquire()
# print('consumer locks')
#
# # release the locks
# locks[0].release()
# locks[1].release()
# print('release locks')

import threading

import cv2

from src.emotic_app import emotic

class EmoticLoop(threading.Thread):

    def __init__(self, tid, fp, locks):
        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks

    def run(self):
        while self.fp.isOpened():
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break
            print(f"EL::Lock P is locked: {self.locks[0].locked()}")
            print(f"EL::Lock C is locked: {self.locks[1].locked()}")
            self.locks[1].acquire()
            print('consumer locks')

            print(emotic())

            self.locks[0].release()
            print(f"EL::Lock P is locked: {self.locks[0].locked()}")
            print(f"EL::Lock C is locked: {self.locks[1].locked()}")
            print('release producer\n')

