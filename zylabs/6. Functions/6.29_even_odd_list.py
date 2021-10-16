def is_list_even(my_list):
    for i in my_list:
        if i % 2 == 0:
            x = True
            continue
        else:
            x = False
            break
    return x


def is_list_odd(my_list):
    for i in my_list:
        if i % 2 == 1:
            x = True
            continue
        else:
            x = False
            break
    return x


if __name__ == '__main__':
    numint = int(input())
    my_list = []
    while numint > 0:
        numint -= 1
        value = int(input())
        my_list.append(value)

    if is_list_even(my_list) == True:
        print('all even')
    elif is_list_odd(my_list) == True:
        print('all odd')
    else:
        print('not even or odd')

# numint = int(input())
# values = []
# while numint > 0:
#     numint -= 1
#     value = int(input())
#     values.append(value)
# threshold = int(input())
# for value in values:
#     if value <= threshold:
#         print(value, end=',')
#     else:
#         continue
# # print(values)
