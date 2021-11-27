import csv


name = input()
with open(name, 'r') as myfile:
    Reader = csv.reader(myfile, delimiter=',')
    dictionary = dict()
    for l in Reader:
        for m in l:
            if m in dictionary:
                dictionary[m] = dictionary[m] + 1
            else:
                dictionary[m] = 1
    for n in list(dictionary.keys()):
        print("{} {}".format(n, dictionary[n]))

# f = open(text)
# file = f.readlines()
# for word in file:
#     word = word.split(',')
#     print(word)
# f.close()


# text = input()
# with open(text, 'r') as file:
#     words = csv.reader(file)
#     for i in words:
#         list1 = set(i)
#         for j in i:
#             count = i.count(j)
#             print(j, count)

# f = open(text)
# file = f.readlines()
# for word in file:
#     word = word.split(',')
#     print(word)
# f.close()




#https://stackoverflow.com/questions/64235261/how-to-find-the-frequency-of-words-in-a-list-created-from-a-csv-file