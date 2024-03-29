from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (PasswordField, SelectField, SelectMultipleField,
                     StringField, SubmitField, TextAreaField)
from wtforms.validators import Email, Length, ValidationError, data_required

from vibes import db
from vibes.models import Article, Category, User


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
        user = db.session.query(User).filter_by(username = username.data).first()
        # If in database there is User with variable username, user variable contains User object and if not variable is None 
        if user and username!=self.username:
            # Check if user is object and check if username variable is not changed
            raise ValidationError ('There is already account with this username')


    def validate_email(self, email):
        # Function to verify if new variable email exist in database
        user = db.session.query(User).filter_by(email = email.data).first()
        # If in database there is User with variable email, user variable contains User object and if not variable is None  
        if user and email!=self.email:
            # Check if user is object and check if email variable is not changed
            raise ValidationError ('There is already account with this email')

class CreateArticleForm (FlaskForm):
    # Constructor of Create article form
    title = StringField('Title of Article', validators=[data_required(), Length(min = 2, max = 255)])
    image_of_article = FileField('Main image of Article', validators=[FileAllowed(['jpg', 'png'])])
    subtitle = TextAreaField('Subtitle', validators=[data_required()])
    content = TextAreaField('Content', validators=[data_required()])
    source = StringField('Source', validators=[data_required(), Length(min = 2, max = 255)])
    category = SelectField('Categories', choices=[(c.name, c.name) for c in db.session.query(Category).all()])
    submit = SubmitField('Create Article')


    def validate_title(self, title):
        # Function to verify if new variable title exist in database
        article = db.session.query(Article).filter_by(title = title.data).first()
        # If in database there is Article with variable title, article variable contains Article object and if not variable is None 
        if article:
            # Check if article is object
            raise ValidationError ('There is already Article with this title')