import os
import platform
import subprocess
from datetime import datetime
import gtts
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
            a1.save("tts2.mp3")
            print(c + msg)
            subprocess.run("mpv tts2.mp3", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except ModuleNotFoundError:
            print(bcolors.FAIL+ "ModuleNotFoundError")
        except Exception as e:
            print(bcolors.FAIL+ str(e))

def detect_env():
    if "android" in platform.uname().release.lower():
        printf(bcolors.GREEN, ". Android Environment Detected. Running on  Termux.")
        log("Android environment detected. Running on Termux.")
        subprocess.run(["pkg", "install", "mpv", "-y"], check=True)
        return "termux"
    elif platform.system() == "Linux":
        printf(bcolors.GREEN, ". Linux Environment Detected. Running on Terminal.")
        subprocess.run(["sudo", "apt", "install", "mpv", "-y"], check=True)
        log("Linux environment detected. Running on Terminal.")
        return "linux"
    else:
        printf(bcolors.FAIL, ". Unsupported environment detected. Exiting.")
        log("Unsupported environment detected. Exiting.")
        return "unsupported"

def run_command(command, cwd):
    try:
        if command in ["sl", "htop", "nano"]:  # interactive programs
            subprocess.run(command, shell=True, cwd=cwd)
        else:
            printf(bcolors.GREEN ,f"running command {command}")
            result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
            if result.stdout:
                print("[OUTPUT]")
                print(result.stdout)
            if result.stderr:
                log_error(result.stderr)
    except Exception as e:
        log_error(str(e))


def log_error(error_message):
    """Log errors to error_log.txt with timestamp."""
    log_file = "error_log.txt"
    with open(log_file, "a") as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {error_message}")
    print(f"[!] Error logged to {log_file}")

if __name__ == "__main__":
    env = detect_env()
    current_dir = os.getcwd()  # Start in current directory

    if env != "unsupported":
        while True:
            cmd = input(f"\n[{current_dir}]$ ").strip()
            
            if cmd.lower() == "exit":
                printf(bcolors.FAIL,". Exiting program.")
                break

            elif cmd.startswith("cd "):  # Handle directory change
                path = cmd[3:].strip()
                new_path = os.path.abspath(os.path.join(current_dir, path))
                if os.path.isdir(new_path):
                    current_dir = new_path
                    printf(bcolors.GREEN, f". Changed directory to: {current_dir}")
                else:
                    log_error(f"Directory not found: {path}")

            elif cmd:
                run_command(cmd, current_dir)
