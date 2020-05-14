# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name):
    user = {'username': name}
    return render_template('index.html', title='Great!', user=user)
