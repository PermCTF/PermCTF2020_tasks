from flask import Blueprint, render_template, request, redirect, url_for, flash, render_template_string
from flask_login import login_required, current_user
from setup import db
from models import Post


app = Flask(__name__)

app.config['SECRET_KEY'] = 'PermCTF{you_are_cool}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
	return User.query.get(int(user_id))

    # blueprint for auth routes in our app
from .auth import auth as auth_blueprint
 app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)



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
