import inputHandler
from inputHandler import InputFlags
seasons = ("Kevät", "Kesä", "Syksy", "Talvi")

month = inputHandler.getIntInput("Enter month (1-12): ", max=12, flags=inputHandler.InputFlags.POSITIVE | inputHandler.InputFlags.NON_ZERO)

# 12, 1, 2 -> Talvi
# 3, 4, 5 -> Kevät
# 6, 7, 8 -> Kesä
# 9, 10, 11 -> Syksy

if month in (12, 1, 2):
    season = seasons[3]
elif month in (3, 4, 5):
    season = seasons[0]
elif month in (6, 7, 8):
    season = seasons[1]
else:
    season = seasons[2]

print(f"Season: {season}")