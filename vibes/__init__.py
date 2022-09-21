from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
# Initialize of whole application
app.config['SECRET_KEY'] = '532f7ffa0a70512660d0bc83ad3388c0'
# Set up secret key to prevent unauthorized acces
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Set sql db as local file (in future changed to other source) 
db = SQLAlchemy(app)
# Create variable db contains database 
bcrypt = Bcrypt(app)
# Create variable bcrypt allows to create hashed string from string
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# Create variable login_manager that allows to keep user login
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cc247b2204acaa'
app.config['MAIL_PASSWORD'] = '516d30cc44f9e2'
# Set up mail server 

mail = Mail(app)
# Create variable mail allows to create mail and send them through mail server 

from vibes import routs
