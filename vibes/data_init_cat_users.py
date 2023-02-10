from vibes import bcrypt, db
from vibes.models import Article, Category, User

# Catergories
cat_news = Category(name = 'News')
cat_sport = Category(name = 'Sport')
cat_buissnes = Category(name = 'Buissnes')
cat_culture = Category(name = 'Culture')
cat_game_news = Category(name = 'Game News')
# Users
user_admin = User(fullname = 'Admin', username = 'Admin', email='admin@gmail.com', password=bcrypt.generate_password_hash('123').decode('utf-8'), admin_rights = 2, category =[cat_news,cat_sport,cat_buissnes,cat_culture,cat_game_news], articles=[])
user_editor1 = User(fullname = 'Emily Taylor', username = 'emilytaylor', email='editor1@gmail.com', password=bcrypt.generate_password_hash('123').decode('utf-8'), admin_rights = 1, category=[cat_news,cat_sport], articles=[])
user_editor2 = User(fullname = 'Matthew Rodriguez', username = 'matthewr', email='editor2@gmail.com', password=bcrypt.generate_password_hash('123').decode('utf-8'), admin_rights = 1, category= [cat_news, cat_buissnes, cat_culture, cat_game_news], articles=[])
user_user1 = User(fullname = 'Olivia Hernandez', username = 'oliviah', email='user1@gmail.com', password=bcrypt.generate_password_hash('123').decode('utf-8'), category = [cat_news,cat_game_news], articles=[])
user_user2 = User(fullname = 'James Green', username = 'jamesg', email='user2@gmail.com', password=bcrypt.generate_password_hash('123').decode('utf-8'), category = [cat_sport,cat_buissnes,cat_culture], articles=[])