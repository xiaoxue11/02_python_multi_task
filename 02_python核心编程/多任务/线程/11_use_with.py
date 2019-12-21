import logging
import threading
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

def threading_with(statement):
    with statement:
        logging.debug('%s acquired via with' % statement)


def threading_no_with(statement):
    statement.acquire()
    try:
        logging.debug('%s acquired directly' % statement )
    finally:
        statement.release()

def main():
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    semaphore = threading.Semaphore(1)
    threading_methods = [lock, rlock, condition, semaphore]
    for method in threading_methods:
        t1 = threading.Thread(target=threading_with, args=(method,))
        t2 = threading.Thread(target=threading_no_with, args=(method,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == '__main__':
    main()
