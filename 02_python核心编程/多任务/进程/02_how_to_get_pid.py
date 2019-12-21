import multiprocessing
import time
import os

def test1():
    print('This is the subprocess, the pid = {}'.format(os.getpid()))
    for i in range(5):
        print('-------subprocess: {}------------'.format(i))

def main():
    print('This is the parent process, the pid = {}'.format(os.getpid()))
    p = multiprocessing.Process(target=test1)
    p.start()
    # p.join()
    for i in range(5):
        print('------parent_process: {}------'.format(i))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
