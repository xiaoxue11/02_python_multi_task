import time
import threading


g_num = 0
# create lock to solve
mutex = threading.RLock()


def test1(num):
    global g_num
    mutex.acquire()
    mutex.acquire()
    for i in range(num):
        g_num += i
    mutex.release()
    mutex.release()
    print('This time use 2 times acquire, then g_num is {} in test1'.format(g_num))


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += i
    mutex.release()
    print('g_num is {} in test2'.format(g_num))


def main():
    #create threading 1
    t1 = threading.Thread(target=test1, args=(100000,))
    #create threading 2
    t2 = threading.Thread(target=test2, args=(100000,))
    #start threading
    t1.start()
    t2.start()
    time.sleep(1)
    #print result
    print('g_num is {} in main'.format(g_num))


if __name__ == '__main__':
    main()
