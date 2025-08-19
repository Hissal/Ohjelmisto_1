import inputHandler

def inchToCm(inches: float) -> float:
    return inches * 2.54

while True:
    inputInches = inputHandler.getFloatInput("Enter a length in inches: ", "Invalid input. Please enter a valid number.")

    if inputInches <= 0:
        break

    cm = inchToCm(inputInches)
    print(f"{inputInches} inches is equal to {cm:.2f} centimeters")