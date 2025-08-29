import random
def throw_dice() -> int:
    return random.randint(1, 6)

result = throw_dice()
print(result)

while result != 6:
    result = throw_dice()
    print(result)