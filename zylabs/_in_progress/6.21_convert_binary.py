def integer_to_reverse_binary(integer_value):
    binary = []
    while integer_value > 0:
        y = integer_value % 2
        y = str(y)
        binary.append(y)
        integer_value = integer_value // 2
    binar = ''.join(binary)
    return binar


def reverse_string(input_string):
    x = integer_to_reverse_binary(integer_value)[::-1]
    return x


if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    integer_value = int(input())
    x = integer_to_reverse_binary(integer_value)
    # print(integer_to_reverse_binary(integer_value))
    print(reverse_string(integer_to_reverse_binary(integer_value)))

# x = int(input())
# while x > 0:
#     print(x % 2, end="")
#     x = x // 2
# print()