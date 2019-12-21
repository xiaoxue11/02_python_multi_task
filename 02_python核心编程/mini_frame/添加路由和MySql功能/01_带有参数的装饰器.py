def set_lever(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print('----This is level 1 authenticate----')
            elif level_num ==2:
                print('----This is level 2 authenticate----')
            return func(*args, **kwargs)
        return call_func
    return set_func

@set_lever(2)
def test():
    print('----This is test1----')


test()