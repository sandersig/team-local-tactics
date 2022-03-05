import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os
from socket import socket
import pickle

def retrieve_champions():
  sock = socket()
  sock.connect(("localhost", 8888))

  # Get you password from .env file
  password = os.environ.get("password")
  username = "sandersig"
  clusterName = "inf142-cluster-demo"

  # Connect to you cluster
  #client = MongoClient('localhost', 27017)
  client = MongoClient('mongodb+srv://' + username + ':' + password + '@' + clusterName + '.6t1y5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

  # Create a new database in your cluster
  database = client.INF142

  # Create a new collection in your database
  champions = database.champions

  champion_details = champions.find()
  result = []
  for champion in champion_details:
    result.append(champion)

  data = pickle.dumps(result)
  sock.send(data)




