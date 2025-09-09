import mysql.connector
import re
from geopy import distance

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="lassi",
        password="alfauros",
        database="flight_game",
        autocommit=True
    )

def isValidICAO(s: str) -> bool:
    pattern = r'^[A-Z0-9]+(-[A-Z0-9]+)?$'
    return bool(re.match(pattern, s.upper()))

def getInputICAO(prompt: str) -> str:
    while True:
        icao = input(prompt).upper()
        if icao == 'EXIT':
            exit()
        elif isValidICAO(icao):
            return icao
        print("Invalid ICAO code format. Please try again.")

def fetchAirportData(cursor, icao: str):
    cursor.execute("SELECT name, latitude_deg, longitude_deg "
                   "FROM airport "
                   "WHERE ident = %s", (icao,))
    return cursor.fetchone()

def getAirportDataWithRetry(prompt: str, cursor):
    while True:
        icao = getInputICAO(prompt)
        row = fetchAirportData(cursor, icao)
        if row is not None:
            return row
        print(f"No airport found with the given ICAO code {icao}. Please try again.")


connection = create_connection()
cursor = connection.cursor()

airport1 = getAirportDataWithRetry("Enter first ICAO code: ", cursor)
airport2 = getAirportDataWithRetry("Enter second ICAO code: ", cursor)

coords1 = (airport1[1], airport1[2])
coords2 = (airport2[1], airport2[2])
dist = distance.distance(coords1, coords2).km

print(f"Airport 1: {airport1[0]}, {coords1}")
print(f"Airport 2: {airport2[0]}, {coords2}")
print(f"Distance: {dist:.2f} km")

cursor.close()
connection.close()