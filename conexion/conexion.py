import pymysql.cursors

def conectar():
    try:
        conexion = pymysql.connect(
            host="b6yidpnlrwoyrb2wge9z-mysql.services.clever-cloud.com",
            user="uvaqtfxavnoiylnp",
            password="SMbCjlqgP29ck7OuxTiA",
            database="b6yidpnlrwoyrb2wge9z",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor  # << Muy importante para que funcione tu HTML
        )
        return conexion

    except Exception as e:
        print("Error conectando a la base de datos:", e)
        return None