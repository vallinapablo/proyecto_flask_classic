from my_crypto import app
from flask import render_template

@app.route("/")
def index():
    return render_template("inicio.html")