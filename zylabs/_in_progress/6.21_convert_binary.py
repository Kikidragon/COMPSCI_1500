def integer_to_reverse_binary(integer_value):
    binary = []
    while integer_value > 0:
        y = integer_value % 2
        binary.append(y)
        integer_value = integer_value // 2
    return binary


def reverse_string(input_string):
    x = reverse.binary
    return x


if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    integer_value = int(input())
    x = integer_to_reverse_binary(integer_value)
    print(integer_to_reverse_binary(integer_value))
    print(integer_to_reverse_binary(x))