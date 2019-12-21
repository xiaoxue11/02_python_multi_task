import socket

def main():
    #create tcp socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #create connect
    tcp_client_socket.connect(('192.168.0.6', 7890))
    #send downloading file
    file_name = input('Please input file name: ')
    tcp_client_socket.send(file_name.encode('utf-8'))
    #receive file content
    rec_data = tcp_client_socket.recv(1024).decode('utf-8')
    if rec_data:
        with open('new'+ file_name,'w',encoding='utf-8') as f:
            f.write(rec_data)
    #close socket
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
