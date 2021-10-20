import math
a = int(input())
b = int(input())
c = int(input())

ab = [a, b, c]

more = max(ab)


if more == ab[0]:
    print(a)
elif more == ab[1]:
    print(b)
elif more == ab[2]:
    print(c)