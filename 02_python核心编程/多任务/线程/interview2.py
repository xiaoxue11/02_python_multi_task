# 开3个线程按照顺序打印ABC 10次,按照如下的方法无法完成任务
# 因为线程执行时随机的，无法通过控制线程调度程序，需要用到特殊的方法
# 尝试用锁完成,无法实现，进程时随机的
import threading

lock = threading.RLock()

def ClassA():
    for _ in range(10):
        lock.acquire()
        print('A')
        lock.release()


def ClassB():
    for _ in range(10):
        lock.acquire()
        print('B')
        lock.release()


def ClassC():
    for _ in range(10):
        lock.acquire()
        print('C')
        lock.release()


def main():
    t1 = threading.Thread(target=ClassA)
    t2 = threading.Thread(target=ClassB)
    t3 = threading.Thread(target=ClassC)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()
