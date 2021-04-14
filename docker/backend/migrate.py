from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:user@projarka-db/projarka'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'true'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class First(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_text = db.Column(db.String(50))
    sec_text = db.Column(db.String(50))
    something= db.Column(db.String(50))


if __name__ == '__main__':
    manager.run()
