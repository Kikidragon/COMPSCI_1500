low = int(input())
high = int(input())
x = int(input())
y = 1
for i in range(low, high):
    if i % x == 0:
        y += 1
    # elif high % x == 0:
    #     y += 1
    elif x > high:
        y = 0
    else:
        continue
print(y)
