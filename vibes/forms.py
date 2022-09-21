from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, SelectMultipleField, BooleanField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from vibes.models import Article, Category, User


class LoginForm (FlaskForm):
    # Constructor of login form
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Log In')


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


class ContactAdminFrom (FlaskForm):
    # Constructor of contact admin form
    fullname = StringField('Full Name', validators=[data_required(), Length(min = 2, max = 100)])
    email = StringField('Email', validators=[data_required(), Email()])
    text = TextAreaField('Message', validators=[data_required()])
    submit = SubmitField('Send')


class RegisterForm (FlaskForm):
    # Constructor of Register form
    fullname = StringField('Full Name', validators=[data_required(), Length(min = 2, max = 100)])
    username = StringField('Username', validators=[data_required(), Length(min = 2, max = 100)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Create Account')


    def validate_username(self, username):
        # Function to verify if variable username exist in database
        user = User.query.filter_by(username = username.data).first()
        # If in database there is User with variable username, user variable contains User object and if not variable is None 
        if user:
            # Check if user is object
            raise ValidationError ('There is already account with this username')


    def validate_email(self, email):
        # Function to verify if variable email exist in database
        user = User.query.filter_by(email = email.data).first()
        # If in database there is User with variable email, user variable contains User object and if not variable is None  
        if user:
             # Check if user is object
            raise ValidationError ('There is already account with this email')


class ChangeUserForm (FlaskForm):
    # Constructor of Change user form
    fullname = StringField('Full Name', validators=[data_required(), Length(min = 2, max = 100)])
    username = StringField('Username', validators=[data_required(), Length(min = 2, max = 100)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    admin_right = SelectField('Privilege Right', choices=[(1, 'Editor'), (0, 'User')], validators=[data_required()])
    categories = SelectMultipleField('Categories Rights', choices=[(c.name, c.name) for c in Category.query.all()])
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


class DeleteUserForm (FlaskForm):
    # Constructor of Delete user form
    aprove = BooleanField('Are you sure you want to delete user?', validators=[data_required()])
    submit = SubmitField('Delete User')


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


class ChangeArticleForm (FlaskForm):
    # Constructor of Change article form
    title = StringField('Title of Article', validators=[data_required(), Length(min = 2, max = 255)])
    image_of_article = FileField('Main image of Article', validators=[FileAllowed(['jpg', 'png'])])
    subtitle = TextAreaField('Subtitle', validators=[data_required()])
    content = TextAreaField('Content', validators=[data_required()])
    source = StringField('Source', validators=[data_required(), Length(min = 2, max = 255)])
    category = SelectField('Categories', choices=[(c.name, c.name) for c in Category.query.all()])
    submit = SubmitField('Change Article')


    def validate_title(self, title):
        # Function to verify if new variable title exist in database
        article: Article = Article.query.filter_by(title = title.data).first()
        # If in database there is Article with variable title, article variable contains Article object and if not variable is None  
        if article and (title!=self.title):
            # Check if article is object and check if title variable is not changed
            raise ValidationError ('There is already Article with this title')


class DeleteArticleForm (FlaskForm):
    # Constructor of Delete article form
    aprove = BooleanField('Are you sure you want to delete Article?', validators=[data_required()])
    submit = SubmitField('Delete Article')