import socket
import re


def serve_client(client_sockets):
    for client_socket in client_sockets:
        try:
            # receive client request
            request = client_socket.recv(1024).decode('utf-8')
            # print(request)
        except:
            pass
            # print('Not get request message')
        else:
            # if request:
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
            file_path = './test' + file_name
            f = open(file_path, 'rb')
            file_contend = f.read()
            f.close()

            client_socket.send(response.encode('utf-8'))
            client_socket.send(file_contend)
            client_socket.close()


def main():
    # create tcp socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind port
    tcp_server_socket.bind(('',7788))
    # set listen state
    tcp_server_socket.listen(128)
    # set tcp server blocking state
    tcp_server_socket.setblocking(False)
    # define a list to store client socket
    client_sockets = []
    # accept client message
    while True:
        try:
            new_client_socket, client_addr = tcp_server_socket.accept()
            print(client_addr)
        except:
            pass
            # print('No client comes')
        else:
            print('A new client comes')
            new_client_socket.setblocking(False)
            client_sockets.append(new_client_socket)
        # serve client request and response
        serve_client(client_sockets)
    # close socket
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
