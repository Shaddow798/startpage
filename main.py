from flask import Flask, render_template, url_for, request, redirect, send_from_directory, flash
from werkzeug.utils import secure_filename
from datetime import datetime
import sqlite3
import os
import uuid


UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# define basic things such as the config file
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config.from_pyfile('config.py')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Routes for every page and what the function is
@app.route('/')
def index():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "icons.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Icon')
    results = cur.fetchall()
    return render_template('index.html', results=results)


# WHY THE FUCK DOES THIS NOT WORK
# setuo the settings 
@app.route('/settings', methods=('GET', 'POST'))
def settings():
    return render_template('settings.html')


@app.route('/about')
def about():
    return render_template(about.html)


# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error=404)
 

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=500)


# run the program

# All this does it run it aslong as its not being imported

if __name__ == "__main__":
    app.run()