import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="lassi",
        password="alfauros",
        database="flight_game",
        autocommit=True
    )

inputCountry = input("Enter country code: ").upper()

connection = create_connection()
cursor = connection.cursor()

cursor.execute("SELECT a.type, count(a.type) "
        "from airport a "
        "join country c on c.iso_country = a.iso_country "
        "where c.iso_country = %s "
        "group by a.type "
        "order by count(a.type) desc; ", (inputCountry,))

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()