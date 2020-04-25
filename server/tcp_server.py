import re
import pickle
from socket import socket, AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR


HEADER = b'START'
READING_SIZE = 1024


def parsing(chunk: bytes, tail: bytes):
    chunk = tail + chunk
    frames = [i for i in re.split(HEADER, chunk) if i != b'']
    return frames[:-1], frames[-1]


def tcp_server(host='localhost', port=5000):
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen()

    while True:
        client_sock, addr = server_sock.accept()
        tail = b''
        for chunk in iter(lambda: client_sock.recv(READING_SIZE), ''):
            data_frames, tail = parsing(chunk, tail)
            for data_frame in data_frames:
                yield pickle.loads(data_frame)
