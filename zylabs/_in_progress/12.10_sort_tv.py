#FIXME UNFINISHED
name = input()
f = open(str(name))
file = f.readlines()
dict = {}
for i in range(len(file)):
    list1 = []
    file1 = file[i].strip('\n')
    if i+1<len(file) and i%2==0:
        if int(file1) in dict:
            dict[int(file1)].append(file[i+1].strip('\n'))
        else:
            list1.append(file[i+1].strip('\n'))
            dict[int(file1)] = list1
sorted1 = sorted(dict.items())
for key in sorted(dict):
    print('{}: {}'.format(key, '; '.join(dict.get(key))))
    # print("{}: ".format(key), end='')
    # for i in dict[key]:
    #     print(i)
# for i in sorted1:
#     for j in i:
#         if j == int:
#             print("{}: ".format(j),end='')
#         else:
#             print('{}'.format(j))
f.close()
# print(dict)
# print(sorted)

# with open(name, 'r') as myfile:
#     for i in myfile

        #
        # f = open(text)
        # file = f.readlines()
        # for word in file:
        #     word = word.strip()
        #     if start <= word <= end:
        #         print(word)
        # f.close()

        # print(key + ': ' + str(your_dictionary[key]))