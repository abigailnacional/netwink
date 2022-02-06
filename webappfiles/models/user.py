from flask_login import UserMixin
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
#from .. import login

import sys
sys.path.append('webappdb')
from create import users_ref

class User(UserMixin):
    def __init__(
            self,
            id: int,
            email: str,
            first_name: str,
            last_name:  str,
            password: Optional[str] = ""):
            
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    

    """
    This method is used to save the information from the registration
    form to the database. Email, first name, last name, and address
    (if one is provided) are saved as is to the database. The password
    is hashed and the hashed version is saved to the database.
    """
    @staticmethod
    def register(first_name, last_name, email, password):
        new_user = users_ref.push({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": generate_password_hash(password)
        })
        return True

