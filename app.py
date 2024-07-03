from flask import Flask, request, redirect, render_template
import string
import random

app = Flask(__name__)


def pw_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pw_size = int(request.form["pw_size"])
        pw = pw_generator(size=pw_size)
        return render_template("pwgen.html", password=pw)

    return render_template("main.html")

if __name__ == '__main__':
    app.run()

