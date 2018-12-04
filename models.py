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
    uid = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(64), primary_key=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
	  # connecting table Filter to a User table
	  filters = db.relationship('Filter',backref='author',lazy=True)


class Filter(db.Model):
#Create the relationship to the User table
#users = db.relationship(User)
		__tablename__ = 'filters'
		#Create the relationship to the User table
	  users = db.relationship(User)
		# Model for the Filter on the site.
		id = db.Column(db.Integer, autoincrement=True)
		zip = db.Column(db.Integer, nullable=False)
		beds = db.Column(db.Integer, nullable=False)
		baths = db.Column(db.Integer, nullable=False)
		photourl = db.Column(db.String, nullable=False)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)


		def __init__(self, id):
			self.id = id

		def __repr__(self):
			return "Filter Id: {}".format(self.id)

