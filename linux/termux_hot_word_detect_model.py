import sounddevice as sd # type: ignore
import queue
from vosk import Model, KaldiRecognizer # type: ignore
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

model = Model("model-small-en-us")
rec = KaldiRecognizer(model, 16000)

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening for wake word 'hello echo'...")
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if "hello" in result.get("text", "").lower():
                print("Wake word detected!")
                break
