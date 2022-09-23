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
app.config['SQLALCHEMY_BINDS'] = {'two': 'sqlite:///tokens.db'}
db = SQLAlchemy(app)
# Create variable db contains database 
bcrypt = Bcrypt(app)
# Create variable bcrypt allows to create hashed string from string
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
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


from vibes.main.routes import main
from vibes.articles.routes import articles
from vibes.users.routes import users
from vibes.user.routes import user
from vibes.editor.routes import editor
from vibes.admin.routes import admin
from vibes.errors.handlers import errors

app.register_blueprint(main)
app.register_blueprint(articles)
app.register_blueprint(users)
app.register_blueprint(user)
app.register_blueprint(editor)
app.register_blueprint(admin)
app.register_blueprint(errors)