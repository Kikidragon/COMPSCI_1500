import math

num_values = int(input())
values = []
while num_values > 0:
    num = float(input())
    values.append(num)
    num_values = num_values - 1

norm = []
for i in values:
    normal = float(i) / max(values)
    norm.append(normal)
# print(norm)

for i in norm:
    print('{:.2f}'.format(i))