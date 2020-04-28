from network.udp_client import udp_client
from network.tcp_client import tcp_client
from ingestor import ingestor
from video import compess_video, capture_video


def main():
    tcp_client(compess_video(capture_video()))


def main2():
    udp_client(ingestor())


if __name__ == '__main__':
    main2()
