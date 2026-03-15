import os
import mysql.connector
from urllib.parse import urlparse

def conectar():
    try:
        db_url = os.getenv("DATABASE_URL")

        if not db_url:
            print("DATABASE_URL no existe")
            return None

        url = urlparse(db_url)

        conexion = mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path[1:],
            port=url.port
        )

        print("Conexion exitosa a MySQL")
        return conexion

    except Exception as e:
        print("Error conectando a la base de datos:", e)
        return None