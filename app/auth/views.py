from flask import render_template,url_for,redirect,flash
from . import auth
from .forms import LoginForm,RegisterForm
from ..models import User
from flask_login import login_required
from app import db

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    return render_template('auth/login.html',form=login_form)

@auth.route('/register',methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        user = User(username=username,password=password,email=email)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('.login'))
    flash('Check Your Details!')

    return render_template('auth/register.html',form=register_form, title='Sign Up')
