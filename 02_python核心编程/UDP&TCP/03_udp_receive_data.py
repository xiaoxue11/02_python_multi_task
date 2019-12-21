import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ('', 7788)
    udp_socket.bind(localaddr)
    while True:
        rec_data = udp_socket.recvfrom(1024)
        rec_msg = rec_data[0].decode('gbk')
        if rec_msg == 'exit':
            break
        addr_msg = rec_data[1]
        print('{}:{}'.format(str(addr_msg),rec_msg))
    udp_socket.close()

if __name__ == "__main__":
    main()
