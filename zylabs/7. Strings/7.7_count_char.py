the_word = input()
x = the_word.split()
check = x.pop(0)
count = 0
for y in x:
    for c in y:
        if c == check:
            count += 1
        else:
            continue
print(count)