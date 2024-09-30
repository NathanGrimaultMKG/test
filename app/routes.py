from flask import render_template, redirect, url_for, flash
from app import db
from app.models import User, Post
from app.forms import LoginForm, PostForm
from flask import current_app as app

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logique de connexion (simplifiée)
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash(f'Logged in as {user.username}', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=1)  # Placeholder for user ID
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)
