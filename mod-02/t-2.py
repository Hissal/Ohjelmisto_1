import math

def circle_area(radius: float) -> float:
    return math.pi * math.pow(radius, 2)

inputRadius = input("Input Circle Radius: ")

print(f"Circle Area: {circle_area(float(inputRadius)):.2f}")
