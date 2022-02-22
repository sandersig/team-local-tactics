from socket import socket, AF_INET, SOCK_STREAM
from teamNetworkTactics import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 8888))

sock.listen(2)

#while True:
conn, addr = sock.accept()
print(f"Connected by {addr}")
main()


#start game
#need to show the available champions to both players
#need to prompt "player 1" for their choice of champion
#when all player have chosen their champions the "playing" of the game can continue

#while True:
#    data = conn.recv(1024)
#    if not data:
#        break
#    conn.sendall(data)

sock.close()

