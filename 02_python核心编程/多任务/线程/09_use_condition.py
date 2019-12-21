from threading import Thread, Condition
import time

items = []
condition = Condition()

class Consumer(Thread):

    def __init__(self):
        Thread.__init__(self)
    
    def consumer(self):
        global items
        global condition
        condition.acquire()
        # with condition:
        if len(items)==0:
            condition.wait()
            print('Consumer Notify: no item to consume')
        item = items.pop()
        print('Consumer Notify: consumed %s item'%item)
        print('Consume Notify: items to be consumed are ' + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for _ in range(10):
            time.sleep(1)
            self.consumer()


class Producer(Thread):

    def __init__(self):
        Thread.__init__(self)
    
    def producer(self):
        global items
        global condition
        condition.acquire()
        # with condition:
        if len(items)==3:
            condition.wait()
            print("Producer notify : items producted are " + str(len(items)))
            print("Producer notify : stop the production!!")
        items.append(1)
        print("Producer notify : total items producted " + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for _ in range(5):
            time.sleep(1)
            self.producer()

def main():
    t1 = Producer()
    t2 = Consumer()
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
