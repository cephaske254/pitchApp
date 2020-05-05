from flask import render_template,flash,redirect,url_for
from . import main
from flask_login import login_required,current_user
# from app.functions import get_tags
from .forms import PitchForm,TagsForm,CommentForm
from ..models import Pitch,Tags,Comments
from app import db
import markdown2

@main.route('/')
def index():
    tag_list = Tags.get_tags()
    pitches = Pitch.get_pitches()

    title = 'Home'
    return render_template('index.html',title=title,tag_list = tag_list,pitch_list=pitches)

@main.route('/tags', methods=['GET','POST'])
@main.route('/tags/<tag_name>')
def tags(tag_name=None):
    if tag_name:
        pitches = Pitch.get_pitches()
        title = f'Tags #{tag_name}'
        return render_template('tags.html',title = title,tag_name=tag_name,pitch_list=pitches)

    title = 'Category'
    # tag_list = get_tags()
    tag_list = Tags.get_tags()
    form = TagsForm()
    if form.is_submitted():
        name = form.name.data
        tag_name=name.replace(' ','_')
        tag = Tags(name=name,tag=tag_name)
        db.session.add(tag)
        db.session.commit()
        return redirect(url_for('main.tags'))

    return render_template('tags.html',title = title,form = form,tag_list=tag_list,tag_name=tag_name)

@main.route('/new-pitch',methods=['GET','POST'])
@login_required
def new_pitch():
    tag_list = Tags.get_tags()
    form = PitchForm()
    if form.is_submitted():
        if form.content.data:
            user_id = current_user.id
            title = form.title.data
            content = form.content.data
            tag_id = form.tag.data
            published = form.publish.data
            pitch = Pitch(user_id=user_id,title=title,content=content,tag_id=tag_id,published=published)
            db.session.add(pitch)
            db.session.commit()
            flash (f'Post {title} added')
            return redirect('/new-pitch')

    title = 'Add New Pitch'
    return render_template('new_pitch.html',title = title,form = form,tag_list = tag_list)
 
@main.route('/pitch/<int:id>/<filter>',methods=['GET','POST'])
@main.route('/pitch/<int:id>',methods=['GET','POST'])
def pitch(id=None,filter=None):
    pitches = Pitch.get_pitch(id)
    title = f'Single Pitch - {id}'
    comments = Comments.get_comments(id)
    comment_form=CommentForm()
    return render_template('pitch.html',pitch_list=pitches,title=title,comments=comments,comment_form=comment_form)

@main.route('/profile')
def profile():
    pitches = Pitch.get_user_pitches(current_user.id)
    return render_template ('profile/profile.html',title=f'Profile | @{current_user.username}',pitches=pitches)