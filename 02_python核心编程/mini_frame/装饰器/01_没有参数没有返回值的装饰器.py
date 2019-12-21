def set_func(func):
    def call_func():
        print('-----This is the authenticate 1-----')
        print('-----This is the authenticate 2-----')
        func()
    return call_func

def test():
    print('----this is the test function----')

set_func(test)()