# create Condo Model
# create Favorites Model

# (top agents 10% conduct over 90% sales)
# (agents sold nearby properties)


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


db = SQLAlchemy()


likes = db.Table('likes',
    db.Column('lid', db.Integer),
    db.Column('liker', db.Integer, db.ForeignKey('users.uid')),
    db.Column('liked', db.Integer, db.ForeignKey('condos.cid'))
)

# Create class User
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    likes = db.relationship(
        'Condo',
        secondary=likes,
        lazy='dynamic'
    )
    def like(self, condo):
        if not self.is_favorite(condo):
            self.likes.append(condo)
            db.session.commit()
    def unlike(self, condo):
        if self.is_favorite(condo):
            self.likes.remove(condo)
            db.session.commit()
    def is_favorite(self, condo):
        return self.likes.filter(
            likes.c.liked == condo.cid
        ).count() > 0


class Condo(db.Model):
#Create the relationship to the User table
#users = db.relationship(User)
    __tablename__ = 'condos'# Model for the Filter on the site.
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mlsnum = db.Column(db.Integer, nullable=False)
    zip = db.Column(db.String, nullable=False)
    beds = db.Column(db.Integer, nullable=False)
    baths = db.Column(db.Float, nullable=False)
    sqft = db.Column(db.Float, nullable=False)
    listprice = db.Column(db.Float, nullable=False)
    photourl = db.Column(db.String, nullable=False)


    def __init__(self, id):
    	self.id = id

    def __repr__(self):
    	return "Filter Id: {}".format(self.id)


class Photo(db.Model):
    __tablename__ = 'photos'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mlsnum = db.Column(db.Integer, nullable=False)
    imgnum = db.Column(db.Integer, nullable=False)
    features = db.Column(db.String, nullable=False)
