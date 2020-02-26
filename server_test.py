import socket
import time

HOST = '10.50.16.5'  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        count = 0
        while True:
            conn.sendall(str(count).encode())
            print(count)
            time.sleep(1)
            count += 1