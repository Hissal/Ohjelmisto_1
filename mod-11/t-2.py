from classes.car import *

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gasoline_car.accelerate(100)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric Car - Distance traveled: {electric_car.distance_traveled} km, Battery level: {electric_car.current_battery_kwh:.1f} kWh")
print(f"Gasoline Car - Distance traveled: {gasoline_car.distance_traveled} km, Fuel level: {gasoline_car.current_fuel_liters:.1f} liters")