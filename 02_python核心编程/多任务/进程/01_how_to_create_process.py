import time
import multiprocessing

def test1():
    while True:
        print('This is test1---------1')
        time.sleep(2)


def test2():
    while True:
        print('This is test2---------2')
        time.sleep(2)

 
def main():
    # create process
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    # start process
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
 