from socket import socket
from teamNetworkTactics import *

sock = socket()
sock.connect(("localhost", 8888))

data = sock.recv(1024)
print(data.decode())

data = sock.recv(1024)

print('\n'
    'Welcome to [bold yellow]Team Network Tactics[/bold yellow]!'
    '\n'
    'Each player choose a champion each time.'
    '\n')

print(data.decode()) #Table getting printed
print('\n')

while True:
    prompt = sock.recv(2048)
    if prompt.decode().startswith('Player'):  
        data = str(input(prompt.decode()))
        sock.send(str.encode(f"{data}"))
    elif len(prompt.decode()) > 1:
        print(prompt.decode())
    else:
        sock.close()
        break
    
    

