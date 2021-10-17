num = input()
nums = num.split()
count = []
for i in nums:
    i = int(i)
    if i >= 0:
        count.append(i)

nums2 = sorted(count)
for i in nums2:
    print(i, end=' ')