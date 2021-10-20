def calc_average(nums):
    summ = 0
    for i in nums:
        summ += i
    avg = summ / len(nums)
    return avg


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))  # calc_average() should return 3.0