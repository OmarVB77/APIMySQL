import pyodbc
from config import SQLSERVER_CONFIG

def get_sqlserver_data():
    try:
        conn = pyodbc.connect(
            f"DRIVER={SQLSERVER_CONFIG['driver']};"
            f"SERVER={SQLSERVER_CONFIG['host']};"
            f"DATABASE={SQLSERVER_CONFIG['database']};"
            f"Trusted_Connection={SQLSERVER_CONFIG['trusted_connection']}"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tu_tabla")  # Reemplaza con tu tabla
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return data
    except Exception as e:
        return {"error": str(e)}
