from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query(int(user_id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('Password Cannot Be Read!')

    @password.setter
    def password(self,password):
        generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
