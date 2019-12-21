def index():
    return 'This is the first page.'

def register():
    return 'This is the register page.'

def application(env, start_response):
    start_response('200 OK',[('content-type','text/html;charset=UTF-8')])
    return 'hello,world. This is the mini web test program.'