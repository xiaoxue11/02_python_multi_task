import time
import random
from threading import Thread, Event

items = []
event = Event()

class Producer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global item
        for _ in range(10):
            time.sleep(2)
            item = random.randint(0,256)
            self.items.append(item)
            print('Producer notify : item %d appended to list by %s' %(item, self.name))
            print('Producer notify : event set by %s' % self.name)
            self.event.set()
            print('Produce notify : event cleared by %s ' % self.name)
            self.event.clear()


class Cosumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print('Consumer notify : %d popped from list by %s' %(item, self.name))

def main():
    t1 = Producer(items, event)
    t2 = Cosumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
