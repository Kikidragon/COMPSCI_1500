def print_num_pattern(num1: int, num2: int):
    print(num1, end=' ')
    if num1 <= 0:
        return
    else:
        print_num_pattern(num1-num2, num2)
        print(num1, end=' ')
# done in class


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)