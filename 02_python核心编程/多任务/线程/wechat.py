import socket
import threading


def rec_msg(socket):
    while True:
        rec_data = socket.recvfrom(1024)
        print(rec_data)


def send_msg(socket):
    while True:
        send_data = input('please input send data: ')
        socket.sendto(send_data.encode('utf-8'), ('192.168.0.6', 8080))


def main():
    # create udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind port 
    udp_socket.bind(('', 7788))
    # receive data
    t_rec=threading.Thread(target = rec_msg, args = (udp_socket,))
    # send data
    t_send=threading.Thread(target = send_msg, args = (udp_socket,))
    #execute threading
    t_rec.start()
    t_send.start()
    # close socket
    #udp_socket.close()


if __name__ == '__main__':
    main()
