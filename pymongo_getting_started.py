
import pymongo

from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 28000)

db = connection.video

# handle to names collection
movies = db.movies

movie = movies.find_one()

print movie
