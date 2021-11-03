import math

num_values = input()
values = num_values.split()

maxx = 0
for i in values:
    i = float(i)
    if i > maxx:
        maxx = i
# print(maxx)

norm = []
for i in values:
    normal = float(i) / float(maxx)
    norm.append(normal)
#print(norm)

for i in norm:
    print('{:.2f}'.format(i), end=' ')
print()
