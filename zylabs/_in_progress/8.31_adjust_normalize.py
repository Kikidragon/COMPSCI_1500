import math

num_values = input()
values = num_values.split()

for i in values:
    i = float(i)

print(values)
x = max(values)
print(x)
norm = []
for i in values:
    normal = float(i) / float(x)
    norm.append(normal)
# print(norm)

for i in norm:
    print('{:.2f}'.format(i), end=' ')