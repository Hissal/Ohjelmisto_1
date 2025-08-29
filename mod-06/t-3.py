import inputHandler
import unitConverter

while True:
    gallons = inputHandler.getFloatInput("Enter gallons: ", "Invalid input. Please enter a valid number.")

    if gallons < 0:
        print("Exiting the program.")
        break

    liters = unitConverter.gallon_to_liter(gallons)
    print(f"{gallons} gallons is {liters} liters.")