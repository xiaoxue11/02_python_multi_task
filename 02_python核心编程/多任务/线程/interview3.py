from threading import Thread, Condition

condition = Condition()
current = 'A'

class ClassA(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != 'A':
                    condition.wait()
                print('A')
                current = 'B'
                condition.notify_all()   


class ClassB(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != 'B':
                    condition.wait()
                print('B')
                current = 'C'
                condition.notify_all()


class ClassC(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != 'C':
                    condition.wait()
                print('C')
                current = 'A'
                condition.notify_all()


def main():
    t1 = ClassA()
    t2 = ClassB()
    t3 = ClassC()
    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    main()
