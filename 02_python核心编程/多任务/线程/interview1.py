# 开3个线程按照顺序打印ABC 10次,按照如下的方法无法完成任务
# 因为线程执行时随机的，无法通过控制线程调度程序，需要用到特殊的方法
import threading


def ClassA():
    for _ in range(10):
        print('A')

def ClassB():
    for _ in range(10):
        print('B')

def ClassC():
    for _ in range(10):
        print('C')

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
