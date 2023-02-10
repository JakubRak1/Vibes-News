from flask import Blueprint, render_template

from vibes import db
from vibes.models import Article, Category

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    carousel_news: Article = carousel_select('News')
    carousel_sport: Article = carousel_select('Sport')
    carousel_buissnes: Article = carousel_select('Buissnes')
    carousel_culture: Article = carousel_select('Culture')
    carousel_game_news: Article = carousel_select('Game News')
    carousel_items: list[Article] = [carousel_sport, carousel_buissnes, carousel_culture, carousel_game_news]
    all_news: list[Article] = all_articles('News')
    all_sport: list[Article] = all_articles('Sport')
    all_buissnes: list[Article] = all_articles('Buissnes')
    all_culture: list[Article] = all_articles('Culture')
    all_game_news: list[Article] = all_articles('Game News')
    return render_template('home.html', title = 'Vibes News', carousel_items = carousel_items, carousel_item_first = carousel_news, news=all_news, sport=all_sport, buissnes = all_buissnes, culture = all_culture, game_news=all_game_news)


@staticmethod
def carousel_select(category):
    # Function to find news article from entered category
    category: Category = db.session.query(Category).filter_by(name=category).first()
    first_article: Article = db.session.query(Article).filter_by(category_id=category.id).first()
    all_articles: list[Article] = db.session.query(Article).filter_by(category_id=category.id).all()
    for article in all_articles:
        if first_article.time_posted < article.time_posted:
            first_article = article
    return first_article


@staticmethod
def all_articles(category):
    #Function that returns all articles from category and limit to 5
    category: Category = db.session.query(Category).filter_by(name=category).first()
    all_articles: list[Article] = db.session.query(Article).filter_by(category_id=category.id).all()
    return all_articles


@main.route("/about")
def about():
    return render_template('about.html', title = 'About Us')

