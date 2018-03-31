from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Post, User
from app.forms import LoginForm, SubmitPost, Registration
from flask import render_template, flash, redirect
from app import app, db

@app.route('/')
@app.route('/index', methods=['GET'])
@login_required
def index():
    data = request.form
    print('form data', data)
    posts = Post.query.all()
    return render_template('index.html', title="dildosmasher", posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/post', methods=['GET', 'POST'])
def submit_post():
    form = SubmitPost()
    if request.method == 'POST':
        user_post = Post(body=form.new_post.data)
        print('user_post', user_post)
        db.session.add(user_post)
        db.session.commit()
        flash('Your post was successfully submitted')                    
        return redirect(url_for('index'))
    return render_template('submit_post.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Registration()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)