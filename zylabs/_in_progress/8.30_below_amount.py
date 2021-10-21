# Define your get_user_values function here
def get_user_values(values):
    num = 1
    while num > 0:
        num = input()
        num = int(num)
        values.append(num)
    values.pop()
    return values


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