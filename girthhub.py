#!/usr/bin/env python

import requests
import json
import random
from flask import Flask, redirect

app = Flask(__name__)

def get_commits():
    headers = {'Accept': 'application/vnd.github.cloak-preview'}
    r = requests.get('https://api.github.com/search/commits?q=donger', headers=headers)
    
    donger_commits = []
    dongers = json.loads(r.text.encode('utf-8'))
    #print type(dongers)
    #print r.text.encode('utf-8')
    
    for key, value in dongers.iteritems():
        if key == 'items':
            for commits in value:
                donger_commits.append(commits['html_url'])
    
    return random.choice(donger_commits)

@app.route('/')
def index():
    commit_url = get_commits()
    return redirect(commit_url, code=302)

if __name__ == '__main__':
    print "Girthmode engaged."
    app.run(host='127.0.0.1', port=8001)

    
