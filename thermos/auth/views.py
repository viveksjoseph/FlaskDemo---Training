from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user

from . import auth
from .. import db, login_manager
from ..models import User
from .forms import LoginForm, SignupForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login View
@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate user
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}".format(user.username))
            # if user is redirected to login page, after login redirect to source page. Else go to index page
            return redirect(request.args.get('next') or url_for('bookmarks.user', username=user.username))
        flash('Incorrect username or password')
    return render_template("Login.html", form=form)

# Logout View
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Signup View
@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome, {}! Please login.'.format(user.username))
        return redirect(url_for('.login'))
    return render_template("signup.html", form=form)