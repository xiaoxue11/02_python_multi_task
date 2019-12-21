def set_func(func):
    print('decorate start')
    def call_func(*args, **kwargs):
        print('-----This is the authenticate 1-----')
        print('-----This is the authenticate 2-----')
        return func(*args, **kwargs)
    return call_func

@set_func
def test(num, *args, **kwargs):
    print('----this is the test function {}----'.format(num))
    print('---test--', args)
    print('----test----', kwargs)
    return 'ok'

print(test(100))
print('='*50)
print(test(100,200,300))
print('='*50)
print(test(100,200,mm=100))
print('='*50)
