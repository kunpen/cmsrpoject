from exts import db
from datetime import datetime
class Users(db.Model):
    __tablename__='jq_user'
    uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(50),nullable=False,unique=True)