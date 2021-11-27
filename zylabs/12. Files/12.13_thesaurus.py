synonyms = []   # Define dictionary
name1 = input()
name = name1+'.txt'
letter = input()
f = open(str(name))
file = f.readlines()
for i in file:
    i = i.strip('\n')
    if letter in i[:1]:
        i = i.split()
        synonyms.append(i)
        for j in i:
            print(j)
if len(synonyms) == 0:
    print("No synonyms for {} begin with {}.".format(name1, letter))
