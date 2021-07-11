from flask_script import Manager,Command
from flask_migrate import Migrate
from app import creat_app
from exts import db
from apps.admin import models as admin_models

app=creat_app()
manager=Manager(creat_app)
migrate = Migrate(app, db)

@manager.option('-u','--username',dest='name')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_user(name,password,email):
    user=admin_models.Users(username=name,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print('user add success')
if __name__ == '__main__':
    manager.run()

