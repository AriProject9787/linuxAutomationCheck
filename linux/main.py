import subprocess
import platform
import os
import shutil
import json
from datetime import datetime
import gtts # type: ignore
# Define color codes for terminal output
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
# ---------- Config ----------
DEVELOPER_NAME = "Arirama Selvam M"
DESCRIPTION = "Cybersecurity | Automation | SaaS Developer"
GITHUB_LINK = "https://github.com/AriProject9787"
LINKEDIN_LINK = "https://www.linkedin.com/in/ariramaselvam"
GMAIL_LINK = "ariofficial9787@gmail.com"
LOG_FILE = "update_tool_log.txt"

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
# ---------- Tools ----------
with open("tools.json") as f:
    TOOLS = json.load(f)
# ---------- Logger ----------
def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

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

ENVIRONMENT = detect_env()
PKG_MANAGER = "pkg" if ENVIRONMENT == "termux" else "apt"


# ---------- Connectivity Check ----------
def check_connectivity():
    try:
        subprocess.run(["ping", "-c", "1", "google.com"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        printf(bcolors.GREEN, ". Internet connection is active.")
        return True
    except:
        printf(bcolors.FAIL, ". No internet connection detected.")
        return False

# ---------- Update System ----------
def update_system():
    if not check_connectivity():
        printf(bcolors.FAIL ,"[!] No internet connection. Skipping system update.")
        return
    printf(bcolors.CYAN ,f"\n[*]Please wait Updating system...")
    update_cmd = [PKG_MANAGER, "update"]
    upgrade_cmd = [PKG_MANAGER, "upgrade", "-y"]
    if ENVIRONMENT != "termux":
        update_cmd.insert(0, "sudo")
        upgrade_cmd.insert(0, "sudo")
    subprocess.run(update_cmd, check=True)
    subprocess.run(upgrade_cmd, check=True)
    printf(bcolors.GREEN ,"[+]. System updated successfully.\n")

# ---------- Install Tools ----------
def install_tools():
    printf(bcolors.BLUE ,"\n. Available Tools to Install:\n")
    for i, tool in enumerate(TOOLS, 1):
        print(bcolors.ENDC + f"{str(i).zfill(2)}. {tool} - {TOOLS[tool]}")
    print("00. Exit\n")
    printf(bcolors.HEADER, ". Enter tool number(s) to install : ")

    choice = input().strip().split()

    if "00" in choice:
        return

    selected = []
    try:
        for c in choice:
            key = list(TOOLS.keys())[int(c) - 1]
            selected.append(key)
    except:
        printf(bcolors.WARNING ,". Invalid selection.\n")
        return

    printf(bcolors.CYAN ,f"\n Please wait Installing tools: {', '.join(selected)}\n")

    for tool in selected:
        try:
            cmd = ["pkg", "install", "-y", tool] if ENVIRONMENT == "termux" else ["sudo", "apt", "install", "-y", tool]
            subprocess.run(cmd, check=True)
            printf(bcolors.GREEN ,f"The {tool} installed successfully.")
            log(f"{tool} installed.")
        except subprocess.CalledProcessError as e:
            printf(bcolors.FAIL ,f". Failed to install {tool}: {e}")
            log(f". Failed to install {tool}: {e}")
    print()

# ---------- Update Tools ----------
def update_tools():
    printf(bcolors.BLUE ,"\n. Available Tools to Update:\n")
    for i, tool in enumerate(TOOLS, 1):
        print(bcolors.ENDC + f"{str(i).zfill(2)}. {tool} - {TOOLS[tool]}")
    print("00. Exit\n")
    printf(bcolors.HEADER, ". Enter tool number(s) to update : ")
    choice = input().strip().split()

    if "00" in choice:
        return

    selected = []
    try:
        for c in choice:
            key = list(TOOLS.keys())[int(c) - 1]
            selected.append(key)
    except:
        printf(bcolors.FAIL ,". Invalid selection.\n")
        return

    printf(bcolors.CYAN ,f"\n. Updating tools: {', '.join(selected)}\n")

    for tool in selected:
        try:
            cmd = ["pkg", "upgrade", tool, "-y"] if ENVIRONMENT == "termux" else ["sudo", "apt", "install", "--only-upgrade", "-y", tool]
            subprocess.run(cmd, check=True)
            printf(bcolors.GREEN ,f".  {tool} updated successfully.")
            log(f"{tool} updated.")
        except subprocess.CalledProcessError as e:
            printf(bcolors.FAIL ,f". Failed to update {tool}: {e}")
            log(f"Failed to update {tool}: {e}")
    print()


# ---------- Installed Tools Viewer ----------
def view_installed_tools():
    printf(bcolors.HEADER ,"\n Tool Status Installed or not:\n")
    for tool in TOOLS:
        if shutil.which(tool):
            print(bcolors.ENDC +f" {tool.ljust(12)} - Installed")
        else:
            print(bcolors.WARNING +f" {tool.ljust(12)} - Not Found")
    print()

# ---------- About Developer ----------
def about_developer():
    print(bcolors.GREEN +f"\n Developer Information")
    print(bcolors.GREEN +f"=" * 40)
    print(bcolors.GREEN +f"Name     : {DEVELOPER_NAME}")
    print(bcolors.GREEN +f"About    : {DESCRIPTION}")
    print(bcolors.GREEN +f"GitHub   : {GITHUB_LINK}")
    print(bcolors.GREEN +f"LINKEDIN   : {LINKEDIN_LINK}")
    print(bcolors.GREEN +f"GMAIL   : {GMAIL_LINK}")
    print(bcolors.GREEN +f"Log File : {os.path.abspath(LOG_FILE)}")
    print(bcolors.GREEN +f"=" * 40 + "\n")

# ---------- Exit Program ----------
def exit_program():
    printf(bcolors.FAIL ,"\n Exiting Program... Thank You, !\n")
    log("Program exited.")
    exit()

# ---------- Main Menu ----------
def main():
    while True:
        print(bcolors.BLUE +"=" * 50)
        print(bcolors.BLUE + "  LINUX & TERMUX TOOLKIT - BY ARIRAMA SELVAM M")
        print(bcolors.BLUE +"=" * 50)
        print(bcolors.BLUE +"01.  Update System")
        print(bcolors.BLUE +"02.  Install Tools")
        print(bcolors.BLUE +"03.  Update Selected Tools")
        print(bcolors.BLUE +"04.  About Developer")
        print(bcolors.BLUE +"05.  View Installed Tools")
        print(bcolors.BLUE +"06.  Clear Terminal")
        print(bcolors.BLUE +"07.  Metasploit Automation Tool")
        print(bcolors.BLUE +"08.  Wifi Deauth Attack")
        print(bcolors.BLUE +"09.  Exit Program")
        print(bcolors.BLUE +"=" * 50)
        printf(bcolors.HEADER, ". Please select an option: ")
        choice = input().strip()

        if choice == "01":
            update_system()
        elif choice == "02":
            install_tools()
        elif choice == "03":
            update_tools()
        elif choice == "04":
            printf(bcolors.CYAN ,"\n. This tool was developed by Arirama Selvam M. this tool is designed to automate various tasks in Linux and Termux environments.")
            about_developer()
        elif choice == "05":
            view_installed_tools()
        elif choice == "06":
            printf(bcolors.CYAN ,"\n. Clearing terminal...")
            log("Terminal cleared.")
            subprocess.run(["clear"], check=True)
        elif choice == "07":
            printf(bcolors.CYAN ,"\n. Launching Metasploit Automation Tool...")
            log("Launching Metasploit Automation Tool.")
            subprocess.run(["python3", "metasploit.py"])
        elif choice == "08":
            printf(bcolors.CYAN ,"\n. Launching Wifi Deauth Attack Tool...")
            log("Launching Wifi Deauth Attack Tool.")
            subprocess.run(["python3", "deauthAttack.py"])
        elif choice == "09" or choice == "00":
            exit_program()
        else:
            printf(bcolors.WARNING ,"\n Invalid input. Please try again.\n")

if __name__ == "__main__":
    main()
