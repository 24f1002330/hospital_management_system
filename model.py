from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    usertype = db.Column(db.String)