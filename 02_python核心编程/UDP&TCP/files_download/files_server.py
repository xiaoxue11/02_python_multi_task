import socket

def main():
    #create tcp socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind port
    tcp_server_socket.bind(('',7890))
    #set socket listen state
    tcp_server_socket.listen(128)
    #accept client request: obtain client socket and client address
    new_client_socket, client_addr = tcp_server_socket.accept()
    print(client_addr)
    #new client socket gets file name from client
    file_name = new_client_socket.recv(1024).decode('gbk')
    print(file_name)
    #judge whether the file exites and reads
    file_content = None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        print(file_content)
    except Exception :
        print('No such file in server')
    #send read information to client
    if file_content:
        new_client_socket.send(file_content)
    #close socket
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
