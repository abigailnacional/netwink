import pyrebase
import firebase_admin
from firebase_admin import db

from flask import Blueprint
bp = Blueprint('create', __name__)

ref = db.reference('/')

#Creating database "tables"
users_ref = ref.child('Users')


