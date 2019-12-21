import socket


def serve_client(new_client_socket):
    # receive client request
    request = new_client_socket.recv(1024)
    print(request)
    # response the client request
    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    response += '<h1>hello, world!</h1>'
    print(response)
    new_client_socket.send(response.encode('utf-8'))
    new_client_socket.close()


def main():
    # create tcp socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind port
    tcp_server_socket.bind(('',7790))
    # set listen state
    tcp_server_socket.listen(128)
    # accept client message
    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)
    # serve client request and response
        serve_client(new_client_socket)
    # close socket
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
