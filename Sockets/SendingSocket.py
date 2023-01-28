import socket
from constant import *

with WebSocket as s:
    s.connect((HOST,RECEIVINGPORT))
    s.sendall(b"Hello,World")
    data = s.recv(1024)

print(f"Received {data!r}")
        
        