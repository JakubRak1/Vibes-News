from datetime import datetime

from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from vibes import bcrypt, db
from vibes.articles.utils import save_picture
from vibes.models import Article, Category, User
from vibes.user.forms import ChangeUserFormEditor, CreateArticleForm

user = Blueprint('user', __name__)

@user.route("/user_panel")
@login_required
# To access this template user need to be log in
def user_panel():
    # Function that display admin_panel.html template when url is /admin_panel
    if (current_user.is_authenticated and current_user.admin_rights == 0):
        # Checks if current user object have editor privilige
        return render_template('admin_panel.html', title = 'Account Panel', user = current_user)
        # Passing to admin_panel.html templete user variable
    else:
        return redirect(url_for('main.home'))
        # Redirect to home function


@user.route("/user_panel/manage_article" , methods= ["GET"])
@login_required
def manage_article_user():
    # Function that display manage_article.html template when url is /editor_panel/manage_article
    if (current_user.is_authenticated and current_user.admin_rights == 0):
        # Checks if current user object have admin privilige
        user_articles: list = db.session.query(Article).filter(Article.user_id == current_user.id).all()
        time = datetime.utcnow()
        return render_template('manage_article.html', title = 'User Panel', articles = user_articles, time = time, user = current_user)
        # Passing to manage_article.html templete articles variables
    else:
        abort(403)
        # Display error


@user.route("/user_panel/create_article" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def create_article():
# Function that display create_article.html template when url is /admin_panel/create_article
    if (current_user.is_authenticated and current_user.admin_rights == 0):
        # Checks if current user object have admin privilige
        categories_of_user: list = []
        for category in current_user.category:
            categories_of_user.append(category)
        form: object = CreateArticleForm()
        form.category.choices = [(cat.name, cat.name) for cat in categories_of_user]
        if form.validate_on_submit():
            # Check if submit is correct and create user
            if form.image_of_article.data:
                # Check if user filled form.image_of_article
                picture_file: str = save_picture(form.image_of_article.data)
                article: Article = Article(title = form.title.data, image_of_article = picture_file, subtitle = form.subtitle.data, content = form.content.data, source = form.source.data, category_id = db.session.query(Category).filter_by(name=form.category.data).first().id , user_id = current_user.id)
                # Save picture on local storage and set article as new Article object with provided through form data                
            else: 
                article = Article(title = form.title.data, subtitle = form.subtitle.data, content = form.content.data, source = form.source.data, category_id = db.session.query(Category).filter_by(name=form.category.data).first().id , user_id = current_user.id)
                # Set article as new Article object with provided through form data without image   
            db.session.add(article)
            # Add article to database
            db.session.commit()
            # Saves changes to database
            flash(f'Article added succusfully', 'text-success')
            return redirect(url_for('user.manage_article_user'))
            # Display message and redirect to manage_article function
        return render_template('create_article.html', title = 'USer Panel', legend = 'Create Article', form = form)
        # Passing to manage_article.html templete form variable
    else:
        abort(403)
        # Display error


@user.route("/edit_account", methods = ["GET", "POST"])
@login_required
def edit_account():
    user: User = db.session.query(User).get_or_404(current_user.id)
    # Function that display set_password.html template when url is /reset_password/{token}
    if current_user.is_authenticated and current_user.admin_rights != 2:
        # Check if user is already login and its not admin
        form: object = ChangeUserFormEditor()
        if form.validate_on_submit():
            # Check if submit is correct and edit user data 
            user.fullname: str = form.fullname.data
            user.username: str = form.username.data
            user.email: str = form.email.data
            # Set user properties as data from form
            # Clearing user category priviliges
            db.session.commit()
            # Saving changes to database
            flash(f'Account edited and saved changes', 'text-success')
            if (current_user.admin_rights == 1):
                return redirect(url_for('editor.editor_panel'))
            elif(current_user.admin_rights == 0):
                return redirect(url_for('user.user_panel'))
            # Display message and redirect to manage_users_editor function
        form.fullname.data: str= user.fullname
        form.username.data: str = user.username
        form.email.data: str = user.email
        # Sets form space as current user properties from database
        return render_template('edit_account.html', title = 'Edit Account', legend = 'Edit Account', current_user = current_user, form = form)
        # Passing to edit_users.html templete user, current_user and form variable
    else:
        abort(403)
        # Display error