# not done teh right way
def digit_count(num):
    if num > 10:
        return 1
    num = str(num)
    return len(num)


if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)
    