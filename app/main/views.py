from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources

# views

@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	source = get_sources('business')
	sports_sources = get_sources('sports')
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
	title = "News Source website"

	return render_template('index.html', title=title, business=source, sports=sports_sources, technology=technology_sources, entertainment=entertainment_sources)

@main.route('/articles/<id>')
def source(id):
	'''
	view articles
	'''
	articles = get_articles(id)
   
	return render_template('articles.html', id=id, articles=articles)