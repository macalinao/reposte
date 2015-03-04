import os
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/r/<subreddit>')
def subreddit(subreddit):
    return 'Subreddit %s' % subreddit

if __name__ == '__main__':
    app.run()
