import threading
import time

def sing():
    for i in range(3):
        print('I am singing.')
        time.sleep(i)

def dance():
    for i in range(3):
        print('I am dancing.')
        time.sleep(i)

class MyThread(threading.Thread):
    
    def run(self):
        for i in range(3):
            time.sleep(1)
            print('I am '+self.name+'@'+str(i))

def main():
    for i in range(5):
        t = MyThread()
        t.start()
        time.sleep(i)

if __name__ == '__main__':
    main()
