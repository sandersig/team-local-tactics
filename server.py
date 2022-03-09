from socket import socket, AF_INET, SOCK_STREAM
from _thread import *
from teamNetworkTactics import *
from champlistloader import from_db
import pickle
#from mongoDB import retrieve_champions

players = []

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 8888))

sock.listen(3)

def prompt_user_for_champion_choice(player_nr : int,
                                     player1 : list[str],
                                     player2 : list[str],
                                     champions : dict[Champion]) -> None:
    
    players[player_nr].send(str.encode(f"Player {player_nr}: "))
    data = players[player_nr].recv(1024)
    msg = input_champion(data.decode(), champions, player1, player2)
    #TODO: Need to fix better error-treatment
    if msg != "N/A":
        players[player_nr].send(str.encode(f"{msg}"))
        prompt_user_for_champion_choice(player_nr, champions, player2, player1)

def new_client(conn, champions):
    msg = print_available_champs(champions)
    players[1].send(str.encode(f"{msg}"))
    players[2].send(str.encode(f"{msg}"))
    
    player1 = []
    player2 = []

    for _ in range(2):
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
        start_new_thread(new_client, (conn, champions)) 
    #Everytime a client connects, a new thread gets started
    #Each thread should run its own version of the game