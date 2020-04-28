from video import decompess_video, show_video
from network.tcp_server import tcp_server
from network.udp_server import udp_server


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
