from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,Length,EqualTo

class LoginForm(FlaskForm):
    username = StringField('Your Username or Email', validators=[Required()])
    password = PasswordField('Your Password',validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('SIGN IN')