from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Artem'}
    posts = [
        {
            'author' : {'nickname' : 'John'},
            'body' : 'Beautiful day in Brno!'
        },
        {
            'author' : {'nickname' : 'Susan'},
            'body' : 'The TP 3 is so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

