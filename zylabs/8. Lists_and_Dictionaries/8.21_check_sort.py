def in_order(nums):
    a = [nums[i - 1] <= nums[i] for i in range(1, len(nums))]
    return all(x == a[0] for x in a)


#     counter = False
#     for x, i in enumerate(nums):
#         if x[i] < x[i+1]:
#             counter = True
#     return counter
# if nums[0] < nums[1] and nums[1] < nums [2] and nums[2] < nums[3] and nums[3] < nums[4]:
#     return True
# else:
#     return False

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')

    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')