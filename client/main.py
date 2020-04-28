from network.udp_client import udp_client
from network.tcp_client import tcp_client
from ingestor import ingestor
from audio import sounds_iterator
from video import compess_video, capture_video


def main():
    tcp_client(compess_video(capture_video()))


def main2():
    udp_client(ingestor(compess_video(capture_video()), sounds_iterator()))


if __name__ == '__main__':
    main2()
