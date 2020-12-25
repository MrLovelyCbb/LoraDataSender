"""
multiprocessing 多进程
"""

import threading
import time


def func(str):
    while True:
        print("this is process 2--%s" % (str))
        time.sleep(1.5)


if __name__ == '__main__':
    t = threading.Thread(target=func, args=("123",))
    t.start()
    # t.join()