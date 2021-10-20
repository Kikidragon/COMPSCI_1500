import math
a = input()
b = input()

ab = [len(a), len(b)]

more = max(ab)


if ab[1] == ab[0]:
    print(b)
elif more == ab[0]:
    print(a)
elif more == ab[1]:
    print(b)

