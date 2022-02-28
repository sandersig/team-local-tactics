from socket import socket, AF_INET, SOCK_STREAM
from _thread import *
from teamNetworkTactics import *

players = []

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 8888))

sock.listen(2)

def input_champion(name: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:
    while True:
        match name:
            case name if name not in champions:
                print(f'The champion {name} is not available. Try again.')
            case name if name in player1:
                print(f'{name} is already in your team. Try again.')
            case name if name in player2:
                print(f'{name} is in the enemy team. Try again.')
            case _:
                player1.append(name)
                break

def new_client(conn):
    conn.send(str.encode("Connected")) #Let the player know when they are connected
    if len(players) == 2:
        players[0].send(str.encode("1"))
        players[1].send(str.encode("1"))
    
        champions = load_some_champs()
        msg = print_available_champs(champions)
        players[0].send(str.encode(f"{msg}"))
        players[1].send(str.encode(f"{msg}"))

        player1 = []
        player2 = []
        for _ in range(2):
            players[0].send(str.encode("Player 1"))
            data = players[0].recv(1024)
            #player1.append(data.decode())
            #print(player1)
            input_champion(data.decode() , champions, player1, player2)

            players[1].send(str.encode("Player 2"))
            data = players[1].recv(1024)
            #player2.append(data.decode())
            #print(player1)
            input_champion(data.decode(), champions, player2, player1)
        
        # Match
        match = Match(
            Team([champions[name] for name in player1]),
            Team([champions[name] for name in player2])
        )
        match.play()

        # Print a summary
        result = print_match_summary(match)
        players[0].send(str.encode(f"{result}"))
        players[1].send(str.encode(f"{result}"))
        sock.close()
        

while True:
    conn, addr = sock.accept()
    print(f"Connected to {addr}")
    players.append(conn)
    start_new_thread(new_client, (conn,)) 
    #Everytime a client connects, a new thread gets started
    #Each thread should run its own version of the game