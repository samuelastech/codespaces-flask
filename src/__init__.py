from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

from src.config import connection
from src import routes