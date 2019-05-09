from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/introduction')
def introduction():
    return render_template('intro.html')

@app.route('/cage')
def cage(picture1=None, picture2=None):
    return render_template('cage.html', picture1="static/images/almond.png", picture2="static/images/almond.png")

@app.route('/wheel')
def wheel(picture1=None, picture2=None):
    return render_template('wheel.html', picture1="static/images/almond.png", picture2="static/images/almond.png")

@app.route('/bottle')
def bottle():
    return render_template('bottle.html')

@app.route('/play')
def play():
    return render_template('play.html')