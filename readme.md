# Aplicacion web: Registro de movimientos de criptomonedas

Proyecto final BootCamp XVI:
Se trata de realizar un registro de inversiones y compra/venta de criptomonedas.

Se crea una aplicacion flask que consultará el valor real en euros de las siguientes criptomonedas: EUR, ETH, BNB, ADA, DOT, BTC, USDT, XRP, SOL, MATIC

Objetivo:
La aplicación nos permitirá realizar las siguientes conversiones: Compra, Tradeo, Venta.
Hay dos formas de conseguir más euros de los invertidos, la primera es el tiempo, es decir, comprar más barato que al momento de la venta. La segunda es intercambiar criptos entre ellas.

# Instalación

Servicios externo:
El sistema consultará con coinAPI.io para obtener el total de monedas que se pueden conseguir al precio actual. Para hacerla funcionar es necesario obtener una apikey en su web.

Paso a paso:
Replicar fichero .env_template y renombrarlo .env
Informar las siguientes claves:
        FLASK_APP: main.py (no cambiar)
        FLASK_DEBUG: debe ser False en entornos de producción.
        FLASK_PATH_SQLITE: los movimientos se grabarán en un fichero sqlite. Aquí se pondra su nombre y path.
        FLASK_SECRET_KEY: clave secreta cualquiera.
        FLASK_API_KEY: obtener una apikey de coinApi.io

Requirements:
Instalar requirements:
pip install -r requirements.txt

Lanzar la aplicación:
flask run
