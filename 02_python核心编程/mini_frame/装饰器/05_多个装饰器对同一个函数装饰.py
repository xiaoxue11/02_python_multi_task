def set_pri1(func):
    print('decorate111 start')
    def call_func(*args, **kwargs):
        print('-----This is the authenticate 1-----')
        return func(*args, **kwargs)
    return call_func

def set_pri2(func):
    print('decorate222 start')
    def call_func(*args, **kwargs):
        print('-----This is the authenticate 2-----')
        return func(*args, **kwargs)
    return call_func

@set_pri1
@set_pri2
def test():
    print('-----test-----')

test()
