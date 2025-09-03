airports: dict[str, str] = {}

ADD = "add"
FIND = "find"
EXIT = "exit"

def HandleAddingAirport():
    inputName = input("Enter airport name: ")
    inputCode = input("Enter airport ICAO code: ")

    if inputCode in airports:
        print(f"!!! An airport with the given ICAO code already exists: {airports[inputCode]}")
        inputOverride = input("Do you want to override the existing airport (y/n): ").lower()

        if inputOverride == "y":
            airports[inputCode] = inputName
    else:
        airports[inputCode] = inputName

def HandleFindingAirport():
    inputCode = input("Enter airport ICAO code: ")
    if inputCode in airports:
        print(f"Airport name: {airports[inputCode]}")
    else:
        print(f"No airport found with the given ICAO code {inputCode}")

while True:
    inputOption = input(f"Do you want to add an airport, find an airport or exit ({ADD}/{FIND}/{EXIT}): ").lower()

    if inputOption == EXIT:
        break
    elif inputOption == ADD:
        HandleAddingAirport()
    elif inputOption == FIND:
        HandleFindingAirport()
    else:
        print("Invalid option")