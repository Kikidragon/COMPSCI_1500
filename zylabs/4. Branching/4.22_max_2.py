import math
a = int(input())
b = int(input())

ab = [a, b]

more = max(ab)


#if ab[1] == ab[0]:
#    print(b)
if more == ab[0]:
    print(a)
elif more == ab[1]:
    print(b)
