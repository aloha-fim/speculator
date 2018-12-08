# create Condo Model
# create Favorites Model

# (top agents 10% conduct over 90% sales)
# (agents sold nearby properties)


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



db = SQLAlchemy()

# Create class User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
    	self.username = username
    	self.password = generate_password_hash(password)

    def check_password(self,password):
    	return check_password_hash(self.password,password)

    def followed_posts(self):
    	followed_posts = Condo.query.join(likes,(likes.c.following == Condo.mlsnum)).filter(likes.c.follower == self.id)
    	return followed_posts

class Condo(db.Model):
#Create the relationship to the User table
#users = db.relationship(User)
		__tablename__ = 'condos'
		#Create the relationship to the User table
		#users = db.relationship(User)
	  # Model for the Condo on the site.
		id = db.Column(db.Integer, autoincrement=True)
		mlsnum = db.Column(db.Integer, primary_key=True, autoincrement=False)
		list_price = db.Column(db.Integer, nullable=False)
		zip = db.Column(db.Integer, nullable=False)
		sqft = db.Column(db.Integer, nullable=False)
		beds = db.Column(db.Integer, nullable=False)
		baths = db.Column(db.Integer, nullable=False)
		photourl = db.Column(db.String, nullable=False)
    #username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)


		def __init__(self, id):
			self.id = id

		def __repr__(self):
			return "Filter Id: {}".format(self.id)

		def is_following(self, condo):
			return self.followed.filter(likes.c.following == condo.mlsnum).count() > 0

		def follow(self, condo):
			if not self.is_following(condo):
				self.followed.append(condo)

		def unfollow(self, condo):
			if self.is_following(condo):
				self.followed.remove(condo)

class Like(db.Model):
	#Create the relationship to the User table
	#users = db.relationship(User)

	__tablename__ = 'likes'
	fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	follower = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	following = db.Column(db.Integer, db.ForeignKey('condos.mlsnum'), nullable=False)

