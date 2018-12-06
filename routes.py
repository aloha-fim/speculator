#create user route
#create post route


import os
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from flask_bower import Bower
from models import db, User
from forms import LoginForm, SignupForm
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.secret_key = "cscie14a-speculator"

Bower(app)

# local postgresql or heroku postgresql
db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost/speculator_db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db.init_app(app)


from models import db
from flask import Flask, flash, render_template, request, url_for, redirect, session
from models import Condo, User, Like


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return render_template('index.html')


@app.route('/info/<mlsnum>', methods=['GET','POST'])
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
            user = User(username=username, password=sha256_crypt.hash(password))
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            session['username'] = username
            return redirect(url_for('index'))
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
            return redirect(url_for('index'))

    else:
        return render_template('login.html', form=form)

# logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
