full = input()

x = full.split()

first = x[0]
last = x[1]
year = x[2]


a = last[:5]
b = first[:1]
c = year[-2:]

print("Your login name: {}{}{}".format(a, b, c))


# word = input()
# pre = word[-3:]
# print("Postfix: {}".format(pre))

# word = input()
# pre = word[:3]
# print("Prefix: {}".format(pre))


# s = input()
# y = int(len(s)/2)
# mid2 = s[y]
# mid1 = s[y-1]
# mid3 = s[y+1]