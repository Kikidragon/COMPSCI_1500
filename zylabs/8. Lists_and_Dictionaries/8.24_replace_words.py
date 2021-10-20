replacement = input()
line = input()

# replace pair : word to replace, word replacing that word

replacement_pair = replacement.split('  ')
rep = []
for i in replacement_pair:
    i = i.strip()
    a = i.split()
    rep.append(a)
# print(rep)

for i in rep:
    # print(i)
    line = line.replace(i[0], i[1])
    # for (j, string) in enumerate(i):
    #     print(j)
    #     line = line.replace(i[j], i[j+1])

print(line)

# Index = variable.index(value)
# For index, num in enumerate(numbers):
# 	Print('{} in the list at index {}'.format(num, index))     (number and index as tuple)
