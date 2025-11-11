from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__= 'Users'
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    username = db.Column(db.String, nullable = False)
    dob = db.Column(db.Date, unique = True)
    email = db.Column(db.String, nullable = False , unique = True)
    phoneno = db.Column(db.Integer, unique = True)
    password = db.Column(db.String, nullable = False )


class Departments(db.Model):
    __tableanme__ = 'Departments'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    name = db.Column(db.String , unique = True, nullable = False)
    

    