from socket import socket

sock = socket()
sock.connect(("localhost", 8888))

#sock.sendall(b"Hello, world")
#data = sock.recv(1024)

#print(f"Received {data}")

