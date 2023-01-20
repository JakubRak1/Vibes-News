from flask import url_for
from flask_mail import Message

from vibes import db, mail
from vibes.models import Tokens


def send_reset_email(user):
# Function to create mail content and send it
    token: str = user.get_reset_token()
    # Creates token in variable token based on passed user object
    if not (Tokens.query.filter_by(str_of_token = token)):
    # Check if generated token is already in database
        send_reset_email(user)
        # Re run token generation
    else:
        msg: Message = Message('Password Reset Request', sender = 'noreplay@demo.com', recipients=[user.email])
        msg.body = f''' To reset password visit following link:
{url_for('users.reset_token', token = token, _external = True)}
If you dont request reset password ignore this mail'''
        # Set mail properties as title, sender, reciver and content 
        mail.send(msg)
        # Send mail
        new_token = Tokens(str_of_token = token)
        db.session.add(new_token)
        db.session.commit()
        # Saving used token to database