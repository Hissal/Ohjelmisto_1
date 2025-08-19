import inputHandler

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

yearInput = inputHandler.getIntInput("Enter a year: ", "Invalid input. Please enter a valid year.")
if is_leap_year(yearInput):
    print(f"{yearInput} is a leap year.")
else:
    print(f"{yearInput} is not a leap year.")