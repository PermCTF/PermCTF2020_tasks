from flask import Blueprint, render_template, request, redirect, url_for, flash, render_template_string
from flask_login import login_required, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from . import  db
from .models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)
@main.route('/')
def index():
    posts = Post.query
    return render_template('index.html',posts=posts)

@main.route('/profile')
@login_required
def profile():
    posts = Post.query.filter_by(author_id=current_user.id)
    return render_template('profile.html',posts=posts)

@main.route('/dobavitkota')
@login_required
def dobavitkota():
    return render_template('dobavitkota.html')

@main.route('/dobavitkota', methods=['POST'])
@login_required
def dobavitkota_post():
    name = request.form.get("name")
    if '.' in name or '_' in name or '\'' in name:
        flash('Некорректное имя')
        return redirect(url_for('main.dobavitkota'))
    image = request.form.get("image")
    author_name = current_user.name
    author_id = current_user.id
    new_post = Post(name=name, image=image, author_name = author_name, author_id = author_id)
    db.session.add(new_post)
    db.session.commit()
    template = """
    {{% extends "base.html" %}}
    {{% block content %}}
    <h2>{} was added</h1>
    {{% endblock %}}
    """.format(name)
    return render_template_string(template)
@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if email == "develop_acc@kitties.com":
        if not user or not user.password==password:
            flash('Неверно')
            return redirect(url_for('main.login')) # if the user doesn't exist or password is wrong, reload the page
    elif not user or not check_password_hash(user.password, password):
        flash('Неверно')
        return redirect(url_for('main.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
