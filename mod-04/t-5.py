USERNAME = "python"
PASSWORD = "rules"

MAX_ATTEMPTS = 5

totalAttempts = 0

def userBlocked() -> bool:
    return totalAttempts >= MAX_ATTEMPTS

while not userBlocked():
    inputUsername = input("Syötä käyttäjätunnus: ")
    inputPassword = input("Syötä salasana: ")
    totalAttempts += 1

    if inputUsername == USERNAME and inputPassword == PASSWORD:
        print(f"Tervetuloa")
        break
    elif not userBlocked():
        yritysStr = "yritystä" if MAX_ATTEMPTS - totalAttempts > 1 else "yritys"
        print(f"Väärä käyttäjätunnus tai salasana. {MAX_ATTEMPTS - totalAttempts} {yritysStr} jäljellä.")
    else:
        print("Pääsy evätty")
        break
