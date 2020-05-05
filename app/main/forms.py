from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField,BooleanField
from ..models import Tags
from wtforms.validators import Required,Length,EqualTo
from flask_login import current_user

class TagsForm(FlaskForm):
    name = StringField('Tag Name')
    user_id = StringField('UserId',default=1)

class PitchForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    tag = SelectField('Tag',validators=[])
    content = TextAreaField('Content')
    publish = BooleanField('Publish Now')
    submit = SubmitField('Add')

class CommentForm(FlaskForm):
    content = StringField()
    
