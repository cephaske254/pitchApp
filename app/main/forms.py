from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from ..models import Tags
from flask_login import current_user

class TagsForm(FlaskForm):
    name = StringField('Tag Name')
    user_id = StringField('UserId',default=current_user.id)
