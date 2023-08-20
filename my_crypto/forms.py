from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from my_crypto.models import get_rate

class CompraForm(FlaskForm):
    
    moneda_from = SelectField("Moneda from", choices=[("EUR", "Euros"), ("ETH", "ETH"), ("BNB", "BNB"),("ADA", "ADA"),
                                               ("DOT", "DOT"),("BTC", "BTC"),("XRP", "XRP"),("SOL", "SOL"), ("MATIC", "MATIC")])

    moneda_to = SelectField("Moneda to", choices=[("EUR", "Euros"), ("ETH", "ETH"), ("BNB", "BNB"),("ADA", "ADA"),
                                               ("DOT", "DOT"),("BTC", "BTC"),("XRP", "XRP"),("SOL", "SOL"), ("MATIC", "MATIC")])
    
    cantidad_from =  FloatField("Cantidad from", validators=[DataRequired("Cantidad obligatoria")])
    
    cantidad_to = HiddenField()
    calculate = SubmitField("Calcular")
    comprar = SubmitField("Comprar") 

    

    
