from exts import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
class Users(db.Model):
    __tablename__='jq_user'
    uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    _password=db.Column(db.String(100),nullable=False)
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw_passwword):
        self._password=generate_password_hash(raw_passwword)


    def check_password(self,raw_password):
        result=check_password_hash(self.password,raw_password)
        return result



