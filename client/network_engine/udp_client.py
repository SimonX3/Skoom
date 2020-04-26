import sys
import pickle
from socket import socket, AF_INET, SOCK_DGRAM
import numpy as np


def udp_client(data_iterator, host='localhost', port=5000):
    client = socket(AF_INET, SOCK_DGRAM)
    for df_num, data_frame in enumerate(data_iterator):
        for dumped_chunk in get_dumped_chanks(df_num, data_frame):
            client.sendto(dumped_chunk, (host, port))


def get_dumped_chanks(df_num, data_frame):
    first_bool_arg = data_frame[0]
    second_np_arg = data_frame[1]
    chanks_num = second_np_arg.shape[0] // 63000 + 1
    slices = np.array_split(second_np_arg, chanks_num)
    for num_slice, np_slice in enumerate(slices):
        yield pickle.dumps({'df_num': df_num, 'chunk':(first_bool_arg, np_slice),
                      'slice_num': num_slice, 'total_slices': len(slices)})

