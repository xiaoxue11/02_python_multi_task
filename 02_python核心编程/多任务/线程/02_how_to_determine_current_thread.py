import time
from time import ctime 
import threading


def sing():
    for i in range(3):
        print(threading.currentThread().getName()+' is starting.')
        print('I am singing.')
        time.sleep(i)
        print(threading.currentThread().getName()+' is existing.')


def dance():
    for i in range(3):
        print(threading.currentThread().getName()+' is starting.')
        print('I am dancing.')
        time.sleep(i)
        print(threading.currentThread().getName()+' is existing.')


def main():
    print('---开始---:%s'%ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print('---结束---:%s'%ctime())


if __name__ == "__main__":
    main()
