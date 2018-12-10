#create user route
#create post route


import os
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from flask_bower import Bower
from models import db, User
from forms import LoginForm, SignupForm
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import json

app = Flask(__name__)
app.secret_key = "cscie14a-speculator"

Bower(app)

# migration commands: flask db init, flask db migrate -m "msg", flask db upgrade

# local postgresql or heroku postgresql
db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost/speculator_db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db = SQLAlchemy(app)
Migrate(app,db)



from models import db
from flask import Flask, flash, render_template, request, url_for, redirect, session, jsonify
from models import Condo, User, Like
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash,check_password_hash
import base64
import numpy as np 
import io
from PIL import Image
import keras
from keras import backend as K 
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array


#load model from keras into memory
def get_model():
    global model
    model = load_model('VGG16.h5')
    print("h5 works")

#function to accept PIL, python to format into keras model (numpy array)
def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    #format image into array for Keras
    return image

print(" Keras model loading")
get_model




@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return render_template('index.html')


@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if 'username' in session:
        return render_template('info.html', username=session['username'])
    else:
        return render_template('index.html')

def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'condo': prediction[0],
            'condo': prediction[1]
        }
    }
    return jsonify(response)

def info(mlsnum):
    condo = Condo.query.filter_by(mlsnum=mlsnum).first()

    if "username" in session:
        session_user = User.query.filter_by(username=session['username']).first()
        if Like.query.filter_by(follower=session_user.id, following=condo.mlsnum).first():
            followed = True
        else:
            followed = False
        return render_template('info.html', condo=condo, session_username=session_user.username, followed=followed)
    return render_template('info.html', condo=condo)

# Profile route   

@app.route('/favorite', methods=['POST','GET'])
def favorite():
    username_to_query = User.query.filter_by(username=session['username']).first()
    return redirect(url_for('profilecondo', username=username_to_query.username)) 


@app.route('/profilecondo/<username>', methods=['GET'])
def profilecondo(username):

    
    if 'username' in session: 
        session_user = User.query.filter_by(username=session['username']).first()
        
        # followers
        users_followed = Like.query.filter_by(follower=session_user.id).all()
        uids_followed = [f.following for f in users_followed]
        followed_posts = Condo.query.filter(Condo.mlsnum.in_(uids_followed)).all()
        
        return render_template('profile.html', title='Home', condos=followed_posts, session_username=session_user.username)
    else:
        all_posts = Condo.query.all()
        return render_template('profile.html', title='Home', condos=all_posts)




@app.route('/like/<mlsnum>', methods=['POST','GET'])
def follow(mlsnum):
    session_user = User.query.filter_by(username=session['username']).first()
    condo_to_follow = Condo.query.filter_by(mlsnum=mlsnum).first()

    new_follow = Like(follower=session_user.id, following=condo_to_follow.mlsnum)

    db.session.add(new_follow)
    db.session.commit()
    return redirect(url_for('info', mlsnum=mlsnum))


@app.route('/unlike/<mlsnum>', methods=['POST','GET'])
def unfollow(mlsnum):
    session_user = User.query.filter_by(username=session['username']).first()
    condo_to_unfollow = Condo.query.filter_by(mlsnum=mlsnum).first()
    
    delete_follow = Like.query.filter_by(follower=session_user.id, following=condo_to_unfollow.mlsnum).first()
    db.session.delete(delete_follow)
    db.session.commit()
    return redirect(url_for('info', mlsnum=mlsnum))




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
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            session['username'] = username
            return redirect(url_for('predict'))
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

        if user is not None and user.check_password(form.password.data) :
            session['username'] = username
            return redirect(url_for('prediction'))

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # Check if that next exists, otherwise go to the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('users.index')

            return redirect(next)
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))

    else:
        return render_template('login.html', form=form)

# logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))





if __name__ == "__main__":
    app.run(debug=True)
