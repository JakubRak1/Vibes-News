from datetime import datetime
from vibes.models import User, Category
from flask_login import current_user, login_required
from flask import render_template, url_for, redirect, abort, Blueprint
from vibes.models import User

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


@editor.route("/editor_panel/manage_users" , methods= ["GET", "POST"])
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
