from flask import Flask
from webappfiles import create_bps
import pyrebase
from flask_babel import Babel

# create and configure the app
app = Flask(__name__)

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

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
#app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

db = firebase.database()

create_bps(app)

if __name__ == '__main__':
	app.run(debug=True)
