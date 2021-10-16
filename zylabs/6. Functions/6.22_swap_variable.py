def swap_values(user_val1, user_val2):
    return user_val2, user_val1

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    y=swap_values(a, b)
    for i in y:
        if y.index(i) == 0:
            print(i, end=' ')
        else:
            print(i)