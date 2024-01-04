from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О компании", "url": "about"},
    {"name": "Контакты", "url": "contact"}
]


@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        print(request.form)
    return render_template('index.html', title="Купить билет", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О компании", menu=menu)


@app.route("/contact")
def contact():
    return render_template('contact.html', title="Контакты", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
