from tokenize import String
from flask_login import UserMixin
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
from firebase_admin import db
import sys
sys.path.append('webappdb')
from create import users_ref

class User(UserMixin):
    def __init__(
            self,
            id: Optional[int],
            email: str,
            first_name: str,
            last_name:  str,
            password: Optional[str] = "",
            country: Optional[str] = "",
            institution: Optional[str] = "",
            aos: Optional[str] = "",
            exp: Optional[str] = ""):
            
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.country = country
        self.institution = institution
        self.aos = aos
        self.exp = exp

    """
    This method is used to save the information from the registration
    form to the database. Email, first name, last name, are saved as is 
    to the database. The password is hashed for security and the hashed 
    version is saved to the database.
    """

    @staticmethod
    def register(first_name, last_name, email, password, country, ins, aos, exp, gender) -> String :
        user_id = users_ref.push({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": generate_password_hash(password),
            "country": country,
            "institution": ins,
            "aos": aos,
            "exp": exp,
            "gender": gender
        })
        return True

    """
    This method is used to confirm if there is a user account with the
    given email and if the given password is the correct password for that
    account.
    """
    #@staticmethod
    #def get_by_auth(email, password):
    #    return None

    """
    This method is used to confirm if there is a user account with the
    given email.
    """
    #@staticmethod
    #def email_exists(email):
     #   exist = users_ref.child('User').order_by_child('email').equal_to(email).get()
      #  if len(exist) == 1:
       #     print(exist)
        #    return False
        #else: 
         #   print(exist)
          #  return True
    