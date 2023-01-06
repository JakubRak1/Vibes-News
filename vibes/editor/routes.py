from datetime import datetime

from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from vibes import bcrypt, db
from vibes.articles.utils import save_picture
from vibes.editor.forms import ChangeUserFormEditor, CreateArticleForm
from vibes.models import Article, Category, User

editor = Blueprint('editor', __name__)


@editor.route("/editor_panel")
@login_required
# To access this template user need to be log in
def editor_panel():
    # Function that display admin_panel.html template when url is /admin_panel
    if (current_user.is_authenticated and current_user.admin_rights == 1):
        # Checks if current user object have editor privilige
        return render_template('admin_panel.html', title = 'Editor Panel', user = current_user)
        # Passing to admin_panel.html templete user variable
    else:
        return redirect(url_for('main.home'))
        # Redirect to home function


@editor.route("/editor_panel/manage_users" , methods= ["GET"])
@login_required
# To access this template user need to be log in
def manage_users_editor():
    # Function that display manage_users.html template when url is /manage_users
    if (current_user.is_authenticated and current_user.admin_rights == 1):
        # Checks if current user object have editor privilige
        users: list = []
        # Create users variable as empty list
        for category in current_user.category:
            users_cat: list[User] = User.query.filter(User.category.any(Category.name == category.name), User.admin_rights == 0).all()
            users += users_cat
        time: object = datetime.utcnow()
        # Create time viarable and set as current time
        return render_template('manage_users.html', title = 'Editor Panel', users = users, current_user = current_user, time = time )
        # Passing to manage_users.html templete users, current_user and time variable
    else:
        abort(403)
        # Display error


@editor.route("/editor_panel/edit_<int:user_id>" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def edit_user_editor(user_id: int):
    # Function that display edit_users.html template when url is /admin_panel/edit_{user_id}
    user: User = User.query.get_or_404(user_id)
    # Try to find User data in database if not display error
    if (current_user.is_authenticated and current_user.admin_rights == 1 and user.category[0] in current_user.category):
        # Checks if current user object have admin privilige
        categories_of_editor: list = []
        for category in current_user.category:
            categories_of_editor.append(category)
        form: object = ChangeUserFormEditor()
        # Set form as ChangeUserForm from vibes.forms
        form.categories.choices = [(cat.name, cat.name) for cat in categories_of_editor]
        # Set choises of SelectMultipleField from current_user category
        if form.validate_on_submit():
            # Check if submit is correct and edit user data 
            user.fullname: str = form.fullname.data
            user.username: str = form.username.data
            user.email: str = form.email.data
            user.admin_rights: int = 0
            user.password: str = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
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
            return redirect(url_for('editor.manage_users_editor'))
            # Display message and redirect to manage_users_editor function
        form.fullname.data: str= user.fullname
        form.username.data: str = user.username
        form.email.data: str = user.email
        # Sets form space as current user properties from database
        return render_template('edit_user.html', title = 'Edit User', legend = 'Edit User', current_user = current_user, form = form)
        # Passing to edit_users.html templete user, current_user and form variable
    else:
        abort(403)
        # Display error


@editor.route("/editor_panel/manage_article" , methods= ["GET"])
@login_required
def manage_article_editor():
    # Function that display manage_article.html template when url is /editor_panel/manage_article
    if (current_user.is_authenticated and current_user.admin_rights == 1):
        # Checks if current user object have admin privilige
        editor_articles: list = []
        for category in current_user.category:
            article_cat: list[Article] = Article.query.filter(Article.category_id == category.id).all()
            editor_articles += article_cat #To fix all articles is showing
        time = datetime.utcnow()
        return render_template('manage_article.html', title = 'Editor Panel', articles = editor_articles, time = time, user = current_user)
        # Passing to manage_article.html templete articles variables
    else:
        abort(403)
        # Display error


@editor.route("/editor_panel/create_article" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def create_article():
# Function that display create_article.html template when url is /admin_panel/create_article
    if (current_user.is_authenticated and current_user.admin_rights == 1):
        # Checks if current user object have admin privilige
        categories_of_editor: list = []
        for category in current_user.category:
            categories_of_editor.append(category)
        form: object = CreateArticleForm()
        form.category.choices = [(cat.name, cat.name) for cat in categories_of_editor]
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
            return redirect(url_for('editor.manage_article_editor'))
            # Display message and redirect to manage_article function
        return render_template('create_article.html', title = 'Editor Panel', legend = 'Create Article', form = form)
        # Passing to manage_article.html templete form variable
    else:
        abort(403)
        # Display error