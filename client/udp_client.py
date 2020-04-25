import sys
import pickle
from socket import socket, AF_INET, SOCK_DGRAM


def udp_client(data_iterator, host='localhost', port=5000):
    client = socket(AF_INET, SOCK_DGRAM)
    for data_frame in data_iterator:
        ser_frame = pickle.dumps(data_frame)
        for chunk in cut_up(ser_frame):
            client.sendto(chunk, (host, port))


def cut_up(data_frame: bytes):
    while len(data_frame) > 0:
        chunk = data_frame[:65000]
        data_frame = data_frame[:65000]
        yield chunk

