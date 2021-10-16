def largest_number(num1, num2, num3):
    maxx = num1
    if num2 > maxx:
        maxx = num2
    # else:
    #     continue
    if num3 > maxx:
        maxx = num3
    # else:
    #     continue
    return maxx


def smallest_number(num1, num2, num3):
    minn = num1
    if num2 < minn:
        minn = num2
    # else:
    #     continue
    if num3 < minn:
        minn = num3
    # else:
    #     continue
    return minn


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    print("largest: {}".format(largest_number(num1, num2, num3)))
    print("smallest: {}".format(smallest_number(num1, num2, num3)))