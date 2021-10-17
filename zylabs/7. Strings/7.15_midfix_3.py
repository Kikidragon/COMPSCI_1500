s = input()
y = int(len(s)/2)
mid2 = s[y]
mid1 = s[y-1]
mid3 = s[y+1]

# x = len(s)/2
# y = x=1
# mid = s[y]


# def get_middle_char(string):
#     if len(string) % 2 == 0:
#         return None
#     elif len(string) <= 1:
#         return None

#     str_len = int(len(string)/2))

#     return string[strlen]


# middle_index = len(s)/2
# first_half, middle, second_half = s[:middle_index], s[middle_index], s[middle_index+1:]
# first_half, middle, second_half

#   variable = len(odd_string)/2
#     middle_character = odd_string[variable +1]
#     return middle_character

# # x = len(string)
# y = str((x/2))
# mid = string.find(y)

# string = string[3:-3]
# print(string)
print("Midfix: {}{}{}".format(mid1, mid2, mid3))

# def middle(x, y, z):
#     if x > y and x < z:
#         return x
#     if y > x and y < z:
#         return y
#     return z

# def get_middle_character(odd_string):
#     variable = len(odd_string)
#     x = str((variable/2))
#     middle_character = odd_string.find(x)
#     middle_character2 = odd_string[middle_character]
#     return middle_character2