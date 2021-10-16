def get_user_values():
    numint = int(input())
    my_list = []
    while numint > 0:
        numint -= 1
        value = int(input())
        my_list.append(value)
    return my_list


# def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
#     # threshold = my_list.pop()
#     for i in user_values():
#         if i >= upper_threshold:
#             print(i)
#         else:
#             continue

if __name__ == '__main__':
    user_values = get_user_values()
    upper_threshold = user_values.pop()
    print(upper_threshold)
    # print(output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold))

