from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print('{} starts to execute, the process id is {}.'.format(msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print('{} is already finished, the total time is {:.2f}.'.format(msg, (t_stop-t_start)))


def main():
    # create a pool
    po = Pool(3)
    # use spare pool resource to execute process
    for i in range(10):
        po.apply_async(worker, (i,))
    # close pool
    print('-----start------')
    po.close()
    # wait all son process finish
    po.join()
    # print msg indicate that the task is finished
    print('-----end-----')


if __name__ == '__main__':
    main()