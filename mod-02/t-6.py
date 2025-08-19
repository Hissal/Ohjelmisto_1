import random

def random_number_chain(length: int, min: int, max: int) -> list[int]:
    arr = []
    for _ in range(length):
        arr.append(random.randint(min, max))
    return arr

def num_list_as_int(numList) -> int:
    return int(''.join(map(str, numList)))

code1 = random_number_chain(3, 0, 9)
code2 = random_number_chain(4, 1, 6)

print(f"Code 1: {num_list_as_int(code1)} {code1}")
print(f"Code 2: {num_list_as_int(code2)} {code2}")
