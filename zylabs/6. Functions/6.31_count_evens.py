def count_evens(num1, num2, num3, num4):
    list1 = (num1, num2, num3, num4)
    count = 0
    for n in list1:
        if n % 2 == 0:
            count += 1
        else:
            continue
    return count


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    result = count_evens(num1, num2, num3, num4)
    print('Total evens:', result)