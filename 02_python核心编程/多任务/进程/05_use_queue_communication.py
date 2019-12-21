import multiprocessing


def test1(q):
    nums = [11,22,33]
    for num in nums:
        q.put(num)
    print('write over')


def test2(q):
    while True:
        if q.empty():
            break
        print(q.get())

        

def main():
    # create a queue
    q = multiprocessing.Queue()
    # create a process to write data
    p1 = multiprocessing.Process(target=test1, args=(q,))
    # create a process to read data
    p2 = multiprocessing.Process(target=test2, args=(q,))
    # start process
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
