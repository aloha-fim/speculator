# create Condo Model
# create Favorites Model

# (top agents 10% conduct over 90% sales)
# (agents sold nearby properties)


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


db = SQLAlchemy()

# Create class User
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Condo(db.Model):
#Create the relationship to the User table
#users = db.relationship(User)
		__tablename__ = 'condos'
		# Model for the Post on the site.
		id = db.Column(db.Integer, autoincrement=True)
		mlsnum = db.Column(db.Integer, primary_key=True, autoincrement=False)
        list_price = db.Column(db.Integer, nullable=False)
		zip = db.Column(db.Integer, nullable=False)
		beds = db.Column(db.Integer, nullable=False)
		baths = db.Column(db.Integer, nullable=False)
		sqft = db.Column(db.Integer, nullable=True)photo_url = db.Column(db.String, nullable=False)

		def __init__(self, mlsnum):
			self.mlsnum = mlsnum

		def __repr__(self):
			return "Condo Id: {}".format(self.id)

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mlsnum = db.Column(db.Integer, nullable=False)
    imgnum = db.Column(db.Integer, nullable=False)
    features = db.Column(db.Text, nullable=False)
