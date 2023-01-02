from datetime import datetime
from vibes.models import User, Category, Article
from vibes import db, bcrypt
from flask_login import current_user, login_required
from flask import render_template, url_for, redirect, flash, Blueprint, abort
from vibes.user.forms import ChangeUserFormEditor



user = Blueprint('user', __name__)

@user.route("/edit_account", methods = ["GET", "POST"])
@login_required
def edit_account():
    user: User = User.query.get_or_404(current_user.id)
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
            flash(f'Account Edited')
            if (current_user.admin_rights == 1):
                return redirect(url_for('editor.manage_users_editor'))
            elif(current_user.admin_rights == 0):
                return 'to Change'
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