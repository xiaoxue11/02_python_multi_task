import threading
import time
import random

# If the value given is less than 0, ValueError is raised.
semaphore = threading.Semaphore(0)

def Consumer():
    print('Consumer  is waiting.')
    semaphore.acquire()
    print('Consumer: consumed item number %s' % item)

def Producer():
    global item
    time.sleep(10)
    item = random.randint(0,1000)
    print('Producer: produced item number %s'%item)
    semaphore.release()

def main():
    for i in range(5):
        t1 = threading.Thread(target=Producer)
        t2 = threading.Thread(target=Consumer)
        t1.start()
        t2.start()
        time.sleep(i)
        t1.join()
        t2.join()
    print('program terminated.')


if __name__ == '__main__':
    main()
