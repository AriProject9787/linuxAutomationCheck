import subprocess
import sys
import platform

# Python libraries needed
python_packages = [
    "gtts",                # Text-to-speech
    "sounddevice",         # Audio input/output
    "vosk"                 # Speech recognition
]

# System packages needed (Linux)
system_packages = [
    "mpv",                 # Audio player
    "python3-pip",         # Pip package manager
    "portaudio19-dev"      # Required for sounddevice (correct name for Debian/Ubuntu)
]


# Additional Termux packages
termux_packages = [
    "mpv",
    "python",
    "clang",
    "ffmpeg",
    "portaudio"  # Termux package name
]

# =========================
# Terminal Color Formatting
# =========================
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'



# ======================
# Install Python Packages
# ======================
def install_python_packages():
    for package in python_packages:
        try:
            __import__(package)
            print(f"{bcolors.GREEN}[✓]{bcolors.ENDC} Python package '{package}' already installed.")
        except ImportError:
            print(f"{bcolors.CYAN}[+]{bcolors.ENDC} Installing Python package: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# ======================
# Install System Packages
# ======================
def install_system_packages():
    os_type = platform.system().lower()

    if "linux" in os_type:
        if "android" in platform.uname().release.lower():
            # Termux environment
            print(f"{bcolors.CYAN}[+]{bcolors.ENDC} Detected Termux environment.")
            subprocess.check_call(["pkg", "update", "-y"])
            subprocess.check_call(["pkg", "install", "-y"] + termux_packages)
        else:
            # Regular Linux
            print(f"{bcolors.CYAN}[+]{bcolors.ENDC} Detected Linux environment.")
            subprocess.check_call(["sudo", "apt", "update"])
            subprocess.check_call(["sudo", "apt", "install", "-y"] + system_packages)

    elif "windows" in os_type:
        print(f"{bcolors.WARNING}[!]{bcolors.ENDC} Please install 'mpv' manually from https://mpv.io/installation/")
    elif "darwin" in os_type:
        print(f"{bcolors.CYAN}[+]{bcolors.ENDC} Installing system packages in macOS...")
        subprocess.check_call(["brew", "install"] + system_packages)
    else:
        print(f"{bcolors.FAIL}[!]{bcolors.ENDC} Unsupported OS for system package installation.")

# ======================
# Main Execution
# ======================
if __name__ == "__main__":
    print(f"{bcolors.HEADER}=== Python & System Package Setup ==={bcolors.ENDC}")
    install_python_packages()
    install_system_packages()
    print(f"{bcolors.GREEN}[✓]{bcolors.ENDC} Setup completed successfully!")
