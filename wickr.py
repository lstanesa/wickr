from flask import Flask, request, session, render_template, g, url_for, redirect
from markdown import markdown
import os

from db import Database

app = Flask(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'wickr.db'),
    DEBUG = True,
    SITE_TITLE = 'Wickr',
    JSON_API = True
))
app.config.from_envvar('WICKR_SETTINGS', silent=True)

g.db = Database(app.config['DATABASE'])

@app.route('/')
def route_index():
    return render_template('home.html')

@app.route('/wiki/<path:article>')
def route_article(article):
    return render_template('article.html', article=article)

@app.template_filter('markdown')
def filter_markdown(s):
    return markdown(s)
