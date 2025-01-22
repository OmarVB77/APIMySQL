import mysql.connector
from config import MYSQL_CONFIG

def get_mysql_data():
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tu_tabla")  # Reemplaza con tu tabla
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        return {"error": str(e)}
