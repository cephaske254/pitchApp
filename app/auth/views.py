from flask import render_template,url_for,redirect,flash,request
from . import auth
from .forms import LoginForm,RegisterForm
from ..models import User
from flask_login import login_required,login_user,logout_user,current_user
from sqlalchemy import or_
from app import db
from flask_login.mixins import UserMixin

@auth.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('You are logged In')
        return redirect (url_for('main.index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid login details!')

    
    title = 'Login'
    return render_template('auth/login.html',form=login_form,title=title)

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
        return redirect(url_for('.login'))
    return render_template('auth/register.html',form=register_form, title='Sign Up')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Youve been logged out!')
    return redirect(url_for('main.index'))

