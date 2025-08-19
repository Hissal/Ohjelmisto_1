num = 0

divisibleByThree = []

while num <= 1000:
    if num % 3 == 0:
        divisibleByThree.append(num)

    num += 1

print(divisibleByThree)