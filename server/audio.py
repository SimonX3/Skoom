import pyaudio


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 40100
CHUNK = 1024
RECORD_SECONDS = 5

audio = pyaudio.PyAudio()
audio_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

def play_audio(audio_data):
    audio_stream.write(audio_data['sound'])