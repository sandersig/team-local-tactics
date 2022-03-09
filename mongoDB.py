import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os
from socket import socket
import pickle


sock = socket()
sock.connect(("localhost", 8888))

data = sock.recv(1024) #Message when connected to server 
print(data.decode())

# Get you password from .env file
password = os.environ.get("password")
username = "sandersig"
clusterName = "inf142-cluster-demo"

# Connect to you cluster
client = MongoClient('mongodb+srv://' + username + ':' + password + '@' + clusterName + '.6t1y5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# Create a new database in your cluster
database = client.INF142

# Create a new collection in your database
champions = database.champions

champion_details = champions.find()
result = []
for champion in champion_details:
  result.append(champion)

data = sock.recv(1024) #Waits for signal
print(data.decode())

data = pickle.dumps(result)
sock.send(data)




