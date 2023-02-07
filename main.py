from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///icons.db'
app.app_context()
db = SQLAlchemy(app)

class Icons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Content is equal to to name of the link
    content = db.Column(db.String(200), nullable=False)
    content_link = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id





@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run()