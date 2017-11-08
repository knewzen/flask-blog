from config.database import db


class User(db.Model):


    __tablename__ = 'users'


    id = db.Column('id', db.Integer, primary_key=True)
    fullname = db.Column('fullname', db.String)
    username = db.Column('username', db.String)
    password = db.Column('password', db.String)

    def __init__(self,id=None,fullname=None, username=None, password=None):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username