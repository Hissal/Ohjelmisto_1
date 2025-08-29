import math
import unitConverter
import inputHandler
from inputHandler import InputFlags
from typing import NamedTuple
class Pizza(NamedTuple):
    price: float
    diameter: float

def price_per_square_meter(area: float, price: float) -> float:
    return price / area

def circle_area(diameter: float) -> float:
    radius = diameter / 2.0
    return math.pi * math.pow(radius, 2)

pizzaCount = inputHandler.getIntInput("Enter the number of pizzas: ", flags=InputFlags.POSITIVE | InputFlags.NON_ZERO)
pizzaList: list[Pizza] = []

for i in range(pizzaCount):
    inputDiameter_cm = inputHandler.getFloatInput("Enter the diameter of the pizza in cm: ", flags=InputFlags.POSITIVE | InputFlags.NON_ZERO)
    inputPrice = inputHandler.getFloatInput("Enter the price of the pizza in euros: ", flags=InputFlags.POSITIVE | InputFlags.NON_ZERO)

    pizza = Pizza(price=inputPrice, diameter=inputDiameter_cm)
    pizzaList.append(pizza)

cheapestPizzaIndex = 0
cheapestPricePerSqm = float('inf')

for i in range(pizzaCount):
    pizza = pizzaList[i]
    diameter_m = unitConverter.cm_to_meter(pizza.diameter)
    pizzaArea_m = circle_area(diameter_m)
    pricePerSqm = price_per_square_meter(pizzaArea_m, pizza.price)

    if pricePerSqm < cheapestPricePerSqm:
        cheapestPricePerSqm = pricePerSqm
        cheapestPizzaIndex = i

    print(f"Pizza {i + 1}: [diameter: {pizza.diameter} cm, price: {pizza.price}€, price per sqm: {pricePerSqm:.2f}€/m²]")

cheapestPizza = pizzaList[cheapestPizzaIndex]
print(f"The cheapest pizza is Pizza {cheapestPizzaIndex + 1} with diameter: {cheapestPizza.diameter} cm and price: {cheapestPizza.price}€, costing {cheapestPricePerSqm:.2f}€/m².")