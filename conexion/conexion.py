import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="b6yidpnlrwoyrb2wge9z-mysql.services.clever-cloud.com",
            user="USUARIO",
            password="CONTRASEÑA",
            database="b6yidpnlrwoyrb2wge9z",
            port=3306,
            ssl_ca="/etc/ssl/certs/ca-certificates.crt"
        )
        return conexion

    except Exception as e:
        print("Error conectando a la base de datos:", e)
        return None