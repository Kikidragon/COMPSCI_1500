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
            # series.append(n1)
            i += 1
        return n1
        #     num = series[i-1] + series[i-2]
        #     series.append(num)
        # return sum(series)

    # Type your code here.
    # f(0) = 0
    # f(1) = 1
    # f(n) = f(n-1) + f(n-2)


if __name__ == '__main__':
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))