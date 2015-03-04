import json
import os
import praw
import random
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

# PRAW
r = praw.Reddit(user_agent='reposte')

# Top subreddits
top_subs = json.load(open('top_subs.json'))

def find_sub():
    """ Finds a good subreddit to post in. """
    return random.choice(top_subs)

def find_repost(sub):
    """ Finds a good post to repost. """
    submissions = r.get_subreddit(sub).get_top_from_year(limit = 100)
    return random.choice(list(submissions))

@app.route('/')
def index():
    sub = find_sub()
    return render_template('index.html', post = find_repost(sub), sub = sub)

@app.route('/r/<sub>')
def sub(sub):
    return render_template('subreddit.html', post = find_repost(sub), sub = sub)

if __name__ == '__main__':
    app.run()
