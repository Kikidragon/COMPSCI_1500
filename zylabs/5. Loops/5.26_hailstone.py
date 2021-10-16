num = int(input())
nums = [num]
while num > 1:
    if num % 2 == 0:
        num = num / 2
        nums.append(num)
    else:
        num = (num * 3) + 1
        nums.append(num)
# print(nums)
# print('{:.0f}'.format(num), end='\t')
y = 0
nums.pop()
for i in nums:
    y += 1
    print('{:.0f}'.format(i), end='\t' if y < 10 else '\t')
    if y == 10:
        print()
        y = 0

print(1)
# print(num, end=(" " if counter < 10 else "\n"))
# for i in nums:
#     print('{:.0f}'.format(i), end='\t')
#     j = i - 1
#     if (j % 10 == 0):
#         print('\n')
#     else:
#         continue
