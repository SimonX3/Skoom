import cv2
from server.udp_server import udp_server
from server.tcp_server import tcp_server
from server.brokers import main_datagram_broker
import pyaudio


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 40100
CHUNK = 4000
RECORD_SECONDS = 5


def show_video(frame):
    type_frame = 'frame'
    cv2.imshow(type_frame, frame)


def decompess_video(frame):
    de_frame = cv2.imdecode(frame[1], frame[0])
    return de_frame




def main():
    show_video(decompess_video(tcp_server()))

audio = pyaudio.PyAudio()
audio_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)


def play_sound(data):
    audio_stream.write(data['sound'])


def main2():
    for data_type, data in main_datagram_broker(udp_server()):
        if data_type == 'video':
            show_video(frame=decompess_video(frame=data))
        elif data_type == 'audio':
            play_sound(data)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main2()