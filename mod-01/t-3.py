def perimeter(length: float, height: float) -> float:
    return length * 2 + height * 2

def area(length: float, height: float) -> float:
    return length * height

def isfloat(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

inputLength_str = input("Input Length: ")

while not isfloat(inputLength_str):
    print("Invalid input. Please enter a valid number for length.")
    inputLength_str = input("Input Length: ")

inputHeight_str = input("Input Height: ")

while not isfloat(inputHeight_str):
    print("Invalid input. Please enter a valid number for height.")
    inputHeight_str = input("Input Height: ")

inputLength = float(inputLength_str)
inputHeight = float(inputHeight_str)

print(f"Length: {inputLength} \n"
      f"Height: {inputHeight} \n"
      f"Perimeter: {perimeter(inputLength, inputHeight)} \n"
      f"Area: {area(inputLength, inputHeight)}")
