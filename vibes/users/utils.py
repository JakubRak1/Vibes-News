from flask import url_for
from vibes import mail
from flask_mail import Message


def send_reset_email(user):
# Function to create mail content and send it
    token: str = user.get_reset_token()
    # Creates token in variable token based on passed user object
    msg: Message = Message('Password Reset Request', sender = 'noreplay@demo.com', recipients=[user.email])
    msg.body = f''' To reset password visit following link:
{url_for('users.reset_token', token = token, _external = True)}
If you dont request reset password ignore this mail'''
    # Set mail properties as title, sender, reciver and content 
    mail.send(msg)
    # Send mail