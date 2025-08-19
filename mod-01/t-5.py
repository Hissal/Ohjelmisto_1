import inputHandler
from typing import Tuple

def luotiToGrams(luoti: float) -> float:
    return luoti * 13.3

def naulaToGrams(naula: float) -> float:
    return luotiToGrams(naula * 32)

def leviskaToGrams(leviska: float) -> float:
    return naulaToGrams(leviska * 20)

def calculateTotalWeight(leviska: float, naula: float, luoti: float) -> Tuple[int, float]:
    totalGrams = leviskaToGrams(leviska) + naulaToGrams(naula) + luotiToGrams(luoti)
    totalKilograms = totalGrams // 1000
    remainingGrams = totalGrams % 1000
    return (int(totalKilograms), remainingGrams)

inputLeviska = inputHandler.getFloatInput("Leviskät: ", "Invalid input. Please enter a valid number.")
inputNaula = inputHandler.getFloatInput("Naulat: ", "Invalid input. Please enter a valid number.")
inputLuoti = inputHandler.getFloatInput("Luodit: ", "Invalid input. Please enter a valid number.")

totalWeight = calculateTotalWeight(inputLeviska, inputNaula, inputLuoti)

print(f"Total weight: {totalWeight[0]} kg and {totalWeight[1]:.2f} g")
print(f"Total weight in grams: {sum([leviskaToGrams(inputLeviska), naulaToGrams(inputNaula), luotiToGrams(inputLuoti)]):.2f} g")