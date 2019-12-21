import time
import threading

g_num = 100

def test1():
    global g_num
    g_num +=1
    print('g_num is : {} in test1......'.format(g_num))


def test2():
    print('g_num is : {} in test2......'.format(g_num))


def main():
    # create threading: execute globle variable addition
    t1 = threading.Thread(target=test1)
    # create the other threading: execute read and print globle variable
    t2 = threading.Thread(target=test2)
    # execute threading
    t1.start()
    time.sleep(1)

    t2.start()
    print('g_num is : {} in main......'.format(g_num))

     
if __name__ == '__main__':
    main()
