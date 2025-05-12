from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home_ru():
    return render_template('index.html', lang='ru')

@main.route('/en')
def home_en():
    return render_template('index.html', lang='en')

@main.route('/about')
def about_ru():
    return render_template('about.html', lang='ru')

@main.route('/en/about')
def about_en():
    return render_template('about.html', lang='en')

@main.route('/gallery')
def gallery_ru():
    return render_template('gallery.html', lang='ru')

@main.route('/en/gallery')
def gallery_en():
    return render_template('gallery.html', lang='en')

@main.route("/contacts")
def contacts_ru():
    return render_template("contacts.html", lang="ru")

@main.route("/en/contacts")
def contacts_en():
    return render_template("contacts.html", lang="en")

@main.route("/team")
def team_ru():
    return render_template("team.html", lang="ru")

@main.route("/en/team")
def team_en():
    return render_template("team.html", lang="en")

@main.route("/news")
def news_ru():
    return render_template("news.html", lang="ru")

@main.route("/en/news")
def news_en():
    return render_template("news.html", lang="en")
