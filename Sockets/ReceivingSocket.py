import socket
from constant import *

with WebSocket as s:
    s.bind((HOST,RECEIVINGPORT)) #self
    s.listen()
    conn,addr = s.accept() #take all 
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) #buffer size 1024bytes
            if not data:
                break
            conn.sendall(data)
