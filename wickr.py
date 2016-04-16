from flask import Flask, request, session, render_template, g, url_for, redirect
import os

app = Flask(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'wickr.db'),
    DEBUG = True,

))
app.config.from_envvar('WICKR_SETTINGS', silent=True)

@app.route('/')
def route_index():
    return render_template('home.html')

@app.route('/wiki/<path:article>')
def route_article(article):
    return render_template('article.html', article=article)
