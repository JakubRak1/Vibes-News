from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, TextAreaField, SelectField
from wtforms.validators import data_required, Length, Email, ValidationError
from vibes.models import User, Article, Category


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

class CreateArticleForm (FlaskForm):
    # Constructor of Create article form
    title = StringField('Title of Article', validators=[data_required(), Length(min = 2, max = 255)])
    image_of_article = FileField('Main image of Article', validators=[FileAllowed(['jpg', 'png'])])
    subtitle = TextAreaField('Subtitle', validators=[data_required()])
    content = TextAreaField('Content', validators=[data_required()])
    source = StringField('Source', validators=[data_required(), Length(min = 2, max = 255)])
    category = SelectField('Categories', choices=[(c.name, c.name) for c in Category.query.all()])
    submit = SubmitField('Create Article')


    def validate_title(self, title):
        # Function to verify if new variable title exist in database
        article = Article.query.filter_by(title = title.data).first()
        # If in database there is Article with variable title, article variable contains Article object and if not variable is None 
        if article:
            # Check if article is object
            raise ValidationError ('There is already Article with this title')