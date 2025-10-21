from car import Car

car = Car("ABC-123", 142.0)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current Speed: {car.current_speed} km/h")
car.accelerate(-200)
print(f"Current Speed after braking: {car.current_speed} km/h")