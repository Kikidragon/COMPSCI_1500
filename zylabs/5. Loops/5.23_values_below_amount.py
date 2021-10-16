numint = int(input())
values = []
while numint > 0:
    numint -= 1
    value = int(input())
    values.append(value)
threshold = int(input())
for value in values:
    if value <= threshold:
        print(value, end=',')
    else:
        continue
# print(values)

