import math
import inputHandler

def isPrime(value: int) -> bool:
    if value <= 1:
        return False
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True

intInput = inputHandler.getIntInput("Enter an integer: ", "Invalid input. Please enter a valid integer.")

if isPrime(intInput):
    print(f"{intInput} is a prime number.")
else:
    print(f"{intInput} is not a prime number.")