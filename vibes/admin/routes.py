from datetime import datetime

from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from vibes import bcrypt, db
from vibes.admin.forms import (ChangeUserForm, CreateArticleForm,
                               DeleteUserForm, RegisterForm)
from vibes.articles.utils import save_picture
from vibes.models import Article, Category, User

admin = Blueprint('admin', __name__)


@admin.route("/admin_panel")
@login_required
# To access this template user need to be log in
def admin_panel():
    # Function that display admin_panel.html template when url is /admin_panel
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        return render_template('admin_panel.html', title = 'Admin Panel', user = current_user)
        # Passing to admin_panel.html templete user variable
    else:
        abort(403)
        # Redirect to home function


@admin.route("/admin_panel/manage_users" , methods= ["GET"])
@login_required
# To access this template user need to be log in
def manage_users():
    # Function that display manage_users.html template when url is /manage_users
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        users: list[User] = User.query.filter(User.admin_rights < 2).all()
        # Create users variable that contains all users object with admin_rights equal to 1 or 0 
        time: object = datetime.utcnow()
        # Create time viarable and set as current time
        return render_template('manage_users.html', title = 'Admin Panel', users = users, time = time )
        # Passing to manage_users.html templete users and time variable
    else:
        abort(403)
        # Display error


@admin.route("/admin_panel/edit_<int:user_id>" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def edit_user(user_id: int):
    # Function that display edit_users.html template when url is /admin_panel/edit_{user_id}
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        user: User = User.query.get_or_404(user_id)
        # Try to find User data in database if not display error 
        form: object = ChangeUserForm()
        # Set form as ChangeUserForm from vibes.forms
        if form.validate_on_submit():
            # Check if submit is correct and edit user data 
            user.fullname: str = form.fullname.data
            user.username: str = form.username.data
            user.email: str = form.email.data
            user.password: str = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.admin_rights: int = form.admin_right.data
            # Set user properties as data from form
            user.category: list = []
            # Clearing user category priviliges
            for category in form.categories.data:
                # Finding Category object from list and append to user category properies
                cat: Category = Category.query.filter_by(name=category).first()
                user.category.append(cat)
            db.session.commit()
            # Saving changes to database
            flash(f'Changes accepted')
            return redirect(url_for('admin.manage_users'))
            # Display message and redirect to manage_users function
        form.fullname.data: str= user.fullname
        form.username.data: str = user.username
        form.email.data: str = user.email
        # Sets form space as current user properties from database
        return render_template('edit_user.html', title = 'Edit User', legend = 'Edit User', current_user = current_user, form = form)
        # Passing to edit_users.html templete user, current_user and form variable
    else:
        abort(403)
        # Display error


@admin.route("/admin_panel/delete_<int:user_id>" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def delete_user(user_id):
    # Function that display delete_users.html template when url is /admin_panel/delete_{user_id}
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        user: User = User.query.get_or_404(user_id)
        # Try to find User data in database if not display error 
        form: object = DeleteUserForm()
        # Set form as DeleteUserForm from vibes.forms
        if form.validate_on_submit():
            # Check if submit is correct and delete user from database also change authors of deleted user articles
            articles_deleted_user: Article = Article.query.filter_by(user_id=user.id).all()
            for article in articles_deleted_user:
                article.user_id = current_user.id
            # Changing article author to prevent erorr on page
            db.session.commit()
            db.session.delete(user)
            db.session.commit()
            flash(f'User deleted from db, also all articles of deleted user has author to admin')
            return redirect(url_for('admin.manage_users'))
            # Display message and redirect to manage_users function
        return render_template('delete_user.html', title = 'Delete User', legend = 'Delete User', form = form)
        # Passing to delete_user.html templete form variable
    else:
        abort(403)
        # Display error


@admin.route("/admin_panel/create_user" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def create_user():
    # Function that display create_user.html template when url is /admin_panel/create_user
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        form = RegisterForm()
        # Set form as RegisterForm from vibes.forms
        if form.validate_on_submit():
            # Check if submit is correct and create user
            user: User = User(fullname = form.fullname.data, username = form.username.data, email = form.email.data, password = bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
            # Sets User object from data provided from form 
            db.session.add(user)
            # Add user to database
            db.session.commit()
            # Save changes to database
            flash(f'Account created succusfully')
            return redirect(url_for('admin.manage_users'))
            # Display message and redirect to manage_users function
        return render_template('create_user.html', title = 'Admin Panel', legend = 'Create User', form = form)
        # Passing to create_user.html templete form variable
    else:
        abort(403)
        # Display error


@admin.route("/admin_panel/manage_article" , methods= ["GET"])
@login_required
# To access this template user need to be log in
def manage_article():
    # Function that display manage_article.html template when url is /admin_panel/manage_article
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        articles: Article = Article.query.all()
        # Create articles variable that contains all Article object 
        time = datetime.utcnow()
        # Create time viarable and set as current time
        return render_template('manage_article.html', title = 'Admin Panel', articles = articles, time = time, user = current_user)
        # Passing to manage_article.html templete article and form variable
    else:
        abort(403)
        # Display error


@admin.route("/admin_panel/create_article" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def create_article():
# Function that display create_article.html template when url is /admin_panel/create_article
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        form: object = CreateArticleForm()
        # Set form as CreateArticleForm from vibes.forms
        if form.validate_on_submit():
            # Check if submit is correct and create user
            if form.image_of_article.data:
                # Check if user filled form.image_of_article
                picture_file: str = save_picture(form.image_of_article.data)
                article: Article = Article(title = form.title.data, image_of_article = picture_file, subtitle = form.subtitle.data, content = form.content.data, source = form.source.data, category_id = Category.query.filter_by(name=form.category.data).first().id , user_id = current_user.id)
                # Save picture on local storage and set article as new Article object with provided through form data                
            else: 
                article = Article(title = form.title.data, subtitle = form.subtitle.data, content = form.content.data, source = form.source.data, category_id = Category.query.filter_by(name=form.category.data).first().id , user_id = current_user.id)
                # Set article as new Article object with provided through form data without image   
            db.session.add(article)
            # Add article to database
            db.session.commit()
            # Saves changes to database
            flash(f'Article added succusfully')
            return redirect(url_for('admin.manage_article'))
            # Display message and redirect to manage_article function
        return render_template('create_article.html', title = 'Admin Panel', legend = 'Create Article', form = form)
        # Passing to manage_article.html templete form variable
    else:
        abort(403)
        # Display error