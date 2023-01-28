import socket
DOMAIN = "www.google.com";
HOST = '127.0.0.1'
CONNECTINGPORT = 80
RECEIVINGPORT = 63291
WebSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
