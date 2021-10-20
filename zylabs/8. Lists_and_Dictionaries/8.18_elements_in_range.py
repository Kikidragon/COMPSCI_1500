num = input()
nums = num.split()

bound = input()
bounds = bound.split()
lower = int(bounds[0])
upper = int(bounds[1])

in_bounds = []
for i in nums:
    i = int(i)
    if i >= lower and i <= upper:
        in_bounds.append(i)
    else:
        continue

for i in in_bounds:
    print(i, end=' ')

# num = input()
# nums = num.split()
# count = []
# for i in nums:
#     i = int(i)
#     if i >= 0:
#         count.append(i)

# nums2 = sorted(count)
# for i in nums2:
#     print(i, end=' ')