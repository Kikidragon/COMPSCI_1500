# name = input()
# f = open(str(name))
# file = f.readlines()
# dict = {}
# list1 = []
# for i in range(len(file)):
#     file1 = file[i].strip('\n')
#     if i+1<len(file) and i%2==0:
#         if int(file1) in dict:
#             dict[int(file1)].append(file[i+1].strip('\n'))
#         else:
#             list1.append(file[i+1].strip('\n'))
#             dict[int(file1)] = list1
# sorted1 = sorted(dict.items())
# for key in sorted(dict):
#     print('{}: {}'.format(key, '; '.join(dict.get(key))))

filename = input()

f = open(filename, 'r')
data = f.readlines()
f.close()

dictionary = {}
list_of_values = []

for i in range(len(data)):
    data[i] = data[i].strip()

for i in range(0, len(data), 2):
    list_of_values.append(data[i + 1])
    if data[i] in dictionary:
        dictionary[data[i]] = dictionary[data[i]] + '; ' + data[i + 1]
    else:
        dictionary[data[i]] = data[i + 1]

f = open('output_keys.txt', 'w')

for item in sorted(dictionary.items()):
    f.write(str(int(item[0])) + ': ' + item[1] + '\n')

f.close()

f = open('output_titles.txt', 'w')

list_of_values.sort()

for each in list_of_values:
    f.write(each + '\n')

f.close()

# print("{}: ".format(key), end='')
    # for i in dict[key]:
    #     print(i)
# for i in sorted1:
#     for j in i:
#         if j == int:
#             print("{}: ".format(j),end='')
#         else:
#             print('{}'.format(j))
# f.close()
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