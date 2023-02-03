import socket 
from constant import * 
      # AF_INET IPv4.  
      # SOCK_STREAM socket type for TCP
WebSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
WebSocket.connect((DOMAIN,CONNECTINGPORT));
Request = 'GET https://www.youtube.com HTTP/1.1\n\n'.encode(); #convert to UTF8
WebSocket.sendall(Request);

while True:
      data = WebSocket.recv(1024) ## char type
      if(len(data) < 1):
            break;
      print(data.decode())
WebSocket.close()
