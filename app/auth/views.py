from flask import render_template
from . import auth
from .forms import LoginForm,RegisterForm

@auth.route('/login')
def login():
    login_form = LoginForm()
    return render_template('auth/login.html',form=login_form)

@auth.route('/register')
def register():
    register_form = RegisterForm()
    return render_template('auth/register.html',form=register_form)