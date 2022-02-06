from flask import Flask
from webappfiles import create_bps
from flask_babel import Babel
from configFB import config

# create and configure the app
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate('webappdb/netwink-firebase-adminsdk-pm6tc-b7a888220f.json')
firebase_admin.initialize_app(cred, config)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
babel = Babel(app)

create_bps(app)

if __name__ == '__main__':
	app.run(debug=True)
