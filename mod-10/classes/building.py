from elevator import Elevator

class Building:
    def __init__(self, min_floor: int, max_floor: int, elevator_count: int):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = [Elevator(min_floor, max_floor) for _ in range(elevator_count)]

    def move_elevator(self, elevator_number: int, target_floor: int):
        if 0 <= elevator_number < len(self.elevators):
            self.elevators[elevator_number].move_to_floor(target_floor)
        else:
            raise ValueError(f"Elevator number {elevator_number} is out of range.")

    def raise_firealarm(self):
        for elevator in self.elevators:
            elevator.move_to_floor(self.min_floor)