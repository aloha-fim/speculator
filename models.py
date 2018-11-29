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
class User(db.Model):
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
		display_y = db.Column(db.Numeric, nullable=True)
		display_x = db.Column(db.Numeric, nullable=True)
		status = db.Column(db.String, nullable=False)
		list_price = db.Column(db.Integer, nullable=False)
		sold_price = db.Column(db.Integer, nullable=False)
		list_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
		sold_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
		expired_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
		dom = db.Column(db.Integer, nullable=False)
		dto = db.Column(db.Integer, nullable=False)
		address = db.Column(db.String, nullable=False)
		city = db.Column(db.String, nullable=False)
		state = db.Column(db.String, nullable=False)
		zip = db.Column(db.Integer, nullable=False)
		area = db.Column(db.Integer, nullable=False)
		beds = db.Column(db.Integer, nullable=False)
		baths = db.Column(db.Integer, nullable=False)
		age = db.Column(db.Integer, nullable=False)
		lot_size = db.Column(db.Integer, nullable=False)
		agent_name = db.Column(db.String, nullable=False)
		office_name = db.Column(db.String, nullable=False)
		office_phone = db.Column(db.String, nullable=False)
		showing_instructions = db.Column(db.String, nullable=False)		
		remarks = db.Column(db.String, nullable=False)
		style = db.Column(db.String, nullable=False)
		level = db.Column(db.String, nullable=False)
		garage = db.Column(db.String, nullable=False)
		heating = db.Column(db.String, nullable=False)
		cooling = db.Column(db.String, nullable=False)
		elementary_school = db.Column(db.String, nullable=False)
		junior_high_school = db.Column(db.String, nullable=False)
		high_school = db.Column(db.String, nullable=False)
		other_features = db.Column(db.String, nullable=False)
		prop_type = db.Column(db.String, nullable=False)
		street_name = db.Column(db.String, nullable=False)
		house_num1 = db.Column(db.String, nullable=False)
		house_num2 = db.Column(db.String, nullable=False)
		sqft = db.Column(db.Integer, nullable=True)
		photo_url = db.Column(db.String, nullable=False)
		ppsf = db.Column(db.Float, nullable=True)
		predicted_price = db.Column(db.Float, nullable=True)

		def __init__(self, mlsnum):
			self.mlsnum = mlsnum

		def __repr__(self):
			return "Condo Id: {}".format(self.id)




