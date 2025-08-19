import inputHandler

numList = []

while True:
    inputNumber = inputHandler.getFloatInputOrNone("Enter a number (or nothing to stop): ", "Invalid input. Please enter a valid number.")

    if inputNumber is None:
        break

    # noinspection PyTypeChecker
    numList.append(inputNumber)

if len(numList) == 0:
    print("No numbers were entered.")
    exit()

print(f"You entered the following numbers: {numList}")
print(f"of which the largest is: {max(numList)}")
print(f"and the smallest is: {min(numList)}")