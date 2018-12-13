#create user route
#create post route


import os
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from flask_bower import Bower
from models import db, User, Condo, Photo
from forms import LoginForm, SignupForm
from utils import allowed_file,findClosest
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "cscie14a-speculator"

Bower(app)

# local postgresql or heroku postgresql
db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost/speculator_db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return redirect(url_for('info'))
    else:
        return render_template('index.html')

@app.route('/info')
def info():
    if 'username' in session:
        return render_template('info.html', username=session['username'])
    else:
        return render_template('info.html')

# profile route
@app.route('/profile')
def profile():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        return render_template('profile.html', username=user.username, favorites=user.likes)
    else:
        flash('You must be logged in to view your profile.')
        return redirect('index')


# search route
@app.route('/search', methods=['POST'])
def search():
    if 'photo' not in request.files:
        flash('Please upload a valid image file')
        return redirect(url_for('index'))
    photo = request.files['photo']
    if not allowed_file(photo.filename):
        flash('Please upload a valid image file')
        return redirect(url_for('index'))

    form = request.form
    filtered = Condo.query.filter(Condo.beds.between(form['bedsMin'], form['bedsMax'])).\
        filter(Condo.baths.between(form['bathsMin'], form['bathsMax']))
    if form['sqftMin'] and form['sqftMax']:
        filtered = filtered.filter(Condo.sqft.between(form['sqftMin'], form['sqftMax']))
    if form['priceMin'] and form['priceMax']:
        filtered = filtered.filter(Condo.listprice.between(form['priceMin'], form['priceMax']))
    if 'zip' in form:
        filtered = filtered.filter(Condo.zip==form['zip'])
    mlsnums = [condo.mlsnum for condo in filtered.limit(50).all()]

    images = Photo.query.filter(Photo.mlsnum.in_(mlsnums)).all()

    closest = findClosest(photo, images)
    condos = filtered.filter(Condo.mlsnum.in_(closest))

    # we have no reason to save uploaded images
    if 'username' in session:
        return render_template('results.html', username=session['username'], closest=condos)
    else:
        return render_template('results.html', closest=condos)

# signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form['username'].data
        password = form['password'].data
        confirm = form['confirm'].data

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('This username already exists. Please pick another one.')
            return redirect(url_for('signup'))
        elif password != confirm:
            flash('Your password confirmation is incorrect. Make sure you wrote the same password twice.')
            return redirect(url_for('signup'))
        else:
            user = User(username=username, password=sha256_crypt.hash(password))
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            session['username'] = username
            return redirect(url_for('info'))
    else:
        return render_template('signup.html', form=form)

# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form['username'].data
        password = form['password'].data

        user = User.query.filter_by(username=username).first()

        if user is None or not sha256_crypt.verify(password, user.password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session['username'] = username
            return redirect(url_for('info'))

    else:
        return render_template('login.html', form=form)

# logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
