import pickle
from socket import socket, AF_INET, SOCK_DGRAM


def udp_client(data_iterator, host='localhost', port=5000):
    client = socket(AF_INET, SOCK_DGRAM)
    for data in data_iterator:
            client.sendto(pickle.dumps(data), (host, port))


