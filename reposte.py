import os
import praw
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

# PRAW
r = praw.Reddit(user_agent='reposte')

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/r/<subreddit>')
def subreddit(subreddit):
    submissions = r.get_subreddit(subreddit).get_new(limit = 100)
    return render_template('subreddit.html', submissions=submissions)

if __name__ == '__main__':
    app.run()
