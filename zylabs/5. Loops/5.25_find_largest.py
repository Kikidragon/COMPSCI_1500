nums = []
x = 1
while x != 0:
    x += 1
    num2 = int(input())
    nums.append(num2)
    if num2 < 0:
        nums.pop()
        break
#print(nums)
print(max(nums))
