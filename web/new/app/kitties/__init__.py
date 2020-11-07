from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()

# init SQLAlchemy so we can use it later in our models

app = Flask(__name__)

app.config['SECRET_KEY'] = 'PermCTF{you_are_cool}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.init_app(app)
from .models import User

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

