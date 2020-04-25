import cv2

from tcp_server import tcp_server
from udp_server import udp_server


def show_video(video_iterator):
    type_frame = 'frame'
    for frame in video_iterator:
        cv2.imshow(type_frame, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def decompess_video(video_iterator):
    for frame in video_iterator:
        de_frame = cv2.imdecode(frame[1], frame[0])
        yield de_frame


def main():
    show_video(decompess_video(tcp_server()))


def main2():
    show_video(decompess_video(udp_server()))


if __name__ == '__main__':
    main2()
