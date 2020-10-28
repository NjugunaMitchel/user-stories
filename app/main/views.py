from flask import render_template, request, redirect, url_for, flash
from . import main
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required,current_user
from ..auth.forms import RegistrationForm,Login,updateAccount,postForm
from ..models import User,Post
from app import db, login_manager

@main.route('/')
@login_required
def index():
    title = 'Pitch'
    posts =Post.query.all( )
    return render_template('index.html', title = title, post=posts)

@main.route('/pitch', methods=['GET','POST'])
@login_required
def new_post():
    form =postForm()
    if form.validate_on_submit():
        post = post(title = form.title.data, content = form.content.data, author = current_user) 
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_post.html', title = 'Pitch', form= form )



@main.route('/account')
@login_required
def account():
    form = updateAccount()
    profile_photo = url_for('static',filename='prof/' + User.profile_photo)
    return render_template('account.html',profile_photo = profile_photo, form= form)