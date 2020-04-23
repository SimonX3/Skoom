import cv2


def capture_video(video_input=0):
    cap = cv2.VideoCapture(video_input)
    feedback = None
    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret is True and not feedback:
            feedback = yield frame
            cv2.waitKey(1)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    yield None


def show_video(video_iterator):
    window_name = 'frame'
    window_is_open = False
    for frame in video_iterator:
        if window_is_open and (cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE)) != 1.0:
            cv2.destroyWindow(window_name)
            video_iterator.send('stop')
        else:
            cv2.imshow(window_name, frame)
            window_is_open = True



def write_video(video_iterator, file_path='output.avi'):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))
    for frame in video_iterator:
        if frame is not None:
            out.write(frame)
            feedback = yield frame
            video_iterator.send(feedback)

    out.release()
    yield None


if __name__ == '__main__':
    show_video(write_video(capture_video()))
