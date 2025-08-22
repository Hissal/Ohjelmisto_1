from itertools import count

import inputHandler

values = []

while True:
    floatInputOrNone = inputHandler.getFloatInputOrNone("Enter an integer (or press Enter to skip): ", "Invalid input. Please enter a valid integer.")
    if floatInputOrNone is None:
        break

    values.append(floatInputOrNone)

values.sort(reverse=True)

iterationCount = 5 if len(values) > 5 else len(values)
for i in range(iterationCount):
    print(values[i])