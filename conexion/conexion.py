import mysql.connector
import os
from urllib.parse import urlparse

def conectar():
    try:
        url = os.environ.get("DATABASE_URL")

        datos = urlparse(url)

        conexion = mysql.connector.connect(
            host=datos.hostname,
            user=datos.username,
            password=datos.password,
            database=datos.path.replace("/", ""),
            port=datos.port,
            ssl_disabled=False
        )

        return conexion

    except Exception as e:
        print("Error conectando a la base de datos:", e)
        return None