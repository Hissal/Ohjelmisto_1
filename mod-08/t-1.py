import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="lassi",
        password="alfauros",
        database="flight_game",
        autocommit=True
    )

inputICAO = input("Enter ICAO code: ").upper()

connection = create_connection()
cursor = connection.cursor()

cursor.execute("SELECT name, municipality "
               "FROM airport "
               "where ident = %s", (inputICAO,))

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()