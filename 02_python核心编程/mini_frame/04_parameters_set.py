import sys

def main():
    with open('web_server.conf', 'r') as f:
        info = eval(f.read())
    print(info)
    print(type(info))
    file_name = 'mini_web'
    app_name = 'application'
    sys.path.append(info['dynamic_path'])
    frame = __import__(file_name)
    print(frame)
    app = getattr(frame, app_name)
    print(app)

    
if __name__ == '__main__':
    main()
