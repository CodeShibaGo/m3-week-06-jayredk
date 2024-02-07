from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'H'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'LEO'},
            'body': 'God like!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)