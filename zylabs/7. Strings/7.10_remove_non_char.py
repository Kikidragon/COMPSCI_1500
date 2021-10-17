words = input()
x = []
for c in words:
    if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
        x.append(c)
    else:
        continue

for i in x:
    print(i, end='')
print()