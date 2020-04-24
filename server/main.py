import cv2

from tcp_server import tcp_server


def show_video(video_iterator):
    type_frame = 'frame'
    for frame in video_iterator:
        cv2.imshow(type_frame, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main():
    show_video(tcp_server())


if __name__ == '__main__':
    main()
