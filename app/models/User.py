from config.database import db


class User(db.Model):


    __tablename__ = "users"


    id = db.Column('id', db.Integer, primary_key=True)
    fullname = db.Column('fullname', db.String)