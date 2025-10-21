import random

from classes.race import Race
from classes.car import Car

cars: list[Car] = []
for i in range(10):
    top_speed: float = random.uniform(100, 200)
    car = Car(f"ABC-{i + 1}", top_speed)
    cars.append(car)

race = Race("Suuri romuralli", 8000.0, cars)

hours_passed: int = 0
while not race.is_finished():
    race.advance_hour()
    hours_passed += 1

    if hours_passed % 10 == 0:
        print(f"--- After {hours_passed} hours ---")
        race.print_standings()

print(f"--- Race finished in {hours_passed} hours! ---")
race.print_standings()