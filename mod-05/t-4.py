import inputHandler

cityNames = []

for i in range(5):
    cityName = input(f"Enter the name of city {i + 1}: ")
    cityNames.append(cityName)


for cityName in cityNames:
    print(cityName)