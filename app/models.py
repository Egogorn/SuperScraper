import flask_sqlalchemy
import datetime

db = flask_sqlalchemy.SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    name = db.Column(db.String(100))
    time = db.Column(db.DateTime())
