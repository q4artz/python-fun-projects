import socket 
from constant import * 
      # socket type. AF_INET is the Internet address family for IPv4.      # SOCK_STREAM is the socket type for TCP
WebSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
WebSocket.connect((DOMAIN,CONNECTINGPORT));
Request = 'GET https://google.com HTTP/2\n\n'.encode();
WebSocket.send(Request);

while True:
      data = WebSocket.recv(1024)
      if(len(data) < 1):
            break;
      print(data.decode())
WebSocket.close()
