from video_engine import capture_video, compess_video
from tcp_client import tcp_client


def main():
    tcp_client(compess_video(capture_video()))


if __name__ == '__main__':
    main()
