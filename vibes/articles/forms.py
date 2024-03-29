from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (BooleanField, SelectField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import Length, ValidationError, data_required

from vibes import db
from vibes.models import Article, Category


class ChangeArticleForm (FlaskForm):
    # Constructor of Change article form
    title = StringField('Title of Article', validators=[data_required(), Length(min = 2, max = 255)])
    image_of_article = FileField('Main image of Article', validators=[FileAllowed(['jpg', 'png'])])
    subtitle = TextAreaField('Subtitle', validators=[data_required()])
    content = TextAreaField('Content', validators=[data_required()])
    source = StringField('Source', validators=[data_required(), Length(min = 2, max = 255)])
    category = SelectField('Categories', choices=[(c.name, c.name) for c in db.session.query(Category).all()])
    submit = SubmitField('Change Article')


    def validate_title(self, title):
        # Function to verify if new variable title exist in database
        article: Article = db.session.query(Article).filter_by(title = title.data).first()
        # If in database there is Article with variable title, article variable contains Article object and if not variable is None  
        if article and (title!=self.title):
            # Check if article is object and check if title variable is not changed
            raise ValidationError ('There is already Article with this title')


class DeleteArticleForm (FlaskForm):
    # Constructor of Delete article form
    aprove = BooleanField('Are you sure you want to delete Article?', validators=[data_required()])
    submit = SubmitField('Delete Article')