import os

import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database Configs [Check it base on other Database Configuration]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Initialize Database
db = SQLAlchemy(app)


# ------------------  Database Models ------------------

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Post', backref='author')


    def __repr__(self):
        return '<User %r>' % self.email


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    image = db.Column(db.String(1000))
    author_name = db.Column(db.String(1000))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.name

class Path(db.Model):
    __tablename__ = 'developing'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    path = db.Column(db.String(100))

    def __repr__(self):
        return '<Path %r>' % self.path



# ------------------ Graphql Schemas ------------------


# Objects Schema
class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)

class PathObject(SQLAlchemyObjectType):
    class Meta:
        model = Path
        interfaces = (graphene.relay.Node,)

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)
    all_paths = SQLAlchemyConnectionField(PathObject)


# noinspection PyTypeChecker
schema_query = graphene.Schema(query=Query)


# Mutation Objects Schema
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        email = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, email):
        user = User.query.filter_by(email=email).first()
        post = Post(title=title, body=body)
        if user is not None:
            post.author = user
        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)


class Mutation(graphene.ObjectType):
    save_post = CreatePost.Field()


# noinspection PyTypeChecker
schema_mutation = graphene.Schema(query=Query)


# Flask Rest & Graphql Routes
@app.route('/')
def hello_world():
    return 'Hello to graphql app!'


# /graphql-query
app.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema_query, graphiql=True
))

if __name__ == '__main__':
    app.run()

