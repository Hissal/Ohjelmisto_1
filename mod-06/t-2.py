import inputHandler
import random
def throw_dice(sides: int) -> int:
    return random.randint(1, sides)

sideCount = inputHandler.getIntInput("Enter the number of sides for the dice: ", "Invalid input. Please enter a valid integer.")

result = throw_dice(sideCount)
print(result)

while result != sideCount:
    result = throw_dice(sideCount)
    print(result)