import os
import mysql.connector
from urllib.parse import urlparse

def conectar():
    db_url = os.getenv("DATABASE_URL")
    url = urlparse(db_url)

    conexion = mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],  # quita el "/" inicial
        port=url.port
    )
    return conexion