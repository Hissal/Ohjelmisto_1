import random
from classes.car import Car

class Race:
    def __init__(self, name: str, distance_km: float, cars: list[Car]):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def advance_hour(self):
        for car in self.cars:
            speed_increase: float = random.uniform(-10, 15)
            car.accelerate(speed_increase)
            car.drive(1)

    def print_standings(self):
        standings = sorted(self.cars, key=lambda car: car.distance_traveled, reverse=True)
        w_place, w_plate, w_top, w_cur, w_dist = 5, 10, 10, 10, 12
        header = (
            f"{'| Place':>{w_place}} | {'Plate':<{w_plate}} | "
            f"{'Top km/h':>{w_top}} | {'Cur km/h':>{w_cur}} | {'Distance km':>{w_dist}} |"
        )
        sep = f"| {'-' * w_place}-+-{'-' * w_plate}-+-{'-' * w_top}-+-{'-' * w_cur}-+-{'-' * w_dist} |"

        print(header)
        print(sep)
        for i, car in enumerate(standings, 1):
            print(
                f"| {i:>{w_place}} | {car.plate_id:<{w_plate}} | "
                f"{car.top_speed:>{w_top}.2f} | {car.current_speed:>{w_cur}.2f} | {car.distance_traveled:>{w_dist}.2f} |"
            )

    def is_finished(self) -> bool:
        for car in self.cars:
            if car.distance_traveled >= self.distance_km:
                return True
        return False