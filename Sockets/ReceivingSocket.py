import socket
from constant import *

with WebSocket as s:
    s.bind((HOST,RECEIVINGPORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
