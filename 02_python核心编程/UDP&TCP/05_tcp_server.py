import socket

def main():
    #create socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind port
    tcp_server_socket.bind(('',7890))
    #set socket state as listen
    tcp_server_socket.listen(128)
    #wait client information
    new_client_socket, client_addr = tcp_server_socket.accept()
    print(client_addr)
    #server receive data from client
    rec_data = new_client_socket.recv(1024)
    print(rec_data.decode('gbk'))
    #server receiver data and response, reply
    new_client_socket.send('Thank you for your cooperation.'.encode('utf-8'))
    #close socket  
    new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
