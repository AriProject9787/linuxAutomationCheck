import pvporcupine
import pyaudio
import struct

# 🔑 Get your free Access Key from https://console.picovoice.ai/
ACCESS_KEY = "dyeFdiGOnaCVLV4C4cD6JZhRW3vzageCGtODwRn9/s4Tcns6vKEtXw=="  # Replace with your key

# Initialize Porcupine
porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keywords=["terminator"]  # You can change to "bumblebee", "porcupine",ngrapefruit, smart mirror, hey barista, bumblebee, picovoice, hey siri, computer, snowboy, porcupine, terminator, blueberry, hey google, grasshopper, ok google, jarvis, view glass, alexa, pico clock, americano or your custom wake word
)
#keywords=smart mirror
# Setup PyAudio stream
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("🎤 Listening for wake word...")

try:
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm_unpacked)

        if keyword_index >= 0:
            print("Wake word detected!")
            print("Hello Echo, I am awake!")

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    audio_stream.close()
    pa.terminate()
    porcupine.delete()
