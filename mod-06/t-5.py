import inputHandler

def erase_uneven(numbers: list[int]) -> list[int]:
    evenNumbers: list[int] = []

    for number in numbers:
        if number % 2 == 0:
            evenNumbers.append(number)

    return evenNumbers

numberList: list[int] = []

while True:
    numbrInput = inputHandler.getIntInputOrNone("Enter an integer (or press Enter to finish): ", "Invalid input. Please enter a valid integer or press Enter to finish.")

    if numbrInput is None:
        break

    numberList.append(numbrInput)

evenNumbers = erase_uneven(numberList)
print(f"Original numbers: {numberList}")
print(f"Even numbers: {evenNumbers}")