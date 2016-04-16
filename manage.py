import sys, os

from flask_script import Manager, prompt_bool
from wickr import app
from db import Database

manager = Manager(app)
db = Database(app.config['DATABASE'])

@manager.command
def initdb():
    db.create()
    print("Database created")

@manager.command
def dropdb():
    if prompt_bool("Really drop all rows? (The database will be re-created) y/n"):
        db.clean()
        print("Database cleared")

if __name__ == "__main__":
    manager.run()
