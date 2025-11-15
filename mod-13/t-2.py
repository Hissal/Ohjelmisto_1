import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="lassi",
        password="alfauros",
        database="flight_game",
        autocommit=True
    )

@app.get("/kentta/<string:icao>")
def fetch_airport(icao):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT a.name, a.municipality "
                   "from airport a "
                   "where a.ident = %s ", (icao,))

    airport_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify({
        "ICAO": icao,
        "Name": airport_data[0],
        "Municipality": airport_data[1]
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)