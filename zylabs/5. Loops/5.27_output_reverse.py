values = []
def Reverse(values):
    values.reverse()
    return values
value = input()
values.append(value)
a = 1
while a == 1:
    if value == '*':
        break
    value = input()
    values.append(value)
values.pop()
#print(values)
valuesr = Reverse(values)
for i in valuesr:
    print(i, end=',')
print()