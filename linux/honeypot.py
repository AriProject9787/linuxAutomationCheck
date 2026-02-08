import socket
import threading
from datetime import datetime

# Configuration
HOST = '0.0.0.0'     # Listen on all interfaces
PORT = 80          # Fake SSH port
LOG_FILE = "honeypot_log.txt"

def log_attempt(ip, data):
    with open(LOG_FILE, 'a') as file:
        file.write(f"[{datetime.now()}] Connection from {ip} | Data: {data}\n")

def handle_connection(client_socket, address):
    print(f"[+] Connection from {address[0]}")
    try:
        client_socket.send(b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n")
        data = client_socket.recv(1024).decode(errors="ignore").strip()
        log_attempt(address[0], data)
        client_socket.send(b"Permission denied (publickey,password).\n")
    except Exception as e:
        print(f"[-] Error handling connection: {e}")
    finally:
        client_socket.close()

def start_honeypot():
    print(f"[STARTING] Honeypot listening on port {PORT}...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_connection, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    try:
        start_honeypot()
    except KeyboardInterrupt:
        print("\n[STOPPED] Honeypot shut down.")
