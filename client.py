from socket import socket
from teamNetworkTactics import *

sock = socket()
sock.connect(("localhost", 8888))

data = sock.recv(1024)
print(data.decode())

while True:
    data = sock.recv(1024) #Receive signal when both players are connected
    if(data.decode() == "1"):
        print('\n'
          'Welcome to [bold yellow]Team Network Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')
        data = sock.recv(1024)
        print(data.decode()) #Table gettin printed
        print('\n')
        while True:
            prompt = sock.recv(2048)
            data = input(prompt.decode())
            sock.send(str.encode(f"{data}"))    

