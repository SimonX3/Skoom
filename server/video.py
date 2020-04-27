import cv2


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
