from socket import socket, AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_REUSEADDR


def udp_server(host='localhost', port=5000):
    server_sock = socket(AF_INET, SOCK_DGRAM)
    server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_sock.bind((host, port))

    while True:
        msg, addr = server_sock.recvfrom(65000)
        print(msg)
        yield msg


def integrate_frame(msg):
    pass
