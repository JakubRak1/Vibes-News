from datetime import datetime
import os
import secrets
from flask import render_template, url_for, flash, redirect, request, abort
from vibes import app, db, bcrypt, mail
from vibes.models import User, Category, Article
from vibes.forms import LoginForm, RequestResetForm, ContactAdminFrom, RegisterForm, ChangeUserForm, DeleteUserForm, ResetPasswordForm, CreateArticleForm, ChangeArticleForm, DeleteArticleForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/")
@app.route("/home")
def home():
    # Function that display home.html template when url is /home or empty 
    return render_template('home.html', title = 'Vibes News')


@app.route("/about")
def about():
    # Function that display about.html template when url is /about 
    return render_template('about.html', title = 'About Us')


@app.route("/article_<int:article_id>" , methods = ["GET"])
def article(article_id: int):
    # Function that display article.html template when url is /article_{article_id} 
    current_article: Article = Article.query.get_or_404(article_id)
    # Try to find Article data in database if not display error  
    if (current_user.is_authenticated):
        # Checks if user is loged  
        if(current_user.admin_rights == 2):
            # Checks if loged user is admin, and create variable edit_delete with value of 1 
            edit_delete: int = 1
        elif(current_user.admin_rights == 1 and current_user.category in current_article.category):
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


@app.route("/login", methods = ["GET", "POST"])
def login():
    # Function that display login.html template when url is /login
    if current_user.is_authenticated:
        # Check if user is already login if its true redirects to home function
        return redirect(url_for('home'))
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
            return redirect(next_page) if next_page else redirect(url_for('home'))
            # Redirect to page that required login
        else:
            flash(f'Login Unsuccusefully, check email and password again')
            # Display error message
    return render_template('login.html', title = 'Log In', legend = 'Log In', form = form)
    # Passing to article.html templete form variable


@app.route("/logout", methods = ["GET", "POST"])
@login_required 
# To acces this template user need to be log in
def logout():
    # Function that logout user and redirecting to home function 
    logout_user()
    return redirect(url_for('home'))


def send_reset_email(user):
# Function to create mail content and send it
    token: str = user.get_reset_token()
    # Creates token in variable token based on passed user object
    msg: Message = Message('Password Reset Request', sender = 'noreplay@demo.com', recipients=[user.email])
    msg.body = f''' To reset password visit following link:
{url_for('reset_token', token = token, _external = True)}
If you dont request reset password ignore this mail'''
    # Set mail properties as title, sender, reciver and content 
    mail.send(msg)
    # Send mail


@app.route("/reset_password", methods = ["GET", "POST"])
def reset_password():
    # Function that display reset_password.html template when url is /reset_password
    if current_user.is_authenticated:
        # Check if user is already login if its true redirects to home function
        return redirect(url_for('home'))
    form: object = RequestResetForm()
    # Set form as RequestResetForm from vibes.forms
    if form.validate_on_submit():
        # Check if submit is correct and checks if User object exist in database with provided email 
        user: User = User.query.filter_by(email = form.email.data).first()
        if user:
            # Check if user is object and runs function send_reset_email with user object
            send_reset_email(user)
            flash(f'Email with reset link sent to {form.email.data}', 'succsess')
            return redirect(url_for('login'))
        else:
            flash(f'There is no account with email: {form.email.data}')
            # Display error message
    return render_template('reset_password.html', title = 'Reset Password', legend = 'Reset Password', form = form)
    # Passing to reset_password.html templete form variable


@app.route("/reset_password/<token>", methods = ["GET", "POST"])
def reset_token(token):
    # Function that display set_password.html template when url is /reset_password/{token}
    if current_user.is_authenticated:
        # Check if user is already login if its true redirects to home function
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None: 
        # Check if token was invalid
        flash('Thats its invalid token or its expired')
         # Display error message
        return redirect(url_for('reset_password'))
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
        return redirect(url_for('login'))
        # After successfully changing password redirecting to login function
    return render_template('set_password.html', title = 'Set Password', legend = 'Set Password', form = form )
    # Passing to set_password.html templete form variable


@app.route("/request", methods = ["GET", "POST"])
def contact_admin():
    # Function that display contact.html template when url is /request
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
        return redirect(url_for('home'))
        # Display message and redirect to home function
    return render_template('contact.html', title = 'Log In', legend = 'Contact with Us', form = form)
    # Passing to contact.html templete form variable


@app.route("/admin_panel")
@login_required
# To access this template user need to be log in
def admin_panel():
    # Function that display admin_panel.html template when url is /admin_panel
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        return render_template('admin_panel.html', title = 'Admin Panel')
    else:
        return redirect(url_for('home'))
        # Redirect to home function


@app.route("/admin_panel/manage_users" , methods= ["GET", "POST"])
@login_required
# To access this template user need to be log in
def manage_users():
    # Function that display manage_users.html template when url is /manage_users
    if (current_user.is_authenticated and current_user.admin_rights == 2):
        # Checks if current user object have admin privilige
        editors: list[User] = User.query.filter_by(admin_rights = 1).all()
        users: list[User] = User.query.filter_by(admin_rights = 0).all()
        all_users: list[User] = editors + users
        # Create all_users variable that contains all users and editors object 
        time: object = datetime.utcnow()
        # Create time viarable and set as current time
        return render_template('manage_users.html', title = 'Admin Panel', users = all_users, time = time )
        # Passing to manage_users.html templete users and time variable
    else:
        abort(403)
        # Display error


@app.route("/admin_panel/edit_<int:user_id>" , methods= ["GET", "POST"])
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
            return redirect(url_for('manage_users'))
            # Display message and redirect to manage_users function
        form.fullname.data: str= user.fullname
        form.username.data: str = user.username
        form.email.data: str = user.email
        # Sets form space as current user properties from database
        return render_template('edit_user.html', title = 'Edit User', legend = 'Edit User', user = user, form = form)
        # Passing to edit_users.html templete user and form variable
    else:
        abort(403)
        # Display error


@app.route("/admin_panel/delete_<int:user_id>" , methods= ["GET", "POST"])
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
            # Check if submit is correct and delete user from database 
            db.session.delete(user)
            # Dele user object from database
            db.session.commit()
            # Saving changes to database
            flash(f'User deleted from db')
            return redirect(url_for('manage_users'))
            # Display message and redirect to manage_users function
        return render_template('delete_user.html', title = 'Delete User', legend = 'Delete User', form = form)
        # Passing to delete_user.html templete form variable
    else:
        abort(403)
        # Display error


@app.route("/admin_panel/create_user" , methods= ["GET", "POST"])
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
            return redirect(url_for('manage_users'))
            # Display message and redirect to manage_users function
        return render_template('create_user.html', title = 'Admin Panel', legend = 'Create User', form = form)
        # Passing to create_user.html templete form variable
    else:
        abort(403)
        # Display error


@app.route("/admin_panel/manage_article" , methods= ["GET", "POST"])
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
        return render_template('manage_article.html', title = 'Admin Panel', articles = articles, time = time)
        # Passing to manage_article.html templete article and form variable
    else:
        abort(403)
        # Display error


def save_picture(form_image) -> str:
    # Function that allow save provided in form_image image in local storage
    random_hex: str = secrets.token_hex(8)
    # Set variable random_hex as string of random created token
    _, f_ext = os.path.splitext(form_image.filename)
    picture_fn: str = random_hex + f_ext
    # Set picture_fn as sum of random_hex and file extension
    picture_path: str = os.path.join(app.root_path, 'static/pics', picture_fn)
    # Set picture_path as sum of app.root_path , 'static/pics' and picture_fn
    form_image.save(picture_path)
    return picture_fn
    # Saving picture on local storage and returns picture_fn


@app.route("/admin_panel/create_article" , methods= ["GET", "POST"])
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
            return redirect(url_for('manage_article'))
            # Display message and redirect to manage_article function
        return render_template('create_article.html', title = 'Admin Panel', legend = 'Create Article', form = form)
        # Passing to manage_article.html templete form variable
    else:
        abort(403)
        # Display error


@app.route("/article/edit_<int:article_id>" , methods= ["GET", "POST"])
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
            return redirect(url_for('article', article_id = current_article.id))
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


@app.route("/article/delete_<int:article_id>" , methods= ["GET", "POST"])
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
            return redirect(url_for('home'))
            # Display message and redirect to home function
        return render_template('delete_user.html', title = 'Delete Article', legend = 'Delete Article', form = form)
        # Passing to delete_article.html templete form variable
    else:
        abort(403)
        # Display error
