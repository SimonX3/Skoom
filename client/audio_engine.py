import sounddevice as sd
from queue import Queue
import time

 
def sound_iterator():
    sounds_queue = Queue()

    def callback(outdata, frames, time_, status):
        sounds_queue.put(outdata, time.time())

    with sd.InputStream(channels=1, callback=callback, samplerate=1000):
        while True:
            yield sounds_queue.get()
