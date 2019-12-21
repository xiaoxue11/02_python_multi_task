import time
import greenlet


def task_1():
    while True:
        print('----1----')
        gr2.switch()
        time.sleep(0.5)


def task_2():
    while True:
        print('----2----')
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet.greenlet(task_1)
gr2 = greenlet.greenlet(task_2)
gr1.switch()
