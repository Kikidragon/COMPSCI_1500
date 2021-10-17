num = input()
nums = num.split()
count = 0
for i in nums:
    i = int(i)
    count += i
avg = count/len(nums)
print('{:.0f}'.format(avg), end=' ')
maxx = 0
for i in nums:
    i = int(i)
    if i > maxx:
        maxx = i
print(maxx)