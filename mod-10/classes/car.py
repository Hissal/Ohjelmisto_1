class Car:
    def __init__(self, plate_id: str, top_speed: float):
        self.plate_id = plate_id
        self.top_speed = top_speed
        self.current_speed = 0.0
        self.distance_traveled = 0.0

    def accelerate(self, speed_increase_kmh: float):
        self.current_speed += speed_increase_kmh
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours: float):
        distance = self.current_speed * hours
        self.distance_traveled += distance