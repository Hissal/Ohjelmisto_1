import inputHandler
import random
import math

N = inputHandler.getIntInput("Enter the amount of points: ", "Invalid input. Please enter a valid number.")

points = []
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    points.append((x, y))

pointsInCircle = 0

for point in points:
    x, y = point
    if math.pow(x, 2) + math.pow(y, 2) < 1:
        pointsInCircle += 1

print(f"Total points: {N}")
print(f"Points within unit circle: {pointsInCircle}")
print(f"Ratio: {pointsInCircle / N:.2f}")
print(f"Estimated value of pi: {4 * pointsInCircle / N}")