import os
from flask import render_template, url_for, flash, redirect, abort, Blueprint
from vibes import app, db
from vibes.models import Category, Article
from vibes.articles.forms import ChangeArticleForm, DeleteArticleForm
from vibes.articles.utils import save_picture
from flask_login import current_user, login_required


articles = Blueprint('articles', __name__)


@articles.route("/article_<int:article_id>" , methods = ["GET"])
def article(article_id: int):
    # Function that display article.html template when url is /article_{article_id} 
    current_article: Article = Article.query.get_or_404(article_id)
    # Try to find Article data in database if not display error  
    if (current_user.is_authenticated):
        # Checks if user is loged  
        if(current_user.admin_rights == 2):
            # Checks if loged user is admin, and create variable edit_delete with value of 1 
            edit_delete: int = 1
        elif(current_user.admin_rights == 1 and current_article.category in current_user.category):
            # Checks if loged user is editor, and have category right of article category then create variable edit_delete with value of 1 
            edit_delete: int = 1
        elif(current_user in current_article.author):
            # Checks if loged user is author of article, then create variable edit_delete with value of 1 
            edit_delete: int = 1
        else:
            # If all conditions are not met create variable edit_delete with value of 0 
            edit_delete: int = 0
    else:
        # If user is not login create variable edit_delete with value of 0 
        edit_delete: int = 0
    return render_template('article.html', title = 'Article from', option = edit_delete, article = current_article)
    # Passing to article.html templete edit_delete variable and current_article object


@articles.route("/article/edit_<int:article_id>" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def edit_article(article_id: int):
    # Function that display edit_article.html template when url is /article/edit_{article_id}
    current_article: Article = Article.query.get_or_404(article_id)
    # Try to find Article data in database if not display error 
    if (current_user.is_authenticated and (current_user.admin_rights == 2 or (current_user.admin_rights == 1 and current_user.category in current_article.category) or (current_user in current_article.author))):
        # Checks if logged user have privilege to edit Article
        form: object = ChangeArticleForm()
        # Set form as CreateArticleForm from vibes.forms
        if form.validate_on_submit():
            # Check if submit is correct and edit article data 
            current_article.title: str = form.title.data
            current_article.subtitle: str = form.subtitle.data
            current_article.content: str = form.content.data
            current_article.source: str = form.source.data
            current_article.category_id: int = Category.query.filter_by(name = form.category.data).first().id
            # Set current_article properties as data from form
            if form.image_of_article.data:
                # Check if user filled form.image_of_article
                if (current_article.image_of_article != 'default.png'):
                    # Check if article image is diffrent that default.png
                    delete_file_path = os.path.join(app.root_path, 'static/pics', current_article.image_of_article)
                    os.remove(delete_file_path)
                    # Delete old image form local storage
                picture_file: str = save_picture(form.image_of_article.data)
                current_article.image_of_article: str = picture_file
                # Save picture on local storage and set article pictore property from form data 
            db.session.commit()
            # Saves changes to database
            flash(f'Changes accepted')
            return redirect(url_for('articles.article', article_id = current_article.id))
            # Display message and redirect to article function
        form.title.data = current_article.title
        form.subtitle.data = current_article.subtitle
        form.content.data = current_article.content
        form.source.data = current_article.source
        # Sets form space as current user properties from database
        return render_template('edit_article.html', title = 'Edit Article', legend = 'Edit Article', form = form)
        # Passing to edit_article.html templete form variable
    else:
        abort(403)
        # Display error


@articles.route("/article/delete_<int:article_id>" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def delete_article(article_id: int):
    # Function that display delete_article.html template when url is /article/delete_{article_id}
    current_article = Article.query.get_or_404(article_id)
    # Try to find Article data in database if not display error 
    if (current_user.is_authenticated and (current_user.admin_rights == 2 or (current_user.admin_rights == 1 and current_user.category in current_article.category) or (current_user in current_article.author))):
        # Checks if logged user have privilege to edit Article
        form: object = DeleteArticleForm()
         # Set form as CreateArticleForm from vibes.forms
        if form.validate_on_submit():
            # Check if submit is correct and delete article from database 
            if (current_article.image_of_article != 'default.png'):
                # Check if article image is diffrent that default.png
                delete_file_path = os.path.join(app.root_path, 'static/pics', current_article.image_of_article)
                os.remove(delete_file_path)
                # Delete old image form local storage
            db.session.delete(current_article)
            # Delete current_article from database
            db.session.commit()
            # Saves changes to database
            flash(f'Article deleted from db')
            return redirect(url_for('main.home'))
            # Display message and redirect to home function
        return render_template('delete_user.html', title = 'Delete Article', legend = 'Delete Article', form = form)
        # Passing to delete_article.html templete form variable
    else:
        abort(403)
        # Display error