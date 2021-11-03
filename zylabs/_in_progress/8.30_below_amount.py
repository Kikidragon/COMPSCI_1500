# Define your get_user_values function here
def get_user_values(nums):
    num = nums[0]
    values = []
    while num != -1:
        num = int(input())
        num = int(num)
        values.append(num)
    values.pop()
    return values


# num_values = int(input())
# values = []
# while num_values > 0:
#     num = float(input())
#     values.append(num)
#     num_values = num_values - 1


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
    num = input()
    nums = [num]

    get_user_values(nums)
    print(get_user_values(nums))

    output_ints_less_than_or_equal_to_threshold(nums, threshold)

