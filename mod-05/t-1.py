import random

import inputHandler

diceCount = inputHandler.getIntInput("How many dice do you want to roll? ", "Please input a valid whole number.")

rolls = []

for i in range(diceCount):
    roll = random.randint(1, 6)
    rolls.append(roll)

print(rolls)