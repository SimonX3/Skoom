import cv2


def show_video(frame):
    type_frame = 'frame'
    cv2.imshow(type_frame, frame)


def decompess_video(frame):
    de_frame = cv2.imdecode(frame[1], frame[0])
    return de_frame
