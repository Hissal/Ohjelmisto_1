from car import Car

car = Car("ABC-123", 142)
car.accelerate(50)
car.drive(2)
print(f"Distance traveled: {car.distance_traveled} km")  # Output: Distance traveled: 100.0 km
car.accelerate(100)
car.drive(1)
print(f"Distance traveled: {car.distance_traveled} km")  # Output: Distance traveled: 242.0 km
car.accelerate(-200)
car.drive(1)
print(f"Distance traveled: {car.distance_traveled} km")  # Output: Distance traveled: 242.0 km