from datetime import datetime
from vibes.models import User, Category
from flask_login import current_user, login_required
from flask import render_template, url_for, redirect, abort, Blueprint
from vibes.models import User


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500