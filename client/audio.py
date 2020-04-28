# sudo apt install python3-pyaudio
# sudo apt-get install portaudio19-dev
import pyaudio


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 40100
CHUNK = 1024
RECORD_SECONDS = 5


audio = pyaudio.PyAudio()


def sounds_iterator():
    audio_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while True:
        yield audio_stream.read(audio_stream.get_read_available())






