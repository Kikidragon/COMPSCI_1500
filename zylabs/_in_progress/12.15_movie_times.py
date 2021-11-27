# FIXME UNFINISHED
import csv
name = input()
f = open(str(name))
file = f.readlines()
# file: time, title, rating
# print: title | rating | time
for i in file:
    split = i.split(',')
    title = split[1]
    rating = split[2]
    time = []
    if title in i:
        time.append(split[0])
print(title, rating)
for i in time:
    print(i)
#print('{title: ' '<44} | {rating:' '>5} | {}'.format(title = title, rating = rating, time))



# for i in file:
#     if "Available" in i:
#         split = i.split('\t')
#         print("{} ({}) -- {}".format(split[1], split[0], split[2]), end='\n')
#
#


# print('{title:' '>33}'.format(title=title))
# print('{col1:' '<19} | {col2:' '>22}'.format(col1=header1, col2=header2))
# print("--------------------------------------------")
# for pair in data_list:
#     for key, val in pair.items():
#         print('{col1:' '<19} | {col2:' '>22}'.format(col1=key, col2=val))
