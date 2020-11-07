from kitties import db, app
from werkzeug.security import generate_password_hash

from kitties.models import User, Post

with app.app_context():
    db.create_all()

    users = [{"email":"admin@kitties.com","name":"admin","password":"$%hlljbj","posts":[]},
             {"email": "roma@kitties.com","name":"Roma","password":"hfasb$hbfa","posts":[]},
             {"email": "develop_acc@kitties.com","name":"developer","password":"s3cur3d", "posts":[]},
            ]
    users[0]["posts"] = [{"name":"Солнышко","image":"1.jpg"},
            {"name":"Мурзик","image":"2.png"},]

    users[1]["posts"] = [{"name":"Тимофей","image":"3.jpg"},
                         {"name":"Михаил","image":"4.jpg"},]

    for user in users:
        new_user = User(email=user["email"], name=user["name"],
                        password=generate_password_hash(user["password"], method='sha256'))
        for po in user["posts"]:
            p = Post(name=po["name"],image=po["image"],author=new_user, author_name = user["name"])
            db.session.add(p)
        db.session.add(new_user)
    db.session.commit()
