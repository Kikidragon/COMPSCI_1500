numint = input()
values = numint.split()
for i in values:
    i = int(i)
threshold = int(values.pop())
for value in values:
    value = int(value)
    if value <= threshold:
        print(value, end=',')
    else:
        continue
# print(threshold)
# print(values)
print()
