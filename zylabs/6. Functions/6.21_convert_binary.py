def integer_to_reverse_binary(integer_value):
    binary = []
    while integer_value > 0:
        y = integer_value % 2
        y = str(y)
        binary.append(y)
        integer_value = integer_value // 2
    z = ''.join(binary)
    return z


def reverse_string(input_string):
    x = input_string[::-1]
    return x
#cant do integer_to_reverse_binary(integer_value)[::-1]


if __name__ == '__main__':
    integer_value = int(input())
    # print(integer_to_reverse_binary(integer_value))
    input_string = integer_to_reverse_binary(integer_value)
    print(reverse_string(input_string))

# x = int(input())
# while x > 0:
#     print(x % 2, end="")
#     x = x // 2
# print()