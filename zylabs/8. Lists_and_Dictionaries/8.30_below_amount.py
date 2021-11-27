def get_user_values(values):
    value = int(input())
    values.append(value)
    while value != -1:
        if value == -1:
            break
        else:
            value = int(input())
            values.append(value)
    values.pop()
    return values
    #
    # user_string = 0
    # enter = []
    # while user_string != '-1':
    #     user_string = input()
    #     enter.append(user_string)
    #     if user_string == '-1':
    #         enter.pop()
    #

    # num = int(input())
    # values = []
    # while num != -1:
    #     num = int(input())
    #     num = int(num)
    #     values.append(num)
    #     if num == -1:
    #         break
    # values.pop()
    # return values


def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for i in user_values:
        if i <= upper_threshold:
            print(i)
        else:
            continue
#
# if __name__ == '__main__':
#     user_values, upper_threshold = get_user_values()
#     output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
#     # print(upper_threshold)


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
#


# # Define your output_ints_less_than_or_equal_to_threshold function here
# def output_ints_less_than_or_equal_to_threshold(nums, threshold):
#     x = threshold
#     y = []
#     for i in nums:
#         if i > x:
#             y.append(x)
#     return y
#

if __name__ == '__main__':
    threshold = int(input())
    nums = []

    get_user_values(nums)
    # print(get_user_values(nums))

    output_ints_less_than_or_equal_to_threshold(nums, threshold)
