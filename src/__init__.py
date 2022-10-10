from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# Setup MongoDB
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
client = PyMongo(app)
database = client.db
print(database)

from src import routes