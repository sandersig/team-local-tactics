from socket import socket, AF_INET, SOCK_STREAM
from _thread import *
from teamNetworkTactics import *
from champlistloader import from_db
import pickle

players = []

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 8888))

sock.listen(3)

def prompt_user_for_champion_choice(player_nr : int,
                                     player1 : list[str],
                                     player2 : list[str],
                                     champions : dict[Champion]) -> None:

    while True:
        players[player_nr].send(str.encode(f"Player {player_nr}: "))
        name = players[player_nr].recv(1024).decode()
        if name not in champions:
            players[player_nr].send(str.encode(f'The champion {name} is not available. Try again.'))
        elif name in player1:
            players[player_nr].send(str.encode(f'{name} is already in your team. Try again.'))
        elif name in player2:
            players[player_nr].send(str.encode(f'{name} is in the enemy team. Try again.'))
        else:
            player1.append(name)
            break

def start_game(champions):
    msg = print_available_champs(champions)
    players[1].send(str.encode(f"{msg}"))
    players[2].send(str.encode(f"{msg}"))
    
    player1 = []
    player2 = []

    for _ in range(2):
        # 
        prompt_user_for_champion_choice(1, player1, player2, champions)

        prompt_user_for_champion_choice(2, player2, player1, champions)

        print(player1)
        print(player2)

    result = play_match(champions, player1, player2)
    players[1].send(str.encode(f"{result}"))
    players[2].send(str.encode(f"{result}"))
    sock.close()
        
while True:
    conn, addr = sock.accept()
    print(f"Connected to {addr}")
    conn.send(str.encode("Connected")) #Let the player know when they are connected
    players.append(conn)
    if len(players) == 3:
        players[0].send(str.encode("Ready for db"))
        data = players[0].recv(2048)
        champs = pickle.loads(data)
        champions = from_db(champs)
        start_game(champions)