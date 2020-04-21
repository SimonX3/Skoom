import cv2


def capture_video(video_input=0):
    cap = cv2.VideoCapture(video_input)

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret is True:

            yield frame

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def show_video(video_iterator):
    for frame in video_iterator:
        cv2.imshow('frame', frame)


def write_video(video_iterator, file_path='output.avi'):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))
    for frame in video_iterator:
        out.write(frame)
        yield frame
    out.release()


if __name__ == '__main__':
    show_video(write_video(capture_video()))
