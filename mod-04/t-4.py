import inputHandler
import random

correctNum = random.randint(1, 10)
totalGuesses = 0

while True:
    inputGuess = inputHandler.getIntInput("Guess a number between 1 and 10: ", "Invalid input. Please enter a valid number.")
    totalGuesses += 1

    if inputGuess < 1 or inputGuess > 10:
        print("Your guess is out of range. Please try again.")
        continue

    if inputGuess == correctNum:
        print(f"Congratulations! You guessed the correct number in {totalGuesses} tries.")
        break
    elif inputGuess < correctNum:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")