# fix if time Write recursive fibonacci() function
def fibonacci(n):
    series = [0, 1]
    n1 = 0
    n2 = 1
    x = 1
    if n < 0:
        return -1
    else:
        for i in range(n):
            num = n1 + n2
            n1 = n2
            n2 = num
            i += 1
        return n1


if __name__ == "__main__":
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))
