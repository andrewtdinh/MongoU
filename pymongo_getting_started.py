
import pymongo

from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 28000)

db = connection.test

# handle to names collection
names = db.names

name = movies.find_one()

print name
