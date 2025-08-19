import inputHandler

number1 = inputHandler.getFloatInput("Enter the first number: ", "Invalid input. Please enter a valid number.")
number2 = inputHandler.getFloatInput("Enter the second number: ", "Invalid input. Please enter a valid number.")
number3 = inputHandler.getFloatInput("Enter the third number: ", "Invalid input. Please enter a valid number.")

print(f"Sum: {number1 + number2 + number3}\n"
      f"Product: {number1 * number2 * number3}\n"
      f"Average: {(number1 + number2 + number3) / 3}")