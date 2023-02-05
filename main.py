from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run()