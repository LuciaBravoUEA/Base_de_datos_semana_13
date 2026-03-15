import os
import mysql.connector
from urllib.parse import urlparse

def conectar():
    try:
        db_url = os.getenv("DATABASE_URL")

        # Cambiar mysql:// por mysql+mysqlconnector://
        if db_url.startswith("mysql://"):
            db_url = db_url.replace("mysql://", "mysql+mysqlconnector://", 1)

        url = urlparse(db_url)

        conexion = mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path.replace("/", ""),
            port=url.port
        )

        print("Conexión exitosa")
        return conexion

    except Exception as e:
        print("Error conectando a la base de datos:", e)
        return None