import socket
def main():
     udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     send_data = input('Please input content')
     udp_s.sendto(send_data.encode('utf-8'), ("192.168.0.6", 8080))
     udp_s.close()

if __name__ == '__main__':
    main()