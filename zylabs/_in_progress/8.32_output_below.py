numint = input()
values = numint.split()
for i in values:
    i = int(i)
threshold = values.pop()
for value in values:
    if value <= threshold:
        print(value, end=',')
    else:
        continue
print(values)

