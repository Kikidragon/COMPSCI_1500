name = input()
f = open(str(name))
file = f.readlines()
for i in file:
    if "Available" in i:
        split = i.split('\t')
        print("{} ({}) -- {}".format(split[1], split[0], split[2]), end='\n')


