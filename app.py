from flask import Flask, request, jsonify
from models.mysql_model import get_mysql_data
from models.sqlserver_model import get_sqlserver_data

app = Flask(__name__)

# Ruta para datos desde MySQL
@app.route('/mysql', methods=['GET'])
def mysql_endpoint():
    data = get_mysql_data()
    return jsonify(data)

# Ruta para datos desde SQL Server
@app.route('/sqlserver', methods=['GET'])
def sqlserver_endpoint():
    data = get_sqlserver_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
