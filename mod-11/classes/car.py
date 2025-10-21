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


class ElectricCar(Car):
    def __init__(self, plate_id: str, top_speed: float, battery_capacity_kwh: float):
        super().__init__(plate_id, top_speed)
        self.battery_capacity_kwh = battery_capacity_kwh
        self.current_battery_kwh = battery_capacity_kwh

    def accelerate(self, speed_increase_kmh: float):
        if self.current_battery_kwh <= 0:
            self.current_speed = 0
            return
        super().accelerate(speed_increase_kmh)

    def drive(self, hours: float):
        if self.current_battery_kwh <= 0:
            self.current_speed = 0
            return
        distance = self.current_speed * hours
        energy_consumed = distance * 0.1  # 0.1 kwh per km
        if energy_consumed > self.current_battery_kwh:
            distance = self.current_battery_kwh / 0.1
            self.current_speed = 0
            self.current_battery_kwh = 0
        else:
            self.current_battery_kwh -= energy_consumed
        self.distance_traveled += distance


class GasolineCar(Car):
    def __init__(self, plate_id: str, top_speed: float, fuel_tank_capacity_liters: float):
        super().__init__(plate_id, top_speed)
        self.fuel_tank_capacity_liters = fuel_tank_capacity_liters
        self.current_fuel_liters = fuel_tank_capacity_liters

    def accelerate(self, speed_increase_kmh: float):
        if self.current_fuel_liters <= 0:
            self.current_speed = 0
            return
        super().accelerate(speed_increase_kmh)

    def drive(self, hours: float):
        if self.current_fuel_liters <= 0:
            self.current_speed = 0
            return
        distance = self.current_speed * hours
        fuel_consumed = distance * 0.05  # 0.05 liters per km
        if fuel_consumed > self.current_fuel_liters:
            distance = self.current_fuel_liters / 0.05
            self.current_speed = 0
            self.current_fuel_liters = 0
        else:
            self.current_fuel_liters -= fuel_consumed
        self.distance_traveled += distance