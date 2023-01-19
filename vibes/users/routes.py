from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message

from vibes import app, bcrypt, db, mail
from vibes.models import Article, User
from vibes.users.forms import (ContactAdminFrom, LoginForm, RequestResetForm,
                               ResetPasswordForm)
from vibes.users.utils import send_reset_email

users = Blueprint('users', __name__)


@users.route("/login", methods = ["GET", "POST"])
def login():
    # Function that display login.html template when url is /login
    if current_user.is_authenticated:
        # Check if user is already login if its true redirects to home function
        return redirect(url_for('main.home'))
    form: object = LoginForm()
    # Set form as LoginForm from vibes.forms
    if form.validate_on_submit():
        # Check if submit is correct and checks if User object exist in database with provided email 
        user: User = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Check if user is object and password of this user is correct with provided from form
            login_user(user)
            # Logs user in
            next_page = request.args.get('next')
            flash(f'Login Succusefully, Welcome {user.fullname}', 'succsess')
            # Display sucess message
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
            # Redirect to page that required login
        else:
            flash(f'Login Unsuccusefully, check email and password again')
            # Display error message
    return render_template('login.html', title = 'Log In', legend = 'Log In', form = form)
    # Passing to article.html templete form variable


@users.route("/logout", methods = ["GET", "POST"])
@login_required 
# To acces this template user need to be log in
def logout():
    # Function that logout user and redirecting to home function 
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/contact", methods = ["GET", "POST"])
def contact_admin():
    # Function that display contact.html template when url is /contact
    form: object = ContactAdminFrom()
    # Set form as ContactAdminForm from vibes.forms
    if form.validate_on_submit():
        # Check if submit is correct and sends message to admin email 
        admin: User = User.query.filter_by(admin_rights = 2).first()
        # Finding admin object from database
        msg: Message = Message('Contact through site', sender = form.email.data, recipients=[admin.email])
        msg.body = f'''Message from: {form.fullname.data}
{form.text.data}'''
        # Set mail properties as title, sender, reciver and content
        mail.send(msg)
        # Sends mail
        flash(f'Email was sent to admin, wait for replay')
        return redirect(url_for('main.home'))
        # Display message and redirect to home function
    if current_user.is_authenticated:
            form.fullname.data = current_user.fullname
            form.email.data = current_user.email
    return render_template('contact.html', title = 'Log In', legend = 'Contact with Us', form = form)
    # Passing to contact.html templete form variable


@users.route("/reset_password", methods = ["GET", "POST"])
def reset_password():
    # Function that display reset_password.html template when url is /reset_password
    if current_user.is_authenticated:
        # Check if user is already login if its true redirects to home function
        return redirect(url_for('main.home'))
    form: object = RequestResetForm()
    # Set form as RequestResetForm from vibes.forms
    if form.validate_on_submit():
        # Check if submit is correct and checks if User object exist in database with provided email 
        user: User = User.query.filter_by(email = form.email.data).first()
        if user:
            # Check if user is object and runs function send_reset_email with user object
            send_reset_email(user)
            flash(f'Email with reset link sent to {form.email.data}', 'succsess')
            return redirect(url_for('users.login'))
        else:
            flash(f'There is no account with email: {form.email.data}')
            # Display error message
    return render_template('reset_password.html', title = 'Reset Password', legend = 'Reset Password', form = form)
    # Passing to reset_password.html templete form variable


@users.route("/reset_password/<token>", methods = ["GET", "POST"])
def reset_token(token):
    # Function that display set_password.html template when url is /reset_password/{token}
    if current_user.is_authenticated:
        # Check if user is already login if its true redirects to home function
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None: 
        # Check if token was invalid
        flash('Thats its invalid token or its expired')
         # Display error message
        return redirect(url_for('users.reset_password'))
    form: object = ResetPasswordForm()
    # Set form as ResetPasswordForm from vibes.forms
    if form.validate_on_submit():
        # Check if submit is correct and create new hashed password 
        hashed_password: str = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Creates hashed string based on data from form
        user.password = hashed_password
        # Set user password as new hased password
        db.session.commit()
        # Saving changes to database
        flash('Your password is changed you can log now with him', 'succes')
        return redirect(url_for('users.login'))
        # After successfully changing password redirecting to login function
    return render_template('set_password.html', title = 'Set Password', legend = 'Set Password', form = form )
    # Passing to set_password.html templete form variable


@users.route("/news", methods = ["GET"])
def news_articles():
    page = request.args.get('page', 1, type=int)
    news_articles = Article.query.filter(Article.category_id == 1).paginate(page=page, per_page = 3)
    return render_template('articles_category.html', title = 'News Articles', Articles = news_articles)

@users.route("/sport", methods = ["GET"])
def sport_articles():
    page = request.args.get('page', 1, type=int)
    sport_articles = Article.query.filter(Article.category_id == 2).paginate(page=page, per_page = 3)
    return render_template('articles_category.html', title = 'Sport Articles', Articles = sport_articles)

@users.route("/buissnes", methods = ["GET"])
def buissnes_articles():
    page = request.args.get('page', 1, type=int)
    buissnes_articles = Article.query.filter(Article.category_id == 3).paginate(page=page, per_page = 3)
    return render_template('articles_category.html', title = 'Buissnes Articles', Articles = buissnes_articles)

@users.route("/culture", methods = ["GET"])
def culture_articles():
    page = request.args.get('page', 1, type=int)
    culture_articles = Article.query.filter(Article.category_id == 4).paginate(page=page, per_page = 3)
    return render_template('articles_category.html', title = 'Culture Articles', Articles = culture_articles)


@users.route("/game", methods = ["GET"])
def game_articles():
    page = request.args.get('page', 1, type=int)
    game_articles = Article.query.filter(Article.category_id == 5).paginate(page=page, per_page = 3)
    return render_template('articles_category.html', title = 'Game News Articles', Articles = game_articles)