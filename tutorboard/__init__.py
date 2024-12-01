from flask import Flask, render_template, url_for, redirect
import socket
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import pandas as pd
import csv

app = Flask(__name__)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
# Initialize the SQLAlchemy database object and Flask-Migrate for database migrations
db = SQLAlchemy()
migrate = Migrate()

# define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route("/course", methods=['GET','POST'])
def course():
    return render_template('course.html')
@app.route('/dashboard', methods=['GET','POST'] )
def dashboard():
    return render_template('dashboard.html')
@app.route("/watchcourse", methods=['GET','POST'])
def watchcourse():
    return render_template('watchcourse.html')
# Create the Flask application factory function
def data():
 
    load_dotenv()  # Load environment variables from the .env file
    
    # Configure the app with database and secret key (read from environment variables)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Set the database URI
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Secret key for session management
    
    # Initialize database and migration extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register the routes from the 'routes' file
    from MyPDMTutor.pdm_venv.tutorboard.routes import main  # Blueprint import (from app/routes.py)
    app.register_blueprint(main)  # Register the routes with the app

if __name__ == '__main__':
    app.run(debug=True)