from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    name1 = User(username='Name1', email='name1@example.com', password="test")
    db.session.add(name1)
    db.session.add(User(username='Name2', email='name2@example.com', password="test"))

    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description, user=name1, tags=tags))

    for name in ["python", "webdev", "programming", "databases"]:
        db.session.add(Tag(name=name))

    db.session.commit()

    add_bookmark("http://www.pluralsight.com", "Pluralsight", "programming, python")
    add_bookmark("http://www.python.org", "Python", "python")

    db.session.commit()

    print ('Initialzed the database')

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your  data"):
        db.drop_all()
        print ('Dropped the database')


if __name__ == '__main__':
    manager.run()