from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
import os

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# define basic things such as the config file
app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Define where the database is.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///icons.db'
app.app_context()
db = SQLAlchemy(app)

# Setup what each thing is in the database
class Icons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Content is equal to to name of the link
    content = db.Column(db.String(100), nullable=False)
    content_link = db.Column(db.String(200), nullable=False)
    content_order = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Pins %r>' % self.id

# Trying to get this to work but its being a bitch.

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# Routes for every page and what the function is
@app.route('/', methods=['GET'])
def index():
    #pins = Icons.query.order_by(Icons.date_created).all()
    return render_template('index.html')
# WHY THE FUCK DOES THIS NOT WORK
# setuo the settings 
@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        pin_content = request.form['content']
        pin_link_content = request.form['link_content']
        pin_order = request.form['order']
        new_pin = Icons(content=pin_content)
        new_link_pin = Icons(content=pin_link_content)
        new_order = Icons(content=pin_order)
        try:
            db.session.add(new_pin)
            db.session.add(new_link_pin)
            db.session.add(new_order)
            db.session.commit()
            return redirect('/settings')
        except:
            return 'Something went wrong adding your item to the database'
    else:
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
            #return redirect(url_for('download_file', name=filename))
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
#@app.route('/uploads/<name>')
#def download_file(name):
#    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/about')
def about():
    return render_template(about.html)

# DOES THIS EVEN MATTER
# Load Browser Favorite Icon
#@app.route('/favicon.ico')
#def favicon():
#    return url_for('static',filename='images/favicon.ico')

#Handling error 404 and displaying relevant web page
@app.errorhandler(404)


def not_found_error(error):
    return render_template('404.html'),404
 
#Handling error 500 and displaying relevant web page
@app.errorhandler(500)


def internal_error(error):
    return render_template('500.html'),500


# run the program

# All this does it run it aslong as its not being imported

if __name__ == "__main__":
    app.run()