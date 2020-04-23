from client.video_engine import capture_video
from client.tcp_client import tcp_client


if __name__ == '__main__':
    tcp_client(capture_video())
