from my_crypto import app
from my_crypto.models import *
from my_crypto.forms import *
from flask import render_template, flash, redirect, request

dao= MovementDAOsqlite(app.config.get("PATH_SQLITE"))

@app.route("/", methods=['GET'])
def index():
    movements = dao.get_all()
    return render_template("inicio.html", movements=movements)

@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
    form = CompraForm()
    cantidad_to = None
    if request.method == 'GET':
        return render_template("compra.html", the_form = form)
    
    elif request.method == 'POST' and form.validate_on_submit():
        
        if 'calculate' in request.form:
            moneda_from = form.moneda_from.data
            moneda_to = form.moneda_to.data
            cantidad_from = form.cantidad_from.data
            
            
            tasa_cambio = get_rate(moneda_from, moneda_to)
            if tasa_cambio is not None:
                cantidad_to = cantidad_from * tasa_cambio
                    
            return render_template("compra.html", the_form = form, cantidad_to=cantidad_to)
    
        if 'comprar' in request.form:
            moneda_from = form.moneda_from.data
            moneda_to = form.moneda_to.data
            cantidad_from = form.cantidad_from.data
            cantidad_to = form.cantidad_to.data

            try:
                dao.insert(Movement("jiji", "jaja" ,moneda_from, cantidad_from, 
                                    moneda_to, cantidad_from))
                return redirect("/")
            except ValueError as e:
                flash(str(e))
                return render_template("compra.html", the_form=form)
        else:
            return render_template("compra.html", the_form=form)

   
            



@app.route("/status", methods=["GET"])
def status():
    return render_template("status.html")
