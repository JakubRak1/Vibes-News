from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from vibes.models import User


class LoginForm (FlaskForm):
    # Constructor of login form
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Log In')


class ContactAdminFrom (FlaskForm):
    # Constructor of contact admin form
    fullname = StringField('Full Name', validators=[data_required(), Length(min = 2, max = 100)])
    email = StringField('Email', validators=[data_required(), Email()])
    text = TextAreaField('Message', validators=[data_required()])
    submit = SubmitField('Send')


class RequestResetForm (FlaskForm):
    # Constructor of request reset form
    email = StringField('Email', validators=[data_required(), Email()])
    confirm_email = StringField('Confirm Email', validators=[data_required(), Email(), EqualTo('email')])
    submit = SubmitField('Reset Password')

    
    def validate_email(self, email):
        # Function to verify if variable email exist in database
        user = User.query.filter_by(email = email.data).first()
        # If in database there is User with variable email, user variable contains User object and if not variable is None 
        if not user:
            # Check if user is object
            raise ValidationError ('There is no account with this email')


class ResetPasswordForm(FlaskForm):
    # Constructor of reset password form
    password = PasswordField('Password', validators=[data_required()])
    confirm_password = PasswordField('Confirm Password', validators=[data_required(), EqualTo('password')])
    submit = SubmitField('Set up new password')
