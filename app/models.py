from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
import markdown2


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String())
    profile_pic = db.Column(db.String(),default='avatar.png')
    pitches = db.relationship('Pitch', backref='user')
    comments = db.relationship('Comments', backref='user')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_user(cls,id):
        return User.query.get(id)
    def __repr__(self):
        return f'{self}'


class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    tag = db.Column(db.String(255))
    pitch_names = db.relationship('Pitch', backref='pitch_object')

    @classmethod
    def get_tags(cls):
        tags = Tags.query.all()
        return tags


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    published = db.Column(db.String())

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        for pitch in pitches:
            pitch.content = markdown2.markdown(pitch.content,extras=["code-friendly", "fenced-code-blocks"])
        return pitches
    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(id=id).all()
        for pitch in pitches:
            pitch.content = markdown2.markdown(pitch.content,extras=["code-friendly", "fenced-code-blocks"])
        return pitches

    @classmethod
    def get_user_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        for pitch in pitches:
            pitch.content = markdown2.markdown(pitch.content,extras=["code-friendly", "fenced-code-blocks"])
        return pitches

    @classmethod
    def get_pitches_by_tag(cls,tag_name):
        tag_id = Tags.query.filter_by(tag=tag_name).first()
        pitches = Pitch.query.filter_by(tag_id=tag_id.id).all()
        for pitch in pitches:
            pitch.content = markdown2.markdown(pitch.content,extras=["code-friendly", "fenced-code-blocks"])
        return pitches

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.ForeignKey('pitches.id'))
    user_id = db.Column(db.ForeignKey('users.id'))
    content = db.Column(db.String(255))

    @classmethod
    def get_comments(cls,id):
        return Comments.query.filter_by(pitch_id=id).all()

    def __repr__(self):
        return self

