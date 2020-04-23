import pickle
from socket import socket, AF_INET, SOCK_STREAM

HEADER = b'START'
FOOTER = b'END'


def tcp_client(data_iterator, host='localhost', port=5000):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host, port))
    for data_frame in data_iterator:
        client.send(encapsulate_frame(data_frame))


def encapsulate_frame(data_frame):
    return HEADER + pickle.dumps(data_frame) + FOOTER
