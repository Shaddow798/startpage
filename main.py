from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


# define basic things such as the config file
app = Flask(__name__)
app.config.from_pyfile('config.py')


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


# Routes for every page and what the function is
@app.route('/', methods=['POST', 'GET'])


def index():
    #pins = Icons.query.order_by(Icons.date_created).all()
    return render_template('index.html')
    #return render_template('index.html')

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
            return 'Something went wrong'
    else:
        return render_template('settings.html')

# Load Browser Favorite Icon
@app.route('/favicon.ico')


def favicon():
    return url_for('static',filename='images/favicon.ico')

#Handling error 404 and displaying relevant web page
@app.errorhandler(404)


def not_found_error(error):
    return render_template('404.html'),404
 
#Handling error 500 and displaying relevant web page
@app.errorhandler(500)


def internal_error(error):
    return render_template('500.html'),500


# run the program

if __name__ == "__main__":
    app.run()