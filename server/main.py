from server.video import decompess_video, show_video, cv2
from server.audio import play_audio
from server.network.tcp_server import tcp_server
from server.network.udp_server import udp_server
from server.brokers import main_datagram_broker



def main():
    show_video(decompess_video(tcp_server()))




def main2():
    for data_type, data in main_datagram_broker(udp_server()):
        if data_type == 'video':
            show_video(frame=decompess_video(frame=data))
        elif data_type == 'audio':
            play_audio(data)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main2()
