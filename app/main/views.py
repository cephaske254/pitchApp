from flask import render_template,flash,redirect,url_for,request
from . import main
from flask_login import login_required,current_user
# from app.functions import get_tags
from .forms import PitchForm,TagsForm,CommentForm
from ..models import Pitch,Tags,Comments,User
from app import db,photos
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
 
@main.route('/pitch/<int:id>',methods=['GET','POST'])
def pitch(id=None):
    pitches = Pitch.get_pitch(id)
    for pitch in pitches:
        title = f'Pitch {pitch.title}'
    comments = Comments.get_comments(id)
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        content = comment_form.content.data
        user_id = current_user.id
        pitch_id = id
        comment = Comments(pitch_id=pitch_id,user_id=user_id,content=content)
        db.session.add(comment)
        db.session.commit()


    return render_template('pitch.html',pitch_list=pitches,title=title,comments=comments,comment_form=comment_form)

@main.route('/profile')
@login_required
def profile():
    pitches = Pitch.get_user_pitches(current_user.id)
    return render_template ('profile/profile.html',title=f'Profile | @{current_user.username}',pitches=pitches)

@main.route('/profile/update_photo',methods= ['POST','PUT'])
@login_required
def change_photo():
    user = User.query.filter_by(id = current_user.id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        user.profile_pic = filename
        print(filename)
        db.session.commit()
    return redirect(url_for('main.profile'))