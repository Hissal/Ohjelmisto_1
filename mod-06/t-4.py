import inputHandler

def sum_of(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

numberList: list[int] = []

while True:
    numbrInput = inputHandler.getIntInputOrNone("Enter an integer (or press Enter to finish): ", "Invalid input. Please enter a valid integer or press Enter to finish.")

    if numbrInput is None:
        break

    numberList.append(numbrInput)

sum = sum_of(numberList)
print(f"The sum of the entered integers is: {sum}")