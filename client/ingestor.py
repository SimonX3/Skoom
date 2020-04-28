from video_engine import capture_video, compess_video
from audio_engine import sounds_iterator
import numpy as np
from random import randint

def ingestor():
    for (frame, audio) in zip(compess_video(capture_video()), sounds_iterator()):
        yield get_sounds(audio)
        df_num = randint(0, 10000000)
        for chunk in get_video_chanks(df_num, data_frame=frame):
            yield chunk


def get_video_chanks(df_num, data_frame):
    first_bool_arg = data_frame[0]
    second_np_arg = data_frame[1]
    chanks_num = second_np_arg.shape[0] // 6300 + 1
    slices = np.array_split(second_np_arg, chanks_num)
    for num_slice, np_slice in enumerate(slices):
        yield {'datagram_type': 'video', 'df_num': df_num, 'chunk':(first_bool_arg, np_slice),
                      'slice_num': num_slice, 'total_slices': len(slices)}


def get_sounds(sound_data):
    return {'datagram_type': 'audio', 'sound': sound_data}