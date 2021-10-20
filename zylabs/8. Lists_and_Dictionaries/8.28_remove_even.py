def remove_evens(nums):
    no_even = []
    for i in nums:
        if i % 2 == 1:
            no_even.append(i)
        else:
            continue
    return no_even


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = remove_evens(nums)

    print(result)


