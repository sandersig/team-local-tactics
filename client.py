from socket import socket
from teamNetworkTactics import *

sock = socket()
sock.connect(("localhost", 8888))

data = sock.recv(1024)
print(data.decode())

while True:
    data = sock.recv(1024) #Receive signal when both players are connected
    if(data.decode() == "1"):
        champions = load_some_champs()
        print_available_champs(champions)
        while True:
            prompt = sock.recv(1024)
            input(prompt.decode())
        #print overview of champions to player
        #take input one at a time, and put straight into a list
        #When done, return this list to the main-program and let it do its result handling
        

#input_champion(input from one of the clients)

