from flask import render_template, Blueprint


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # Function that display home.html template when url is /home or empty 
    return render_template('home.html', title = 'Vibes News')


@main.route("/about")
def about():
    # Function that display about.html template when url is /about 
    return render_template('about.html', title = 'About Us')
