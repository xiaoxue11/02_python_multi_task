import os
import time
from multiprocessing import Manager, Pool

def writer(q):
    print('writer start: ({}), the paraent process is: {}'.format(os.getpid(),os.getppid()))
    for i in [11,22,33]:
        q.put(i)

def reader(q):
    print('reader start: ({}), the paraent process is: {}'.format(os.getpid(), os.getppid()))
    while True:
        if q.empty():
            break
        print(q.get())

def main():
    # create pool and queue
    pool = Pool(3)
    q = Manager().Queue()
    # create son process to write data 
    pool.apply_async(writer, args=(q,))
    time.sleep(1)
    # create son process to read data
    pool.apply_async(reader, args=(q,))
    pool.close()
    pool.join()
    print('({}) End'.format(os.getpid()))


if __name__ == '__main__':
    main()
