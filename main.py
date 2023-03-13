from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
import sqlite3
import os


UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# define basic things such as the config file
app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = sqlite3.connect('icons.db')
cur = conn.cursor()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Routes for every page and what the function is
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# WHY THE FUCK DOES THIS NOT WORK
# setuo the settings 
@app.route('/settings', methods=['POST', 'GET'])
def settings():
    return render_template('settings.html')


# File uploader test
@app.route('/fileuploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            return redirect('/', background=filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# This allows fot the file uploader to open the file after being uploadsed

#@app.route('/uploads/<name>')
#def download_file(name):
#    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


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