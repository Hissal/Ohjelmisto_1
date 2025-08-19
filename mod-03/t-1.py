import inputHandler

MIN_LENGTH_CM = 37
LARGE_LENGTH_CM = 70

lengthInput = inputHandler.getFloatInput("Kuinkas iso kuha tuli? (cm): ", "Laita numero bro.")

if lengthInput < MIN_LENGTH_CM:
    print("Aikas piäni, päästä vapaaks.")
    print(f"Tarvis olla vielä {MIN_LENGTH_CM - lengthInput:.2f} cm pidempi.")
elif lengthInput < LARGE_LENGTH_CM:
    print("Hyvä kuha, laita pannulle")
else:
    print("No huhhuh, iso kuha! Laita savustimeen!")