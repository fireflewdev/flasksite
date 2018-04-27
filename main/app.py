from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from wtforms import *
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import *
from random import *
import time
from functools import wraps
###
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.file import FileField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=5, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

###
# Init the application
app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = "random_large_int"
Bootstrap(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(15))
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    password = db.Column(db.String(80))

# Routes
@app.route('/')
def index():
    name = 'John Smith'
    return render_template('index.html', **locals())

@app.route('/login', methods=['GET', 'POST']) # Step 1 = Methods
def login():
    form = LoginForm()

    if request.method == 'POST': # Step 2 = If POST is the type of request
        print('Success signing in {}'.format(form.email.data))
        return redirect(url_for('profile'))

    return render_template('login.html', **locals())

@app.route('/profile')
def profile():
    name = 'John Smith'
    return render_template('index.html', **locals())

@app.route('/articles')
def articles():
    return render_template('articles.html')

# Run the server
app.run(port=port)
# test
