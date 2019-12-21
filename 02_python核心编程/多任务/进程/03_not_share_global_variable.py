import multiprocessing
import time
import os

nums = [11,22]

def worker1():
    print('Subprocess 1, pid: {}'.format(os.getpid()))
    nums.append(33)
    print(nums)

def worker2():
    print('Subprocess 2, pd: {}'.format(os.getpid()))
    print(nums)

def main():
    # create a subprocess to change global varibale
    p1 = multiprocessing.Process(target=worker1)
    # create the other subprocess to read global variable
    p2 = multiprocessing.Process(target=worker2)
    # start 
    p1.start()
    time.sleep(1)
    p2.start()
    # wait subprocess end
    p1.join()
    p2.join()
    print('Parent process, pid= {}'.format(os.getpid()))
    print(nums)

if __name__ == '__main__':
    main()