import socket

def main():
    #create tcp client socket
    tcpclient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #create connection
    server_ip = '192.168.0.6'
    server_port = 7788
    tcpclient_socket.connect((server_ip, server_port))
    #data transmition
    send_data = input('please input data:').encode('utf-8')
    tcpclient_socket.send(send_data)
    #close socket
    tcpclient_socket.close()

if __name__ == "__main__":
    main()