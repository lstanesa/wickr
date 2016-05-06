from flask import Flask, request, session, render_template, g, url_for, redirect
from markdown import markdown
import os
import json

from db import Database
from model import Article

app = Flask(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'wickr.db'),
    DEBUG = True,
    SITE_TITLE = 'Wickr',
    JSON_API = True
))
app.config.from_envvar('WICKR_SETTINGS', silent=True)


@app.route('/')
def route_index():
    init_db()
    rows = g.db.query('SELECT name FROM article ORDER BY `created` LIMIT 10;').fetchone()
    return render_template('home.html', articles=rows)

@app.route('/wiki/<path:name>')
def route_article(name):
    init_db()
    article = Article(name);
    article.fetch()
    close_db()
    return render_template('article.html', article=article)

@app.route('/random')
def route_random():
    init_db()
    row = g.db.query('SELECT name FROM article ORDER BY RANDOM() LIMIT 1;').fetchone()
    close_db()
    return redirect(url_for('route_article', name=row[0]))

@app.template_filter('markdown')
def filter_markdown(s):
    return markdown(s)

def init_db():
    g.db = Database(app.config['DATABASE'], True)

def close_db():
    g.db.close()
