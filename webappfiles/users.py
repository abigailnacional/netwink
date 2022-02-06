from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Length
from flask_babel import _, lazy_gettext as _l
#from flask_babel import Babel

from .models.user import User

from flask import Blueprint
bp = Blueprint('users', __name__)

"""
This form takes input from the user that is needed for registration, namely
a first name, last name, email, password, and address.
All fields except for the address field are required for submission.
All fields have a length requirement of 0 and a length limit.
The password must be repeated in a second field.
All data from this form is saved, unchanged, to our database, EXCEPT for the
password, which is saved as its hashed version.
"""
#for email, check email
class RegistrationForm(FlaskForm):
    first_name = StringField(_l('First Name'), validators=[DataRequired(),
        Length(min=0, max=32, message='First name must be between 0 and 32 characters in length.')])
    last_name = StringField(_l('Last Name'), validators=[DataRequired(),
        Length(min=0, max=32, message='Last name must be between 0 and 32 characters in length.')])
    email = StringField(_l('Email'), validators=[DataRequired(),
        Length(min=0, max=64, message='Email must be between 0 and 64 characters in length.')])
    password = PasswordField(_l('Password'), validators=[DataRequired(),
        Length(min=0, max=32, message='Password must be between 0 and 32 characters in length.')])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Register'))

    """
    This method validates whether or not the email being inputted is already
    within the database.
    """
    #def validate_email(self, email):
     #   if User.email_exists(email.data):
      #      raise ValidationError(_('Already a user with this email.'))

"""
This method allows the user to register with at minimum an email, password,
and first and last name. The user may also enter an address.
"""
@bp.route('/register', methods=['GET', 'POST'])
def register():
    #if current_user.is_authenticated:
    #    return redirect(url_for('index.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.register(form.first_name.data,
                         form.last_name.data,
                         form.email.data,
                         form.password.data):
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('index.index')) #change
    return render_template('register.html', title='Register', form=form)

