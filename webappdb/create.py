import pyrebase
#from flask import current_app as app
from flask import Flask
from flask import Blueprint
bp = Blueprint('create', __name__)

config = {
    "apiKey": "AIzaSyCm-za0dBaptEx6evvv3gTp9Pn7RUYN6e8",
    "authDomain": "netwink.firebaseapp.com",
    "projectId": "netwink",
    "storageBucket": "netwink.appspot.com",
    "messagingSenderId": "275178035488",
    "appId": "1:275178035488:web:37bb9512aedf562e885f45",
    "measurementId": "G-R3428S6FKW",
    "databaseURL": "https://netwink-default-rtdb.firebaseio.com/"
    }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#Creating database "tables"

#Users
users_ref = db.child("Users")
