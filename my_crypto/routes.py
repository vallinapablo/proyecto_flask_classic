from my_crypto import app
from flask import render_template

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/purchase", methods=["GET"])
def purchase():
    return render_template("compra.html")

@app.route("/status", methods=["GET"])
def status():
    return render_template("status.html")
