import random
from car import Car


def print_cars_table(cars: list[Car]) -> None:
    w_place, w_plate, w_top, w_cur, w_dist = 5, 10, 10, 10, 12
    header = (
        f"{'| Place':>{w_place}} | {'Plate':<{w_plate}} | "
        f"{'Top km/h':>{w_top}} | {'Cur km/h':>{w_cur}} | {'Distance km':>{w_dist}} |"
    )
    sep = f"| {'-'*w_place}-+-{'-'*w_plate}-+-{'-'*w_top}-+-{'-'*w_cur}-+-{'-'*w_dist} |"

    print(header)
    print(sep)
    for i, car in enumerate(cars, 1):
        print(
            f"| {i:>{w_place}} | {car.plate_id:<{w_plate}} | "
            f"{car.top_speed:>{w_top}.2f} | {car.current_speed:>{w_cur}.2f} | {car.distance_traveled:>{w_dist}.2f} |"
        )


cars: list[Car] = []
for i in range(10):
    top_speed: float = random.uniform(100, 200)
    car = Car(f"ABC-{i}", top_speed)
    cars.append(car)

longest_distance: float = 0.0
while longest_distance < 10000:
    for car in cars:
        speed_increase: float = random.uniform(-10, 15)
        car.accelerate(speed_increase)
        car.drive(1)
        if car.distance_traveled > longest_distance:
            longest_distance = car.distance_traveled

ordered_cars = sorted(cars, key=lambda c: c.distance_traveled, reverse=True)
print_cars_table(ordered_cars)