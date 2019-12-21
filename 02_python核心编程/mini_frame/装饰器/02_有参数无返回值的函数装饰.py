def set_func(func):
    def call_func(a):
        print('-----This is the authenticate 1-----')
        print('-----This is the authenticate 2-----')
        func(a)
    return call_func

@set_func
def test(num):
    print('----this is the test function {}----'.format(num))

test(100)
test(200)