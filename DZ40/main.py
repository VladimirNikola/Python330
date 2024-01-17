from flask import Flask, render_template, request, flash, g, abort
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


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title="Каталог курсов", menu=dbase.get_menu(), posts=dbase.get_posts_anonce())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 10 and len(request.form['price']) > 10 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['price'], request.form['post'], request.form['url'])
            if not res:
                flash("Ошибка добавления курса", category="error")
            else:
                flash("Курс добавлен успешно", category="success")
        else:
            flash("Ошибка добавления курса", category="error")

    return render_template('add_post.html', title="Добавление курса", menu=dbase.get_menu())


@app.route("/info/<alias>")
def add_info(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, price, text = dbase.get_info(alias)
    if not title:
        abort(404)

    return render_template('info.html', menu=dbase.get_menu(), title=title, price=price, text=text)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run(debug=True)
