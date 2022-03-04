import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

# Get you password from .env file
password = os.environ.get("password")
username = "sandersig"
clusterName = "inf142-cluster-demo"

# Connect to you cluster
client = MongoClient('mongodb+srv://' + username + ':' + password + '@' + clusterName + '.6t1y5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# Create a new database in your cluster
database = client.INF142

# Create a new collection in you database
person = database.person

personDocument = {
  "firstname": "Ola",
  "lastname": "Engelskmann",
  "course": "INF142"
}

person.insert_one(personDocument)





