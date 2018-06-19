from thermos import app, db
from thermos.models import User, Bookmark
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='Name1', email='name1@example.com', password="test"))
    db.session.add(User(username='Name2', email='name2@example.com', password="test"))
    db.session.commit()
    print ('Initialzed the database')

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to losr all your  data"):
        db.drop_all()
        print ('Dropped the database')


if __name__ == '__main__':
    manager.run()