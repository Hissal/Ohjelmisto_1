def getFloatInput(message: str, invalidValueMessage: str) -> float:
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print(invalidValueMessage)