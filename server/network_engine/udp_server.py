from socket import socket, AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_REUSEADDR
import numpy as np
import pickle


def udp_server(host='localhost', port=5000):
    server_sock = socket(AF_INET, SOCK_DGRAM)
    server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    frame_courutine = integrate_frame()
    frame_courutine.send(None)

    while True:
        msg_slice, addr = server_sock.recvfrom(65000)
        frame = frame_courutine.send(msg_slice)
        if frame is not None:
            yield frame


def integrate_frame():
    current_frame = None
    current_df_num = None
    current_chunk_num = 0
    frame_is_done = False

    while True:
        msg_slice = yield current_frame if frame_is_done else None
        if frame_is_done:
            frame_is_done = False
            current_frame = None
        msg_slice = pickle.loads(msg_slice)
        chunk_df_num = msg_slice['df_num']
        chunk_frame = msg_slice['chunk']
        chunk_num = msg_slice['slice_num']
        total_slices = msg_slice['total_slices']
        if chunk_num == 0:
            current_frame = chunk_frame
            current_df_num = chunk_df_num
            current_chunk_num = 0
            if total_slices == 1:
                frame_is_done = True
                current_chunk_num = 0
        else:
            if current_df_num == chunk_df_num:
                if current_chunk_num + 1 == chunk_num and current_frame is not None:
                    stacked_slices = np.vstack((current_frame[1], chunk_frame[1]))
                    current_frame = (current_frame[0], stacked_slices)
                    if chunk_num + 1 < total_slices:
                        current_chunk_num += 1
                    else:
                        current_chunk_num = 0
                        frame_is_done = True
