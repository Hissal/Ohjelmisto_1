knownNames: set[str] = set()

while True:
    nameInput = input("Name: ")

    if nameInput == "":
        break

    if nameInput in knownNames:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        knownNames.add(nameInput)

for name in knownNames:
    print(name)