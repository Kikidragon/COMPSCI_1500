import math
r = int(input())
g = int(input())
b = int(input())

color = [r, g, b]
n = min(color)
r = r - n
g = g - n
b = b - n

print(r, g, b)