from socket import socket, AF_INET, SOCK_STREAM
from _thread import *
from teamNetworkTactics import *

players = []
player1 = []
player2 = []

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 8888))

sock.listen(2)

def new_client(conn):
    conn.send(str.encode("Connected")) #Let the player know when they are connected
    if len(players) == 2:
        players[0].send(str.encode("1"))
        players[1].send(str.encode("1"))
    
    champions = load_some_champs()
    msg = print_available_champs(champions)
    players[0].send(str.encode(f"{msg}"))
    players[1].send(str.encode(f"{msg}"))
    """
    for _ in range(2):
        players[0].send(str.encode("Player 1"))
        data = conn.recv(1024)
        player1.append(data)
        print(player1)

        #input_champion('Player 1', 'red', champions, player1, player2)
        players[1].send(str.encode("Player 2"))
        data = conn.recv(1024)
        player2.append(data)
        print(player1)
        #input_champion('Player 2', 'blue', champions, player2, player1)
       """
        
#players = {}

while True:
    conn, addr = sock.accept()
    print(f"Connected to {addr}")
    players.append(conn)
    1#players["Player1"] = conn 
    start_new_thread(new_client, (conn,)) 
    #Everytime a client connects, a new thread gets started
    #Each thread should run its own version of the game


#start game -> game logic should be client-side
#need to show the available champions to both players
#need to prompt "player 1" for their choice of champion
#when all player have chosen their champions the "playing" of the game can continue

sock.close()

