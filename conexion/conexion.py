import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="b6yidpnlrwoyrb2wge9z-mysql.services.clever-cloud.com",
            user="USUARIO", # Recuerda poner tu usuario real
            password="CONTRASEÑA", # Recuerda poner tu contraseña real
            database="b6yidpnlrwoyrb2wge9z",
            port=3306
           
        )
        if conexion.is_connected():
            return conexion
    except Exception as e:
        print("Error conectando a la base de datos:", e)
        return None