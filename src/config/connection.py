from src import app
from flask_pymongo import PyMongo
import os

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
client = PyMongo(app)
database = client.db