from video import decompess_video, show_video
from network.tcp_server import tcp_server
from network.udp_server import udp_server


def main():
    show_video(decompess_video(tcp_server()))


def main2():
    show_video(decompess_video(udp_server()))


if __name__ == '__main__':
    main2()
