# import socket 
# 
        # socket type. AF_INET is the Internet address family for IPv4.
        # SOCK_STREAM is the socket type for TCP
# WebSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# WebSocket.connect(('dtat.pr4e.org',80));
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode();
# WebSocket.send(cmd);
# 
# while True:
#     data = mysock.recv(512)
#     if(len(data)<1):
#         break;
#     print(data.decode())
# WebSocket.close();