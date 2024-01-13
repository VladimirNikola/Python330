from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase

DATABASE = 'JD.db'
DEBUG = True
SECRET_KEY = '7f30a6bd7f6855965c2c8a41f3c4474006232304'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'JD.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


# menu = [
#     {"name": "Главная", "url": "index"},
#     {"name": "О компании", "url": "about"},
#     {"name": "Контакты", "url": "contact"}
# ]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
# @app.route("/index", methods=["POST", "GET"])
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title="Купленные билеты", menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['surname']) > 2:
            flash("Сообщение отправлено успешно!", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template('add_post.html', title="Купить билеты", menu=dbase.get_menu())


@app.route("/about")
def about():
    return render_template('about.html', title="О компании", menu=[])


@app.route("/contact")
def contact():
    return render_template('contact.html', title="Контакты", menu=[])


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run(debug=True)
