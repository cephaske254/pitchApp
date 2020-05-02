from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from ..models import User
from wtforms.validators import Required,Email,Length,EqualTo

class LoginForm(FlaskForm):
    username = StringField('Your Username or Email', validators=[Required()])
    password = PasswordField('Your Password',validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('SIGN IN')

class RegisterForm(FlaskForm):
    email = StringField('Email',validators=[Email(),Required()])
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required(),EqualTo('confirm_password',message='Passwords must match!')])
    confirm_password = PasswordField('Confirm password',validators=[Required()])
    agree = BooleanField('Accept T&Cs',validators=[Required()])
    submit = SubmitField('SIGN UP')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email already registered!')

        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username taken!')
    