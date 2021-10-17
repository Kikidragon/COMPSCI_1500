user_string = input()
words = user_string.split()
# print(words)

for i in words:
    for c in i:
        # print(c)
        if c.isupper() == True:
            print(c, end='')
print()

# words = user_string.split()
# acr = []
# for c in words:
#     x = c.split()
#     for i in x:
#         if i.isupper() == True:
#             acr.append(i)
# print(acr)
# for i in acr:
#     print(i, end='')


# user_string = input()
# x = user_string.isdigit()
# if x == True:
#     print('yes')
# else:
#     print('no')