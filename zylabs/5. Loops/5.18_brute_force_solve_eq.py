''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())
#ax + by = c AND dx + ey = f
''' Type your code here. '''
g = 0
for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
            g = 1
            print("x =", x, ", y =", y)
if g == 0:
    print("There is no solution")