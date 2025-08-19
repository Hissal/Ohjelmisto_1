def getFloatInput(message: str, invalidValueMessage: str) -> float:
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print(invalidValueMessage)

def getIntInput(message: str, invalidValueMessage: str) -> int:
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print(invalidValueMessage)

def getStringInput(allowedStrings: list[str], message: str, invalidValueMessage: str) -> str:
    while True:
        value = input(message)
        if value in allowedStrings:
            return value
        else:
            print(invalidValueMessage)

def getStringInputLowercased(allowedStrings: list[str], message: str, invalidValueMessage: str) -> str:
    while True:
        value = input(message).lower()
        if value in allowedStrings:
            return value
        else:
            print(invalidValueMessage)