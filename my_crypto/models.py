from my_crypto import app
import sqlite3
import requests
from datetime import datetime

class Movement:
    def __init__(self, date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, id=None):
        self.id = id
        self.date = date
        self.time = time
        self.moneda_from = moneda_from
        self.cantidad_from = cantidad_from
        self.moneda_to = moneda_to
        self.cantidad_to = cantidad_to



class MovementDAOsqlite:
    def __init__(self, db_path):
        self.path = db_path

        query = """
        CREATE TABLE IF NOT EXISTS "movements" (
            "id"	INTEGER,
            "date"	TEXT,
            "time"	TEXT,
            "moneda_from"	TEXT,
            "cantidad_from"	REAL,
            "moneda_to"	TEXT,
            "cantidad_to"	REAL,
            PRIMARY KEY("id" AUTOINCREMENT)
         );
        """
    
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query)
        conn.close() 
    
    def insert(self, movement):

        query = """
        INSERT INTO movements 
                (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query, (movement.date, movement.time, movement.moneda_from,
                            movement.cantidad_from, movement.moneda_to, movement.cantidad_to))
        conn.commit()
        conn.close()

    def get(self, id):
        query ="""
        SELECT id, date, time, moneda_from, cantidad_from, moneda_to, cantidad_to
            FROM movements
            WHERE id = ?;
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query, (id,))
        res = cur.fetchone()
        conn.close()
        if res is None:
            return None
        return Movement(*res)

    def get_all(self):
        query ="""
        SELECT  date, time, moneda_from, cantidad_from, moneda_to, cantidad_to
            FROM movements
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        lista = []
        for reg in res:
            lista.append(Movement(*reg))
        conn.close()
        return lista
    

def get_rate(moneda_from, moneda_to):

    url = f'https://rest.coinapi.io/v1/exchangerate/{moneda_from}/{moneda_to}?apikey={app.config.get("API_KEY")}'

    
    response = requests.get(url)
    data = response.json()
    
    if 'rate' in data:
        get_rate = data['rate']
        return get_rate
    else:
        return None

