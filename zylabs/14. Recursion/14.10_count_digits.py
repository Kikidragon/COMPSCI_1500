# not done teh right way
def digit_count(num):
    # if num > 10:
    #     return 1
    # num = str(num)
    # return len(num)

    if num < 10:
        return 1
    else:
        new_num = num // 10
        return 1 + digit_count(new_num)
# now its done the right way from class


if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)
    