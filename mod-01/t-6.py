import random
def getRandonNumberChain(length: int, min: int, max: int) -> list[int]:
    arr = []
    for _ in range(length):
        arr.append(random.randint(min, max))
    return arr

def numListAsInt(list) -> int:
    return int(''.join(map(str, list)))

code1 = getRandonNumberChain(3, 0, 9)
code2 = getRandonNumberChain(4, 1, 6)

print(f"Code 1: {numListAsInt(code1)} {code1}")
print(f"Code 2: {numListAsInt(code2)} {code2}")
