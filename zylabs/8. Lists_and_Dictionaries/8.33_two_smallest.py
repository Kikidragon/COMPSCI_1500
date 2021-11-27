# FIXME UNFINISHED
numint = input()
values = numint.split(' ')
test = 100
for i in values:
    i = int(i)
    if i < test:
        test = i
values.remove(str(test))
test2 = 100
for i in values:
    i = int(i)
    if i < test2:
        test2 = i
# print(test)
# print(test2)
print("{} and {}".format(test, test2))

# min1 = 1000
# for i in values:
#     if int(i) < min1:
#         i = min1
# min2 = 1000
# for i in values:
#     if int(i) < min2:
#         i = min2
#
# print(values)
# print(min(values))
# print("{} and {}".format(min1, min2))

# nums = []
# x = 1
# while x != 0:
#     x += 1
#     num2 = int(input())
#     nums.append(num2)
#     if num2 <= 0:
#         nums.pop()
#         break
# #print(nums)
# print(min(nums), "and", max(nums))
