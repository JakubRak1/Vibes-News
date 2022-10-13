from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import data_required, Length, Email, ValidationError
from vibes.models import User


class ChangeUserFormEditor (FlaskForm):
    # Constructor of Change user form
    fullname = StringField('Full Name', validators=[data_required(), Length(min = 2, max = 100)])
    username = StringField('Username', validators=[data_required(), Length(min = 2, max = 100)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    categories = SelectMultipleField('Categories Rights', choices=[])
    submit = SubmitField('Edit User')


    def validate_username(self, username):
        # Function to verify if new variable username exist in database 
        user = User.query.filter_by(username = username.data).first()
        # If in database there is User with variable username, user variable contains User object and if not variable is None 
        if user and username!=self.username:
            # Check if user is object and check if username variable is not changed
            raise ValidationError ('There is already account with this username')


    def validate_email(self, email):
        # Function to verify if new variable email exist in database
        user = User.query.filter_by(email = email.data).first()
        # If in database there is User with variable email, user variable contains User object and if not variable is None  
        if user and email!=self.email:
            # Check if user is object and check if email variable is not changed
            raise ValidationError ('There is already account with this email')