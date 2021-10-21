import math


def get_minimum_int(nums):
    x = max(nums)
    for i in nums:
        if i < x:
            x = i
    return x

    # Type your code here.


if __name__ == '__main__':
    num = int(input())
    values = []
    values.append(num)
    while num > 0:
        num = int(input())
        values.append(num)
    values.pop()
    # print(values)
    for i in values:
        i = i - get_minimum_int(values)
        print(i)
    # print(values)
    # for i in get_minimum_int(values):
    #     print('{:.2f}'.format(i))
    # Type your code here.




