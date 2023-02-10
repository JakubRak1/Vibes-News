import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Initialize of whole application
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'] 
app.config['SQLALCHEMY_BINDS'] = {'two': "postgresql://postgres_user:123@db_tokens:5432/db_tokens"}


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
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
# Set up mail server 


mail = Mail(app)
# Create variable mail allows to create mail and send them through mail server 

# DB SETTING UP
# 
# 
# 

from vibes.data_init_cat_users import (cat_buissnes, cat_culture,
                                       cat_game_news, cat_news, cat_sport,
                                       user_admin, user_editor1, user_editor2,
                                       user_user1, user_user2)
from vibes.models import Article, Category, Rights, User

db.create_all()
# Checking if db is empty
categories = [cat_news, cat_buissnes, cat_culture, cat_game_news, cat_sport] 
users = [user_admin, user_editor1, user_editor2, user_user1, user_user2]
if bool(db.session.query(Category).filter_by(name='News').first())==False:
    db.session.add_all(categories)
    db.session.commit()
    db.session.add_all(users)
    db.session.commit()

    from vibes.data_init_articles import (buissnes_all, culture_all, game_all,
                                          news_all, sport_all)


    articles = [news_all, sport_all, buissnes_all, culture_all, game_all]

    for article in articles:
        db.session.add_all(article)
        db.session.commit()


from vibes.admin.routes import admin
from vibes.articles.routes import articles
from vibes.editor.routes import editor
from vibes.errors.handlers import errors
from vibes.main.routes import main
from vibes.user.routes import user
from vibes.users.routes import users

app.register_blueprint(main)
app.register_blueprint(articles)
app.register_blueprint(users)
app.register_blueprint(user)
app.register_blueprint(editor)
app.register_blueprint(admin)
app.register_blueprint(errors)