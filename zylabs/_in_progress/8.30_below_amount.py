# FIXME UNFINISHED
def get_user_values(values):
    num = int(input())
    values = []
    while num != -1:
        num = int(input())
        num = int(num)
        values.append(num)
        if num == -1:
            break
    values.pop()
    return values

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


# Define your output_ints_less_than_or_equal_to_threshold function here
def output_ints_less_than_or_equal_to_threshold(nums, threshold):
    x = threshold
    y = []
    for i in nums:
        if i > x:
            y.append(x)
    return y


if __name__ == '__main__':
    threshold = int(input())
    nums = []

    get_user_values(nums)
    print(get_user_values(nums))

    output_ints_less_than_or_equal_to_threshold(nums, threshold)
