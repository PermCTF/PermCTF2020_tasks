from kitties import db, app
from kitties.models import User, Post

with app.app_context():
    posts = Post.query.filter_by(author_name="developer")
    for p in posts:
        print(p)
        db.session.delete(p)
    db.session.commit()
