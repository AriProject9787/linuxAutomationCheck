import pvporcupine
import pyaudio
import struct
import gtts
import subprocess
from datetime import datetime
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
LOG_FILE = "update_tool_log.txt"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def printf(c, msg):
        try:
            a1 = gtts.gTTS(msg)
            a1.save("tts1.mp3")
            print(c + msg)
            subprocess.run("mpv tts1.mp3", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except ModuleNotFoundError:
            print(bcolors.FAIL+ "ModuleNotFoundError")
        except Exception as e:
            print(bcolors.FAIL+ str(e))

ACCESS_KEY = "dyeFdiGOnaCVLV4C4cD6JZhRW3vzageCGtODwRn9/s4Tcns6vKEtXw=="  # From Picovoice Console

# Load custom wake word model
porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keyword_paths=["killer.ppn"]  # Path to your custom model
)

# Setup audio input
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("🎤 Listening for 'ok killer'...")

try:
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm_unpacked)

        if keyword_index >= 0:
            printf(bcolors.BLUE,". Wake word detected! killer is active.")
            printf(bcolors.CYAN ,"\n. Launching Main Program Tool...")
            log("Wake word detected redirect to main menu.")
            subprocess.run(["python3", "main.py"])

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    audio_stream.close()
    pa.terminate()
    porcupine.delete()
