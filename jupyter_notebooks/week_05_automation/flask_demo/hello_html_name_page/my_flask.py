# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def index(name):
    user = {'username': name}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello ''' + user['username'] + '''!</h1>
    </body>
</html>'''
