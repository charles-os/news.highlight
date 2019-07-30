from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles
from ..models import News, Articles

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	business_news = get_news('business')
	sports_news = get_news('sports')
	technology_news = get_news('technology')
	entertainment_news = get_news('entertainment')
	title = "News Highlighter"

	return render_template('index.html', title=title, business_news=business_news, sports_news=sports_news, technology_news=technology_news, entertainment_news=entertainment_news )

@main.route('/entertainment')
def entertainment():
    general_news = get_news('entertainment')
    title = 'general-news Page - Get The Latest News Oline'
    return render_template('entertainment.html', title = title, entertainment =general_news)


@main.route('/general')
def general():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('general')
	title = 'general-news Page - Get The latest News Online'
	return render_template('general.html', title=title, general=general_news)


@main.route('/sport')
def sport():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('sports')
	title = 'general-news Page - Get The latest News Online'
	return render_template('sport.html', title=title, sports=general_news)


@main.route('/tech')
def tech():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('technology')
	title = 'general-news Page - Get The latest News Online'
	return render_template('tech.html', title=title, technology=general_news)


@main.route('/business')
def business():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('business')
	title = 'general-news Page - Get The latest News Online'
	return render_template('business.html', title=title, business=general_news)


@main.route('/articles/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html', title=title, articles=articles)
