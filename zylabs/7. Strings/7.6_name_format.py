name = input()
names = name.split()
last = names.pop()

if len(names) == 1:
    for i in names:
        x = len(i) - 1
        c = i[:-x]
    print("{}, {}.".format(last, c))

else:
    e = []
    for i in names:
        x = len(i) - 1
        c = i[:-x]
        e.append(c)
    e1 = e[0]
    e2 = e[1]
    print("{}, {}.{}.".format(last, e1, e2))

