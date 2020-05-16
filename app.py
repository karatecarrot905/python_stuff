from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/poo')
def poop():
	return 'Peepeepoopooman'

@app.route('/coolstuff')
def coolstuff(name=None):
	return render_template('Stuff.html', name=name)
