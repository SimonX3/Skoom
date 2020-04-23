import socket

HEADER = b'START'
HEADER_LENGTH = len(HEADER)
FOOTER = b'END'
FOOTER_LENGTH = len(FOOTER)


def tcp_server(host='localhost', port=5000):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen()

    while True:
        client_sock, addr = server_sock.accept()
        for _byte in iter(lambda: client_sock.recv(1), ''):
            if _byte is b'S':
                _bytes = client_sock.recv(FOOTER_LENGTH - 1)
                if _byte + _bytes == HEADER:
                    pass
