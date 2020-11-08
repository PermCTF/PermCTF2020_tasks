from kitties_beta.main import db, User, Post, Path
from werkzeug.security import generate_password_hash

db.create_all()

users = [{"email":"admin@kitties.com","name":"admin","password":"$%hlljbj","posts":[]},
         {"email": "roma@kitties.com","name":"Roma","password":"hfasb$hbfa","posts":[]},
        ]
users[0]["posts"] = [{"name":"Солнышко","image":"1.jpg"},
        {"name":"Мурзик","image":"2.png"},]

users[1]["posts"] = [{"name":"Тимофей","image":"3.jpg"},
        {"name":"Михаил","image":"4.jpg"},]

paths = ["index","login","dobavitkota","PermCTF{Gr4phQL}"]
for user in users:
    new_user = User(email=user["email"], name=user["name"],
                    password=generate_password_hash(user["password"], method='md5'))
    for po in user["posts"]:
        p = Post(name=po["name"],image=po["image"],author=new_user, author_name = user["name"])
        db.session.add(p)
    db.session.add(new_user)
user = {"email": "develop_acc@kitties.com","name":"developer","password":"liverpool", "posts":[]}
new_user = User(email=user["email"], name=user["name"],password=user["password"])
db.session.add(new_user)
for p in paths:
    path = Path(path=p)
    db.session.add(path)
db.session.commit()
