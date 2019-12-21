def set_func(func):
    print('decorate start')
    def call_func(*args, **kwargs):
        print('-----This is the authenticate 1-----')
        print('-----This is the authenticate 2-----')
        print(*args)
        print(*kwargs)
        print(args)
        print(kwargs)
        func(*args, **kwargs)
    return call_func

@set_func
def test(num, *args, **kwargs):
    print('----this is the test function {}----'.format(num))
    print('---test--', args)
    print('----test----', kwargs)

test(100)
print('='*50)
test(100,200,300)
print('='*50)
test(100,200,mm=100)
print('='*50)
