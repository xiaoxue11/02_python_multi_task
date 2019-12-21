import socket
import re
import gevent
from gevent import monkey


def serve_client(new_client_socket):
    # receive client request
    request = new_client_socket.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()
    # print(request_lines)
    # GET /index.html HTTP/1.1
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        print(file_name)
    # response the client request
    # get response header
    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    # get response body
    file_path = '../test' + file_name
    f = open(file_path, 'rb')
    file_contend = f.read()
    f.close()

    new_client_socket.send(response.encode('utf-8'))
    new_client_socket.send(file_contend)
    new_client_socket.close()


def main():
    # create tcp socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set port socket reuse
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind port
    tcp_server_socket.bind(('',7788))
    # set listen state
    tcp_server_socket.listen(128)
    while True:
        # accept client message
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)
        # create son Process to execute tasks
        # g1 = gevent.spawn(serve_client, new_client_socket)
        # g1.join()
        gevent.spawn(serve_client, new_client_socket)

    # close socket
    tcp_server_socket.close()


if __name__ == '__main__':
    monkey.patch_all()
    main()
