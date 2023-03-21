from flask import Flask, render_template, url_for, request, redirect, send_from_directory, flash
# import validators
# from validators import ValidationFailure
# from werkzeug.utils import secure_filename
# from datetime import datetime
import sqlite3
import os
import config

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# define basic things such as the config file
app = Flask(__name__)
# app.config['SECRET_KEY'] = config.secret_key
app.config.from_pyfile('config.py')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def is_string_an_url(url_string: str) -> bool:
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        return False

    return result


def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "icons.db")
    conn = sqlite3.connect(db_path)
    return conn


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Routes for every page and what the function is
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Icon')
    results = cur.fetchall()
    return render_template('index.html', results=results)


# WHY THE FUCK DOES THIS NOT WORK
# setuo the settings 
@app.route('/settings', methods=('GET', 'POST'))
def settings():
    if request.method == 'POST':
        title = request.form[1]
        url = request.form[2]

        if not title:
            flash('Title is required!')
        elif not url:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (1, 2) VALUES (?, ?)',
                         (title, url))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
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
    app.run(host='0.0.0.0', port=5000, debug=True)