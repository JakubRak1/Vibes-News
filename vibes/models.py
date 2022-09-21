from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from vibes import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id: int) -> object:
    # Function to return User entry by his ID
    return User.query.get(int(user_id))

# Constructor to Rights table
Rights = db.Table('Rights', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)


class User(db.Model, UserMixin):
    # Constructor to User table
    id = db.Column (db.Integer, primary_key = True)
    fullname = db.Column (db.String(100), nullable = False)
    username = db.Column (db.String(100), unique = True, nullable = False)
    email = db.Column (db.String(250), unique = True, nullable = False)
    password = db.Column (db.String(255), nullable = False)
    admin_rights = db.Column (db.Integer, nullable = False, default = 0)
    create_time = db.Column (db.DateTime, nullable = False, default = datetime.utcnow)
    articles = db.relationship('Article', backref = 'author', lazy = True)
    category = db.relationship('Category', secondary = Rights, backref = 'users', lazy = True)
    

    def get_reset_token(self, expires_sec: int = 1800) -> str:
        # Function to create and return token 
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')


    @staticmethod
    def verify_reset_token(token: str):
        # Function to verify token
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__(self) -> str:
        return f"User fullname: {self.fullname}, email: {self.email}, admin_rights: {self.admin_rights}"


class Category(db.Model):
    # Constructor to Category table
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(50), nullable = False)
    articles = db.relationship('Article', backref = 'category', lazy = True)


    def __repr__(self) -> str:
        return f"{self.name}"



class Article(db.Model):
    # Constructor to Article table
    id = db.Column (db.Integer, primary_key = True)
    title = db.Column (db.String(255), unique = True, nullable = False)
    image_of_article = db.Column (db.String(255), nullable = False, default = 'default.png')
    subtitle = db.Column (db.Text, nullable = False)
    content = db.Column (db.Text, nullable = False)
    source = db.Column (db.String(255), nullable = False)
    time_posted = db.Column (db.DateTime, nullable = False, default = datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __repr__(self) -> str:
        return f"Name of article {self.title}, time posted: {self.time_posted}"