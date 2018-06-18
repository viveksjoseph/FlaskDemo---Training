from flask import render_template, url_for, redirect, flash, request
from flask_login import login_required, login_user, logout_user, current_user

from thermos import app, db, login_manager
from thermos.forms import BookmarkForm, LoginForm, SignupForm
from thermos.models import User, Bookmark

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Basic View
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks = Bookmark.newest(5))

# Bookmarks View
@app.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user = current_user, url = url, description = description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored bookmark '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form = form)

# User View
@app.route('/user/<username>')
def user(username):
    #if user exists return user page else show 404 error
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

# Login View
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate user
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}".format(user.username))
            # uf user is redirected to login page, after login redirect to source page. Else go to index page
            return redirect(request.args.get('next') or url_for('user', username=user.username))
        flash('Incorrect username or password')
    return render_template("Login.html", form=form)

# Logout View
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Signup View
@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome, {}! Please login.'.format(user.username))
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)

# 401 error page
@app.errorhandler(401)
def page_not_authorized(e):
    return render_template('401.html'), 401

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500 error page
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500